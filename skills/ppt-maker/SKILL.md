---
name: ppt-maker
description: Create, revise and reconstruct editable PowerPoint presentations using PptxGenJS. Use for approved HTML-to-PPTX handoff, reference reconstruction or original deck production. Delivers rebuildable JavaScript source and local PPTX; new creative work uses outline, page-copy, wireframe and preview confirmation.
---

<!--
[INPUT]: User evidence, approved pages or reference visuals; references/ and scripts/.
[OUTPUT]: Self-contained editable source project and validated local PPTX.
[POS]: Standalone public presentation skill; institutional styles belong to the selected style skill.
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# PPT Maker

Public version 0.8.0. This implementation uses MIT-licensed PptxGenJS. It has no Kimi service, mirrored editor, patched WASM or proprietary-font dependency. Read [provenance](references/provenance.md) for the replacement boundary.

Default final delivery is **a rebuildable JavaScript project plus PPTX**. The source includes `build.cjs`, `package.json`, `package-lock.json`, local media when used, evidence and rebuild instructions. Public 0.8 does not import/export legacy PPTD or provide the old browser editor. Do not promise round-trip conversion of an arbitrary existing PPTX.

## Route and retain approval

- New creative work: establish audience, setting, decision, language, scope and page count. Show a page outline with conclusion titles, messages and evidence; obtain confirmation before elaborating pages.
- For each new page (or requested batch), show full copy, evidence, visual hierarchy, an actual ASCII placement sketch, style tokens and asset route. Confirm content/design, then render a preview. Full-deck production follows approval of the intended scope.
- Honor explicit user authorization and already-confirmed pages; do not restart the gate after a user has approved complete production. A request for one page does not silently authorize unrelated pages.
- Exact reconstruction, deterministic export and narrow specified edits can proceed using the fixed content/layout. Preserve unaffected source and deliver revisions separately.
- Discussion does not require a toolchain install or slide production.

## Approved HTML handoff

For `ib-analysis-slides`, read its final HTML, evidence, page decisions and actual preview. The approved institutional theme is authoritative: do not replace its typography with a generic consulting/BP preset. Goldman pages remain English; another profile or user determines other output languages.

Approval to export a finished HTML deck covers its existing content/layout. Ask only about unresolved decisions that materially affect the result. Map text to editable text boxes, tables to native tables, simple geometry to native shapes, and charts to a native chart or documented editable shapes. Images remain images. A full-slide screenshot is not an editable reconstruction.

Read [production](references/production.md) before building. Reconstruct the approved layout deliberately; this package is not an arbitrary HTML/CSS converter. Keep text role, weight, italic, tracking, alignment, object color and grouping geometry together. Do not promise pixel identity or spreadsheet-editable charts without inspecting the actual PPTX.

## Content and design

Read [design and component selection](references/design.md) for new creative work or consulting components. A supplied deck can be a strict template, a style reference or only an asset source; follow the user's stated role. An asset-only source supplies neither claims nor theme.

Keep each argument traceable to an entity, period, unit, denominator and source. Separate historical facts, forecasts and synthesis. Compute derived values from full-precision inputs and verify the displayed result. Never import example values into a real company analysis.

Use real evidence images when they carry the claim. For missing conceptual illustrations, mention built-in image generation if available; simple editable diagrams should remain native. Avoid irrelevant imagery. Save permitted media locally, preserve aspect ratio and record origin. No private brand pack is bundled.

## Build and check

Only when production begins:

1. Check Node.js 20+, npm and Python 3.10+. Run `npm ci --ignore-scripts` in the installed `ppt-maker` directory. This downloads pinned dependencies; subsequent local generation needs no network for locally stored assets. Do not install dependencies silently during discussion.
2. Create a separate source project. Copy this skill's `package.json` and lockfile, author `build.cjs` using `pptxgenjs`, and copy required local media. Run `npm ci --ignore-scripts` in that project; it must not depend on an author's private path or an adjacent skill installation.
3. Reuse [the original worked example](examples/build.cjs) for API mechanics, not its fictional content or fixed layout. `node build.cjs output-directory` writes a new `raw.pptx` and refuses an existing output directory.
4. Finalize the raw file: `python3 /path/to/ppt-maker/scripts/pptx.py finalize output-directory/raw.pptx output-directory/deck.pptx`. Default transitions are root-level fade. Use `--transition none` only when requested. The destination must be new.
5. Run `python3 /path/to/ppt-maker/scripts/pptx.py check output-directory/deck.pptx --expect-slides N --transition fade`. Inspect text, native tables/shapes, chart parts and workbooks as relevant. Package validity does not prove layout or application behavior.
6. Render the final PPTX in a target application. Optional local route: install LibreOffice and Poppler, then `python3 /path/to/ppt-maker/scripts/render.py output-directory/deck.pptx new-qa-directory`. This opens the PPTX through LibreOffice, emits PDF and per-page PNG. Open every image; compare against approved previews. Fix clipping, wrapping, alignment, density, missing text, labels and source notes, then rebuild/recheck/re-render. A web preview alone is insufficient evidence of PowerPoint layout.
7. If no renderer is available, report the exact unperformed visual check; deliver source and structurally checked PPTX without claiming visual acceptance. Font substitution and PowerPoint/WPS/Keynote behavior need their own review. System fonts are referenced, not automatically embedded.

After changes, record the final PPTX and screenshot hashes, evidence checks, editability observed and remaining differences. Element animations and speaker notes are opt-in; do not add them to reading-oriented decks by default. This version only automates slide-level transitions.

## Delivery

Link the complete project directory, `build.cjs`, local media if any, and final PPTX. Retain exact dependencies and copy the small finalizer into the project if its rebuild command uses it. Include sources and reproduction commands. Do not deliver only a script that imports files from the installed skill.

Explain editable scope precisely: native text/table/shape edits, native chart data if verified, raster media exceptions and font limitations. Users can edit the PPTX in PowerPoint, WPS or LibreOffice, or modify the source and rebuild. Do not suggest the removed legacy editor command.
