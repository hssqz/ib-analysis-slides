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
| Inspect the four pages and independently check calculations | Arithmetic and inspected technical checks passed; subsequent user review rejected the overall visual/analytical quality |

The input was a fictional equipment company and a separately scoped fund: historical revenue with missing early splits, a subscription subset, customer mix, a target floor, annual costs/profit, quarterly revenue, selected balance-sheet values, an AUM bridge and two classifications of the same stock. The agent retained missing values, units, entity boundaries and the distinction between business revenue contribution and company profit growth.

Checked results include revenue200→230; service contribution20/30=66.7%; profit24→27; quarter totals230; company assets150=90+60; fund100+15−5+0=110; fee-earning88 is80% of110. The agent did not infer undisclosed business profit or a company-wide forecast from a service target.

An image preview made two titles appear too close to the top. DOM inspection, actual PNG pixels and an independent recapture ruled out an output defect: title pixels start at y32/y33. No geometry was changed to compensate for the viewer. Final HTML hashes match the capture reports:

- analysis.html: `99e21052f32187454afd0042231b1ebdf36f84a75f9835a824fd83c529d95ed4`
- financial.html: `bdf3cd741cd1889df2d87743e3f2211a0809027cc7d974875d54772e0d6f3cdd`

## Quality assessment correction

The initial wording overstated the visual result. The small fictional input was useful for testing installation, arithmetic and a few chart contracts, but the requested two analytical pages repeated a narrow set of facts and devoted substantial space to missing-data qualifications. Technical correctness did not establish a convincing investment-research presentation. This run must not be cited as user-approved visual quality or as the package’s capability ceiling.

## Follow-up in v0.6.2

The maintainer clarified the intended language contract: Goldman profiles require English; shared language checking must also accommodate future domestic-bank profiles. This is a product-rule clarification, not an installation failure found by the independent trial. The checker now accepts `--language`, defaults to English and checks bundled Goldman examples as English. Regression confirms that a Chinese-declared page fails `--language en` and passes `--language zh`; both independently generated English decks also pass the updated checker.

No installation or generation blocker was found in this case. It does not prove arbitrary inputs, every chart choice, a clean operating system, other font stacks, Chinese institutional profiles or PPTX/PDF export. The fresh agent tested v0.6.1; v0.6.2 received focused language and existing-output regressions, not a second fresh-agent generation run. Screenshot diagnostics are not comprehensive HTML layout or semantic verification.

## Matched rich-input comparison — 2026-09-18

Two fresh-context agents independently produced five English analytical pages from the same complete [ASML 2024 EU-IFRS annual report](https://ourbrand.asml.com/m/3035813cf1b8ea4f/original/2024-Annual-Report-based-on-IFRS-FINAL.pdf), using the same company-research brief and Chrome 153.0.8010.52 / Playwright 1.62.1 environment. One used the frozen development v0.6 package and its declared companion dependency; the other used the complete public package at `7b3267da84ca6c294ad339c909d6cc27849c0ae8`. Neither received historical generated slides, the other output, or reviewer feedback before final delivery.

The brief covered manufacturing needs and product capabilities, operating and geographic structure, R&D and ecosystem mechanisms, and long-term opportunities and constraints. Both outputs were inspected page by page; a separate reviewer compared screenshots, source evidence and final records.

| Observation | Result |
|---|---|
| Useful evidence and composition | Both produced substantial, complementary evidence; no clear overall quality-tier drop in the public output |
| Public-output strengths | Three-year revenue structure plus a reconciled operating-profit bridge; technology and geographic exposure; concrete development and delivery conditions |
| Development-output strengths | More immediate geographic-change comparison; an actual revenue baseline beside future scenarios; explicit ecosystem network |
| Font scale | Both retained the 19-source-unit title at 720×405 scaled to 960×540; the public output did not reduce body roles to footnote scale |
| Remaining caveat | Development output showed a 0.7pp operating-margin change from rounded disclosed rates without stating that basis; exact amounts give 0.644216pp, shown as 0.6pp and documented by the public output |
| Independent self-review | Public producer found and corrected a table/note-spacing issue before delivery; final reviewed pages had no confirmed clipping or overlap |

Input SHA256: `1dd779ecc302d3d84857ab933df8f3d33c939f722555686e3ea60815cfc964e4`.
Development HTML SHA256: `5e5187e88482568fb08774896dc6da830e294a8fa331f176d8406827825c9769`.
Public HTML SHA256: `bb04f11cf47ab7be62a4ef58dddd79e90e2f41ad1dcc1c743ddf072fc89682bc`.
The unchanged input/package snapshots and generated artifacts remain in the maintainer’s private test archive; they are not distributed with this skill. Exact deployed model identifiers were not exposed and are not asserted.

This result supports input adequacy and the earlier brief as important contributors to the weak small-input trial; it does not establish input as the sole cause. Publication changed both examples and execution dependencies, so this is a comparison of whole packages, not an isolated test of either change. One pair cannot establish statistical equivalence, every supported relationship, the financial theme, or user aesthetic approval. No skill rule was changed on the basis of an unconfirmed packaging regression.

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
