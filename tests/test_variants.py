"""Unit tests for core.variants.

The single most important invariant: every variant's weights must sum to 1.00
and cover exactly D1..D6. If a future variant is added and violates this, the
build fails.
"""

import pytest

from core.variants import ALL_VARIANTS, PUBLIC_SECTOR, LARGE_ENTERPRISE, get_variant


def test_all_variants_have_weights_summing_to_one() -> None:
    for variant in ALL_VARIANTS:
        total = sum(variant.weights.values())
        assert abs(total - 1.0) < 1e-6, (
            f"Variant {variant.id} weights sum to {total}, expected 1.00"
        )


def test_all_variants_cover_exactly_d1_to_d6() -> None:
    expected = {"D1", "D2", "D3", "D4", "D5", "D6"}
    for variant in ALL_VARIANTS:
        assert set(variant.weights.keys()) == expected, (
            f"Variant {variant.id} does not cover exactly {expected}"
        )


def test_public_sector_weights_match_thesis_table_3_3() -> None:
    """Table 3.3 of the thesis specifies these weights exactly."""
    assert PUBLIC_SECTOR.weights == {
        "D1": 0.15,
        "D2": 0.15,
        "D3": 0.15,
        "D4": 0.20,
        "D5": 0.20,
        "D6": 0.15,
    }


def test_large_enterprise_weights_match_thesis_table_3_3() -> None:
    """Table 3.3 of the thesis specifies these weights exactly."""
    assert LARGE_ENTERPRISE.weights == {
        "D1": 0.20,
        "D2": 0.20,
        "D3": 0.15,
        "D4": 0.15,
        "D5": 0.15,
        "D6": 0.15,
    }


def test_get_variant_returns_the_named_variant() -> None:
    assert get_variant("public_sector").id == "public_sector"
    assert get_variant("large_enterprise").id == "large_enterprise"


def test_get_variant_unknown_raises() -> None:
    with pytest.raises(KeyError):
        get_variant("does_not_exist")


def test_variant_validate_catches_broken_weights() -> None:
    """If a future variant is edited to break the sum-to-1 invariant, the
    scoring engine catches it."""
    from core.variants import Variant
    broken = Variant(
        id="broken",
        name="Broken",
        description="Weights sum to 0.99",
        weights={"D1": 0.15, "D2": 0.15, "D3": 0.15, "D4": 0.19, "D5": 0.20, "D6": 0.15},
    )
    with pytest.raises(ValueError):
        broken.validate()


def test_variant_validate_catches_wrong_dimension_keys() -> None:
    """Weights that sum to 1.00 but cover the wrong dimensions are still
    invalid and must be rejected on the key-coverage branch."""
    from core.variants import Variant
    wrong_keys = Variant(
        id="wrong_keys",
        name="Wrong keys",
        description="Sums to 1.00 but includes D7 and drops D6",
        weights={"D1": 0.15, "D2": 0.15, "D3": 0.15, "D4": 0.20, "D5": 0.20, "D7": 0.15},
    )
    with pytest.raises(ValueError):
        wrong_keys.validate()


def test_valid_variants_pass_validate() -> None:
    for variant in ALL_VARIANTS:
        variant.validate()  # must not raise


def test_variant_is_immutable() -> None:
    import dataclasses
    with pytest.raises(dataclasses.FrozenInstanceError):
        PUBLIC_SECTOR.name = "mutated"  # type: ignore[misc]
