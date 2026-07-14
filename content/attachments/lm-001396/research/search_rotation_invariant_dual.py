#!/usr/bin/env python3
"""Search rotation-invariant dual certificates for stable Kneser finite cores.

For fixed `(s, n)`, every 3-stable triple is assigned a non-negative weight
depending only on its cyclic gap multiset.  The linear program maximizes total
vertex weight subject to every maximal non-star intersecting family having
weight at most one.  If the optimum exceeds `n - 2s - 1`, then that finite
core has a weighted star-forcing certificate for the expected lower bound
`chi >= n - 2s`.

Output is numerical evidence only.  A successful floating-point solution must
be rationalized and independently checked before it becomes a certificate.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations

import numpy as np
from scipy.optimize import linprog

from explore_stable_k3_capacity import (
    Triple,
    intersection_graph,
    is_nonstar,
    maximal_cliques,
    stable_triples,
)


def gap_type(triple: Triple, n: int) -> tuple[int, int, int]:
    left, middle, right = sorted(triple)
    return tuple(sorted((middle - left, right - middle, n - right + left)))


def solve(s: int, n: int) -> dict[str, object]:
    vertices = stable_triples(n, s)
    types = sorted({gap_type(vertex, n) for vertex in vertices})
    position = {gap: index for index, gap in enumerate(types)}
    vertex_type = [position[gap_type(vertex, n)] for vertex in vertices]
    total_counts = Counter(vertex_type)

    nonstar_rows: list[list[float]] = []
    nonstar_families: list[tuple[int, ...]] = []
    for family in maximal_cliques(intersection_graph(vertices)):
        if not is_nonstar(family, vertices):
            continue
        row = [0.0] * len(types)
        for index in family:
            row[vertex_type[index]] += 1.0
        nonstar_rows.append(row)
        nonstar_families.append(family)

    objective = np.array([-float(total_counts[index]) for index in range(len(types))])
    result = linprog(
        objective,
        A_ub=np.array(nonstar_rows) if nonstar_rows else None,
        b_ub=np.ones(len(nonstar_rows)) if nonstar_rows else None,
        bounds=[(0, None)] * len(types),
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)

    exact_weights = [
        Fraction(float(weight)).limit_denominator(100_000)
        if abs(weight) > 1e-10
        else Fraction(0)
        for weight in result.x
    ]
    weights = {
        str(gap): float(weight)
        for gap, weight in zip(types, result.x)
        if abs(weight) > 1e-10
    }
    rational_hint = {
        str(gap): str(weight)
        for gap, weight in zip(types, exact_weights)
        if weight
    }
    exact_total = sum(
        (total_counts[index] * exact_weights[index] for index in range(len(types))),
        Fraction(0),
    )
    exact_max_nonstar = max(
        (
            sum((exact_weights[vertex_type[index]] for index in family), Fraction(0))
            for family in nonstar_families
        ),
        default=Fraction(0),
    )
    total = -float(result.fun)
    threshold = n - 2 * s - 1

    return {
        "s": s,
        "n": n,
        "gap_type_count": len(types),
        "maximal_nonstar_family_count": len(nonstar_rows),
        "dual_total": total,
        "target_nonstar_color_count": threshold,
        "strict_star_forcing_margin": total - threshold,
        "nonzero_weights": weights,
        "rational_hints": rational_hint,
        "rational_total": str(exact_total),
        "rational_max_nonstar": str(exact_max_nonstar),
        "rational_certificate_feasible": exact_max_nonstar <= 1,
        "rational_strict_star_forcing": exact_total > threshold,
    }


def parse_case(text: str) -> tuple[int, int]:
    try:
        s_text, n_text = text.split(":", maxsplit=1)
        return int(s_text), int(n_text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("cases must have the form s:n") from exc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("cases", nargs="+", type=parse_case)
    arguments = parser.parse_args()

    for s, n in arguments.cases:
        result = solve(s=s, n=n)
        print(
            "s={s}, n={n}: dual={dual_total:.12g}, q={target_nonstar_color_count}, "
            "margin={strict_star_forcing_margin:.12g}, gap-types={gap_type_count}, "
            "nonstar-families={maximal_nonstar_family_count}".format(**result)
        )
        print("  rational hints:", result["rational_hints"])
        print(
            "  exact check: total={rational_total}, max_nonstar={rational_max_nonstar}, "
            "feasible={rational_certificate_feasible}, forcing={rational_strict_star_forcing}".format(
                **result
            )
        )


if __name__ == "__main__":
    main()
