---
ossuary_id: OSS-BCDR-SYS-002
altitude: System
domain: Business Continuity & Disaster Recovery
state: Target State
output_type: Pattern
togaf_constructs:
  primary: [Capability, Control, Measure]
  secondary: [Course of Action, Value Stream, Contract]
adm_phase: omit
bureau_calibration: false
region: US, NY regulatory jurisdiction
regulatory_surface:
  primary: NY State IT
  secondary: 23 NYCRR 500
---

# BCDR — System Altitude — Target State

## Motivational Layer

### Resolved
| Construct | Declaration |
|---|---|
| Driver | [Resolved: regulatory obligation and client contractual exposure governed under unified compliance posture] |
| Goal | [Resolved: recovery capability proven end-to-end; dual regulatory surface satisfied] |
| Objective | [Resolved: regulatory-committed timeline met; full DR validated per service tier] |
| Measure | [Declared: RTO/RPO evidence per service tier; audit-ready documentation current] |

## Organization Structure (Rationalized)

| Entity | Type | Disposition |
|---|---|---|
| [Unified compliance function] | Organization Unit | Test authority declared; owns end-to-end DR execution |
| [Engineering function] | Organization Unit | AZ architecture maintained; DR runbook owned |
| [Client-facing function] | Organization Unit | SLA mapped to service-tier RTO/RPO; client obligations governed |

## Capability Landscape

- Recovery capability is proven. Full DR executed and evidenced per service tier.
- Regulatory commitment is active. Both surfaces carry committed schedules.
- Dual regulatory surface is unified. Single compliance posture governing.
- Test authority is declared. Single Organization Unit owns end-to-end DR execution.
- Declaration and proof are connected. Service-tier RTO/RPO backed by current evidence.

## Value Streams (Resolved)

| Value Stream | Triggering Capability | Terminal Condition | Typed As |
|---|---|---|---|
| Recovery Execution | [DR Capability] | Service restoration evidenced per tier | Value Stream |
| Compliance Reporting | [Governance Capability] | Audit cycle satisfied; continuous obligation met | Process with Control |
| Client SLA Assurance | [Service Delivery Capability] | SLA mapped and evidenced against RTO/RPO | Contract |

## Architectural Achievement Profile

| Construct | Target Condition |
|---|---|
| Capability | DR capability proven end-to-end per service tier |
| Control | Unified compliance posture; test authority declared; audit evidence current |
| Course of Action | Regulatory-committed timeline active on both surfaces |
| Measure | RTO/RPO evidence per service tier; audit-ready |
| Contract | Client SLA mapped to service-tier declarations |
| Organization Unit | Test authority declared; RACI governed |

## Ossuary Notes

Target state closes all four current-state findings. Bureau scoring uses this pattern
as the validation completeness benchmark. Both regulatory surfaces must show committed
schedules and current evidence before target state is declared achieved.