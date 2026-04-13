---
ossuary_id: OSS-MA-SCH-CUS-003
altitude: Schema
domain: M&A Integration Architecture
state: Transition State
output_type: Pattern
subsystem: Customer Domain
togaf_constructs:
  primary: [Data Entity, Logical Data Component]
  secondary: [Physical Data Component, Data Entity, Information System Service]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SEQ-CUS-003
---

# M&A Integration Architecture — Schema Altitude — Customer Domain — Transition State

## Altitude and Parentage

This pattern sits at **Schema** altitude under the M&A Integration Architecture domain.
It declares the governed data shapes, keys, lineage, and authority for **Customer Domain**,
descending from Sequence pattern `OSS-MA-SEQ-CUS-003`. It names what must be true in data for the
declared sequences and components to be coherent.

**Schema focus:** party, account, agreement, and consent entities; golden customer keys; privacy classification.

## Logical Data Inventory (As-Reported)

| Data entity (candidate) | Authority | Notes |
|---|---|---|
| [Primary business entities] | Contested across entities | No single MDM authority |
| [Reference data] | Duplicated masters | Drift between entities |
| [Transactional artifacts] | System-local stores | Reconciliation required for cross-entity reporting |

## Key Strategy and Identity

Transition: staged reconciliation, golden-record pilot, and explicit freeze rules for competing writes.

## Lineage and Transformation

Declare how data moves from origin systems to consumers: batch vs. near-real-time,
transformations applied, and where semantic drift is introduced. Bureau scores lineage
gaps as Data Entity relationship defects.

## Privacy, Classification, and Regulatory Constraints

Declare classification per attribute where relevant. Schema altitude is where residency,
retention, and purpose-limitation constraints bind to fields and entities.

## Architectural Risk Profile

| Risk | Severity | Broken construct relationship | Bureau suggestion |
|---|---|---|---|
| Contested master for a domain | Critical | Data Entity: no authoritative Logical Data Component | Yes |
| Undocumented lineage | High | Data Entity: transformations not traceable | Yes |
| Key collision across entities | High | Data Entity: identifier semantics incompatible | Yes |

## Ossuary Notes

Schema patterns must align with Sequence and Component parents. Bureau references
Ossuary reference tier when suggesting remediation for MDM and lineage controls.
