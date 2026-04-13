---
ossuary_id: OSS-MA-COM-INT-002
altitude: Component
domain: M&A Integration Architecture
state: Target State
output_type: Pattern
subsystem: Integration Domain
togaf_constructs:
  primary: [Application Service, Logical Application Component]
  secondary: [Physical Application Component, Data Entity, Interface, Control]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-002
---

# M&A Integration Architecture — Component Altitude — Integration Domain — Target State

## Application Component Inventory

**ESB or iPaaS Platform (Unified)** — Logical Application Component. Enterprise message routing, canonical transformation, governed orchestration. Enterprise-wide. Cloud-native preferred. ARB-governed. All endpoints declared and versioned.
**API Gateway (Unified)** — Logical Application Component. Enterprise API lifecycle management, governed traffic routing, canonical OAuth 2.0. Enterprise-wide. ARB-governed. Versioning policy declared.
**Message Broker (Unified)** — Logical Application Component. Enterprise asynchronous event distribution. AMQP canonical. Governed topic taxonomy. No ungoverned topics permitted.
**Enterprise Integration Registry** — Logical Application Component. Authoritative endpoint inventory. Governed system of record. All endpoints declared, versioned, dependency-mapped.

## Interface Inventory (Governed)

| Interface | Owner | Protocol | Consumer | Governed |
|---|---|---|---|---|
| Enterprise ESB inbound | Unified integration platform | REST, AMQP | All governed applications | Yes, ARB |
| Enterprise API Gateway | Unified integration platform | REST, OAuth 2.0 | All governed API consumers | Yes, ARB |
| Enterprise Message Broker | Unified integration platform | AMQP | All governed event consumers | Yes, ARB |

All interfaces governed. No ungoverned interface exists. Any interface not in this inventory is a Bureau finding.

## Architectural Achievement Profile

| Construct | Target Condition |
|---|---|
| Logical Application Component | Single governed instance per integration function |
| Interface | All interfaces governed; canonical protocols declared |
| Application Service | All services route through enterprise integration platform |
| Control | ARB governs all integration changes |
| Integration Registry | Authoritative; all endpoints declared and versioned |

## Ossuary Notes

Target state closes all current-state findings for Integration Domain at Component altitude.
Enterprise integration platform is the dependency anchor for all other domain Component
migrations. No domain Component target state is achievable without this pattern's
conditions being met first.