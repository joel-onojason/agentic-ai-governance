"""Unit tests for the evaluation.runner and evaluation.cases modules."""

import pytest

from evaluation.cases import STUB_CASES, META_WHATSAPP, APPLE_CARD, GHANA_MAHAMA, get_case
from evaluation.runner import run_case, run_all, stub_summary


def test_three_stub_cases_present() -> None:
    assert len(STUB_CASES) == 3
    ids = {c.id for c in STUB_CASES}
    assert ids == {
        "meta_whatsapp_ng_2024",
        "apple_card_us_2019",
        "ghana_mahama_deepfake_2026",
    }


def test_every_case_has_six_dimension_scores_and_rationales() -> None:
    expected_dims = {"D1", "D2", "D3", "D4", "D5", "D6"}
    for case in STUB_CASES:
        assert set(case.scores.keys()) == expected_dims
        assert set(case.rationale.keys()) == expected_dims
        for dim, score in case.scores.items():
            assert 1 <= score <= 5, f"{case.id} {dim} score {score} out of range"


def test_every_case_has_at_least_one_primary_source() -> None:
    for case in STUB_CASES:
        assert len(case.primary_sources) >= 1, f"{case.id} has no primary sources"


def test_meta_whatsapp_matches_appendix_coding() -> None:
    """Empirical coding from docs/CASE_CODING_APPENDIX.md, Case 1."""
    assert META_WHATSAPP.scores == {
        "D1": 2, "D2": 2, "D3": 2, "D4": 2, "D5": 3, "D6": 2
    }


def test_apple_card_matches_appendix_coding() -> None:
    """Empirical coding from docs/CASE_CODING_APPENDIX.md, Case 2."""
    assert APPLE_CARD.scores == {
        "D1": 3, "D2": 3, "D3": 3, "D4": 2, "D5": 4, "D6": 3
    }


def test_ghana_mahama_matches_appendix_coding() -> None:
    """Empirical coding from docs/CASE_CODING_APPENDIX.md, Case 3."""
    assert GHANA_MAHAMA.scores == {
        "D1": 1, "D2": 1, "D3": 1, "D4": 1, "D5": 1, "D6": 2
    }


def test_apple_card_scores_higher_than_meta_under_both_variants() -> None:
    """Sanity check on the three-case signature separation: Apple Card has a
    higher overall governance profile than Meta/WhatsApp on this rubric,
    reflecting Goldman's fair-lending program maturity."""
    for variant_id in ("public_sector", "large_enterprise"):
        r_apple = run_case(APPLE_CARD, variant_id)
        r_meta = run_case(META_WHATSAPP, variant_id)
        assert r_apple["weighted_score"] > r_meta["weighted_score"]


def test_ghana_mahama_scores_lowest_under_both_variants() -> None:
    """Ghana Mahama should sit at the floor since five of six dimensions are Level 1."""
    for variant_id in ("public_sector", "large_enterprise"):
        r_gh = run_case(GHANA_MAHAMA, variant_id)
        r_meta = run_case(META_WHATSAPP, variant_id)
        r_apple = run_case(APPLE_CARD, variant_id)
        assert r_gh["weighted_score"] < r_meta["weighted_score"]
        assert r_gh["weighted_score"] < r_apple["weighted_score"]


def test_run_all_returns_six_rows() -> None:
    """Three cases x two variants = six rows."""
    df = run_all()
    assert len(df) == 6


def test_get_case_returns_the_named_case() -> None:
    assert get_case("apple_card_us_2019").id == "apple_card_us_2019"


def test_get_case_unknown_raises() -> None:
    with pytest.raises(KeyError):
        get_case("nonexistent_case")


def test_run_case_row_has_expected_schema() -> None:
    row = run_case(APPLE_CARD, "public_sector")
    expected_keys = {
        "case_id", "case_name", "jurisdiction", "date_range", "variant_id",
        "weighted_score", "maturity_level",
        "D1", "D2", "D3", "D4", "D5", "D6",
    }
    assert set(row.keys()) == expected_keys
    assert row["variant_id"] == "public_sector"
    assert 1.0 <= row["weighted_score"] <= 5.0


def test_run_all_dataframe_columns_and_dtypes() -> None:
    df = run_all()
    for col in ("case_id", "variant_id", "weighted_score", "maturity_level", "D1", "D6"):
        assert col in df.columns
    # every case appears under both variants
    assert set(df["variant_id"]) == {"public_sector", "large_enterprise"}
    assert len(df["case_id"].unique()) == 3


def test_run_all_is_sorted_by_variant_then_score() -> None:
    df = run_all()
    for variant_id in ("public_sector", "large_enterprise"):
        sub = df[df["variant_id"] == variant_id]["weighted_score"].tolist()
        assert sub == sorted(sub), f"{variant_id} not ascending by score"


def test_run_all_accepts_a_custom_case_subset() -> None:
    df = run_all([GHANA_MAHAMA])
    assert len(df) == 2                      # one case x two variants
    assert set(df["case_id"]) == {"ghana_mahama_deepfake_2026"}


def test_stub_summary_names_all_three_cases() -> None:
    summary = stub_summary()
    assert "Meta" in summary
    assert "Apple Card" in summary
    assert "Ghana Mahama" in summary


def test_every_case_has_a_failure_signature() -> None:
    for case in STUB_CASES:
        assert len(case.failure_signature) > 40, case.id


def test_case_is_immutable() -> None:
    import dataclasses
    with pytest.raises(dataclasses.FrozenInstanceError):
        META_WHATSAPP.name = "mutated"  # type: ignore[misc]
