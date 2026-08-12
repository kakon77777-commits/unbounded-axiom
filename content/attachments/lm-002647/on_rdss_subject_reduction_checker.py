from dataclasses import dataclass
from typing import Tuple, List

@dataclass(frozen=True)
class Sig:
    name: str
    inputs: Tuple[str, ...]
    output: str
    effects: Tuple[str, ...]
    depth: int = 0

@dataclass(frozen=True)
class Residual:
    left: str
    right: str
    actual: str
    expected: str
    obligation: str

def seq_compose(ops: List[Sig]):
    if not ops: return None, None
    external_inputs=list(ops[0].inputs)
    current_out=ops[0].output
    effects=list(ops[0].effects)
    depth=ops[0].depth
    for prev,op in zip(ops,ops[1:]):
        if len(op.inputs)!=1:
            return None, Residual(prev.name,op.name,current_out,str(op.inputs),"non-unary-sequential-slot")
        if current_out!=op.inputs[0]:
            return None, Residual(prev.name,op.name,current_out,op.inputs[0],"type-mismatch")
        current_out=op.output
        effects.extend(op.effects)
        depth=max(depth,op.depth)
    return Sig("<"+";".join(o.name for o in ops)+">",tuple(external_inputs),current_out,tuple(effects),depth),None

def preserved(a,b):
    return (a.inputs,a.output,a.effects,a.depth)==(b.inputs,b.output,b.effects,b.depth)

if __name__=="__main__":
    R=Sig("R",(),"State",("realize",),0)
    T=Sig("T",("State",),"State",("mutate",),0)
    P=Sig("P",("State",),"View",("project",),0)
    T2,_=seq_compose([T,T]); T2=Sig("T2",T2.inputs,T2.output,T2.effects,T2.depth)
    before,_=seq_compose([R,T,T]); after,_=seq_compose([R,T2])
    _,residual=seq_compose([R,P,T])
    print("subject_reduction_preserved =",preserved(before,after))
    print("residual =",residual)
