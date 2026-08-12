# Standalone ON-RDSS HP/HHP regression entry point.
import json
from pathlib import Path

if __name__ == "__main__":
    p = Path(__file__).with_name("on_rdss_explicit_backward_hhp_results.json")
    data = json.loads(p.read_text(encoding="utf-8"))
    assert data["regression_assertion"]["expected_HP_true_HHP_false"] is True
    assert data["hhp_downward_closure_crosscheck"]["same_relation_as_explicit_backward"] is True
    print(json.dumps(data, ensure_ascii=False, indent=2))
