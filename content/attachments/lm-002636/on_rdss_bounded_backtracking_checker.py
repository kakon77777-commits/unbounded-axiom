# ON-RDSS bounded-backtracking regression checker.
# Reads the generated result bundle and verifies the expected monotone hierarchy
# on the classical HP-not-HHP regression fixture.

import json
from pathlib import Path

if __name__ == "__main__":
    p = Path(__file__).with_name("on_rdss_bounded_backtracking_results.json")
    data = json.loads(p.read_text(encoding="utf-8"))

    levels = data["classical_fixture_levels"]
    assert levels[0]["initial_related"] is True       # BHHP_0 = HP
    assert levels[1]["initial_related"] is False      # one-step mapped backtracking separates this fixture
    assert data["monotone_relation_sizes"] is True
    print(json.dumps(data, ensure_ascii=False, indent=2))
