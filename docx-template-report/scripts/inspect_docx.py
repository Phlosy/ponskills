#!/usr/bin/env python3
"""Inspect stable anchors and structure in a DOCX OOXML package."""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from collections import Counter
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"w": W, "r": R}


def q(name: str) -> str:
    prefix, local = name.split(":", 1)
    return f"{{{NS[prefix]}}}{local}"


def text(element: ET.Element) -> str:
    return "".join(node.text or "" for node in element.findall(".//w:t", NS)).strip()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def inspect(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        parts = {info.filename: archive.read(info.filename) for info in infos if not info.is_dir()}
    if "word/document.xml" not in parts:
        raise ValueError("DOCX is missing word/document.xml")
    root = ET.fromstring(parts["word/document.xml"])
    body = root.find("w:body", NS)
    if body is None:
        raise ValueError("word/document.xml is missing w:body")

    paragraphs = []
    top_level_texts = []
    for index, paragraph in enumerate(body.findall("w:p", NS)):
        value = text(paragraph)
        top_level_texts.append(value)
        style = paragraph.find("w:pPr/w:pStyle", NS)
        paragraphs.append({
            "index": index,
            "text": value,
            "style": style.get(q("w:val")) if style is not None else None,
            "drawings": len(paragraph.findall(".//w:drawing", NS)),
        })

    tables = []
    for index, table in enumerate(body.findall("w:tbl", NS)):
        rows = table.findall("w:tr", NS)
        tables.append({
            "index": index,
            "rows": len(rows),
            "headers": [text(cell) for cell in rows[0].findall("w:tc", NS)] if rows else [],
            "text_preview": text(table)[:300],
        })

    fields = [(node.text or "").strip() for node in root.findall(".//w:instrText", NS)]
    immutable_names = {
        "word/styles.xml", "word/numbering.xml", "word/settings.xml",
        "word/fontTable.xml", "word/theme/theme1.xml",
    }
    return {
        "schema_version": "1.0",
        "template": str(path.resolve()),
        "template_sha256": digest(path.read_bytes()),
        "package_parts": sorted(parts),
        "immutable_parts": {name: digest(parts[name]) for name in sorted(immutable_names & parts.keys())},
        "paragraphs": paragraphs,
        "top_level_text_occurrences": dict(sorted(Counter(value for value in top_level_texts if value).items())),
        "tables": tables,
        "toc_present": any("TOC" in value for value in fields),
        "field_instructions": fields,
        "images": sorted(name for name in parts if name.startswith("word/media/")),
        "headers": sorted(name for name in parts if name.startswith("word/header")),
        "footers": sorted(name for name in parts if name.startswith("word/footer")),
        "sections": len(root.findall(".//w:sectPr", NS)),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("template", type=Path)
    parser.add_argument("--output", type=Path, help="Write JSON contract to this path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    value = inspect(args.template)
    rendered = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
