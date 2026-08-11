#!/usr/bin/env python3
"""CDI Runtime + AIVS MVP v0.1

Standard-library-only reference implementation.

Scope:
- SQLite persistent state/event log
- AIVS Vertical Sync Packet + deterministic pressure/regime
- Compute Candidate + relevant-conflict commit validation
- Lease/fencing + idempotency
- Shadow route benchmark + route promotion
- Game Equivalence Contract (basic JSON state comparator)
- Serialization-gap findings
- JSONL evidence import
- Windows WPR/WPA command planning

Non-goals:
- native ETW parsing
- live process thread rewriting
- arbitrary binary patching
- hard real-time scheduling
- automatic GPU kernel generation
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sqlite3
import sys
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

HERE = Path(__file__).resolve().parent
SCHEMA_PATH = HERE.parent / "schemas" / "sqlite_schema.sql"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def uid(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4()}"


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def jload(text: str | None, default: Any) -> Any:
    if not text:
        return default
    return json.loads(text)


@dataclass
class FenceResult:
    ok: bool
    reason: str
    relevant_conflicts: list[str]


class CDIRuntime:
    def __init__(self, db_path: str | Path):
        self.db_path = Path(db_path)
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys=ON")

    def close(self) -> None:
        self.conn.close()

    def init_db(self) -> None:
        self.conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.conn.commit()

    def create_run(self, name: str, run_id: str | None = None) -> str:
        run_id = run_id or uid("run")
        self.conn.execute(
            """INSERT INTO runs
            (run_id,name,epoch,topology_version,policy_version,current_state_version,created_at)
            VALUES(?,?,?,?,?,?,?)""",
            (run_id, name, 1, 1, 1, 0, utc_now()),
        )
        self.conn.commit()
        self.emit_event(run_id, "run.created", "global", {"name": name})
        return run_id

    def get_run(self, run_id: str) -> sqlite3.Row:
        row = self.conn.execute("SELECT * FROM runs WHERE run_id=?", (run_id,)).fetchone()
        if not row:
            raise KeyError(f"unknown run: {run_id}")
        return row

    def emit_event(self, run_id: str, event_type: str, scope: str | None, payload: Any) -> str:
        event_id = uid("evt")
        self.conn.execute(
            "INSERT INTO events(event_id,run_id,event_type,scope,payload_json,created_at) VALUES(?,?,?,?,?,?)",
            (event_id, run_id, event_type, scope, canonical_json(payload), utc_now()),
        )
        self.conn.commit()
        return event_id

    # ---------- AIVS ----------

    @staticmethod
    def sync_pressure(
        anomaly: float = 0.0,
        drift: float = 0.0,
        conflict: float = 0.0,
        uncertainty: float = 0.0,
        risk: float = 0.0,
        novelty: float = 0.0,
        weights: Iterable[float] = (1, 1, 1, 1, 1, 1),
    ) -> float:
        vals = [anomaly, drift, conflict, uncertainty, risk, novelty]
        ws = list(weights)
        if len(ws) != 6:
            raise ValueError("weights must contain six values")
        denom = sum(ws) or 1.0
        return max(0.0, min(1.0, sum(v*w for v, w in zip(vals, ws)) / denom))

    @staticmethod
    def select_regime(pressure: float) -> str:
        if pressure < 0.25:
            return "R0"
        if pressure < 0.50:
            return "R1"
        if pressure < 0.75:
            return "R2"
        return "ESCALATE"

    def build_vsp(
        self,
        run_id: str,
        relay_id: str,
        worker_id: str,
        flow_id: str,
        region_id: str,
        *,
        anomaly: float = 0.0,
        drift: float = 0.0,
        conflict: float = 0.0,
        uncertainty: float = 0.0,
        risk: float = 0.0,
        novelty: float = 0.0,
        dependency: str = "valid",
        invariant: str = "pass",
        evidence_refs: list[str] | None = None,
    ) -> dict[str, Any]:
        run = self.get_run(run_id)
        pressure = self.sync_pressure(anomaly, drift, conflict, uncertainty, risk, novelty)
        regime = self.select_regime(pressure)
        vsp = {
            "protocol": "aivs/0.1",
            "identity": {
                "relay_id": relay_id,
                "worker_id": worker_id,
                "flow_id": flow_id,
                "region_id": region_id,
            },
            "temporal": {
                "epoch": run["epoch"],
                "topology_version": run["topology_version"],
                "policy_version": run["policy_version"],
                "state_version": run["current_state_version"],
                "created_at": utc_now(),
            },
            "status": {
                "dependency": dependency,
                "invariant": invariant,
                "pressure": pressure,
                "regime": regime,
            },
            "evidence_refs": evidence_refs or [],
        }
        sync_id = uid("sync")
        self.conn.execute(
            """INSERT INTO sync_events(sync_id,run_id,relay_id,flow_id,region_id,pressure,regime,vsp_json,created_at)
               VALUES(?,?,?,?,?,?,?,?,?)""",
            (sync_id, run_id, relay_id, flow_id, region_id, pressure, regime, canonical_json(vsp), utc_now()),
        )
        self.conn.commit()
        return vsp

    # ---------- authority / fencing ----------

    def grant_lease(self, run_id: str, scope: str, holder_id: str, valid_until: str | None = None) -> int:
        old = self.conn.execute(
            "SELECT fencing_token FROM leases WHERE run_id=? AND scope=?",
            (run_id, scope),
        ).fetchone()
        token = (old["fencing_token"] + 1) if old else 1
        self.conn.execute(
            """INSERT INTO leases(run_id,scope,holder_id,fencing_token,valid_until,updated_at)
               VALUES(?,?,?,?,?,?)
               ON CONFLICT(run_id,scope) DO UPDATE SET
                 holder_id=excluded.holder_id,
                 fencing_token=excluded.fencing_token,
                 valid_until=excluded.valid_until,
                 updated_at=excluded.updated_at""",
            (run_id, scope, holder_id, token, valid_until, utc_now()),
        )
        self.conn.commit()
        self.emit_event(run_id, "lease.granted", scope, {"holder_id": holder_id, "fencing_token": token})
        return token

    def current_fencing_token(self, run_id: str, scope: str) -> int | None:
        row = self.conn.execute(
            "SELECT fencing_token FROM leases WHERE run_id=? AND scope=?",
            (run_id, scope),
        ).fetchone()
        return int(row["fencing_token"]) if row else None

    # ---------- candidates / commit ----------

    def create_candidate(
        self,
        run_id: str,
        *,
        task_id: str,
        region_id: str,
        flow_id: str,
        producer_id: str,
        read_keys: list[str],
        write_keys: list[str],
        output: Any,
        idempotency_key: str,
        input_state_version: int | None = None,
        dependency_status: str = "pass",
        invariant_status: str = "pass",
        semantic_status: str = "pass",
        risk: float = 0.1,
        speculative: bool = False,
        side_effect_class: str = "Pure",
        authority_scope: str | None = None,
        fencing_token: int | None = None,
    ) -> str:
        run = self.get_run(run_id)
        input_state_version = (
            int(run["current_state_version"])
            if input_state_version is None
            else int(input_state_version)
        )
        candidate_id = uid("cand")
        self.conn.execute(
            """INSERT INTO candidates(
               candidate_id,run_id,task_id,region_id,flow_id,producer_id,
               input_state_version,epoch,topology_version,policy_version,
               read_keys_json,write_keys_json,output_json,output_digest,
               dependency_status,invariant_status,semantic_status,risk,speculative,
               side_effect_class,authority_scope,fencing_token,idempotency_key,status,reject_reason,created_at
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                candidate_id, run_id, task_id, region_id, flow_id, producer_id,
                input_state_version, run["epoch"], run["topology_version"], run["policy_version"],
                canonical_json(read_keys), canonical_json(write_keys), canonical_json(output), digest(output),
                dependency_status, invariant_status, semantic_status, float(risk), int(bool(speculative)),
                side_effect_class, authority_scope, fencing_token, idempotency_key, "PRODUCED", None, utc_now(),
            ),
        )
        self.conn.commit()
        self.emit_event(run_id, "candidate.produced", flow_id, {"candidate_id": candidate_id, "region_id": region_id})
        return candidate_id

    def _changed_keys_since(self, run_id: str, version: int) -> set[str]:
        rows = self.conn.execute(
            """SELECT changed_keys_json FROM state_changes
               WHERE run_id=? AND state_version>? ORDER BY state_version""",
            (run_id, version),
        ).fetchall()
        changed: set[str] = set()
        for row in rows:
            changed.update(jload(row["changed_keys_json"], []))
        return changed

    def fence_candidate(self, candidate_id: str) -> FenceResult:
        c = self.conn.execute("SELECT * FROM candidates WHERE candidate_id=?", (candidate_id,)).fetchone()
        if not c:
            return FenceResult(False, "unknown_candidate", [])
        run = self.get_run(c["run_id"])

        if c["epoch"] != run["epoch"]:
            return FenceResult(False, "stale_epoch", [])
        if c["topology_version"] != run["topology_version"]:
            return FenceResult(False, "stale_topology", [])
        if c["policy_version"] != run["policy_version"]:
            return FenceResult(False, "stale_policy", [])
        if c["dependency_status"] != "pass":
            return FenceResult(False, "dependency_failed", [])
        if c["invariant_status"] != "pass":
            return FenceResult(False, "invariant_failed", [])
        if c["semantic_status"] != "pass":
            return FenceResult(False, "semantic_failed", [])
        if c["speculative"] and c["side_effect_class"] == "Irreversible":
            return FenceResult(False, "effect_barrier_irreversible_speculation", [])

        scope = c["authority_scope"]
        if scope:
            current = self.current_fencing_token(c["run_id"], scope)
            if current is None or c["fencing_token"] != current:
                return FenceResult(False, "stale_fencing_token", [])

        current_version = int(run["current_state_version"])
        if c["input_state_version"] != current_version:
            changed = self._changed_keys_since(c["run_id"], int(c["input_state_version"]))
            reads = set(jload(c["read_keys_json"], []))
            conflicts = sorted(changed & reads)
            if conflicts:
                return FenceResult(False, "relevant_state_conflict", conflicts)

        return FenceResult(True, "pass", [])

    def commit_candidate(self, candidate_id: str, commit_scope: str = "local") -> dict[str, Any]:
        c = self.conn.execute("SELECT * FROM candidates WHERE candidate_id=?", (candidate_id,)).fetchone()
        if not c:
            raise KeyError(candidate_id)

        existing = self.conn.execute(
            "SELECT * FROM commit_receipts WHERE run_id=? AND idempotency_key=?",
            (c["run_id"], c["idempotency_key"]),
        ).fetchone()
        if existing:
            return dict(existing)

        fence = self.fence_candidate(candidate_id)
        if not fence.ok:
            self.conn.execute(
                "UPDATE candidates SET status='REJECTED', reject_reason=? WHERE candidate_id=?",
                (fence.reason, candidate_id),
            )
            self.conn.commit()
            self.emit_event(
                c["run_id"], "candidate.rejected", c["flow_id"],
                {"candidate_id": candidate_id, "reason": fence.reason, "conflicts": fence.relevant_conflicts},
            )
            return {"status": "REJECTED", "reason": fence.reason, "conflicts": fence.relevant_conflicts}

        run = self.get_run(c["run_id"])
        prev = int(run["current_state_version"])
        new = prev + 1
        commit_id = uid("commit")
        changed_keys = jload(c["write_keys_json"], [])
        evidence_digest = digest({
            "candidate_id": candidate_id,
            "output_digest": c["output_digest"],
            "read_keys": jload(c["read_keys_json"], []),
            "write_keys": changed_keys,
        })

        with self.conn:
            self.conn.execute(
                "UPDATE runs SET current_state_version=? WHERE run_id=?",
                (new, c["run_id"]),
            )
            self.conn.execute(
                """INSERT INTO state_changes(run_id,state_version,commit_id,changed_keys_json,created_at)
                   VALUES(?,?,?,?,?)""",
                (c["run_id"], new, commit_id, canonical_json(changed_keys), utc_now()),
            )
            self.conn.execute(
                """INSERT INTO commit_receipts(
                   commit_id,candidate_id,run_id,idempotency_key,previous_state_version,
                   committed_state_version,commit_scope,evidence_digest,created_at
                ) VALUES(?,?,?,?,?,?,?,?,?)""",
                (
                    commit_id, candidate_id, c["run_id"], c["idempotency_key"],
                    prev, new, commit_scope, evidence_digest, utc_now(),
                ),
            )
            self.conn.execute(
                "UPDATE candidates SET status='COMMITTED', reject_reason=NULL WHERE candidate_id=?",
                (candidate_id,),
            )

        self.emit_event(
            c["run_id"], "candidate.committed", c["flow_id"],
            {"candidate_id": candidate_id, "commit_id": commit_id, "state_version": new},
        )
        return dict(self.conn.execute(
            "SELECT * FROM commit_receipts WHERE commit_id=?", (commit_id,)
        ).fetchone())

    # ---------- paradigms / routes ----------

    def register_backend(self, backend_id: str, kind: str, capabilities: Any, state: Any) -> None:
        self.conn.execute(
            """INSERT INTO backend_capabilities(backend_id,kind,capabilities_json,state_json,updated_at)
               VALUES(?,?,?,?,?)
               ON CONFLICT(backend_id) DO UPDATE SET
                 kind=excluded.kind,
                 capabilities_json=excluded.capabilities_json,
                 state_json=excluded.state_json,
                 updated_at=excluded.updated_at""",
            (backend_id, kind, canonical_json(capabilities), canonical_json(state), utc_now()),
        )
        self.conn.commit()

    def create_paradigm_profile(
        self,
        run_id: str,
        region_id: str,
        *,
        context: Any,
        morphology: Any,
        dynamics: Any,
        modifiers: Any,
        confidence: float,
        evidence: Any,
    ) -> str:
        profile_id = uid("profile")
        self.conn.execute(
            """INSERT INTO paradigm_profiles(
               profile_id,run_id,region_id,context_json,morphology_json,dynamics_json,
               modifiers_json,confidence,evidence_json,created_at
            ) VALUES(?,?,?,?,?,?,?,?,?,?)""",
            (
                profile_id, run_id, region_id,
                canonical_json(context), canonical_json(morphology), canonical_json(dynamics),
                canonical_json(modifiers), float(confidence), canonical_json(evidence), utc_now(),
            ),
        )
        self.conn.commit()
        return profile_id

    def propose_route(
        self,
        run_id: str,
        region_id: str,
        *,
        profile_id: str | None,
        from_backend: str,
        to_backend: str,
        predicted_ms: float | None,
        predicted_risk: float,
        fallback_backend: str,
    ) -> str:
        route_id = uid("route")
        self.conn.execute(
            """INSERT INTO route_candidates(
               route_id,run_id,region_id,profile_id,from_backend,to_backend,predicted_ms,
               predicted_risk,status,fallback_backend,created_at
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?)""",
            (
                route_id, run_id, region_id, profile_id, from_backend, to_backend,
                predicted_ms, float(predicted_risk), "PROPOSED", fallback_backend, utc_now(),
            ),
        )
        self.conn.commit()
        self.emit_event(run_id, "route.proposed", region_id, {"route_id": route_id, "to": to_backend})
        return route_id

    @staticmethod
    def _state_equivalent(a: Any, b: Any, tolerance: float = 0.0) -> bool:
        if isinstance(a, dict) and isinstance(b, dict):
            if set(a) != set(b):
                return False
            return all(CDIRuntime._state_equivalent(a[k], b[k], tolerance) for k in a)
        if isinstance(a, list) and isinstance(b, list):
            if len(a) != len(b):
                return False
            return all(CDIRuntime._state_equivalent(x, y, tolerance) for x, y in zip(a, b))
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return math.isclose(float(a), float(b), rel_tol=tolerance, abs_tol=tolerance)
        return a == b

    def benchmark_shadow_route(
        self,
        route_id: str,
        *,
        baseline_state: Any,
        candidate_state: Any,
        baseline_ms: float,
        candidate_ms: float,
        tolerance: float = 0.0,
        details: Any | None = None,
    ) -> dict[str, Any]:
        equivalent = self._state_equivalent(baseline_state, candidate_state, tolerance)
        speedup = baseline_ms / candidate_ms if candidate_ms > 0 else 0.0
        benchmark_id = uid("bench")
        self.conn.execute(
            """INSERT INTO route_benchmarks(
               benchmark_id,route_id,baseline_ms,candidate_ms,speedup,equivalent,
               baseline_digest,candidate_digest,details_json,created_at
            ) VALUES(?,?,?,?,?,?,?,?,?,?)""",
            (
                benchmark_id, route_id, float(baseline_ms), float(candidate_ms), float(speedup), int(equivalent),
                digest(baseline_state), digest(candidate_state), canonical_json(details or {}), utc_now(),
            ),
        )
        new_status = "VERIFIED" if equivalent and candidate_ms < baseline_ms else "REJECTED"
        self.conn.execute("UPDATE route_candidates SET status=? WHERE route_id=?", (new_status, route_id))
        self.conn.commit()
        return {
            "benchmark_id": benchmark_id,
            "equivalent": equivalent,
            "speedup": speedup,
            "status": new_status,
        }

    def promote_route(self, route_id: str) -> dict[str, Any]:
        route = self.conn.execute("SELECT * FROM route_candidates WHERE route_id=?", (route_id,)).fetchone()
        if not route:
            raise KeyError(route_id)
        if route["status"] != "VERIFIED":
            return {"status": "REJECTED", "reason": "route_not_verified"}
        bench = self.conn.execute(
            "SELECT * FROM route_benchmarks WHERE route_id=? ORDER BY created_at DESC LIMIT 1",
            (route_id,),
        ).fetchone()
        if not bench or not bench["equivalent"] or bench["speedup"] <= 1.0:
            return {"status": "REJECTED", "reason": "promotion_gate_failed"}
        run = self.get_run(route["run_id"])
        route_commit_id = uid("routecommit")
        benchmark_digest = digest(dict(bench))
        self.conn.execute(
            """INSERT INTO route_receipts(
               route_commit_id,route_id,run_id,previous_backend,active_backend,
               state_version,benchmark_digest,created_at
            ) VALUES(?,?,?,?,?,?,?,?)""",
            (
                route_commit_id, route_id, route["run_id"], route["from_backend"], route["to_backend"],
                run["current_state_version"], benchmark_digest, utc_now(),
            ),
        )
        self.conn.execute("UPDATE route_candidates SET status='ACTIVE' WHERE route_id=?", (route_id,))
        self.conn.commit()
        self.emit_event(route["run_id"], "route.committed", route["region_id"], {"route_id": route_id})
        return {
            "status": "ACTIVE",
            "route_commit_id": route_commit_id,
            "active_backend": route["to_backend"],
        }

    # ---------- serialization / evidence ----------

    def record_serialization_finding(
        self,
        run_id: str,
        region_id: str,
        *,
        evidence_level: str,
        observed_serial_ms: float,
        estimated_necessary_serial_ms: float,
        confidence: float,
        blockers: list[str] | None = None,
        next_measurement: str | None = None,
    ) -> dict[str, Any]:
        gap = max(0.0, float(observed_serial_ms) - float(estimated_necessary_serial_ms))
        finding_id = uid("finding")
        self.conn.execute(
            """INSERT INTO serialization_findings(
               finding_id,run_id,region_id,evidence_level,observed_serial_ms,
               estimated_necessary_serial_ms,estimated_gap_ms,confidence,blockers_json,
               next_measurement,created_at
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?)""",
            (
                finding_id, run_id, region_id, evidence_level, observed_serial_ms,
                estimated_necessary_serial_ms, gap, confidence, canonical_json(blockers or []),
                next_measurement, utc_now(),
            ),
        )
        self.conn.commit()
        return {"finding_id": finding_id, "estimated_gap_ms": gap, "confidence": confidence}

    def import_jsonl(self, run_id: str, path: str | Path, source_type: str = "jsonl") -> int:
        path = Path(path)
        count = 0
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                event_type = (
                    obj.get("event_type")
                    or obj.get("event")
                    or obj.get("type")
                    or "external.event"
                )
                scope = obj.get("flow_id") or obj.get("scope") or obj.get("task_id")
                self.emit_event(run_id, event_type, scope, obj)
                count += 1
        self.conn.execute(
            "INSERT INTO external_imports(import_id,run_id,source_type,source_path,imported_count,created_at) VALUES(?,?,?,?,?,?)",
            (uid("import"), run_id, source_type, str(path), count, utc_now()),
        )
        self.conn.commit()
        return count

    def summary(self, run_id: str) -> dict[str, Any]:
        run = dict(self.get_run(run_id))
        counts = {}
        for table in [
            "events", "candidates", "commit_receipts", "sync_events",
            "paradigm_profiles", "route_candidates", "route_benchmarks",
            "route_receipts", "serialization_findings",
        ]:
            counts[table] = self.conn.execute(
                f"SELECT COUNT(*) AS n FROM {table} WHERE run_id=?" if table not in {"route_benchmarks"} else
                """SELECT COUNT(*) AS n FROM route_benchmarks
                   WHERE route_id IN (SELECT route_id FROM route_candidates WHERE run_id=?)""",
                (run_id,),
            ).fetchone()["n"]
        return {"run": run, "counts": counts}


