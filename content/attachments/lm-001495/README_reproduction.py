"""
DMSSTT first practical fitting validation.

Input:
    qfwdt_48_case_grid.csv

Protocol:
    Double-axis holdout: each test case excludes its amplitude family and mode family.

Dynamic candidate:
    Use M = {A, initial curvature, line-length factor} first.
    Acquire S only when 0.10 < p_M < 0.90.

Important:
    This is a reanalysis of existing numerical simulations, not new physical data.
    Threshold selection is exploratory, not preregistered.
"""
