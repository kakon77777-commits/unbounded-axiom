# DEST v0.9 Validation Report

**Date:** 2026-08-14

## v0.8 inherited theorem regression

Exit code: **0**

```text

Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/generated/interface/models.py", line 32317, in hydrate_crdt_from_proto
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/rpc/remote.py", line 749, in __call__
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
test_blocker_leq_one_census_n4 (tests.test_v08_math.V08MathTests.test_blocker_leq_one_census_n4) ... ok
test_exact_pure_census_n4 (tests.test_v08_math.V08MathTests.test_exact_pure_census_n4) ... ok
test_full_mixed_census_exact_stats_n4 (tests.test_v08_math.V08MathTests.test_full_mixed_census_exact_stats_n4) ... ok
test_minimal_counterexamples_found (tests.test_v08_math.V08MathTests.test_minimal_counterexamples_found) ... ok
test_one_blocker_release_term_is_submodular (tests.test_v08_math.V08MathTests.test_one_blocker_release_term_is_submodular) ... ok
test_pure_small_example_is_monotone_submodular (tests.test_v08_math.V08MathTests.test_pure_small_example_is_monotone_submodular) ... ok
test_three_node_mixed_nonsubmodularity (tests.test_v08_math.V08MathTests.test_three_node_mixed_nonsubmodularity) ... ok
test_two_blocker_release_term_is_not_submodular (tests.test_v08_math.V08MathTests.test_two_blocker_release_term_is_not_submodular) ... ok
test_two_node_mixed_nonmonotonicity (tests.test_v08_math.V08MathTests.test_two_node_mixed_nonmonotonicity) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.968s

OK

```

## v0.9 breakdown regression

Exit code: **0**

```text

Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/generated/interface/models.py", line 32317, in hydrate_crdt_from_proto
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/rpc/remote.py", line 749, in __call__
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
test_adaptive_grid_minimum_denominator_two (tests.test_v09_breakdown.V09BreakdownTests.test_adaptive_grid_minimum_denominator_two) ... ok
test_correlated_two_item_adaptive_violation (tests.test_v09_breakdown.V09BreakdownTests.test_correlated_two_item_adaptive_violation) ... ok
test_deadline_order_break (tests.test_v09_breakdown.V09BreakdownTests.test_deadline_order_break) ... ok
test_deadline_small_census_has_order_sensitive_cases (tests.test_v09_breakdown.V09BreakdownTests.test_deadline_small_census_has_order_sensitive_cases) ... ok
test_dynamic_cost_changes_feasibility (tests.test_v09_breakdown.V09BreakdownTests.test_dynamic_cost_changes_feasibility) ... ok
test_exact_independent_grid (tests.test_v09_breakdown.V09BreakdownTests.test_exact_independent_grid) ... ok
test_independent_modular_marginal_invariant (tests.test_v09_breakdown.V09BreakdownTests.test_independent_modular_marginal_invariant) ... ok
test_mixed_minimal_breaks_preserved (tests.test_v09_breakdown.V09BreakdownTests.test_mixed_minimal_breaks_preserved) ... ok
test_one_item_time_break (tests.test_v09_breakdown.V09BreakdownTests.test_one_item_time_break) ... ok
test_property_matrix_distinguishes_false_from_na (tests.test_v09_breakdown.V09BreakdownTests.test_property_matrix_distinguishes_false_from_na) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.003s

OK

```

## Exact executable census

- correlated binary joint distributions through denominator 8: **494**
- adaptive-submodularity violations: **170**
- minimum violating denominator: **2**
- independent modular conditional checks: **722**
- independent modular violations: **0**
- two-job deadline models: **4**
- order-sensitive deadline models: **2**

Finite census is a verification companion. The general statements rely on the theorem/counterexample arguments in the paper, not on finite enumeration alone.