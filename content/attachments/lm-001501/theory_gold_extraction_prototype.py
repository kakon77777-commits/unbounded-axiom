"""
Prototype: theory residual extraction and bridge-audit framework.

This script demonstrates:
1. Information loss under projection (beta, gamma) -> gamma.
2. Structural-signature similarity does not prove isomorphism.
3. Dependency-graph blast radius for invalid inference edges.
4. Residual-value scoring for salvageable ideas.
5. A transverse-defect measure that preserves the real-part deviation.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Iterable


class ClaimKind(str, Enum):
    KNOWN = "known theorem/fact"
    DERIVED = "derived claim"
    CONJECTURE = "conjecture"
    ANALOGY = "analogy"
    METHOD = "methodological salvage"
    ERROR = "invalid claim"


@dataclass(frozen=True)
class Claim:
    id: str
    text: str
    kind: ClaimKind
    novelty: float
    testability: float
    transferability: float
    independence: float
    coherence: float

    def salvage_score(self) -> float:
        return (
            0.15 * self.novelty
            + 0.25 * self.testability
            + 0.20 * self.transferability
            + 0.30 * self.independence
            + 0.10 * self.coherence
        )


@dataclass(frozen=True)
class Edge:
    premises: tuple[str, ...]
    conclusion: str
    relation: str
    valid: bool
    preserves: tuple[str, ...] = ()
    loses: tuple[str, ...] = ()


def descendants(start: str, edges: Iterable[Edge]) -> set[str]:
    adjacency: dict[str, set[str]] = {}
    for edge in edges:
        for premise in edge.premises:
            adjacency.setdefault(premise, set()).add(edge.conclusion)

    seen: set[str] = set()
    stack = [start]
    while stack:
        node = stack.pop()
        for nxt in adjacency.get(node, set()):
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return seen


def blast_radius(edge: Edge, edges: Iterable[Edge]) -> int:
    return len({edge.conclusion} | descendants(edge.conclusion, edges))


def transverse_defect(beta: float) -> float:
    return (beta - 0.5) ** 2


def defect_measure(points: list[dict]) -> dict[float, float]:
    out: dict[float, float] = {}
    for p in points:
        gamma = float(p["gamma"])
        out[gamma] = out.get(gamma, 0.0) + transverse_defect(float(p["beta"]))
    return out


if __name__ == "__main__":
    points = [
        {"beta": 0.30, "gamma": 14.0},
        {"beta": 0.50, "gamma": 14.0},
        {"beta": 0.70, "gamma": 14.0},
    ]

    print("Projection values:", [p["gamma"] for p in points])
    print("Transverse-defect measure:", defect_measure(points))

    signature_a = {"symmetry", "critical_parameter", "spectrum", "periodic_orbits"}
    signature_b = {"symmetry", "critical_parameter", "spectrum", "invariant_measure"}
    similarity = len(signature_a & signature_b) / len(signature_a | signature_b)
    print("Signature similarity:", similarity)
    print("Isomorphism proved:", False)
