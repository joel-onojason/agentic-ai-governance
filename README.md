# Agentic AI Governance Management System

A Streamlit-based governance assessment tool for **Nigerian public sector
institutions and large enterprises**. The system scores an institution's
governance of agentic AI across **six dimensions** and **five maturity
levels**, calibrated to two sector variants, and produces a weighted
maturity score, a six-cell heat-map, and a regulatory cross-walk.

**Source:** the artefact of a Master's project (MIT 8343, Miva Open
University). See the thesis for the full design rationale.

**Repository:** https://github.com/joel-onojason/agentic-ai-governance

**Licence:** MIT.

---

## What it does

- Scores an institution on six governance dimensions:
  1. **D1** Autonomy and tool-use governance
  2. **D2** Agent identity and authentication
  3. **D3** Multi-agent and delegation oversight
  4. **D4** Human-in-the-loop and kill-switch design
  5. **D5** Data and privacy under NDPA and GAID
  6. **D6** Accountability and audit logging
- Applies one of two configured variants:
  - **Public Sector** (raises D4 and D5 to 0.20 each)
  - **Large Enterprise** (raises D1 and D2 to 0.20 each)
- Returns a weighted score in [1.00, 5.00] mapped to the CMMI-aligned
  levels (Ad hoc, Initial, Defined, Managed, Optimising).
- Renders a six-cell heat-map that visualises the per-dimension score.
- Runs a retrospective case set (three stub cases in this version;
  twelve to fifteen in the full thesis evaluation).

## Design principle: stateless by choice

The system stores no user data. There is no database, no user account,
and no persistent institutional record. A governance management system
that retained institutional data would itself become a Data Controller
of Major Importance under section 44 of the Nigeria Data Protection Act,
which would contradict the very Act the system assesses against.
Statelessness removes that contradiction.

## Run it locally

Requires Python 3.10 or later.

```bash
git clone https://github.com/joel-onojason/agentic-ai-governance.git
cd agentic-ai-governance
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Open the URL Streamlit prints (usually http://localhost:8501).

## Run the tests

```bash
pip install pytest
python -m pytest tests/
```

The test suite verifies:

- Every variant's weights sum to 1.00 and cover exactly D1..D6.
- All 30 descriptor cells are present and non-empty.
- The scoring engine rejects out-of-range scores and unknown variants.
- The three stub cases carry the exact scores documented in the
  case coding appendix.

## Deploy to Streamlit Community Cloud

1. Fork or push this repo to GitHub.
2. Sign in at https://share.streamlit.io with the same GitHub account.
3. Point Streamlit Cloud at `app.py` in this repo.
4. Streamlit builds the environment from `requirements.txt` and
   publishes at a public URL of the form
   `https://<repo>.streamlit.app`.
5. Every push to `main` triggers a redeploy.

No secrets, no environment variables, no external services are needed.

## Repository layout

```
agentic-ai-governance/
├── app.py                    Streamlit entry point
├── core/                     The immutable reference layer
│   ├── dimensions.py         Six governance dimensions (D1..D6)
│   ├── levels.py             Five maturity levels
│   ├── descriptors.py        Thirty descriptor cells
│   ├── variants.py           Two weight profiles
│   ├── crosswalk.py          Regulatory cross-walk per dimension
│   └── scoring.py            Weighted score arithmetic
├── ui/                       Streamlit presentation layer
│   ├── components.py         Reusable widgets
│   └── heatmap.py            Six-cell Plotly heat-map
├── evaluation/               Retrospective case runner
│   ├── cases.py              Three stub cases (empirically coded)
│   └── runner.py             Scores every case under every variant
├── tests/                    Unit tests
├── docs/
│   └── CASE_CODING_APPENDIX.md    Full per-dimension evidence tables
├── .streamlit/config.toml    Streamlit runtime configuration
├── requirements.txt          Python dependencies
├── LICENSE                   MIT
└── README.md                 This file
```

## Case coding

The three stub cases in `evaluation/cases.py` are:

| Case | Jurisdiction | Signature |
|------|--------------|-----------|
| Meta / WhatsApp joint NDPC-FCCPC (2024-2025) | Nigerian precursor | Documented controls defeated by enforcement collapse |
| Apple Card / Goldman Sachs (2019-2021) | International agentic comparator | Defensible model governance without transparency |
| Ghana Mahama deepfake (2026) | International agentic comparator | Governance vacuum with reactive criminal accountability |

Full per-dimension evidence tables, with primary-source citations, are
in `docs/CASE_CODING_APPENDIX.md`. Chapter Five of the thesis extends
the sample to the full twelve to fifteen case set using the same method.

## Repository state and reproducibility

Two git tags mark the two ex-ante and ex-post moments of the design
science progression documented in the thesis:

- `v1.0-chapter4` — the three-stub state at the close of Chapter Four.
  Reproduces Table 4.2, Figures 4.1 through 4.4, and the pytest suite
  as it stood at initial delivery.
- `v1.1-chapter5` — the fifteen-case extended state at the close of
  Chapter Five. Reproduces Tables 5.4 and 5.5, Figures 5.1 through
  5.4, and the extended pytest suite.

To inspect either state locally:

    git checkout v1.0-chapter4    # ex-ante artefact (3 stubs)
    git checkout v1.1-chapter5    # ex-post extended artefact (15 cases)
    git checkout main             # current live state

## Citation

If you use this artefact, please cite the thesis:

> Onojason, J. (2026). *Agentic AI Governance Management System for
> Nigerian Public Sector and Large Enterprises*. Master's dissertation,
> Miva Open University.
