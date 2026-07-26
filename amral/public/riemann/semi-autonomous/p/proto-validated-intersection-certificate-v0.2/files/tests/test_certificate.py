from pathlib import Path

from validated_certificate.certificate import run_certificate


def test_supplied_certificate(tmp_path: Path):
    root = Path(__file__).resolve().parents[1]
    result = run_certificate(root / "examples/certificate.json", tmp_path)
    assert result["strict_intersection_certificate_passed"]
    assert result["region"]["unresolved_cell_count"] == 0
    assert result["region"]["global_block_upper"] < 0
    assert result["arithmetic"]["arithmetic_total_interval"][0] > 0
    assert result["arithmetic"]["prime_power_count"] == 98
