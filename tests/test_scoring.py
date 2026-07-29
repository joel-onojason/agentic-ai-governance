"""Unit tests for core.scoring."""

import pytest

from core.scoring import calculate_by_variant_id, calculate, ScoringResult
from core.variants import PUBLIC_SECTOR, LARGE_ENTERPRISE


def test_scoring_all_level_1_gives_score_of_1() -> None:
    scores = {"D1": 1, "D2": 1, "D3": 1, "D4": 1, "D5": 1, "D6": 1}
    result = calculate_by_variant_id("public_sector", scores)
    assert result.weighted_total == 1.00
    assert result.maturity_level_name == "Ad hoc"


def test_scoring_all_level_5_gives_score_of_5() -> None:
    scores = {"D1": 5, "D2": 5, "D3": 5, "D4": 5, "D5": 5, "D6": 5}
    result = calculate_by_variant_id("large_enterprise", scores)
    assert result.weighted_total == 5.00
    assert result.maturity_level_name == "Optimising"


def test_scoring_all_level_3_gives_score_of_3() -> None:
    scores = {"D1": 3, "D2": 3, "D3": 3, "D4": 3, "D5": 3, "D6": 3}
    # Under any variant, uniform level 3 gives exactly 3.00
    for variant_id in ("public_sector", "large_enterprise"):
        result = calculate_by_variant_id(variant_id, scores)
        assert result.weighted_total == 3.00
        assert result.maturity_level_name == "Defined"


def test_public_sector_prioritises_d4_and_d5() -> None:
    """A high D4/D5 score should lift the public-sector weighted total more
    than the same high score on D1/D2."""
    high_d45 = {"D1": 1, "D2": 1, "D3": 1, "D4": 5, "D5": 5, "D6": 1}
    high_d12 = {"D1": 5, "D2": 5, "D3": 1, "D4": 1, "D5": 1, "D6": 1}

    r_ps_d45 = calculate_by_variant_id("public_sector", high_d45)
    r_ps_d12 = calculate_by_variant_id("public_sector", high_d12)

    assert r_ps_d45.weighted_total > r_ps_d12.weighted_total


def test_large_enterprise_prioritises_d1_and_d2() -> None:
    """A high D1/D2 score should lift the large-enterprise weighted total
    more than the same high score on D4/D5."""
    high_d12 = {"D1": 5, "D2": 5, "D3": 1, "D4": 1, "D5": 1, "D6": 1}
    high_d45 = {"D1": 1, "D2": 1, "D3": 1, "D4": 5, "D5": 5, "D6": 1}

    r_le_d12 = calculate_by_variant_id("large_enterprise", high_d12)
    r_le_d45 = calculate_by_variant_id("large_enterprise", high_d45)

    assert r_le_d12.weighted_total > r_le_d45.weighted_total


def test_score_below_1_rejected() -> None:
    scores = {"D1": 0, "D2": 1, "D3": 1, "D4": 1, "D5": 1, "D6": 1}
    with pytest.raises(ValueError):
        calculate_by_variant_id("public_sector", scores)


def test_score_above_5_rejected() -> None:
    scores = {"D1": 6, "D2": 1, "D3": 1, "D4": 1, "D5": 1, "D6": 1}
    with pytest.raises(ValueError):
        calculate_by_variant_id("public_sector", scores)


def test_missing_dimension_rejected() -> None:
    scores = {"D1": 1, "D2": 1, "D3": 1, "D4": 1, "D5": 1}  # D6 missing
    with pytest.raises(ValueError):
        calculate_by_variant_id("public_sector", scores)


def test_unknown_variant_rejected() -> None:
    scores = {"D1": 1, "D2": 1, "D3": 1, "D4": 1, "D5": 1, "D6": 1}
    with pytest.raises(KeyError):
        calculate_by_variant_id("nonexistent_variant", scores)


def test_contributions_sum_to_weighted_total() -> None:
    scores = {"D1": 2, "D2": 3, "D3": 4, "D4": 2, "D5": 5, "D6": 3}
    result = calculate_by_variant_id("public_sector", scores)
    assert abs(sum(result.contributions.values()) - result.weighted_total) < 1e-6


def test_result_is_immutable() -> None:
    scores = {"D1": 2, "D2": 3, "D3": 4, "D4": 2, "D5": 5, "D6": 3}
    result = calculate_by_variant_id("public_sector", scores)
    with pytest.raises(Exception):  # frozen dataclass rejects assignment
        result.weighted_total = 999


def test_non_integer_score_rejected() -> None:
    """A float (e.g. from a mis-wired widget) must be rejected, not silently
    coerced, since the rubric is defined only on integer levels."""
    scores = {"D1": 3.5, "D2": 1, "D3": 1, "D4": 1, "D5": 1, "D6": 1}
    with pytest.raises(ValueError):
        calculate_by_variant_id("public_sector", scores)


def test_extra_dimension_rejected() -> None:
    scores = {"D1": 1, "D2": 1, "D3": 1, "D4": 1, "D5": 1, "D6": 1, "D7": 1}
    with pytest.raises(ValueError):
        calculate_by_variant_id("public_sector", scores)


def test_calculate_accepts_a_variant_object_directly() -> None:
    scores = {"D1": 3, "D2": 3, "D3": 3, "D4": 3, "D5": 3, "D6": 3}
    result = calculate(PUBLIC_SECTOR, scores)
    assert result.variant_id == "public_sector"
    assert result.weighted_total == 3.00


def test_result_scores_are_a_defensive_copy() -> None:
    """Mutating the caller's dict afterwards must not change the stored result."""
    scores = {"D1": 2, "D2": 2, "D3": 2, "D4": 2, "D5": 2, "D6": 2}
    result = calculate_by_variant_id("public_sector", scores)
    scores["D1"] = 5
    assert result.scores["D1"] == 2


def test_weights_recorded_match_the_variant() -> None:
    scores = {"D1": 1, "D2": 1, "D3": 1, "D4": 1, "D5": 1, "D6": 1}
    result = calculate_by_variant_id("large_enterprise", scores)
    assert result.weights == LARGE_ENTERPRISE.weights
