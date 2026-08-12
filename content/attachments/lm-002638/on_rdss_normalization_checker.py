# Generated ON-RDSS toy normalization checker
from dataclasses import dataclass
from typing import Tuple, List, Dict
from collections import deque

@dataclass(frozen=True)
class Rewrite:
    lhs: Tuple[str, ...]
    rhs: Tuple[str, ...]
    cert: str
    note: str = ""

class CertifiedRewriteSystem:
    def __init__(self, rules: List[Rewrite]): self.rules = rules
    def one_steps(self, word):
        out=[]
        for i in range(len(word)):
            for r in self.rules:
                n=len(r.lhs)
                if word[i:i+n] == r.lhs:
                    out.append((word[:i]+r.rhs+word[i+n:], r))
        return out
    def normal_forms(self, start, max_nodes=10000):
        q=deque([start]); seen={start}; normals=set()
        while q and len(seen)<max_nodes:
            w=q.popleft(); steps=self.one_steps(w)
            if not steps: normals.add(w)
            for nw,_ in steps:
                if nw not in seen: seen.add(nw); q.append(nw)
        return normals, seen

def inversion_count(word, rank):
    xs=[rank.get(x,99) for x in word]
    return sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))

def run_demo():
    rank={"E":0,"C":1,"V":2}
    ecv=CertifiedRewriteSystem([
        Rewrite(("C","E"),("E","C"),"CommCert(C,E)"),
        Rewrite(("V","E"),("E","V"),"CommCert(V,E)"),
        Rewrite(("V","C"),("C","V"),"CommCert(V,C)"),
    ])
    n1,_=ecv.normal_forms(("V","E","C","E","V","C"))
    missing=CertifiedRewriteSystem([
        Rewrite(("PrepA","AtoB"),("AB",),"CompCert"),
        Rewrite(("CtoD","FinishD"),("CD",),"CompCert"),
    ])
    n2,_=missing.normal_forms(("PrepA","AtoB","CtoD","FinishD"))
    confl=CertifiedRewriteSystem([
        Rewrite(("NeedBridge",),("B1",),"BridgeCert1"),
        Rewrite(("NeedBridge",),("B2",),"BridgeCert2"),
        Rewrite(("Left","B1","Right"),("ObservedSame",),"ObsEqCert1"),
        Rewrite(("Left","B2","Right"),("ObservedSame",),"ObsEqCert2"),
    ])
    n3,_=confl.normal_forms(("Left","NeedBridge","Right"))
    hist=CertifiedRewriteSystem([
        Rewrite(("NeedBridge",),("B1",),"BridgeCert1"),
        Rewrite(("NeedBridge",),("B2",),"BridgeCert2"),
        Rewrite(("Left","B1","Right"),("Result","H:B1"),"HistoryCert1"),
        Rewrite(("Left","B2","Right"),("Result","H:B2"),"HistoryCert2"),
    ])
    n4,_=hist.normal_forms(("Left","NeedBridge","Right"))
    return {"ecv":sorted(n1),"missing_bridge":sorted(n2),"bridge_confluent":sorted(n3),"bridge_history":sorted(n4)}

if __name__=="__main__":
    import json
    print(json.dumps(run_demo(), indent=2))