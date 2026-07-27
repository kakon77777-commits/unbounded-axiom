from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class NotchCode:
    code_id: str
    value_points: tuple[float, ...]
    derivative_points: tuple[float, ...] = ()
    interpretation: str = ""


def atlas_primary_peaks(atlas: dict[str, Any]) -> dict[str, float]:
    return {
        row["band_id"]: round(
            float(row["primary_peak"]["x"]),
            2,
        )
        for row in atlas["band_rows"]
    }


def resolve_codes(
    patch_center: float,
    patch_x_min: float,
    patch_x_max: float,
    atlas: dict[str, Any],
) -> list[NotchCode]:
    center = round(float(patch_center), 6)
    peaks = atlas_primary_peaks(atlas)
    return [
        NotchCode(
            "baseline",
            (),
            interpretation="No added real-axis notch.",
        ),
        NotchCode(
            "anchor1",
            (center,),
            interpretation=(
                "Force G to vanish at the patch real center; preserve "
                "the first derivative that generates the local "
                "negative square."
            ),
        ),
        NotchCode(
            "anchor_A3",
            (center, peaks["A3"]),
            interpretation="Patch anchor plus the recurrent A3 peak.",
        ),
        NotchCode(
            "anchor_A4",
            (center, peaks["A4"]),
            interpretation="Patch anchor plus the recurrent A4 peak.",
        ),
        NotchCode(
            "atlas3",
            (center, peaks["A3"], peaks["A4"]),
            interpretation=(
                "Patch anchor plus recurrent distant A3 and A4 peaks."
            ),
        ),
        NotchCode(
            "harmonic3",
            (center, 2.0 * center, 4.0 * center),
            interpretation=(
                "Patch anchor and exact second/fourth harmonics; "
                "tests whether the observed peaks are truly harmonic."
            ),
        ),
        NotchCode(
            "five_band",
            (
                peaks["A0"],
                center,
                peaks["A2"],
                peaks["A3"],
                peaks["A4"],
            ),
            interpretation=(
                "One designed zero in every charged band, with A1 "
                "locked to the patch center."
            ),
        ),
        NotchCode(
            "atlas5",
            tuple(peaks[f"A{index}"] for index in range(5)),
            interpretation=(
                "Use all five global atlas peaks without adapting A1 "
                "to the patch."
            ),
        ),
        NotchCode(
            "edge_pair",
            (
                round(float(patch_x_min), 6),
                round(float(patch_x_max), 6),
            ),
            interpretation=(
                "Zeros at both real edges of the subpatch; an "
                "ablation for derivative suppression by close zeros."
            ),
        ),
        NotchCode(
            "anchor_flat",
            (center,),
            (center,),
            interpretation=(
                "Force both G and G' to vanish at the patch center; "
                "Taylor-sign ablation expected to be harmful."
            ),
        ),
    ]
