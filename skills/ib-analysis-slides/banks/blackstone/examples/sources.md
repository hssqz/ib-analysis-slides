# Original example evidence and review

All Northfield Credit data and policy/sensitivity scenarios are fictional inputs authored in build.py. They do not represent Blackstone or any actual issuer, and are not research or investment recommendations. Private report text, charts, icons, logos and fonts are not distributed.

Rebuild with `python3 build.py`. Seven ordered pages in index.html are complete, editable HTML/SVG instances. They require no script at viewing time. B2/B7 use native HTML tables; the rest use editable text and shapes. No raster charts or embedded font dependencies are used in these public examples.

| Page | Question → evidence areas | Source-style observation → intentional adaptation | Input checks / migration boundary |
|---|---|---|---|
| B1 | What supports the platform claim? Four labeled evidence rows | V2 relationship rows, four distinct fills, serif claim and sans explanation; original fictional copy with fallback typography | Platform capital differs from portfolio NAV; three/four rows checked after overview typography correction; five rows remain untested |
| B2 | How do flows and dated stocks compare? Quarterly/LTM results, activity, balance sheet | E6 mixed periods, section bands and current columns;792×612 proportions,19 fictional rows | 60m shares;45/60=.75,174/60=2.90,1200/60=20; debt/equity computed separately. Full statement, waivers and6 periods untested |
| B3 | How might lower rates affect returns? Three parallel channels converging on one conditional outcome | I6 three mechanisms and result frame; mixed serif emphasis/sans qualification; editable connector paths | No numerical causal contribution claimed; 2/4 mechanisms and longer mixed-role copy untested |
| B4 | Which responsibilities sit under each lifecycle stage? Office, shared group, stage grid | D36 role hierarchy and centered broken-line group label; source pictograms replaced by generic initials | Three groups each contain four roles, not12 sequential steps. Gap measured for current label only |
| B5 | How does one portfolio differ by classification and period? Four rings with two local legends | D38 group-local categories and divider; reduced to two explicit fictional categories per ring | Each ring sums100; leader touches its sector; gray label uses darker companion color. Source right-side healthcare selection list is not implemented here |
| B6 | What do different policy measures show? Signed flows+net, separate rate line, share comparison | S29 topic/claim shell and one-large/two-small composition; quarterly fictional dates and explicit forecast boundary | Net[100,150,40,-60,-10,120,200,200] equals signed components; positive and negative stacks separated;75%+25%=100% |
| B7 | How do explicit assumptions change a value? EPS×yield matrix | S19 input-axis matrix and visible values; fictional perpetual formula replaces no real source data | 42 cells calculated from EPS×.4/(yield+.05−.02); stated model differs from source DDM. Input extension/model change untested |

## Overview correction after migration feedback

The source V2 body is12.96–12.984pt and labels14.04–14.064pt; the earlier example used10.1pt evidence. That role-specific omission, a heavier Georgia Bold fallback, and fixed-height rows made titles/color blocks dominate. B1 now uses the shared `drawing.overview` with13pt evidence,14pt short labels, Georgia Regular22pt and content-derived row height. These are explicit fallback/reflow choices, not exact source-font reproduction. Three-row real content and four-row fictional content were rendered; B2–B7 HTML remained byte-identical. The first correction was rejected for overall layout: minimum-height rows packed content at the top. The next candidate adds bounded whole-page vertical distribution and a narrower label column; the final six-page local migration, including the balanced overview, was accepted by the user. This approval does not extend automatically to independent outputs.

## Actual checks

2026-09-18: builder assertions, package/static checks and actual Chromium rendering completed for all seven pages. Every page was visually inspected, including grouping-label clearance, financial row hierarchy, forecast region, negative-stack net line and ring label/sector association. An initial ring leader association was corrected; B3's mixed-role conclusion and B4's non-sequential initials were clarified. Stage-four regression restored B3's colored panel outlines, circular channel identifiers, rust action phrases and blue outcome frame. Final screenshots form preview.png. No external requests or SVG-text-outside candidates occurred in the final public render; these mechanical results do not replace the visual inspection.

Original-reference comparisons belong to private stage-two development records, outside this package. Exact brand-font identity is not established:2025 source uses unbundled Sanomat/Guardian; current examples deliberately fall back to Georgia/Arial. The whole-page examples demonstrate executable structures. Independent generation and clean-install results are reported separately in the repository release notes; these examples alone do not establish arbitrary migration or PowerPoint compatibility.

Selected local and independent tasks exercise different row/category/period counts, long group labels and financial evidence. The release notes distinguish these tests from remaining untested variants. Fee-waiver-specific migration and complete 66-variant coverage remain unverified.

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
