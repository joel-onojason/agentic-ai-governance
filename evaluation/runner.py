"""
evaluation.runner
==================
Runs each retrospective case through the same scoring engine the live user
touches, which is what makes the Chapter Five evaluation reproducible from
the system itself rather than asserted alongside it.

Reference: Section 4.2.8 of the project thesis.
"""

from typing import List

import pandas as pd

from core.scoring import calculate_by_variant_id
from core.variants import ALL_VARIANTS
from evaluation.cases import RetrospectiveCase, STUB_CASES, ALL_CASES


def run_case(case: RetrospectiveCase, variant_id: str) -> dict:
    """Score one case under one variant and return a flat result row."""
    result = calculate_by_variant_id(variant_id, case.scores)
    return {
        "case_id": case.id,
        "case_name": case.name,
        "jurisdiction": case.jurisdiction,
        "date_range": case.date_range,
        "variant_id": result.variant_id,
        "weighted_score": result.weighted_total,
        "maturity_level": result.maturity_level_name,
        "D1": case.scores["D1"],
        "D2": case.scores["D2"],
        "D3": case.scores["D3"],
        "D4": case.scores["D4"],
        "D5": case.scores["D5"],
        "D6": case.scores["D6"],
    }


def run_all(cases: List[RetrospectiveCase] = None) -> pd.DataFrame:
    """
    Score every case against every variant. Returns a DataFrame with one row
    per (case, variant) pair, ordered by weighted_score ascending so weak
    cases surface at the top.
    """
    if cases is None:
        cases = list(ALL_CASES)
    rows = []
    for case in cases:
        for variant in ALL_VARIANTS:
            rows.append(run_case(case, variant.id))
    df = pd.DataFrame(rows)
    return df.sort_values(["variant_id", "weighted_score"]).reset_index(drop=True)


def stub_summary() -> str:
    """
    Human-readable one-liner summarising the extended fifteen-case sample.
    Used in the Streamlit evaluation tab. Kept under the name stub_summary
    for backward compatibility with the Chapter Four wiring; the actual
    output now describes the full fifteen-case extended sample.
    """
    return (
        "Fifteen retrospective cases loaded: the three initial stubs "
        "(Meta/WhatsApp, Apple Card, Ghana Mahama) carried forward from "
        "the Chapter Four delivery, plus twelve extensions added for "
        "Chapter Five (ten additional entity cases and two "
        "regulator-maturity benchmarks: FCCPC/DEON and NDPC 1,368-firm "
        "compliance notice). Full per-dimension evidence tables sit in "
        "docs/CASE_CODING_APPENDIX.md."
    )
