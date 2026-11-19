# -*- coding: utf-8 -*-
"""
UFPS Academic Studio: Suite de publicación académica para la Universidad Francisco de Paula Santander Seccional Ocaña.
"""

from .formats.paper import AcademicPaper
from .formats.guide import StudyGuide
from .formats.workshop import WorkshopSolution
from .formats.presentation import SlideDeck
from .core.diagrams import UFPSDiagram
from .core.compiler import compile_pdf
from .core.tokens import (
    UFPS_RED,
    UFPS_RED_DARK,
    SLATE_TITLE,
    SLATE_BODY,
    SLATE_MUTED,
    BORDER_SUBTLE,
    CHALK_CYAN
)

__version__ = "2.0.0"
__all__ = [
    "AcademicPaper",
    "StudyGuide",
    "WorkshopSolution",
    "SlideDeck",
    "UFPSDiagram",
    "compile_pdf",
    "UFPS_RED",
    "SLATE_TITLE"
]

