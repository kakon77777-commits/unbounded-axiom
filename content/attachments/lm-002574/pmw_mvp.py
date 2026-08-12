#!/usr/bin/env python3
"""
PMW Runtime MVP v0.1
Single-process SQLite proof-of-concept.

Purpose:
- Stable Agent IDs
- Append-only event log
- Versioned shared state with compare-and-set
- Scoped memory
- Idempotent wake events
- Handoffs
- Decision receipts
- Minimal topology edges

This is intentionally small. It is not production security code.
"""

from __future__ import annotations

import json
import sqlite3
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional


def now() -> float:
    return time.time()


def uid(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex}"


class VersionConflict(RuntimeError):
    pass


class PMW:
    def __init__(self, db_path: str = ":memory:"):
        self.db = sqlite3.connect(db_path)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys = ON")
        self._init_schema()

    def _init_schema(self) -> None:
        self.db.executescript(
            """
            CREATE TABLE IF NOT EXISTS agents (
                agent_id TEXT PRIMARY KEY,
                display_name TEXT NOT NULL,
                role_id TEXT,
                status TEXT NOT NULL DEFAULT 'SLEEPING',
                capabilities_json TEXT NOT NULL DEFAULT '{}',
                permissions_json TEXT NOT NULL DEFAULT '{}',
                last_seen REAL NOT NULL
            );

            CREATE TABLE IF NOT EXISTS events (
                event_id TEXT PRIMARY KEY,
                event_type TEXT NOT NULL,
                actor_id TEXT,
                payload_json TEXT NOT NULL,
                parent_event_id TEXT,
                causation_event_id TEXT,
                state_version INTEGER,
                created_at REAL NOT NULL
            );

            CREATE TABLE IF NOT EXISTS shared_state (
                key TEXT PRIMARY KEY,
                value_json TEXT NOT NULL,
                version INTEGER NOT NULL,
                updated_by TEXT,
                updated_at REAL NOT NULL
            );

            CREATE TABLE IF NOT EXISTS tasks (
                task_id TEXT PRIMARY KEY,
                goal TEXT NOT NULL,
                owner_agent TEXT,
                status TEXT NOT NULL,
                version INTEGER NOT NULL DEFAULT 1,
                dependencies_json TEXT NOT NULL DEFAULT '[]',
                constraints_json TEXT NOT NULL DEFAULT '[]',
                updated_at REAL NOT NULL
            );

            CREATE TABLE IF NOT EXISTS memory (
                memory_id TEXT PRIMARY KEY,
                owner_agent TEXT,
                scope TEXT NOT NULL,
                epistemic_type TEXT NOT NULL,
                content TEXT NOT NULL,
                status TEXT NOT NULL,
                confidence REAL,
                source_refs_json TEXT NOT NULL DEFAULT '[]',
                created_at REAL NOT NULL
            );

            CREATE TABLE IF NOT EXISTS wake_events (
                wake_id TEXT PRIMARY KEY,
                target_agent TEXT NOT NULL,
                cause TEXT NOT NULL,
                status TEXT NOT NULL,
                payload_json TEXT NOT NULL,
                idempotency_key TEXT NOT NULL UNIQUE,
                not_before REAL NOT NULL,
                created_at REAL NOT NULL
            );

            CREATE TABLE IF NOT EXISTS handoffs (
                handoff_id TEXT PRIMARY KEY,
                source_agent TEXT NOT NULL,
                target_agent TEXT NOT NULL,
                task_id TEXT NOT NULL,
                status TEXT NOT NULL,
                payload_json TEXT NOT NULL,
                created_at REAL NOT NULL
            );

            CREATE TABLE IF NOT EXISTS decision_receipts (
                receipt_id TEXT PRIMARY KEY,
                wake_id TEXT,
                agent_id TEXT NOT NULL,
                task_id TEXT,
                decision TEXT NOT NULL,
                base_state_version INTEGER,
                result_state_version INTEGER,
                payload_json TEXT NOT NULL,
                created_at REAL NOT NULL
            );

            CREATE TABLE IF NOT EXISTS topology_edges (
                source_agent TEXT NOT NULL,
                target_agent TEXT NOT NULL,
                edge_type TEXT NOT NULL,
                scope TEXT NOT NULL DEFAULT 'PROJECT',
                weight REAL NOT NULL DEFAULT 1.0,
                topology_version INTEGER NOT NULL,
                active INTEGER NOT NULL DEFAULT 1,
                PRIMARY KEY (source_agent, target_agent, edge_type, topology_version)
            );
            """
        )
        self.db.commit()

    def register_agent(
        self,
        display_name: str,
        role_id: str = "",
        capabilities: Optional[dict[str, Any]] = None,
        permissions: Optional[dict[str, Any]] = None,
        agent_id: Optional[str] = None,
    ) -> str:
        agent_id = agent_id or uid("agent")
        self.db.execute(
            """
            INSERT INTO agents
            (agent_id, display_name, role_id, capabilities_json, permissions_json, last_seen)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                agent_id,
                display_name,
                role_id,
                json.dumps(capabilities or {}),
                json.dumps(permissions or {}),
                now(),
            ),
        )
        self.db.commit()
        return agent_id

    def append_event(
        self,
        event_type: str,
        payload: dict[str, Any],
        actor_id: Optional[str] = None,
        parent_event_id: Optional[str] = None,
        causation_event_id: Optional[str] = None,
        state_version: Optional[int] = None,
    ) -> str:
        event_id = uid("evt")
        self.db.execute(
            """
            INSERT INTO events
            (event_id, event_type, actor_id, payload_json,
             parent_event_id, causation_event_id, state_version, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                event_id,
                event_type,
                actor_id,
                json.dumps(payload),
                parent_event_id,
                causation_event_id,
                state_version,
                now(),
            ),
        )
        self.db.commit()
        return event_id

    def get_state(self, key: str) -> tuple[Any, int] | None:
        row = self.db.execute(
            "SELECT value_json, version FROM shared_state WHERE key = ?",
            (key,),
        ).fetchone()
        if not row:
            return None
        return json.loads(row["value_json"]), row["version"]

    def compare_and_set_state(
        self,
        key: str,
        new_value: Any,
        expected_version: int,
        actor_id: Optional[str] = None,
    ) -> int:
        current = self.get_state(key)
        if current is None:
            if expected_version != 0:
                raise VersionConflict(
                    f"{key}: expected {expected_version}, current absent"
                )
            new_version = 1
            self.db.execute(
                """
                INSERT INTO shared_state
                (key, value_json, version, updated_by, updated_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (key, json.dumps(new_value), new_version, actor_id, now()),
            )
        else:
            _, current_version = current
            if current_version != expected_version:
                raise VersionConflict(
                    f"{key}: expected {expected_version}, current {current_version}"
                )
            new_version = current_version + 1
            cur = self.db.execute(
                """
                UPDATE shared_state
                SET value_json = ?, version = ?, updated_by = ?, updated_at = ?
                WHERE key = ? AND version = ?
                """,
                (
                    json.dumps(new_value),
                    new_version,
                    actor_id,
                    now(),
                    key,
                    current_version,
                ),
            )
            if cur.rowcount != 1:
                raise VersionConflict(f"{key}: concurrent state mutation")
        self.db.commit()
        self.append_event(
            "STATE_UPDATED",
            {"key": key, "new_version": new_version},
            actor_id=actor_id,
            state_version=new_version,
        )
        return new_version

    def create_task(
        self,
        goal: str,
        owner_agent: Optional[str] = None,
        constraints: Optional[list[str]] = None,
    ) -> str:
        task_id = uid("task")
        self.db.execute(
            """
            INSERT INTO tasks
            (task_id, goal, owner_agent, status, constraints_json, updated_at)
            VALUES (?, ?, ?, 'ACTIVE', ?, ?)
            """,
            (task_id, goal, owner_agent, json.dumps(constraints or []), now()),
        )
        self.db.commit()
        self.append_event(
            "TASK_CREATED",
            {"task_id": task_id, "goal": goal},
            actor_id=owner_agent,
        )
        return task_id

    def store_memory(
        self,
        owner_agent: str,
        scope: str,
        epistemic_type: str,
        content: str,
        status: str = "ACTIVE",
        confidence: Optional[float] = None,
        source_refs: Optional[list[str]] = None,
    ) -> str:
        memory_id = uid("mem")
        self.db.execute(
            """
            INSERT INTO memory
            (memory_id, owner_agent, scope, epistemic_type, content,
             status, confidence, source_refs_json, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                memory_id,
                owner_agent,
                scope,
                epistemic_type,
                content,
                status,
                confidence,
                json.dumps(source_refs or []),
                now(),
            ),
        )
        self.db.commit()
        return memory_id

    def list_memories(self, requesting_agent: str) -> list[dict[str, Any]]:
        rows = self.db.execute(
            """
            SELECT * FROM memory
            WHERE scope != 'PRIVATE' OR owner_agent = ?
            ORDER BY created_at
            """,
            (requesting_agent,),
        ).fetchall()
        return [dict(r) for r in rows]

    def enqueue_wake(
        self,
        target_agent: str,
        cause: str,
        payload: Optional[dict[str, Any]] = None,
        idempotency_key: Optional[str] = None,
        not_before: Optional[float] = None,
    ) -> str:
        key = idempotency_key or uid("idem")
        existing = self.db.execute(
            "SELECT wake_id FROM wake_events WHERE idempotency_key = ?",
            (key,),
        ).fetchone()
        if existing:
            return existing["wake_id"]

        wake_id = uid("wake")
        self.db.execute(
            """
            INSERT INTO wake_events
            (wake_id, target_agent, cause, status, payload_json,
             idempotency_key, not_before, created_at)
            VALUES (?, ?, ?, 'PENDING', ?, ?, ?, ?)
            """,
            (
                wake_id,
                target_agent,
                cause,
                json.dumps(payload or {}),
                key,
                not_before or now(),
                now(),
            ),
        )
        self.db.commit()
        return wake_id

    def claim_wake(self, target_agent: str) -> Optional[dict[str, Any]]:
        row = self.db.execute(
            """
            SELECT * FROM wake_events
            WHERE target_agent = ? AND status = 'PENDING' AND not_before <= ?
            ORDER BY created_at
            LIMIT 1
            """,
            (target_agent, now()),
        ).fetchone()
        if not row:
            return None
        self.db.execute(
            "UPDATE wake_events SET status = 'CLAIMED' WHERE wake_id = ?",
            (row["wake_id"],),
        )
        self.db.commit()
        return dict(row)

    def ack_wake(self, wake_id: str, status: str = "ACKED") -> None:
        self.db.execute(
            "UPDATE wake_events SET status = ? WHERE wake_id = ?",
            (status, wake_id),
        )
        self.db.commit()

    def create_handoff(
        self,
        source_agent: str,
        target_agent: str,
        task_id: str,
        payload: Optional[dict[str, Any]] = None,
    ) -> str:
        handoff_id = uid("handoff")
        self.db.execute(
            """
            INSERT INTO handoffs
            (handoff_id, source_agent, target_agent, task_id, status, payload_json, created_at)
            VALUES (?, ?, ?, ?, 'PENDING', ?, ?)
            """,
            (
                handoff_id,
                source_agent,
                target_agent,
                task_id,
                json.dumps(payload or {}),
                now(),
            ),
        )
        self.db.commit()
        self.append_event(
            "HANDOFF_CREATED",
            {
                "handoff_id": handoff_id,
                "source": source_agent,
                "target": target_agent,
                "task_id": task_id,
            },
            actor_id=source_agent,
        )
        return handoff_id

    def write_receipt(
        self,
        agent_id: str,
        decision: str,
        wake_id: Optional[str] = None,
        task_id: Optional[str] = None,
        base_state_version: Optional[int] = None,
        result_state_version: Optional[int] = None,
        payload: Optional[dict[str, Any]] = None,
    ) -> str:
        receipt_id = uid("receipt")
        self.db.execute(
            """
            INSERT INTO decision_receipts
            (receipt_id, wake_id, agent_id, task_id, decision,
             base_state_version, result_state_version, payload_json, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                receipt_id,
                wake_id,
                agent_id,
                task_id,
                decision,
                base_state_version,
                result_state_version,
                json.dumps(payload or {}),
                now(),
            ),
        )
        self.db.commit()
        return receipt_id

    def set_topology_edge(
        self,
        source_agent: str,
        target_agent: str,
        edge_type: str,
        topology_version: int,
        scope: str = "PROJECT",
        weight: float = 1.0,
        active: bool = True,
    ) -> None:
        self.db.execute(
            """
            INSERT OR REPLACE INTO topology_edges
            (source_agent, target_agent, edge_type, scope, weight, topology_version, active)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                source_agent,
                target_agent,
                edge_type,
                scope,
                weight,
                topology_version,
                int(active),
            ),
        )
        self.db.commit()

    def get_topology(self, topology_version: Optional[int] = None) -> list[dict[str, Any]]:
        if topology_version is None:
            row = self.db.execute(
                "SELECT MAX(topology_version) AS v FROM topology_edges"
            ).fetchone()
            topology_version = row["v"] if row and row["v"] is not None else 0
        rows = self.db.execute(
            """
            SELECT * FROM topology_edges
            WHERE topology_version = ? AND active = 1
            """,
            (topology_version,),
        ).fetchall()
        return [dict(r) for r in rows]


