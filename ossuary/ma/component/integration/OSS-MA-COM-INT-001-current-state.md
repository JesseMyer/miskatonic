---
ossuary_id: OSS-MA-COM-INT-001
altitude: Component
domain: M&A Integration Architecture
state: Current State
output_type: Pattern
subsystem: Integration Domain
togaf_constructs:
  primary: [Application Service, Logical Application Component]
  secondary: [Physical Application Component, Data Entity, Interface]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-001
---

# M&A Integration Architecture — Component Altitude — Integration Domain — Current State

## Application Component Inventory

### Entity A
**ESB or iPaaS Platform** — Logical Application Component. Message routing, transformation, orchestration. Entity-local. Shadow integrations undocumented.
**API Gateway** — Logical Application Component. API lifecycle management, traffic routing, authentication. Entity-local.
**Message Broker** — Logical Application Component. Asynchronous event distribution. AMQP. Entity-local.
**Integration Registry** — Absent or informal. Spreadsheet or wiki. Not fit for purpose.

### Entity B
**ESB or iPaaS Platform** — Logical Application Component. Entity-local. May differ from Entity A vendor.
**API Gateway** — Logical Application Component. Entity-local. Standards non-aligned with Entity A.
**Message Broker** — Logical Application Component. AMQP or JMS; may differ from Entity A.
**Integration Registry** — Absent or informal. Same condition as Entity A.

## Interface Inventory

| Interface | Owner | Protocol | Consumer | Governed |
|---|---|---|---|---|
| Entity A ESB inbound | Entity A | SOAP, REST | Entity A applications | Entity-local only |
| Entity A API Gateway | Entity A | REST, OAuth 2.0 | Entity A consumers | Entity-local only |
| Entity A Message Broker | Entity A | AMQP | Entity A event consumers | Entity-local only |
| Entity B ESB inbound | Entity B | REST | Entity B applications | Entity-local only |
| Entity B API Gateway | Entity B | REST, OAuth 2.0 | Entity B consumers | Entity-local only |
| Entity B Message Broker | Entity B | AMQP or JMS | Entity B event consumers | Entity-local only |
| Cross-entity interfaces | None | N/A | N/A | None exist |

## Architectural Risk Profile

| Risk | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|
| Shadow integrations undiscovered | Critical | Application Service: ungoverned services outside Logical Application Component boundary | Yes |
| No cross-entity interface exists | Critical | Interface: no governed cross-entity integration surface | Yes |
| Dual integration registries informal | High | Logical Application Component: no authoritative endpoint inventory | Yes |
| Protocol non-alignment between entities | High | Interface: AMQP vs JMS; SOAP vs REST | Yes |
| API standards non-aligned | Medium | Logical Application Component: OAuth and REST implementations non-comparable | Yes |
| Topic taxonomy non-aligned | Medium | Logical Application Component: event consumers cannot span entities | Yes |

## Ossuary Notes

First Component altitude pattern in the Ossuary corpus. Shadow integration discovery
is a Wave 0 exit criterion. Component descent for dependent domains blocked until
discovery is complete. Bureau scores against interface governance dimension.