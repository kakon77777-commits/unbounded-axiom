from fractions import Fraction

from bmcc.cover import coarse_cover, coverage_audit, default_cover


def test_default_cover_has_no_rational_gap() -> None:
    audit = coverage_audit(default_cover())
    assert audit["cover_pass"]
    assert audit["covered_exactly_on_rational_atomic_cells"]
    assert audit["dense_grid_uncovered_count"] == 0
    assert audit["x_audit"]["gaps"] == []
    assert audit["y_audit"]["gaps"] == []


def test_overlaps_are_nontrivial() -> None:
    patches = default_cover()
    x0 = next(p for p in patches if p.patch_id == "X0_Y0")
    x1 = next(p for p in patches if p.patch_id == "X1_Y0")
    y0 = next(p for p in patches if p.patch_id == "X0_Y0")
    y1 = next(p for p in patches if p.patch_id == "X0_Y1")
    assert Fraction(str(x0.x_max)) > Fraction(str(x1.x_min))
    assert Fraction(str(y0.y_max)) > Fraction(str(y1.y_min))


def test_near_axis_height_bands_are_refined() -> None:
    patches = default_cover()
    far_widths = {
        Fraction(str(p.x_max)) - Fraction(str(p.x_min))
        for p in patches
        if p.patch_id.endswith("_Y0")
    }
    near_widths = {
        Fraction(str(p.x_max)) - Fraction(str(p.x_min))
        for p in patches
        if p.patch_id.endswith("_Y3")
    }
    assert far_widths == {Fraction("0.2")}
    assert near_widths == {Fraction("0.1")}


def test_coarse_cover_is_retained_as_ablation_baseline() -> None:
    patches = coarse_cover()
    assert len(patches) == 6
    assert coverage_audit(patches)["cover_pass"]
