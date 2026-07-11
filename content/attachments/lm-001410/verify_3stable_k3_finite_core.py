#!/usr/bin/env python3
"""
Exact verifier for the finite core of the 3-stable Kneser graph argument.

Goal
----
For G_n = KG(n,3)_{3-stable}, verify that every hypothetical
(n-7)-coloring for 10 <= n <= 14 contains a star color.

Method
------
1. Enumerate all 3-stable triples on the n-cycle.
2. Enumerate all maximal pairwise-intersecting families as maximal cliques
   of the intersection graph.
3. Remove star families (families with nonempty total intersection).
4. Verify an exact rational fractional-cover dual certificate:
      sum_{A in F} y_A <= 1
   for every maximal non-star family F, while
      sum_A y_A > n-7.
   Hence n-7 non-star color classes cannot cover all vertices.

The certificates are rotation-invariant and depend only on the cyclic gap
multiset of a stable triple.

Dependencies:
    pip install networkx
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from typing import Dict, Iterable, List, Sequence, Tuple

import networkx as nx

Triple = Tuple[int, int, int]
GapType = Tuple[int, int, int]


def cyclic_distance(a: int, b: int, n: int) -> int:
    d = abs(a - b)
    return min(d, n - d)


def stable_triples(n: int, s: int = 3) -> List[Triple]:
    return [
        triple
        for triple in combinations(range(n), 3)
        if all(
            cyclic_distance(a, b, n) >= s
            for a, b in combinations(triple, 2)
        )
    ]


def cyclic_gap_type(triple: Triple, n: int) -> GapType:
    a, b, c = sorted(triple)
    gaps = (b - a, c - b, n - c + a)
    return tuple(sorted(gaps))  # type: ignore[return-value]


def maximal_intersecting_families(
    vertices: Sequence[Triple],
) -> List[List[int]]:
    graph = nx.Graph()
    graph.add_nodes_from(range(len(vertices)))

    vertex_sets = [set(v) for v in vertices]
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if vertex_sets[i] & vertex_sets[j]:
                graph.add_edge(i, j)

    return [list(clique) for clique in nx.find_cliques(graph)]


def is_star_family(
    family: Sequence[int],
    vertices: Sequence[Triple],
) -> bool:
    if not family:
        return False

    common = set(vertices[family[0]])
    for idx in family[1:]:
        common.intersection_update(vertices[idx])
    return bool(common)


CERTIFICATES: Dict[int, Dict[GapType, Fraction]] = {
    11: {
        (3, 3, 5): Fraction(1, 2),
        (3, 4, 4): Fraction(0),
    },
    12: {
        (3, 3, 6): Fraction(1, 8),
        (3, 4, 5): Fraction(1, 8),
        (4, 4, 4): Fraction(1, 4),
    },
    13: {
        (3, 3, 7): Fraction(5, 56),
        (3, 4, 6): Fraction(9, 112),
        (3, 5, 5): Fraction(1, 8),
        (4, 4, 5): Fraction(1, 7),
    },
    14: {
        (3, 3, 8): Fraction(1, 14),
        (3, 4, 7): Fraction(1, 14),
        (3, 5, 6): Fraction(1, 14),
        (4, 4, 6): Fraction(1, 14),
        (4, 5, 5): Fraction(1, 7),
    },
}


def verify_n(n: int) -> dict:
    vertices = stable_triples(n)
    maximal = maximal_intersecting_families(vertices)
    nonstar = [
        family
        for family in maximal
        if not is_star_family(family, vertices)
    ]

    result = {
        "n": n,
        "vertices": len(vertices),
        "maximal_intersecting_families": len(maximal),
        "maximal_nonstar_families": len(nonstar),
        "target_color_count": n - 7,
    }

    if n == 10:
        assert not nonstar
        result["status"] = "all maximal intersecting families are stars"
        return result

    certificate = CERTIFICATES[n]
    weights = [
        certificate[cyclic_gap_type(vertex, n)]
        for vertex in vertices
    ]

    total_weight = sum(weights, Fraction(0))
    maximum_family_weight = max(
        (
            sum((weights[idx] for idx in family), Fraction(0))
            for family in nonstar
        ),
        default=Fraction(0),
    )

    assert maximum_family_weight <= 1
    assert total_weight > n - 7

    result.update(
        {
            "dual_total": str(total_weight),
            "dual_total_float": float(total_weight),
            "maximum_nonstar_family_weight": str(maximum_family_weight),
            "status": "exact dual certificate verified",
        }
    )
    return result


def main() -> None:
    print("Exact finite-core verification")
    print("=" * 40)

    for n in range(10, 15):
        result = verify_n(n)
        print(result)

    print("\nAll finite certificates verified successfully.")


if __name__ == "__main__":
    main()
