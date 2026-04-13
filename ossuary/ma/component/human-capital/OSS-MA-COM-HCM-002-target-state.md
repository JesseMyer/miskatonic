---
ossuary_id: OSS-MA-COM-HCM-002
altitude: Component
domain: M&A Integration Architecture
state: Target State
output_type: Pattern
subsystem: Human Capital Domain
togaf_constructs:
  primary: [Application Service, Logical Application Component]
  secondary: [Physical Application Component, Data Entity, Interface, Control]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-002
---

# M&A Integration Architecture — Component Altitude — Human Capital Domain — Target State

## Application Component Inventory

**HRIS Platform (Unified)** — Logical Application Component. Enterprise employee record management, governed position management, unified organizational hierarchy, enterprise workforce reporting. Enterprise-wide. ARB-governed. Canonical employee data model enforced.
**Payroll Platform (Unified)** — Logical Application Component. Enterprise payroll calculation, governed tax withholding, unified payslip generation, multi-jurisdiction payroll governance where applicable. Enterprise-wide. Payroll rules governed per jurisdiction.
**Benefits Administration Platform (Unified)** — Logical Application Component. Enterprise benefits enrollment, governed plan management, rationalized carrier integration, unified life event processing. Enterprise-wide. Rationalized benefit plans declared. Carrier contracts renegotiated at enterprise scale.
**Talent Acquisition System (Unified)** — Logical Application Component. Enterprise job requisition management, governed candidate tracking, unified offer management. Enterprise-wide.
**Enterprise HR Master (MDM)** — Logical Data Component. Single authoritative employee record store. Canonical compensation model enforced. Organizational hierarchy ratified by HR and legal. Single named MDM authority.

## Interface Inventory (Governed)

| Interface | Owner | Protocol | Consumer | Governed |
|---|---|---|---|---|
| Enterprise HRIS API | Unified HRIS | REST, OAuth 2.0 | All governed consumers | Yes, ARB |
| Workforce feed | Unified HRIS | Governed event stream | Payroll, benefits, ERP backbone | Yes, ARB |
| Payroll feed | Unified payroll | Governed batch | Unified ERP | Yes, ARB |
| Tax filing submissions | Unified payroll | Jurisdiction-specific | Tax authorities | Yes, ARB |
| Carrier feeds | Unified benefits | EDI (rationalized) | Benefits carriers | Yes, ARB |

## Data Entity Canonical Models

| Data Entity | MDM Authority | Resolution Status |
|---|---|---|
| Employee | Named Organization Unit | Resolved |
| Position | Named Organization Unit | Resolved; HR ratified |
| Organization | Named Organization Unit | Resolved; HR and legal ratified |
| Compensation | Named Organization Unit | Resolved; HR, legal, finance ratified |
| Benefit | Named Organization Unit | Resolved; carrier contracts renegotiated |

## Ossuary Notes

Compensation model ratification by HR, legal, and finance is a non-negotiable prerequisite.
Benefit plan rationalization requires carrier contract renegotiation: this is a procurement
and legal activity with architectural consequences. Bureau does not close this pattern
without documented evidence of HR and legal ratification.