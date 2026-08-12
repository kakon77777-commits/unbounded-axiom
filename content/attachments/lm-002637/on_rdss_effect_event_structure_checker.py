from dataclasses import dataclass
from typing import FrozenSet, Tuple, Dict

@dataclass(frozen=True)
class GES:
    events: FrozenSet[str]
    conflict_pairs: FrozenSet[FrozenSet[str]]
    enables: Dict[str, Tuple[FrozenSet[str], ...]]

    def consistent(self,c):
        return all(not pair.issubset(c) for pair in self.conflict_pairs)

    def enabled(self,c,e):
        if e in c or not self.consistent(c|frozenset({e})): return False
        return any(a.issubset(c) for a in self.enables.get(e,(frozenset(),)))

    def configs(self):
        q=[frozenset()]; seen={frozenset()}
        while q:
            c=q.pop()
            for e in self.events:
                if self.enabled(c,e):
                    nc=c|frozenset({e})
                    if nc not in seen: seen.add(nc); q.append(nc)
        return seen

def demo():
    es=GES(
        frozenset({"a","b","c"}),frozenset(),
        {"a":(frozenset(),),"b":(frozenset(),),
         "c":(frozenset({"a"}),frozenset({"b"}))}
    )
    cs=es.configs()
    assert frozenset({"a","c"}) in cs
    assert frozenset({"b","c"}) in cs

    conflict=GES(
        frozenset({"a","b"}),
        frozenset({frozenset({"a","b"})}),
        {"a":(frozenset(),),"b":(frozenset(),)}
    )
    assert frozenset({"a","b"}) not in conflict.configs()
    return True

if __name__=="__main__":
    print("event_structure_regressions_pass =",demo())
