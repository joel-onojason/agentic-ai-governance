"""
evaluation.cases
=================
The retrospective case set used to validate the Agentic AI Governance
Management System.

This module carries the three stub cases coded in Chapter Four of the
thesis. Chapter Five extends the sample to the full twelve to fifteen cases
using the same coding method.

Each case carries:
  - a unique id and a human-readable name
  - the jurisdiction (Nigerian precursor or international agentic comparator)
  - the six dimension scores (D1..D6), each an integer in [1, 5]
  - the primary source(s) the scoring is anchored on
  - a per-dimension rationale traceable to the coding appendix
  - a narrative failure signature summarising the case

**Coding method.** Every score in this file is empirically coded against
primary sources under the five-level rubric. The full per-dimension
evidence tables sit in docs/CASE_CODING_APPENDIX.md and are also cited in
Section 4.2.8 of the thesis. The coding rule was: default to the lower
level when a dimension was not directly at issue in the primary source, and
raise the level only when the primary source affirmatively documented the
higher-level attribute (continuous monitoring, scheduled auditing, drilling,
prospective review, or red-teaming).
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class RetrospectiveCase:
    id: str
    name: str
    jurisdiction: str          # 'Nigerian precursor' or 'International agentic comparator'
    date_range: str            # e.g. '2024-2025'
    scores: Dict[str, int]     # dimension id → level 1..5
    primary_sources: List[str]
    rationale: Dict[str, str]  # dimension id → one-sentence reason for the score
    failure_signature: str     # 3-4 sentence narrative summary


# =====================================================================
# CASE 1 — Meta / WhatsApp joint NDPC-FCCPC enforcement action
# =====================================================================
# Empirical coding: D1=2, D2=2, D3=2, D4=2, D5=3, D6=2
# Failure signature: documented controls defeated by enforcement collapse.
# Full evidence table: docs/CASE_CODING_APPENDIX.md, Case 1.
META_WHATSAPP = RetrospectiveCase(
    id="meta_whatsapp_ng_2024",
    name="Meta / WhatsApp joint NDPC-FCCPC enforcement action (Nigeria)",
    jurisdiction="Nigerian precursor",
    date_range="2024-2025",
    scores={"D1": 2, "D2": 2, "D3": 2, "D4": 2, "D5": 3, "D6": 2},
    primary_sources=[
        "FCCPC Final Order, WhatsApp LLC and Meta Platforms Inc., 18 July 2024. "
        "https://fccpc.gov.ng/wp-content/uploads/2024/07/Final-order-FCCPC-Meta-18072024.pdf",
        "Competition and Consumer Protection Tribunal ruling, 25 April 2025.",
        "NDPC Final Orders against Meta Platforms Inc. and WhatsApp LLC, 18 February 2025.",
        "Federal High Court Abuja consent judgment, Suit No. FHC/ABJ/CS/355/2025, "
        "3 November 2025 (Hon. Justice J. K. Omotosho).",
        "Data Privacy Lawyers Association of Nigeria pre-action notice, 15 December 2025.",
    ],
    rationale={
        "D1": (
            "Level 2. The FCCPC Final Order of 18 July 2024 required Meta to "
            "revert to 2016 data-sharing practices and to install an opt-in "
            "screen, showing that scope constraints on the automated data "
            "pipeline had to be imposed by the regulator rather than by the "
            "controller."
        ),
        "D2": (
            "Level 2. The NDPC action found Meta was processing the data of "
            "non-users, indicating the data-subject identity boundary was not "
            "properly bounded at scale (approximately 61 million Nigerians "
            "affected)."
        ),
        "D3": (
            "Level 2. FCCPC Order 5 directed Meta to cease the tying and "
            "transfer of data between WhatsApp and Facebook without express "
            "consent, showing that inter-service delegation was occurring "
            "without governed oversight."
        ),
        "D4": (
            "Level 2. FCCPC Order 1 required Meta to reinstate the right of "
            "Nigerian users to restrict and withdraw consent without deleting "
            "the app; no proportionate human control point existed by design."
        ),
        "D5": (
            "Level 3. The regulatory findings were mapped to named anchors "
            "(FCCPA ss. 17, 33, 110, 111; NDPR Reg 2.3 consent and Reg 2.11 "
            "cross-border transfer) and produced enforceable orders on "
            "consent, cross-border transfer, and non-user data."
        ),
        "D6": (
            "Level 2. Documented Final Orders existed but were vacated on the "
            "NDPC track by the November 2025 consent judgment, with no "
            "affected data subjects joined, collapsing sustained accountability."
        ),
    },
    failure_signature=(
        "Documented controls defeated by enforcement collapse. Moderate "
        "regulatory maturity (Level 3 on data-and-privacy findings mapped to "
        "named statutory anchors) regressed when the NDPC's $32.8 million "
        "order was set aside by a Federal High Court consent judgment entered "
        "without affected data subjects. Autonomy, identity, delegation, and "
        "human-oversight dimensions never rose above Level 2, giving a "
        "high-D5 / depressed-D6 shape."
    ),
)


# =====================================================================
# CASE 2 — Apple Card / Goldman Sachs algorithmic credit-decision investigation
# =====================================================================
# Empirical coding: D1=3, D2=3, D3=3, D4=2, D5=4, D6=3
# Failure signature: defensible model governance without human-facing transparency.
# Full evidence table: docs/CASE_CODING_APPENDIX.md, Case 2.
APPLE_CARD = RetrospectiveCase(
    id="apple_card_us_2019",
    name="Apple Card / Goldman Sachs algorithmic credit-decision investigation (USA)",
    jurisdiction="International agentic comparator",
    date_range="2019-2021",
    scores={"D1": 3, "D2": 3, "D3": 3, "D4": 2, "D5": 4, "D6": 3},
    primary_sources=[
        "NYDFS Report on Apple Card Investigation, 23 March 2021. "
        "https://www.dfs.ny.gov/reports_and_publications/202103_report_apple_card_investigation",
        "NYDFS Press Release, DFS Issues Findings on the Apple Card and Its "
        "Underwriter Goldman Sachs Bank, 23 March 2021.",
        "Statements by David Heinemeier Hansson, November 2019.",
        "Goldman Sachs public statements on Apple Card credit methodology, "
        "November 2019.",
    ],
    rationale={
        "D1": (
            "Level 3. NYDFS found the underwriting model operated within a "
            "documented credit policy and the fair-lending program was in "
            "place to ensure the model did not consider prohibited "
            "characteristics; scope was bounded by policy."
        ),
        "D2": (
            "Level 3. Goldman Sachs Bank USA was the identified, regulated "
            "New York State-chartered bank operating under ECOA and NY Exec. "
            "Law s. 296-a; the acting-party identity layer was clear and "
            "documented."
        ),
        "D3": (
            "Level 3. Although Apple Card was marketed as created by Apple, "
            "NYDFS confirmed Goldman was responsible for the credit policy, "
            "underwriting decisions, and program management; the Apple to "
            "Goldman delegation was allocated to the regulated party."
        ),
        "D4": (
            "Level 2. Customers perceived a black box and customer-service "
            "agents could not explain individual credit-limit decisions; the "
            "six-month waiting period before appeals meant no timely human "
            "override existed by design, only removed reactively after media "
            "scrutiny."
        ),
        "D5": (
            "Level 4. NYDFS ran regression analysis on approximately 400,000 "
            "New York State applicants and found no unlawful discrimination; "
            "the Bank ran a documented, third-party-reviewed fair-lending "
            "program that met the Managed level of the rubric."
        ),
        "D6": (
            "Level 3. At NYDFS's request the Bank explained credit decisions "
            "for individuals who sent discrimination complaints and could "
            "identify the factors driving each decision; the audit trail and "
            "the accountable owner (Goldman Sachs Bank USA) were established."
        ),
    },
    failure_signature=(
        "Technically defensible model governance without human-facing "
        "transparency. Goldman's fair-lending program and model auditing "
        "reached Level 4, and NYDFS found no unlawful discrimination. The "
        "failure was concentrated in the human-in-the-loop dimension: the "
        "credit-decision was a black box to consumers and front-line staff, "
        "with no timely appeal path until public pressure forced a change. "
        "The signature is strong back-end model governance with an absent "
        "front-end explainability and override layer."
    ),
)


# =====================================================================
# CASE 3 — Ghana Mahama deepfake case
# =====================================================================
# Empirical coding: D1=1, D2=1, D3=1, D4=1, D5=1, D6=2
# Failure signature: no preventive governance, reactive criminal accountability only.
# Full evidence table: docs/CASE_CODING_APPENDIX.md, Case 3.
GHANA_MAHAMA = RetrospectiveCase(
    id="ghana_mahama_deepfake_2026",
    name="Ghana Mahama deepfake case (Ghana)",
    jurisdiction="International agentic comparator",
    date_range="March-May 2026",
    scores={"D1": 1, "D2": 1, "D3": 1, "D4": 1, "D5": 1, "D6": 2},
    primary_sources=[
        "Ghana Police Service / Cyber Vetting and Enforcement Team (CVET) "
        "statement on 11 arrests, 7 May 2026.",
        "Ghana News Agency, Eleven arrested for allegedly impersonating "
        "President John Mahama, 8 May 2026. "
        "https://gna.org.gh/2026/05/eleven-arrested-for-allegedly-impersonating-president-john-mahama/",
        "Ghana Cyber Security Authority statements on deepfake takedown "
        "workflow, 29 September 2025 (via GhanaFact).",
        "Ghana Data Protection Act 2012, Act 843.",
        "Cybersecurity Act 2020, Act 1038.",
    ],
    rationale={
        "D1": (
            "Level 1. The generative pipeline was itself the criminal "
            "instrument; no tool allow-list, scope constraint, or action "
            "logging existed, and no source identified the specific "
            "generation model or app used."
        ),
        "D2": (
            "Level 1. The fraud is an identity-authentication failure by "
            "definition: the deepfake impersonated a verified public figure "
            "(the President) with no platform identity verification preventing "
            "propagation; exhibits included 120 pre-registered SIM cards "
            "indicating deliberate identity obfuscation."
        ),
        "D3": (
            "Level 1. Distribution ran across Facebook, TikTok, and WhatsApp "
            "with no governed oversight of cross-platform propagation and no "
            "automated delegation control."
        ),
        "D4": (
            "Level 1. No preventive human checkpoint or kill-switch existed "
            "on distribution channels; the Cyber Security Authority described "
            "takedown as manual and reactive, with new accounts appearing "
            "faster than existing ones could be removed."
        ),
        "D5": (
            "Level 1. Misuse of President Mahama's likeness and voice "
            "occurred with no lawful basis or consent; Ghana's Data "
            "Protection Act 2012 does not explicitly reference DPIA, and no "
            "data-protection control operated over the synthetic reproduction."
        ),
        "D6": (
            "Level 2. Accountability was reactive only, through the CVET "
            "arrests of eleven suspects and remand of nine; media referenced "
            "the Cybersecurity Act 2020 in general but no specific charge "
            "sections were itemised in the sources available."
        ),
    },
    failure_signature=(
        "No preventive governance with reactive criminal accountability. "
        "Because the system is an adversarial criminal pipeline rather than "
        "a governed enterprise, five of the six dimensions sit at Level 1: "
        "no tool constraints, no identity verification, no delegation "
        "oversight, no human kill-switch on distribution, and no data-"
        "protection control over misuse of the President's likeness. The "
        "single dimension that rises is D6, and only reactively, through "
        "arrests. The signature is a governance vacuum with an ex-post "
        "criminal response."
    ),
)


# =====================================================================
# The full stub set exported for the runner
# =====================================================================
STUB_CASES: Tuple[RetrospectiveCase, ...] = (META_WHATSAPP, APPLE_CARD, GHANA_MAHAMA)


def get_case(case_id: str) -> RetrospectiveCase:
    for c in STUB_CASES:
        if c.id == case_id:
            return c
    raise KeyError(f"Unknown case id: {case_id}")
