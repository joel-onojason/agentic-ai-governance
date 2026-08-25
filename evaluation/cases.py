"""
evaluation.cases
=================
The retrospective case set used to validate the Agentic AI Governance
Management System.

This module carries the initial three stub cases shipped with the Chapter
Four delivery, plus the twelve extension cases added for Chapter Five,
giving a total sample of fifteen. The three originals sit in STUB_CASES.
The full fifteen sit in ALL_CASES. The runner defaults to ALL_CASES so the
Retrospective cases tab surfaces the full extended sample.

Each case carries:
  - a unique id and a human-readable name
  - the jurisdiction ('Nigerian precursor', 'International agentic
    comparator', or 'Regulator-maturity benchmark')
  - the six dimension scores (D1..D6), each an integer in [1, 5]
  - the primary source(s) the scoring is anchored on
  - a per-dimension rationale traceable to the coding appendix
  - a narrative failure signature summarising the case

**Coding method.** Every score in this file is empirically coded against
primary sources under the five-level rubric. The full per-dimension
evidence tables sit in docs/CASE_CODING_APPENDIX.md and are also cited in
Chapter Four (three original stubs) and Chapter Five (twelve extensions)
of the thesis. The coding rule was: default to the lower level when a
dimension was not directly at issue in the primary source, and raise the
level only when the primary source affirmatively documented the higher-
level attribute (continuous monitoring, scheduled auditing, drilling,
prospective review, or red-teaming).
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class RetrospectiveCase:
    id: str
    name: str
    jurisdiction: str
    date_range: str
    scores: Dict[str, int]
    primary_sources: List[str]
    rationale: Dict[str, str]
    failure_signature: str


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
            "logging existed."
        ),
        "D2": (
            "Level 1. The fraud is an identity-authentication failure by "
            "definition: the deepfake impersonated a verified public figure "
            "with no platform identity verification preventing propagation; "
            "exhibits included 120 pre-registered SIM cards."
        ),
        "D3": (
            "Level 1. Distribution ran across Facebook, TikTok, and WhatsApp "
            "with no governed oversight of cross-platform propagation."
        ),
        "D4": (
            "Level 1. No preventive human checkpoint or kill-switch existed; "
            "the Cyber Security Authority described takedown as manual and "
            "reactive, with new accounts appearing faster than existing ones "
            "could be removed."
        ),
        "D5": (
            "Level 1. Misuse of President Mahama's likeness and voice "
            "occurred with no lawful basis or consent; Ghana's Data "
            "Protection Act 2012 does not explicitly reference DPIA."
        ),
        "D6": (
            "Level 2. Accountability was reactive only, through the CVET "
            "arrests of eleven suspects and remand of nine."
        ),
    },
    failure_signature=(
        "No preventive governance with reactive criminal accountability. "
        "Because the system is an adversarial criminal pipeline rather than "
        "a governed enterprise, five of the six dimensions sit at Level 1: "
        "no tool constraints, no identity verification, no delegation "
        "oversight, no human kill-switch on distribution, and no data-"
        "protection control. D6 rises only through ex-post arrests."
    ),
)


# =====================================================================
# CASE 4 — Sokoloan / Soko Lending Company (NITDA sanction, 2021)
# =====================================================================
# Empirical coding: D1=1, D2=2, D3=1, D4=1, D5=2, D6=1
# PS 1.35, LE 1.35. Data-privacy and oversight dominated, automation-abused.
SOKOLOAN_NITDA_2021 = RetrospectiveCase(
    id="sokoloan_nitda_2021",
    name="Sokoloan / Soko Lending Company NITDA sanction (Nigeria)",
    jurisdiction="Nigerian precursor",
    date_range="August 2021",
    scores={"D1": 1, "D2": 2, "D3": 1, "D4": 1, "D5": 2, "D6": 1},
    primary_sources=[
        "NITDA, 'NITDA Sanctions SokoLoan for Privacy Invasion', August 2021. "
        "https://nitda.gov.ng/nitda-sanctions-soko-loan-for-privacy-invasion/",
        "Nairametrics, 19 August 2021.",
        "TechCabal, 24 August 2021.",
        "NDPR 2019, Articles 2.2, 2.3, 2.5, 3.1(7), 4.1(7).",
    ],
    rationale={
        "D1": (
            "Level 1. The app auto-harvested contacts and triggered privacy-"
            "invading debt-recovery messages with no controls; no tool "
            "allow-list or scope constraint existed."
        ),
        "D2": (
            "Level 2. Not directly at issue; inferred from posture that loans "
            "were disbursed on app-provided data with minimal verification."
        ),
        "D3": (
            "Level 1. Embedded trackers shared customer data with third "
            "parties without disclosure; no governed delegation oversight."
        ),
        "D4": (
            "Level 1. Automated privacy-invading messages were sent with no "
            "human gate; NITDA had to order a stop as the corrective, not a "
            "pre-existing control."
        ),
        "D5": (
            "Level 2. A privacy notice existed but was non-conforming (NDPR "
            "Arts 2.5, 3.1(7)) with insufficient lawful basis for processing."
        ),
        "D6": (
            "Level 1. No compliance audit filed via a licensed DPCO (NDPR "
            "Art 4.1(7)); the entity refused cooperation with the data "
            "protection authority."
        ),
    },
    failure_signature=(
        "Data-privacy and oversight dominated failure with a strong "
        "automation-abuse element. Near-uniform Level 1 across D1, D3, D4, "
        "and D6 reflects an entity with essentially no governance, "
        "weaponising automated data-harvesting and messaging. The NITDA "
        "order (mandatory DPIA, nine-month oversight) is the corrective, "
        "not a pre-existing control."
    ),
)


# =====================================================================
# CASE 5 — NIMC NIN/BVN black-market breaches
# =====================================================================
# Empirical coding: D1=1, D2=1, D3=1, D4=2, D5=2, D6=1
# PS 1.40, LE 1.30. Identity-authentication and accountability dominated failure.
NIMC_NIN_BVN = RetrospectiveCase(
    id="nimc_nin_bvn",
    name="NIMC NIN/BVN black-market breaches (Nigeria)",
    jurisdiction="Nigerian precursor",
    date_range="2024-2026",
    scores={"D1": 1, "D2": 1, "D3": 1, "D4": 2, "D5": 2, "D6": 1},
    primary_sources=[
        "Foundation for Investigative Journalism (FIJ), Investigation series "
        "on NIMC licensed front-end partners and the NIN/BVN black market, "
        "2024-2025. https://fij.ng/",
        "Paradigm Initiative statements, 2024-2025.",
        "NIMC public statement denying database breach, 2025.",
        "NIMC Act 2007 ss. 28-30 (unlawful access provisions).",
        "Biometric Update, August 2025.",
    ],
    rationale={
        "D1": (
            "Level 1. API keys enabling verification and modification were "
            "resold to unauthorised parties; no effective control over "
            "tool-level access."
        ),
        "D2": (
            "Level 1. FEP credentials were sub-leased with no binding of "
            "access to authorised identities; licensed-partner access was "
            "uncontrolled."
        ),
        "D3": (
            "Level 1. Licensed FEPs sub-leased access 'while regulators look "
            "away'; no monitoring of the delegation chain."
        ),
        "D4": (
            "Level 2. Reactive takedowns only after journalist exposure; no "
            "proactive halt to access existed."
        ),
        "D5": (
            "Level 2. Statutory protections exist (NIMC Act s. 30: up to 10 "
            "years or N10m for unlawful access) but were not enforced against "
            "the ecosystem."
        ),
        "D6": (
            "Level 1. FIJ recorded 'no outcome in 3 major cases'; NIMC denied "
            "any leak and the NDPC produced no visible enforcement outcome."
        ),
    },
    failure_signature=(
        "Identity-authentication and accountability dominated public-sector "
        "failure. A near-uniform Level 1 vector: the compromise is precisely "
        "in D2 and D3 (licensed-partner access resold with no oversight) at "
        "the heart of the national identity system, with D6 undermined by "
        "institutional denial. The single Level 2 (D4) reflects only "
        "reactive, journalist-triggered takedowns."
    ),
)


# =====================================================================
# CASE 6 — Hong Kong / UAE voice-clone bank fraud
# =====================================================================
# Empirical coding: D1=2, D2=1, D3=1, D4=1, D5=2, D6=2
# PS 1.50, LE 1.50. Identity-authentication dominated; the audio-only precursor to Arup.
HK_UAE_VOICE_CLONE_2020 = RetrospectiveCase(
    id="hk_uae_voice_clone_2020",
    name="Hong Kong / UAE bank voice-clone fraud",
    jurisdiction="International agentic comparator",
    date_range="Early 2020 (reported October 2021)",
    scores={"D1": 2, "D2": 1, "D3": 1, "D4": 1, "D5": 2, "D6": 2},
    primary_sources=[
        "Forbes, Thomas Brewster, 'Fraudsters Cloned Company Director's "
        "Voice In $35 Million Heist', 14 October 2021. "
        "https://www.forbes.com/sites/thomasbrewster/2021/10/14/huge-bank-fraud-uses-deep-fake-voice-tech-to-steal-millions/",
        "AI Incident Database, Incident 147. https://incidentdatabase.ai/cite/147/",
        "US court filing referenced in Forbes coverage (case documents not "
        "publicly indexed).",
    ],
    rationale={
        "D1": (
            "Level 2. Transfer authority was exercised on voice plus email "
            "confirmation, with no independent out-of-band verification for "
            "a USD 35 million transaction."
        ),
        "D2": (
            "Level 1. Voice recognition was treated as authentication; a "
            "'deep voice' clone defeated the only identity check present."
        ),
        "D3": (
            "Level 1. The instruction chain (director to lawyer to manager) "
            "was accepted at face value with no verification of the "
            "delegated coordination."
        ),
        "D4": (
            "Level 1. The manager acted alone; funds dispersed to accounts "
            "globally before any control triggered."
        ),
        "D5": (
            "Level 2. Data breach was not the issue; inferred low baseline "
            "given the absence of any verification infrastructure."
        ),
        "D6": (
            "Level 2. A transaction trail existed sufficient for post-hoc "
            "tracing of USD 400,000 across borders, but no proactive audit "
            "control detected the fraud."
        ),
    },
    failure_signature=(
        "Identity-authentication dominated failure and the audio-only "
        "precursor to the Arup video-conference fraud. Total D2 collapse "
        "(voice-as-identity) combined with Level 1 D3 and D4 (single actor, "
        "no delegation oversight, no kill-switch) produced the loss. D6 is "
        "marginally above ad hoc only because transaction logs later "
        "supported cross-border tracing."
    ),
)


# =====================================================================
# CASE 7 — JAMB 2025 UTME technical failure
# =====================================================================
# Empirical coding: D1=2, D2=2, D3=1, D4=1, D5=2, D6=3
# PS 1.80, LE 1.85. Algorithmic decision and oversight dominated public-sector failure.
JAMB_UTME_2025 = RetrospectiveCase(
    id="jamb_utme_2025",
    name="JAMB 2025 UTME technical failure (Nigeria)",
    jurisdiction="Nigerian precursor",
    date_range="May 2025",
    scores={"D1": 2, "D2": 2, "D3": 1, "D4": 1, "D5": 2, "D6": 3},
    primary_sources=[
        "TechCabal, 'Inside the server glitch behind JAMB's scrambled UTME "
        "score', 16 May 2025. "
        "https://techcabal.com/2025/05/16/inside-the-server-glitch-behind-jambs-scrambled-utme-score/",
        "TheCable, 'JAMB admits to error in 2025 UTME', 14 May 2025.",
        "TheCable, 'Man narrates how daughter committed suicide over subpar "
        "2025 UTME score'.",
        "Punch, 'UTME resit: JAMB to release results of 379,000 candidates'.",
        "JAMB press briefing by Registrar Prof. Ishaq Oloyede, 14 May 2025.",
    ],
    rationale={
        "D1": (
            "Level 2. New scoring and patch tools were deployed but the patch "
            "was not applied uniformly across servers; 'the real failure was "
            "in system discipline' (Educare lead engineer to TechCabal)."
        ),
        "D2": (
            "Level 2. Not directly at issue; candidate authentication was "
            "not the failure point."
        ),
        "D3": (
            "Level 1. Delegation to two service providers with no "
            "synchronisation oversight; the South-East had no dedicated "
            "server cluster and relied on the Lagos cluster over 450km away."
        ),
        "D4": (
            "Level 1. No human check caught the mass anomaly before results "
            "were released; the error was detected externally by Educare "
            "through a performance-prediction discrepancy."
        ),
        "D5": (
            "Level 2. Data protection was not the primary issue; result-data "
            "integrity was. Inferred from posture."
        ),
        "D6": (
            "Level 3. JAMB engaged psychometricians and computer scientists "
            "for an independent post-incident audit; Registrar Oloyede "
            "accepted personal responsibility publicly."
        ),
    },
    failure_signature=(
        "Algorithmic decision and oversight dominated public-sector failure. "
        "Total D3 and D4 collapse (no synchronisation oversight of delegated "
        "providers, no human check before releasing life-altering automated "
        "scores affecting 379,997 candidates), with the anomaly detected "
        "only externally. D6 rises to Defined on the strength of the "
        "post-hoc independent audit and candid public accountability."
    ),
)


# =====================================================================
# CASE 8 — Arup deepfake video conference fraud
# =====================================================================
# Empirical coding: D1=2, D2=1, D3=1, D4=2, D5=2, D6=3
# PS 1.85, LE 1.80. Identity-authentication and human-in-the-loop dominated failure.
ARUP_DEEPFAKE_2024 = RetrospectiveCase(
    id="arup_deepfake_2024",
    name="Arup deepfake video conference fraud (Hong Kong)",
    jurisdiction="International agentic comparator",
    date_range="January-May 2024",
    scores={"D1": 2, "D2": 1, "D3": 1, "D4": 2, "D5": 2, "D6": 3},
    primary_sources=[
        "CNN, 'Arup revealed as victim of $25 million deepfake scam', "
        "16 May 2024. "
        "https://www.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk",
        "South China Morning Post, 17 May 2024.",
        "World Economic Forum, 'Cybercrime: Lessons learned from a $25m "
        "deepfake attack' (Rob Greig, CIO), February 2025. "
        "https://www.weforum.org/stories/2025/02/deepfake-ai-cybercrime-arup/",
        "AI Incident Database, Incident 634. https://incidentdatabase.ai/cite/634/",
        "Hong Kong Police Force briefing (Acting Senior Superintendent "
        "Baron Chan Shun-ching), 17 May 2024.",
    ],
    rationale={
        "D1": (
            "Level 2. Fifteen transfers totalling HKD 200 million were "
            "executed on the strength of a video call with no independent "
            "tool or transaction verification gating high-value payments."
        ),
        "D2": (
            "Level 1. No mechanism existed to authenticate that call "
            "participants were genuine; deepfakes built from public video "
            "and audio went undetected."
        ),
        "D3": (
            "Level 1. A single employee acted on a delegated 'confidential "
            "transaction' instruction with no secondary approver or "
            "escalation until after funds were sent."
        ),
        "D4": (
            "Level 2. A human was in the loop and initially suspicious, but "
            "no verification protocol or stop-gate halted the fifteen "
            "transactions over a week."
        ),
        "D5": (
            "Level 2. No data breach was at issue (Arup: 'none of our "
            "internal systems were compromised'); inferred baseline given "
            "executives' public images and voice were exploitable open-"
            "source data."
        ),
        "D6": (
            "Level 3. Arup reported promptly to police, cooperated with the "
            "investigation, and the CIO publicly documented lessons at the "
            "World Economic Forum; post-incident review is evidenced."
        ),
    },
    failure_signature=(
        "Identity-authentication and human-in-the-loop dominated failure. "
        "Catastrophic collapse of D2 (no way to prove who was on the call) "
        "compounded by weak D1 and D3 transaction controls that let a "
        "single employee execute fifteen high-value transfers on a "
        "deepfaked instruction. D6 is relatively strong because of prompt "
        "reporting and public post-incident learning."
    ),
)


# =====================================================================
# CASE 9 — Flutterwave security incident series
# =====================================================================
# Empirical coding: D1=2, D2=2, D3=2, D4=2, D5=2, D6=2
# PS 2.00, LE 2.00. Control-monitoring and delegation dominated enterprise fintech failure.
FLUTTERWAVE_SERIES = RetrospectiveCase(
    id="flutterwave_series",
    name="Flutterwave security incident series (Nigeria)",
    jurisdiction="Nigerian precursor",
    date_range="2023-2024 (four incidents)",
    scores={"D1": 2, "D2": 2, "D3": 2, "D4": 2, "D5": 2, "D6": 2},
    primary_sources=[
        "TechCabal, 'Flutterwave begins recovery of $24 million', 8 February 2024. "
        "https://techcabal.com/2024/02/08/flutterwave-to-recover-missing-24million/",
        "TechCabal, 'Flutterwave loses N11 billion in security breach', 16 May 2024.",
        "Techpoint Africa, 'A fatal error by NIBSS worsened Flutterwave's N21 "
        "billion glitch'.",
        "Federal High Court Lagos Mareva injunction, 1 February 2024.",
        "Sahara Reporters coverage of February 2023 incident.",
    ],
    rationale={
        "D1": (
            "Level 2. POS merchants 'abused their access' and a settlement-"
            "limit misconfiguration went unreverted for three months; "
            "controls existed but were applied inconsistently."
        ),
        "D2": (
            "Level 2. KYC gaps at receiving neobanks hampered recovery; "
            "identity controls were inconsistent across the ecosystem."
        ),
        "D3": (
            "Level 2. The failure spanned Flutterwave, POS merchants, NIBSS "
            "and 35 institutions with no effective inter-party monitoring."
        ),
        "D4": (
            "Level 2. The settlement-limit tool cut off at N19 billion only "
            "after exposure; suspensions were applied reactively."
        ),
        "D5": (
            "Level 2. Data privacy was not the primary issue; a financial-"
            "controls failure. Inferred from posture."
        ),
        "D6": (
            "Level 2. Four recurrences in about fourteen months indicate "
            "audit and monitoring were not embedded; recovery relied on "
            "court order rather than internal control."
        ),
    },
    failure_signature=(
        "Control-monitoring and delegation dominated enterprise fintech "
        "failure. A flat Level 2 vector reflects an entity with policies "
        "and some detection (the N19 billion cut-off) but no continuous, "
        "audited, drilled controls, as evidenced by four recurrences in "
        "about fourteen months and reliance on a court order rather than "
        "internal kill-switches for recovery."
    ),
)


# =====================================================================
# CASE 10 — INEC IReV 2023 presidential election failure
# =====================================================================
# Empirical coding: D1=2, D2=2, D3=2, D4=2, D5=2, D6=3
# PS 2.15, LE 2.15. Algorithmic and system-availability dominated public-sector failure.
INEC_IREV_2023 = RetrospectiveCase(
    id="inec_irev_2023",
    name="INEC IReV 2023 presidential election failure (Nigeria)",
    jurisdiction="Nigerian precursor",
    date_range="25 February 2023",
    scores={"D1": 2, "D2": 2, "D3": 2, "D4": 2, "D5": 2, "D6": 3},
    primary_sources=[
        "INEC, Report on the conduct of the 2023 general elections, "
        "526-page post-mortem, February 2024.",
        "Premium Times, 'INEC gives details of IReV failure'. "
        "https://www.premiumtimesng.com/news/top-news/671063",
        "BusinessDay, 'INEC finally reveals why IReV failed in 2023 "
        "presidential poll'. "
        "https://businessday.ng/news/article/inec-finally-reveals-why-irev-failed-in-2023-presidential-poll/",
        "TheCable, 'HTTP server error: INEC finally opens up on IReV failure'.",
    ],
    rationale={
        "D1": (
            "Level 2. A configuration bug in the upload tool went undetected; "
            "controls were inconsistent across result types (NASS uploads "
            "worked while presidential did not)."
        ),
        "D2": (
            "Level 2. BVAS accreditation functioned; identity was not the "
            "failure point. Inferred moderate posture."
        ),
        "D3": (
            "Level 2. NASS results uploaded but presidential did not, "
            "revealing a configuration or mapping fault in a differentiated "
            "pipeline delegated across parallel processes."
        ),
        "D4": (
            "Level 2. Problem reported at 4pm, partially resolved in four "
            "hours via hotfixes; no pre-tested failover for the flagship poll."
        ),
        "D5": (
            "Level 2. Not a data-privacy failure; election-data integrity "
            "and availability. Inferred from posture."
        ),
        "D6": (
            "Level 3. Documented 526-page public post-mortem with root cause "
            "and remediation ('additional quality assurance checks', "
            "'end-to-end testing'); Supreme Court noted the effect on public "
            "confidence."
        ),
    },
    failure_signature=(
        "Algorithmic and system-availability dominated public-sector "
        "failure. A D1, D3, D4 configuration and contingency failure on "
        "the single most consequential upload path, with the flagship "
        "result stream failing while parallel streams succeeded. D6 "
        "reaches Defined on the strength of the detailed published post-"
        "mortem and documented resilience improvements."
    ),
)


# =====================================================================
# CASE 11 — NDPC v. Fidelity Bank (August 2024)
# =====================================================================
# Empirical coding: D1=2, D2=2, D3=2, D4=2, D5=3, D6=2
# PS 2.20, LE 2.15. Data-privacy dominated failure with vendor-oversight collapse.
NDPC_V_FIDELITY_2024 = RetrospectiveCase(
    id="ndpc_fidelity_2024",
    name="NDPC v. Fidelity Bank (Nigeria)",
    jurisdiction="Nigerian precursor",
    date_range="April 2023 - August 2024",
    scores={"D1": 2, "D2": 2, "D3": 2, "D4": 2, "D5": 3, "D6": 2},
    primary_sources=[
        "NDPC Final Order against Fidelity Bank Plc, 21 August 2024, "
        "statement by Babatunde Bamigboye, Head of Legal, Enforcement and "
        "Regulations.",
        "Premium Times, 'Nigerian govt fines Fidelity Bank N555.8 million', "
        "21 August 2024. https://www.premiumtimesng.com/business/business-news/726713",
        "TechCabal, 21 August 2024.",
        "BusinessDay, 'NDPC fines Fidelity Bank N555.8 million over data "
        "privacy violations'.",
    ],
    rationale={
        "D1": (
            "Level 2. Automated data-collection tools (cookies, banking app "
            "downloaded over one million times) were deployed without lawful "
            "basis; controls existed but were inconsistent."
        ),
        "D2": (
            "Level 2. Not directly at issue; inferred from posture that "
            "account-opening on data without proper consent implies weak "
            "subject-identity controls."
        ),
        "D3": (
            "Level 2. Reliance on 'non-compliant third-party data "
            "processors' cited by the NDPC is a failed delegation-oversight "
            "finding under NDPA vendor accountability."
        ),
        "D4": (
            "Level 2. Not directly at issue; inferred low posture given no "
            "evidence of consent-withdrawal or stop mechanisms."
        ),
        "D5": (
            "Level 3. Documented breach of NDPA 2023 and NDPR 2019 "
            "processing-without-consent provisions; a policy framework "
            "existed but was applied defectively."
        ),
        "D6": (
            "Level 2. The bank failed to provide accountability over more "
            "than ten correspondences during the year-long probe; penalty "
            "was aggravated for non-cooperation."
        ),
    },
    failure_signature=(
        "Data-privacy dominated failure. D5 is the crux (documented NDPA/"
        "NDPR consent breach), aggravated by D3 (processor non-compliance) "
        "and D6 (poor accountability during the probe). The bank had "
        "policies on paper but no tested, mapped controls, and its dispute "
        "of the finding underscores an immature accountability culture."
    ),
)


# =====================================================================
# CASE 12 — NDPC v. MultiChoice Nigeria (July 2025)
# =====================================================================
# Empirical coding: D1=2, D2=2, D3=2, D4=2, D5=3, D6=2
# PS 2.20, LE 2.15. Data-privacy dominated failure centred on cross-border transfer.
NDPC_V_MULTICHOICE_2025 = RetrospectiveCase(
    id="ndpc_multichoice_2025",
    name="NDPC v. MultiChoice Nigeria",
    jurisdiction="Nigerian precursor",
    date_range="Q2 2024 - July 2025",
    scores={"D1": 2, "D2": 2, "D3": 2, "D4": 2, "D5": 3, "D6": 2},
    primary_sources=[
        "NDPC statement (Babatunde Bamigboye), 6 July 2025.",
        "Punch, 'NDPC fines MultiChoice N766m', 7 July 2025. "
        "https://punchng.com/ndpc-fines-multichoice-%E2%82%A6766m-for-data-privacy-violations/",
        "Vanguard, 7 July 2025.",
        "The ICIR, 'NDPC fines MultiChoice Nigeria N766 million over data "
        "privacy violations'.",
        "Section 37, 1999 Constitution of the Federal Republic of Nigeria.",
        "NDPA 2023 s. 41 (cross-border transfer).",
    ],
    rationale={
        "D1": (
            "Level 2. Data-collection processes deemed 'patently intrusive, "
            "unfair, unnecessary and disproportionate' by the NDPC; tool "
            "governance was weak."
        ),
        "D2": (
            "Level 2. Not directly at issue; inferred from posture that "
            "processing extended to non-subscribers implies weak subject-"
            "identity boundaries."
        ),
        "D3": (
            "Level 2. Illegal cross-border transfer without adequacy, BCR, "
            "or SCC safeguards constitutes failed delegation to foreign "
            "processors."
        ),
        "D4": (
            "Level 2. Not directly at issue; inferred low posture."
        ),
        "D5": (
            "Level 3. Documented finding of illegal cross-border transfer "
            "and privacy violation (NDPA s. 41; s. 37 of the 1999 "
            "Constitution); policies existed but were non-compliant."
        ),
        "D6": (
            "Level 2. Remedial steps were unsatisfactory; the NDPC recorded "
            "'want of cooperation' and accountability was immature."
        ),
    },
    failure_signature=(
        "Data-privacy dominated failure centred on unlawful cross-border "
        "data flows (D5 and D3). The extension of processing to non-"
        "subscribers and the 'unsatisfactory' remediation give a D6 "
        "weakness. The vector closely mirrors Fidelity, marking a "
        "consistent NDPC enforcement pattern against large enterprises."
    ),
)


# =====================================================================
# CASE 13 — NDPC seven-firm N400m enforcement action (June 2024)
# =====================================================================
# Empirical coding: D1=2, D2=2, D3=2, D4=2, D5=3, D6=3
# PS 2.35, LE 2.30. Aggregate data-privacy enforcement across seven firms.
NDPC_SEVEN_FIRM_2024 = RetrospectiveCase(
    id="ndpc_seven_firm_2024",
    name="NDPC seven-firm N400m enforcement action (Nigeria)",
    jurisdiction="Nigerian precursor",
    date_range="June 2024",
    scores={"D1": 2, "D2": 2, "D3": 2, "D4": 2, "D5": 3, "D6": 3},
    primary_sources=[
        "NDPC public statement by Vincent Olatunji, National Commissioner, "
        "11 June 2024.",
        "TheCable, 'NDPC fines four banks, three companies N400m for data "
        "violation'. https://www.thecable.ng/ndpc-fines-four-banks-three-companies-n400m-for-data-violation/",
        "Nairametrics, 'Seven firms pay N400 million to NDPC as sanction "
        "for data breach', 12 June 2024. "
        "https://nairametrics.com/2024/06/12/seven-firms-pay-n400-million-to-ndpc-as-sanction-for-data-breach/",
        "Techpoint Africa, 'NDPC gets N400 million in fines from 7 "
        "companies for data breaches'.",
    ],
    rationale={
        "D1": (
            "Level 2. Aggregate action across seven firms; underlying "
            "entities showed inconsistent processing controls."
        ),
        "D2": (
            "Level 2. Not itemised per firm; inferred aggregate posture."
        ),
        "D3": (
            "Level 2. Breaches across sectors imply processor and delegation "
            "weaknesses common to the group."
        ),
        "D4": (
            "Level 2. Not detailed per firm; inferred low posture."
        ),
        "D5": (
            "Level 3. Seven documented resolutions with remediation fees "
            "under the NDPA (s. 48); enforcement mapped to the Act."
        ),
        "D6": (
            "Level 3. Regulator-driven accountability across 1,000+ "
            "investigations to date; entities paid remediation fees."
        ),
    },
    failure_signature=(
        "Data-privacy dominated aggregate enforcement case. The entity-side "
        "vector is a modest Level 2 with D5 and D6 at Defined, reflecting "
        "the documented, mapped remediation of seven firms. It corroborates "
        "the NDPC's escalating enforcement posture that culminates in the "
        "Fidelity, MultiChoice, and 1,368-firm actions."
    ),
)


# =====================================================================
# CASE 14 — FCCPC digital lending / DEON Regulations (BENCHMARK)
# =====================================================================
# Empirical coding: D1=3, D2=2, D3=3, D4=3, D5=3, D6=4
# PS 3.00, LE 2.95. Regulator-maturity benchmark, top-of-scale anchor.
FCCPC_DEON_2025 = RetrospectiveCase(
    id="fccpc_deon_2025",
    name="FCCPC digital lending / DEON Regulations 2025 (Nigeria)",
    jurisdiction="Regulator-maturity benchmark",
    date_range="2022-2026",
    scores={"D1": 3, "D2": 2, "D3": 3, "D4": 3, "D5": 3, "D6": 4},
    primary_sources=[
        "Sahara Reporters, 12 March 2022 (initial raids on GoCash, OKash, "
        "EasyCredit, Kashkash, Speedy Choice, Easy Moni, Sokoloan).",
        "TechCabal, 12 March 2022.",
        "FCCPC, 'FCCPC Resumes Digital Lending Regulation', 20 July 2026. "
        "https://fccpc.gov.ng/fccpc-resumes-digital-lending-regulation/",
        "Federal High Court Lagos judgment, Suit No. FHC/L/CS/760/2026, "
        "20 July 2026 (Hon. Justice A. L. Allagoa), upholding DEON "
        "Regulations 2025 as intra vires.",
        "TheCable, 'FCCPC resumes enforcement as court upholds digital "
        "lending regulations'.",
    ],
    rationale={
        "D1": (
            "Level 3. DEON creates documented controls over lending tools "
            "and data access mapped to the FCCPA 2018."
        ),
        "D2": (
            "Level 2. Operator registration and identity are required but "
            "only newly enforced; industry compliance is nascent."
        ),
        "D3": (
            "Level 3. Coordinated FCCPC, ICPC, NITDA, and NPF oversight of "
            "the sector; documented and role-assigned."
        ),
        "D4": (
            "Level 3. FCCPC executed kill-switch equivalents (app-store "
            "removals via letters to Google and Apple; account freezes with "
            "court warrants)."
        ),
        "D5": (
            "Level 3. DEON data-protection provisions upheld as intra vires "
            "by the Federal High Court in July 2026; documented and "
            "judicially validated."
        ),
        "D6": (
            "Level 4. Monitored enforcement with compliance deadlines (5 "
            "January 2026), suspension, and court-tested resumption "
            "evidence audit and accountability maturity."
        ),
    },
    failure_signature=(
        "Regulator-maturity benchmark rather than an entity failure. The "
        "FCCPC regime scores Defined to Managed because controls are "
        "documented, role-assigned, mapped to the FCCPA and NDPA, court-"
        "tested, and continuously enforced (D6 Managed). It does not reach "
        "Level 5 as no prospective or red-team adaptive governance is "
        "documented, only reactive-then-sustained enforcement."
    ),
)


# =====================================================================
# CASE 15 — NDPC 1,368-firm compliance notice (BENCHMARK, August 2025)
# =====================================================================
# Empirical coding: D1=3, D2=3, D3=3, D4=3, D5=4, D6=4
# PS 3.35, LE 3.30. Regulator-maturity benchmark, top-of-scale anchor.
NDPC_COMPLIANCE_NOTICE_2025 = RetrospectiveCase(
    id="ndpc_compliance_notice_2025",
    name="NDPC 1,368-firm compliance notice (Nigeria)",
    jurisdiction="Regulator-maturity benchmark",
    date_range="August 2025",
    scores={"D1": 3, "D2": 3, "D3": 3, "D4": 3, "D5": 4, "D6": 4},
    primary_sources=[
        "NDPC public notice, 25 August 2025, requiring proof of NDPA 2023 "
        "and GAID 2025 compliance from 1,368 organisations within 21 days.",
        "Hamu Legal, 'NDPC Compliance Notice: What You Need to Do'. "
        "https://hamulegal.com/ndpc-compliance-notice-nigeria-2025/",
        "Web Security Lab, 'NDPC Orders 1,300+ Firms to Prove Compliance "
        "with Nigeria's Data Protection Act'.",
        "Mondaq, 'NDPC Sets 21-Day Deadline'.",
        "GAID 2025 Article 43 (Emerging Technologies), Article 28(3) "
        "(mandatory DPIA), NDPA 2023 s. 44 (DCPMI registration).",
    ],
    rationale={
        "D1": (
            "Level 3. GAID Article 43 sets documented parameters for AI "
            "and automated processing across a sector-wide directive."
        ),
        "D2": (
            "Level 3. Requires controller registration and DPO appointment "
            "(NDPA s. 44), establishing controller identity and "
            "accountability."
        ),
        "D3": (
            "Level 3. Requires DPCO compliance audits and processor "
            "agreements; documented delegation oversight."
        ),
        "D4": (
            "Level 3. A compliance deadline (21 days) with an enforcement "
            "trigger functions as a governance stop-gate."
        ),
        "D5": (
            "Level 4. Continuous, monitored, sector-by-sector enforcement "
            "across 1,368 entities in banking, insurance, pensions, and "
            "gaming, mapped to NDPA and GAID."
        ),
        "D6": (
            "Level 4. Mandatory annual compliance-audit-return cycle filed "
            "with the Commission (GAID 2025 annual deadline); monitored, "
            "scheduled audit."
        ),
    },
    failure_signature=(
        "Regulator-maturity exemplar rather than an entity failure. The "
        "NDPC anchors the high end of the D5 and D6 scale (Managed) because "
        "it evidences continuous, scheduled, sector-wide monitored "
        "enforcement with audit cycles mapped to named anchors. It does not "
        "reach Level 5 as the notice is enforcement, not documented "
        "prospective or adaptive red-teaming."
    ),
)


# =====================================================================
# Exported case tuples
# =====================================================================
# STUB_CASES: the original three shipped with the Chapter Four artefact.
# Kept as a stable tuple so any test or reference that specifically audits
# the initial delivery continues to work.
STUB_CASES: Tuple[RetrospectiveCase, ...] = (META_WHATSAPP, APPLE_CARD, GHANA_MAHAMA)

# EXTENSION_CASES: the twelve added for Chapter Five (ten new entity cases
# plus the two regulator-maturity benchmarks), in ascending PS-score order.
EXTENSION_CASES: Tuple[RetrospectiveCase, ...] = (
    SOKOLOAN_NITDA_2021,
    NIMC_NIN_BVN,
    HK_UAE_VOICE_CLONE_2020,
    JAMB_UTME_2025,
    ARUP_DEEPFAKE_2024,
    FLUTTERWAVE_SERIES,
    INEC_IREV_2023,
    NDPC_V_FIDELITY_2024,
    NDPC_V_MULTICHOICE_2025,
    NDPC_SEVEN_FIRM_2024,
    FCCPC_DEON_2025,
    NDPC_COMPLIANCE_NOTICE_2025,
)

# ALL_CASES: the full extended sample of fifteen. This is what the runner
# and the Retrospective cases tab iterate over.
ALL_CASES: Tuple[RetrospectiveCase, ...] = STUB_CASES + EXTENSION_CASES


def get_case(case_id: str) -> RetrospectiveCase:
    for c in ALL_CASES:
        if c.id == case_id:
            return c
    raise KeyError(f"Unknown case id: {case_id}")
