---
ossuary_id: OSS-MA-COM-CUS-003
altitude: Component
domain: M&A Integration Architecture
state: Transition State
output_type: Pattern
subsystem: Customer Domain
togaf_constructs:
  primary: [Work Package, Course of Action, Control]
  secondary: [Application Service, Logical Application Component, Data Entity]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-003
---

# M&A Integration Architecture — Component Altitude — Customer Domain — Transition State

## Dependency Declaration

| Dependency | Pattern | Wave Required | Type |
|---|---|---|---|
| Enterprise integration backbone | OSS-MA-COM-INT-003 | Wave 1 complete | Hard |
| Enterprise API gateway | OSS-MA-COM-INT-003 | Wave 1 complete | Hard |
| Enterprise message broker | OSS-MA-COM-INT-003 | Wave 1 complete | Hard |

## Wave Alignment

### Wave 0 — Customer Domain Discovery
**Exit criteria:** Both CRM platforms documented. Both customer masters documented. Both CDPs documented or absence confirmed. Identity resolution rules documented per entity. Data Entity semantic comparison complete. Qualification holds issued.

### Wave 1 — MDM Authority and Identity Resolution Foundation
**Exit criteria:** Qualification holds resolved. Enterprise MDM platform selected. Canonical Data Entity models drafted. Identity resolution service selected. CRM platform disposition decision ARB-ratified. Legacy CRM platforms under freeze. Customer Domain integration patterns registered.

### Wave 2 — Migration and Identity Resolution Execution
**Exit criteria:** Enterprise customer master operational. Identity resolution service operational. CRM migration initiated with data quality validation gates. CDP consolidation initiated. Legacy customer master in migration queue. Canonical Data Entity models ratified. Cross-sell motion pilot executed.

### Wave 3 — Legacy Decommission and Domain Closure
**Exit criteria:** Unified CRM operational enterprise-wide. Legacy CRM platforms decommissioned. Enterprise customer master authoritative. Legacy customer masters decommissioned. Unified CDP operational. Cross-sell motion confirmed operational. Customer Domain validated against OSS-MA-COM-CUS-002. All qualification holds closed in Grimoire.

## Component Transition Risk Register

| Risk | Wave | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|---|
| Integration backbone not ready at Wave 1 entry | 1 | Critical | Course of Action: dependency violated | Yes |
| Qualification holds unresolved at Wave 1 close | 1 | High | Control: MDM authority cannot be declared | Yes |
| Data quality failures during CRM migration | 2 | High | Data Entity: source data does not conform to canonical model | Yes |
| Duplicate golden records post-identity resolution | 2 | High | Logical Data Component: resolution rules insufficient | Yes |
| Legacy customer master decommissioned before migration validated | 3 | Critical | Logical Data Component: authoritative record lost | Yes |
| Cross-sell motion blocked by incomplete identity resolution | 3 | High | Application Service: System-altitude Value Stream not achievable | Yes |

## Ossuary Notes

Identity resolution is the critical path construct. Data quality at source is the
highest execution risk. Data quality remediation work package should be declared in
Wave 1 if discovery reveals significant quality gaps.