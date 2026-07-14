
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from enum import Enum
from hashlib import sha256
from copy import deepcopy
import json


class Status(str, Enum):
    INVALID = "invalid"
    ANALOGY = "analogy"
    QUESTION = "research_question"
    CONJECTURE = "conjecture"
    CONDITIONAL = "conditional_result"
    VERIFIED = "verified_result"


class Relation(str, Enum):
    JUSTIFIES = "justifies"
    DEFINES = "defines"
    MOTIVATES = "motivates"
    DIAGNOSES = "diagnoses"
    ILLUSTRATES = "illustrates"


TRUTH_EDGES = {Relation.JUSTIFIES, Relation.DEFINES}


@dataclass(frozen=True)
class Failure:
    failure_id: str
    kind: str
    description: str
    affects_truth: bool = True


@dataclass(frozen=True)
class Evidence:
    independent_proof: bool = False
    executable_test: bool = False
    reproducible: bool = False
    source_verified: bool = False
    assumptions_explicit: bool = False
    countermodel_search: bool = False


@dataclass
class Claim:
    claim_id: str
    statement: str
    status: Status
    artifact_class: str
    parents: list[str] = field(default_factory=list)
    relations: dict[str, Relation] = field(default_factory=dict)
    direct_failures: list[str] = field(default_factory=list)
    discharged_failures: list[str] = field(default_factory=list)
    evidence: Evidence = field(default_factory=Evidence)
    semantic_delta: str = ""

    def payload(self) -> dict:
        return {
            "claim_id": self.claim_id,
            "statement": self.statement,
            "status": self.status.value,
            "artifact_class": self.artifact_class,
            "parents": self.parents,
            "relations": {k: v.value for k, v in sorted(self.relations.items())},
            "direct_failures": self.direct_failures,
            "discharged_failures": self.discharged_failures,
            "evidence": asdict(self.evidence),
            "semantic_delta": self.semantic_delta,
        }

    def content_hash(self) -> str:
        raw = json.dumps(self.payload(), sort_keys=True, ensure_ascii=False)
        return sha256(raw.encode("utf-8")).hexdigest()


class Ledger:
    def __init__(self, failures: dict[str, Failure], claims: dict[str, Claim]):
        self.failures = failures
        self.claims = claims
        self.events: list[dict] = []

    def ancestors(self, claim_id: str) -> set[str]:
        seen, stack = set(), list(self.claims[claim_id].parents)
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            stack.extend(self.claims[node].parents)
        return seen

    def provenance_failures(self, claim_id: str) -> set[str]:
        nodes = {claim_id} | self.ancestors(claim_id)
        out = set()
        for node in nodes:
            out.update(self.claims[node].direct_failures)
        return out

    def active_truth_taint(self, claim_id: str) -> set[str]:
        claim = self.claims[claim_id]
        active = set(claim.direct_failures)
        for parent in claim.parents:
            if claim.relations[parent] in TRUTH_EDGES:
                active |= self.active_truth_taint(parent)
        active -= set(claim.discharged_failures)
        return {f for f in active if self.failures[f].affects_truth}

    def independent_route(self, claim_id: str) -> bool:
        e = self.claims[claim_id].evidence
        return e.independent_proof or (
            e.executable_test and e.reproducible and e.assumptions_explicit
        )

    def append_event(self, event_type: str, claim_id: str, payload: dict) -> None:
        prev = self.events[-1]["hash"] if self.events else "GENESIS"
        body = {
            "event_id": f"E{len(self.events)+1:03d}",
            "event_type": event_type,
            "claim_id": claim_id,
            "payload": payload,
            "previous_hash": prev,
        }
        body["hash"] = sha256(
            json.dumps(body, sort_keys=True, ensure_ascii=False).encode("utf-8")
        ).hexdigest()
        self.events.append(body)

    def verify_chain(self) -> bool:
        prev = "GENESIS"
        for event in self.events:
            body = {k: v for k, v in event.items() if k != "hash"}
            if body["previous_hash"] != prev:
                return False
            expected = sha256(
                json.dumps(body, sort_keys=True, ensure_ascii=False).encode("utf-8")
            ).hexdigest()
            if expected != event["hash"]:
                return False
            prev = event["hash"]
        return True


