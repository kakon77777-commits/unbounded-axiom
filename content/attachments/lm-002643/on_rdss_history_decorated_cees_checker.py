from dataclasses import dataclass
from typing import FrozenSet, Tuple, Dict
import hashlib, json

Event = str
Witness = FrozenSet[Event]

@dataclass(frozen=True)
class HistStep:
    event: Event
    witness: Witness
    version: str

@dataclass(frozen=True)
class DecoratedHistory:
    steps: Tuple[HistStep, ...]

    @property
    def events(self):
        return frozenset(s.event for s in self.steps)

    def causal_closure(self):
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

    def realization_id(self):
        payload=[(s.event,sorted(s.witness),s.version) for s in self.steps]
        return hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()[:16]

def demo():
    h_a=DecoratedHistory((
        HistStep("a",frozenset(),"v1"),
        HistStep("b",frozenset(),"v1"),
        HistStep("c",frozenset({"a"}),"v1"),
    ))
    h_b=DecoratedHistory((
        HistStep("a",frozenset(),"v1"),
        HistStep("b",frozenset(),"v1"),
        HistStep("c",frozenset({"b"}),"v1"),
    ))
    return {
        "same_raw_event_set":h_a.events==h_b.events,
        "same_causal_history":h_a.causal_closure()==h_b.causal_closure(),
        "history_A_order":sorted(h_a.causal_closure()),
        "history_B_order":sorted(h_b.causal_closure()),
        "different_realization_ids":h_a.realization_id()!=h_b.realization_id(),
    }

if __name__=="__main__":
    print(json.dumps(demo(),indent=2))
