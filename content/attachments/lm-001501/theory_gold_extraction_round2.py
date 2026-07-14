"""
Round 2 prototype for theory-residual extraction.

Core ideas:
1. Typed dependencies: falsity propagates through justificatory/definitional
   edges, but not through motivational, diagnostic, or illustrative use.
2. Residual independence has semantic, epistemic, and generative dimensions.
3. Bridge certificates separate completeness, validity, and target adequacy.
4. Same coarse structural signature does not imply isomorphism.
5. Countermodels suggest which missing observables should enrich a signature.
"""

from dataclasses import dataclass
from enum import Enum
from itertools import permutations
from typing import Sequence


class DepMode(str, Enum):
    JUSTIFIES = "justifies"
    DEFINES = "defines"
    MOTIVATES = "motivates"
    DIAGNOSES = "diagnoses"
    ILLUSTRATES = "illustrates"


TRUTH_TRANSMITTING = {DepMode.JUSTIFIES, DepMode.DEFINES}


@dataclass(frozen=True)
class Dependency:
    source: str
    target: str
    mode: DepMode
    reliability: float = 1.0


@dataclass(frozen=True)
class Route:
    premises: tuple[str, ...]
    edge_reliabilities: tuple[float, ...] = ()

    def reliability(self) -> float:
        out = 1.0
        for q in self.edge_reliabilities:
            out *= q
        return out


def typed_contamination_closure(
    failed: set[str],
    dependencies: Sequence[Dependency],
) -> set[str]:
    adjacency: dict[str, set[str]] = {}
    for dep in dependencies:
        if dep.mode in TRUTH_TRANSMITTING:
            adjacency.setdefault(dep.source, set()).add(dep.target)

    contaminated = set(failed)
    stack = list(failed)
    while stack:
        node = stack.pop()
        for nxt in adjacency.get(node, set()):
            if nxt not in contaminated:
                contaminated.add(nxt)
                stack.append(nxt)
    return contaminated


def epistemic_independence(
    target: str,
    routes: dict[str, list[Route]],
    failed: set[str],
) -> float:
    target_routes = routes.get(target, [])
    if not target_routes:
        return 1.0
    surviving = [
        route.reliability()
        for route in target_routes
        if failed.isdisjoint(route.premises)
    ]
    return max(surviving, default=0.0)


def canonical_edge(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def isomorphic(
    n: int,
    edges_a: set[tuple[int, int]],
    edges_b: set[tuple[int, int]],
) -> bool:
    normalized_b = {canonical_edge(u, v) for u, v in edges_b}
    for perm in permutations(range(n)):
        mapped = {
            canonical_edge(perm[u], perm[v])
            for u, v in edges_a
        }
        if mapped == normalized_b:
            return True
    return False


if __name__ == "__main__":
    path_p4 = {
        canonical_edge(0, 1),
        canonical_edge(1, 2),
        canonical_edge(2, 3),
    }
    star_k13 = {
        canonical_edge(0, 1),
        canonical_edge(0, 2),
        canonical_edge(0, 3),
    }

    print("Same coarse signature: connected 4-vertex bipartite trees with 3 edges")
    print("Isomorphic:", isomorphic(4, path_p4, star_k13))
    print("Missing observable: degree sequence")
