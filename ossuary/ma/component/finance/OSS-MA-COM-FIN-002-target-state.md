---
ossuary_id: OSS-MA-COM-FIN-002
altitude: Component
domain: M&A Integration Architecture
state: Target State
output_type: Pattern
subsystem: Finance Domain
togaf_constructs:
  primary: [Application Service, Logical Application Component]
  secondary: [Physical Application Component, Data Entity, Interface, Control]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-002
---

# M&A Integration Architecture — Component Altitude — Finance Domain — Target State

## Application Component Inventory

**ERP Platform (Unified)** — Logical Application Component. Enterprise general ledger management, governed AP and AR, unified fixed assets, governed financial close orchestration. Enterprise-wide. ARB-governed. Canonical chart of accounts enforced.
**Financial Close Management Platform (Unified)** — Logical Application Component. Enterprise close task orchestration, governed reconciliation management, unified close calendar. Enterprise-wide. Close calendar governing enterprise-wide.
**Regulatory Reporting Platform (Unified)** — Logical Application Component. Enterprise statutory reporting, unified tax reporting, governed regulatory filing management. Enterprise-wide. All jurisdictional obligations declared and governed.
**Enterprise Financial Master (MDM)** — Logical Data Component. Single authoritative financial record store. Canonical chart of accounts enforced. Legal entity hierarchy ratified by legal and tax. Single named MDM authority.

## Interface Inventory (Governed)

| Interface | Owner | Protocol | Consumer | Governed |
|---|---|---|---|---|
| Enterprise ERP API | Unified ERP | REST, OAuth 2.0 | All governed consumers | Yes, ARB |
| Financial data feed | Unified ERP | Governed event stream | Reporting, integration backbone | Yes, ARB |
| Close status feed | Close management platform | REST | Reporting, ERP | Yes, ARB |
| Regulatory submission feeds | Regulatory reporting platform | Jurisdiction-specific | Regulatory bodies | Yes, ARB |
| Consolidation feed | Unified ERP | Automated | Group finance reporting | Yes, ARB |

## Data Entity Canonical Models

| Data Entity | MDM Authority | Resolution Status |
|---|---|---|
| Account | Named Organization Unit | Resolved; legal and tax ratified |
| Cost Center | Named Organization Unit | Resolved |
| Legal Entity | Named Organization Unit | Resolved; legal and tax ratified |
| Journal Entry | Named Organization Unit | Resolved |
| Regulatory Report | Named Organization Unit | Resolved; all jurisdictions declared |

## Ossuary Notes

Consolidation automation is the primary System-altitude outcome. Financial Flow Value
Stream only achievable when consolidation feed is automated and chart of accounts unified.
Legal and tax ratification of legal entity hierarchy is a non-negotiable prerequisite.
Bureau does not close this pattern without documented evidence of that ratification.