"""
core.crosswalk
===============
The regulatory cross-walk from each dimension to the named provisions of the
Nigerian and international instruments the dimension operationalises.

Reference: Section 3.4 of the project thesis. This module is what the
"View Regulatory Cross-Walk" sub-use-case in Figure 3.2 renders.
"""

from typing import Dict, List


CROSSWALK: Dict[str, Dict[str, List[str]]] = {

    "D1": {
        "nigerian": [
            "NDPA 2023, s. 37 (automated decision making)",
            "GAID 2025, Art. 8 (processing tiers and duties)",
        ],
        "international": [
            "IMDA Agentic AI MGF 2026 (action-space and autonomy)",
            "EU AI Act, Art. 14 (human oversight of high-risk systems)",
            "OpenAI baseline practices (Shavit et al., 2023): action-space constraint",
        ],
    },

    "D2": {
        "nigerian": [
            "CBN Risk-Based Cybersecurity Framework 2024 (identity and access management)",
        ],
        "international": [
            "ISO/IEC 42001:2023, Annex A.6 (roles and responsibilities)",
            "LOKA Protocol (Ranjan et al., 2025): universal agent identity layer",
        ],
    },

    "D3": {
        "nigerian": [
            "NITDA Code of Practice for Interactive Computer Service Platforms 2022",
        ],
        "international": [
            "IMDA Agentic AI MGF 2026 (multi-agent setups)",
            "NIST AI RMF 1.0: MAP function",
        ],
    },

    "D4": {
        "nigerian": [
            "GAID 2025, Schedules on grievance and intervention procedures",
        ],
        "international": [
            "IMDA Agentic AI MGF 2026 (levels of human involvement)",
            "EU AI Act, Art. 14 (human oversight)",
            "OpenAI baseline practices (Shavit et al., 2023): interruptibility",
        ],
    },

    "D5": {
        "nigerian": [
            "NDPA 2023, Parts VI to IX (data protection principles, rights, transfers)",
            "GAID 2025, Schedules 1 to 10 (DPIA, transfer, DCPMI, audit)",
            "NDPA 2023, s. 44 (DCPMI registration)",
        ],
        "international": [
            "ISO/IEC 42001:2023, Annex A.7 (data for AI systems)",
            "NIST AI 600-1 (Generative AI Profile): data privacy risks",
        ],
    },

    "D6": {
        "nigerian": [
            "NDPA 2023, s. 44 (registration and record-keeping)",
            "FCCPA 2018 (accountability of commercial data controllers)",
        ],
        "international": [
            "NIST AI RMF 1.0: GOVERN function",
            "ISO/IEC 42001:2023, Annex A.9 (performance evaluation)",
            "COBIT 2019 (governance and management objectives)",
        ],
    },
}


def get_crosswalk(dimension_id: str) -> Dict[str, List[str]]:
    """Return the {'nigerian': [...], 'international': [...]} cross-walk."""
    if dimension_id not in CROSSWALK:
        raise KeyError(f"No cross-walk for dimension {dimension_id}")
    return CROSSWALK[dimension_id]
