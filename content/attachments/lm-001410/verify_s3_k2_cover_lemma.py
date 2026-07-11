#!/usr/bin/env python3
"""
Exact finite verifier for the small-r part of the cover lemma used in the
s=3, k=2 stable-Kneser coloring argument.

For a cyclically ordered subset R of size r, let g_i be positive cyclic gaps.
The graph H_N[R] has an edge between selected vertices iff their cyclic
distance in C_N is at least 3. This adjacency depends only on
min(g_i, 3), so every case reduces to a word in {1,2,3}^r.

A "block" is either:
  * a singleton edge, or
  * all three edges of an internal triangle.

The verifier checks that no realizable truncated gap word with 4 <= r <= 8
admits a cover by at most r-4 blocks. Equivalently, every such case needs
at least r-3 blocks.
"""

import itertools
from functools import lru_cache

def realizable_for_N_ge_6(gaps):
    # Symbols 1,2 are exact gaps; symbol 3 means an original gap >= 3.
    # If the truncated total is already >=6, realizable directly.
    # If a 3 occurs, inflate that original gap as needed to reach N>=6.
    return sum(gaps) >= 6 or 3 in gaps

def graph_edges_from_truncated_gaps(gaps):
    r = len(gaps)
    N = sum(gaps)
    pos = [0]
    for g in gaps[:-1]:
        pos.append(pos[-1] + g)

    edges = []
    for i in range(r):
        for j in range(i + 1, r):
            d = abs(pos[j] - pos[i])
            d = min(d, N - d)
            if d >= 3:
                edges.append((i, j))
    return edges

def can_cover_with_at_most_t_blocks(r, edges, t):
    edges = sorted(tuple(sorted(e)) for e in edges)
    m = len(edges)
    if m == 0:
        return True

    idx = {e: i for i, e in enumerate(edges)}
    edge_set = set(edges)

    blocks = [1 << i for i in range(m)]  # singleton blocks

    for tri in itertools.combinations(range(r), 3):
        pairs = [tuple(sorted(p)) for p in itertools.combinations(tri, 2)]
        if all(p in edge_set for p in pairs):
            mask = 0
            for p in pairs:
                mask |= 1 << idx[p]
            blocks.append(mask)

    by_edge = [[] for _ in range(m)]
    for mask in blocks:
        for i in range(m):
            if (mask >> i) & 1:
                by_edge[i].append(mask)

    full = (1 << m) - 1

    @lru_cache(None)
    def dfs(uncovered, remaining):
        if uncovered == 0:
            return True
        if remaining == 0:
            return False

        # Each block covers at most three uncovered edges.
        if uncovered.bit_count() > 3 * remaining:
            return False

        candidates = [i for i in range(m) if (uncovered >> i) & 1]
        pivot = min(
            candidates,
            key=lambda j: sum(1 for b in by_edge[j] if b & uncovered),
        )

        for block in by_edge[pivot]:
            if dfs(uncovered & ~block, remaining - 1):
                return True
        return False

    return dfs(full, t)

def main():
    summary = {}
    counterexamples = []

    for r in range(4, 9):
        checked = 0
        for gaps in itertools.product((1, 2, 3), repeat=r):
            if not realizable_for_N_ge_6(gaps):
                continue

            checked += 1
            edges = graph_edges_from_truncated_gaps(gaps)

            # A counterexample to tau(R) >= r-3 would have a cover
            # using at most r-4 blocks.
            if can_cover_with_at_most_t_blocks(r, edges, r - 4):
                counterexamples.append(
                    {
                        "r": r,
                        "gaps": gaps,
                        "edge_count": len(edges),
                        "block_budget": r - 4,
                    }
                )
                break

        summary[r] = checked

    print("checked patterns:", summary)
    print("counterexamples:", counterexamples)

    assert not counterexamples

if __name__ == "__main__":
    main()
