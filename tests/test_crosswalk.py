"""Unit tests for core.crosswalk.

The cross-walk is what gives every score a named regulatory anchor (the core
promise of the tool). These tests guarantee it covers exactly the six
dimensions, that every dimension maps to at least one Nigerian and one
international provision, and that the lookup helper behaves.
"""

import pytest

from core.crosswalk import CROSSWALK, get_crosswalk
from core.dimensions import ALL_DIMENSIONS


def test_crosswalk_covers_exactly_the_six_dimensions() -> None:
    assert set(CROSSWALK.keys()) == {d.id for d in ALL_DIMENSIONS}


def test_every_dimension_has_both_tracks_populated() -> None:
    for dim_id, tracks in CROSSWALK.items():
        assert set(tracks.keys()) == {"nigerian", "international"}, dim_id
        assert len(tracks["nigerian"]) >= 1, f"{dim_id} has no Nigerian anchor"
        assert len(tracks["international"]) >= 1, f"{dim_id} has no international anchor"


def test_no_anchor_string_is_empty() -> None:
    for dim_id, tracks in CROSSWALK.items():
        for track in ("nigerian", "international"):
            for anchor in tracks[track]:
                assert anchor.strip(), f"empty anchor in {dim_id}/{track}"


def test_get_crosswalk_returns_the_named_entry() -> None:
    xw = get_crosswalk("D5")
    assert xw is CROSSWALK["D5"]
    assert "nigerian" in xw and "international" in xw


def test_get_crosswalk_unknown_raises_keyerror() -> None:
    with pytest.raises(KeyError):
        get_crosswalk("D9")
