# Case Coding Appendix

**Empirical per-dimension evidence tables for the fifteen retrospective
cases used to validate the Agentic AI Governance Management System.**

This appendix is the audit trail for every score in
`evaluation/cases.py`. Chapter Four of the thesis references this
document at the point of the initial three-stub delivery (Meta/WhatsApp,
Apple Card, Ghana Mahama). Chapter Five extends the sample to the full
fifteen-case set by adding twelve cases: ten new entity cases and two
regulator-maturity benchmarks (FCCPC/DEON, NDPC 1,368-firm compliance
notice). All fifteen are coded under the same rubric and coding rules,
and every score cites a primary source.

---

## Coding method

Every score in this document was derived by mapping the primary source
against the five-level maturity rubric.

**The rubric.**

| Level | Name | Descriptor |
|-------|------|------------|
| 1 | Ad hoc | No governance in this dimension. Absent controls. |
| 2 | Initial | Some policy exists but applied inconsistently, not tied to named regulatory obligations. |
| 3 | Defined | Documented controls, assigned roles, tested procedures, mapped to named regulatory anchors. |
| 4 | Managed | Controls monitored continuously, audited, drilled on schedule. |
| 5 | Optimising | Adaptive governance, prospective reviews, learning loops, red-team exercises. |

**Coding rules applied.**

1. Where a dimension was directly at issue in a primary source, the score
   reflects the documented finding.
2. Where a dimension was not directly at issue, the score reflects
   inferred maturity from the entity's overall governance posture as
   evidenced in the primary source.
3. Ties or ambiguities default to the **lower** level unless the primary
   source affirmatively documents the higher-level attribute (continuous
   monitoring, scheduled auditing, drilling, prospective review, or red
   teaming).
4. No dimension in any of the fifteen cases is scored at Level 5,
   because none of the primary sources evidenced adaptive governance,
   learning loops, or red-team exercises. Level 5 is therefore
   aspirational within the sample studied here.

---

## Case 1: Meta / WhatsApp joint NDPC-FCCPC enforcement action (Nigeria, 2024-2025)

**Score vector:** D1=2, D2=2, D3=2, D4=2, D5=3, D6=2.

**Failure signature:** documented controls defeated by enforcement
collapse. Moderate regulatory maturity (Level 3 on data-and-privacy
findings mapped to named statutory anchors) regressed when the NDPC's
$32.8 million order was set aside by a Federal High Court consent
judgment entered without affected data subjects. High D5 with depressed
D6.

**Primary sources.**

- FCCPC Final Order, WhatsApp LLC and Meta Platforms Inc., 18 July 2024.
  <https://fccpc.gov.ng/wp-content/uploads/2024/07/Final-order-FCCPC-Meta-18072024.pdf>
- Competition and Consumer Protection Tribunal ruling, 25 April 2025.
- NDPC Final Orders against Meta Platforms Inc. and WhatsApp LLC, 18 February 2025.
- Federal High Court Abuja consent judgment, Suit No. FHC/ABJ/CS/355/2025, 3 November 2025 (Hon. Justice J. K. Omotosho).
- Data Privacy Lawyers Association of Nigeria pre-action notice, 15 December 2025.

**Per-dimension coding.**

| Dim | Level | Descriptor language matched | Evidence source | Specific finding | Score |
|-----|-------|----------------------------|-----------------|------------------|-------|
| D1 | 2 (Initial) | Some policy exists but applied inconsistently | FCCPC Final Order, 18 July 2024, Orders 3-5 | Order 4 required Meta to "immediately revert to the data sharing practices adopted in 2016" and to establish an opt-in screen; scope constraints on the automated data-sharing pipeline had to be imposed by the regulator rather than by the controller. | 2 |
| D2 | 2 (Initial) | Some policy exists but applied inconsistently | NDPC Final Orders, 18 February 2025; DPLAN pre-action notice, 15 December 2025 | NDPC found Meta was "processing the data of non-users of its platforms," indicating the data-subject identity boundary was not properly bounded at scale (approximately 61 million Nigerians affected). | 2 |
| D3 | 2 (Initial) | Some policy exists but applied inconsistently | FCCPC Final Order, 18 July 2024, Order 5 | Order 5 directed Meta to "cease the tying and transfer of data from its WhatsApp market to its Facebook market, and other third parties' services without express consent"; inter-service delegation was occurring without governed oversight. | 2 |
| D4 | 2 (Initial) | Some policy exists but applied inconsistently | FCCPC Final Order, 18 July 2024, Order 1 | Order 1 required Meta to reinstate "the rights of Nigerian users to self-determine and control the use, processing, sharing or transfer of their data" and to allow withdrawal of consent "without losing functionality or deleting the application"; no proportionate human control point existed by design. | 2 |
| D5 | 3 (Defined) | Documented controls mapped to named regulatory anchors | FCCPC Final Order preamble (FCCPA ss. 17(a)(e)(l)(g)(s)(x), 33, 110, 111, 155, 157-159; NDPR Reg 2.3 consent and Reg 2.11 cross-border); NDPC $32.8m action, 18 February 2025 | Regulatory findings were mapped to named statutory anchors and produced enforceable orders on consent, cross-border transfer, and non-user data. The dimension is documented and anchored at Level 3. | 3 |
| D6 | 2 (Initial) | Some policy exists but applied inconsistently | Federal High Court consent judgment, 3 November 2025; DPLAN pre-action notice, 15 December 2025 | Documented Final Orders existed (Level 3 potential), but were vacated via a consent judgment that released Meta from claims with no affected data subjects joined. Net score reflects the accountability collapse. | 2 |

**Note on the FCCPA track.** The FCCPC's separate $220 million penalty
was upheld by the Competition and Consumer Protection Tribunal on 25
April 2025; the accountability collapse is specific to the NDPC data
protection track, not the FCCPA competition track. Chapter Five will
discuss this asymmetry.

---

## Case 2: Apple Card / Goldman Sachs algorithmic credit-decision investigation (USA, 2019-2021)

**Score vector:** D1=3, D2=3, D3=3, D4=2, D5=4, D6=3.

