from __future__ import annotations

import json
from pathlib import Path

from interval_cert.certificate import build_certificate


ROOT = Path(__file__).resolve().parent


def main() -> None:
    witness = json.loads(
        (
            ROOT
            / "data"
            / "rational_atomic_witness_v0.6.json"
        ).read_text(encoding="utf-8")
    )
    certificate = build_certificate(witness)
    output = ROOT / "outputs" / "interval_atomic_certificate.json"
    output.write_text(
        json.dumps(
            certificate,
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": output.name,
                "neumann_defect_upper": certificate["proof"][
                    "neumann_defect_infinity_norm_upper"
                ],
                "first_minor_lower": certificate["proof"][
                    "first_leading_minor_lower"
                ],
                "determinant_lower": certificate["proof"][
                    "determinant_lower"
                ],
                "abstract_continuous_interval_certificate": (
                    certificate["classification"][
                        "abstract_continuous_interval_certificate"
                    ]
                ),
                "global_rh_certificate": False,
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()

