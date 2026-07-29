"""End-to-end smoke tests for the Streamlit app via the AppTest harness.

These exercise app.py together with ui/components.py the way a real browser
session does: initial render plus widget interactions that trigger full script
reruns. Beyond checking the app assembles, the interaction tests are a
permanent regression guard against the native-library segfault that used to
crash the app on every rerun.
"""

import pytest

from streamlit.testing.v1 import AppTest

APP = "app.py"
TIMEOUT = 90


def _score(at: AppTest) -> float:
    """Parse the weighted-maturity metric value, e.g. '1.6 / 5.00' -> 1.6."""
    return float(at.metric[0].value.split("/")[0].strip())


@pytest.fixture
def app() -> AppTest:
    at = AppTest.from_file(APP, default_timeout=TIMEOUT).run()
    assert not at.exception, at.exception
    return at


def test_app_starts_without_exception(app: AppTest) -> None:
    assert not app.exception


def test_expected_widgets_render(app: AppTest) -> None:
    assert len(app.slider) == 6          # one per dimension
    assert len(app.radio) == 1           # variant selector
    assert len(app.tabs) == 3            # Assess / Cases / About
    assert len(app.metric) >= 2          # weighted score + maturity level
    assert len(app.dataframe) == 1       # retrospective cases table


def test_default_state_is_floor_score(app: AppTest) -> None:
    """All sliders default to level 1, so the weighted score must be 1.0."""
    assert _score(app) == pytest.approx(1.0)


def test_slider_interaction_reruns_without_crashing(app: AppTest) -> None:
    app.slider[0].set_value(5).run()
    assert not app.exception          # <-- would be a segfault/exception before the fix
    assert _score(app) > 1.0          # raising a dimension raises the weighted score


def test_all_sliders_max_gives_top_score(app: AppTest) -> None:
    for s in app.slider:
        s.set_value(5)
    app.run()
    assert not app.exception
    assert _score(app) == pytest.approx(5.0)


def test_variant_switch_reweights_score(app: AppTest) -> None:
    """With only D1 high, the large-enterprise variant (D1 weight 0.20) must
    score higher than the public-sector variant (D1 weight 0.15). This proves
    the variant weighting flows end-to-end through the UI."""
    app.slider[0].set_value(5).run()      # D1 -> 5, others stay 1
    assert not app.exception
    public_score = _score(app)

    app.radio[0].set_value("large_enterprise").run()
    assert not app.exception
    enterprise_score = _score(app)

    assert enterprise_score > public_score


def test_repeated_interactions_are_stable(app: AppTest) -> None:
    """Hammer several reruns in a row; the old pyarrow segfault surfaced on
    interaction, so this loop is the tightest regression net."""
    for level in (2, 3, 4, 5, 1):
        app.slider[2].set_value(level).run()
        assert not app.exception
    assert len(app.dataframe) == 1