def obligations(claim: Claim, active_taint: set[str]) -> set[str]:
    e = claim.evidence
    out = set()
    if e.assumptions_explicit:
        out |= {"assumptions_explicit", "testable_statement"}
    if e.independent_proof:
        out |= {"independent_validation", "proof_under_assumptions"}
    if e.executable_test and e.reproducible:
        out.add("independent_validation")
    if e.reproducible:
        out.add("reproducible")
    if e.source_verified:
        out.add("source_verified")
    if e.countermodel_search:
        out.add("counterexample_checked")
    if not active_taint:
        out.add("zero_active_taint")
    return out


VERIFIED_REQUIREMENTS = {
    "assumptions_explicit",
    "independent_validation",
    "reproducible",
    "source_verified",
    "zero_active_taint",
}


def can_promote_verified(ledger: Ledger, claim_id: str) -> tuple[bool, set[str]]:
    c = ledger.claims[claim_id]
    have = obligations(c, ledger.active_truth_taint(claim_id))
    missing = VERIFIED_REQUIREMENTS - have
    return not missing, missing


def demote(current: Status, triggers: set[str]) -> Status:
    if "counterexample" in triggers:
        return Status.INVALID
    if "type_mismatch" in triggers:
        return Status.ANALOGY
    if "proof_gap" in triggers or "circularity" in triggers:
        return Status.CONJECTURE
    if "source_unverified" in triggers and current == Status.VERIFIED:
        return Status.CONDITIONAL
    return current


@dataclass(frozen=True)
class SearchState:
    step: int
    signature: str
    new_outputs: int
    marginal_gain: float
    unresolved: int
    complexity: float
    external_data_required: bool = False


def stop_reason(
    history: list[SearchState],
    epsilon: float = 0.02,
    patience: int = 2,
    max_steps: int = 8,
    max_complexity: float = 10.0,
) -> list[str]:
    cur = history[-1]
    reasons = []
    if cur.step >= max_steps:
        reasons.append("finite_step_budget_reached")
    if cur.complexity >= max_complexity:
        reasons.append("complexity_budget_reached")
    if cur.new_outputs == 0:
        reasons.append("no_new_admissible_output")
    if cur.external_data_required:
        reasons.append("external_evidence_required")
    if cur.signature in {s.signature for s in history[:-1]}:
        reasons.append("canonical_cycle_detected")
    if len(history) >= patience and all(
        s.marginal_gain <= epsilon for s in history[-patience:]
    ):
        reasons.append("marginal_gain_below_threshold")
    if len(history) >= patience + 1:
        vals = [s.unresolved for s in history[-(patience+1):]]
        if all(b >= a for a, b in zip(vals, vals[1:])):
            reasons.append("obligations_not_decreasing")
    return reasons


failures = {
    "F1": Failure("F1", "analogy_to_identity", "Shared 1/2 was promoted to spectral identity."),
    "F2": Failure("F2", "information_loss", "Projection discarded the real-part coordinate."),
}

claims = {
    "C3": Claim(
        "C3", "Shared 1/2 proves full spectral identity.",
        Status.INVALID, "failed_claim", direct_failures=["F1"]
    ),
    "C5": Claim(
        "C5", "A projected trace identity proves the target theorem.",
        Status.INVALID, "failed_claim",
        parents=["C3"], relations={"C3": Relation.JUSTIFIES},
        direct_failures=["F2"]
    ),
    "C6": Claim(
        "C6", "The original target theorem follows.",
        Status.CONJECTURE, "original_target",
        parents=["C5"], relations={"C5": Relation.JUSTIFIES},
        evidence=Evidence(assumptions_explicit=True)
    ),
    "C8": Claim(
        "C8", "Use a bridge certificate to audit cross-domain mappings.",
        Status.CONDITIONAL, "methodological_gold",
        parents=["C3"], relations={"C3": Relation.DIAGNOSES},
        evidence=Evidence(
            independent_proof=True, executable_test=True, reproducible=True,
            source_verified=True, assumptions_explicit=True
        ),
        semantic_delta="The failed bridge is diagnostic data, not a premise."
    ),
    "C9": Claim(
        "C9", "Build a high-fluency false-proof benchmark.",
        Status.CONDITIONAL, "negative_gold",
        parents=["C3", "C5"],
        relations={"C3": Relation.ILLUSTRATES, "C5": Relation.ILLUSTRATES},
        evidence=Evidence(
            executable_test=True, reproducible=True, source_verified=True,
            assumptions_explicit=True, countermodel_search=True
        ),
        semantic_delta="Failed claims become labeled examples."
    ),
    "C10": Claim(
        "C10", "Define a residual observable restoring lost information.",
        Status.CONDITIONAL, "creative_gold",
        parents=["C5"], relations={"C5": Relation.MOTIVATES},
        evidence=Evidence(
            independent_proof=True, executable_test=True, reproducible=True,
            source_verified=True, assumptions_explicit=True
        ),
        semantic_delta="Information loss generates a new observable."
    ),
}

