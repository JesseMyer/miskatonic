---
ossuary_id: OSS-MA-COM-CUS-001
altitude: Component
domain: M&A Integration Architecture
state: Current State
output_type: Pattern
subsystem: Customer Domain
togaf_constructs:
  primary: [Application Service, Logical Application Component]
  secondary: [Physical Application Component, Data Entity, Interface]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-001
---

# M&A Integration Architecture — Component Altitude — Customer Domain — Current State

## Application Component Inventory

### Entity A
**CRM Platform** — Logical Application Component. Customer record management, opportunity tracking, relationship history. Entity-local. Data Entity: Customer, Contact, Opportunity, Account.
**Customer Data Platform** — Logical Application Component (present or absent). Customer profile unification, behavioral data aggregation. Entity-local.
**Identity Resolution Service** — Logical Application Component (formal or informal). Customer identity matching, deduplication. Entity-local. Resolution rules undocumented at cross-entity level.
**Customer Master** — Logical Data Component. Entity-local. Data Entities: Customer, Party, Contact, Preference.

### Entity B
**CRM Platform** — Logical Application Component. Entity-local. Standards non-aligned with Entity A. Customer data model non-aligned regardless of vendor.
**Customer Data Platform** — Logical Application Component (present or absent). Entity-local.
**Identity Resolution Service** — Logical Application Component. Entity-local. Resolution rules non-aligned with Entity A.
**Customer Master** — Logical Data Component. Entity-local. Semantic definitions non-aligned with Entity A.

## Interface Inventory

| Interface | Owner | Protocol | Consumer | Governed |
|---|---|---|---|---|
| Entity A CRM API | Entity A | REST | Entity A applications | Entity-local only |
| Entity A CDP export | Entity A | Batch, REST | Entity A marketing | Entity-local only |
| Entity B CRM API | Entity B | REST | Entity B applications | Entity-local only |
| Entity B CDP export | Entity B | Batch, REST | Entity B marketing | Entity-local only |
| Cross-entity customer interface | None | N/A | N/A | Does not exist |

## Data Entity Non-Alignment

| Data Entity | Conflict |
|---|---|
| Customer | Non-identical semantics; resolution required |
| Party | May be absent in one entity |
| Contact | Relationship to Customer differs |
| Preference | Channel and consent models differ |

## Architectural Risk Profile

| Risk | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|
| No cross-entity customer identity | Critical | Data Entity: no canonical Customer model spans both entities | Yes |
| Dual customer masters non-aligned | Critical | Logical Data Component: two authoritative sources, non-identical semantics | Yes |
| Identity resolution rules undocumented | High | Logical Application Component: resolution logic ungoverned at enterprise level | Yes |
| CDP absent in one or both entities | Medium | Logical Application Component: behavioral data aggregation gap | Yes |
| Cross-entity customer interface absent | Critical | Interface: no governed cross-entity customer data surface | Yes |

## Qualification Holds
- Customer entity canonical definition required before MDM authority declared.
- Identity resolution terminal condition: probabilistic threshold, deterministic, or human review?

## Ossuary Notes

Customer Domain is highest business-value domain post-integration backbone. Identity
resolution is the critical path construct. All cross-entity customer interfaces route
through enterprise integration backbone per OSS-MA-COM-INT-002.