def smoke_test() -> None:
    pmw = PMW(":memory:")

    a = pmw.register_agent("Agent A", role_id="research")
    b = pmw.register_agent("Agent B", role_id="review")

    task = pmw.create_task(
        "Validate PMW cross-agent continuity",
        owner_agent=a,
        constraints=["Do not expose PRIVATE memory"],
    )

    v1 = pmw.compare_and_set_state(
        "phase",
        {"name": "research"},
        expected_version=0,
        actor_id=a,
    )
    assert v1 == 1

    private_mem = pmw.store_memory(
        owner_agent=a,
        scope="PRIVATE",
        epistemic_type="HYPOTHESIS",
        content="A private hypothesis",
        confidence=0.6,
    )

    visible_to_b = pmw.list_memories(b)
    assert all(m["memory_id"] != private_mem for m in visible_to_b)

    handoff = pmw.create_handoff(
        source_agent=a,
        target_agent=b,
        task_id=task,
        payload={"state_key": "phase"},
    )
    assert handoff

    w1 = pmw.enqueue_wake(
        b,
        cause="HANDOFF",
        payload={"handoff_id": handoff},
        idempotency_key="same-event",
    )
    w2 = pmw.enqueue_wake(
        b,
        cause="HANDOFF_RETRY",
        payload={"handoff_id": handoff},
        idempotency_key="same-event",
    )
    assert w1 == w2

    claimed = pmw.claim_wake(b)
    assert claimed and claimed["wake_id"] == w1

    v2 = pmw.compare_and_set_state(
        "phase",
        {"name": "review"},
        expected_version=1,
        actor_id=b,
    )
    assert v2 == 2

    stale_detected = False
    try:
        pmw.compare_and_set_state(
            "phase",
            {"name": "stale-write"},
            expected_version=1,
            actor_id=a,
        )
    except VersionConflict:
        stale_detected = True
    assert stale_detected

    pmw.set_topology_edge(
        a,
        b,
        edge_type="SHARE",
        topology_version=1,
    )
    assert len(pmw.get_topology()) == 1

    receipt = pmw.write_receipt(
        agent_id=b,
        decision="ACTION",
        wake_id=w1,
        task_id=task,
        base_state_version=1,
        result_state_version=2,
        payload={"note": "handoff processed"},
    )
    assert receipt

    pmw.ack_wake(w1)

    event_count = pmw.db.execute(
        "SELECT COUNT(*) AS n FROM events"
    ).fetchone()["n"]
    assert event_count >= 4

    print("PMW MVP smoke test: PASS")
    print(f"agents=2 task={task}")
    print(f"state_phase_version={pmw.get_state('phase')[1]}")
    print(f"events={event_count}")
    print(f"wake_idempotent={w1 == w2}")
    print(f"private_memory_isolated=True")
    print(f"stale_state_detected={stale_detected}")


if __name__ == "__main__":
    smoke_test()
