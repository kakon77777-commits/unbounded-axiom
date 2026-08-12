
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import copy, hashlib, json, time, uuid

def digest(obj: Any) -> str:
    raw = json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()

@dataclass(frozen=True)
class AuthorityVersion:
    definition_id: str
    version: int
    content_hash: str
    content: Dict[str, Any]
    parent_version: Optional[int] = None

@dataclass
class Trace:
    run_id: str
    definition_id: str
    version: int
    runtime_id: str
    input_digest: str
    output_digest: str
    state_diff: Dict[str, Any]
    events: List[Dict[str, Any]]
    cost: Dict[str, Any]
    error: Optional[str]
    local_time: int
    environment: str

@dataclass
class Proposal:
    proposal_id: str
    definition_id: str
    base_version: int
    diff: Dict[str, Any]
    reason: str
    evidence_refs: List[str] = field(default_factory=list)
    impact_radius: int = 1
    rollback: Dict[str, Any] = field(default_factory=dict)
    status: str = "candidate"

class AuthorityStore:
    def __init__(self):
        self.versions: Dict[str, List[AuthorityVersion]] = {}

    def create(self, definition_id: str, content: Dict[str, Any]) -> AuthorityVersion:
        if definition_id in self.versions:
            raise ValueError("definition already exists")
        c = copy.deepcopy(content)
        v = AuthorityVersion(definition_id, 1, digest(c), c, None)
        self.versions[definition_id] = [v]
        return v

    def latest(self, definition_id: str) -> AuthorityVersion:
        return self.versions[definition_id][-1]

    def get(self, definition_id: str, version: int) -> AuthorityVersion:
        return next(v for v in self.versions[definition_id] if v.version == version)

    def commit(self, proposal: Proposal, validated_content: Dict[str, Any]) -> AuthorityVersion:
        base = self.get(proposal.definition_id, proposal.base_version)
        latest = self.latest(proposal.definition_id)
        if latest.version != base.version:
            raise ValueError("stale proposal: base version is no longer latest")
        c = copy.deepcopy(validated_content)
        v = AuthorityVersion(
            proposal.definition_id,
            latest.version + 1,
            digest(c),
            c,
            latest.version
        )
        self.versions[proposal.definition_id].append(v)
        proposal.status = "committed"
        return v

    def rollback(self, definition_id: str, target_version: int) -> AuthorityVersion:
        target = self.get(definition_id, target_version)
        latest = self.latest(definition_id)
        restored = copy.deepcopy(target.content)
        v = AuthorityVersion(
            definition_id,
            latest.version + 1,
            digest(restored),
            restored,
            latest.version
        )
        self.versions[definition_id].append(v)
        return v

class CapabilityIndex:
    def __init__(self):
        self.entries: Dict[str, Dict[str, Any]] = {}

    def rebuild(self, authority: AuthorityStore):
        self.entries.clear()
        for definition_id, versions in authority.versions.items():
            v = versions[-1]
            c = v.content
            self.entries[definition_id] = {
                "definition_id": definition_id,
                "version": v.version,
                "content_hash": v.content_hash,
                "type": c.get("type"),
                "capabilities": list(c.get("capabilities", [])),
                "children": list(c.get("children", [])),
            }

    def status(self, authority: AuthorityStore, definition_id: str) -> str:
        if definition_id not in self.entries:
            return "missing"
        idx_v = self.entries[definition_id]["version"]
        auth_v = authority.latest(definition_id).version
        return "fresh" if idx_v == auth_v else "stale"

@dataclass
class RuntimeInstance:
    runtime_id: str
    definition_id: str
    version: int
    content_hash: str
    environment: str
    state: Dict[str, Any]
    materialized_children: Dict[str, "RuntimeInstance"] = field(default_factory=dict)

