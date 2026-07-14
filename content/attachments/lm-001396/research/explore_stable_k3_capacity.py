#!/usr/bin/env python3
"""Explore non-star intersecting capacities in s-stable 3-set systems.

This is an exploratory, exact finite program.  It does not prove an infinite
formula.  For each selected `(s, n)` it:

1. enumerates the 3-stable triples on the n-cycle;
2. enumerates maximal intersecting families by Bron--Kerbosch on their
   intersection graph;
3. reports the largest non-star family; and
4. compares it with the type-2 pair-ray candidate `3n - 10s + 2`.

The candidate comes from three pair-rays based at cyclic gaps `(s, s, n-2s)`:
two kernel pairs have forbidden-neighborhood size `3s-1`, one has size
`4s-2`, and the common kernel triple is counted three times.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from typing import Iterator, Sequence

Triple = tuple[int, int, int]


def cyclic_distance(n: int, a: int, b: int) -> int:
    difference = abs(a - b)
    return min(difference, n - difference)


def stable_triples(n: int, s: int) -> list[Triple]:
    return [
        triple
        for triple in combinations(range(n), 3)
        if all(cyclic_distance(n, left, right) >= s for left, right in combinations(triple, 2))
    ]


def is_nonstar(family: Sequence[int], vertices: Sequence[Triple]) -> bool:
    if not family:
        return False
    common = set(vertices[family[0]])
    for index in family[1:]:
        common.intersection_update(vertices[index])
    return not common


def maximal_cliques(adjacency: dict[int, set[int]]) -> Iterator[tuple[int, ...]]:
    """Yield all maximal cliques using Bron--Kerbosch with pivoting."""

    def expand(
        chosen: set[int], possible: set[int], excluded: set[int]
    ) -> Iterator[tuple[int, ...]]:
        if not possible and not excluded:
            yield tuple(sorted(chosen))
            return

        pivot_domain = possible | excluded
        pivot = max(
            pivot_domain,
            key=lambda node: len(possible & adjacency[node]),
            default=None,
        )
        blocked = adjacency[pivot] if pivot is not None else set()

        for node in list(possible - blocked):
            yield from expand(
                chosen | {node},
                possible & adjacency[node],
                excluded & adjacency[node],
            )
            possible.remove(node)
            excluded.add(node)

    yield from expand(set(), set(adjacency), set())


def intersection_graph(vertices: Sequence[Triple]) -> dict[int, set[int]]:
    adjacency = {index: set() for index in range(len(vertices))}
    vertex_sets = [set(triple) for triple in vertices]
    for left in range(len(vertices)):
        for right in range(left + 1, len(vertices)):
            if vertex_sets[left] & vertex_sets[right]:
                adjacency[left].add(right)
                adjacency[right].add(left)
    return adjacency


def type2_pair_ray_family(n: int, s: int, vertices: Sequence[Triple]) -> list[Triple] | None:
    kernel = (0, s, 2 * s)
    if kernel[-1] >= n:
        return None
    if not all(cyclic_distance(n, left, right) >= s for left, right in combinations(kernel, 2)):
        return None

    pairs = {frozenset(pair) for pair in combinations(kernel, 2)}
    return [
        triple
        for triple in vertices
        if any(pair <= set(triple) for pair in pairs)
    ]


def analyse(n: int, s: int) -> dict[str, object]:
    vertices = stable_triples(n, s)
    adjacency = intersection_graph(vertices)

    maximal_count = 0
    nonstar_count = 0
    maximum_nonstar: tuple[int, ...] = ()

    for family in maximal_cliques(adjacency):
        maximal_count += 1
        if is_nonstar(family, vertices):
            nonstar_count += 1
            if len(family) > len(maximum_nonstar):
                maximum_nonstar = family

    candidate = type2_pair_ray_family(n, s, vertices)
    candidate_size = len(candidate) if candidate is not None else None
    candidate_is_nonstar = (
        is_nonstar(
            tuple(vertices.index(triple) for triple in candidate),
            vertices,
        )
        if candidate is not None
        else None
    )

    return {
        "s": s,
        "n": n,
        "stable_triple_count": len(vertices),
        "maximal_intersecting_family_count": maximal_count,
        "maximal_nonstar_family_count": nonstar_count,
        "maximum_nonstar_size": len(maximum_nonstar),
        "maximum_nonstar_witness": [vertices[index] for index in maximum_nonstar],
        "type2_pair_ray_size": candidate_size,
        "type2_pair_ray_is_nonstar": candidate_is_nonstar,
        "type2_linear_candidate": 3 * n - 10 * s + 2,
    }


def parse_case(text: str) -> tuple[int, int]:
    try:
        s_text, n_text = text.split(":", maxsplit=1)
        return int(s_text), int(n_text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("cases must have the form s:n") from exc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "cases",
        nargs="*",
        type=parse_case,
        default=[(3, 9), (3, 10), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15)],
        help="finite cases as s:n; default is the existing s=3 finite core",
    )
    parser.add_argument("--json", action="store_true", help="emit machine-readable output")
    arguments = parser.parse_args()

    results = [analyse(n=n, s=s) for s, n in arguments.cases]
    if arguments.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    for result in results:
        print(
            "s={s}, n={n}: vertices={stable_triple_count}, max_nonstar={maximum_nonstar_size}, "
            "type2={type2_pair_ray_size}, linear_candidate={type2_linear_candidate}, "
            "maximal_families={maximal_intersecting_family_count}".format(**result)
        )


if __name__ == "__main__":
    main()
