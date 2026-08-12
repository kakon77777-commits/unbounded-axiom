from dataclasses import dataclass
from typing import FrozenSet, Tuple, Dict, Set
import json

Event = str
Config = FrozenSet[Event]

@dataclass(frozen=True)
class EventDef:
    label: str
    typ: str = "Effect"
    auth: FrozenSet[str] = frozenset()
    residual: FrozenSet[str] = frozenset()

@dataclass
class Snapshot:
    version: str
    events: Dict[Event, EventDef]
    conflict_pairs: Set[FrozenSet[Event]]
    enables: Dict[Event, Tuple[FrozenSet[Event], ...]]

    def consistent(self, c: Config) -> bool:
        return all(not p.issubset(c) for p in self.conflict_pairs)

    def enabled(self, c: Config, e: Event) -> bool:
        if e in c:
            return False
        if not self.consistent(c | frozenset({e})):
            return False
        # Missing is not the same as empty enabling.
        # Missing => disabled/undefined. (empty-set,) => initially enabled.
        if e not in self.enables:
            return False
        return any(a.issubset(c) for a in self.enables[e])

    def enabled_set(self, c: Config) -> FrozenSet[Event]:
        return frozenset(e for e in self.events if self.enabled(c, e))

    def reachable_configs(self) -> Set[Config]:
        q=[frozenset()]; seen={frozenset()}
        while q:
            c=q.pop()
            for e in self.events:
                if self.enabled(c,e):
                    nc=c|frozenset({e})
                    if nc not in seen:
                        seen.add(nc); q.append(nc)
        return seen

def event_profile(s: Snapshot, e: Event):
    d=s.events[e]
    return (d.label,d.typ,tuple(sorted(d.auth)),tuple(sorted(d.residual)))

def history_profile(s: Snapshot, c: Config):
    return tuple(sorted((event_profile(s,e) for e in c), key=repr))

def future_signature(s: Snapshot, c: Config, depth=3):
    memo={}
    def rec(cfg,d):
        key=(cfg,d)
        if key in memo: return memo[key]
        if d==0:
            ans=("cut",)
        else:
            branches=[]
            for e in sorted(s.enabled_set(cfg)):
                branches.append((event_profile(s,e),rec(cfg|frozenset({e}),d-1)))
            branches.sort(key=repr)
            ans=tuple(branches)
        memo[key]=ans
        return ans
    return rec(c,depth)

def safe_branch_quotient_toy(s: Snapshot, c1: Config, c2: Config, depth=3):
    obs1=tuple(sorted(s.events[e].label for e in c1))
    obs2=tuple(sorted(s.events[e].label for e in c2))
    hp1=history_profile(s,c1); hp2=history_profile(s,c2)
    f1=future_signature(s,c1,depth); f2=future_signature(s,c2,depth)
    return {
        "same_current_projection": obs1==obs2,
        "same_history_profile": hp1==hp2,
        "same_future_signature": f1==f2,
        "safe_toy": obs1==obs2 and hp1==hp2 and f1==f2
    }

def build_v1():
    return Snapshot(
        "v1",
        {
            "a":EventDef("choice"), "b":EventDef("choice"),
            "ra":EventDef("result"), "rb":EventDef("result"),
            "fa":EventDef("future"), "fb":EventDef("future"),
        },
        {frozenset({"a","b"}),frozenset({"ra","rb"}),frozenset({"fa","fb"})},
        {
            "a":(frozenset(),), "b":(frozenset(),),
            "ra":(frozenset({"a"}),), "rb":(frozenset({"b"}),),
            "fa":(frozenset({"ra"}),), "fb":(frozenset({"rb"}),),
        }
    )

def run():
    s1=build_v1()
    ca=frozenset({"a","ra"}); cb=frozenset({"b","rb"})
    symmetric=safe_branch_quotient_toy(s1,ca,cb)

    s_diff=Snapshot(
        "v1-diff",
        {**{k:v for k,v in s1.events.items() if k!="fb"},
         "fb":EventDef("different_future",auth=frozenset({"admin"}))},
        set(s1.conflict_pairs),dict(s1.enables)
    )
    different=safe_branch_quotient_toy(s_diff,ca,cb)

    s_meta=Snapshot(
        "v2",
        {**s1.events,"xa":EventDef("new_capability",auth=frozenset({"special"}))},
        set(s1.conflict_pairs),
        {**s1.enables,"xa":(frozenset({"ra"}),)}
    )
    after_meta=safe_branch_quotient_toy(s_meta,ca,cb)

    s_no_ra=Snapshot(
        "v2-no-ra",dict(s1.events),set(s1.conflict_pairs),
        {
            "a":(frozenset(),),"b":(frozenset(),),
            "rb":(frozenset({"b"}),),
            "fa":(frozenset({"ra"}),),"fb":(frozenset({"rb"}),),
        }
    )

    return {
        "symmetric_fold_safe":symmetric["safe_toy"],
        "same_observation_different_future_safe":different["safe_toy"],
        "safe_before_meta":symmetric["safe_toy"],
        "safe_after_meta":after_meta["safe_toy"],
        "old_committed_config_reachable_v1":ca in s1.reachable_configs(),
        "same_config_generable_v2":ca in s_no_ra.reachable_configs(),
    }

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
