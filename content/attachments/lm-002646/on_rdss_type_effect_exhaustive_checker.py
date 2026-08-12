from dataclasses import dataclass
from typing import Tuple, Optional, Dict
from itertools import product
from collections import deque
import json

@dataclass(frozen=True)
class Op:
    name: str
    inp: Optional[str]
    out: str
    eff: Tuple[str, ...]
    depth: int = 0

OPS: Dict[str, Op] = {
    "R": Op("R", None, "State", ("realize",), 0),
    "T": Op("T", "State", "State", ("mutate",), 0),
    "P": Op("P", "State", "View", ("project",), 0),
    "V": Op("V", "View", "State", ("validate_view",), 0),
    "Q": Op("Q", "State", "State", ("read_a",), 0),
    "Q2": Op("Q2", "State", "State", ("read_b",), 0),
}
INDEPENDENT={frozenset(("read_a","read_b"))}

def trace_equiv(a,b):
    if len(a)!=len(b): return False
    q=deque([a]); seen={a}
    while q:
        t=q.popleft()
        if t==b: return True
        xs=list(t)
        for i in range(len(xs)-1):
            if frozenset((xs[i],xs[i+1])) in INDEPENDENT:
                ys=xs.copy(); ys[i],ys[i+1]=ys[i+1],ys[i]
                y=tuple(ys)
                if y not in seen: seen.add(y); q.append(y)
    return False

def type_word(word):
    first=OPS[word[0]]
    ext=first.inp; cur=first.out; eff=list(first.eff); depth=first.depth
    for name in word[1:]:
        op=OPS[name]
        if op.inp!=cur:
            return {"kind":"residual","actual":cur,"expected":op.inp,"at":name}
        cur=op.out; eff.extend(op.eff); depth=max(depth,op.depth)
    return {"kind":"typed","inp":ext,"out":cur,"eff":tuple(eff),"depth":depth}

def macro(name,lhs):
    t=type_word(lhs)
    return Op(name,t["inp"],t["out"],t["eff"],t["depth"])

MACROS={("T","T"):"TT",("P","V"):"PV",("Q","Q2"):"QQ2",("Q2","Q"):"Q2Q"}
for lhs,rhs in MACROS.items(): OPS[rhs]=macro(rhs,lhs)

def steps(word):
    out=[]
    for lhs,rhs in MACROS.items():
        n=len(lhs)
        for i in range(len(word)-n+1):
            if word[i:i+n]==lhs: out.append(word[:i]+(rhs,)+word[i+n:])
    for i in range(len(word)-1):
        a,b=word[i],word[i+1]; oa,ob=OPS[a],OPS[b]
        if oa.inp==oa.out==ob.inp==ob.out=="State" and len(oa.eff)==len(ob.eff)==1:
            if frozenset((oa.eff[0],ob.eff[0])) in INDEPENDENT:
                out.append(word[:i]+(b,a)+word[i+2:])
    return out

def preserved(a,b):
    return a["kind"]==b["kind"]=="typed" and \
        (a["inp"],a["out"],a["depth"])==(b["inp"],b["out"],b["depth"]) and \
        trace_equiv(a["eff"],b["eff"])

if __name__=="__main__":
    alphabet=("R","T","P","V","Q","Q2")
    failures=[]; checked=0; typed=residual=0
    for n in range(1,5):
        for w in product(alphabet,repeat=n):
            t=type_word(w)
            if t["kind"]=="typed":
                typed+=1
                for w2 in steps(w):
                    checked+=1
                    if not preserved(t,type_word(w2)): failures.append((w,w2))
            else:
                residual+=1
    print(json.dumps({
        "typed_words":typed,
        "residual_words":residual,
        "structural_steps_checked":checked,
        "preservation_failures":failures,
    },indent=2))
