#!/usr/bin/env python3
"""Render simple paragraph, section, and table mappings into a DOCX template."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import zipfile
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"w": W, "r": R}
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

ET.register_namespace("w", W)
ET.register_namespace("r", R)


def q(name: str) -> str:
    prefix, local = name.split(":", 1)
    return f"{{{NS[prefix]}}}{local}"


def text(element: ET.Element) -> str:
    return "".join(node.text or "" for node in element.findall(".//w:t", NS)).strip()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def value_and_uncertainty(value: Any) -> tuple[str, bool]:
    if isinstance(value, dict):
        if "value" not in value:
            raise ValueError("value object must contain 'value'")
        return str(value["value"]), value.get("certainty", "confirmed") != "confirmed"
    if value is None:
        return "", False
    return str(value), False


def set_text(container: ET.Element, value: Any) -> None:
    raw, uncertain = value_and_uncertainty(value)
    if container.tag == q("w:tc"):
        paragraphs = container.findall("w:p", NS)
        if not paragraphs:
            paragraphs = [ET.SubElement(container, q("w:p"))]
        for extra in paragraphs[1:]:
            container.remove(extra)
        paragraph = paragraphs[0]
    elif container.tag == q("w:p"):
        paragraph = container
    else:
        raise ValueError(f"unsupported text container: {container.tag}")

    paragraph_properties = paragraph.find("w:pPr", NS)
    run_template = paragraph.find("w:r", NS)
    run_properties = run_template.find("w:rPr", NS) if run_template is not None else None
    for child in list(paragraph):
        if child is not paragraph_properties:
            paragraph.remove(child)
    run = ET.SubElement(paragraph, q("w:r"))
    if run_properties is not None:
        run.append(copy.deepcopy(run_properties))
    if uncertain:
        properties = run.find("w:rPr", NS)
        if properties is None:
            properties = ET.Element(q("w:rPr"))
            run.insert(0, properties)
        highlight = properties.find("w:highlight", NS)
        if highlight is None:
            highlight = ET.SubElement(properties, q("w:highlight"))
        highlight.set(q("w:val"), "yellow")
    for index, line in enumerate(raw.split("\n")):
        if index:
            ET.SubElement(run, q("w:br"))
        node = ET.SubElement(run, q("w:t"))
        node.text = line
        if line.startswith(" ") or line.endswith(" "):
            node.set(XML_SPACE, "preserve")


def select_candidate(candidates: list[ET.Element], operation: dict[str, Any], label: str) -> ET.Element:
    expected = int(operation.get("expected_matches", 1))
    if len(candidates) != expected:
        raise ValueError(f"{label}: expected {expected} matches, got {len(candidates)}")
    occurrence = operation.get("occurrence")
    if occurrence is None:
        if len(candidates) != 1:
            raise ValueError(f"{label}: ambiguous match; declare a one-based occurrence")
        return candidates[0]
    index = int(occurrence) - 1
    if index < 0 or index >= len(candidates):
        raise ValueError(f"{label}: occurrence is out of range")
    return candidates[index]


def select_top_level(body: ET.Element, anchor: str, occurrence: Any, label: str) -> ET.Element:
    matches = [item for item in body if item.tag == q("w:p") and text(item) == anchor]
    if occurrence is None:
        if len(matches) != 1:
            raise ValueError(f"{label} {anchor!r}: expected 1 match, got {len(matches)}")
        return matches[0]
    index = int(occurrence) - 1
    if index < 0 or index >= len(matches):
        raise ValueError(f"{label} {anchor!r}: occurrence is out of range")
    return matches[index]


def apply_replacements(root: ET.Element, operations: list[dict[str, Any]]) -> None:
    for operation in operations:
        anchor = str(operation["anchor"])
        matches = [item for item in root.findall(".//w:p", NS) if text(item) == anchor]
        paragraph = select_candidate(matches, operation, f"replacement anchor {anchor!r}")
        set_text(paragraph, operation.get("value", ""))


def apply_sections(body: ET.Element, operations: list[dict[str, Any]]) -> None:
    for operation in operations:
        start = select_top_level(body, str(operation["start_anchor"]), operation.get("start_occurrence"), "section start")
        end = select_top_level(body, str(operation["end_anchor"]), operation.get("end_occurrence"), "section end")
        prototype = select_top_level(body, str(operation["prototype_anchor"]), operation.get("prototype_occurrence"), "section prototype")
        children = list(body)
        start_index = children.index(start)
        end_index = children.index(end)
        if start_index >= end_index:
            raise ValueError("section start must occur before section end")
        generated = []
        for value in operation.get("paragraphs", []):
            paragraph = copy.deepcopy(prototype)
            set_text(paragraph, value)
            generated.append(paragraph)
        for child in children[start_index + 1:end_index]:
            body.remove(child)
        for offset, paragraph in enumerate(generated, 1):
            body.insert(start_index + offset, paragraph)


def remove_vertical_merge(cell: ET.Element) -> None:
    properties = cell.find("w:tcPr", NS)
    merge = properties.find("w:vMerge", NS) if properties is not None else None
    if merge is not None and properties is not None:
        properties.remove(merge)


def apply_tables(body: ET.Element, operations: list[dict[str, Any]]) -> None:
    for operation in operations:
        headers = [str(value) for value in operation["headers"]]
        candidates = []
        for table in body.findall("w:tbl", NS):
            first_row = table.find("w:tr", NS)
            actual = [text(cell) for cell in first_row.findall("w:tc", NS)] if first_row is not None else []
            if actual == headers:
                candidates.append(table)
        table = select_candidate(candidates, operation, f"table headers {headers!r}")
        rows = table.findall("w:tr", NS)
        header_rows = int(operation.get("header_rows", 1))
        footer_rows = int(operation.get("footer_rows", 0))
        prototype_index = int(operation.get("prototype_row", header_rows))
        if prototype_index < 0 or prototype_index >= len(rows):
            raise ValueError(f"table {headers!r}: prototype_row is out of range")
        if header_rows + footer_rows > len(rows):
            raise ValueError(f"table {headers!r}: preserved rows exceed table length")
        prototype = copy.deepcopy(rows[prototype_index])
        footer = rows[len(rows) - footer_rows:] if footer_rows else []
        data_end = len(rows) - footer_rows if footer_rows else len(rows)
        for row in rows[header_rows:data_end]:
            table.remove(row)
        insert_at = list(table).index(footer[0]) if footer else len(table)
        for values in operation.get("rows", []):
            if not isinstance(values, list):
                raise ValueError(f"table {headers!r}: every row must be an array")
            row = copy.deepcopy(prototype)
            cells = row.findall("w:tc", NS)
            if len(values) > len(cells):
                raise ValueError(f"table {headers!r}: input row has more values than prototype cells")
            for cell in cells:
                remove_vertical_merge(cell)
            for cell, value in zip(cells, values):
                set_text(cell, value)
            table.insert(insert_at, row)
            insert_at += 1


def validate_document(root: ET.Element, mapping: dict[str, Any]) -> dict[str, Any]:
    rules = mapping.get("validation", {})
    document_text = text(root)
    errors = []
    for value in rules.get("required_text", []):
        if str(value) not in document_text:
            errors.append(f"required text missing: {value}")
    for value in rules.get("forbidden_text", []):
        if str(value) in document_text:
            errors.append(f"forbidden text remains: {value}")
    body = root.find("w:body", NS)
    table_count = len(body.findall("w:tbl", NS)) if body is not None else 0
    expected_tables = rules.get("expected_tables")
    if expected_tables is not None and table_count != int(expected_tables):
        errors.append(f"expected {expected_tables} top-level tables, got {table_count}")
    return {
        "passed": not errors,
        "errors": errors,
        "top_level_tables": table_count,
        "uncertainty_highlights": len(root.findall(".//w:highlight", NS)),
    }


def read_parts(path: Path) -> tuple[list[zipfile.ZipInfo], dict[str, bytes]]:
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        parts = {info.filename: archive.read(info.filename) for info in infos if not info.is_dir()}
    return infos, parts


def render(template: Path, mapping_path: Path, output: Path) -> dict[str, Any]:
    if template.resolve() == output.resolve():
        raise ValueError("output must not overwrite the source template")
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    infos, parts = read_parts(template)
    if "word/document.xml" not in parts:
        raise ValueError("DOCX is missing word/document.xml")
    preserved_before = {name: digest(content) for name, content in parts.items() if name != "word/document.xml"}
    root = ET.fromstring(parts["word/document.xml"])
    body = root.find("w:body", NS)
    if body is None:
        raise ValueError("word/document.xml is missing w:body")

    apply_replacements(root, list(mapping.get("replacements", [])))
    apply_sections(body, list(mapping.get("sections", [])))
    apply_tables(body, list(mapping.get("tables", [])))
    validation = validate_document(root, mapping)
    if not validation["passed"]:
        raise ValueError("document validation failed: " + "; ".join(validation["errors"]))
    parts["word/document.xml"] = ET.tostring(root, encoding="utf-8", xml_declaration=True)

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w") as target:
        for info in infos:
            target.writestr(info, b"" if info.is_dir() else parts[info.filename])

    _, generated_parts = read_parts(output)
    ET.fromstring(generated_parts["word/document.xml"])
    preserved_after = {name: digest(content) for name, content in generated_parts.items() if name != "word/document.xml"}
    if preserved_before != preserved_after:
        raise ValueError("one or more preserved OOXML parts changed")
    return {
        "schema_version": "1.0",
        "passed": True,
        "template": str(template.resolve()),
        "output": str(output.resolve()),
        "template_sha256": digest(template.read_bytes()),
        "output_sha256": digest(output.read_bytes()),
        "preserved_parts_verified": len(preserved_before),
        **validation,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", required=True, type=Path)
    parser.add_argument("--mapping", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = render(args.template, args.mapping, args.output)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
