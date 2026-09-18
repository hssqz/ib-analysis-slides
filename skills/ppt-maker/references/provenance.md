# Implementation and distribution provenance

Public ppt-maker 0.8 is a new JavaScript/Python implementation using [PptxGenJS](https://github.com/gitbrent/PptxGenJS), pinned to4.0.1. Its npm package declares MIT; the installed package contains its upstream license. The lockfile overrides transitive `image-size` to2.0.4 to avoid the image-parser denial-of-service advisories affecting earlier versions. Real PNG embedding and export are tested with this resolution. Transitive dependencies keep their own licenses. `npm ci` installs them separately; node_modules is not redistributed in the skill ZIP.

The user's previous local ppt-maker used a PPTD/WASM/editor chain derived from open-kimi-ppt-skill. On2026-09-18 its [upstream repository](https://github.com/Binaryify/open-kimi-ppt-skill) was archived and stated that contents had been cleared for copyright reasons. This release does not copy that editor, WASM, upstream runtime scripts, format manual, font pack or slide templates. It does not route users to a mirror of the removed code. The previous local installation is not modified.

Workflow requirements and original design decisions are re-expressed for this backend. The worked example is authored here using fictional evidence already published in ib-analysis-slides plus separately labeled synthetic data. No Webis brand imagery, original bank report, report screenshot, proprietary font or private path is included. The institution-profile skill remains separate and retains its own provenance.

Legacy PPTD projects and the old browser editor are not compatible interfaces of public0.8. Deliver editable PPTX and JavaScript source. Do not represent the replacement as preserving every feature of the retired backend. New integration changes require source, native-object and actual-render review.

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
