# LIFECYCLE_PROTOCOL — GCORF-04 v0.1

## Transition protocol

1. Identify current state
2. Select meta-operator
3. Type / domain / license check
4. Protected invariant check
5. Resource bound check
6. Execute transition
7. Compute progress vector
8. Determine legal status
9. Determine progress status
10. Record residuals
11. Commit / Reject / Rollback / Reopen

## Progress statuses

- progress
- tradeoff
- no_progress
- regression
- unknown

## Stable-state reopening triggers

- new counterexample
- observer disagreement
- metric drift
- new domain
- new tool
- new bottom-space
- license conflict
- composition failure

## Meta-rule mutation

Requires:
- LegalMeta
- ProgressMeta
- provenance
- protected invariants
- rollback route
- independent audit
