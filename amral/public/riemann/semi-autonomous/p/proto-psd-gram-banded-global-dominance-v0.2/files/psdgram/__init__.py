"""Factorized PSD Gram research prototype for banded RH certificates."""

from .cover import Patch, default_cover
from .model import build_model

__all__ = ["Patch", "build_model", "default_cover"]
