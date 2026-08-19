# VWDC-10 Trust, Capability, Quarantine, and Reentry Schema

## Runtime trust vector

```yaml
runtime_id:
trust_epoch:
status: ACTIVE | LIMITED | PROBATION | QUARANTINED | REVOKED

trust:
  identity:
  observation:
  evidence:
  learning:
  proposal:
  certificate:
  reservation:
  commit:

capabilities:
  observe: true|false
  evidence: true|false
  learn: true|false
  propose: true|false
  certify: true|false
  reserve: true|false
  commit: true|false
  audit: true|false
  admin: true|false
```

## Influence graph node

```yaml
node_id:
node_type: capability | evidence | model | proposal | certificate | reservation | commit | actuator
owner_runtime:
protected_sink: true|false
version:
trust_epoch:
```

## Influence edge

```yaml
source:
target:
influence_type:
required: true|false
validation_gate:
provenance:
```

## Quarantine action

```yaml
incident_id:
runtime_id:
trust_epoch:
revoked_capabilities:
cut_nodes:
protected_sinks:
unblocked_paths_remaining:
historical_descendants:
availability_impact:
quorum_impact:
replay_required:
```

## Reentry packet

```yaml
runtime_id:
incident_id:
new_trust_epoch:
root_cause:
remediation:
old_keys_revoked:
fresh_keys:
fresh_attestation:
dependency_audit:
replay_status:
rtc_refresh:
safety_refresh:
probation_results:
authority_approval:
restored_capabilities:
```

## Reentry progression

```text
REVOKED
  -> FORENSIC_ONLY
  -> READ_ONLY
  -> SHADOW_PROPOSAL
  -> LIMITED_PROPOSAL
  -> CERTIFY_PROBATION
  -> FULL_ACTIVE
```

No stage is automatically granted from model accuracy alone.
