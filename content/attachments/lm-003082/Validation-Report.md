# DEST v0.8 Validation Report

**Date:** 2026-08-14

## Final mathematical-layer validation

- v0.8-specific unit tests: **9/9 PASS**
- exact pure-cascade census: **1099 ordered DAGs**, **421861 structural diminishing-return checks**, **0 violations**
- full mixed n<=4 census: **1098 DAG/status models**
- blocker-at-most-one n<=4 regression: **938 models**, **0 submodularity violations**
- minimal non-monotone witness: **2 nodes**
- minimal non-submodular witness: **3 nodes**

## Legacy runtime regression

Before the final exact-stat census test was added, the same v0.8 package completed the combined suite with **38/38 PASS**: 30 inherited Runtime tests plus 8 then-current v0.8 math tests.

After the final census statistic was added, the v0.8 math suite was rerun independently and passed **9/9**. A later attempt to rerun the full inherited runtime suite hit the tool execution time limit; no runtime module had been modified after its successful combined run. This report therefore keeps the two validation surfaces separate rather than claiming a fresh 39/39 run that did not complete.

## Exact result boundary

The pure-cascade theorem is analytic and applies to arbitrary nonnegative target weights under fixed affected sets. The n<=5 census is a computational companion.

The mixed n<=4 census uses fixed positive regression weights (invalid=0.1, release=1.0). The arbitrary-weight blocker-at-most-one result is carried by the analytic proof, not by the finite census.
