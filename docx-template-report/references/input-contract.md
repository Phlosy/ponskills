# Input contract

Use this checklist when collecting a report-generation request.

## Required paths

```text
Template DOCX: /absolute/path/template.docx
Output DOCX:   /absolute/path/output.docx
Content data:  /absolute/path/report-data.json
Implementation root, if code must be added: /absolute/path/project
```

## Content-location mapping

Describe every generated item with one of these location types:

| Content | Operation | Location | Expected matches | Source field |
|---|---|---|---:|---|
| Project name | Replace paragraph | `{{PROJECT_NAME}}` | 1 | `project.name` |
| Overview | Replace between | `概述正文开始` … `概述正文结束` | 1 pair | `overview[]` |
| Device list | Fill table | headers `序号/设备名称/规格` | 1 | `devices[]` |
| Test cases | Repeat block | heading `测试项1` through its table | 1 prototype | `cases[]` |
| Evidence | Insert image | result cell in each case table | 1 per case | `cases[].evidence[]` |

Require exact, stable anchors. If an anchor occurs more than once, require a one-based occurrence number or a stronger structural signature.

## Behavioral decisions

Ask for these only when relevant:

- Generate completed report only, or also outline and blank variants?
- Leave missing values blank, insert a visible marker, or fail generation?
- Highlight uncertain values? Which color?
- Insert all evidence images or a bounded number per case?
- Update the cached TOC, preserve the field only, or let users refresh it in Word?
- Produce PDF and previews?
- What headings, tables, sections, and phrases must validation require?
- Which OOXML parts are allowed to change?

## Recommended normalized model

Build one report model before rendering:

```json
{
  "schema_version": "1.0",
  "report_id": "report-20260823-001",
  "template_sha256": "...",
  "cover": {
    "project_name": {"value": "示例系统", "certainty": "confirmed"},
    "report_date": {"value": "2026年8月23日", "certainty": "confirmed"}
  },
  "overview": ["第一段", "第二段"],
  "devices": [["1", "服务器", "32 核 / 128 GB"]],
  "cases": [],
  "validation": {
    "required_text": ["示例系统"],
    "forbidden_text": ["{{PROJECT_NAME}}"]
  }
}
```

Keep provenance and certainty in the model when draft/final completeness matters. Do not query live systems while mutating the DOCX.
