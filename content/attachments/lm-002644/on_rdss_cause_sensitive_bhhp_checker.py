from dataclasses import dataclass
from typing import FrozenSet, Tuple, Dict, Set, List
from itertools import permutations
import json

Event = str
Witness = FrozenSet[Event]

@dataclass(frozen=True)
class Profile:
    label: str
    typ: str = "Effect"
    auth: Tuple[str, ...] = ()
    residual: Tuple[str, ...] = ()

@dataclass(frozen=True)
class Step:
    event: Event
    witness: Witness
    version: str

@dataclass(frozen=True)
class DHist:
    steps: Tuple[Step, ...]

    @property
    def events(self):
        return frozenset(s.event for s in self.steps)

    def witness_map(self):
        return {s.event: s.witness for s in self.steps}

    def cause_closure(self):
        r={(x,s.event) for s in self.steps for x in s.witness}
        changed=True
        while changed:
            changed=False
            new=set(r)
            for a,b in r:
                for c,d in r:
                    if b==c and (a,d) not in new:
                        new.add((a,d)); changed=True
            r=new
        return r

    def maximal(self):
        r=self.cause_closure()
        return frozenset(
            e for e in self.events
            if not any(a==e for a,_ in r)
        )

@dataclass
class GCEES:
    version: str
    profiles: Dict[Event, Profile]
    enables: Dict[Event, Tuple[Witness, ...]]

    def valid(self,h:DHist):
        occurred=set()
        for s in h.steps:
            if s.version != self.version:
                return False
            if s.event in occurred:
                return False
            if s.event not in self.enables:
                return False
            if s.witness not in self.enables[s.event]:
                return False
            if not s.witness <= occurred:
                return False
            occurred.add(s.event)
        return True

    def next_steps(self,h:DHist):
        occurred=h.events
        out=[]
        for e,alts in self.enables.items():
            if e in occurred:
                continue
            for w in alts:
                if w <= occurred:
                    out.append(Step(e,w,self.version))
        return out

    def histories(self):
        start=DHist(())
        seen={start}; stack=[start]
        while stack:
            h=stack.pop()
            for s in self.next_steps(h):
                nh=DHist(h.steps+(s,))
                if self.valid(nh) and nh not in seen:
                    seen.add(nh); stack.append(nh)
        return tuple(seen)

def realization_isos(g1,h1,g2,h2):
    if len(h1.events)!=len(h2.events):
        return tuple()
    left=sorted(h1.events); right=sorted(h2.events)
    c1=h1.cause_closure(); c2=h2.cause_closure()
    out=[]
    for perm in permutations(right):
        f=dict(zip(left,perm))
        if any(g1.profiles[a] != g2.profiles[f[a]] for a in left):
            continue
        ok=True
        for a in left:
            for b in left:
                if a==b:
                    continue
                if ((a,b) in c1) != ((f[a],f[b]) in c2):
                    ok=False; break
            if not ok:
                break
        if ok:
            out.append(tuple(sorted(f.items())))
    return tuple(out)

def witness_corresponds(h1,h2,m,e1,e2):
    f=dict(m)
    w1=h1.witness_map()[e1]
    w2=h2.witness_map()[e2]
    return frozenset(f[x] for x in w1) == w2

def forward_extensions(g,h):
    out=[]
    for s in g.next_steps(h):
        nh=DHist(h.steps+(s,))
        if g.valid(nh):
            out.append((s,nh))
    return out

def backward_extensions(h):
    out=[]
    for e in h.maximal():
        nh=DHist(tuple(s for s in h.steps if s.event != e))
        out.append((e,nh))
    return out

Triple = Tuple[DHist, Tuple[Tuple[Event,Event],...], DHist]

def all_triples(g1,g2):
    out=set()
    for h1 in g1.histories():
        for h2 in g2.histories():
            for m in realization_isos(g1,h1,g2,h2):
                out.add((h1,m,h2))
    return out

def extend_map(m,e1,e2):
    return tuple(sorted(tuple(m)+((e1,e2),)))

def restrict_map(m,e1,e2):
    return tuple(sorted((a,b) for a,b in m if a!=e1 and b!=e2))