**Failure signature:** technically defensible model governance without
human-facing transparency. Goldman's fair-lending program reached Level 4
and NYDFS found no unlawful discrimination. The failure was concentrated
in the human-in-the-loop dimension: the credit-decision was a black box
to consumers and front-line staff, with no timely appeal path until
public pressure forced a change.

**Primary sources.**

- NYDFS Report on Apple Card Investigation, 23 March 2021.
  <https://www.dfs.ny.gov/reports_and_publications/202103_report_apple_card_investigation>
- NYDFS Press Release, DFS Issues Findings on the Apple Card and Its Underwriter Goldman Sachs Bank, 23 March 2021.
- Statements by David Heinemeier Hansson, November 2019.
- Goldman Sachs public statements on Apple Card credit methodology, November 2019.

**Per-dimension coding.**

| Dim | Level | Descriptor language matched | Evidence source | Specific finding | Score |
|-----|-------|----------------------------|-----------------|------------------|-------|
| D1 | 3 (Defined) | Documented controls mapped to named regulatory anchors | NYDFS Report, March 2021, section III(a) | NYDFS found "the Bank had a fair lending program in place for ensuring its lending policy, and underlying statistical model, did not consider prohibited characteristics of applicants and would not produce disparate impacts." The model's decision authority was bounded by policy. | 3 |
| D2 | 3 (Defined) | Documented controls mapped to named regulatory anchors | NYDFS Report, March 2021, sections II(b), III | Goldman Sachs Bank USA, "a New York State-chartered bank," was the identified accountable underwriter operating under ECOA and NY Exec. Law s. 296-a; identity of the acting party was clear and regulated. (Individual applicant authentication was not at issue.) | 3 |
| D3 | 3 (Defined) | Documented controls, assigned roles | NYDFS Report, March 2021, section II(b) | Although Apple Card was marketed as "created by Apple, not a bank," NYDFS confirmed "Goldman Sachs was responsible for the Apple Card credit policy and underwriting decisions as well as the management of the Apple Card program"; the Apple to Goldman delegation was allocated to the regulated bank. | 3 |
| D4 | 2 (Initial) | Some policy exists but applied inconsistently | NYDFS Report, March 2021, section IV(b)(1) "Lack of Transparency" | Consumers perceived a "black box"; a customer-service agent "could not explain these algorithms or the basis for the difference in credit limits." The six-month waiting period before appealing terms meant no timely human override existed by design; the Bank only "eliminated the six-month waiting period for appeals" reactively "after media scrutiny in November 2019." | 2 |
| D5 | 4 (Managed) | Controls monitored continuously, audited, drilled on schedule | NYDFS Report, March 2021, section III(a); NYDFS press release, 23 March 2021; Goldman statement, November 2019 | NYDFS's Consumer Examinations Unit, which "regularly conducts fair lending exams of all New York state-chartered banks," used regression analysis on "approximately 400,000 New York State applicants for the Apple Card" and "did not produce evidence of unlawful discrimination against applicants under fair lending law." The Bank ran a documented, third-party-reviewed fair-lending program. | 4 |
| D6 | 3 (Defined) | Documented controls, assigned roles, tested procedures | NYDFS Report, March 2021, section III(a) | "At the Department's request, the Bank also explained its Apple Card credit decisions for individuals who sent discrimination complaints. In each instance, the Bank was able to identify the factors that led to the credit decisions, such as credit score, indebtedness, income, credit utilization, missed payments," demonstrating retained auditable decision records and a named accountable owner. | 3 |

**Note.** The Level 4 score on D5 reflects governance process maturity
(testing, auditing, third-party review), not a normative judgment that
the outcome was fair. NYDFS itself flagged systemic credit-scoring bias
as a residual concern.

---

## Case 3: Ghana Mahama deepfake case (Ghana, March to May 2026)

**Score vector:** D1=1, D2=1, D3=1, D4=1, D5=1, D6=2.

**Failure signature:** no preventive governance with reactive criminal
accountability. Because the system is an adversarial criminal pipeline
rather than a governed enterprise, five of the six dimensions sit at
Level 1. The single dimension that rises is D6, and only reactively,
through arrests. A governance vacuum with an ex-post criminal response.

**Primary sources.**

- Ghana Police Service / Cyber Vetting and Enforcement Team (CVET) statement on 11 arrests, 7 May 2026.
- Ghana News Agency, "Eleven arrested for allegedly impersonating President John Mahama," 8 May 2026.
  <https://gna.org.gh/2026/05/eleven-arrested-for-allegedly-impersonating-president-john-mahama/>
- Ghana Cyber Security Authority statements on deepfake takedown workflow, 29 September 2025 (via GhanaFact).
- Ghana Data Protection Act 2012, Act 843.
- Cybersecurity Act 2020, Act 1038.

**Per-dimension coding.**

| Dim | Level | Descriptor language matched | Evidence source | Specific finding | Score |
|-----|-------|----------------------------|-----------------|------------------|-------|
| D1 | 1 (Ad hoc) | No governance in this dimension | Ghana Police / CVET statement, 7 May 2026 | Per the situational report, "the suspects used AI-generated content to fraudulently solicit money and sensitive personal information from unsuspecting members of the public through online platforms." No tool allow-list, scope constraint, or action logging existed; no source identified the specific generation model or app used. | 1 |
| D2 | 1 (Ad hoc) | No governance in this dimension | CVET statement, 7 May 2026 (exhibits list) | The fraud is an identity-authentication failure by definition: the deepfake impersonated a verified public figure with no platform identity verification preventing propagation. Exhibits included "120 pre-registered SIM cards" indicating deliberate identity obfuscation. | 1 |
| D3 | 1 (Ad hoc) | No governance in this dimension | Ghana CSA statement, 29 September 2025; police briefing, 30 March 2026 | Distribution ran across Facebook (primary), TikTok, and WhatsApp with no governed oversight; no automated platform detection or delegation control prevented the cross-platform spread. | 1 |
| D4 | 1 (Ad hoc) | No governance in this dimension | Ghana CSA statement, 29 September 2025; CSA remarks via GhanaFact, 4 August 2025 | No preventive human checkpoint or kill-switch existed on distribution channels; takedown was manual and reactive: "we've taken down multiple accounts, but sometimes you take one down and a new one pops up the next morning." | 1 |
| D5 | 1 (Ad hoc) | No governance in this dimension | Ghana Data Protection Act 2012 (Act 843); DataGuidance GDPR vs. Ghana comparison | Misuse of Mahama's likeness and voice occurred with no lawful basis or consent; Act 843 "does not explicitly refer to DPIA," so no data-protection framework applied to the misuse context. | 1 |
| D6 | 2 (Initial) | Some policy exists but applied inconsistently | Ghana Police / CVET statement, 7 May 2026; Ghana News Agency, 8 May 2026 | Accountability exists ex post via criminal enforcement only: 11 arrested; nine remanded to reappear on 25 May 2026; two granted bail. Media referenced the Cybersecurity Act 2020 in general, but no specific charge sections were itemised in the sources available, so Level 2 rather than 3. | 2 |

