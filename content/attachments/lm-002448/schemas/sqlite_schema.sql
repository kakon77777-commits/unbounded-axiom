
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS runs (
    run_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    epoch INTEGER NOT NULL DEFAULT 1,
    topology_version INTEGER NOT NULL DEFAULT 1,
    policy_version INTEGER NOT NULL DEFAULT 1,
    current_state_version INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS events (
    event_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL,
    event_type TEXT NOT NULL,
    scope TEXT,
    payload_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(run_id) REFERENCES runs(run_id)
);

CREATE TABLE IF NOT EXISTS state_changes (
    run_id TEXT NOT NULL,
    state_version INTEGER NOT NULL,
    commit_id TEXT NOT NULL,
    changed_keys_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    PRIMARY KEY(run_id, state_version)
);

CREATE TABLE IF NOT EXISTS leases (
    run_id TEXT NOT NULL,
    scope TEXT NOT NULL,
    holder_id TEXT NOT NULL,
    fencing_token INTEGER NOT NULL,
    valid_until TEXT,
    updated_at TEXT NOT NULL,
    PRIMARY KEY(run_id, scope)
);

CREATE TABLE IF NOT EXISTS candidates (
    candidate_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL,
    task_id TEXT NOT NULL,
    region_id TEXT NOT NULL,
    flow_id TEXT NOT NULL,
    producer_id TEXT NOT NULL,
    input_state_version INTEGER NOT NULL,
    epoch INTEGER NOT NULL,
    topology_version INTEGER NOT NULL,
    policy_version INTEGER NOT NULL,
    read_keys_json TEXT NOT NULL,
    write_keys_json TEXT NOT NULL,
    output_json TEXT NOT NULL,
    output_digest TEXT NOT NULL,
    dependency_status TEXT NOT NULL,
    invariant_status TEXT NOT NULL,
    semantic_status TEXT NOT NULL,
    risk REAL NOT NULL,
    speculative INTEGER NOT NULL,
    side_effect_class TEXT NOT NULL,
    authority_scope TEXT,
    fencing_token INTEGER,
    idempotency_key TEXT NOT NULL,
    status TEXT NOT NULL,
    reject_reason TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY(run_id) REFERENCES runs(run_id)
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_candidates_idem
ON candidates(run_id, idempotency_key);

CREATE TABLE IF NOT EXISTS commit_receipts (
    commit_id TEXT PRIMARY KEY,
    candidate_id TEXT NOT NULL UNIQUE,
    run_id TEXT NOT NULL,
    idempotency_key TEXT NOT NULL,
    previous_state_version INTEGER NOT NULL,
    committed_state_version INTEGER NOT NULL,
    commit_scope TEXT NOT NULL,
    evidence_digest TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(candidate_id) REFERENCES candidates(candidate_id)
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_receipts_idem
ON commit_receipts(run_id, idempotency_key);

CREATE TABLE IF NOT EXISTS sync_events (
    sync_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL,
    relay_id TEXT NOT NULL,
    flow_id TEXT NOT NULL,
    region_id TEXT,
    pressure REAL NOT NULL,
    regime TEXT NOT NULL,
    vsp_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS paradigm_profiles (
    profile_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL,
    region_id TEXT NOT NULL,
    context_json TEXT NOT NULL,
    morphology_json TEXT NOT NULL,
    dynamics_json TEXT NOT NULL,
    modifiers_json TEXT NOT NULL,
    confidence REAL NOT NULL,
    evidence_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS backend_capabilities (
    backend_id TEXT PRIMARY KEY,
    kind TEXT NOT NULL,
    capabilities_json TEXT NOT NULL,
    state_json TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS route_candidates (
    route_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL,
    region_id TEXT NOT NULL,
    profile_id TEXT,
    from_backend TEXT NOT NULL,
    to_backend TEXT NOT NULL,
    predicted_ms REAL,
    predicted_risk REAL NOT NULL,
    status TEXT NOT NULL,
    fallback_backend TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS route_benchmarks (
    benchmark_id TEXT PRIMARY KEY,
    route_id TEXT NOT NULL,
    baseline_ms REAL NOT NULL,
    candidate_ms REAL NOT NULL,
    speedup REAL NOT NULL,
    equivalent INTEGER NOT NULL,
    baseline_digest TEXT NOT NULL,
    candidate_digest TEXT NOT NULL,
    details_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS route_receipts (
    route_commit_id TEXT PRIMARY KEY,
    route_id TEXT NOT NULL UNIQUE,
    run_id TEXT NOT NULL,
    previous_backend TEXT NOT NULL,
    active_backend TEXT NOT NULL,
    state_version INTEGER NOT NULL,
    benchmark_digest TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS serialization_findings (
    finding_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL,
    region_id TEXT NOT NULL,
    evidence_level TEXT NOT NULL,
    observed_serial_ms REAL NOT NULL,
    estimated_necessary_serial_ms REAL NOT NULL,
    estimated_gap_ms REAL NOT NULL,
    confidence REAL NOT NULL,
    blockers_json TEXT NOT NULL,
    next_measurement TEXT,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS negative_routes (
    negative_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL,
    region_id TEXT NOT NULL,
    route_fingerprint TEXT NOT NULL,
    reason TEXT NOT NULL,
    benchmark_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS external_imports (
    import_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL,
    source_type TEXT NOT NULL,
    source_path TEXT NOT NULL,
    imported_count INTEGER NOT NULL,
    created_at TEXT NOT NULL
);
