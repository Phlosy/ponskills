---
name: docx-template-report
description: Build or implement a deterministic DOCX report generator from an existing Word template by editing OOXML while preserving template styles and layout. Use when a user supplies or references a .docx template and asks to generate reports, fill declared sections or tables, repeat template blocks, insert evidence images, preserve formatting, update a table of contents, or create Python code for template-bound DOCX generation. Also use for Chinese requests such as “按 Word 模板生成报告”“指定模板和内容位置”“基于 DOCX 模板实现报告生成”.
---

# DOCX Template Report

Implement template-bound report generation by treating DOCX as an OOXML ZIP package. Preserve the template's styles and layout, make every content location explicit, and fail safely when the template no longer matches its declared contract.

## Require an input contract

Collect these inputs before modifying code or generating a deliverable:

1. Obtain the absolute template path and confirm that it exists.
2. Obtain the output path. Never overwrite the source template.
3. Obtain the content source: sample JSON, schema, database/API contract, or explicit values.
4. Obtain a location mapping for every generated field. Require an exact paragraph anchor, boundary anchors, table headers, or a named prototype block.
5. Obtain required variants such as outline, blank report, and completed report.
6. Obtain requirements for images, TOC, PDF rendering, missing values, and structural validation.

If an item is missing, ask the user for it and wait. If the user asks for help choosing locations, inspect the template, propose a mapping, and require confirmation for ambiguous or repeated anchors. Do not silently select the first fuzzy match.

Use the intake template and mapping schema in [references/input-contract.md](references/input-contract.md).

## Follow the workflow

### 1. Inspect the template

Run:

```bash
python scripts/inspect_docx.py /absolute/path/template.docx --output /tmp/template-contract.json
```

Review top-level paragraphs, exact text occurrence counts, table headers, TOC presence, images, sections, and immutable OOXML parts. Use exact text and structural properties to identify anchors.

### 2. Freeze the inputs

Copy the selected template and report data into an immutable run/work directory when reproducibility matters. Record their SHA-256 digests. Build one normalized JSON report model before touching Word XML; do not mix data collection with document mutation.

### 3. Define the mapping

Write a mapping file that declares each operation and its expected match count. Prefer, in order:

1. Explicit placeholder text unique in the document.
2. Exact start/end boundary paragraphs.
3. Exact table header signatures.
4. A prototype heading/table/block that can be deep-copied.

Reject missing or duplicate anchors unless the mapping explicitly supplies a one-based `occurrence`.

### 4. Implement the renderer

For paragraph replacement, bounded section replacement, and table row expansion, start from:

```bash
python scripts/render_docx.py \
  --template /absolute/path/template.docx \
  --mapping /absolute/path/mapping.json \
  --output /absolute/path/generated.docx
```

Read [references/mapping-schema.md](references/mapping-schema.md) before creating the mapping.

For repeated multi-element case blocks, images, relationships, multiple report variants, or cached TOC page numbers, read [references/ooxml-patterns.md](references/ooxml-patterns.md) and adapt a project-owned renderer. Keep those domain rules out of a generic core.

### 5. Preserve template structure

Edit only the necessary package parts. Preserve ZIP metadata where practical. Treat these as immutable unless the requirement explicitly says otherwise:

- `word/styles.xml`
- `word/numbering.xml`
- `word/settings.xml`
- `word/fontTable.xml`
- `word/theme/theme1.xml`
- headers, footers, section definitions, page size, and margins

Copy paragraph, run, row, table, and drawing prototypes with `copy.deepcopy()` so generated content inherits the supplied design.

### 6. Validate before delivery

Always verify:

- The output opens as a ZIP and every edited XML part parses.
- Required anchors were matched exactly as declared.
- Required text and expected table/block counts exist.
- Placeholders and forbidden text are absent.
- Immutable package-part hashes match the source template.
- Image relationships and content types resolve when images are inserted.
- The TOC field and generated bookmarks are internally consistent when a TOC is required.

If LibreOffice is installed, render a PDF with a temporary user profile and inspect the result:

```bash
libreoffice --headless \
  -env:UserInstallation=file:///tmp/docx-report-profile \
  --convert-to pdf --outdir /tmp/rendered /absolute/path/generated.docx
```

Treat structural validation as mandatory and visual rendering as an additional check.

## Deliver the implementation

Return:

- The renderer code and mapping/configuration.
- The generated DOCX path.
- The template and output SHA-256 values.
- A concise list of anchors and expected occurrences.
- Validation results and any unavailable optional checks.
- A warning about template elements that must not be renamed or removed.

Do not claim that a template is freely replaceable when the renderer depends on exact headings, table headers, prototype rows, drawing nodes, or TOC controls.