---

## Case 4: Sokoloan / Soko Lending Company NITDA sanction (Nigeria, August 2021)

**Score vector:** D1=1, D2=2, D3=1, D4=1, D5=2, D6=1.
**Weighted totals:** Public Sector 1.35, Large Enterprise 1.35. Maturity level: Ad hoc.

**Failure signature:** data-privacy and oversight dominated failure with a
strong automation-abuse element. Near-uniform Level 1 across D1, D3, D4,
and D6 reflects an entity with essentially no governance, weaponising
automated data-harvesting and messaging. The NITDA order (mandatory DPIA,
nine-month oversight) is the corrective, not a pre-existing control.

**Primary sources.**

- NITDA, "NITDA Sanctions SokoLoan for Privacy Invasion" (Hadiza Umar), August 2021. <https://nitda.gov.ng/nitda-sanctions-soko-loan-for-privacy-invasion/>
- Nairametrics, 19 August 2021.
- TechCabal, 24 August 2021.
- NDPR 2019, Articles 2.2, 2.3, 2.5, 3.1(7), 4.1(7); NDPR Implementation Framework Art 3.1(1).

**Evidence table.**

| Dim | Level | Descriptor matched | Finding | Score |
|---|---|---|---|---|
| D1 | Ad hoc | No governance | App auto-harvested contacts and triggered debt-shaming messages with no controls. | 1 |
| D2 | Initial | Not directly at issue | Inferred; loans disbursed on app data. | 2 |
| D3 | Ad hoc | Trackers shared data with third parties | Embedded trackers shared customer data with undisclosed third parties. | 1 |
| D4 | Ad hoc | No stop control on automated messaging | Automated privacy-invading messages sent with no human gate; NITDA had to order a stop. | 1 |
| D5 | Initial | Some policy, not tied to anchors | Privacy notice existed but was non-conforming (NDPR Arts 2.2, 2.3, 2.5) with insufficient lawful basis. | 2 |
| D6 | Ad hoc | Non-filing of audit reports | NDPR Art 4.1(7) audit filing missed; refused cooperation with the DPA. | 1 |

**Coding confidence.** D2 scored on inferred posture. All other dimensions documented.

---

## Case 5: NIMC NIN/BVN black-market breaches (Nigeria, 2024-2026)

**Score vector:** D1=1, D2=1, D3=1, D4=2, D5=2, D6=1.
**Weighted totals:** Public Sector 1.40, Large Enterprise 1.30. Maturity level: Ad hoc.

**Failure signature:** identity-authentication and accountability dominated
public-sector failure. A near-uniform Level 1 vector: the compromise is
precisely in D2 and D3 (licensed-partner access resold with no oversight)
at the heart of the national identity system, with D6 undermined by
institutional denial. The single Level 2 (D4) reflects only reactive,
journalist-triggered takedowns.

**Primary sources.**

- Foundation for Investigative Journalism (FIJ), Investigation series on NIMC licensed front-end partners and the NIN/BVN black market, 2024-2025. <https://fij.ng/>
- FIJ, "After FIJ's Story, Website Selling BVNs, NINs Goes Dark" (NIMC denial).
- FIJ, "New NIMC Act Promises Data Privacy, Yet It Excludes Nigeria's Data Protection Regulator From Board".
- Paradigm Initiative statements, 2024-2025.
- Biometric Update, August 2025.
- NIMC Act 2007 ss. 28-30 (unlawful access, up to 10 years or N10m).

**Evidence table.**

| Dim | Level | Descriptor matched | Finding | Score |
|---|---|---|---|---|
| D1 | Ad hoc | No control over API/tool access | API keys enabling verification and modification resold to unauthorised parties. | 1 |
| D2 | Ad hoc | Licensed-partner access uncontrolled | FEP credentials sub-leased with no binding of access to authorised identities. | 1 |
| D3 | Ad hoc | Delegated partner oversight absent | Licensed FEPs sub-leasing access "while regulators look away". | 1 |
| D4 | Initial | Reactive takedowns only | Takedowns occurred only after journalist exposure; no proactive halt. | 2 |
| D5 | Initial | Policy exists, weak enforcement | Statutory protections exist (NIMC Act s. 30) but not enforced against the ecosystem. | 2 |
| D6 | Ad hoc | Denial, no outcome | FIJ recorded "no outcome in 3 major cases"; NIMC denial without documented governance. | 1 |

**Coding confidence.** All dimensions documented via investigative reporting and NIMC statement. NIMC's denial is a contested finding; the coding takes the documented ecosystem failure at face value.

---

## Case 6: Hong Kong / UAE bank voice-clone fraud (Early 2020, reported October 2021)

**Score vector:** D1=2, D2=1, D3=1, D4=1, D5=2, D6=2.
**Weighted totals:** Public Sector 1.50, Large Enterprise 1.50. Maturity level: Initial.

**Failure signature:** identity-authentication dominated failure and the
audio-only precursor to the Arup video-conference fraud. Total D2 collapse
(voice-as-identity) combined with Level 1 D3 and D4 (single actor, no
delegation oversight, no kill-switch) produced the USD 35 million loss.
D6 is marginally above ad hoc only because transaction logs later
supported cross-border tracing of USD 400,000.

**Primary sources.**

