# IB Analysis Slides

[English](../README.md) | 简体中文

**把研究材料变成投行风格的演示：图表可编辑、信息密度高、证据可追溯。**

两个独立 Skill 协作：`ib-analysis-slides` 负责研究材料与投行风格 HTML，`ppt-maker` 负责可编辑 PPTX 和可重建源码。目前已支持高盛，后续将陆续加入更多外资及内地机构。

![文字角色示例：分组标题、对象配色、斜体证据与财务层级](../skills/ib-analysis-slides/banks/goldman/examples/typography/preview.png)
![财务页面示例：可编辑表格与利润驱动](../skills/ib-analysis-slides/banks/goldman/examples/financial/preview.png)

预览数据均为虚构。本项目独立开发，与高盛无隶属关系，亦未获得其背书。

## 支持的机构风格

已勾选为已支持，未勾选为待支持；暂无具体上线时间。

- [x] 高盛 · Goldman Sachs
- [ ] 摩根大通 · J.P. Morgan
- [ ] 摩根士丹利 · Morgan Stanley
- [ ] 美国银行 · Bank of America
- [ ] 花旗 · Citi
- [ ] 瑞银 · UBS
- [ ] 巴克莱 · Barclays
- [ ] 中金公司 · CICC
- [ ] 中信证券 · CITIC Securities
- [ ] 华泰证券 · Huatai Securities

## 安装

下载[最新版本](https://github.com/hssqz/ib-analysis-slides/releases/latest)：

- **只需要 HTML**：安装完整的 `ib-analysis-slides` 文件夹。
- **还需要 PPTX**：同时安装完整的 `ppt-maker` 文件夹，在其中执行 `npm ci --ignore-scripts`（Node20+、Python3.10+）。

两者可独立安装。[PowerPoint 配置与衔接](pptx/workflow.md)说明运行依赖、交付内容与旧版差异。

如需使用附带的截图工具，请查看[配置说明](../skills/ib-analysis-slides/references/execution.md)。

## 使用

附上研究材料，然后告诉 Agent：

```text
使用 $ib-analysis-slides，把这份报告做成 5 页高盛风格的英文演示，
交付可编辑的 HTML。
```

确认 HTML 后，再告诉 Agent：

```text
使用 $ppt-maker，按已确认的 HTML 制作可编辑 PPTX，
保留内容、布局和高盛字体层级，同时交付可重建的源码项目。
```

公开版使用 PptxGenJS，按需要生成原生文本、表格、形状与图表；图片仍是图片，图表编辑范围随交付说明。不承诺任意 HTML 自动无损转换。

![实际 PPTX 渲染：分析页、财务页与原生图表](../skills/ppt-maker/examples/preview.png)

[下载可编辑 PPTX 示例](https://github.com/hssqz/ib-analysis-slides/releases/download/v0.8.0/ppt-maker-example.pptx).

## 能力范围与贡献

目前支持高盛风格的投资者演示，具体能力和边界见版本说明。

[发布与验证记录](release.md)说明已验证的能力和剩余限制；[贡献指南](contributing.md)介绍如何在同一个 Skill 中新增机构风格。如果对你有帮助，欢迎点个 Star，让更多人发现这个项目。

## 许可证

仓库中的原创代码、指令和虚构示例采用 [MIT](../LICENSE) 许可证。机构名称仅用于标识所研究的风格，不授予任何商标权利。仓库不包含机构原始报告、报告截图、标识、商业字体或旧版镜像编辑器/WASM。PptxGenJS 及其依赖保留各自许可证，见[后端来源说明](../skills/ppt-maker/references/provenance.md)。请使用你有权使用的研究材料。
