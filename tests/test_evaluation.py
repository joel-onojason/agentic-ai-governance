"""Unit tests for the evaluation.runner and evaluation.cases modules."""

import pytest

from evaluation.cases import (
    STUB_CASES,
    EXTENSION_CASES,
    ALL_CASES,
    META_WHATSAPP,
    APPLE_CARD,
    GHANA_MAHAMA,
    get_case,
)
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
    for case in ALL_CASES:
        assert set(case.scores.keys()) == expected_dims
        assert set(case.rationale.keys()) == expected_dims
        for dim, score in case.scores.items():
            assert 1 <= score <= 5, f"{case.id} {dim} score {score} out of range"


def test_every_case_has_at_least_one_primary_source() -> None:
    for case in ALL_CASES:
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


def test_run_all_returns_thirty_rows() -> None:
    """Fifteen cases x two variants = thirty rows."""
    df = run_all()
    assert len(df) == 30


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
    assert len(df["case_id"].unique()) == 15


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
    for case in ALL_CASES:
        assert len(case.failure_signature) > 40, case.id


def test_case_is_immutable() -> None:
    import dataclasses
    with pytest.raises(dataclasses.FrozenInstanceError):
        META_WHATSAPP.name = "mutated"  # type: ignore[misc]


# =====================================================================
# Extended fifteen-case sample (Chapter Five)
# =====================================================================
# The loops above now run over ALL_CASES, so every invariant they assert
# (six dimensions, scores in range, rationales, a primary source, a
# failure signature) covers the twelve extensions as well as the three
# stubs. The tests below pin the structure of the extended sample itself.

# (case_id, Public Sector total, Large Enterprise total) exactly as
# published in docs/CASE_CODING_APPENDIX.md, Cross-case synthesis.
APPENDIX_TOTALS = [
    ("ghana_mahama_deepfake_2026", 1.15, 1.15),
    ("sokoloan_nitda_2021", 1.35, 1.35),
    ("nimc_nin_bvn", 1.40, 1.30),
    ("hk_uae_voice_clone_2020", 1.50, 1.50),
    ("jamb_utme_2025", 1.80, 1.85),
    ("arup_deepfake_2024", 1.85, 1.80),
    ("flutterwave_series", 2.00, 2.00),
    ("inec_irev_2023", 2.15, 2.15),
    ("meta_whatsapp_ng_2024", 2.20, 2.15),
    ("ndpc_fidelity_2024", 2.20, 2.15),
    ("ndpc_multichoice_2025", 2.20, 2.15),
    ("ndpc_seven_firm_2024", 2.35, 2.30),
    ("apple_card_us_2019", 3.00, 3.00),
    ("fccpc_deon_2025", 3.00, 2.95),
    ("ndpc_compliance_notice_2025", 3.35, 3.30),
]


def test_extended_sample_is_fifteen_cases() -> None:
    assert len(STUB_CASES) == 3
    assert len(EXTENSION_CASES) == 12
    assert len(ALL_CASES) == 15
    assert ALL_CASES == STUB_CASES + EXTENSION_CASES


def test_all_case_ids_are_unique() -> None:
    ids = [c.id for c in ALL_CASES]
    assert len(set(ids)) == len(ids), "duplicate case id in ALL_CASES"


def test_get_case_resolves_every_case() -> None:
    for case in ALL_CASES:
        assert get_case(case.id) is case


def test_every_case_has_a_known_jurisdiction() -> None:
    allowed = {
        "Nigerian precursor",
        "International agentic comparator",
        "Regulator-maturity benchmark",
    }
    for case in ALL_CASES:
        assert case.jurisdiction in allowed, f"{case.id}: {case.jurisdiction}"


def test_every_case_has_a_name_and_date_range() -> None:
    for case in ALL_CASES:
        assert case.name.strip(), case.id
        assert case.date_range.strip(), case.id


def test_every_case_has_a_rationale_sentence_per_dimension() -> None:
    for case in ALL_CASES:
        for dim, text in case.rationale.items():
            assert len(text) > 40, f"{case.id} {dim} rationale too thin"


def test_every_case_scores_in_range_under_both_variants() -> None:
    for case in ALL_CASES:
        for variant_id in ("public_sector", "large_enterprise"):
            row = run_case(case, variant_id)
            assert 1.0 <= row["weighted_score"] <= 5.0, f"{case.id} {variant_id}"
            assert row["maturity_level"], f"{case.id} {variant_id} has no level"


def test_weighted_totals_match_the_published_appendix() -> None:
    """Every total printed in the appendix must come back out of the engine.

    This is the test that keeps the thesis prose and the code honest: if a
    score or a weight changes, the published table is wrong and this fails.
    """
    assert len(APPENDIX_TOTALS) == len(ALL_CASES)
    for case_id, expected_ps, expected_le in APPENDIX_TOTALS:
        case = get_case(case_id)
        assert run_case(case, "public_sector")["weighted_score"] == expected_ps, case_id
        assert run_case(case, "large_enterprise")["weighted_score"] == expected_le, case_id


def test_no_dimension_in_any_case_reaches_level_five() -> None:
    """Coding rule 4 in docs/CASE_CODING_APPENDIX.md: Level 5 is aspirational
    within the sample, as no primary source evidenced adaptive governance."""
    for case in ALL_CASES:
        for dim, score in case.scores.items():
            assert score <= 4, f"{case.id} {dim} is Level 5, contradicting coding rule 4"


def test_regulator_benchmarks_outrank_the_primary_sample_ceiling() -> None:
    """The two benchmarks anchor the top of the scale, per the synthesis."""
    benchmarks = {"fccpc_deon_2025", "ndpc_compliance_notice_2025"}
    assert {c.id for c in ALL_CASES if c.jurisdiction == "Regulator-maturity benchmark"} == benchmarks
    primary = [c for c in ALL_CASES if c.id not in benchmarks]
    assert len(primary) == 13
    top_primary = max(run_case(c, "public_sector")["weighted_score"] for c in primary)
    for bid in benchmarks:
        assert run_case(get_case(bid), "public_sector")["weighted_score"] >= top_primary


def test_run_all_covers_every_case_under_every_variant() -> None:
    df = run_all()
    assert set(df["case_id"]) == {c.id for c in ALL_CASES}
    for case in ALL_CASES:
        assert set(df[df["case_id"] == case.id]["variant_id"]) == {
            "public_sector",
            "large_enterprise",
        }


def test_stub_summary_describes_the_fifteen_case_sample() -> None:
    summary = stub_summary()
    assert "Fifteen" in summary
    assert "CASE_CODING_APPENDIX.md" in summary
