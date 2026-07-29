"""
core.levels
============
The five maturity levels of the model, adapted from the CMMI staged scale
(CMMI Product Team, 2010) for agentic-AI governance.

Reference: Table 3.2 in Chapter Three of the project thesis.
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class MaturityLevel:
    number: int              # 1 through 5
    name: str                # CMMI-aligned name
    general_descriptor: str  # what maturity at this level looks like in general


LEVEL_1 = MaturityLevel(
    number=1,
    name="Ad hoc",
    general_descriptor=(
        "No agentic-AI governance. Agents, where present, run without documented "
        "oversight, identity controls, or escalation paths."
    ),
)

LEVEL_2 = MaturityLevel(
    number=2,
    name="Initial",
    general_descriptor=(
        "Some written policy exists. Controls are manual, inconsistent, and not "
        "tied to named NDPA or GAID obligations."
    ),
)

LEVEL_3 = MaturityLevel(
    number=3,
    name="Defined",
    general_descriptor=(
        "Documented controls, assigned roles, and tested escalation paths cover "
        "every dimension. Controls map to named regulatory anchors."
    ),
)

LEVEL_4 = MaturityLevel(
    number=4,
    name="Managed",
    general_descriptor=(
        "Controls are monitored continuously. Audit logs, identity checks, and "
        "kill-switch drills run on a routine schedule."
    ),
)

LEVEL_5 = MaturityLevel(
    number=5,
    name="Optimising",
    general_descriptor=(
        "Governance adapts. The institution runs learning loops, red-team "
        "exercises, and prospective reviews ahead of new agent deployments."
    ),
)


ALL_LEVELS: Tuple[MaturityLevel, ...] = (LEVEL_1, LEVEL_2, LEVEL_3, LEVEL_4, LEVEL_5)


def get_level(number: int) -> MaturityLevel:
    """Return the MaturityLevel with the given number (1 through 5)."""
    if number < 1 or number > 5:
        raise ValueError(f"Level must be 1..5, got {number}")
    return ALL_LEVELS[number - 1]


def level_name_from_score(weighted_score: float) -> str:
    """Map a continuous weighted score in [1.0, 5.0] to a maturity level name."""
    if weighted_score < 1.0 or weighted_score > 5.0:
        raise ValueError(f"Weighted score must be in [1.0, 5.0], got {weighted_score}")
    # Standard rounding: 1.00 to 1.49 → Level 1, 1.50 to 2.49 → Level 2, etc.
    # Level 5 caps at 5.0.
    level_number = min(5, int(weighted_score + 0.5))
    return get_level(level_number).name
