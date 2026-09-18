## v0.6.2 — profile language contracts

Released 2026-09-18. [Independent public-package trial](forward-test.md): public installation, browser setup, checks and four-page generation passed on v0.6.1. This patch received focused language and existing-output regressions.

Goldman Sachs profiles require English output, including when research inputs are Chinese. Shared language handling is kept separate for future domestic-bank profiles; no Chinese bank profile is released by this update.

The static checker accepts `--language` and keeps English as its default and as the packaged Goldman-example requirement. Regression verifies that a Chinese-declared document fails the Goldman English check and passes an explicitly selected Chinese-language check. Visible prose still requires actual review.

---

# v0.6.1 — first public package

Released 2026-09-18. One installable skill, Goldman Sachs-inspired analytical and reporting profiles, ten fictional example pages and optional screenshot tooling.

## What changed for publication

Accepted v0.6 evidence and visual rules were reorganized into shared references and `banks/goldman/`. The HTML execution path is self-contained and no longer requires a private companion skill. Original institutional page reconstructions and private development logs are replaced by selected fictional HTML examples. Existing analytical rules, role scales and income-attribution constraints remain; no additional institutional support is claimed.

## Validation and limits

During development, nine local migration pages and thirty-two pages across seven fresh agent tasks exercised industry, company, financial and fictional inputs. A financial attribution failure led to the v0.6 rule: revenue contribution cannot imply profit contribution without matching evidence. A fresh two-page financial regression then passed. Revision testing recomputed affected pages and preserved unrelated pages. This summarizes development history; private reports and task logs are not distributed.

The public package is a different distribution. Release checks cover complete-directory copying into a fresh path, no private dependency references, local link integrity, static checks on four HTML files/ten pages, screenshot-helper self-test, final rendering and visual inspection, matching screenshot hashes and selected fictional arithmetic. [Final checks and hashes](validation.json): package/static checks passed; all ten rendered pages were viewed. Eight screenshots match the archived reviewed pages exactly; two have minor pixel differences recorded in the JSON, with no observed layout change. HTML content is unchanged apart from comments/inter-tag whitespace. No external requests or SVG text overflow; two rotated-label box intersections were inspected and accepted. `npm ci --ignore-scripts` installed the lockfile dependencies; rendering used an existing Chrome on the same host. A fresh directory on the same host does not establish clean-machine installation, cross-platform font parity or fresh-agent generative equivalence after packaging.

Directed tests establish that the demonstrated donuts, qualitative rings and broken axis can be drawn. They do not establish automatic selection of every complex expression. Some source-observed patterns have no public worked example; the example mapping names them. No PPTX/PowerPoint check or workbook-linked chart capability is included.

## Distribution boundary

Included: original instruction text, measured visual conventions, authored helper scripts, fictional evidence and editable generated examples. Excluded: original bank PDF/PPTX, logos, verbatim institutional presentations/legal text, proprietary research reports, private paths, session records, credentials and dependencies themselves. Runtime dependency licenses remain those of their respective packages; this repository does not relicense them.

MIT covers the repository's original material; no representation of institutional affiliation or endorsement is made. Source research provided by a user remains that user's input and does not become a redistributable part of this project.

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
