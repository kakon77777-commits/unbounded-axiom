# CDI Runtime + AIVS — Engineering Specification v0.1

**Status:** IMPLEMENTABLE MVP / synthetic core tested  
**Date:** 2026-08-10  
**Python:** 3.11+  
**Dependencies:** Python standard library only  
**Primary OS target:** Windows 10/11  
**Current test environment:** synthetic, non-Windows container  
**Integration target:** `mssp-game-computer-runtime-mvp` v0.8.x

---

# 1. Build Order

Do **not** start by writing an AI that rewrites a game binary.

Implement in this order:

```text
M0 Core State
→ M1 Windows Evidence Import
→ M2 Serialization Advisor
→ M3 Source-visible Shadow
→ M4 Game GEC
→ M5 Low-risk Promotion
→ M6 Live AIVS
```

---

# 2. Directory Layout

```text
CDI_AIVS_series_paper06/
├─ 06_CDI_Runtime_AIVS_工程架構協議與MVP_v0.1.md
├─ CDI_Runtime_MVP_spec_v0.1.md
├─ LOCAL_AI_HANDOFF.md
├─ SERIES_FINAL_INDEX_6of6.md
├─ 06_source_notes_2026-08-10.md
├─ README.md
├─ schemas/
│  ├─ sqlite_schema.sql
│  ├─ vertical_sync_packet.schema.json
│  ├─ compute_candidate.schema.json
│  ├─ paradigm_profile.schema.json
│  └─ game_equivalence_contract.schema.json
├─ examples/
│  ├─ runtime.example.json
│  └─ scenario.game.example.json
├─ src/
│  └─ cdi_runtime_mvp.py
└─ tests/
   ├─ smoke_test.py
   ├─ MVP_SMOKE_TEST.json
   └─ cdi_smoke.db
```

---

# 3. Runtime Ports

Define conceptual ports even if v0.1 uses one Python process:

```text
EvidencePort
PersistencePort
RelayDecisionPort
GovernorDecisionPort
CandidatePort
FencePort
RoutePort
BenchmarkPort
GameStatePort
```

---

# 4. Evidence Adapter Contract

Normalized event:

```json
{
  "event_type": "cpu.region",
  "scope": "npc.paths",
  "timestamp": "...",
  "run_id": "...",
  "payload": {},
  "evidence_ref": "..."
}
```

MVP accepts generic JSONL.

Future adapters:

- `WpaCsvAdapter`
- `EtwRealtimeAdapter`
- `PixTimingAdapter`
- `VtuneCsvAdapter`
- `MsspDmsAdapter`

---

# 5. Windows Collection v0.1

Official-tool-first:

```powershell
wpr -start GeneralProfile -filemode
# reproduce benchmark
wpr -stop "cdi_trace.etl" "CDI capture"
```

Then export selected WPA tables:

```powershell
wpaexporter.exe -i "cdi_trace.etl" `
  -profile "<your-profile>.wpaProfile" `
  -outputfolder "wpa_export"
```

Production work must define a CDI `.wpaProfile` and WPR profile.

---

# 6. Why Not Native ETW First?

Native ETW is a later adapter.

The current research uncertainty is not “can Windows emit events?” It can.

The research uncertainty is:

```text
trace
→ causal region
→ serialization finding
→ candidate route
→ equivalence
→ promotion
```

Validate that first.

---

# 7. State Model

Run state:

```json
{
  "epoch": 1,
  "topology_version": 1,
  "policy_version": 1,
  "current_state_version": 0
}
```

These versions MUST NOT be merged.

---

# 8. Candidate Contract

Every candidate must carry at least:

```text
input_state_version
read_keys
write_keys
epoch
topology_version
policy_version
effect_class
idempotency_key
authority_scope/fencing_token when applicable
```

---

# 9. Relevant Conflict Algorithm

Given candidate read set `R` and changed keys since read version `ΔW`:

```text
if R ∩ ΔW != ∅:
    reject relevant_state_conflict
else:
    version mismatch may continue
```

This is deliberately stronger than `if version changed: reject everything`.

---

# 10. Commit Validation Order

Use cheap deterministic checks first:

```text
epoch
→ topology
→ policy
→ dependency status
→ invariant
→ effect barrier
→ fencing
→ relevant conflict
→ semantic AI only if unresolved
```

---

# 11. AIVS Regimes

MVP:

```text
R0 < 0.25
R1 < 0.50
R2 < 0.75
ESCALATE >= 0.75
```

Pressure is synthetic weighted mean of:

```text
anomaly
drift
conflict
uncertainty
risk
novelty
```

