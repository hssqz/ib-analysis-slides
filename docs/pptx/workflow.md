# HTML → editable PowerPoint

Install only `ib-analysis-slides` for research-to-HTML. Install both `ib-analysis-slides` and `ppt-maker` for PowerPoint delivery. Each release ZIP contains one complete skill directory; keep both directory names. The PPTX skill works by itself for other presentations too.

## Setup

In the installed ppt-maker directory, with Node20+ and Python3.10+:

```sh
npm ci --ignore-scripts
npm test
```

Its own lockfile pins PptxGenJS and dependencies. Installing the repository root's optional HTML screenshot tools is separate; root `npm ci` does not install ppt-maker's dependencies. In a repository clone, run `npm --prefix skills/ppt-maker ci --ignore-scripts` then `npm run test:pptx`. First-time npm setup needs network; locally authored decks with local media export without network. No login, cookie, mirrored editor, legacy WASM or proprietary font pack is needed.

For actual slide rendering, install LibreOffice and Poppler, or use your target presentation application. These optional applications are not silently installed. The included renderer uses `soffice` and `pdftoppm` on PATH; executable overrides are supported. See [production guidance](../../skills/ppt-maker/references/production.md).

## Use

```text
Use $ib-analysis-slides to turn this report into Goldman Sachs-style
English HTML. After I confirm the preview, use $ppt-maker to reproduce
these approved pages as editable PPTX and a complete rebuildable source project.
Keep the confirmed content, layout and institution typography.
```

For already approved HTML, request the second step directly. The agent reviews the actual HTML and maps its objects into native PowerPoint text, shapes, tables and charts. Approval of the existing design need not be repeated. New design decisions remain within the user's authorized scope.

The bundled three-page example includes two approved-HTML reconstructions and a separate chart/media test. Run `node examples/build.cjs NEW_OUTPUT`, then `python3 scripts/pptx.py finalize NEW_OUTPUT/raw.pptx NEW_OUTPUT/deck.pptx`. Inspect it using the documented render command. It is not a general HTML/CSS import engine.

## What is editable

- Text, simple geometry and financial tables are native when authored that way.
- Native charts include an embedded data workbook; some source-specific charts are intentionally native shapes/text instead. Disclose which route was used.
- Photos and screenshots remain images. Do not flatten entire slides merely to match pixels.
- Default slide transition is fade. Fonts are referenced from the target system, not automatically embedded.

Delivery includes `build.cjs`, exact npm manifests, local assets, finalizer when used, evidence and final `.pptx`. The recipient can install dependencies and rebuild without either installed skill. The authoring source executes JavaScript; inspect untrusted source before running it.

## Legacy local version

Public0.8 replaces the old PPTD/mirrored-editor implementation. It does not ship that runtime, import/export PPTD, supply the old browser editor or convert arbitrary existing PPTX losslessly. Existing local installations are not overwritten by publication; if replacing your local ppt-maker folder, preserve any custom local version first. The twelve former consulting-kit relationships are retained as selection guidance, not advertised as twelve migrated native templates.

The new package was rendered in the application recorded in [validation](validation.json). That is not a promise of pixel identity or identical behavior in PowerPoint, WPS and Keynote. Bank support still comes from ib-analysis-slides; adding this exporter does not add bank profiles.

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