class RDSSRuntime:
    def __init__(self, authority: AuthorityStore, index: CapabilityIndex):
        self.authority = authority
        self.index = index
        self.instances: Dict[str, RuntimeInstance] = {}
        self.traces: Dict[str, Trace] = {}
        self.proposals: Dict[str, Proposal] = {}
        self.local_clock = 0

    def materialize(self, definition_id: str, version: Optional[int] = None, environment: str = "local"):
        v = self.authority.latest(definition_id) if version is None else self.authority.get(definition_id, version)
        runtime_id = str(uuid.uuid4())
        inst = RuntimeInstance(
            runtime_id=runtime_id,
            definition_id=definition_id,
            version=v.version,
            content_hash=v.content_hash,
            environment=environment,
            state=copy.deepcopy(v.content.get("initial_state", {})),
        )
        self.instances[runtime_id] = inst
        return inst

    def materialize_child(self, parent: RuntimeInstance, child_id: str):
        if child_id not in self.authority.latest(parent.definition_id).content.get("children", []):
            raise ValueError("child is not declared by parent authority version")
        child = self.materialize(child_id, environment=parent.environment)
        parent.materialized_children[child_id] = child
        return child

    def expand(self, runtime_id: str):
        inst = self.instances[runtime_id]
        v = self.authority.get(inst.definition_id, inst.version)
        return {
            "definition_id": inst.definition_id,
            "version": inst.version,
            "state": copy.deepcopy(inst.state),
            "known_children": list(v.content.get("children", [])),
            "materialized_children": list(inst.materialized_children.keys()),
            "contract": copy.deepcopy(v.content.get("contract", {})),
        }

    def invoke(self, runtime_id: str, event: Dict[str, Any]):
        inst = self.instances[runtime_id]
        v = self.authority.get(inst.definition_id, inst.version)
        before = copy.deepcopy(inst.state)
        t0 = time.perf_counter()
        error = None
        events = []
        try:
            et = event.get("type")
            rules = v.content.get("rules", {})
            rule = rules.get(et)
            if rule is None:
                raise ValueError(f"no rule for event {et!r}")
            field = rule["field"]
            op = rule["op"]
            value = rule.get("value", 1)
            if op == "inc":
                inst.state[field] = inst.state.get(field, 0) + value
            elif op == "set":
                inst.state[field] = value
            else:
                raise ValueError(f"unsupported op {op!r}")
            events.append({"type": "state_changed", "field": field})
            output = {"ok": True, "state": copy.deepcopy(inst.state)}
        except Exception as e:
            error = str(e)
            output = {"ok": False, "error": error, "state": copy.deepcopy(inst.state)}
        elapsed = time.perf_counter() - t0
        self.local_clock += 1
        diff = {k: {"before": before.get(k), "after": inst.state.get(k)}
                for k in set(before) | set(inst.state)
                if before.get(k) != inst.state.get(k)}
        tr = Trace(
            run_id=str(uuid.uuid4()),
            definition_id=inst.definition_id,
            version=inst.version,
            runtime_id=inst.runtime_id,
            input_digest=digest(event),
            output_digest=digest(output),
            state_diff=diff,
            events=events,
            cost={"seconds": elapsed},
            error=error,
            local_time=self.local_clock,
            environment=inst.environment,
        )
        self.traces[tr.run_id] = tr
        return output, tr

    def propose(self, definition_id: str, diff: Dict[str, Any], reason: str, evidence_refs=None, impact_radius=1):
        p = Proposal(
            proposal_id=str(uuid.uuid4()),
            definition_id=definition_id,
            base_version=self.authority.latest(definition_id).version,
            diff=copy.deepcopy(diff),
            reason=reason,
            evidence_refs=list(evidence_refs or []),
            impact_radius=impact_radius,
            rollback={"target_version": self.authority.latest(definition_id).version}
        )
        self.proposals[p.proposal_id] = p
        return p

def deep_merge(base: Dict[str, Any], diff: Dict[str, Any]) -> Dict[str, Any]:
    out = copy.deepcopy(base)
    for k, v in diff.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = copy.deepcopy(v)
    return out

def validate_proposal(authority: AuthorityStore, proposal: Proposal):
    base = authority.get(proposal.definition_id, proposal.base_version)
    candidate = deep_merge(base.content, proposal.diff)
    required = ["type", "initial_state", "rules", "contract"]
    missing = [k for k in required if k not in candidate]
    if missing:
        return False, candidate, {"missing": missing}
    for event_type, rule in candidate["rules"].items():
        if not {"field", "op"} <= set(rule):
            return False, candidate, {"bad_rule": event_type}
        if rule["op"] not in {"inc", "set"}:
            return False, candidate, {"unsupported_op": rule["op"]}
    return True, candidate, {"ok": True}

