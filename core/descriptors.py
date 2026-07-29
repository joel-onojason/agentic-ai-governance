"""
core.descriptors
=================
The thirty descriptor cells that populate the six-by-five maturity matrix.

Each cell is a concrete, scoreable statement of what maturity looks like at
that (dimension, level) pair. Descriptors are anchored on the regulatory
instruments in Table 3.1 wherever possible.

Reference: Section 3.4 of the project thesis.
"""

from typing import Dict, Tuple


# The dictionary is keyed on (dimension_id, level_number).
# Every one of the 30 cells is populated. The test suite verifies this.
DESCRIPTORS: Dict[Tuple[str, int], str] = {

    # -------- D1: Autonomy and tool-use governance --------
    ("D1", 1): (
        "No scope constraints on agent actions. No tool allow-list. No logging "
        "of actions the agent takes."
    ),
    ("D1", 2): (
        "Informal restrictions on which tools the agent may call. Actions are "
        "logged inconsistently and no owner reviews the logs."
    ),
    ("D1", 3): (
        "Written action-space policy in place. Tool allow-list maintained. All "
        "agent actions logged and mapped to NDPA s. 37 automated decision-making "
        "duties."
    ),
    ("D1", 4): (
        "Action-space monitored continuously against policy. Deviations "
        "flagged for review. Tool allow-list reviewed on a quarterly schedule."
    ),
    ("D1", 5): (
        "Prospective action-space reviews before each new agent goes live. "
        "Tool usage analysed for scope creep. Findings feed back into policy."
    ),

    # -------- D2: Agent identity and authentication --------
    ("D2", 1): (
        "Agents run under generic service accounts. No distinction between "
        "one agent and another at the identity layer."
    ),
    ("D2", 2): (
        "Agents have distinct credentials, but no key rotation and no "
        "multi-factor authentication for agent-to-system calls."
    ),
    ("D2", 3): (
        "Unique agent identity per deployment. Credentials rotated on a "
        "documented schedule. MFA required for sensitive operations. Meets "
        "the CBN Risk-Based Cybersecurity Framework 2024 identity provisions."
    ),
    ("D2", 4): (
        "Agent identity verified on every session. High-value actions "
        "cryptographically signed. Identity events form part of the audit trail."
    ),
    ("D2", 5): (
        "Verifiable agent identity across systems in the LOKA Protocol sense. "
        "Continuous risk-based re-authentication. Non-repudiation supported "
        "by cryptographic evidence."
    ),

    # -------- D3: Multi-agent and delegation oversight --------
    ("D3", 1): (
        "No oversight of agent-to-agent handoffs. No policy on when one agent "
        "may delegate work to another."
    ),
    ("D3", 2): (
        "Informal awareness of delegation between agents. No systematic "
        "monitoring of handoff points."
    ),
    ("D3", 3): (
        "Documented delegation policy. Handoffs logged. At least one human "
        "review point in every multi-agent workflow."
    ),
    ("D3", 4): (
        "Delegation chains monitored continuously. Alerts fire when work "
        "passes to an agent outside the trusted set. Reviews run quarterly."
    ),
    ("D3", 5): (
        "Prospective delegation-risk assessment before deploying any "
        "multi-agent system. Topology tested through simulation and red team "
        "exercises."
    ),

    # -------- D4: Human-in-the-loop and kill-switch design --------
    ("D4", 1): (
        "No kill-switch. No human approval required for any agent action. If "
        "the agent misbehaves, there is nothing to stop it in real time."
    ),
    ("D4", 2): (
        "Kill-switch exists on paper. It has never been tested. Approval rules "
        "for sensitive actions are informal."
    ),
    ("D4", 3): (
        "Kill-switch documented. Approval required before an agent writes to "
        "a sensitive system. The kill-switch path has been tested at least once."
    ),
    ("D4", 4): (
        "Kill-switch drilled on a routine schedule. Approval thresholds "
        "monitored. Deviations trigger review under the GAID grievance provisions."
    ),
    ("D4", 5): (
        "Prospective kill-switch reviews before each new agent goes live. "
        "Drill outcomes feed back into the design. Human override tested under "
        "adversarial conditions."
    ),

    # -------- D5: Data and privacy under NDPA and GAID --------
    ("D5", 1): (
        "No Data Protection Impact Assessment. No DCPMI registration under "
        "NDPA s. 44. No documented lawful basis for processing personal data."
    ),
    ("D5", 2): (
        "Some privacy policies exist but are applied inconsistently. DPIA "
        "not carried out for agentic deployments. DCPMI registration missing "
        "or overdue."
    ),
    ("D5", 3): (
        "DPIA completed for every agentic deployment that processes personal "
        "data. DCPMI registered under NDPA s. 44. Lawful basis documented. "
        "Cross-border transfers assessed against GAID Schedules."
    ),
    ("D5", 4): (
        "DPIAs reviewed on schedule. Breach-notification procedure tested. "
        "Data subject rights operationalised through a working request channel."
    ),
    ("D5", 5): (
        "Privacy-by-design embedded in agent architecture. DPIAs updated "
        "continuously as agents evolve. Data minimisation verified through "
        "automated checks."
    ),

    # -------- D6: Accountability and audit logging --------
    ("D6", 1): (
        "No audit logging. No named accountability owner. No documented "
        "incident response procedure."
    ),
    ("D6", 2): (
        "Some logging exists but is incomplete. Accountability chain unclear. "
        "Incident response procedure informal."
    ),
    ("D6", 3): (
        "Agent-attributable audit logs. Named accountability owner per agent. "
        "Incident response procedure documented and mapped to NDPA s. 44 duties."
    ),
    ("D6", 4): (
        "Audit logs monitored continuously. Accountability reviewed quarterly. "
        "Incident response drilled at least annually."
    ),
    ("D6", 5): (
        "Independent audit of agent operations. Prospective accountability "
        "review before deployment. Lessons from incidents feed back into the "
        "design of subsequent agents."
    ),
}


def get_descriptor(dimension_id: str, level: int) -> str:
    """Return the descriptor for the given dimension and level."""
    key = (dimension_id, level)
    if key not in DESCRIPTORS:
        raise KeyError(f"No descriptor for {key}")
    return DESCRIPTORS[key]


def get_dimension_ladder(dimension_id: str) -> Dict[int, str]:
    """Return the full 5-level ladder for one dimension."""
    return {level: DESCRIPTORS[(dimension_id, level)] for level in range(1, 6)}
