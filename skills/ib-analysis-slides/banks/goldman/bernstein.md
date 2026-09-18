# Goldman Sachs · Bernstein 2024 · White

> Runtime profile v0.5. Load with PROFILE.md for shared page tokens. This file contains the theme-specific selection and evidence rules; original PDFs are not a normal generation dependency.

## Choose the analytical task first

| Task | Whole-page example | Required evidence | Preserve |
|---|---|---|---|
| Two complementary franchises | B02 | Two business roles, supporting facts and outcomes | Overlap means relationship; the four bottom indicators are separate metrics |
| Capability plus composition | B03 | Same-denominator component amounts and headline total | Quantitative donut; total in centre; outside labels; three evidence groups |
| Parallel growth opportunities | B04 | Three comparable initiatives | Consistent row rhythm, a single emphasized column |
| Capability plus product breadth | B05 | Advantages, categories, category values, strategy lists | Unequal list lengths; no fabricated blank cells; category header distinct from strategy |
| Margin improvement | B06 | Peer range/floor, actual margin, stated target, levers | “35%+” remains a floor; qualitative target has faded boundary, never an invented exact percentage |
| Operating leverage mechanism | B07 | Current state, repeated process, mature state and examples | Nonquantitative schematic; common infrastructure spans the process; examples sit below |
| Market opportunity plus firm history | Existing B08 | Comparable history, market estimates and company goal | Keep estimated TAM and company goal separate |
| Channel relationships | B09 | Client channels, proven capabilities and new actions | Ring is qualitative; checkmarks and amber tilde marks have distinct meanings |
| Drivers to medium-term targets | B10 | Drivers, shared targets, result measures | Shared target spans the first two drivers; result rows shaded |
| Scale and durable revenue growth | B12 | Total history, endpoint components, revenue components and a subset | Selective stacks, gray totals, latest-period break, subset not added to total |
| Assets and fee generation | B13 | Historical assets, total/fee-earning stock, process | Monetary boxes are quantitative; circular steps are not shares |
| Peer scale plus market growth | B14 | Comparable peer assets, fee-earning subset, categories, market estimates | Gray peers/colored focal stack; second metric boxes; four market rows |
| Fundraising history and peers | B15 | Cumulative series and comparable cumulative peer amounts | Not annual flows; explicit highest-bar break; latest stack and focal outline |
| Returns across strategies | B16 | Net IRR, cash-flow-matched PME, same sample methodology | Three small multiples use one numeric scale, distinct category colors, methodological notes |
| Ecosystem and delivery mechanisms | B17 | Business departments, client classes, three mechanisms | Five business sectors around clients are NOT customer shares; right rows are mechanisms |

Public examples use fictional data: [analytical deck](examples/analysis/index.html) and [relationship/axis-break deck](examples/relationships/analysis.html). See [example mapping](examples/README.md). B-identifiers below describe source observations, not files bundled with this release. Original report reconstructions are not distributed.

## Page grammar and geometry

Use 720×405 source units, displayed at 960×540 CSS pixels. Arial. Main title x33,y38 baseline, 19pt bold deep blue, second line at y58. Main content normally begins around y93; chart baselines around y300–327. These are reconstructed anchors, not exact coordinates for every source object. White background; #00355F headings, #23C7BA relational accents, #6E93BE / #20657C / #6AA5B6 categories and #B2B2B2 context totals. When selected, bracket heads use 8–10pt uppercase with letter spacing; calculate the white gap from actual rendered text, including spacing. Use the role measurements below rather than one body/chart font default. Small source notes are about 6–7 source units. Change area or wrapping before reducing type.

A few arguments may contain many independent evidence elements. B12 carries time history, endpoint composition, a second revenue series, latest subset and period distinctions; replacing it with two large number cards loses the analysis. B07's full-width process is one connected argument, not three independent panels.

Use source-task templates rather than a single grid. Preserve the left-to-right hierarchy and supporting positions: B03/B05 evidence explains capability; B12/B14/B15 have two parallel quantitative questions; B16 has three comparable panels; B07 is state→mechanism→potential outcome.

## Role scale and evidence area

All values below are source units on 720×405, not final CSS font sizes. At 960×540, scale geometry and text by 4/3: 10 becomes approximately 13.33 CSS pixels. PDF bounding-box tops are not SVG baselines. These are measured examples, not a universal type scale.

