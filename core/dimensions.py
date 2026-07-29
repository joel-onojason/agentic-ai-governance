"""
core.dimensions
================
The six governance dimensions of the Agentic AI Governance Management System.

Each dimension is anchored on a Nigerian regulatory instrument and an
international standard, per Table 3.1 of the thesis. Dimensions are held as
frozen dataclasses so that the six-dimension core is immutable at runtime.

Reference: Table 3.1 in Chapter Three of the project thesis.
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Dimension:
    """A single governance dimension of the maturity model."""
    id: str                  # D1 through D6
    name: str                # short human-readable name
    long_name: str           # full descriptive name used in the UI
    nigerian_anchor: str     # named Nigerian regulatory instrument
    international_anchor: str  # named international standard or framework
    rationale: str           # why this dimension exists in the model


D1 = Dimension(
    id="D1",
    name="Autonomy",
    long_name="Autonomy and tool-use governance",
    nigerian_anchor="NDPA 2023, s. 37 (automated decision making); GAID 2025, Art. 8",
    international_anchor="IMDA Agentic MGF 2026 (action-space and autonomy); EU AI Act, Art. 14",
    rationale=(
        "Agentic systems act through tools. The scope of that action-space, and "
        "the degree of autonomy inside it, is the primary governance surface. "
        "This dimension asks whether an institution has bounded what its agents "
        "can do, logged what they did, and reviewed the tools they were given."
    ),
)

D2 = Dimension(
    id="D2",
    name="Identity",
    long_name="Agent identity and authentication",
    nigerian_anchor="CBN Risk-Based Cybersecurity Framework 2024",
    international_anchor="ISO/IEC 42001:2023, A.6; LOKA Protocol agent identity layer",
    rationale=(
        "An agent that acts on behalf of an institution must have a distinct, "
        "verifiable identity. Weak identity turns every downstream control into "
        "a guess about who or what actually took an action."
    ),
)

D3 = Dimension(
    id="D3",
    name="Delegation",
    long_name="Multi-agent and delegation oversight",
    nigerian_anchor="NITDA Code of Practice for Interactive Computer Service Platforms 2022",
    international_anchor="IMDA Agentic MGF 2026 (multi-agent setups); NIST AI RMF MAP",
    rationale=(
        "One agent handing work to another is the fastest way a governed action "
        "becomes an ungoverned one. This dimension asks whether delegation is "
        "documented, logged, monitored, and reviewed."
    ),
)

D4 = Dimension(
    id="D4",
    name="Human oversight",
    long_name="Human-in-the-loop and kill-switch design",
    nigerian_anchor="GAID 2025 grievance and intervention Schedules",
    international_anchor="IMDA human involvement levels; EU AI Act, Art. 14",
    rationale=(
        "Agents fail. Governance without a working human override and a tested "
        "kill-switch is governance on paper only. This dimension asks whether "
        "the override exists, is documented, and has been drilled."
    ),
)

D5 = Dimension(
    id="D5",
    name="Data & privacy",
    long_name="Data and privacy under NDPA and GAID",
    nigerian_anchor="NDPA 2023, Parts VI to IX; GAID 2025, Schedules 1 to 10",
    international_anchor="ISO/IEC 42001:2023, A.7; NIST AI 600-1 (data privacy)",
    rationale=(
        "Personal data flows through every agentic operation. This dimension "
        "asks whether DPIAs are done, lawful basis is documented, cross-border "
        "transfers are governed, and data subject rights are operationalised."
    ),
)

D6 = Dimension(
    id="D6",
    name="Accountability",
    long_name="Accountability and audit logging",
    nigerian_anchor="NDPA 2023, s. 44 (registration); FCCPA 2018",
    international_anchor="NIST AI RMF GOVERN; ISO/IEC 42001:2023, A.9; COBIT 2019",
    rationale=(
        "Accountability is the dimension the other five are measured against. "
        "This dimension asks whether an owner is named, whether audit logs "
        "exist and attribute actions to identities, and whether the response "
        "to an incident is documented and tested."
    ),
)


ALL_DIMENSIONS: Tuple[Dimension, ...] = (D1, D2, D3, D4, D5, D6)


def get_dimension(dimension_id: str) -> Dimension:
    """Return the Dimension with the given id (D1 through D6)."""
    for d in ALL_DIMENSIONS:
        if d.id == dimension_id:
            return d
    raise KeyError(f"Unknown dimension id: {dimension_id}")
