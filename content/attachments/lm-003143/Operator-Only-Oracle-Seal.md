# Operator-only oracle seal

Do not mount or index this directory in any Agent workspace.

For a real benchmark, place hidden truth / scoring labels here only after the benchmark is frozen. Runtime Agents must never read it.

Required sequence:
1. freeze benchmark + hash;
2. seal operator-only oracle;
3. execute all four arms;
4. freeze proof and observer ledgers + hashes;
5. only then run post-freeze oracle scoring;
6. append `PostFreezeScored` events to a **derived scoring ledger**, not to the frozen raw observer ledger.
