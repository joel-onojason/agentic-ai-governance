# Case Coding Appendix

**Empirical per-dimension evidence tables for the three stub retrospective
cases used to validate the Agentic AI Governance Management System.**

This appendix is the audit trail for every score in
`evaluation/cases.py`. Chapter Four of the thesis references this
document in Section 4.2.8. Chapter Five extends the same method to the
full twelve to fifteen case sample.

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
4. No dimension in any case is scored at Level 5 because none of the
   primary sources evidenced adaptive governance, learning loops, or
   red-team exercises.

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

## Cross-case synthesis

The three cases occupy three different regions of the maturity space
rather than three points on a single line, which is what a stub-code
demonstration needs.

- **Case 1 (Meta/WhatsApp)**: high D5 with depressed D6. Diagnostic
  marker for institutional maturity defeated by enforcement collapse.
- **Case 2 (Apple Card/Goldman)**: high D5 with depressed D4. Diagnostic
  marker for technical maturity without human-facing transparency.
- **Case 3 (Ghana deepfake)**: flat Level-1 profile with a single D6
  bump. Diagnostic marker for governance absence with reactive criminal
  accountability.

Plotted as vectors of the six scores:

| Case | D1 | D2 | D3 | D4 | D5 | D6 |
|------|----|----|----|----|----|----|
| Meta/WhatsApp | 2 | 2 | 2 | 2 | 3 | 2 |
| Apple Card | 3 | 3 | 3 | 2 | 4 | 3 |
| Ghana deepfake | 1 | 1 | 1 | 1 | 1 | 2 |

These three produce numerically separable profiles under both variants,
which shows that the six-dimension coding discriminates between failure
types rather than collapsing them into a single "bad governance" label.

---

## Evidence gaps and viva-relevant caveats

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
