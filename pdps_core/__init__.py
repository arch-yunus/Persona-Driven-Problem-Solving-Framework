"""
PDPS-Core: Persona-Driven Problem Solving Framework

A philosophical alternative to modern development methodologies like Agile, Scrum, or Kanban.
Based on the three prophetic personas: Yunus, Yusuf, and Musa.
"""

__version__ = "0.1.0"
__author__ = "PDPS-Core Team"

from .core import PDPSFramework
from .personas import YunusPersona, YusufPersona, MusaPersona

__all__ = [
    "PDPSFramework",
    "YunusPersona",
    "YusufPersona",
    "MusaPersona",
]
