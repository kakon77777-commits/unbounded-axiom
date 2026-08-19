# T Query Runtime v0.1 — Architecture

```mermaid
flowchart LR
    I[Input / Seed T] --> C[Query Compiler]
    C --> AST[Typed Ordered AST]
    AST --> E[Speculative Expansion]
    E --> FA[AI Frontier]
    E --> FC[Solver/Computer Frontier]
    E --> FH[Human Frontier]
    FA --> CRL[Convergent Re-linking / 收連]
    FC --> CRL
    FH --> CRL
    CRL --> V[Validation / Review]
    V --> K{Commit Policy}
    K -->|commit| S[Committed Semantic State]
    K -->|reject| R[Rejected / Archived Branch]
    K -->|need more| M[Meta-Query Expansion]
    M --> E
    S --> N[Next Query / Action / T']
```

## Core chain

\[
NaturalInput
\rightarrow
TypedAST
\rightarrow
SpecExpand
\rightarrow
AsyncFrontiers
\rightarrow
Compute
\rightarrow
Validate
\rightarrow
CRL
\rightarrow
Commit
\]

## Meta-chain

\[
Q
\rightarrow
Inspect(Q)
\rightarrow
SpecMetaExpand(Q)
\rightarrow
Validate
\rightarrow
CRL
\rightarrow
Commit(nextQ)
\]
