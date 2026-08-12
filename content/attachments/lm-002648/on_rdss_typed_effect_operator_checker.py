from dataclasses import dataclass
from typing import Tuple, FrozenSet
import json

@dataclass(frozen=True)
class OpSig:
    name: str
    inputs: Tuple[str, ...]
    output: str
    effects: FrozenSet[str]
    meta_depth: int = 0

def classify(sig):
    roles=[]
    if len(sig.inputs)==0 and "realize" in sig.effects: roles.append("Realize")
    if len(sig.inputs)>=1 and "mutate" in sig.effects: roles.append("Transform")
    if len(sig.inputs)>=2 and sig.output=="Relation" and "relate" in sig.effects: roles.append("Relate")
    if sig.inputs==("Family<State>",) and sig.output=="Family<State>" and "select" in sig.effects: roles.append("Select")
    if sig.output=="Cert" and {"judge","witness"} <= sig.effects: roles.append("Certify")
    if sig.output.startswith("Algebra[") and "meta" in sig.effects and sig.meta_depth>=1: roles.append("Meta")
    return roles

if __name__=="__main__":
    ops=[
        OpSig("spawn_state",(),"State",frozenset({"realize"})),
        OpSig("tick_state",("State",),"State",frozenset({"mutate"})),
        OpSig("bind_relation",("State","State"),"Relation",frozenset({"relate"})),
        OpSig("choose_support",("Family<State>",),"Family<State>",frozenset({"select","support-nonincreasing"})),
        OpSig("certify_candidate",("Candidate",),"Cert",frozenset({"judge","witness","provenance"})),
        OpSig("rewrite_algebra",("Algebra[0]","Evidence"),"Algebra[1]",frozenset({"meta","rewrite"}),1),
    ]
    print(json.dumps({o.name:classify(o) for o in ops},indent=2))
