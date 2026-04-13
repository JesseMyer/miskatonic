---
ossuary_id: OSS-MA-COM-CUS-002
altitude: Component
domain: M&A Integration Architecture
state: Target State
output_type: Pattern
subsystem: Customer Domain
togaf_constructs:
  primary: [Application Service, Logical Application Component]
  secondary: [Physical Application Component, Data Entity, Interface, Control]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-002
---

# M&A Integration Architecture — Component Altitude — Customer Domain — Target State

## Application Component Inventory

**CRM Platform (Unified)** — Logical Application Component. Enterprise customer record management, unified relationship history, cross-entity communication logging. Enterprise-wide. ARB-governed. Canonical data model.
**Customer Data Platform (Unified)** — Logical Application Component. Enterprise customer profile unification, cross-entity segmentation. Enterprise-wide. Consent and preference model declared.
**Identity Resolution Service (Unified)** — Logical Application Component. Enterprise customer identity matching, automated deduplication, golden record management. Resolution rules declared and governed. Match quality metrics declared.
**Enterprise Customer Master (MDM)** — Logical Data Component. Single authoritative customer record store. Canonical models declared. Single named MDM authority. Golden record policy enforced.

## Interface Inventory (Governed)

| Interface | Owner | Protocol | Consumer | Governed |
|---|---|---|---|---|
| Enterprise CRM API | Unified CRM | REST, OAuth 2.0 | All governed consumers | Yes, ARB |
| CDP profile API | Unified CDP | REST | Marketing, analytics | Yes, ARB |
| Identity resolution API | Unified identity service | REST | CRM, CDP, integration backbone | Yes, ARB |
| Customer master feed | Enterprise MDM | Governed event stream | All customer data consumers | Yes, ARB |

## Data Entity Canonical Models

| Data Entity | MDM Authority | Resolution Status |
|---|---|---|
| Customer | Named Organization Unit | Resolved |
| Party | Named Organization Unit | Resolved |
| Contact | Named Organization Unit | Resolved |
| Preference | Named Organization Unit | Resolved; consent model included |

## Ossuary Notes

Target state enables cross-sell motion declared at System altitude. Identity resolution
service is the enabling construct. MDM authority declaration makes the Data Entity
canonical model defensible. Joint cross-sell closure criterion with OSS-MA-COM-PRD-002.