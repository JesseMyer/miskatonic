---
ossuary_id: OSS-MA-SUB-003
altitude: Subsystem
domain: M&A Integration Architecture
state: Transition State
output_type: Pattern
togaf_constructs:
  primary: [Function, Course of Action, Work Package, Control]
  secondary: [Business Service, Application Service, Organization Unit]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
---

# M&A Integration Architecture — Subsystem Altitude — Transition State

## Context

The governed passage from OSS-MA-SUB-001 to OSS-MA-SUB-002. Wave alignment declared
against OSS-MA-SYS-003. Disposition sequencing is domain-priority ordered: Integration
Domain first, Customer and Product second, Finance third, Human Capital and Technology fourth.

## Wave Alignment

### Wave 0 — Discovery and Subsystem Inventory
**Wave alignment:** OSS-MA-SYS-003 Wave 0
**Primary constructs:** Function, Organization Unit, Data Entity
**Exit criteria:**
- All six bounded contexts documented per entity: twelve Subsystem inventories complete.
- Function sets mapped per Organization Unit per entity.
- Business Service inventory complete per domain per entity.
- Application Service topology documented; all point-to-point integrations inventoried.
- Data Entity ownership declared per domain per entity.
- Qualification holds batched at Subsystem altitude boundary.
- Shadow integration discovery complete for Integration Domain before Wave 1 entry.
**Coexistence:** Observation only. No disposition decisions.

### Wave 1 — Foundation and Domain Authority
**Wave alignment:** OSS-MA-SYS-003 Wave 1
**Primary constructs:** Organization Unit, Control, Course of Action
**Exit criteria:**
- Integration Domain: enterprise integration platform selected; unified Organization Unit authority declared.
- Customer Domain: unified Organization Unit declared; customer MDM authority named; identity resolution hold resolved.
- Product Domain: unified Organization Unit declared; product taxonomy hold resolved.
- Finance Domain: unified Organization Unit declared; financial close construct type hold resolved.
- Human Capital and Technology Domains: unified Organization Unit declared; key authority holds resolved.
- All Subsystem qualification holds resolved and recorded in Grimoire before Wave 2 entry.
**Coexistence:** Twelve Subsystem instantiations remain operational. Integration backbone parallel.

### Wave 2 — Rationalization by Domain Priority
**Wave alignment:** OSS-MA-SYS-003 Wave 2
**Primary constructs:** Work Package, Function, Data Entity
**Priority 1: Integration Domain** — backbone carries all new integrations; 60% legacy volume migrated.
**Priority 2: Customer and Product** — customer MDM migration initiated; product taxonomy harmonized.
**Priority 3: Finance** — chart of accounts harmonization; ERP consolidation initiated.
**Priority 4: Human Capital and Technology** — HRIS consolidation initiated; identity provider consolidation initiated.
**Coexistence:** Disposition-queue systems under freeze.

### Wave 3 — Closure per Domain
**Wave alignment:** OSS-MA-SYS-003 Wave 3
**Primary constructs:** Control, Measure, Work Package
**Domain closure sequence:** Integration, Customer, Product, Finance, Human Capital, Technology.
**Final exit criteria:**
- All twelve legacy Subsystem instantiations decommissioned or absorbed.
- All qualification holds closed in Grimoire.
- Subsystem altitude validated against OSS-MA-SUB-002.

## Cross-Subsystem Transition Risk Register

| Risk | Wave | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|---|
| Integration backbone delayed | 1 | Critical | Course of Action: integration priority sequencing violated | Yes |
| Qualification holds unresolved at Wave 1 close | 1 | High | Control: wave gate unenforced | Yes |
| Disposition-queue systems accumulating new integrations | 2 | High | Control: freeze policy unenforced | Yes |
| Domain closure attempted out of sequence | 3 | High | Work Package: dependency on integration backbone closure violated | Yes |
| Legacy Subsystem decommissioned before migration validated | 2,3 | Critical | Function: service continuity broken | Yes |
| Grimoire qualification hold records incomplete at Wave 3 | 3 | Medium | Control: Subsystem closure declared without evidence | Yes |

## Ossuary Notes

Integration Domain disposition priority is a platform-enforced sequencing rule. Bureau
wave-gate scoring uses domain closure sequence as the primary scoring dimension. All
Component altitude patterns must declare parent Subsystem and wave alignment.