- Forbes, Thomas Brewster, "Fraudsters Cloned Company Director's Voice In $35 Million Heist", 14 October 2021. <https://www.forbes.com/sites/thomasbrewster/2021/10/14/huge-bank-fraud-uses-deep-fake-voice-tech-to-steal-millions/>
- AI Incident Database, Incident 147. <https://incidentdatabase.ai/cite/147/>
- US court filing referenced in Forbes coverage (case documents not publicly indexed).

**Evidence table.**

| Dim | Level | Descriptor matched | Finding | Score |
|---|---|---|---|---|
| D1 | Initial | Some policy, inconsistent | Transfer authority exercised on voice plus email confirmation, no independent verification for USD 35m. | 2 |
| D2 | Ad hoc | No identity authentication | Voice recognition treated as authentication; "deep voice" clone defeated the only identity check. | 1 |
| D3 | Ad hoc | No oversight of instruction chain | Director-to-lawyer-to-manager chain accepted at face value with no verification. | 1 |
| D4 | Ad hoc | Human present but no stop control | Manager acted alone; funds dispersed globally before any control triggered. | 1 |
| D5 | Initial | Not directly at issue | Data breach not the issue; inferred low baseline given absence of verification infrastructure. | 2 |
| D6 | Initial | Some logging enabled cross-border tracing | Transaction trail existed sufficient for post-hoc tracing of USD 400,000, but no proactive audit detected the fraud. | 2 |

**Coding confidence.** D5 scored on inferred posture. The case relies on secondary reporting of a US court filing; no published judgment was located.

---

## Case 7: JAMB 2025 UTME technical failure (Nigeria, May 2025)

**Score vector:** D1=2, D2=2, D3=1, D4=1, D5=2, D6=3.
**Weighted totals:** Public Sector 1.80, Large Enterprise 1.85. Maturity level: Initial.

**Failure signature:** algorithmic decision and oversight dominated
public-sector failure. Total D3 and D4 collapse (no synchronisation
oversight of delegated providers, no human check before releasing
life-altering automated scores affecting 379,997 candidates), with the
anomaly detected only externally. D6 reaches Defined on the strength of
the post-hoc independent audit and candid public accountability. This
case most directly evidences the governance gap the maturity model
targets.

**Primary sources.**

- TechCabal, "Inside the server glitch behind JAMB's scrambled UTME score", 16 May 2025. <https://techcabal.com/2025/05/16/inside-the-server-glitch-behind-jambs-scrambled-utme-score/>
- TheCable, "JAMB admits to error in 2025 UTME", 14 May 2025. <https://www.thecable.ng/breaking-jamb-admits-to-error-in-2025-utme-orders-resit-for-387000-candidates/>
- TheCable, "Man narrates how daughter committed suicide over subpar 2025 UTME score". <https://www.thecable.ng/man-narrates-how-daughter-committed-suicide-over-subpar-2025-utme-score/>
- Punch, "UTME resit: JAMB to release results of 379,000 candidates".
- JAMB press briefing by Registrar Prof. Ishaq Oloyede, 14 May 2025.

**Evidence table.**

| Dim | Level | Descriptor matched | Finding | Score |
|---|---|---|---|---|
| D1 | Initial | Some policy, inconsistent | New scoring/patch tools deployed; patch not applied uniformly. "The real failure was in system discipline." | 2 |
| D2 | Initial | Not directly at issue | Candidate authentication not the failure point. | 2 |
| D3 | Ad hoc | Failed oversight of two providers | Delegation to service providers with no synchronisation oversight; South-East had no dedicated server cluster. | 1 |
| D4 | Ad hoc | No detection/stop before release | No human check caught the mass anomaly; results released; error detected externally by Educare. | 1 |
| D5 | Initial | Not directly at issue | Result-data integrity, not personal data protection, was the issue. Inferred. | 2 |
| D6 | Defined | Post-hoc audit, public admission | Independent psychometric audit engaged; Registrar accepted personal responsibility publicly. | 3 |

**Coding confidence.** D2 and D5 scored on inferred posture. D1, D3, D4, D6 documented.

---

## Case 8: Arup deepfake video conference fraud (Hong Kong, January-May 2024)

**Score vector:** D1=2, D2=1, D3=1, D4=2, D5=2, D6=3.
**Weighted totals:** Public Sector 1.85, Large Enterprise 1.80. Maturity level: Initial.

**Failure signature:** identity-authentication and human-in-the-loop
dominated failure. Catastrophic collapse of D2 (no way to prove who was
on the call) compounded by weak D1 and D3 transaction controls that let
a single employee execute fifteen high-value transfers on a deepfaked
instruction. D6 is relatively strong because of prompt reporting and
public post-incident learning, but does not reach Level 5 as no
pre-incident red-teaming or adaptive controls were documented.

**Primary sources.**

- CNN, "Arup revealed as victim of $25 million deepfake scam", 16 May 2024. <https://www.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk>
- South China Morning Post, 17 May 2024.
- World Economic Forum, "Cybercrime: Lessons learned from a $25m deepfake attack" (Rob Greig, CIO), February 2025. <https://www.weforum.org/stories/2025/02/deepfake-ai-cybercrime-arup/>
- AI Incident Database, Incident 634. <https://incidentdatabase.ai/cite/634/>
- Hong Kong Police Force briefing (Acting Senior Superintendent Baron Chan Shun-ching), 17 May 2024.

**Evidence table.**

| Dim | Level | Descriptor matched | Finding | Score |
|---|---|---|---|---|
| D1 | Initial | Some policy, inconsistently applied | Fifteen transfers of HKD 200m executed on video call, no independent transaction verification gating high-value payments. | 2 |
| D2 | Ad hoc | No verification of participants | No mechanism to authenticate call participants; deepfakes from public video/audio went undetected. | 1 |
| D3 | Ad hoc | No oversight of delegated instruction | Single employee acted on "confidential transaction" delegation with no secondary approver until after funds sent. | 1 |
| D4 | Initial | Human in loop but no stop control | Employee initially suspicious but no verification protocol halted the fifteen transactions over a week. | 2 |
| D5 | Initial | Some policy, not tied to a named finding | No data breach at issue (Arup: "none of our internal systems were compromised"); inferred baseline. | 2 |
| D6 | Defined | Documented controls, reporting, post-incident learning | Prompt police report, full cooperation, public post-incident review by CIO at WEF. | 3 |

