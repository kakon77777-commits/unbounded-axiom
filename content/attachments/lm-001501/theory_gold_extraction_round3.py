from __future__ import annotations

"""
Round 3 prototype: theory-gold admission and creative regeneration.

Core principles
---------------
1. Interestingness is not truth.
2. Admission is class-relative: epistemic, research, methodological,
   negative/diagnostic, and creative residuals have different gates.
3. A failed theory can remain useful as data, a countermodel, or a
   generator without becoming evidence for its original conclusion.
4. Failed uniqueness should be transformed into solution-space
   classification.
5. Invalid implication should be transformed into minimal-premise search.
6. The toy verifier exhaustively checks all 64 simple labeled graphs on
   four vertices.
"""

from itertools import combinations, permutations
from typing import Iterable
import math


def edge(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def all_graphs(n: int) -> Iterable[set[tuple[int, int]]]:
    possible = [edge(u, v) for u, v in combinations(range(n), 2)]
    for mask in range(1 << len(possible)):
        yield {possible[i] for i in range(len(possible)) if mask & (1 << i)}


def adjacency(n: int, edges: set[tuple[int, int]]) -> dict[int, set[int]]:
    out = {i: set() for i in range(n)}
    for u, v in edges:
        out[u].add(v)
        out[v].add(u)
    return out


def connected(n: int, edges: set[tuple[int, int]]) -> bool:
    a = adjacency(n, edges)
    seen = {0}
    stack = [0]
    while stack:
        x = stack.pop()
        for y in a[x]:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return len(seen) == n


def degree_sequence(n: int, edges: set[tuple[int, int]]) -> tuple[int, ...]:
    a = adjacency(n, edges)
    return tuple(sorted(len(a[i]) for i in range(n)))


def isomorphic(n: int, ea: set[tuple[int, int]], eb: set[tuple[int, int]]) -> bool:
    ebn = {edge(u, v) for u, v in eb}
    for p in permutations(range(n)):
        if {edge(p[u], p[v]) for u, v in ea} == ebn:
            return True
    return False


if __name__ == "__main__":
    n = 4
    p4 = {edge(0, 1), edge(1, 2), edge(2, 3)}
    universe = list(all_graphs(n))

    def A(g): return len(g) == 3 and connected(n, g)
    def B(g): return isomorphic(n, g, p4)
    def M(g): return max(degree_sequence(n, g)) <= 2

    print("Original implication A -> B:",
          all(not A(g) or B(g) for g in universe))
    print("Repaired implication A and M -> B:",
          all(not (A(g) and M(g)) or B(g) for g in universe))
