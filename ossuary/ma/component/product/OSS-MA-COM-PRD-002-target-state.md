---
ossuary_id: OSS-MA-COM-PRD-002
altitude: Component
domain: M&A Integration Architecture
state: Target State
output_type: Pattern
subsystem: Product Domain
togaf_constructs:
  primary: [Application Service, Logical Application Component]
  secondary: [Physical Application Component, Data Entity, Interface, Control]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-002
---

# M&A Integration Architecture — Component Altitude — Product Domain — Target State

## Application Component Inventory

**PIM Platform (Unified)** — Logical Application Component. Enterprise product definition, governed attribute management, canonical catalog governance. Enterprise-wide. ARB-governed. Canonical taxonomy enforced.
**Pricing Engine (Unified)** — Logical Application Component. Enterprise price calculation, governed discount management, cross-entity margin governance. Enterprise-wide. Pricing rules documented and governed.
**Product Configuration Service (Unified)** — Logical Application Component. Enterprise product configurator, governed bundle definition, unified entitlement management. Enterprise-wide.
**Enterprise Product Master (MDM)** — Logical Data Component. Single authoritative product record store. Canonical taxonomy declared. Single named MDM authority. Canonical taxonomy enforced.

## Interface Inventory (Governed)

| Interface | Owner | Protocol | Consumer | Governed |
|---|---|---|---|---|
| Enterprise PIM API | Unified PIM | REST, OAuth 2.0 | All governed consumers | Yes, ARB |
| Pricing feed | Unified pricing engine | REST, real-time | CRM, order mgmt, backbone | Yes, ARB |
| Configuration API | Unified config service | REST | CRM, order mgmt | Yes, ARB |
| Product master feed | Enterprise MDM | Governed event stream | All product data consumers | Yes, ARB |

## Data Entity Canonical Models

| Data Entity | MDM Authority | Resolution Status |
|---|---|---|
| Product | Named Organization Unit | Resolved |
| SKU | Named Organization Unit | Resolved |
| Category | Named Organization Unit | Resolved |
| Price | Named Organization Unit | Resolved |
| Entitlement | Named Organization Unit | Resolved |

## Ossuary Notes

Cross-sell motion is the System-altitude Value Stream this pattern enables jointly with
OSS-MA-COM-CUS-002. Neither Customer nor Product Domain Component target state alone
enables cross-sell: both must be achieved. Bureau scores cross-sell enablement as a
joint closure criterion.