**Coding confidence.** D5 scored on inferred posture. D1, D3, D4, D6 documented.

---

## Case 9: Flutterwave security incident series (Nigeria, 2023-2024)

**Score vector:** D1=2, D2=2, D3=2, D4=2, D5=2, D6=2.
**Weighted totals:** Public Sector 2.00, Large Enterprise 2.00. Maturity level: Initial.

**Failure signature:** control-monitoring and delegation dominated
enterprise fintech failure. A flat Level 2 vector reflects an entity with
policies and some detection (the N19 billion cut-off) but no continuous,
audited, drilled controls, as evidenced by four recurrences in about
fourteen months and reliance on a court order rather than internal
kill-switches for recovery.

**Primary sources.**

- TechCabal, "Flutterwave begins recovery of $24 million", 8 February 2024. <https://techcabal.com/2024/02/08/flutterwave-to-recover-missing-24million/>
- TechCabal, "Flutterwave loses N11 billion in security breach", 16 May 2024. <https://techcabal.com/2024/05/16/exclusive-flutterwave-loses-%E2%82%A611-billion-in-security-breach/>
- Techpoint Africa, "A fatal error by NIBSS worsened Flutterwave's N21 billion glitch". <https://techpoint.africa/insight/a-fatal-error-by-nibss-worsened-flutterwaves-%E2%82%A621-billion-glitch/>
- Federal High Court Lagos Mareva injunction, 1 February 2024.

**Evidence table.**

| Dim | Level | Descriptor matched | Finding | Score |
|---|---|---|---|---|
| D1 | Initial | Some policy, inconsistent | POS merchants "abused their access"; settlement-limit misconfiguration unreverted for three months. | 2 |
| D2 | Initial | KYC gaps at receiving institutions | Recovery hampered by weak KYC/customer verification at neobanks. | 2 |
| D3 | Initial | Cross-institution oversight failure | Failure spanned Flutterwave, POS merchants, NIBSS and 35 institutions with no effective inter-party monitoring. | 2 |
| D4 | Initial | Detection after the fact | Settlement-limit tool cut off at N19bn only after exposure; suspensions applied reactively. | 2 |
| D5 | Initial | Not directly at issue | Financial-controls failure, not data-privacy. Inferred. | 2 |
| D6 | Initial | Repeated recurrence | Four incidents in about fourteen months indicates audit/monitoring not embedded; recovery via court, not internal control. | 2 |

**Coding confidence.** D5 scored on inferred posture. Case relies on investigative reporting and court filings, not a published final judgment on liability.

---

## Case 10: INEC IReV 2023 presidential election failure (Nigeria, 25 February 2023)

**Score vector:** D1=2, D2=2, D3=2, D4=2, D5=2, D6=3.
**Weighted totals:** Public Sector 2.15, Large Enterprise 2.15. Maturity level: Initial.

**Failure signature:** algorithmic and system-availability dominated
public-sector failure. A D1/D3/D4 configuration and contingency failure
on the single most consequential upload path, with the flagship result
stream failing while parallel streams succeeded. D6 reaches Defined on
the strength of the detailed published post-mortem and documented
resilience improvements, though these were remedial rather than
prospective.

**Primary sources.**

- INEC, Report on the conduct of the 2023 general elections, 526-page post-mortem, February 2024.
- Premium Times, "INEC gives details of IReV failure". <https://www.premiumtimesng.com/news/top-news/671063>
- BusinessDay, "INEC finally reveals why IReV failed in 2023 presidential poll". <https://businessday.ng/news/article/inec-finally-reveals-why-irev-failed-in-2023-presidential-poll/>
- TheCable, "HTTP server error: INEC finally opens up on IReV failure during presidential poll".

**Evidence table.**

| Dim | Level | Descriptor matched | Finding | Score |
|---|---|---|---|---|
| D1 | Initial | Some policy, inconsistent | Configuration bug in upload tool went undetected; controls inconsistent across result types. | 2 |
| D2 | Initial | Not directly at issue | BVAS accreditation functioned; inferred moderate. | 2 |
| D3 | Initial | Partial: NASS uploads worked | NASS results uploaded, presidential did not; configuration/mapping fault in a differentiated pipeline. | 2 |
| D4 | Initial | Reactive hotfix, no contingency | Problem reported 4pm, partially resolved in four hours via hotfixes; no pre-tested failover for the flagship poll. | 2 |
| D5 | Initial | Not directly at issue | Not a data-privacy failure; election-data integrity/availability. Inferred. | 2 |
| D6 | Defined | Detailed public post-mortem | 526-page report with root cause and remediation ("additional QA checks", "end-to-end testing"); Supreme Court remarks on public confidence. | 3 |

**Coding confidence.** D2 and D5 scored on inferred posture. D1, D3, D4, D6 documented from the official post-mortem.

---

## Case 11: NDPC v. Fidelity Bank (Nigeria, August 2024)

**Score vector:** D1=2, D2=2, D3=2, D4=2, D5=3, D6=2.
**Weighted totals:** Public Sector 2.20, Large Enterprise 2.15. Maturity level: Initial.

**Failure signature:** data-privacy dominated failure. D5 is the crux
(documented NDPA/NDPR consent breach), aggravated by D3 (processor
non-compliance) and D6 (poor accountability during the probe). The bank
had policies (Level 2-3 on paper) but no tested, mapped controls, and
its dispute of the finding underscores an immature accountability
culture.

**Primary sources.**

- NDPC Final Order against Fidelity Bank Plc, 21 August 2024, statement by Babatunde Bamigboye, Head of Legal, Enforcement and Regulations.
- Premium Times, "Nigerian govt fines Fidelity Bank N555.8 million", 21 August 2024. <https://www.premiumtimesng.com/business/business-news/726713>
- TechCabal, 21 August 2024.
- BusinessDay, "NDPC fines Fidelity Bank N555.8 million over data privacy violations".

**Evidence table.**

