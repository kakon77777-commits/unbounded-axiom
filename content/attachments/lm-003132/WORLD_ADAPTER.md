# World-Domain Cognitive Runtime v0.1 — WORLD_ADAPTER

**Purpose:** backend protocol for converting heterogeneous simulators/environments into WDC Runnable Worlds.

---

## 1. Adapter Boundary

A backend is not WDC Core.

$$
\boxed{
WorldBackend
\neq
World-Domain Cognitive Runtime.
}
$$

The backend supplies world execution.

WDC Core supplies:

- identity;
- contract;
- lineage;
- evidence;
- authority;
- lifecycle;
- TCD integration.

---

## 2. Minimum `WorldBackend` Interface

```python
class WorldBackend:
    def capabilities(self): ...
    def instantiate(self, spec, runtime_ctx): ...
    def initialize(self): ...
    def step(self, actions=None): ...
    def observe(self, role_id=None): ...
    def checkpoint(self): ...
    def restore(self, checkpoint): ...
    def intervene(self, delta): ...
    def pause(self): ...
    def resume(self): ...
    def terminate(self, reason): ...
    def health(self): ...
```

---

## 3. Capability Manifest

Every adapter declares truthfully:

```text
exact_checkpoint: bool
deterministic_replay: bool
stochastic_seed_control: bool
causal_intervention: bool
multi_agent: bool
partial_observation: bool
persistent_world: bool
external_data_tether: bool
gpu_required: bool
network_required: bool
```

Never infer capabilities from branding.

A model called a “world model” does not automatically receive:

```text
causal_intervention = true
exact_checkpoint = true
```

---

## 4. Adapter Lifecycle

```text
instantiate(spec, context)
  -> initialize()
  -> step()*
  -> observe()*
  -> checkpoint()*
  -> intervene()*
  -> pause()/resume()*
  -> terminate()
```

---

## 5. `instantiate(spec, runtime_ctx)`

Must:

1. validate the world contract;
2. validate backend capabilities;
3. allocate isolated runtime namespace;
4. bind deterministic/stochastic seed policy;
5. bind role observation/action scopes;
6. return a runtime handle.

Must not:

- grant undeclared external permissions;
- silently change the contract;
- access sibling world state unless allowed.

---

## 6. `initialize()`

Returns initial runtime state metadata:

```text
initial_state_digest
local_time = 0
actor_instances
rng_state_digest
backend_version
contract_hash
```

---

## 7. `step(actions=None)`

Input:

```text
role_id -> action
```

or backend-specific batch mapped through adapter.

Output:

```text
new_local_time
observations
rewards/metrics if relevant
world_events
termination_state
resource_delta
```

No backend event is automatically a parent-real event.

---

## 8. `observe(role_id=None)`

Observation must be role-relative.

```text
observe(LOCAL_AGENT_1)
observe(OBSERVER)
observe(EVALUATOR)
```

may return different views.

Full backend state is not automatically exposed to every role.

---

## 9. `checkpoint()`

Checkpoint must include enough task-relevant hidden state to restore the world within declared mode.

Return:

```text
checkpoint_mode = EXACT | APPROXIMATE
state_blob
actor_state_blobs
rng_state
rules_version
backend_version
trace_offset
digest
tolerance_contract
```

---

## 10. Exact Checkpoint

`EXACT` means restore is expected to reproduce the same world state under the declared equality contract.

It does not necessarily mean every hardware bit or timing detail is identical.

Equality contract must be explicit.

---

## 11. Approximate Checkpoint

`APPROXIMATE` is valid for learned/latent worlds when exact restoration is unavailable.

Must include:

```text
state_equivalence_metric
epsilon
known_hidden_state_loss
replay_limitations
```

Approximate fork evidence must never be reported as exact paired counterfactual evidence.

---

## 12. `restore(checkpoint)`

Must validate:

```text
backend version compatibility
contract hash
state schema
actor state compatibility
RNG policy
```

After restore:

```text
query invariants
dry step if configured
```

---

## 13. `intervene(delta)`

Intervention types:

```text
PERTURBATION
CONDITIONAL_BRANCH
DO_INTERVENTION
PARAMETER_MUTATION
POLICY_MUTATION
RULE_MUTATION
```

`DO_INTERVENTION` is only legal if:

```text
capabilities.causal_intervention == true
```

and the world contract defines intervention semantics.

---

## 14. `pause()` / `resume()`

Pause must return a resumability status.

```text
PAUSABLE_EXACT
PAUSABLE_APPROXIMATE
NOT_PAUSABLE
```

The Governor needs this for preemption decisions.

---

## 15. `terminate(reason)`

Termination reason examples:

```text
TARGET_REACHED
HORIZON_REACHED
BUDGET_EXHAUSTED
GOVERNOR_KILL
SAFETY_KILL
RUNTIME_FAILURE
INVALID_CONTRACT
NO_PROGRESS
```

Termination is not deletion.

---

## 16. `health()`

At minimum:

```text
alive
responsive
resource_usage
local_time
last_event_time
checkpoint_health
```

---

## 17. Optional Methods

```python
def batch_step(self, action_batches): ...
def snapshot_metrics(self): ...
def estimate_cost(self, requested_horizon): ...
def supports_exact_fork(self): ...
def validate_checkpoint(self, checkpoint): ...
```

---

## 18. Adapter Runtime Context

`runtime_ctx` should provide only scoped services:

