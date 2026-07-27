from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np


@dataclass(frozen=True)
class Patch:
    patch_id: str
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    guard_dx: float = 0.0
    guard_dy: float = 0.0

    def points(self, nx: int, ny: int) -> np.ndarray:
        xs = np.linspace(self.x_min, self.x_max, nx)
        ys = np.linspace(self.y_min, self.y_max, ny)
        return (xs[:, None] + 1j * ys[None, :]).reshape(-1)

    def to_dict(self) -> dict[str, object]:
        return asdict(self)
