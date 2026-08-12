from dataclasses import dataclass
from itertools import combinations, permutations
from typing import Dict, FrozenSet, Tuple, Set
import json

Event = str
Config = FrozenSet[Event]
MapTuple = Tuple[Tuple[Event, Event], ...]
Triple = Tuple[Config, MapTuple, Config]

@dataclass(frozen=True)
class EProfile:
    label: str
    typ: str = "Effect"
    auth: Tuple[str, ...] = ()
    residual: Tuple[str, ...] = ()

@dataclass
class PES:
    events: Tuple[Event, ...]
    profile: Dict[Event, EProfile]
    causes: Set[Tuple[Event, Event]]
    conflicts: Set[FrozenSet[Event]]

    def closure(self) -> Set[Tuple[Event, Event]]:
        reach = set(self.causes)
        changed = True
        while changed:
            changed = False
            new = set(reach)
            for a, b in reach:
                for c, d in reach:
                    if b == c and (a, d) not in new:
                        new.add((a, d))
                        changed = True
            reach = new
        return reach

    def conflict(self, a: Event, b: Event) -> bool:
        return frozenset((a, b)) in self.conflicts

    def config(self, c: Config) -> bool:
        reach = self.closure()
        for a, b in combinations(c, 2):
            if self.conflict(a, b):
                return False
        for a, b in reach:
            if b in c and a not in c:
                return False
        return True

    def configurations(self):
        out = []
        ev = list(self.events)
        for r in range(len(ev) + 1):
            for xs in combinations(ev, r):
                c = frozenset(xs)
                if self.config(c):
                    out.append(c)
        return tuple(out)

    def enabled(self, c: Config, e: Event) -> bool:
        return e not in c and self.config(c | frozenset({e}))

    def enabled_events(self, c: Config):
        return tuple(e for e in self.events if self.enabled(c, e))

def profile_eq(p1: PES, e1: Event, p2: PES, e2: Event) -> bool:
    return p1.profile[e1] == p2.profile[e2]

def is_history_iso(p1: PES, c1: Config, p2: PES, c2: Config, m: MapTuple) -> bool:
    if len(c1) != len(c2) or len(m) != len(c1):
        return False
    d = dict(m)
    if set(d) != set(c1) or set(d.values()) != set(c2):
        return False
    if len(set(d.values())) != len(d):
        return False
    for a, b in d.items():
        if not profile_eq(p1, a, p2, b):
            return False
    r1, r2 = p1.closure(), p2.closure()
    for a, a2 in permutations(c1, 2):
        if ((a, a2) in r1) != ((d[a], d[a2]) in r2):
            return False
    return True

def all_history_isos(p1: PES, c1: Config, p2: PES, c2: Config):
    if len(c1) != len(c2):
        return tuple()
    c1s, c2s = sorted(c1), sorted(c2)
    out = []
    for perm in permutations(c2s):
        m = tuple(zip(c1s, perm))
        if is_history_iso(p1, c1, p2, c2, m):
            out.append(m)
    return tuple(out)

def all_triples(p1: PES, p2: PES) -> Set[Triple]:
    out = set()
    for c1 in p1.configurations():
        for c2 in p2.configurations():
            for m in all_history_isos(p1, c1, p2, c2):
                out.add((c1, m, c2))
    return out

def extend_map(m: MapTuple, e1: Event, e2: Event) -> MapTuple:
    return tuple(sorted(tuple(m) + ((e1, e2),)))

