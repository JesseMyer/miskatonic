---
ossuary_id: OSS-MA-COM-FIN-001
altitude: Component
domain: M&A Integration Architecture
state: Current State
output_type: Pattern
subsystem: Finance Domain
togaf_constructs:
  primary: [Application Service, Logical Application Component]
  secondary: [Physical Application Component, Data Entity, Interface]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-001
---

# M&A Integration Architecture — Component Altitude — Finance Domain — Current State

## Application Component Inventory

### Entity A
**ERP Platform** — Logical Application Component. General ledger management, AP, AR, fixed assets, financial close orchestration. Entity-local. Data Entity: Account, Journal Entry, Cost Center, Legal Entity, Vendor, Customer Ledger.
**Financial Close Management Tool** — Logical Application Component (present or absent). Close task orchestration, reconciliation management. Entity-local.
**Regulatory Reporting Platform** — Logical Application Component. Statutory reporting, tax reporting, regulatory filing management. Entity-local. Jurisdiction-specific.
**Financial Master** — Logical Data Component. Entity-local. Data Entities: Account, Journal Entry, Cost Center, Legal Entity, Regulatory Report.

### Entity B
**ERP Platform** — Logical Application Component. Entity-local. Chart of accounts non-aligned with Entity A. Legal entity hierarchy differs materially.
**Financial Close Management Tool** — Logical Application Component (present or absent). Close calendar non-aligned with Entity A.
**Regulatory Reporting Platform** — Logical Application Component. Entity-local. May carry different jurisdictional obligations than Entity A.
**Financial Master** — Logical Data Component. Entity-local. Chart of accounts and legal entity hierarchy non-aligned with Entity A.

## Interface Inventory

| Interface | Owner | Protocol | Consumer | Governed |
|---|---|---|---|---|
| Entity A ERP API | Entity A | REST, batch | Entity A applications | Entity-local only |
| Entity A reporting feed | Entity A | Batch | Entity A reporting platform | Entity-local only |
| Entity B ERP API | Entity B | REST, batch | Entity B applications | Entity-local only |
| Entity B reporting feed | Entity B | Batch | Entity B reporting platform | Entity-local only |
| Cross-entity financial interface | None | N/A | N/A | Does not exist |
| Consolidation feed | Manual | Spreadsheet | Group finance | Ungoverned |

## Data Entity Non-Alignment

| Data Entity | Conflict |
|---|---|
| Account | Account codes, hierarchy, and naming non-aligned |
| Cost Center | Hierarchy depth and allocation logic differ |
| Legal Entity | Holding structure non-aligned; consolidation path differs |
| Journal Entry | Posting rules and period definitions may differ |
| Regulatory Report | Jurisdiction and filing format differ |

## Architectural Risk Profile

| Risk | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|
| Chart of accounts non-alignment | Critical | Data Entity: Account canonical model absent; consolidation impossible | Yes |
| Legal entity hierarchy non-aligned | Critical | Data Entity: Legal Entity structure non-comparable; statutory reporting at risk | Yes |
| Consolidation reporting manual | Critical | Application Service: no governed consolidation interface | Yes |
| Close cycles unsynchronized | High | Process: financial close cannot be governed enterprise-wide | Yes |
| Financial close construct type unresolved | High | Process or Contract: qualification hold open | Yes |
| Regulatory reporting obligations non-aligned | High | Contract or Requirement: jurisdiction-specific obligations not reconciled | Yes |

## Qualification Holds
- Financial close construct type: Process with Control, Process with Contract, or both?
- Regulatory reporting jurisdiction: which jurisdictions govern each entity?
- Chart of accounts rationalization authority: which entity's chart or new construction?
- Legal entity consolidation path: legal and tax decision required before architecture can proceed.

## Ossuary Notes

Finance Domain carries highest qualification hold complexity. Legal entity hierarchy and
chart of accounts rationalization require legal, tax, and regulatory input. Escalation
to legal and tax is a Bureau-recommended action, not an optional suggestion.