```text
world_id
run_id
role_cards
event_sink
blob_store
budget_handle
sandbox_handle
clock_handle
allowed_channels
external_tool_proxy_handle_or_none
```

Never give raw host credentials to the world backend.

---

## 19. PythonStateWorld Reference Backend

v0.1 first backend.

Requirements:

```text
state JSON/msgpack serializable
transition function explicit
seed policy controllable
exact checkpoint
exact restore
no external network
no host filesystem access except scoped blob API
```

Example contract:

```python
class GridState(TypedDict):
    position: tuple[int, int]
    inventory: dict[str, int]
    doors: dict[str, bool]
    hazards: dict[str, bool]
```

Transition:

```python
next_state, events = transition(state, actions, rng)
```

---

## 20. PettingZoo Adapter

Purpose:

- multi-agent local roles;
- sequential AEC environments;
- simultaneous Parallel environments;
- agent-specific observations and actions.

WDC-specific additions:

```text
RoleCard mapping
world/run IDs
checkpoint contract
branch visibility
evidence event mapping
```

PettingZoo itself is not the WDC lineage/evidence layer.

---

## 21. ExternalProcessAdapter

Purpose:

- CLI simulators;
- theorem provers;
- scientific solvers;
- existing engines.

Contract example:

```text
prepare working directory
write input manifest
launch process
capture stdout/stderr
collect artifacts
parse result
checkpoint if backend supports
terminate process group
```

Must use scoped work directories.

---

## 22. LearnedWorldAdapter

Future adapter for learned latent or generative worlds.

Must explicitly declare uncertainty and limitations.

Common capability profile may be:

```text
exact_checkpoint = false
deterministic_replay = false
causal_intervention = false
partial_observation = true
persistent_world = backend-dependent
```

Do not upgrade evidence semantics merely because the output is visually coherent.

---

## 23. Adapter Sandbox Contract

Risk class selects sandbox:

```text
S0_INPROCESS
S1_PROCESS
S2_CONTAINER
S3_GVISOR
S4_MICROVM
```

Adapter receives a sandbox handle, not unrestricted host access.

---

## 24. Filesystem Contract

World-local path:

```text
/wdc/world/<world_id>/run/<run_id>/
```

Prefer ephemeral writable layer.

Shared immutable assets may be mounted read-only.

Parent host paths must not be directly visible by default.

---

## 25. Network Contract

Default:

```text
DENY
```

Optional policies:

```text
DENY
ALLOWLIST
PROXY_ONLY
FULL   # discouraged; requires explicit authority
```

---

## 26. External Tool Contract

World code requests:

```text
ExternalActionRequest
```

It cannot directly execute real actions.

The adapter forwards to `ExternalToolProxy` only if its role contract allows requests.

---

## 27. Resource Contract

Adapter must report requested and used resources:

```text
cpu
gpu
memory
storage
steps
walltime
tokens if applicable
```

Hard limits must produce explicit termination/failure events.

---

## 28. Forkability Contract

Adapter must expose:

```text
forkability = EXACT | APPROXIMATE | NONE
```

`EXACT` requires validated checkpoint restore.

`APPROXIMATE` requires tolerance and hidden-state caveats.

---

## 29. Replayability Contract

```text
replayability = DETERMINISTIC | DISTRIBUTIONAL | NONE
```

`DISTRIBUTIONAL` means repeated runs are expected to reproduce a distribution, not the same trace.

---

## 30. Adapter Event Mapping

Backend-specific events map to WDC events.

Example:

```text
engine: object_destroyed(id=42)
    ->
WDC WORLD_LOCAL:
WorldObjectDestroyed(
  world_id,
  run_id,
  object_id=42
)
```

The adapter must not classify this as `EXTERNAL_REAL`.

---

## 31. Adapter Evidence Mapping

Backend may produce raw outputs.

Evaluator / Evidence Engine decides whether an output becomes:

```text
SUPPORT
COUNTER
INCONCLUSIVE
INVALID
```

Adapter itself should not silently label scientific truth.

---

## 32. Adapter Contract Test Suite

Every adapter must pass:

```text
test_capability_manifest_complete
test_instantiate_contract_hash
test_initialize_scope
test_step_advances_local_time
test_observe_is_role_relative
test_checkpoint_roundtrip_if_exact
test_approx_checkpoint_has_tolerance
test_intervention_capability_enforced
test_pause_resume_contract
test_termination_reason
test_resource_limit_event
test_event_scope_world_local
test_no_host_credential_access
test_no_sibling_access_by_default
```

---

## 33. PythonStateWorld Acceptance Test

A valid reference backend must demonstrate:

```text
create world
run 10 steps
checkpoint at step 5
restore checkpoint
fork child
apply different action
prove shared prefix
prove post-fork divergence
produce evidence packet
terminate both runs
```

---

## 34. Adapter Registration

```python
registry.register(
    backend_type="python_state",
    factory=PythonStateWorld,
    capability_manifest=...
)
```

A `WorldSpec` references only registered backend types.

---

## 35. Backward Compatibility

Backend version changes that can alter execution semantics require a new `backend_version`.

Re-running an old `WorldSpec` with a new backend must be an explicit new run provenance condition.

---

## 36. Adapter Anti-Patterns

Do not:

- put Governor logic inside the simulator;
- give every adapter host credentials;
- infer causality from a generative model;
- call rendered frame equality “same world state”;
- expose full world state to all local agents;
- treat process exit code 0 as evidence validity;
- hide backend version changes;
- pretend an approximate fork is exact.
