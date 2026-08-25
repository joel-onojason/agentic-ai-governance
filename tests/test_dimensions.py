"""Unit tests for core.dimensions.

The six-dimension core is the immutable spine of the whole model. These tests
lock down its shape (exactly D1..D6), the completeness of every dimension's
descriptive and regulatory-anchor fields, the lookup helper, and the frozen
immutability guarantee promised in the module docstring.
"""

import dataclasses

import pytest

from core.dimensions import ALL_DIMENSIONS, get_dimension


def test_exactly_six_dimensions() -> None:
    assert len(ALL_DIMENSIONS) == 6


def test_dimension_ids_are_d1_to_d6_in_order() -> None:
    assert [d.id for d in ALL_DIMENSIONS] == ["D1", "D2", "D3", "D4", "D5", "D6"]


def test_dimension_ids_are_unique() -> None:
    ids = [d.id for d in ALL_DIMENSIONS]
    assert len(set(ids)) == len(ids)


def test_every_dimension_field_is_populated() -> None:
    """Each dimension must carry a non-empty name, long_name, both regulatory
    anchors, and a rationale, since all six feed directly into the About tab
    and the scorer captions."""
    for d in ALL_DIMENSIONS:
        assert d.name.strip(), f"{d.id} has empty name"
        assert d.long_name.strip(), f"{d.id} has empty long_name"
        assert d.nigerian_anchor.strip(), f"{d.id} has empty nigerian_anchor"
        assert d.international_anchor.strip(), f"{d.id} has empty international_anchor"
        assert len(d.rationale) > 40, f"{d.id} rationale suspiciously short"


def test_get_dimension_returns_the_named_dimension() -> None:
    for dim_id in ("D1", "D2", "D3", "D4", "D5", "D6"):
        assert get_dimension(dim_id).id == dim_id


def test_get_dimension_unknown_raises_keyerror() -> None:
    with pytest.raises(KeyError):
        get_dimension("D7")


def test_dimension_is_immutable() -> None:
    d = ALL_DIMENSIONS[0]
    with pytest.raises(dataclasses.FrozenInstanceError):
        d.name = "mutated"  # type: ignore[misc]


def test_names_are_distinct() -> None:
    """Short names appear as axis labels on the heat-map; duplicates would make
    the visualisation ambiguous."""
    names = [d.name for d in ALL_DIMENSIONS]
    assert len(set(names)) == len(names)