def hp_gfp(p1: PES, p2: PES):
    R = all_triples(p1, p2)
    changed = True
    while changed:
        changed = False
        remove = []
        for c1, m, c2 in R:
            ok = True
            for e1 in p1.enabled_events(c1):
                matched = False
                for e2 in p2.enabled_events(c2):
                    if not profile_eq(p1, e1, p2, e2):
                        continue
                    t = (
                        c1 | frozenset({e1}),
                        extend_map(m, e1, e2),
                        c2 | frozenset({e2}),
                    )
                    if t in R:
                        matched = True
                        break
                if not matched:
                    ok = False
                    break
            if not ok:
                remove.append((c1, m, c2))
                continue
            for e2 in p2.enabled_events(c2):
                matched = False
                for e1 in p1.enabled_events(c1):
                    if not profile_eq(p1, e1, p2, e2):
                        continue
                    t = (
                        c1 | frozenset({e1}),
                        extend_map(m, e1, e2),
                        c2 | frozenset({e2}),
                    )
                    if t in R:
                        matched = True
                        break
                if not matched:
                    ok = False
                    break
            if not ok:
                remove.append((c1, m, c2))
        if remove:
            changed = True
            for t in remove:
                R.discard(t)
    return R

def hereditary_subtriple(triple: Triple, sub1: Config):
    c1, m, c2 = triple
    d = dict(m)
    sub2 = frozenset(d[e] for e in sub1)
    mr = tuple(sorted((e, d[e]) for e in sub1))
    return (sub1, mr, sub2)

def hhp_gfp(p1: PES, p2: PES):
    R = all_triples(p1, p2)
    changed = True
    while changed:
        changed = False
        remove = []
        for c1, m, c2 in R:
            ok = True
            c1_list = list(c1)
            for r in range(len(c1_list) + 1):
                for xs in combinations(c1_list, r):
                    s1 = frozenset(xs)
                    st = hereditary_subtriple((c1, m, c2), s1)
                    if p1.config(st[0]) and p2.config(st[2]) and st not in R:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                remove.append((c1, m, c2))
                continue

            for e1 in p1.enabled_events(c1):
                matched = False
                for e2 in p2.enabled_events(c2):
                    if profile_eq(p1, e1, p2, e2):
                        t = (
                            c1 | frozenset({e1}),
                            extend_map(m, e1, e2),
                            c2 | frozenset({e2}),
                        )
                        if t in R:
                            matched = True
                            break
                if not matched:
                    ok = False
                    break
            if not ok:
                remove.append((c1, m, c2))
                continue

            for e2 in p2.enabled_events(c2):
                matched = False
                for e1 in p1.enabled_events(c1):
                    if profile_eq(p1, e1, p2, e2):
                        t = (
                            c1 | frozenset({e1}),
                            extend_map(m, e1, e2),
                            c2 | frozenset({e2}),
                        )
                        if t in R:
                            matched = True
                            break
                if not matched:
                    ok = False
                    break
            if not ok:
                remove.append((c1, m, c2))
        if remove:
            changed = True
            for t in remove:
                R.discard(t)
    return R

def related_maps(R: Set[Triple], c1: Config, c2: Config):
    return [m for a, m, b in R if a == c1 and b == c2]

def demo():
    profiles = {
        "a": EProfile("choice"), "b": EProfile("choice"),
        "ra": EProfile("result"), "rb": EProfile("result"),
        "fa": EProfile("future"), "fb": EProfile("future"),
    }
    conflicts = {
        frozenset({"a","b"}), frozenset({"ra","rb"}), frozenset({"fa","fb"}),
        frozenset({"a","rb"}), frozenset({"a","fb"}),
        frozenset({"ra","b"}), frozenset({"ra","fb"}),
        frozenset({"fa","b"}), frozenset({"fa","rb"}),
    }
    p = PES(
        tuple(profiles), profiles,
        {("a","ra"),("ra","fa"),("b","rb"),("rb","fb")},
        conflicts
    )
    ca, cb = frozenset({"a","ra"}), frozenset({"b","rb"})
    hp, hhp = hp_gfp(p,p), hhp_gfp(p,p)
    return {
        "hp_related": bool(related_maps(hp,ca,cb)),
        "hhp_related": bool(related_maps(hhp,ca,cb)),
        "hp_relation_size": len(hp),
        "hhp_relation_size": len(hhp),
    }

if __name__ == "__main__":
    print(json.dumps(demo(), indent=2))