| 源页/角色 | PDF字号（pt）与定位样例 | 实现含义 |
|---|---|---|
| B03 规模说明 | 10.56；Total Alts Assets文本bbox上缘y216.3 | 解释承担规模与增长证据，不能统一降为脚注 |
| B03 环图外标签 | 12；Liquidity上缘y134.0，金额y148.4 | 类别与金额是主要阅读对象，应比一般图表细目突出 |
| B05 左侧能力正文 | 9.96–9.98；末项两行上缘328.2/340.2，相差12 | 正文与矩阵短条目分角色设计 |
| B05 右侧矩阵 | 类别/金额约9；条目8.04–8.06；单行Buyout上缘169.9 | 约8是局部密集条目，不是整页默认正文 |
| B07 机制与策略例子 | 主要说明约9.96；底部策略7.56–7.58 | 例子从属完整机制，低字号有明确范围 |
| B12 图内数字 | 9–9.02；分组标签9.96 | 数字贴近柱与分项，不另开宽松摘要区重复展示 |
| B14 多指标 | TAM金额11.04–11.06；类别9.96；柱数值9；收费资产约8.04 | 主指标、类别与次指标有不同层级 |
| B17 机制与客户 | 机制名称12；客户/支持点9.96–9.98；内圈客户上缘197.7/213.7/229.8 | 重点节点大字、细目适度紧凑，关系图本身承担信息 |

For a new page, identify the reading role before choosing size: an argument or primary label should not inherit a small matrix-detail size. B03/B05/B12 group-label tops are around y88; even B14's two-line title allows a similar group position. Title, subtitle and group heading are optional levels determined by information, not a fixed vertical stack. Avoid reserving unused title rows.

Give each evidence view a job. A full-width table with a few short rows may need a narrower area, a related evidence view, or a narrower page claim. A large chart with tiny early values still needs an honest scale; improve the surrounding evidence and placement, not the values. Density is the amount of useful evidence and readable relationships, not word or chart count. See the example mapping for supported adaptations.

## Input changes and whole-page selection

The following contracts are migration judgments supported by the source examples. They do not establish tested limits for every label length or category count.

| 源页及观察 | 必需输入关系 | 必须保留的证据组合 | 迁移判断：可调与替代 |
|---|---|---|---|
| B03 左能力/规模证据，右总体构成 | 同分母分项与总量；能力有独立事实支撑 | 构成解释是什么，能力证据解释为何重要；近似总额保留 | 类别增加需重新分配标签/引线空间；小类可改明细表但保留总量关系；仅有构成数据时不虚构左侧优势 |
| B05 左能力，右不等长策略列 | 分类、各类项目清单，可选规模指标；独立能力证据 | 类别与条目层级、有效列长、能力论据 | 列宽与区域面积随名称和项目量调整；没有共同“行对象”时不补空格伪造横向对应；若每行确为同一对象的属性，可选真正对照表 |
| B07 当前状态—共同基础—成熟状态，下附例子 | 有证据的状态差异、共同机制与具体例子 | 共享基础覆盖过程、状态变化与例子归属 | 阶段与例子数量可调；若输入只有时间先后，用时间轴而非经营杠杆机制；没有因果证据则限定为假设，图高不编码虚构利润 |
| B12 总量趋势+端点结构，另有收入分项及子集 | 可比总量历史、已知端点分项；独立收入历史与已知子集 | 趋势、结构、收入及子集各解释一个问题；期间断点 | 只有端点有分项便选择性堆叠；全期有分项才可全期堆叠；子集缺失则省去该层并重分面积，不能补造；独立系列不足时收敛页目标 |
| B14 同业总量+收费资产次指标，右侧市场机会 | 同口径主体总量、可选主体构成、明确次指标、各市场起止值 | 排名、次口径和市场机会各自有标签与归属 | 同业数量可变，次指标与主体对齐；只有单一排名时不复制次指标空框；市场口径不同需另区解释；双区比例随证据调整 |
| B17 业务/客户生态，右侧三组机制 | 类别、参与者与实际机制支持点；无占比分母 | 生态和机制并置，几何无份额意义 | 节点及标签随类别调整；需要精确一一映射时选择矩阵/连线表达，源环不足以说明映射；只有列表时可直接列表，不强画生态 |

