from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class OutputTests(unittest.TestCase):
    def test_saved_output_verification(self) -> None:
        output = json.loads(
            (ROOT / "outputs" / "output_verification.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertTrue(output["verification_pass"])
        self.assertFalse(output["global_rh_certificate"])
