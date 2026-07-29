"""
ui.components
==============
Reusable Streamlit components for the presentation layer.

Each function renders one piece of the interface and returns the value the
user selected. Streamlit re-runs the whole script on every input change, so
these components are written as pure widgets: no session-state manipulation
inside them. Session state is handled in app.py.

Reference: Section 4.2.6 of the project thesis.
"""

from typing import Dict, Tuple

import streamlit as st

from core.dimensions import ALL_DIMENSIONS, get_dimension
from core.descriptors import get_dimension_ladder
from core.variants import ALL_VARIANTS, PUBLIC_SECTOR
from core.crosswalk import get_crosswalk


def render_variant_selector() -> str:
    """
    Render the variant selector in the sidebar. Returns the selected variant id.

    Two variants: Public Sector (default) and Large Enterprise. The default is
    Public Sector because the project's Chapter 1 significance statement is
    ordered public sector first.
    """
    st.sidebar.header("Variant")
    variant_names = {v.id: v.name for v in ALL_VARIANTS}
    default_index = list(variant_names.keys()).index(PUBLIC_SECTOR.id)
    selected = st.sidebar.radio(
        "Select the institution type being assessed:",
        options=list(variant_names.keys()),
        format_func=lambda vid: variant_names[vid],
        index=default_index,
        key="variant_id",
    )

    # Show the variant description so the user knows why the weights differ.
    from core.variants import get_variant  # local import avoids cyclic risk
    v = get_variant(selected)
    st.sidebar.caption(v.description)

    return selected


def render_dimension_scorer(dimension_id: str, default_level: int = 1) -> int:
    """
    Render one dimension's scoring block: heading, the five ladder rungs, and
    a slider that lets the user pick the level. Returns the chosen level.
    """
    dim = get_dimension(dimension_id)
    st.subheader(f"{dim.id}. {dim.long_name}")
    st.caption(f"**Nigerian anchor:** {dim.nigerian_anchor}")
    st.caption(f"**International anchor:** {dim.international_anchor}")

    ladder = get_dimension_ladder(dimension_id)
    with st.expander("View the five-level ladder for this dimension"):
        for level_number in range(1, 6):
            st.markdown(f"**Level {level_number}.** {ladder[level_number]}")

    level = st.slider(
        "Score this dimension on the 1 to 5 scale:",
        min_value=1,
        max_value=5,
        value=default_level,
        step=1,
        key=f"score_{dimension_id}",
    )
    return int(level)


def render_all_dimension_scorers(defaults: Dict[str, int] = None) -> Dict[str, int]:
    """Render every dimension's scorer and return the full score dict."""
    if defaults is None:
        defaults = {d.id: 1 for d in ALL_DIMENSIONS}
    scores: Dict[str, int] = {}
    for dim in ALL_DIMENSIONS:
        scores[dim.id] = render_dimension_scorer(dim.id, defaults.get(dim.id, 1))
        st.divider()
    return scores


def render_crosswalk_view() -> None:
    """Render the regulatory cross-walk expander for all six dimensions."""
    with st.expander("View the full regulatory cross-walk"):
        for dim in ALL_DIMENSIONS:
            st.markdown(f"### {dim.id}. {dim.long_name}")
            xw = get_crosswalk(dim.id)
            st.markdown("**Nigerian anchors:**")
            for anchor in xw["nigerian"]:
                st.markdown(f"- {anchor}")
            st.markdown("**International anchors:**")
            for anchor in xw["international"]:
                st.markdown(f"- {anchor}")
            st.markdown("---")
