"""
core.scoring
=============
The weighted maturity score engine.

Given a variant and a set of six per-dimension scores (each an integer in
[1, 5]), the engine computes the weighted total and the per-dimension
contribution to that total. The arithmetic is deliberately readable: this
module is the core of the accountability the whole system asks its users to
apply to their agents (NFR3: the scoring logic is transparent and
inspectable).

Reference: Section 3.4 of the project thesis.
"""

from dataclasses import dataclass
from typing import Dict, Tuple

from core.variants import Variant, get_variant
from core.levels import level_name_from_score


@dataclass(frozen=True)
class ScoringResult:
    """The output of a single scoring run."""
    variant_id: str
    scores: Dict[str, int]          # dimension id → level 1..5
    weights: Dict[str, float]       # dimension id → weight
    contributions: Dict[str, float]  # dimension id → score × weight
    weighted_total: float           # in [1.0, 5.0]
    maturity_level_name: str        # e.g. "Defined"


def _validate_scores(scores: Dict[str, int]) -> None:
    """Raise ValueError if scores are outside the [1, 5] integer domain or miss a dimension."""
    expected = {"D1", "D2", "D3", "D4", "D5", "D6"}
    if set(scores.keys()) != expected:
        missing = expected - set(scores.keys())
        extra = set(scores.keys()) - expected
        raise ValueError(
            f"Scores must cover exactly D1..D6. Missing: {missing}, Extra: {extra}"
        )
    for dim_id, score in scores.items():
        if not isinstance(score, int):
            raise ValueError(f"Score for {dim_id} must be int, got {type(score).__name__}")
        if score < 1 or score > 5:
            raise ValueError(f"Score for {dim_id} must be 1..5, got {score}")


def calculate(variant: Variant, scores: Dict[str, int]) -> ScoringResult:
    """
    Compute the weighted maturity score for one institution under one variant.

    The arithmetic is: weighted_total = sum(score[d] * weight[d]) for d in D1..D6.
    Because the weights sum to 1.00 and each score is in [1, 5], the weighted
    total is guaranteed to fall in [1.0, 5.0].
    """
    variant.validate()
    _validate_scores(scores)

    contributions: Dict[str, float] = {}
    weighted_total = 0.0
    for dim_id in ("D1", "D2", "D3", "D4", "D5", "D6"):
        contrib = scores[dim_id] * variant.weights[dim_id]
        contributions[dim_id] = contrib
        weighted_total += contrib

    # Round to two decimal places to keep display sane.
    weighted_total = round(weighted_total, 2)

    return ScoringResult(
        variant_id=variant.id,
        scores=dict(scores),
        weights=dict(variant.weights),
        contributions=contributions,
        weighted_total=weighted_total,
        maturity_level_name=level_name_from_score(weighted_total),
    )


def calculate_by_variant_id(variant_id: str, scores: Dict[str, int]) -> ScoringResult:
    """Convenience wrapper: look up the variant by id and score."""
    return calculate(get_variant(variant_id), scores)
