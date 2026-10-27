# OOXML extension patterns

## Package parts

A DOCX is a ZIP package. Report renderers commonly edit:

```text
word/document.xml
word/_rels/document.xml.rels
[Content_Types].xml
word/media/*
```

Keep styles, numbering, settings, fonts, themes, headers, footers, and section definitions unchanged unless the contract explicitly permits changes.

Use the WordprocessingML namespace:

```python
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"w": W, "r": R}
```

## Repeat a multi-element prototype block

1. Identify an exact prototype heading, description, caption, and table.
2. Confirm their relative order and uniqueness.
3. Deep-copy all prototype elements before removing them.
4. Remove the original prototype block.
5. For each model item, deep-copy the prototypes, replace their text/cells, and insert them at one stable body index.
6. Validate that generated block count equals model item count.

Never locate the table by “the next table somewhere later” without also verifying its expected header signature.

## Insert evidence images

1. Obtain a known-good `<w:drawing>` from the supplied template or construct one with explicit dimensions.
2. Copy image bytes to a unique `word/media/<name>` part.
3. Allocate an unused `rId` in `word/_rels/document.xml.rels` and add an image relationship whose target is `media/<name>`.
4. Add a `[Content_Types].xml` default for the extension when absent.
5. Deep-copy the drawing prototype, replace `a:blip/@r:embed`, and assign unique drawing IDs.
6. Append the drawing to the target paragraph or table cell.
7. Validate that every relationship target exists and each drawing relationship resolves.

Bound image count and dimensions. Preserve all source evidence outside the DOCX when the report embeds only representative images.

## Build report variants

For outline, blank report, and completed report, prefer a derivation pipeline:

```text
Golden template -> outline -> blank report -> completed report
```

- Outline: create the final chapter and case layout without measured values.
- Blank report: change only outline-specific wording and preserve empty result fields.
- Completed report: fill measured values, verdicts, people, times, issues, and evidence into the laid-out blank report.

Validate that outline and blank variants contain no measured verdict symbols or evidence drawings.

## Update a cached TOC

Preserving a TOC field is not the same as updating its visible cache.

1. Preserve the `TOC` field instruction.
2. Enumerate paragraphs with heading outline levels.
3. Add deterministic bookmarks to headings.
4. Build cached TOC paragraphs containing `HYPERLINK` and `PAGEREF` fields.
5. Use placeholder page numbers before layout.
6. Render the DOCX to PDF with LibreOffice.
7. If reliable PDF outline/page information is available, update cached page numbers and render again.

Validate TOC entry count, bookmark existence, hyperlink targets, and expected case-heading count.

## Render safely with LibreOffice

Always use a fresh temporary user profile to avoid lock contention and host configuration drift:

```python
subprocess.run([
    executable,
    "--headless",
    f"-env:UserInstallation=file://{temporary_profile}",
    "--convert-to", "pdf",
    "--outdir", output_directory,
    document,
], check=False, capture_output=True, text=True, timeout=180)
```

Treat a missing LibreOffice executable as an unavailable optional check. Treat a failed conversion as a failed visual/render validation.

## Structural verification

Compare template and output contracts:

- Hash immutable package parts.
- Compare section size, orientation, margins, headers, and footers.
- Require a valid TOC field when applicable.
- Count generated case tables or blocks.
- Require report version and mandatory text.
- Reject leaked placeholders and measured results in blank variants.
- Parse every relationship file and verify internal targets.
- Record output SHA-256 and validation errors in a machine-readable manifest.
