# Contributing

Use one entrypoint and one shared evidence/execution workflow. Add an institution under `skills/ib-analysis-slides/banks/<bank>/` only when actual rules and examples are ready; do not add empty future-bank scaffolding.

A useful profile specifies its source/version, visual roles, analytical relationships, evidence requirements and adaptation limits. Provide fictional or otherwise redistributable examples with declared input and sources. Keep quantitative composition distinct from qualitative relationships. Do not upload bank source PDFs, copied report screenshots, proprietary research, institution logos or private machine paths.

Update routing and the local CLAUDE.md map. Check links and static examples with `npm test`; run `npm run test:capture` after helper changes. Render every changed example, inspect the result, and replace only its associated preview. Record actual coverage: automatic choice and explicitly requested rendering are separate outcomes.

For issue reports, include profile, minimal nonsensitive input, expected/actual behavior, rendered screenshot and environment. Never include secrets or third-party material you cannot share. Existing accepted outputs and failed tests should not be silently relabelled as passing.

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