def windows_capture_plan(etl_path: str = "cdi_trace.etl", export_dir: str = "wpa_export") -> dict[str, Any]:
    return {
        "note": "Run on Windows with Windows Performance Toolkit installed. Review/replace profile before production capture.",
        "start": "wpr -start GeneralProfile -filemode",
        "stop": f'wpr -stop "{etl_path}" "CDI capture"',
        "export": (
            'wpaexporter.exe -i "{etl}" -profile "<your-profile>.wpaProfile" '
            '-outputfolder "{out}"'
        ).format(etl=etl_path, out=export_dir),
        "mvp_ingest": "Normalize exported CSV/JSON to JSONL, then use `import-jsonl`.",
    }


def demo(db_path: Path) -> dict[str, Any]:
    if db_path.exists():
        db_path.unlink()
    rt = CDIRuntime(db_path)
    rt.init_db()
    run_id = rt.create_run("CDI synthetic demo", "run-demo")

    rt.register_backend(
        "cpu_serial", "CPU",
        {"parallel": False, "deterministic": True},
        {"utilization": 0.25, "available": True},
    )
    rt.register_backend(
        "cpu_parallel", "CPU",
        {"parallel": True, "deterministic": True},
        {"utilization": 0.35, "available": True},
    )

    low_vsp = rt.build_vsp(
        run_id, "relay.npc", "worker.npc.1", "npc", "npc.paths",
        anomaly=0.02, drift=0.01, conflict=0.01, uncertainty=0.03, risk=0.05, novelty=0.02,
    )
    high_vsp = rt.build_vsp(
        run_id, "relay.world", "worker.world.9", "world", "world.sync",
        anomaly=0.95, drift=0.85, conflict=0.90, uncertainty=0.85, risk=0.95, novelty=0.80,
    )

    # Commit 1 changes npc_paths.
    c1 = rt.create_candidate(
        run_id,
        task_id="npc-paths-1", region_id="npc.paths", flow_id="npc",
        producer_id="worker.npc.1", read_keys=["navmesh"], write_keys=["npc_paths"],
        output={"paths": [1, 2, 3]}, idempotency_key="npc-paths-1",
    )
    r1 = rt.commit_candidate(c1)

    # Candidate produced against v0 but reads weather only; v1 changed npc_paths,
    # therefore version mismatch is conflict-free for this candidate.
    c2 = rt.create_candidate(
        run_id,
        task_id="weather-ui", region_id="ui.weather", flow_id="ui",
        producer_id="worker.ui.1", read_keys=["weather"], write_keys=["ui_weather"],
        output={"icon": "sunny"}, idempotency_key="weather-ui",
        input_state_version=0,
    )
    r2 = rt.commit_candidate(c2)
    r2_dup = rt.commit_candidate(c2)

    # Candidate produced against v0 and reads npc_paths: relevant conflict.
    c3 = rt.create_candidate(
        run_id,
        task_id="npc-decide-stale", region_id="npc.decisions", flow_id="npc",
        producer_id="worker.npc.2", read_keys=["npc_paths"], write_keys=["npc_decisions"],
        output={"decision": "go"}, idempotency_key="npc-stale",
        input_state_version=0,
    )
    r3 = rt.commit_candidate(c3)

    # Fencing.
    token1 = rt.grant_lease(run_id, "npc", "relay.npc.A")
    c4 = rt.create_candidate(
        run_id,
        task_id="lease-test", region_id="npc.lease", flow_id="npc",
        producer_id="worker.npc.3", read_keys=[], write_keys=["npc_lease_state"],
        output={"ok": True}, idempotency_key="lease-test",
        authority_scope="npc", fencing_token=token1,
    )
    token2 = rt.grant_lease(run_id, "npc", "relay.npc.B")
    r4 = rt.commit_candidate(c4)

    # Effect barrier.
    c5 = rt.create_candidate(
        run_id,
        task_id="irreversible-spec", region_id="external.payment", flow_id="external",
        producer_id="worker.external", read_keys=[], write_keys=["external_effect"],
        output={"send": True}, idempotency_key="irreversible-spec",
        speculative=True, side_effect_class="Irreversible",
    )
    r5 = rt.commit_candidate(c5)

    profile_id = rt.create_paradigm_profile(
        run_id, "npc.paths",
        context={"resolution": "task", "time_window": "frame"},
        morphology={"substrate": "D", "update": "P", "observation": "D"},
        dynamics={"transition_law": "F"},
        modifiers={"realtime": True, "side_effect_class": "Pure"},
        confidence=0.92,
        evidence=["synthetic-profile"],
    )

    route_id = rt.propose_route(
        run_id, "npc.paths", profile_id=profile_id,
        from_backend="cpu_serial", to_backend="cpu_parallel",
        predicted_ms=20.0, predicted_risk=0.10, fallback_backend="cpu_serial",
    )
    b1 = rt.benchmark_shadow_route(
        route_id,
        baseline_state={"npc_paths": [1, 2, 3], "rng": 7},
        candidate_state={"npc_paths": [1, 2, 3], "rng": 7},
        baseline_ms=40.0,
        candidate_ms=18.0,
        details={"scenario": "synthetic-npc"},
    )
    route_receipt = rt.promote_route(route_id)

    bad_route = rt.propose_route(
        run_id, "physics", profile_id=None,
        from_backend="cpu_serial", to_backend="cpu_parallel",
        predicted_ms=10.0, predicted_risk=0.30, fallback_backend="cpu_serial",
    )
    b2 = rt.benchmark_shadow_route(
        bad_route,
        baseline_state={"x": 1.0, "rng": 4},
        candidate_state={"x": 1.5, "rng": 5},
        baseline_ms=20.0,
        candidate_ms=10.0,
        tolerance=1e-9,
        details={"expected": "GEC failure"},
    )

    finding = rt.record_serialization_finding(
        run_id, "npc.paths", evidence_level="E3",
        observed_serial_ms=40.0, estimated_necessary_serial_ms=14.0,
        confidence=0.82,
        blockers=["navmesh epoch sync"],
        next_measurement="shadow 1000 ticks",
    )

    summary = rt.summary(run_id)
    result = {
        "run_id": run_id,
        "low_regime": low_vsp["status"]["regime"],
        "high_regime": high_vsp["status"]["regime"],
        "commit1_state": r1.get("committed_state_version"),
        "nonconflicting_stale_version_commit": r2.get("committed_state_version"),
        "idempotent_same_commit": r2.get("commit_id") == r2_dup.get("commit_id"),
        "relevant_conflict_rejected": r3.get("reason") == "relevant_state_conflict",
        "stale_fencing_rejected": r4.get("reason") == "stale_fencing_token",
        "irreversible_speculation_rejected": r5.get("reason") == "effect_barrier_irreversible_speculation",
        "fencing_token_advanced": token2 > token1,
        "shadow_route_equivalent": b1["equivalent"],
        "shadow_route_speedup": b1["speedup"],
        "route_promoted": route_receipt.get("status") == "ACTIVE",
        "bad_route_rejected": b2["status"] == "REJECTED",
        "serialization_gap_ms": finding["estimated_gap_ms"],
        "summary": summary,
    }
    rt.close()
    return result


