"""Unit tests for ui.heatmap.

build_heatmap turns the six scores into a 2x3 Plotly heat-map. These tests
assert the returned Figure's structure without needing a browser: the z-matrix
layout, the fixed 1..5 colour range, one annotation per cell, and correct
propagation of scores and title.
"""

import plotly.graph_objects as go
import pytest

from ui.heatmap import build_heatmap, _LAYOUT


def _all(level: int) -> dict:
    return {d: level for d in ("D1", "D2", "D3", "D4", "D5", "D6")}


def _z_as_lists(fig: go.Figure) -> list:
    """Plotly may store z as lists or tuples; normalise to nested lists."""
    return [list(row) for row in fig.data[0].z]


def test_returns_a_plotly_figure() -> None:
    fig = build_heatmap(_all(3))
    assert isinstance(fig, go.Figure)


def test_single_heatmap_trace() -> None:
    fig = build_heatmap(_all(3))
    assert len(fig.data) == 1
    assert isinstance(fig.data[0], go.Heatmap)


def test_z_matrix_is_2x3_and_follows_layout() -> None:
    scores = {"D1": 1, "D2": 2, "D3": 3, "D4": 4, "D5": 5, "D6": 1}
    fig = build_heatmap(scores)
    z = _z_as_lists(fig)
    assert z == [[1, 2, 3], [4, 5, 1]]
    # z rows/cols correspond exactly to _LAYOUT positions
    for r, row in enumerate(_LAYOUT):
        for c, dim_id in enumerate(row):
            assert z[r][c] == scores[dim_id]


def test_colour_range_is_locked_one_to_five() -> None:
    fig = build_heatmap(_all(3))
    assert fig.data[0].zmin == 1
    assert fig.data[0].zmax == 5


def test_one_annotation_per_cell() -> None:
    fig = build_heatmap(_all(3))
    assert len(fig.layout.annotations) == 6


def test_annotation_text_carries_dimension_and_level() -> None:
    fig = build_heatmap(_all(4))
    texts = [a.text for a in fig.layout.annotations]
    assert any("D1" in t and "Level 4" in t for t in texts)


def test_title_is_propagated() -> None:
    fig = build_heatmap(_all(2), title="Custom title")
    assert fig.layout.title.text == "Custom title"


def test_extreme_scores_render() -> None:
    for level in (1, 5):
        fig = build_heatmap(_all(level))
        assert _z_as_lists(fig) == [[level, level, level], [level, level, level]]


def test_missing_dimension_raises_keyerror() -> None:
    incomplete = {"D1": 1, "D2": 1, "D3": 1, "D4": 1, "D5": 1}  # D6 missing
    with pytest.raises(KeyError):
        build_heatmap(incomplete)
