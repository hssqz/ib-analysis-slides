# Independent public-package trial

2026-09-18. A fresh agent started from the public GitHub README and cloned commit `d13d7d8b6000b67baf0bdce58b24554ded2b96c0` (v0.6.1). It had no development conversation, private skill or local release checkout. The original clone remained clean.

## What was actually run

| Step | Result |
|---|---|
| Clone public repository and copy the complete skill into a temporary skills directory | Passed; no global skill changes |
| `npm ci` | Passed; non-blocking fsevents install-script policy warning |
| `npx playwright install chromium` | Passed; Chromium/headless shell downloaded to the standard macOS Playwright cache |
| `npm test` | Passed: four bundled HTML files, ten example slides |
| `npm run test:capture` | Passed |
| Generate two analytical and two financial pages from new fictional evidence | Completed using only the public skill |
| Check and capture both new decks through the installed skill | Passed; no SVG text overflow, overlap candidates or external requests |
| Review all four rendered pages and independently check calculations | Passed within this case |

The input was a fictional equipment company and a separately scoped fund: historical revenue with missing early splits, a subscription subset, customer mix, a target floor, annual costs/profit, quarterly revenue, selected balance-sheet values, an AUM bridge and two classifications of the same stock. The agent retained missing values, units, entity boundaries and the distinction between business revenue contribution and company profit growth.

Checked results include revenue200→230; service contribution20/30=66.7%; profit24→27; quarter totals230; company assets150=90+60; fund100+15−5+0=110; fee-earning88 is80% of110. The agent did not infer undisclosed business profit or a company-wide forecast from a service target.

An image preview made two titles appear too close to the top. DOM inspection, actual PNG pixels and an independent recapture ruled out an output defect: title pixels start at y32/y33. No geometry was changed to compensate for the viewer. Final HTML hashes match the capture reports:

- analysis.html: `99e21052f32187454afd0042231b1ebdf36f84a75f9835a824fd83c529d95ed4`
- financial.html: `bdf3cd741cd1889df2d87743e3f2211a0809027cc7d974875d54772e0d6f3cdd`

## Follow-up in v0.6.2

The maintainer clarified the intended language contract: Goldman profiles require English; shared language checking must also accommodate future domestic-bank profiles. This is a product-rule clarification, not an installation failure found by the independent trial. The checker now accepts `--language`, defaults to English and checks bundled Goldman examples as English. Regression confirms that a Chinese-declared page fails `--language en` and passes `--language zh`; both independently generated English decks also pass the updated checker.

No installation or generation blocker was found in this case. It does not prove arbitrary inputs, every chart choice, a clean operating system, other font stacks, Chinese institutional profiles or PPTX/PDF export. The fresh agent tested v0.6.1; v0.6.2 received focused language and existing-output regressions, not a second fresh-agent generation run. Screenshot diagnostics are not comprehensive HTML layout or semantic verification.

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