def smoke_assert(result: dict[str, Any]) -> None:
    assert result["low_regime"] == "R0"
    assert result["high_regime"] == "ESCALATE"
    assert result["commit1_state"] == 1
    assert result["nonconflicting_stale_version_commit"] == 2
    assert result["idempotent_same_commit"]
    assert result["relevant_conflict_rejected"]
    assert result["stale_fencing_rejected"]
    assert result["irreversible_speculation_rejected"]
    assert result["fencing_token_advanced"]
    assert result["shadow_route_equivalent"]
    assert result["shadow_route_speedup"] > 2.0
    assert result["route_promoted"]
    assert result["bad_route_rejected"]
    assert abs(result["serialization_gap_ms"] - 26.0) < 1e-9


def main() -> int:
    p = argparse.ArgumentParser(description="CDI Runtime + AIVS MVP")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init-db")
    p_init.add_argument("db")

    p_demo = sub.add_parser("demo")
    p_demo.add_argument("--db", default="cdi_demo.db")

    p_smoke = sub.add_parser("smoke")
    p_smoke.add_argument("--db", default="cdi_smoke.db")

    p_plan = sub.add_parser("windows-plan")
    p_plan.add_argument("--etl", default="cdi_trace.etl")
    p_plan.add_argument("--export-dir", default="wpa_export")

    p_import = sub.add_parser("import-jsonl")
    p_import.add_argument("db")
    p_import.add_argument("run_id")
    p_import.add_argument("jsonl")
    p_import.add_argument("--source-type", default="jsonl")

    args = p.parse_args()

    if args.cmd == "init-db":
        rt = CDIRuntime(args.db)
        rt.init_db()
        rt.close()
        print(args.db)
        return 0

    if args.cmd == "demo":
        result = demo(Path(args.db))
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    if args.cmd == "smoke":
        result = demo(Path(args.db))
        smoke_assert(result)
        print("PASS")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    if args.cmd == "windows-plan":
        print(json.dumps(windows_capture_plan(args.etl, args.export_dir), ensure_ascii=False, indent=2))
        return 0

    if args.cmd == "import-jsonl":
        rt = CDIRuntime(args.db)
        rt.init_db()
        n = rt.import_jsonl(args.run_id, args.jsonl, args.source_type)
        rt.close()
        print(n)
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
