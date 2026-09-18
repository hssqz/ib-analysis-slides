# Native production and HTML handoff

## Units and layout

PptxGenJS positions/sizes are inches; font and line widths are points. For a 960×540 HTML canvas mapped to a 10×5.625 inch slide: x/y/w/h divide by96; CSS font pixels multiply by0.75. For its nested720×405 SVG stretched to960×540, divide SVG coordinates by72 and retain its numeric font size in points. These are different coordinate spaces. SVG text y is a baseline; Office text boxes use top positions and font metrics. Explicitly measure and review, do not treat baseline as top.

Use `defineLayout`, `addText`, `addShape`, `addTable`, `addChart`, `addImage` directly. Read the pinned dependency's TypeScript definitions or official documentation for an unfamiliar option. Fresh options objects prevent library mutation from changing unrelated objects. Name important objects with `objectName`.

Use fixed font sizes and actual line breaks from approved copy where appropriate. Leave measured width for glyphs, especially italic/tracked text; reflow before shrinking. Preserve spacing between groups and between copy and evidence. `charSpacing` is in points. Avoid manually spaced characters plus tracking. A table's declared height can grow if content needs more space: verify actual exported geometry and rendering.

## Editable representation

| Source object | Preferred output | Check |
|---|---|---|
| Text | Native text with font/weight/italic/color | Text content and line breaks survive rendering |
| Financial table | Native table; cell roles/borders/units retained | Table XML, row heights, signs and totals |
| Simple chart | Native chart with embedded data workbook | Chart type/series and embedded XLSX; target rendering |
| Complex source-specific chart | Native shapes/text when they preserve meaning better | Document shape editing vs spreadsheet editing |
| Grouping bracket/connector | Native line/shape plus independent label | Gap, fold, association, no text collision |
| Photo/evidence screenshot | Local raster media | Source, aspect ratio, not described as native data |
| Complex illustration | Image only when appropriate/approved | Label editability and declared limitation |

Preserve chart zeros, ranges, period gaps and subset relationships. Native chart rendering can differ from source SVG. An editable shape chart is acceptable when chart-data editing was not requested and the difference is disclosed. Do not replace all pages with pictures to obtain visual similarity.

## Self-contained project

```text
project/
  build.cjs
  package.json
  package-lock.json
  finalize.py       # copied from scripts/pptx.py when used
  sources.md        # evidence + decisions + known differences
  media/            # only when needed
  output/           # raw.pptx and deck.pptx
```

Run npm ci once, then `node build.cjs output` and `python3 finalize.py finalize output/raw.pptx output/deck.pptx`. Rebuild into a new directory. User-authored JavaScript executes code; review untrusted supplied scripts before running them. Do not download images/fonts implicitly from references.

## Existing PPTX and QA

PptxGenJS creates presentations; it is not a lossless PPTX importer. Inspect existing slides through rendering and XML, preserve the original and reconstruct only agreed scope. If retaining all untouched slide internals is required, use a suitable separately verified editing tool or report that boundary before choosing this path. Do not silently rebuild and lose notes/animations/media.

`pptx.py` checks package integrity, XML, relationship targets, slide count, native object counts, top-level geometry and transitions. It does not detect all text overflow, grouped transforms, appearance, semantics or spreadsheet formulas. `render.py` requires external LibreOffice/Poppler, not a browser mirror; installation is not automatic. Application rendering plus page-by-page inspection is required for visual acceptance. Compare HTML and PPTX at the same canvas size, record substitutions and unexplained differences.

No automatic font embedding, legacy PPTD import, browser editor or element-animation generator is provided. Select a licensed local font and re-render after substitution. A successful LibreOffice render is not proof of PowerPoint/WPS/Keynote playback parity.

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
