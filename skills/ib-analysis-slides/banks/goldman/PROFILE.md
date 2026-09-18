# Goldman Sachs-inspired profiles

Visual rules extend the v0.6 basis with v0.7 text-role and grouping-component observations. Source observations come from investor communications, not internal investment-committee or transaction pitchbooks. Original PDF/PPTX files, institutional marks and verbatim report reconstructions are not distributed.

| Profile | Use | Rules | Public example |
|---|---|---|---|
| `goldman-bernstein-2024` | Industry, capabilities, structure, peers, operating mechanisms, return comparisons | [White analytical](bernstein.md) | [4 analytical pages](examples/analysis/index.html) |
| `goldman-earnings-fy2024` | Financial results, segment income, asset movements, selected balance-sheet/capital metrics | [Financial reporting](earnings.md) | [3 financial pages](examples/financial/index.html) |

Language: **English required** for both profiles, including all slide titles, text, chart labels and short source notes. Chinese input must be interpreted accurately and rendered in English. A Chinese-language adaptation is outside the supported Goldman profile. Run the shared checker with `--language en`; also review the actual wording, since a lang attribute cannot prove the text language.

Both display at 960×540. Analytical source units are 720×405; financial source units are 960×540. Their title scale, body background and table grammar differ. Select a coherent theme; if both are needed, separate chapters. Industry analysis defaults to analytical; financial evidence may justify reporting. The profile date identifies the design source, not the year of new data.

For text hierarchy and local grouping, inspect the [four-page role examples](examples/typography/index.html) and [transfer notes](examples/typography/sources.md): analytical T1–T3 and financial T4 keep separate grammar.

Read [example mapping](examples/README.md) for qualitative rings, quantitative donuts, subset charts, axis breaks and evidence requirements. Examples contain fictional entities. Source identifiers B02–B20 and E13/E16/E17/E20/E22 in the rules are observational references, not a promise that all those source pages are bundled.

First identify composition, trend, peer comparison, subset, rollforward or qualitative relation. Select an expression based on that relationship, then allocate area. Common institutional parameters establish the style; lines, brackets and fill carry local meaning. A donut, a client relationship ring and a process cycle encode different things.

No dark-theme package, full three-statement model, DCF or internal pitchbook is supplied. Unsupported pages may be designed as explicit adaptations when the user supplies evidence, but not claimed as source-faithful replicas. Fonts use the local system and are not embedded. Generated documents should carry the user's identity and appropriate source attribution, not imply bank authorship.

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
