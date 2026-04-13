---
ossuary_id: OSS-MA-SUB-002
altitude: Subsystem
domain: M&A Integration Architecture
state: Target State
output_type: Pattern
togaf_constructs:
  primary: [Function, Business Service, Organization Unit]
  secondary: [Application Service, Data Entity, Logical Data Component, Control]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
---

# M&A Integration Architecture — Subsystem Altitude — Target State

## Context

Decomposition of OSS-MA-SYS-002 into rationalized bounded contexts. Twelve Subsystem
instantiations rationalized to six: one per domain, one per enterprise. Each bounded
context owned by a single Organization Unit with enterprise-wide authority.

## Bounded Context Decomposition

### 1. Customer Domain
**Organization Unit:** Unified Customer Management
**Function:** Customer onboarding, identity resolution, relationship management, lifecycle tracking, cross-sell orchestration
**Business Service:** Unified customer record service, canonical identity service, communication preference service
**Application Service:** Single CRM platform, unified CDP, governed identity resolution service
**Data Entity:** Customer, Party, Contact, Preference (canonical models declared)
**Logical Data Component:** Enterprise customer master; single MDM authority; cross-entity identity resolution automated
**Target state condition:** One CRM, one customer master, one identity model. Cross-sell enabled.

### 2. Product Domain
**Organization Unit:** Unified Product Management
**Function:** Product definition, unified catalog management, harmonized pricing, configuration, lifecycle governance
**Business Service:** Unified product catalog service, governed pricing service, product configuration service
**Application Service:** Single PIM platform, unified pricing engine
**Data Entity:** Product, SKU, Price, Configuration, Entitlement (canonical taxonomy declared)
**Logical Data Component:** Enterprise product master; single taxonomy authority
**Target state condition:** One product catalog, one taxonomy, one pricing engine.

### 3. Finance Domain
**Organization Unit:** Unified Finance and Accounting
**Function:** Unified general ledger management, rationalized AP/AR, governed financial close, consolidated regulatory reporting
**Business Service:** Unified ledger service, governed close orchestration service, consolidated reporting service
**Application Service:** Single ERP platform, unified close management, single reporting platform
**Data Entity:** Account, Journal Entry, Cost Center, Legal Entity, Regulatory Report (unified chart of accounts)
**Logical Data Component:** Enterprise financial master; unified chart of accounts; legal entity hierarchy rationalized
**Target state condition:** One ERP, one chart of accounts. Consolidation reporting automated.

### 4. Integration Domain
**Organization Unit:** Unified Enterprise Architecture and Integration Engineering
**Function:** Governed API management, enterprise event routing, canonical data synchronization, integration standards enforcement
**Business Service:** Enterprise integration brokering service, governed API gateway service, canonical event bus service
**Application Service:** Single enterprise integration platform, unified API gateway, governed message broker
**Data Entity:** Message, Event, API Contract, Integration Endpoint (canonical integration registry declared)
**Logical Data Component:** Enterprise integration registry; all endpoints governed; no ungoverned point-to-point
**Target state condition:** One integration platform, one API gateway, one governed registry.

### 5. Human Capital Domain
**Organization Unit:** Unified Human Resources
**Function:** Unified workforce management, rationalized payroll, harmonized benefits, governed talent acquisition
**Business Service:** Unified HR record service, single payroll service, harmonized benefits service
**Application Service:** Single HRIS platform, unified payroll platform, governed ATS
**Data Entity:** Employee, Position, Compensation, Benefit, Organization (unified workforce model)
**Logical Data Component:** Enterprise employee master; unified compensation model; org design governed
**Target state condition:** One HRIS, one payroll system, one compensation model.

### 6. Technology and Infrastructure Domain
**Organization Unit:** Unified IT Operations and Platform Engineering
**Function:** Unified infrastructure provisioning, governed platform management, enterprise security operations, unified service management
**Business Service:** Enterprise infrastructure service, unified security service, governed platform service, single ITSM service
**Application Service:** Unified cloud platform, single ITSM tool, rationalized security toolchain
**Data Entity:** Asset, Configuration Item, Incident, Service Request (unified CMDB declared)
**Logical Data Component:** Enterprise CMDB; unified asset registry; single identity provider spans combined enterprise
**Target state condition:** One cloud governance model, one ITSM platform, one identity provider.

## Cross-Subsystem Achievement Profile

| Dimension | Target Condition |
|---|---|
| Subsystem instantiation | Six bounded contexts; one per domain; one per enterprise |
| Organization Unit authority | Single owner per domain; enterprise-wide scope |
| Data Entity canonical models | Declared and implemented across all six domains |
| Application Service governance | All services route through governed integration backbone |
| Integration topology | Single platform; no ungoverned point-to-point |
| Identity provider | Single provider; spans combined enterprise |

## Ossuary Notes

Six rationalized bounded contexts. One instantiation per domain. Bureau scoring uses
this pattern as the Subsystem rationalization completeness benchmark. Component
altitude target-state patterns must cohere against this document.