def build_demo(n_children=1000):
    authority = AuthorityStore()
    for i in range(n_children):
        authority.create(
            f"child.{i}",
            {
                "type": "counter-child",
                "capabilities": ["increment"],
                "initial_state": {"value": 0},
                "rules": {"inc": {"field": "value", "op": "inc", "value": 1}},
                "contract": {"inputs": ["inc"], "outputs": ["state"]},
                "children": [],
            }
        )
    authority.create(
        "world",
        {
            "type": "world",
            "capabilities": ["tick"],
            "initial_state": {"ticks": 0},
            "rules": {"tick": {"field": "ticks", "op": "inc", "value": 1}},
            "contract": {"inputs": ["tick"], "outputs": ["state"]},
            "children": [f"child.{i}" for i in range(n_children)],
        }
    )
    index = CapabilityIndex()
    index.rebuild(authority)
    runtime = RDSSRuntime(authority, index)
    return authority, index, runtime

def run_self_test():
    authority, index, rt = build_demo(1000)

    # 1. exact authority + rebuildable index
    assert index.status(authority, "world") == "fresh"
    old_index_hash = digest(index.entries)
    index.entries.clear()
    assert index.status(authority, "world") == "missing"
    index.rebuild(authority)
    assert digest(index.entries) == old_index_hash

    # 2. lazy recursive materialization
    world = rt.materialize("world")
    assert len(world.materialized_children) == 0
    rt.materialize_child(world, "child.17")
    assert len(world.materialized_children) == 1

    # 3. traceable run
    out, tr = rt.invoke(world.runtime_id, {"type": "tick"})
    assert out["state"]["ticks"] == 1
    assert tr.version == 1 and tr.definition_id == "world"
    assert tr.state_diff["ticks"] == {"before": 0, "after": 1}

    # 4. runtime observation only generates proposal
    p = rt.propose(
        "world",
        {"rules": {"tick": {"field": "ticks", "op": "inc", "value": 2}}},
        "synthetic optimization proposal",
        evidence_refs=[tr.run_id],
    )
    assert authority.latest("world").version == 1
    ok, candidate, report = validate_proposal(authority, p)
    assert ok
    v2 = authority.commit(p, candidate)
    assert v2.version == 2
    assert index.status(authority, "world") == "stale"
    index.rebuild(authority)
    assert index.status(authority, "world") == "fresh"

    # 5. old runtime stays pinned to v1; new runtime resolves v2
    out_old, _ = rt.invoke(world.runtime_id, {"type": "tick"})
    assert out_old["state"]["ticks"] == 2  # v1 increments by 1
    world2 = rt.materialize("world")
    out_new, _ = rt.invoke(world2.runtime_id, {"type": "tick"})
    assert out_new["state"]["ticks"] == 2  # v2 increments by 2 from 0

    # 6. rollback creates a new immutable version restoring v1 contents
    v3 = authority.rollback("world", 1)
    assert v3.version == 3
    assert authority.get("world", 1).content_hash == v3.content_hash

    return {
        "tests": 6,
        "status": "passed",
        "world_versions": [v.version for v in authority.versions["world"]],
        "trace_count": len(rt.traces),
        "materialized_child_count": len(world.materialized_children),
    }

def benchmark(n_children=5000, repeats=7):
    eager_times, lazy_times = [], []
    eager_counts, lazy_counts = [], []
    for _ in range(repeats):
        authority, index, rt = build_demo(n_children)
        parent = rt.materialize("world")

        t0 = time.perf_counter()
        for cid in authority.latest("world").content["children"]:
            rt.materialize_child(parent, cid)
        eager_times.append(time.perf_counter() - t0)
        eager_counts.append(len(parent.materialized_children))

        authority2, index2, rt2 = build_demo(n_children)
        parent2 = rt2.materialize("world")
        t0 = time.perf_counter()
        rt2.materialize_child(parent2, f"child.{n_children//2}")
        lazy_times.append(time.perf_counter() - t0)
        lazy_counts.append(len(parent2.materialized_children))

    return {
        "n_children": n_children,
        "repeats": repeats,
        "eager_seconds_median": statistics.median(eager_times),
        "lazy_seconds_median": statistics.median(lazy_times),
        "eager_materialized": eager_counts[-1],
        "lazy_materialized": lazy_counts[-1],
        "speed_ratio_eager_over_lazy": statistics.median(eager_times) / max(statistics.median(lazy_times), 1e-12),
        "note": "Synthetic Python microbenchmark; demonstrates materialization scaling behavior only, not production performance."
    }

if __name__ == "__main__":
    import statistics
    result = {"self_test": run_self_test(), "benchmark": benchmark()}
    print(json.dumps(result, ensure_ascii=False, indent=2))
