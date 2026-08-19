# T Query Runtime v0.1 — Invariants & Failure Modes

## Core invariants

1. **Commit requires provenance**
   \[
   Committed(Q)\Rightarrow CommitRecord(Q)
   \]

2. **Validation-gated commit when required**
   \[
   CP.requiresValidation\Rightarrow(Committed(Q)\Rightarrow Validated(Q))
   \]

3. **Rejected branch cannot commit**
   unless explicitly reopened.

4. **Operator order preservation**
   Without a valid commutation certificate, AST order is immutable under semantic normalization.

5. **Certified merge only**
   Convergent Re-linking may merge branches only with valid query-equivalence evidence.

6. **Observer clocks are independent**
   \[
   \tau_i\neq\tau_j
   \]
   is legal.

7. **Generated != Committed**

8. **Meta-query self-reference barrier**
   Explicit self-reference requires an enabled policy.

9. **Merge provenance preservation**
   Cluster retains all member branch IDs and parent paths.

10. **Committed state is downstream-visible**
    but speculative candidate state must be distinguishable from it.

## Failure modes

- Query False Merge
- Query False Split
- Operator-Sort Semantic Bug
- Semantic Blind Spot
- Semantic Overbranching
- Validation Lag Confusion
- Commit Leak
- Reflection DoS
- Query Frontier Hijack
- Stale Semantic Cache
- Cross-Sort False Merge
