"""Unit tests for core.levels.

Covers the five-level data, get_level bounds, and the continuous-score to
level-name mapping including its rounding boundaries (1.49 vs 1.50, the Level 5
cap at 5.0, and out-of-range rejection).
"""

import dataclasses

import pytest

from core.levels import (
    ALL_LEVELS,
    MaturityLevel,
    get_level,
    level_name_from_score,
)


# ---------------------------------------------------------------- data

def test_five_levels_numbered_one_to_five() -> None:
    assert [lv.number for lv in ALL_LEVELS] == [1, 2, 3, 4, 5]


def test_level_names_match_cmmi_scale() -> None:
    assert [lv.name for lv in ALL_LEVELS] == [
        "Ad hoc",
        "Initial",
        "Defined",
        "Managed",
        "Optimising",
    ]


def test_every_level_has_a_general_descriptor() -> None:
    for lv in ALL_LEVELS:
        assert len(lv.general_descriptor) > 40, f"level {lv.number} descriptor short"


def test_level_is_immutable() -> None:
    with pytest.raises(dataclasses.FrozenInstanceError):
        ALL_LEVELS[0].name = "mutated"  # type: ignore[misc]


# ---------------------------------------------------------------- get_level

@pytest.mark.parametrize("number,name", [
    (1, "Ad hoc"),
    (2, "Initial"),
    (3, "Defined"),
    (4, "Managed"),
    (5, "Optimising"),
])
def test_get_level_returns_expected(number: int, name: str) -> None:
    lv = get_level(number)
    assert lv.number == number
    assert lv.name == name


@pytest.mark.parametrize("bad", [0, 6, -1, 100])
def test_get_level_out_of_range_raises(bad: int) -> None:
    with pytest.raises(ValueError):
        get_level(bad)


# ---------------------------------------------------------------- score → name

@pytest.mark.parametrize("score,expected", [
    (1.00, "Ad hoc"),
    (1.49, "Ad hoc"),      # rounds down
    (1.50, "Initial"),     # rounds up
    (2.49, "Initial"),
    (2.50, "Defined"),
    (3.00, "Defined"),
    (3.49, "Defined"),
    (3.50, "Managed"),
    (4.49, "Managed"),
    (4.50, "Optimising"),
    (5.00, "Optimising"),  # capped at level 5
])
def test_level_name_from_score_boundaries(score: float, expected: str) -> None:
    assert level_name_from_score(score) == expected


@pytest.mark.parametrize("bad", [0.99, 5.01, -1.0, 10.0])
def test_level_name_from_score_out_of_range_raises(bad: float) -> None:
    with pytest.raises(ValueError):
        level_name_from_score(bad)
