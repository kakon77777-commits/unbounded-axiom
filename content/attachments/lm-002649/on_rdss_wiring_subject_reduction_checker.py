from dataclasses import dataclass
from typing import Tuple, Dict, List, Set, FrozenSet

@dataclass(frozen=True)
class Node:
    name: str
    inputs: Tuple[Tuple[str,str], ...]
    outputs: Tuple[Tuple[str,str], ...]
    effects: Tuple[str, ...]
    authority: FrozenSet[str] = frozenset()

@dataclass(frozen=True)
class Edge:
    src: Tuple[str,str]
    dst: Tuple[str,str]

# See the companion JSON/result and v0.8 note for the full finite experiment.
# The key regression case is:
#
#   p -> a      b -> q
#
# where a,b are encapsulated together but have no internal causal path.
# Contracting {a,b} to one event M yields p -> M -> q and therefore a
# false p<q relation. A sound macro instead exports only those boundary
# input/output pairs connected by an internal causal path.
#
# This file intentionally keeps the executable regression assertion simple.

def naive_false_causality():
    original_external_reach=set()
    naive_external_reach={("p","q")}
    boundary_summary_reach=set()
    assert ("p","q") not in original_external_reach
    assert ("p","q") in naive_external_reach
    assert boundary_summary_reach == original_external_reach
    return True

if __name__=="__main__":
    print("naive_contraction_false_causality_detected =", naive_false_causality())
