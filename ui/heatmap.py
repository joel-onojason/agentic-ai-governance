"""
ui.heatmap
===========
Plotly rendering of the six-cell heat-map that visualises per-dimension
scores after a scoring run.

The heat-map is laid out as a 2 x 3 grid (2 rows, 3 columns) rather than as
a 1 x 6 strip. The 1 x 6 strip is what an unconfigured Plotly heat-map
would produce and it stretches oddly on a portrait document. The 2 x 3
grid is compact, prints cleanly, and lets the reader compare adjacent
dimensions at a glance.

Colour scale is sequential (light for low maturity, dark for high). A
sequential scale is used rather than a diverging one because the 1 to 5
score is ordinal, not centred on a neutral midpoint.

Reference: Section 4.2.7 of the project thesis.
"""

from typing import Dict

import plotly.graph_objects as go

from core.dimensions import ALL_DIMENSIONS


# The 2 x 3 layout: row 0 top, row 1 bottom.
# Dimensions are placed left-to-right, top-to-bottom:
#   D1 D2 D3
#   D4 D5 D6
_LAYOUT = [
    ["D1", "D2", "D3"],
    ["D4", "D5", "D6"],
]


def build_heatmap(scores: Dict[str, int], title: str = "Governance Maturity Heat-Map") -> go.Figure:
    """
    Build a Plotly Figure for the six-dimension heat-map.

    Args:
        scores: {dimension_id: level 1..5} for all six dimensions.
        title:  Chart title. Defaults to a descriptive label.

    Returns:
        A Plotly Figure ready for st.plotly_chart().
    """
    # Build the z matrix (values), the hover text, and the annotations.
    z = [[scores[dim_id] for dim_id in row] for row in _LAYOUT]

    dim_name_by_id = {d.id: d.name for d in ALL_DIMENSIONS}

    # Hover text carries the dimension long name and the score.
    hover = [
        [
            f"<b>{dim_id}: {dim_name_by_id[dim_id]}</b><br>Level {scores[dim_id]} / 5"
            for dim_id in row
        ]
        for row in _LAYOUT
    ]

    # Annotations put the score inside each cell.
    annotations = []
    for r, row in enumerate(_LAYOUT):
        for c, dim_id in enumerate(row):
            annotations.append(
                dict(
                    x=c,
                    y=r,
                    text=f"<b>{dim_id}</b><br>Level {scores[dim_id]}",
                    showarrow=False,
                    font=dict(
                        color="white" if scores[dim_id] >= 3 else "black",
                        size=14,
                    ),
                )
            )

    fig = go.Figure(
        data=go.Heatmap(
            z=z,
            x=[dim_name_by_id[d] for d in _LAYOUT[0]],
            y=["", ""],  # rows are unlabelled to keep the layout clean
            hovertext=hover,
            hoverinfo="text",
            colorscale="Blues",
            zmin=1,
            zmax=5,
            colorbar=dict(
                title="Maturity",
                tickmode="array",
                tickvals=[1, 2, 3, 4, 5],
                ticktext=["1 Ad hoc", "2 Initial", "3 Defined", "4 Managed", "5 Optimising"],
                thickness=15,
            ),
            xgap=4,
            ygap=4,
        )
    )

    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor="center"),
        annotations=annotations,
        height=380,
        margin=dict(l=20, r=20, t=60, b=40),
        yaxis=dict(autorange="reversed"),  # so D1..D3 sit on top
    )

    return fig