def cbhhp0(g1,g2):
    """Cause-sensitive forward history-preserving greatest fixed point."""
    R=all_triples(g1,g2)
    changed=True
    while changed:
        changed=False; remove=[]
        for h1,m,h2 in R:
            ok=True

            for s1,n1 in forward_extensions(g1,h1):
                matched=False
                for s2,n2 in forward_extensions(g2,h2):
                    if g1.profiles[s1.event] != g2.profiles[s2.event]:
                        continue
                    mp=extend_map(m,s1.event,s2.event)
                    if not witness_corresponds(n1,n2,mp,s1.event,s2.event):
                        continue
                    if (n1,mp,n2) in R:
                        matched=True; break
                if not matched:
                    ok=False; break

            if ok:
                for s2,n2 in forward_extensions(g2,h2):
                    matched=False
                    for s1,n1 in forward_extensions(g1,h1):
                        if g1.profiles[s1.event] != g2.profiles[s2.event]:
                            continue
                        mp=extend_map(m,s1.event,s2.event)
                        if not witness_corresponds(n1,n2,mp,s1.event,s2.event):
                            continue
                        if (n1,mp,n2) in R:
                            matched=True; break
                    if not matched:
                        ok=False; break

            if not ok:
                remove.append((h1,m,h2))

        if remove:
            changed=True
            for t in remove:
                R.discard(t)
    return R

def cbhhp_next(g1,g2,prev):
    """
    ON-RDSS recursive bounded grade:
    one additional mapped causal-realization rollback obligation into prev.
    """
    R=set(prev)
    changed=True
    while changed:
        changed=False; remove=[]
        for h1,m,h2 in R:
            f=dict(m); finv={v:k for k,v in f.items()}
            ok=True

            backs2={e:n for e,n in backward_extensions(h2)}
            for e1,n1 in backward_extensions(h1):
                e2=f[e1]
                if e2 not in backs2:
                    ok=False; break
                n2=backs2[e2]
                mr=restrict_map(m,e1,e2)
                if (n1,mr,n2) not in prev:
                    ok=False; break

            if ok:
                backs1={e:n for e,n in backward_extensions(h1)}
                for e2,n2 in backward_extensions(h2):
                    e1=finv[e2]
                    if e1 not in backs1:
                        ok=False; break
                    n1=backs1[e1]
                    mr=restrict_map(m,e1,e2)
                    if (n1,mr,n2) not in prev:
                        ok=False; break

            if ok:
                for s1,n1 in forward_extensions(g1,h1):
                    matched=False
                    for s2,n2 in forward_extensions(g2,h2):
                        if g1.profiles[s1.event] != g2.profiles[s2.event]:
                            continue
                        mp=extend_map(m,s1.event,s2.event)
                        if not witness_corresponds(n1,n2,mp,s1.event,s2.event):
                            continue
                        if (n1,mp,n2) in R:
                            matched=True; break
                    if not matched:
                        ok=False; break

            if ok:
                for s2,n2 in forward_extensions(g2,h2):
                    matched=False
                    for s1,n1 in forward_extensions(g1,h1):
                        if g1.profiles[s1.event] != g2.profiles[s2.event]:
                            continue
                        mp=extend_map(m,s1.event,s2.event)
                        if not witness_corresponds(n1,n2,mp,s1.event,s2.event):
                            continue
                        if (n1,mp,n2) in R:
                            matched=True; break
                    if not matched:
                        ok=False; break

            if not ok:
                remove.append((h1,m,h2))

        if remove:
            changed=True
            for t in remove:
                R.discard(t)
    return R

def related(R,h1,h2):
    return [m for a,m,b in R if a==h1 and b==h2]

def demo():
    g=GCEES(
        "v1",
        {
            "a":Profile("A",auth=("source.A",)),
            "b":Profile("B",auth=("source.B",)),
            "c":Profile("C"),
        },
        {
            "a":(frozenset(),),
            "b":(frozenset(),),
            "c":(frozenset({"a"}),frozenset({"b"})),
        }
    )

    hA=DHist((
        Step("a",frozenset(),"v1"),
        Step("b",frozenset(),"v1"),
        Step("c",frozenset({"a"}),"v1"),
    ))
    hB=DHist((
        Step("a",frozenset(),"v1"),
        Step("b",frozenset(),"v1"),
        Step("c",frozenset({"b"}),"v1"),
    ))

    R0=cbhhp0(g,g)
    R1=cbhhp_next(g,g,R0)

    gs=GCEES(
        "v1",
        {"a":Profile("X"),"b":Profile("X"),"c":Profile("C")},
        g.enables
    )
    S0=cbhhp0(gs,gs)

    return {
        "same_surface_event_set":hA.events==hB.events,
        "same_causal_order":hA.cause_closure()==hB.cause_closure(),
        "governed_CBHHP0":bool(related(R0,hA,hB)),
        "governed_CBHHP1":bool(related(R1,hA,hB)),
        "symmetric_profile_CBHHP0":bool(related(S0,hA,hB)),
    }

if __name__=="__main__":
    print(json.dumps(demo(),indent=2))