| Dim | Level | Descriptor matched | Finding | Score |
|---|---|---|---|---|
| D1 | Initial | Some policy, inconsistent | Automated data-collection tools (cookies, banking app over 1m downloads) deployed without lawful basis. | 2 |
| D2 | Initial | Not directly at issue | Inferred from posture; account opened on data without proper consent implies weak identity controls. | 2 |
| D3 | Initial | Vendor oversight failure | Reliance on "non-compliant third-party data processors" is a failed delegation oversight. | 2 |
| D4 | Initial | Not directly at issue | Inferred; no evidence of consent-withdrawal or stop mechanisms. | 2 |
| D5 | Defined | Documented, mapped to named anchors | Documented breach of NDPA 2023 and NDPR 2019 processing-without-consent provisions. | 3 |
| D6 | Initial | Poor accountability during probe | Bank failed to provide accountability over 10+ correspondences; penalty aggravated for non-cooperation. | 2 |

**Coding confidence.** D2 and D4 scored on inferred posture. D1, D3, D5, D6 documented.

---

## Case 12: NDPC v. MultiChoice Nigeria (July 2025)

**Score vector:** D1=2, D2=2, D3=2, D4=2, D5=3, D6=2.
**Weighted totals:** Public Sector 2.20, Large Enterprise 2.15. Maturity level: Initial.

**Failure signature:** data-privacy dominated failure centred on unlawful
cross-border data flows (D5 and D3). The extension of processing to
non-subscribers and the "unsatisfactory" remediation give a D6 weakness.
The vector closely mirrors Fidelity, marking a consistent NDPC
enforcement pattern against large enterprises.

**Primary sources.**

- NDPC statement (Babatunde Bamigboye), 6 July 2025.
- Punch, "NDPC fines MultiChoice N766m", 7 July 2025. <https://punchng.com/ndpc-fines-multichoice-%E2%82%A6766m-for-data-privacy-violations/>
- Vanguard, 7 July 2025.
- The ICIR, "NDPC fines MultiChoice Nigeria N766 million over data privacy violations".
- Section 37, 1999 Constitution of the Federal Republic of Nigeria; NDPA 2023 s. 41.

**Evidence table.**

| Dim | Level | Descriptor matched | Finding | Score |
|---|---|---|---|---|
| D1 | Initial | Some policy, inconsistent | Data-collection deemed "patently intrusive, unfair, unnecessary and disproportionate"; tool governance weak. | 2 |
| D2 | Initial | Not directly at issue | Inferred; processing extended to non-subscribers implies weak subject-identity boundaries. | 2 |
| D3 | Initial | Cross-border transfer without safeguards | Illegal cross-border transfer without adequacy/BCR/SCC safeguards is a failed delegation to foreign processors. | 2 |
| D4 | Initial | Not directly at issue | Inferred low posture. | 2 |
| D5 | Defined | Documented, mapped to named anchors | Documented finding of illegal cross-border transfer and privacy violation (NDPA s. 41; s. 37 Constitution). | 3 |
| D6 | Initial | Non-cooperation | Remedial measures "unsatisfactory"; "want of cooperation" recorded. | 2 |

**Coding confidence.** D2 and D4 scored on inferred posture. D1, D3, D5, D6 documented.

---

## Case 13: NDPC seven-firm N400m enforcement action (Nigeria, June 2024)

**Score vector:** D1=2, D2=2, D3=2, D4=2, D5=3, D6=3.
**Weighted totals:** Public Sector 2.35, Large Enterprise 2.30. Maturity level: Initial.

**Failure signature:** data-privacy dominated aggregate enforcement case.
The entity-side vector is a modest Level 2 with D5 and D6 at Defined,
reflecting the documented, mapped remediation of seven firms. It
corroborates the NDPC's escalating enforcement posture that culminates
in the Fidelity, MultiChoice, and 1,368-firm actions.

**Primary sources.**

- NDPC public statement by Vincent Olatunji, National Commissioner, 11 June 2024.
- TheCable, "NDPC fines four banks, three companies N400m for data violation". <https://www.thecable.ng/ndpc-fines-four-banks-three-companies-n400m-for-data-violation/>
- Nairametrics, "Seven firms pay N400 million to NDPC as sanction for data breach", 12 June 2024. <https://nairametrics.com/2024/06/12/seven-firms-pay-n400-million-to-ndpc-as-sanction-for-data-breach/>
- Techpoint Africa, "NDPC gets N400 million in fines from 7 companies for data breaches". <https://techpoint.africa/news/ndpc-gets-fines-companies-data-breaches/>

**Evidence table.**

| Dim | Level | Descriptor matched | Finding | Score |
|---|---|---|---|---|
| D1 | Initial | Aggregate, entity-level low | Underlying entities showed inconsistent processing controls. | 2 |
| D2 | Initial | Not detailed | Inferred; not itemised per firm. | 2 |
| D3 | Initial | Vendor/processor breaches implied | Breaches across sectors imply processor/delegation weaknesses. | 2 |
| D4 | Initial | Not detailed | Inferred low. | 2 |
| D5 | Defined | Documented, mapped, seven resolved | Seven documented resolutions with remediation under NDPA (s. 48); enforcement mapped to the Act. | 3 |
| D6 | Defined | Monitored programme | Regulator-driven accountability across 1,000+ investigations; entities paid remediation. | 3 |

**Coding confidence.** D2 and D4 scored on inferred aggregate posture. Firms not individually named, so entity-level scores are group inferences. D5 and D6 documented.

---

## Case 14: FCCPC digital lending / DEON Regulations 2025 (Nigeria, 2022-2026) — REGULATOR BENCHMARK

**Score vector:** D1=3, D2=2, D3=3, D4=3, D5=3, D6=4.
**Weighted totals:** Public Sector 3.00, Large Enterprise 2.95. Maturity level: Defined.

**Coded as a regulator-maturity benchmark, not an entity failure.**

**Failure signature:** this is a regulator-maturity case rather than an
entity failure, and it reads as the inverse of the loan-app cases it
targets (Case 4). The FCCPC regime scores Defined-to-Managed because
controls are documented, role-assigned, mapped to the FCCPA and NDPA,
court-tested and continuously enforced (D6 Managed). It does not reach
Level 5 as no prospective/red-team adaptive governance is documented,
only reactive-then-sustained enforcement.

**Primary sources.**