For the remaining task rows above, preserve their stated numeric/relationship contracts; a new combination outside the detailed cases requires its own design record and render review. Select a matching case and inspect that case's actual HTML/preview, rather than choosing an arbitrary example for the entire deck. Record missing inputs explicitly; a component being in the gallery does not make it applicable.

## Select visual relationships

Keep the theme’s canvas, typography and palette stable. Determine hierarchy from the page’s objects and reading order before choosing visual devices. A section name and a shared-scope mark perform different jobs; a renderer should expose text and bracket drawing separately.

| Source observation | Relationship and transfer criterion | Contrast |
|---|---|---|
| B02 bottom four metrics share a labelled frame | A bracket can name a common subject/time scope across distinct evidence | B02 upper business relationship is legible through circles and nearby labels, without another section bracket |
| B04 one bracket spans three colored business headers | Shared parent scope above peer categories; color separates the categories | B10 marks only the target side, while drivers retain direct row labels |
| B10 bottom margin/ROE rows are shaded | Fill distinguishes outcomes from the driver rows above | B04 fills category headers instead; placement follows meaning, not the HTML tag |
| B12 paired chart groups and B16 strategy comparisons | Group titles identify independent scopes or comparable categories | A single chart/table can be identified by its title or column labels alone |

For new content, record the shared scope or comparison to be read, then choose alignment, proximity, text hierarchy, lines or fill. Explain what information the chosen device makes visible. Use the simplest sufficient combination; source examples demonstrate choices rather than a compulsory sequence of levels. Source observations above are verified; applying them to a new industry is a design judgment.

Industry tables define columns, row roles and units first. Compact plain column headers with a separator can carry that hierarchy. Introduce a category band or highlighted result only when its role is stated. The Earnings package’s data-row striping belongs to that financial profile; it is not a Bernstein header token.

Review the actual rendered scope of each line/fill against the intended objects. No per-deck count of brackets or filled headers is a quality criterion. Exact source reconstructions retain their observed devices.

## Numeric and relationship contracts

1. Record amount, unit, denominator, period and actual/estimate/goal before selecting shape. Both stock and cumulative fundraising bars must retain their status. Latest quarter and LTM need a visible break from annual periods.
2. A selectively stacked chart requires only known component periods. Gray bars mean totals, never “other”. Do not invent historical components to fill color.
3. A subset shown with a dotted box sits within the parent series. Do not add it to the parent total. B12 source quantifies the latest subset at $2.1bn; earlier dotted heights are not licensed as exact data by this package.
4. A focal stack must reconcile to its source total, including advisory accounts if that is the disclosed scope. Peer fee-earning values remain a separate box row; no double counting.
5. B15 largest bar is visibly interrupted. Other peer bars retain a common linear scale. If using a fully linear alternative, document the adaptation; never compress only one bar invisibly.
6. B16 uses one height-per-percentage-point across all panels. A matched public-market equivalent and private net IRR are not interchangeable return definitions. Preserve sample, dates and cash-flow matching notes.
7. Quantitative donut: segment angle = amount / common total × 360; verify sum, rounding and outside labels. B03 amounts are rounded; centre is approximate total. Do not force exact precision from approximate labels.
8. Business overlap (B02), channel ring (B09), fee cycle (B13), ecosystem ring (B17) are qualitative. Do not infer percentages or equal business sizes from their geometry. B17 has five department sectors, with client types listed inside.
9. Target ranges/floors stay textual. B06 target column is a schematic gradient, not measured 27% or a data series.
10. A source’s superscript must resolve to retained source notes. In new industry content replace source footnotes with actual evidence IDs; never carry GS methodology numbering into unrelated research.

## Reconstruction versus migration

For reference reconstruction, obtain the user's authorized source and retain its evidence and qualifiers. The public examples are new fictional analyses; they do not reproduce original report wording or institutional marks. Source-task descriptions are not proof that every layout has been independently tested. Cover/divider, full legal-note pages, dark theme, DCF and investment-committee conventions are not supplied as implementations.

## Validation

Follow the shared execution instructions. Render every final page; inspect typography, density, labels, tables and visual relationships. The bundled capture tool reports SVG text candidates, not exhaustive HTML clipping or semantic correctness. Final HTML, screenshots and hash must match after corrections.

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
