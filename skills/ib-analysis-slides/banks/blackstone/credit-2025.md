# 2025 credit: three related, separate themes

## Roles and coordinates

Investor and market pages are 720×540. Left/right content edges 36/684; black top rule y38.82, 5.5pt. Section label is 11.04pt sans, all caps; title is Sanomat Semibold 21.96pt, baselines about 23.8pt apart; subplot titles 14.04–15.96pt; body 11.04–12pt; footnotes 6.96–8.04pt. Retain enough source space for qualifications. The fallback examples use Georgia/Arial and are not font-identical.

Investor label is medium weight; market label is light in the source. Do not blindly make every sans label bold. Main claims are serif, explanation sans. I6 uses 18pt Sanomat Semibold for key actions within the same sentence as 18pt Guardian Light explanation, sharing the baseline despite different font boxes; body baseline step is about21.6pt. Keep phrase emphasis and conditional words together. B3 demonstrates mixed-role text in its conclusion. Source weights cannot be inferred from missing PPTX run attributes without theme/layout/master inheritance.

Palette: green #4B9F8A, dark teal #1B5E5C, sand #C39D78, rust #A95228, gray #C9CED6, blue #006492. Colors identify categories, scopes and emphasis. Do not use green as universally good where a negative value or unfavorable comparison is present.

## Investor overview

[B1](examples/index.html#B1) uses `examples/drawing.py::overview`, also exercised by a three-row real-content migration. V2 is an overview-specific typography case: measured source body12.96–12.984pt, labels14.04–14.064pt, title21.96pt. Do not inherit the smaller body sizes of other analytical pages. The earlier10.1pt example understated the evidence relative to its title.

Current fallback: Georgia Regular22pt title, Arial13pt evidence and14pt category labels. Georgia Bold is not a metrically or visually equivalent replacement for Sanomat Semibold. This is a reviewed fallback candidate, not brand-font identity or user aesthetic approval. Other themes keep their own roles.

Labels name categories in one or two lines; move conditions and explanations into the evidence. Label column132pt and evidence x205 are reflow decisions for the fallback, not copied source coordinates (source evidence starts around224.5). Rows first derive a minimum height from evidence lines, including continuations. Then assess the whole body: tightly packing minimum-height rows at the top leaves an unbalanced empty bottom. Distribute bounded extra vertical padding (up to24pt per row in this candidate) inside the reserved body and center each evidence block within its row; never stretch a sparse single row across the page. Long paragraphs require copy editing or a second page, not another global font reduction. Sources retain reserved space. Compare title weight, readable body size, color-block area and actual information density together; no-overflow alone is insufficient.

For portfolio pages, combine mutually complementary views (e.g. overall quality, sector distribution, seniority). Each numerical panel retains its own unit/denominator. Centered chart titles are roles, not a reason to add brackets. A qualitative platform ring is not a 100% allocation; select the relationship before choosing a circular shape.

## Earnings

Earnings pages use792×612 source coordinates; x39.6–752.4, top rule y51.72,6.05pt. Source table body is roughly8.5–10pt; notes about7pt. Explicitly dated stock sections are separate from quarterly and LTM flow columns. [B2](examples/index.html#B2) is native HTML with row/column header associations.

Black period headers, alternating pale rows, green/blue/sand section bands and rust current-period outlines each do a different job. In full statements, indent details; distinguish orange subtotal text from sand result rows. Keep currencies, per-share values, percentages, pp and share counts distinct. Preserve zero, dash, N/A and parentheses. A waiver reduces expenses, not revenue; do not silently reconcile source rounding by altering a cell. E6/E10 private calibrations cover the original tables; B2's fictional overview is not a tested full-statement generator.

The current column outline follows its period, including the appropriate header and bottom boundary. It is not an outline around every column. Longer labels consume label-column width first; avoid overlapping the next numeric cell. Add periods by reallocating width or changing the page, not globally shrinking every role.

## Credit-market mechanisms

[B3](examples/index.html#B3) has three parallel channels converging on a conditional outcome. They are not successive events. Keep the number and strength of channels supported by evidence. Retain the mechanism identity when the relationship applies: object-colored thin panel frames, circular numbered badges, rust serif action phrases with sans explanations, and a blue conditional-outcome frame. Numbers identify parallel channels, not temporal sequence. B3 now demonstrates these roles. The I6 outcome frame is x36–683.88, y393.88–456.99,1.5pt; its label and mixed-role two-line conclusion are separate.

For I14-like multi-view selection, separate EBITDA growth, sector default rates and lien/protection percentages. Each has independent scales and entity definitions. Industry check/cross marks are judgments bound to the corresponding row; never infer a missing symbol from a broken conversion. Use the original visible PDF for such reconstruction.

## Change conditions

Test rows4→3/5, a two-line category label, quarterly4→6 columns, negative results and fee waivers; test mechanisms3→2/4 with long mixed-role conclusions. These are stage-three tasks, not passed cases. Group geometry, table accounting and font fidelity are distinct checks.

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
