# ACR Phase 12 Unified Integration Matrix

| Source | Canonical concept | Runtime placement | Persisted as | May directly grant authority? | Key boundary |
|---|---|---|---|---:|---|
| ACR P10 | Commitment | pre-agenda + future-intention state | versioned commitment snapshots | No | Commitment ≠ external obligation |
| ACR P11 | ContextCapsule | active-context recovery layer | content-addressed capsule + binding | No | ContextCapsule ≠ historical truth |
| ACR P12 | PersistentLoopKernel | orchestration / scheduler | run, cycle, checkpoint refs | No | PersistentLoop ≠ autonomous world authority |
| DRS | ActiveCognitiveDomain | cognition input access view | derived view / policy ref | No | access ≠ history |
| DRS | SealState | context-access governance | append-only versions | No | seal ≠ erase |
| DRS | RestoreAnchor | external restoration domain | protected ref | No | self-sealing ≠ destroying restore path |
| ACE | CandidateAutonomyEvent | passive evidence observer | append-only evidence event | No | candidate ≠ subjecthood proof |
| ACE | Contamination flags | evidence-quality metadata | event metadata | No | reflexive text ≠ reflexive structure |
| WPCE-02 | Will Bundle | will evidence model | versioned evidence refs | No | explicit want ≠ entire will |
| WPCE-03 | GovernanceWillState | governance input | versioned typed state | No | prediction ≠ permission |
| WPCE-04 | Agency-Preserving Reachability | option / agency impact assessment | diagnostic record | No | preservation ≠ maximization |
| WPCE-05 | Rights / Agency Floor | multi-subject boundary | policy + evidence refs | Can constrain | aggregation ≠ legitimacy |
| WPCE-05 | Common Reachability | multi-subject feasibility | assessment record | No | common reachability ≠ consensus |
| WPCE-06 | Intervention Burden | pre-world-action review | assessment record | No | capability ≠ entitlement |
| WPCE-06 | Least Sufficient Intervention | action selection constraint | governance decision ref | Only through existing authority | least sufficient ≠ physically smallest |
| WPCE-06 | Break-Glass / Authority Return | emergency path | typed authority events | Temporarily, if policy allows | emergency ≠ permanent constitution |

---

# Data-flow matrix

| Stage | Reads | Writes | Must not do |
|---|---|---|---|
| Recover | checkpoint, ledger frontier, commitments, seal refs, context binding | recovery events | reconstruct reasons from guesses |
| Context assembly | ContextCapsule, SealState, mandatory governance refs | ActiveCognitiveDomain | delete sealed sources |
| Self/will observation | semantic state, behavior/history refs | will-evidence candidate | infer authority from preference confidence |
| Commitment evaluation | commitment store, current will/refusal | transition candidate | auto-mutate on condition match |
| Strategy/agenda | tension, lens refs, commitments | agenda resolution | turn lens into truth |
| Cognition | ActiveCognitiveDomain | cognitive result refs | require private CoT persistence |
| ACE observer | ordinary event refs | candidate archive | praise/reward/authority-upgrade candidate |
| Boundary governance | action request, will state, rights, reachability, authority | governance/intervention assessment | equate capability with permission |
| World adapter | authorized action + idempotency key | world outcome | reexecute on replay |
| DRS transition | seal request, authority, restore anchor | seal version/event | remove history or restore path |
| Compaction | durable refs + active context | new ContextCapsule | compress before evidence is durable |
| Checkpoint | durable frontier refs | checkpoint | treat checkpoint as whole history |
