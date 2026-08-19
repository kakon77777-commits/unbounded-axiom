# Methodology Notes — NS Proof-Space Sampling Observatory v0.1

## Scope

This is a corpus-structure instrument, not a mathematical correctness verifier. It is designed to test whether a long AI-assisted research corpus exhibits measurable transition from route novelty to revisit, confluence, and higher-order resampling.

## Corpus classification

Exact-byte SHA-256 deduplication is applied to Markdown files recursively discovered inside nested ZIPs. Artifact types are classified by filename/title conventions. The `paper` class excludes standard package metadata and research-process checkpoints/roadmaps/handoffs/audits.

## Semantic quotient proxy

v0.1 uses two deliberately transparent proxies:

1. TF-IDF cosine similarity over normalized filename/title route descriptors;
2. a controlled concept-family dictionary applied only to filename/title surfaces.

Full bodies are *not* used for route similarity because cumulative checkpoints and inherited summaries would artificially inflate similarity.

## Reconstructed order

Series and internal paper numbers define a deterministic route order. It is useful for trajectory analysis but must not be read as an exact historical timestamp order.

## Higher-order evidence

Full bodies are used only for explicit marker detection such as `second-order`, `higher-order`, `all-order`, `confluence`, `recurrence`, and `no-go`. Those markers do not by themselves prove semantic higher-order structure; they are evidence candidates for audit.

## Sampling tiers

$T_1$ through $T_X$ are empirical labels. $T_X$ means "higher/all-order or family-level saturation evidence" and is not a claim of literal transfinite or categorical order.

## Known failure modes

- lexical overlap may merge mathematically distinct ideas;
- synonymous concepts may fail to merge;
- broad concept families may overstate confluence;
- reconstructed order may differ from actual conversation chronology;
- generated mathematical statements may be incorrect despite structural recurrence.

v0.2 should add theorem/lemma extraction and canonical obstruction IDs.
