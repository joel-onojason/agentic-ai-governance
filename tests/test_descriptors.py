"""Unit tests for core.descriptors.

Verifies that every one of the 30 (dimension, level) cells has a non-empty
descriptor.
"""

import pytest

from core.descriptors import DESCRIPTORS, get_descriptor, get_dimension_ladder


def test_all_thirty_cells_present() -> None:
    for dimension_id in ("D1", "D2", "D3", "D4", "D5", "D6"):
        for level in range(1, 6):
            key = (dimension_id, level)
            assert key in DESCRIPTORS, f"Missing descriptor for {key}"


def test_no_descriptor_is_empty() -> None:
    for key, text in DESCRIPTORS.items():
        assert text.strip(), f"Empty descriptor at {key}"
        assert len(text) > 20, f"Descriptor at {key} suspiciously short"


def test_get_descriptor_returns_expected_text() -> None:
    d1_level_1 = get_descriptor("D1", 1)
    assert "No scope constraints" in d1_level_1


def test_get_dimension_ladder_returns_five_levels() -> None:
    ladder = get_dimension_ladder("D4")
    assert set(ladder.keys()) == {1, 2, 3, 4, 5}
    for level, text in ladder.items():
        assert len(text) > 20


def test_exactly_thirty_descriptor_cells() -> None:
    assert len(DESCRIPTORS) == 30


def test_get_descriptor_unknown_cell_raises_keyerror() -> None:
    with pytest.raises(KeyError):
        get_descriptor("D1", 6)      # level out of range
    with pytest.raises(KeyError):
        get_descriptor("D9", 1)      # dimension out of range


def test_ladder_matches_get_descriptor_for_every_dimension() -> None:
    for dim_id in ("D1", "D2", "D3", "D4", "D5", "D6"):
        ladder = get_dimension_ladder(dim_id)
        for level in range(1, 6):
            assert ladder[level] == get_descriptor(dim_id, level)
