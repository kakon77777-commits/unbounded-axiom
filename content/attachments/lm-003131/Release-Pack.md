# VWDC-10 — Byzantine-Resilient World Federation, Trust Domains, and Fault Containment

## Core trust rule

$$
\boxed{
\text{trust capabilities separately}.
}
$$

## Capability chain

```text
OBSERVE
EVIDENCE
LEARN
PROPOSE
CERTIFY
RESERVE
COMMIT
```

## Containment theorem

If quarantine set $Q$ intersects every directed path from compromised capability sources $S$ to protected sinks $T$, then no such future path remains in:

$$
G_{\mathrm{inf}}\setminus Q.
$$

## Core caveat

$$
\boxed{
\text{future containment}
\not\Rightarrow
\text{past decontamination}.
}
$$

## Reentry rule

Reentry requires fresh integrity/keys/remediation/dependency replay/RTC-safety validation/probation/authority gates.

Model accuracy alone is insufficient.

## Package contents

- canonical paper;
- literature audit;
- trust/quarantine schema;
- roadmap;
- VWDC-11 handoff;
- theorem index;
- regression tests;
- validation;
- checksums.
