---
ossuary_id: OSS-MA-COM-HCM-003
altitude: Component
domain: M&A Integration Architecture
state: Transition State
output_type: Pattern
subsystem: Human Capital Domain
togaf_constructs:
  primary: [Work Package, Course of Action, Control]
  secondary: [Application Service, Logical Application Component, Data Entity]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-003
---

# M&A Integration Architecture — Component Altitude — Human Capital Domain — Transition State

## Dependency Declaration

| Dependency | Pattern | Wave Required | Type |
|---|---|---|---|
| Enterprise integration backbone | OSS-MA-COM-INT-003 | Wave 1 complete | Hard |
| Compensation model ratification | HR, legal, finance function | Wave 1 entry | Hard |
| Benefit plan rationalization decision | HR, legal, procurement | Wave 1 entry | Hard |
| Payroll jurisdiction scope declaration | Compliance, legal function | Wave 0 complete | Hard |
| ERP rationalization sequencing | OSS-MA-COM-FIN-003 | Wave 1 coordinated | Coordination |

## Wave Alignment

### Wave 0 — Human Capital Domain Discovery
**Exit criteria:** Both HRIS platforms documented. Both HR masters documented. Both payroll platforms documented. Both benefits platforms documented. Talent acquisition systems documented or absence confirmed. Data Entity semantic comparison complete. Payroll jurisdiction scope confirmed. Qualification holds issued. Legal, HR, and compliance escalations initiated.

### Wave 1 — Authority Declaration and HCM Foundation
**Exit criteria:** Legal, HR, and compliance escalations resolved. All qualification holds resolved. Enterprise MDM platform selected. Canonical employee data model drafted. Canonical organizational hierarchy declared and ratified. HRIS platform disposition decision ARB-ratified. Payroll platform disposition coordinated with ERP rationalization. Benefits platform disposition initiated. Legacy HRIS platforms under freeze. ERP rationalization coordination confirmed.

### Wave 2 — Migration and Workforce Unification
**Exit criteria:** Enterprise HR master operational. HRIS migration initiated with data quality validation gates. Canonical organizational hierarchy operational. Payroll platform unified with parallel run executed and validated against legacy output. Benefits platform unified with carrier feeds renegotiated and tested. Compensation model unified. Talent acquisition system unified if applicable. Legacy HR master in migration queue. Minimum two parallel pay cycles validated before legacy decommission permitted.

### Wave 3 — Legacy Decommission and Domain Closure
**Exit criteria:** Unified HRIS operational enterprise-wide. Legacy HRIS platforms decommissioned. Enterprise HR master authoritative. Unified payroll operational with minimum two validated parallel cycles complete. Unified benefits platform operational. Unified talent acquisition system operational if applicable. Workforce view confirmed unified. Finance Domain coordination confirmed. Human Capital Domain validated against OSS-MA-COM-HCM-002. Compensation model and org hierarchy ratification documentation filed in Grimoire.

## Component Transition Risk Register

| Risk | Wave | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|---|
| Legal and HR escalation delayed: Wave 1 blocked | 0,1 | Critical | Course of Action: compensation and benefit decisions cannot be architecturally assumed | Yes |
| Payroll parallel run not executed before legacy decommission | 2,3 | Critical | Control: payroll accuracy unvalidated; employee payment risk | Yes |
| Compensation model migration errors | 2 | Critical | Data Entity: pay element mapping failures produce incorrect payroll output | Yes |
| Carrier feed renegotiation delayed | 1,2 | High | Logical Application Component: carrier contracts govern migration timeline | Yes |
| Organizational hierarchy contested during migration | 2 | High | Data Entity: org design disputes surface during HRIS implementation | Yes |
| Payroll and ERP sequencing misaligned | 1,2 | High | Course of Action: payroll feed to ERP broken if platforms rationalized independently | Yes |
| Legacy HRIS decommissioned before payroll validated | 3 | Critical | Logical Application Component: payroll dependency on HRIS data | Yes |

## Ossuary Notes

Payroll parallel run requirement is a platform-declared standard: no payroll platform
decommissioned without minimum two validated parallel pay cycles. This is non-negotiable.
Employee payment accuracy is a legal obligation. Bureau enforces this as a hard Wave 3
entry condition.