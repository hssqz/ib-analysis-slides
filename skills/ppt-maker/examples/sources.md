# Worked example: approved-page reconstruction

Pages1–2 use the original fictional Meridian Instruments evidence from the public ib-analysis-slides text-role gallery, pagesT2/T4. They are a manual native reconstruction, not an automatic HTML importer. The original HTML is available in the sibling skill's `banks/goldman/examples/typography/`; it is not a runtime dependency. Page3 is a separate capability test: synthetic chart values−4,+7 and an original80×40 two-color image. Those values are not Meridian's operating history.

Revenue200→230 consists of equipment150→160 and service50→70. Costs120→140, operating expenses45→52, operating profit35→38, interest5→4, tax6→7 and net profit24→27. Revenue contributions10+20=30 do not establish business-level profit contribution. All values and claims are fictional; no original bank text/images/fonts are distributed.

Page1 uses editable text and a deliberately shape-based stacked chart to preserve label placement; it has no chart-data workbook. Page2 uses a native financial table and editable commentary; line breaks are adapted to Office metrics. Page3 uses a native bar chart with embedded XLSX, tracked editable labels, native shapes and raster media. System Arial is referenced, not embedded. The PNG cannot be edited as chart data.

From the installed skill directory after `npm ci --ignore-scripts`:

```sh
node examples/build.cjs /absolute/new-output
python3 scripts/pptx.py finalize /absolute/new-output/raw.pptx /absolute/new-output/deck.pptx
python3 scripts/pptx.py check /absolute/new-output/deck.pptx --expect-slides 3 --transition fade
python3 scripts/render.py /absolute/new-output/deck.pptx /absolute/new-qa
```

For independent project delivery, copy build.cjs, example.png, this source note, the skill package.json/package-lock.json and scripts/pptx.py (as finalize.py) into the project. Install there and run `node build.cjs new-output`, followed by `python3 finalize.py finalize new-output/raw.pptx new-output/deck.pptx`. No private paths or installed sibling skill are required.

Limits: no legacy PPTD importer, universal HTML/CSS conversion, mirrored editor or automatic font embedding. Actual review describes the tested renderer in release validation; it is not a promise of identical rendering in all Office applications.

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