ledger = Ledger(failures, claims)
for cid, claim in claims.items():
    ledger.append_event("claim_registered", cid, {
        "claim_hash": claim.content_hash(),
        "status": claim.status.value,
    })

promotion = []
for cid in ["C6", "C8", "C9", "C10"]:
    allowed, missing = can_promote_verified(ledger, cid)
    promotion.append({
        "claim_id": cid,
        "historical_failures": sorted(ledger.provenance_failures(cid)),
        "active_truth_taint": sorted(ledger.active_truth_taint(cid)),
        "independent_route": ledger.independent_route(cid),
        "promotion_allowed": allowed,
        "missing_obligations": sorted(missing),
    })
    if allowed:
        claims[cid].status = Status.VERIFIED
        ledger.append_event("status_promoted", cid, {
            "new_status": Status.VERIFIED.value,
            "historical_failures_retained": sorted(ledger.provenance_failures(cid)),
        })

chain_before = ledger.verify_chain()
saved = deepcopy(ledger.events[1])
ledger.events[1]["payload"]["status"] = "verified_result"
chain_after_tamper = ledger.verify_chain()
ledger.events[1] = saved
chain_after_restore = ledger.verify_chain()

demotions = [
    {"trigger": "counterexample", "result": demote(Status.VERIFIED, {"counterexample"}).value},
    {"trigger": "type_mismatch", "result": demote(Status.VERIFIED, {"type_mismatch"}).value},
    {"trigger": "proof_gap", "result": demote(Status.VERIFIED, {"proof_gap"}).value},
    {"trigger": "source_unverified", "result": demote(Status.VERIFIED, {"source_unverified"}).value},
]

histories = {
    "plateau": [
        SearchState(1, "A", 3, .30, 5, 2),
        SearchState(2, "B", 2, .10, 3, 3),
        SearchState(3, "C", 1, .01, 3, 4),
        SearchState(4, "D", 1, .00, 3, 5),
    ],
    "cycle": [
        SearchState(1, "A", 2, .20, 4, 2),
        SearchState(2, "B", 1, .10, 3, 3),
        SearchState(3, "A", 1, .08, 3, 4),
    ],
    "external": [
        SearchState(1, "A", 1, .15, 2, 2),
        SearchState(2, "B", 1, .08, 1, 3, True),
    ],
    "no_output": [
        SearchState(1, "A", 2, .20, 3, 2),
        SearchState(2, "B", 0, .00, 3, 3),
    ],
}

report = {
    "promotion_audit": promotion,
    "final_claim_status": {cid: c.status.value for cid, c in claims.items()},
    "provenance": {
        cid: {
            "historical_failures": sorted(ledger.provenance_failures(cid)),
            "active_truth_taint": sorted(ledger.active_truth_taint(cid)),
            "hash_prefix": c.content_hash()[:16],
        }
        for cid, c in claims.items()
    },
    "hash_chain_test": {
        "before_tamper": chain_before,
        "after_tamper": chain_after_tamper,
        "after_restore": chain_after_restore,
    },
    "demotion_test": demotions,
    "stopping_test": {
        name: stop_reason(history) for name, history in histories.items()
    },
}

out = Path("/mnt/data/theory_gold_extraction_round4_report.json")
out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

print(json.dumps(report, ensure_ascii=False, indent=2))
