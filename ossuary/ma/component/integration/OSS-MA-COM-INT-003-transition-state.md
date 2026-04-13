---
ossuary_id: OSS-MA-COM-INT-003
altitude: Component
domain: M&A Integration Architecture
state: Transition State
output_type: Pattern
subsystem: Integration Domain
togaf_constructs:
  primary: [Work Package, Course of Action, Control]
  secondary: [Application Service, Logical Application Component, Interface]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-003
---

# M&A Integration Architecture — Component Altitude — Integration Domain — Transition State

## Wave Alignment

### Wave 0 — Shadow Integration Discovery
**Exit criteria:** All point-to-point integrations inventoried. All shadow integrations discovered and documented. Protocol inventory complete. Dependency map produced. Topic taxonomy inventory complete.
**Constraint:** No platform selection in Wave 0. Discovery precedes vendor decision. Bureau-enforced.

### Wave 1 — Platform Selection and Backbone Deployment
**Exit criteria:** Enterprise integration platform selected and ARB-ratified. API gateway deployed. Message broker deployed. Integration registry deployed. ARB integration standards published. Freeze policy activated. Parallel operation confirmed.

### Wave 2 — Migration and Decommission Sequencing
**Exit criteria:** Migration sequencing declared per dependency map. 60% of legacy volume routed through backbone. Protocol transformation layer operational. Topic taxonomy harmonized. First decommission tranche complete.

### Wave 3 — Full Migration and Legacy Decommission
**Exit criteria:** 100% of governed traffic through enterprise backbone. All legacy point-to-point decommissioned. Both legacy ESBs decommissioned. Both legacy API gateways decommissioned. Both legacy message brokers decommissioned. Enterprise integration registry authoritative. Bureau validation before closure.

## Component Transition Risk Register

| Risk | Wave | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|---|
| Shadow integrations undiscovered at Wave 0 close | 0 | Critical | Application Service: incomplete inventory | Yes |
| Platform selected before discovery complete | 0,1 | High | Course of Action: vendor decision without full requirements | Yes |
| Freeze policy unenforced | 1,2 | Critical | Control: ARB freeze not operational | Yes |
| Migration out of dependency order | 2 | High | Work Package: consuming application broken | Yes |
| Legacy platform decommissioned before migration validated | 2,3 | Critical | Application Service: service continuity broken | Yes |
| Ungoverned interfaces surviving Wave 3 close | 3 | Critical | Interface: target state not achieved | Yes |
| Dependent domain migrations blocked by Integration delay | 2,3 | High | Course of Action: all domain migrations dependent on backbone | Yes |

## Ossuary Notes

Highest-priority Component transition pattern in the M&A corpus. All other domain
Component transitions declare dependency on this pattern. Integration Domain delay
propagates severity to all dependent domains.