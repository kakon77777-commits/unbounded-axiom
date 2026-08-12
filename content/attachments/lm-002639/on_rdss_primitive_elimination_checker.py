from dataclasses import dataclass
from typing import FrozenSet
import itertools, json

PRIMITIVES = (
    "Realize","Transform","Relate","Type","Select","Gate",
    "Bridge","Project","Remember","Order","Certify","Meta"
)
FREE_SPECS = frozenset({
    "TYPE_SCHEMA","POLICY","LOSS_SPEC","BRIDGE_SPEC",
    "HISTORY_SPEC","ORDER_AXIOMS"
})

@dataclass(frozen=True)
class Rule:
    target: str
    requires: FrozenSet[str]
    note: str

RULES = (
    Rule("Type", frozenset({"Select","Certify","TYPE_SCHEMA"}), "selection + certified type schema"),
    Rule("Gate", frozenset({"Select","Certify","POLICY"}), "certified continuation selection"),
    Rule("Project", frozenset({"Transform","Certify","LOSS_SPEC"}), "view transform + loss certificate"),
    Rule("Order", frozenset({"Relate","Certify","ORDER_AXIOMS"}), "typed relation + order axioms"),
    Rule("Bridge", frozenset({"Transform","Type","Certify","BRIDGE_SPEC"}), "typed cross-domain transform"),
    Rule("Remember", frozenset({"Transform","Project","Certify","HISTORY_SPEC"}), "history transform + projection"),
)

def closure(seed):
    known=set(seed)|set(FREE_SPECS); deriv={}
    changed=True
    while changed:
        changed=False
        for r in RULES:
            if r.target not in known and r.requires <= known:
                known.add(r.target)
                deriv[r.target]={"requires":sorted(r.requires),"note":r.note}
                changed=True
    return known, deriv

def min_bases():
    target=set(PRIMITIVES)
    for k in range(1,len(PRIMITIVES)+1):
        out=[]
        for combo in itertools.combinations(PRIMITIVES,k):
            known,deriv=closure(combo)
            if target <= known:
                out.append((combo,deriv))
        if out: return k,out
    return None,[]

def main():
    elim={}
    full=set(PRIMITIVES)
    for p in PRIMITIVES:
        known,deriv=closure(full-{p})
        elim[p]={"derivable":p in known,"derivation":deriv.get(p)}
    k,bases=min_bases()
    print(json.dumps({
        "elimination":elim,
        "minimum_basis_size":k,
        "minimum_bases":[list(b[0]) for b in bases],
        "warning":"Finite derivability model only; not a proof of mathematical minimality."
    },indent=2))

if __name__=="__main__":
    main()
