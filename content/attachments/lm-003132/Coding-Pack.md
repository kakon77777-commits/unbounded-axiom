# WDC Runtime v0.1 — Coding Pack

This pack is the first implementation-facing split of the World-Domain Cognitive Runtime v0.1 Technical Whitepaper.

Files:

- `ARCHITECTURE.md` — planes, modules, invariants, data/control flow, local/distributed evolution.
- `SCHEMA.md` — canonical entities, tables, enums, storage and versioning rules.
- `EVENTS.md` — event envelope, scope/history firewall, reliability and provenance.
- `WORLD_ADAPTER.md` — backend protocol, checkpoint/fork capability contract, sandbox/resource rules.
- `MVP_PLAN.md` — local-first implementation phases, tests, Branching Grid demo and definition of done.

Permanent engineering boundaries:

```text
Future Candidate != Runnable World != Actual Future
WorldSpec != WorldRun
World-Local Event != Parent-Real Historical Fact
World Count != Independent Evidence Count
Worth Computing != Worth Believing != Worth Deploying
```

Recommended next action: create the repository skeleton and implement Phase 0–2 with tests before adding distributed infrastructure.
