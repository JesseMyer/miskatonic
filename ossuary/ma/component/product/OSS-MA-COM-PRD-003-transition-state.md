---
ossuary_id: OSS-MA-COM-PRD-003
altitude: Component
domain: M&A Integration Architecture
state: Transition State
output_type: Pattern
subsystem: Product Domain
togaf_constructs:
  primary: [Work Package, Course of Action, Control]
  secondary: [Application Service, Logical Application Component, Data Entity]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-003
---

# M&A Integration Architecture — Component Altitude — Product Domain — Transition State

## Dependency Declaration

| Dependency | Pattern | Wave Required | Type |
|---|---|---|---|
| Enterprise integration backbone | OSS-MA-COM-INT-003 | Wave 1 complete | Hard |
| Enterprise API gateway | OSS-MA-COM-INT-003 | Wave 1 complete | Hard |
| Unified customer identity operational | OSS-MA-COM-CUS-003 | Wave 2 initiated | Soft |

## Wave Alignment

### Wave 0 — Product Domain Discovery
**Exit criteria:** Both PIM platforms documented. Both product masters documented. Both pricing engines documented. Product configuration services documented or absence confirmed. Data Entity semantic comparison complete. Qualification holds issued.

### Wave 1 — Taxonomy Authority and MDM Foundation
**Exit criteria:** Qualification holds resolved. Enterprise MDM platform selected. Canonical taxonomy constructed and ARB review initiated. PIM platform disposition decision ARB-ratified. Pricing engine disposition decision ARB-ratified. Legacy PIM and pricing platforms under freeze. Canonical Data Entity models drafted.

### Wave 2 — Migration and Catalog Unification
**Exit criteria:** Enterprise product master operational. PIM migration initiated with taxonomy mapping and attribute conformance validation. Pricing engine unified. Product configuration service unified. Legacy product master in migration queue. Canonical Data Entity models ratified. Cross-sell motion pilot executed. Taxonomy mapping completeness 80% or greater before Wave 3 entry.

### Wave 3 — Legacy Decommission and Domain Closure
**Exit criteria:** Unified PIM operational enterprise-wide. Legacy PIM platforms decommissioned. Enterprise product master authoritative. Unified pricing engine operational. Unified product configuration service operational. Cross-sell motion confirmed operational. Joint cross-sell closure criterion validated with OSS-MA-COM-CUS-002. All qualification holds closed in Grimoire.

## Component Transition Risk Register

| Risk | Wave | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|---|
| Integration backbone not ready at Wave 1 entry | 1 | Critical | Course of Action: hard dependency violated | Yes |
| Taxonomy qualification hold unresolved at Wave 1 close | 1 | Critical | Logical Data Component: MDM cannot be declared without canonical taxonomy | Yes |
| Taxonomy mapping failures during PIM migration | 2 | High | Data Entity: legacy products do not map cleanly to canonical taxonomy | Yes |
| Pricing rule reconciliation conflicts | 2 | High | Logical Application Component: conflicting rules produce margin errors | Yes |
| Cross-sell motion blocked by incomplete Customer Domain | 2,3 | High | Application Service: joint enablement condition not met | Yes |
| Legacy product master decommissioned before migration validated | 3 | Critical | Logical Data Component: authoritative record lost | Yes |
| Taxonomy mapping below 80% threshold at Wave 3 entry | 3 | High | Data Entity: canonical model not fully governing; Wave 3 entry blocked | Yes |

## Ossuary Notes

Taxonomy mapping completeness threshold of 80% at Wave 3 entry is a platform-declared
standard. Below 80%, the canonical taxonomy is not governing in practice. Bureau enforces
this threshold as a hard Wave 3 entry condition.