---
ossuary_id: OSS-MA-COM-PRD-001
altitude: Component
domain: M&A Integration Architecture
state: Current State
output_type: Pattern
subsystem: Product Domain
togaf_constructs:
  primary: [Application Service, Logical Application Component]
  secondary: [Physical Application Component, Data Entity, Interface]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-001
---

# M&A Integration Architecture — Component Altitude — Product Domain — Current State

## Application Component Inventory

### Entity A
**PIM Platform** — Logical Application Component. Product definition, attribute management, catalog governance, lifecycle tracking. Entity-local. Data Entity: Product, SKU, Attribute, Category.
**Pricing Engine** — Logical Application Component. Price calculation, discount management, promotional pricing. Entity-local. Pricing rules proprietary and undocumented at cross-entity level.
**Product Configuration Service** — Logical Application Component (present or absent). Entity-local.
**Product Master** — Logical Data Component. Entity-local. Data Entities: Product, SKU, Price, Configuration, Entitlement, Category.

### Entity B
**PIM Platform** — Logical Application Component. Entity-local. Category hierarchy and attribute schema differ materially from Entity A.
**Pricing Engine** — Logical Application Component. Entity-local. Pricing logic non-comparable with Entity A.
**Product Configuration Service** — Logical Application Component (present or absent). Entity-local.
**Product Master** — Logical Data Component. Entity-local. Semantic definitions non-aligned with Entity A.

## Interface Inventory

| Interface | Owner | Protocol | Consumer | Governed |
|---|---|---|---|---|
| Entity A PIM API | Entity A | REST | Entity A order mgmt, pricing | Entity-local only |
| Entity A pricing feed | Entity A | REST, batch | Entity A CRM, order mgmt | Entity-local only |
| Entity B PIM API | Entity B | REST | Entity B order mgmt, pricing | Entity-local only |
| Entity B pricing feed | Entity B | REST, batch | Entity B CRM, order mgmt | Entity-local only |
| Cross-entity product interface | None | N/A | N/A | Does not exist |

## Data Entity Non-Alignment

| Data Entity | Conflict |
|---|---|
| Product | Attribute schema non-aligned |
| SKU | Identifier format differs |
| Category | Hierarchy depth and naming non-aligned |
| Price | Currency, discount, and tier models differ |
| Entitlement | May be absent in one entity |

## Architectural Risk Profile

| Risk | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|
| No cross-entity product identity | Critical | Data Entity: no canonical Product model spans both entities | Yes |
| Dual product masters non-aligned | Critical | Logical Data Component: two authoritative sources, non-identical taxonomy | Yes |
| Pricing logic non-comparable | High | Logical Application Component: cross-entity margin analysis impossible | Yes |
| Category hierarchy non-aligned | High | Data Entity: taxonomy conflict blocks unified catalog | Yes |
| Cross-entity product interface absent | Critical | Interface: no governed cross-entity product data surface | Yes |
| Product fulfillment terminal condition unresolved | High | Value Stream or Contract: qualification hold open | Yes |

## Qualification Holds
- Product fulfillment terminal condition: Value Stream, Business Service, or Contract?
- Product taxonomy canonical authority: which entity's taxonomy or new construction?
- Entitlement model: scope and governing construct undeclared.

## Ossuary Notes

Product taxonomy non-alignment is frequently underestimated. Category hierarchy conflicts
block catalog unification more reliably than system incompatibility. Pricing logic
non-comparability is a margin governance risk.