- Sahara Reporters, 12 March 2022 (initial raids on GoCash, OKash, EasyCredit, Kashkash, Speedy Choice, Easy Moni, Sokoloan).
- TechCabal, 12 March 2022.
- FCCPC, "FCCPC Resumes Digital Lending Regulation", 20 July 2026. <https://fccpc.gov.ng/fccpc-resumes-digital-lending-regulation/>
- Federal High Court Lagos judgment, Suit No. FHC/L/CS/760/2026, 20 July 2026 (Hon. Justice A. L. Allagoa), upholding DEON Regulations 2025 as intra vires.
- TheCable, "FCCPC resumes enforcement as court upholds digital lending regulations".

**Evidence table.**

| Dim | Level | Descriptor matched | Finding | Score |
|---|---|---|---|---|
| D1 | Defined | Documented regime, roles, anchors | DEON creates documented controls over lending tools/data access mapped to the FCCPA 2018. | 3 |
| D2 | Initial | Registration requirement (new) | Operator registration required but only newly enforced; industry compliance nascent. | 2 |
| D3 | Defined | Multi-agency enforcement | Coordinated FCCPC/ICPC/NITDA/NPF oversight; documented and role-assigned. | 3 |
| D4 | Defined | App takedowns, account freezes | FCCPC executed kill-switch equivalents (app-store removals, frozen accounts) with court warrants. | 3 |
| D5 | Defined | Documented, mapped, tested in court | DEON data-protection provisions upheld as intra vires. | 3 |
| D6 | Managed | Enforcement monitored, litigated, resumed | Monitored enforcement with compliance deadlines (5 Jan 2026), suspension and court-tested resumption. | 4 |

**Coding confidence.** All dimensions documented. Scores reflect the regulator's governance posture, coded as an enforcement/governance exemplar per coding rule 2.

---

## Case 15: NDPC 1,368-firm compliance notice (Nigeria, August 2025) — REGULATOR BENCHMARK

**Score vector:** D1=3, D2=3, D3=3, D4=3, D5=4, D6=4.
**Weighted totals:** Public Sector 3.35, Large Enterprise 3.30. Maturity level: Defined.

**Coded as a regulator-maturity benchmark, not an entity failure.**

**Failure signature:** like Case 14, a regulator-maturity exemplar, not an
entity failure. It anchors the high end of the D5 and D6 scale (Managed)
because it evidences continuous, scheduled, sector-wide monitored
enforcement with audit cycles mapped to named anchors. It does not reach
Level 5 as the notice is enforcement, not documented prospective or
adaptive red-teaming.

**Primary sources.**

- NDPC public notice, 25 August 2025, requiring proof of NDPA 2023 and GAID 2025 compliance from 1,368 organisations within 21 days.
- Hamu Legal, "NDPC Compliance Notice: What You Need to Do". <https://hamulegal.com/ndpc-compliance-notice-nigeria-2025/>
- Web Security Lab, "NDPC Orders 1,300+ Firms to Prove Compliance with Nigeria's Data Protection Act". <https://websecuritylab.org/ndpc-orders-1300-firms-to-prove-compliance-with-nigerias-data-protection-act/>
- Mondaq, "NDPC Sets 21-Day Deadline". <https://www.mondaq.com/nigeria/data-protection/1675960>
- NDPC / GAID 2025 official PDF. <https://ndpc.gov.ng/wp-content/uploads/2025/07/NDP-ACT-GAID-2025-MARCH-20TH.pdf>
- NDPA 2023 s. 44 (DCPMI registration); GAID 2025 Art 18(1)(f), Art 28(3), Art 43.

**Evidence table.**

| Dim | Level | Descriptor matched | Finding | Score |
|---|---|---|---|---|
| D1 | Defined | Documented directive, roles | GAID Art 43 sets documented parameters for AI/automated processing; sector-wide directive. | 3 |
| D2 | Defined | Registration of controllers | Requires registration and DPO appointment (NDPA s. 44); identity/accountability of controllers. | 3 |
| D3 | Defined | Processor/vendor obligations | Requires DPCO compliance audits and processor agreements; documented delegation oversight. | 3 |
| D4 | Defined | Directive with deadline/sanction | 21-day compliance deadline with enforcement trigger functions as governance stop-gate. | 3 |
| D5 | Managed | Monitored, sector-by-sector enforcement | Continuous, monitored, sector-wide enforcement across 1,368 entities mapped to NDPA/GAID. | 4 |
| D6 | Managed | Annual CAR audit cycle | Mandatory annual compliance-audit-return cycle filed with the Commission. | 4 |

**Coding confidence.** Coded as a governance/enforcement exemplar per coding rule 2. All dimensions documented.

---

## Cross-case synthesis

The fifteen cases occupy a wide swath of the maturity space rather than
clustering at a single point, which is what a governance rubric needs to
demonstrate. The primary sample of thirteen entity cases spans from
Ghana Mahama at 1.15 (Ad hoc) to Apple Card at 3.00 (Defined), a range
of 1.85 points on the four-point scale. The two regulator benchmarks
sit above the primary sample and anchor the top of the scale at
approximately 3.0 to 3.35 (Defined).

**Score vectors for all fifteen cases** (ordered by ascending Public
Sector score within each panel).

*Primary sample — thirteen entity cases:*

| Case | D1 | D2 | D3 | D4 | D5 | D6 | PS | LE |
|------|----|----|----|----|----|----|----|----|
| Ghana Mahama deepfake | 1 | 1 | 1 | 1 | 1 | 2 | 1.15 | 1.15 |
| Sokoloan / NITDA (2021) | 1 | 2 | 1 | 1 | 2 | 1 | 1.35 | 1.35 |
| NIMC NIN/BVN | 1 | 1 | 1 | 2 | 2 | 1 | 1.40 | 1.30 |
| HK/UAE voice-clone | 2 | 1 | 1 | 1 | 2 | 2 | 1.50 | 1.50 |
| JAMB 2025 UTME | 2 | 2 | 1 | 1 | 2 | 3 | 1.80 | 1.85 |
| Arup deepfake | 2 | 1 | 1 | 2 | 2 | 3 | 1.85 | 1.80 |
| Flutterwave series | 2 | 2 | 2 | 2 | 2 | 2 | 2.00 | 2.00 |
| INEC IReV 2023 | 2 | 2 | 2 | 2 | 2 | 3 | 2.15 | 2.15 |
| Meta / WhatsApp NDPC | 2 | 2 | 2 | 2 | 3 | 2 | 2.20 | 2.15 |
| NDPC v. Fidelity | 2 | 2 | 2 | 2 | 3 | 2 | 2.20 | 2.15 |
| NDPC v. MultiChoice | 2 | 2 | 2 | 2 | 3 | 2 | 2.20 | 2.15 |
| NDPC seven-firm agg. | 2 | 2 | 2 | 2 | 3 | 3 | 2.35 | 2.30 |
| Apple Card / Goldman | 3 | 3 | 3 | 2 | 4 | 3 | 3.00 | 3.00 |

