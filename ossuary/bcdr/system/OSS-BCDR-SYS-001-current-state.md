---
ossuary_id: OSS-BCDR-SYS-001
altitude: System
domain: Business Continuity & Disaster Recovery
state: Current State
output_type: Pattern
togaf_constructs:
  primary: [Capability, Control]
  secondary: [Course of Action, Value Stream, Organization Unit]
adm_phase: omit
bureau_calibration: false
region: US, NY regulatory jurisdiction
regulatory_surface:
  primary: NY State IT
  secondary: 23 NYCRR 500
---

# BCDR — System Altitude — Current State

## Motivational Layer

### Elicited (Aspirational)
| Construct | Declaration |
|---|---|
| Driver | [Elicited: regulatory obligation, client contractual exposure, reputational risk] |
| Goal | [Elicited: demonstrate recovery capability, satisfy dual regulatory surface] |
| Objective | [Elicited: close end-to-end DR validation gap; establish regulatory-committed timeline] |

### Consumed (Curated)
| Construct | Declaration |
|---|---|
| Driver | [From documentation: BCDR plan exists; component testing evidenced] |
| Goal | [From documentation: RTO/RPO declared per service tier] |
| Objective | [From documentation: internal compliance target exists; not regulatory-committed] |

**Motivational delta:** Internal timeline not externally committed. Declaration and proof disconnected at service tier. Both are Bureau finding candidates.

## Organization Structure (As-Reported)

| Entity | Type | Notes |
|---|---|---|
| [Technology delivery org] | Organization Unit | Mixed: SaaS and managed services |
| [Compliance function] | Organization Unit | Owns BCDR documentation; no test authority declared |
| [Engineering function] | Organization Unit | Owns AZ architecture; component testing executed |
| [Client-facing function] | Organization Unit | DFS regulated and state agency exposure |

## Capability Landscape

The firm operates a cloud native infrastructure with explicitly architected and governed
AZ failover boundaries. BCDR documentation exists. Service-tier RTO/RPO declarations
are in place. The recovery posture is governed but unproven: component testing has been
executed; full end-to-end DR has never been run.

- Recovery architecture is governed. AZ failover explicitly architected.
- Service-tier RTO/RPO declarations exist. Mature posture.
- End-to-end validation is absent. Full DR never executed.
- Regulatory commitment is absent. Internal timeline only.
- Dual regulatory surface is uncoordinated.

## Value Streams (Conditional)

| Candidate | Triggering Capability | Qualification Required | Typed As |
|---|---|---|---|
| Recovery Execution | [DR Capability] | Terminal condition: service restoration or regulatory evidence? | Value Stream or Process, pending |
| Compliance Reporting | [Governance Capability] | Driven by audit cycle or continuous obligation? | Process with Control implications, pending |
| Client SLA Assurance | [Service Delivery Capability] | SLA mapped to service-tier RTO/RPO? | Value Stream or Contract, pending |

## Architectural Risk Profile

| Risk | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|
| End-to-end DR never validated | Critical | Control: no recovery proof against service-tier RTO/RPO | Yes |
| No regulatory-committed timeline | High | Course of Action: internal target unenforceable by either regulator | Yes |
| Dual regulatory surface uncoordinated | High | Control: no unified compliance posture across DFS and NY State IT | Yes |
| Declaration/proof disconnect | High | Process: service-tier RTO/RPO declared but unvalidated under DR conditions | Yes |
| Compliance function lacks test authority | Medium | Organization Unit: no declared owner for end-to-end DR execution | Yes |

## Ossuary Notes

This pattern reflects a governed but unproven BCDR posture. Materially distinct from
ad hoc or undocumented states. Bureau scoring baseline applied accordingly: documentation
and governance credit applied; validation and commitment gaps scored as open findings.
Illustrative example pattern; not P1 primary domain scope.