This formula is a placeholder policy, not a learned truth.

---

# 12. Relay Policy

Default actions:

```text
R0 → NOOP / machine check
R1 → inspect local evidence
R2 → hold candidate / deeper verifier
ESCALATE → governor
```

---

# 13. Governor Policy

Governor handles:

```text
cross-domain conflict
topology mutation
policy mutation
global route promotion
high-risk external effect
repeated relay failure
```

---

# 14. Paradigm Profile

Do not require full 72 classification for every region.

Progressive:

```text
S/J/P/R
→ B/U/O if needed
→ L=F/K/Q if needed
→ modifiers if needed
```

Allow:

```text
UNKNOWN
HYBRID
KEEP_ORIGINAL
```

as runtime sentinels.

---

# 15. Route Candidate

A route candidate is not active until:

```text
feasible
→ shadow
→ equivalent
→ faster / otherwise useful
→ promotion receipt
```

---

# 16. Game Equivalence Contract

At minimum define:

```text
state fields
RNG policy
event ordering policy
numeric tolerance
required shadow runs
minimum speedup
```

---

# 17. Game Epochs

Do not equate frame and simulation tick.

Future adapter:

```text
sim_epoch
render_epoch
asset_epoch
network_epoch
```

---

# 18. MSSP Integration

Current MSSP is semantic/control evidence, not performance profiling.

Preferred bridge:

```text
MSSP DMS / structured events
→ JSONL
→ CDI import-jsonl
```

Later:

```text
shared run_id
shared epoch references
MCP/local transport
```

---

# 19. Smoke Test

Run:

```bash
python tests/smoke_test.py
```

or:

```bash
python src/cdi_runtime_mvp.py smoke --db tests/cdi_smoke.db
```

Expected:

```text
PASS
```

---

# 20. Smoke Assertions

The test MUST fail if any of these stop working:

```text
R0 normal sync
ESCALATE high pressure
valid commit
non-conflicting stale-version commit
relevant stale conflict reject
idempotent retry
stale fencing reject
irreversible speculation reject
equivalent faster shadow promote
non-equivalent faster shadow reject
serialization gap calculation
```

---

# 21. First Windows Milestone

Deliver:

```text
real ETL file
WPA export
normalized JSONL
CDI import
top 20 regions by wall time
thread wait summary
candidate serialization findings
```

No automatic patch yet.

---

# 22. Second Windows Milestone

For source-visible app:

```text
region → source function
finding → candidate patch
build
tests
shadow benchmark
```

---

# 23. First Game Milestone

Pick a source-visible game/simulation satisfying:

```text
Windows buildable
no anti-cheat
repeatable scenario
clear main loop
state probe available
```

Target only one subsystem.

Recommended first candidate:

```text
NPC path batch
asset decoding
read-only UI preprocessing
```

Avoid physics first unless test coverage is excellent.

---

# 24. Promotion Levels

```text
P0 Observe
P1 Advise
P2 Generate Candidate
P3 Shadow
P4 Local Low-Risk Commit
P5 Domain Commit
P6 Adaptive Global Routing
```

Do not skip levels.

---

# 25. Metrics

Performance:

```text
p50/p95/p99
main thread ms
worker utilization
wait time
GPU queue delay
memory
I/O
```

Correctness:

```text
GEC pass
state divergence
RNG divergence
crash
deadlock
rollback
```

AI:

```text
calls
tokens
latency
R0/R1/R2 counts
escalations
false finding
```

Control:

```text
candidate count
commit count
reject reasons
route promotions
fallbacks
```

---

# 26. Acceptance for v0.2

A real Windows observer run is accepted when:

```text
capture reproducible
events normalized
no process mutation required
run persists in DB
at least one serialization finding has evidence refs
```

---

# 27. Acceptance for v0.3

Source-visible optimization accepted when:

```text
build passes
existing tests pass
shadow equivalence passes
p95 not worse
measured speedup > threshold
fallback passes
```

---

# 28. Security Defaults

```text
observer mode by default
no administrator persistence
no anti-cheat target
no arbitrary binary rewrite
no irreversible speculation
AI decisions typed
raw evidence retained
```

---

# 29. Technical Debt Intentionally Deferred

```text
native ETW parser
async multi-process relay
real model connector
JSON Schema runtime validation
Parquet trace store
learned routing controller
GPU auto-codegen
binary rewriting
hard real-time guarantees
```

---

# 30. Engineering Principle

When uncertain:

```text
KEEP_ORIGINAL
```

is a successful decision.

The MVP should optimize **only when it can preserve a credible verification path**.