*Regulator-maturity benchmark panel — two cases:*

| Case | D1 | D2 | D3 | D4 | D5 | D6 | PS | LE |
|------|----|----|----|----|----|----|----|----|
| FCCPC / DEON Regulations | 3 | 2 | 3 | 3 | 3 | 4 | 3.00 | 2.95 |
| NDPC 1,368-firm notice | 3 | 3 | 3 | 3 | 4 | 4 | 3.35 | 3.30 |

**Four failure signatures emerge across the primary sample.**

- **Data-privacy dominated** (Meta/WhatsApp, NDPC v. Fidelity, NDPC v.
  MultiChoice, NDPC seven-firm, Sokoloan). Signature: D5 at Defined on
  a statute-anchored regulator finding while D1-D4 sit at Initial or
  below. Diagnostic marker for an entity that has engaged with data-
  protection compliance on paper but has not built the wider
  governance envelope.
- **Identity-authentication dominated** (Ghana Mahama deepfake, Arup
  deepfake, HK/UAE voice-clone, NIMC NIN/BVN). Signature: D2 at Level
  1 as the crux, with D3 collapse where a delegated instruction chain
  is accepted at face value. Diagnostic marker for synthetic-identity
  attacks or licensed-credential resale defeating human or institutional
  authentication.
- **Algorithmic decision and system-availability dominated** (JAMB 2025
  UTME, INEC IReV 2023). Signature: D3 and D4 at Level 1 with D6 rising
  to Defined only on the strength of a post-hoc public post-mortem.
  Diagnostic marker for public-sector automated pipelines producing
  consequential outputs without pre-release human review, detected
  externally or after the fact.
- **Control-monitoring and delegation dominated** (Flutterwave series).
  Signature: a flat Level 2 vector with recurrence signalling absent
  continuous monitoring. Diagnostic marker for enterprise entities with
  policies and some detection but no drilled, audited controls.

**Two regulator-maturity exemplars** (FCCPC/DEON, NDPC 1,368-firm
notice) sit in a separate benchmark panel because they score regulators
rather than institutions. They anchor the top of the maturity scale
(D6 at Managed on both), demonstrating that the rubric distinguishes
Defined from Managed at the higher levels even though no primary-sample
entity reaches those levels.

The fifteen cases produce numerically separable profiles under both
variants, and the ranking is stable across variants with only marginal
shifts at the edges (largest gap: NIMC at 0.10 between PS and LE
weighting). This confirms that the six-dimension coding discriminates
between failure types rather than collapsing them into a single "bad
governance" label, and that the two variants shift emphasis correctly
without disturbing the overall ordering.

---

## Evidence gaps and viva-relevant caveats

**Original three stub cases (unchanged).**

- The specific generation tool used in the Ghana deepfake case (Case 3
  D1) is not identified in any located source.
- The 25 May 2026 court outcome for the Ghana suspects (Case 3 D6) is
  not documented in the sources available at the time of coding.
- The certified true copy of the November 2025 consent judgment clauses
  in the Meta case (Case 1 D6) was accessed through legal commentary
  rather than through a court-issued PDF; the specific NDPA sections
  cited by NDPC in its 18 February 2025 Final Orders were also accessed
  through secondary summary.
- The NYDFS finding of "no violation" in Case 2 is a legal conclusion
  about disparate treatment and impact, not a normative endorsement of
  the system's governance maturity across all six dimensions. The
  Level 4 score on D5 reflects programme maturity, not outcome fairness.

**Extension cases (added for Chapter Five).**

- Several extension cases (Cases 11, 12, 13, 15) rest on regulator
  statements and reputable secondary reporting rather than full published
  decisions. Where the primary decision is not publicly available, the
  coding cites the regulator statement as the primary source. Fidelity,
  MultiChoice, the seven-firm aggregate, and the NDPC 1,368-firm notice
  fall in this category.
- Case 6 (HK/UAE voice-clone) rests entirely on secondary reporting of a
  US court filing; no published judgment was located. Coding is flagged
  as news-plus-court-document, not a published decision.
- Case 11 (NDPC v. Fidelity) is contested: Fidelity publicly denied the
  NDPC finding. The score reflects the regulator finding with the
  contest flagged.
- Case 5 (NIMC NIN/BVN) is contested: NIMC denied any breach of its
  systems. The score reflects the documented ecosystem failure per
  coding rule 3 (default to the lower level where a denial is not
  accompanied by affirmatively documented governance controls).
- Case 13 (NDPC seven-firm) aggregates seven unnamed firms; its
  entity-level vector is a group inference, not a single-entity finding.
- Cases 14 and 15 (FCCPC/DEON and NDPC 1,368-firm notice) are coded as
  regulator-maturity exemplars rather than as entity failures. They
  score a regulator's posture, not a failing institution. See the
  Cross-case synthesis section above for the separation rationale.
- Enforcement reversals introduce a further caveat. The Meta and
  WhatsApp NDPC track was reversed by a Federal High Court consent
  judgment of 3 November 2025 (documented in Case 1 D6). The FCCPC/DEON
  enforcement was suspended by court order in April 2026 before being
  reinstated by the July 2026 judgment (documented in Case 14 D6).
  Regulator maturity can regress; the coding captures this in the D6
  score for each affected case.
- Coder bias: all fifteen cases were coded by a single researcher. The
  default-low rule (rule 3) was adopted specifically to counter this
  bias, and every inferred score is flagged in the individual case
  entries. A future extension should introduce a second independent
  coder and report Cohen's kappa per dimension.
