"""
Agentic AI Governance Management System
========================================
Main Streamlit entry point.

Run locally:
    streamlit run app.py

The application has three tabs:
  1. Assess: the interactive scoring interface (FR1 through FR6)
  2. Retrospective Cases: runs the three stub cases (FR7)
  3. About: model overview, cross-walk, version, source repo link

Reference: Section 4.2.6 of the project thesis.
"""

import streamlit as st

from core.dimensions import ALL_DIMENSIONS
from core.scoring import calculate_by_variant_id
from core.variants import get_variant
from ui.components import (
    render_variant_selector,
    render_all_dimension_scorers,
    render_crosswalk_view,
)
from ui.heatmap import build_heatmap
from evaluation.cases import STUB_CASES
from evaluation.runner import run_all, stub_summary


# ------------------------------------------------------------------
# Page config
# ------------------------------------------------------------------
st.set_page_config(
    page_title="Agentic AI Governance Management System",
    page_icon=":shield:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Agentic AI Governance Management System")
st.markdown(
    "**For Nigerian public sector and large enterprises.** "
    "This assessment tool scores an institution's governance of agentic AI "
    "across six dimensions and five maturity levels, calibrated to two "
    "sector variants. Every score maps to a named Nigerian and international "
    "regulatory anchor."
)

# ------------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------------
variant_id = render_variant_selector()

st.sidebar.divider()
st.sidebar.markdown(
    "**Source code:** "
    "[github.com/joel-onojason/agentic-ai-governance]"
    "(https://github.com/joel-onojason/agentic-ai-governance)"
)
st.sidebar.caption(
    "This tool is stateless. No account, no database, no institutional data "
    "stored. Every scoring session is independent."
)

# ------------------------------------------------------------------
# Tabs
# ------------------------------------------------------------------
tab_assess, tab_cases, tab_about = st.tabs(
    ["Assess an institution", "Retrospective cases", "About the model"]
)


# ============ TAB 1: ASSESS ============
with tab_assess:
    st.header("Score the six governance dimensions")
    st.caption(
        "Score each dimension on the 1 to 5 scale. Expand the ladder to read "
        "the descriptor for each level before choosing. Both variants use the "
        "same descriptors; only the weighting profile differs."
    )
    st.divider()

    scores = render_all_dimension_scorers()

    st.header("Result")
    result = calculate_by_variant_id(variant_id, scores)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric(
            label="Weighted maturity score",
            value=f"{result.weighted_total} / 5.00",
            help="Sum of (dimension score × dimension weight) for the selected variant.",
        )
        st.metric(
            label="Overall maturity level",
            value=result.maturity_level_name,
        )
        # Contribution breakdown
        st.markdown("**Per-dimension contribution**")
        contribution_lines = []
        for dim in ALL_DIMENSIONS:
            score = result.scores[dim.id]
            weight = result.weights[dim.id]
            contrib = result.contributions[dim.id]
            contribution_lines.append(
                f"- **{dim.id}** {dim.name}: {score} × {weight:.2f} = {contrib:.2f}"
            )
        st.markdown("\n".join(contribution_lines))

    with col2:
        variant = get_variant(variant_id)
        fig = build_heatmap(
            scores, title=f"{variant.name}: governance heat-map"
        )
        st.plotly_chart(fig, width="stretch")

    st.divider()
    render_crosswalk_view()


# ============ TAB 2: RETROSPECTIVE CASES ============
with tab_cases:
    st.header("Retrospective case runner")
    st.caption(stub_summary())

    st.markdown(
        "Each case below has been empirically coded against its primary "
        "source under the five-level rubric. Chapter Four of the thesis "
        "documents the coding method; the full per-dimension evidence tables "
        "sit in `docs/CASE_CODING_APPENDIX.md`."
    )

    # Run the full evaluation table, then show only the selected variant.
    df = run_all()
    df = df[df["variant_id"] == variant_id]
    st.dataframe(
        df,
        hide_index=True,
        width="stretch",
        column_config={
            "case_name": st.column_config.TextColumn("Case", width="medium"),
            "jurisdiction": st.column_config.TextColumn("Jurisdiction"),
            "variant_id": st.column_config.TextColumn("Variant"),
            "weighted_score": st.column_config.NumberColumn("Score", format="%.2f"),
            "maturity_level": st.column_config.TextColumn("Level"),
        },
    )

    st.divider()

    # Detail expander for each case
    for case in STUB_CASES:
        with st.expander(case.name):
            st.markdown(f"**Jurisdiction:** {case.jurisdiction}")
            st.markdown(f"**Date range:** {case.date_range}")
            st.markdown(f"**Failure signature:** {case.failure_signature}")

            st.markdown("**Per-dimension coding**")
            for dim in ALL_DIMENSIONS:
                st.markdown(
                    f"- **{dim.id}** ({dim.name}): Level {case.scores[dim.id]}. "
                    f"{case.rationale[dim.id]}"
                )

            st.markdown("**Primary sources**")
            for src in case.primary_sources:
                st.markdown(f"- {src}")

            # Show heat-map for this case under the selected variant
            fig = build_heatmap(
                case.scores, title=f"{case.name.split(' (')[0]}: heat-map"
            )
            st.plotly_chart(fig, width="stretch")


# ============ TAB 3: ABOUT ============
with tab_about:
    st.header("About the model")
    st.markdown("""
This system is the artefact of a Master's project on the design of an
Agentic AI Governance Management System for Nigerian public sector and
large enterprises. The model is built on the design science research
framework of Hevner et al. (2004) and the maturity-model procedure of
Becker, Knackstedt and Poppelbuss (2009).

The system is intentionally stateless. It holds no user accounts and no
persistent institutional data. A system that stored governance data would
itself become a data controller of major importance under section 44 of
the Nigeria Data Protection Act 2023, which would contradict the very Act
the system assesses against. Statelessness removes that contradiction.

**How to use it**

1. Choose the variant that fits the institution being assessed.
2. Score each of the six dimensions on the 1 to 5 scale, using the ladder
   descriptors as a reference.
3. Read the weighted score, the heat-map, and the per-dimension breakdown.
4. Re-score after acting on the weakest dimensions to plan the path to a
   higher maturity level.

**Six dimensions**
""")
    for dim in ALL_DIMENSIONS:
        st.markdown(f"- **{dim.id} {dim.long_name}.** {dim.rationale}")

    st.divider()
    st.markdown(
        "**Repository:** "
        "[github.com/joel-onojason/agentic-ai-governance]"
        "(https://github.com/joel-onojason/agentic-ai-governance)"
    )
    st.caption("Version 1.0.0. Released under the MIT License.")
