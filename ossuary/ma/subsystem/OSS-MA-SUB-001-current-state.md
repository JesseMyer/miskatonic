---
ossuary_id: OSS-MA-SUB-001
altitude: Subsystem
domain: M&A Integration Architecture
state: Current State
output_type: Pattern
togaf_constructs:
  primary: [Function, Business Service, Organization Unit]
  secondary: [Application Service, Data Entity, Logical Data Component]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
---

# M&A Integration Architecture — Subsystem Altitude — Current State

## Context

Decomposition of OSS-MA-SYS-001 into bounded contexts. One System, many Subsystems.
At current state, each Subsystem exists in duplicate: one instantiation per legacy entity.
Twelve total Subsystem instantiations govern the combined enterprise at close.

## Bounded Context Decomposition

### 1. Customer Domain

**Organization Unit:** Customer Management, per entity
**Function:** Customer onboarding, identity resolution, relationship management, lifecycle tracking
**Business Service:** Customer record management, identity verification, communication preference management
**Application Service:** CRM platform (entity-local), CDP (where present), identity resolution service
**Data Entity:** Customer, Party, Contact, Preference
**Logical Data Component:** Entity-local customer master; no cross-entity canonical model declared
**Current state condition:** Two CRM platforms, two customer masters, non-overlapping identity models.
**Qualification holds:** Customer entity canonical definition; identity resolution terminal condition.

### 2. Product Domain

**Organization Unit:** Product Management, per entity
**Function:** Product definition, catalog management, pricing, configuration, lifecycle governance
**Business Service:** Product catalog service, pricing service, product configuration service
**Application Service:** PIM or product catalog platform (entity-local), pricing engine (entity-local)
**Data Entity:** Product, SKU, Price, Configuration, Entitlement
**Logical Data Component:** Entity-local product master; taxonomies non-aligned across entities
**Current state condition:** Two product catalogs with divergent taxonomies. Cross-sell motions blocked.
**Qualification holds:** Product fulfillment terminal condition; product taxonomy alignment.

### 3. Finance Domain

**Organization Unit:** Finance and Accounting, per entity
**Function:** General ledger management, AP, AR, financial close, regulatory reporting
**Business Service:** Ledger service, close orchestration service, regulatory reporting service
**Application Service:** ERP platform (entity-local), close management tool (where present), reporting platform
**Data Entity:** Account, Journal Entry, Cost Center, Legal Entity, Regulatory Report
**Logical Data Component:** Entity-local chart of accounts; legal entity structures non-aligned
**Current state condition:** Two ERP platforms, two charts of accounts. Consolidation reporting is manual.
**Qualification holds:** Financial close construct type; regulatory reporting obligation.

### 4. Integration Domain

**Organization Unit:** Enterprise Architecture or Integration Engineering, per entity
**Function:** API management, event routing, data synchronization, integration governance
**Business Service:** Integration brokering service, API gateway service, event bus service
**Application Service:** ESB or iPaaS platform (entity-local), API gateway (entity-local), message broker
**Data Entity:** Message, Event, API Contract, Integration Endpoint
**Logical Data Component:** Entity-local integration registry; no cross-entity integration inventory
**Current state condition:** Two ungoverned integration topologies. Shadow integrations undocumented.
**Qualification holds:** Integration governance authority; shadow integration inventory required.

### 5. Human Capital Domain

**Organization Unit:** Human Resources, per entity
**Function:** Workforce management, payroll, benefits administration, talent acquisition, org design
**Business Service:** HR record service, payroll service, benefits administration service
**Application Service:** HRIS platform (entity-local), payroll platform (entity-local), ATS (where present)
**Data Entity:** Employee, Position, Compensation, Benefit, Organization
**Logical Data Component:** Entity-local employee master; no cross-entity workforce model declared
**Current state condition:** Two HRIS platforms, two payroll systems, two compensation models.
**Qualification holds:** Workforce rationalization authority; compensation model harmonization.

### 6. Technology and Infrastructure Domain

**Organization Unit:** IT Operations or Platform Engineering, per entity
**Function:** Infrastructure provisioning, platform governance, security operations, service management
**Business Service:** Infrastructure service, security service, platform service, ITSM service
**Application Service:** Cloud platform (entity-local), ITSM tool (entity-local), security tooling
**Data Entity:** Asset, Configuration Item, Incident, Service Request
**Logical Data Component:** Entity-local CMDB; asset registries non-aligned
**Current state condition:** Two cloud environments, two ITSM platforms, two security toolchains.
**Qualification holds:** Identity provider consolidation authority; security perimeter unification scope.

## Cross-Subsystem Risk Profile

| Risk | Severity | Broken Construct | Subsystems Affected | Bureau Suggestion |
|---|---|---|---|---|
| Duplicate Subsystem instantiation across all domains | Critical | Function: no single Organization Unit owns any domain enterprise-wide | All | Yes |
| No cross-entity Data Entity canonical model | Critical | Data Entity: no Logical Data Component authority declared | Customer, Product, Finance | Yes |
| Integration surface uninventoried | Critical | Application Service: shadow integrations undocumented | Integration | Yes |
| No cross-entity identity provider | High | Application Service: identity resolution is entity-local | Customer, Technology | Yes |
| Qualification holds unresolved at Subsystem boundary | High | Multiple: see per-domain holds above | All | Yes |

## Ossuary Notes

Six bounded contexts declared. Twelve total Subsystem instantiations at current state.
Qualification holds declared per domain; batch issued at this altitude boundary before
Component descent. Component altitude patterns scoped per bounded context.