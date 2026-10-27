# Mapping schema

The bundled `render_docx.py` supports deterministic paragraph, section, and table operations without third-party Python packages.

## Full example

```json
{
  "replacements": [
    {
      "anchor": "{{PROJECT_NAME}}",
      "value": "多域仿真系统",
      "expected_matches": 1
    },
    {
      "anchor": "{{CONTRACT}}",
      "value": {"value": "合同编号待确认", "certainty": "manual_required"},
      "expected_matches": 1
    }
  ],
  "sections": [
    {
      "start_anchor": "概述",
      "end_anchor": "编写依据",
      "prototype_anchor": "【正文段落原型】",
      "paragraphs": ["第一段正文。", "第二段正文。"]
    }
  ],
  "tables": [
    {
      "headers": ["序号", "设备名称", "技术规格"],
      "expected_matches": 1,
      "header_rows": 1,
      "prototype_row": 1,
      "footer_rows": 0,
      "rows": [
        ["1", "服务器", "32 核 / 128 GB"],
        ["2", "终端", "16 核 / 32 GB"]
      ]
    }
  ],
  "validation": {
    "required_text": ["多域仿真系统", "32 核 / 128 GB"],
    "forbidden_text": ["{{PROJECT_NAME}}", "【正文段落原型】"],
    "expected_tables": 1
  }
}
```

## Value objects

A paragraph or cell value can be a string, number, boolean, or an object:

```json
{"value": "待人工确认", "certainty": "manual_required"}
```

Any certainty other than `confirmed` receives a yellow Word highlight.

## Replacements

- `anchor`: Exact concatenated text of a paragraph.
- `value`: Replacement value.
- `expected_matches`: Required occurrence count; default `1`.
- `occurrence`: Optional one-based match to edit. Use only after confirming that repeated anchors are intentional.

Replacement preserves paragraph properties and the first run's run properties. It replaces all other runs in that paragraph.

## Sections

- `start_anchor` and `end_anchor`: Exact top-level body paragraph text.
- `prototype_anchor`: Exact top-level paragraph whose layout is cloned for inserted paragraphs.
- `paragraphs`: Values to insert between the boundaries.
- `start_occurrence`, `end_occurrence`, `prototype_occurrence`: Optional one-based occurrences.

The renderer removes every top-level element between the selected start and end boundaries, including tables. Ensure the boundaries are ordered and intentional.

## Tables

- `headers`: Exact concatenated text of each cell in the first row.
- `expected_matches`: Required table count; default `1`.
- `occurrence`: Optional one-based table occurrence.
- `header_rows`: Rows preserved at the beginning; default `1`.
- `prototype_row`: Zero-based row index cloned for each input row; default equals `header_rows`.
- `footer_rows`: Rows preserved at the end; default `0`.
- `rows`: Array of row arrays.

Every input row must contain no more values than the prototype contains cells. The renderer removes old data rows, clones the prototype, removes vertical merge declarations, fills values, and inserts new rows before preserved footers.

## Validation

- `required_text`: Every string must occur in the final document text.
- `forbidden_text`: No string may occur in the final document text.
- `expected_tables`: Exact number of top-level body tables.

The script also verifies that immutable package parts are byte-identical to the template.

## Unsupported generic operations

Implement project-specific OOXML logic for:

- Repeating a block that mixes headings, paragraphs, captions, and tables.
- Adding, replacing, or removing images.
- Editing headers, footers, footnotes, comments, tracked changes, charts, or content controls.
- Computing real TOC page numbers.
- Conditional page breaks and section definitions.

Use `ooxml-patterns.md` for those extensions instead of hiding assumptions inside fuzzy matching.
