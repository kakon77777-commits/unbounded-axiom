#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Logic Matrix Corpus Engine — entry point.

The build pipeline was refactored (Phase 1) from this single monolith into the
modular package under scripts/:

    scripts/config.py      configuration constants
    scripts/helpers.py     slug / escaping / mime / language / disclaimer
    scripts/render.py      markdown & source rendering, body/raw-text extraction
    scripts/generators.py  all dist/ output generators
    scripts/build.py       build orchestrator (main)

This file is kept as the stable entry point. Equivalent invocations:

    python build.py
    python scripts/build.py
    python -m scripts.build
"""
from scripts.build import main

if __name__ == "__main__":
    main()
