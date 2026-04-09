---
ossuary_id: OSS-MA-SYS-001
altitude: System
domain: M&A Integration Architecture
state: Current State
output_type: Pattern
togaf_constructs:
  primary: [Capability, Value Stream]
  secondary: [Course of Action, Organization Unit]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
---

# M&A Integration Architecture — System Altitude — Current State

## Motivational Layer

### Elicited (Aspirational)
Captured directly from client stakeholders. Represents stated intent: the strategic rationale for the acquisition as articulated by leadership. Recorded as-heard. Flagged: aspirational. Propaganda-risk annotation applied where elicited narrative diverges from documented evidence.

| Construct | Declaration |
|---|---|
| Driver | [Elicited from client: market expansion, capability acquisition, competitive defense, etc.] |
| Goal | [Elicited from client: revenue synergy, cost rationalization, market share, etc.] |
| Objective | [Elicited from client: measurable targets against each Goal] |

### Consumed (Curated)
Captured from requirements documentation, board materials, deal thesis, integration mandate. Represents the governed record of intent. Flagged: curated. Delta between elicited and consumed is a Bureau finding candidate.

| Construct | Declaration |
|---|---|
| Driver | [From documentation: deal thesis, strategic plan, board mandate] |
| Goal | [From documentation: synergy targets, integration KPIs] |
| Objective | [From documentation: measurable commitments made to board or regulators] |

## Organization Structure (As-Reported)
Captured day one. Represents what the client believes their organization is. Contradictions surfaced by capability and function analysis are Bureau findings, not corrections to this record.

| Entity | Type | Notes |
|---|---|---|
| [Acquirer org unit] | Organization Unit | As-reported |
| [Acquiree org unit] | Organization Unit | As-reported |
| [Shared/overlap units] | Organization Unit | Flagged for Subsystem decomposition |

## Capability Landscape
The combined enterprise presents a duplicated capability map. Both entities carry full stacks across core business domains. No rationalization has occurred. No authoritative capability model spans both entities.

- Capability redundancy is universal. Every core domain has at least two instantiations per legacy entity.
- Integration topology is ungoverned. Combined integration surface is not documented, not rationalized.
- Data ownership is contested. No canonical model declared. No authoritative source of record designated.
- Operating models diverge. Technology governance, architecture review, vendor management differ.
- Strategic alignment is assumed, not verified. Delta between elicited and consumed motivational layers is the first Bureau finding candidate.

## Value Streams (Conditional: Declare if Available)
Each Value Stream requires qualification before construct typing is confirmed. Vril qualification prompts govern this elicitation. Hold declaration until answered.

| Candidate | Triggering Capability | Qualification Required | Typed As |
|---|---|---|---|
| Customer Lifecycle | [Customer Management Capability] | What is the canonical customer entity for this client? | Value Stream or Process, pending |
| Product Fulfillment | [Product Administration Capability] | What is the terminal condition: legal handoff, satisfaction state, or regulated delivery? | Value Stream, Business Service, or Contract, pending |
| Financial Close | [Finance & Accounting Capability] | Is this driven by regulatory obligation or internal governance? | Process with Control and Contract implications, pending |

## Architectural Risk Profile

| Risk | Severity | Broken Construct Relationship | Bureau Suggestion Triggered |
|---|---|---|---|
| Capability Collision | Critical | Capability: no single delivering Work Package declared | Yes |
| Integration Surface Opacity | Critical | Application Service: ungoverned; no Logical Application Component authority | Yes |
| Data Sovereignty Conflict | High | Data Entity: no authoritative Logical Data Component declared | Yes |
| Governance Vacuum | High | Control: absent; no Course of Action governing combined enterprise | Yes |
| Shadow Integration Risk | Medium | Application Service: exists outside governed Logical Application Component boundary | Yes |
| Motivational Delta | High | Driver/Goal: elicited and curated records diverge | Yes |

## Ossuary Notes
Foundational current-state exemplar for M&A at System altitude. All Subsystem-altitude current-state patterns must cohere against this document. Bureau scoring at System altitude uses this pattern as the baseline deviation reference. Pelagic Wave 0 initiated from this state. Ossuary reference tier scoped to declared region before Bureau suggestions are generated.
