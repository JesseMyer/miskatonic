---
ossuary_id: OSS-REF-001
altitude: platform
domain: all
output_type: reference tier design
bureau_calibration: false
region: routing key declared per engagement
adm_phase: omit
---

# Ossuary Reference Tier

## Purpose

The Ossuary reference tier is the governed corpus of external knowledge that Bureau draws
from when generating suggestions. It is distinct from the Ossuary pattern corpus: patterns
are synthetic EA exemplars produced by the platform; references are external sources
consumed by the platform.

Every Bureau suggestion cites a reference. Every reference declares its source, tier,
region, and date. No undeclared reference influences a finding or suggestion.

## Three Sub-Tiers

### Tier 1: Framework

Governed, stable, citable standards bodies and methodology frameworks. Slow-changing.
High authority. Region-independent unless the framework is jurisdiction-specific.

Examples: TOGAF, SABSA, COBIT, ISO 22301, NIST, 23 NYCRR 500, NY State IT policy, DORA, FedRAMP.

Characteristics:
- Version-declared: every reference names the specific version in use.
- Jurisdiction-aware: regulatory frameworks declare their jurisdiction explicitly.
- Highest citation authority in Bureau suggestions.
- Supersession tracked: when a framework version is superseded, existing citations are flagged for review.

### Tier 2: Analyst

Opinionated, dated, vendor-influenced market analysis. Authoritative within its publication
window. Region and market weighted.

Examples: Gartner Magic Quadrant, Forrester Wave, IDC MarketScape, sector-specific analyst coverage.

Characteristics:
- Date-stamped: publication quarter and year declared on every citation.
- Region-weighted: Gartner and Forrester are western, English-language, US-market-weighted by default.
- Lower citation authority than Tier 1 for compliance findings.
- Higher citation authority than Tier 1 for vendor evaluation and technology bakeoff findings.
- Shelf life declared: analyst citations older than 24 months are flagged as potentially stale.

### Tier 3: Market Signal

Raw, current, requires interpretation. Open market data and industry signal sources.

Examples: Crunchbase, SEC filings, public earnings data, open regulatory filings, industry association publications.

Characteristics:
- Currency-dependent: value degrades rapidly. Date of retrieval declared on every citation.
- Interpretation required: Bureau cites market signal as supporting evidence, always paired with Tier 1 or Tier 2.
- Never standalone: a Bureau suggestion grounded only in Tier 3 is a malformed suggestion.
- Region-native: market signal sources are inherently regional.

## Region Routing

Region is declared in Vril frontmatter per engagement. Bureau resolves the active reference
set from the declared region. No undeclared region defaults to a western reference set silently.

| Region Declaration | Tier 1 Default | Tier 2 Default | Tier 3 Default |
|---|---|---|---|
| US, NY regulatory jurisdiction | TOGAF, 23 NYCRR 500, NY State IT | Gartner, Forrester | Crunchbase, SEC |
| US, federal | TOGAF, NIST, FedRAMP | Gartner, Forrester | USASpending, SEC |
| EU | TOGAF, DORA, GDPR | Gartner, Forrester, PAC | Eurostat, ESMA filings |
| APAC | TOGAF, regional regulatory | IDC, local analyst | Regional exchange filings |
| MENA | TOGAF, jurisdiction-specific | Regional analyst | Regional regulatory filings |
| Global | TOGAF, ISO standards only | Omitted unless declared | Omitted unless declared |

Region declarations are additive: an engagement can declare multiple regions.

## API Integration Contract

The reference tier is designed for API-backed population at a later phase. Every reference
entry exposes:

```json
{
  "reference_id": "REF-[tier]-[source]-[id]",
  "tier": "1 | 2 | 3",
  "source": "source name",
  "region": ["region declaration"],
  "jurisdiction": "jurisdiction if applicable",
  "version": "version or publication date",
  "retrieved": "date of retrieval or last verified",
  "url": "source URL if publicly accessible",
  "summary": "one sentence describing the reference",
  "superseded_by": "reference_id if superseded, null if current"
}
```

Manual population at proof of concept stage. API integration replaces manual population
in Phase 4. The contract does not change; the population mechanism does.

## Governing Rules

- No Bureau suggestion cites an undeclared reference.
- No Tier 3 citation appears without a paired Tier 1 or Tier 2 citation.
- No analyst citation older than 24 months is used without a staleness flag.
- No western reference set is applied to a non-western engagement without explicit architect override.
- Superseded framework versions are flagged, not silently replaced.
- Every reference entry is versioned in Grimoire.

## Ossuary Notes

This document governs the reference tier structure. Population of each sub-tier is a
separate build activity. Tier 1 framework references for M&A and BCDR domains are the
first population targets. Bureau scoring rubric design in Phase 2 declares which tier
has citation authority for which finding type. API integration layer is Phase 4 scope.

That is all 29 artifacts. Give Cursor this entire block as its source material and point it at the file list in the previous instruction prompt. It has everything it needs.give me that in one message so it has what it needs11:57 AMHere is everything Cursor needs in one message. Copy and paste this entire block directly into Cursor's agent prompt.

You are working in the Miskatonic EA platform repo at the root level.
Task: create the following directory structure and files, populate each file with the exact content provided below, then commit and push to main.
Step 1: Create directory structure.
mkdir -p ossuary/ma/system
mkdir -p ossuary/ma/subsystem
mkdir -p ossuary/ma/component/integration
mkdir -p ossuary/ma/component/customer
mkdir -p ossuary/ma/component/product
mkdir -p ossuary/ma/component/finance
mkdir -p ossuary/ma/component/human-capital
mkdir -p ossuary/ma/component/technology
mkdir -p ossuary/bcdr/system
mkdir -p vril
mkdir -p ossuary-reference-tier
Step 2: Create each file below with exact filename and exact content shown. Do not truncate, summarize, or modify any content. Write every file exactly as shown.
Step 3: After all files are written, run:
git add .
git commit -m "Phase 1: Ossuary M&A corpus complete at System, Subsystem, and Component altitude. BCDR System altitude illustrative. Vril qualification prompt type. Ossuary reference tier design. 29 governed artifacts. Zero human-written code."
git push origin main

FILE: ossuary/ma/system/OSS-MA-SYS-001-current-state.md
markdown---
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

FILE: ossuary/ma/system/OSS-MA-SYS-002-target-state.md
markdown---
ossuary_id: OSS-MA-SYS-002
altitude: System
domain: M&A Integration Architecture
state: Target State
output_type: Pattern
togaf_constructs:
  primary: [Capability, Value Stream]
  secondary: [Course of Action, Organization Unit, Control]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
---

# M&A Integration Architecture — System Altitude — Target State

## Motivational Layer

### Resolved
At target state, the delta between elicited and consumed motivational records has been adjudicated. A single governed motivational record exists. Bureau finding from current state is closed.

| Construct | Declaration |
|---|---|
| Driver | [Resolved: single authoritative statement of strategic driver] |
| Goal | [Resolved: rationalized synergy and integration goals] |
| Objective | [Resolved: measurable targets, board-ratified] |
| Measure | [Declared: performance criteria tracking each Objective] |

## Organization Structure (Rationalized)
The as-reported org structure from current state has been reconciled against capability and function analysis. A single rationalized Organization Unit map governs the combined enterprise.

| Entity | Type | Disposition |
|---|---|---|
| [Unified org unit] | Organization Unit | Rationalized; governs combined enterprise |
| [Dissolved units] | Organization Unit | Decommissioned; Grimoire record closed |
| [Absorbed units] | Organization Unit | Merged into unified structure; traceability maintained |

## Capability Landscape
The integrated enterprise operates a single rationalized capability map. Redundant capabilities resolved through documented disposition: retain, replace, consolidate, or decommission. Every capability has a single authoritative instantiation.

- Capability rationalization is complete. One authoritative system of record per capability domain.
- Integration architecture is governed. Single enterprise integration platform as canonical backbone.
- Master data is authoritative. Canonical models declared and implemented. Single MDM authority per domain.
- Operating model is unified. Single governance structure, ARB, vendor management, and delivery methodology.
- Motivational alignment is verified. Elicited and curated records reconciled. Technology strategy unified.

## Value Streams (Resolved)
Qualification questions answered. Construct typing confirmed. Value Streams fully declared with triggering Capabilities named.

| Value Stream | Triggering Capability | Terminal Condition | Typed As |
|---|---|---|---|
| Customer Lifecycle | [Unified Customer Management Capability] | [Declared per engagement] | [Confirmed construct] |
| Product Fulfillment | [Unified Product Administration Capability] | [Declared per engagement] | [Confirmed construct] |
| Financial Close | [Unified Finance & Accounting Capability] | [Declared per engagement] | [Confirmed construct] |

## Architectural Achievement Profile

| Construct | Target Condition |
|---|---|
| Capability | Single rationalized map; one instantiation per domain |
| Value Stream | Fully typed; triggering Capabilities named; terminal conditions declared |
| Organization Unit | Rationalized; single governed structure |
| Control | Unified ARB; cross-enterprise standards enforcement |
| Course of Action | Single technology strategy; investment allocation governed |
| Data Entity | Authoritative MDM per domain; automated identity resolution |

## Ossuary Notes
System-altitude target-state exemplar for M&A. All Subsystem-altitude target-state patterns must cohere against this document. Bureau scoring uses this pattern as the rationalization completeness benchmark. Pelagic final wave closure validated against this state. Ossuary reference tier scoped to declared region.

FILE: ossuary/ma/system/OSS-MA-SYS-003-transition-state.md
markdown---
ossuary_id: OSS-MA-SYS-003
altitude: System
domain: M&A Integration Architecture
state: Transition State
output_type: Pattern
togaf_constructs:
  primary: [Capability, Course of Action, Work Package]
  secondary: [Value Stream, Organization Unit, Control]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
---

# M&A Integration Architecture — System Altitude — Transition State

## Context
The governed passage from OSS-MA-SYS-001 to OSS-MA-SYS-002. Coexistence is the operating condition. Progress is measured by wave exit criteria. Bureau validates every wave gate before advancement. Grimoire records every disposition decision.

## Wave Structure

### Wave 0 — Discovery and Stabilization
**Primary constructs:** Capability, Organization Unit, Driver, Goal
**Entry condition:** Acquisition close. Legal consolidation complete.
**Exit criteria:**
- Combined capability map produced and validated.
- Integration surface documented.
- Motivational layer dual-track capture complete; delta identified.
- Organization Unit as-reported map complete.
- Value Stream qualification questions issued via Vril.
- Interim ARB constituted; governance vacuum finding formally opened.
- Risk register populated; Bureau construct mapping applied to all findings.

**Bureau constraint:** No rationalization decisions in Wave 0. Discovery precedes disposition. Enforced.

### Wave 1 — Foundation and Governance
**Primary constructs:** Control, Course of Action, Application Service
**Entry condition:** Wave 0 exit criteria Bureau-validated.
**Exit criteria:**
- Enterprise integration platform selected; foundational deployment complete.
- Unified ARB constituted; Control construct instantiated across combined enterprise.
- Canonical capability model ratified.
- Value Stream qualification questions answered; construct typing confirmed.
- Customer MDM authority declared; identity resolution pilot complete.
- Motivational delta finding: remediation in progress.
- Region-scoped Ossuary reference tier active; Bureau suggestions generating.

**Coexistence:** Both legacy integration topologies operational. New backbone operating in parallel. No legacy decommission in Wave 1.

### Wave 2 — Rationalization
**Primary constructs:** Work Package, Capability, Data Entity
**Entry condition:** Wave 1 exit criteria Bureau-validated.
**Exit criteria:**
- Capability disposition decisions executed for all Tier 1 systems.
- Integration migration to backbone: 60% or greater of legacy volume.
- MDM authority declared for all primary Data Entity domains.
- First decommission tranche complete; retired system registry current.
- Unified Organization Unit map published; entity-local structures dissolved.
- Motivational delta finding: closed; single governed motivational record declared.

**Coexistence:** Disposition-queue systems under freeze. No new development, no new integrations. Migration managed by backbone routing layer.

### Wave 3 — Closure and Verification
**Primary constructs:** Capability, Value Stream, Control, Measure
**Entry condition:** Wave 2 exit criteria Bureau-validated.
**Exit criteria:**
- All capability disposition decisions executed and verified.
- Integration backbone carries 100% of governed traffic.
- All legacy point-to-point integrations decommissioned.
- Value Streams verified against resolved target-state declarations.
- Measures tracking all Objectives: active and reporting.
- Target-state architecture validated at all five altitudes against OSS-MA-SYS-002.
- Grimoire transition record closed; Pelagic passage declared complete.

## Cross-Wave Risk Register

| Risk | Wave | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|---|
| Wave advancement without exit criteria validation | All | Critical | Control: wave gate unenforced | Yes |
| Disposition-queue systems accumulating new integrations | 1,2 | High | Control: freeze policy absent | Yes |
| MDM authority contested mid-wave | 1,2 | High | Data Entity: no authoritative Logical Data Component | Yes |
| Discovery gaps surfacing during rationalization | 2 | Medium | Capability: inventory incomplete at Wave 0 close | Yes |
| Value Stream typing unresolved at Wave 2 entry | 2 | High | Value Stream: qualification questions unanswered | Yes |
| Target-state coherence failure at lower altitudes | 3 | High | Work Package: altitude coherence unverified | Yes |
| Motivational delta unresolved at Wave 2 entry | 2 | High | Driver/Goal: elicited and curated records not reconciled | Yes |

## Ossuary Notes
Governs System-altitude transition for M&A. Pelagic roadmap templates derived from this wave structure. Bureau wave-gate scoring rubrics reference exit criteria as scoring baseline. All Subsystem-altitude transition patterns must declare wave alignment against this document. Ossuary reference tier scoped to declared region.

FILE: ossuary/ma/subsystem/OSS-MA-SUB-001-current-state.md
markdown---
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
Decomposition of OSS-MA-SYS-001 into bounded contexts. One System, many Subsystems. At current state, each Subsystem exists in duplicate: one instantiation per legacy entity. Twelve total Subsystem instantiations govern the combined enterprise at close.

## Bounded Context Decomposition

### 1. Customer Domain
**Organization Unit:** Customer Management, per entity
**Function:** Customer onboarding, identity resolution, relationship management, lifecycle tracking
**Business Service:** Customer record management, identity verification, communication preference management
**Application Service:** CRM platform (entity-local), CDP (where present), identity resolution service
**Data Entity:** Customer, Party, Contact, Preference
**Logical Data Component:** Entity-local customer master; no cross-entity canonical model declared
**Current state condition:** Two CRM platforms, two customer masters, non-overlapping identity models. Cross-entity customer recognition is manual.
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
**Current state condition:** Two ERP platforms, two charts of accounts. Consolidation reporting is manual reconciliation.
**Qualification holds:** Financial close construct type; regulatory reporting obligation.

### 4. Integration Domain
**Organization Unit:** Enterprise Architecture or Integration Engineering, per entity
**Function:** API management, event routing, data synchronization, integration governance
**Business Service:** Integration brokering service, API gateway service, event bus service
**Application Service:** ESB or iPaaS platform (entity-local), API gateway (entity-local), message broker
**Data Entity:** Message, Event, API Contract, Integration Endpoint
**Logical Data Component:** Entity-local integration registry; no cross-entity integration inventory
**Current state condition:** Two ungoverned integration topologies. Shadow integrations undocumented.
**Qualification holds:** Integration governance authority; shadow integration inventory required before Component descent.

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
**Current state condition:** Two cloud environments, two ITSM platforms, two security toolchains. No unified identity provider.
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
Six bounded contexts declared. Twelve total Subsystem instantiations at current state. Qualification holds declared per domain; batch issued at this altitude boundary before Component descent. Component altitude patterns scoped per bounded context: one Component pattern set per domain. Ossuary reference tier scoped to declared region.

FILE: ossuary/ma/subsystem/OSS-MA-SUB-002-target-state.md
markdown---
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
Decomposition of OSS-MA-SYS-002 into rationalized bounded contexts. Twelve Subsystem instantiations rationalized to six: one per domain, one per enterprise. Each bounded context owned by a single Organization Unit with enterprise-wide authority.

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
Six rationalized bounded contexts. One instantiation per domain. Bureau scoring uses this pattern as the Subsystem rationalization completeness benchmark. Component altitude target-state patterns must cohere against this document.

FILE: ossuary/ma/subsystem/OSS-MA-SUB-003-transition-state.md
markdown---
ossuary_id: OSS-MA-SUB-003
altitude: Subsystem
domain: M&A Integration Architecture
state: Transition State
output_type: Pattern
togaf_constructs:
  primary: [Function, Course of Action, Work Package, Control]
  secondary: [Business Service, Application Service, Organization Unit]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
---

# M&A Integration Architecture — Subsystem Altitude — Transition State

## Context
The governed passage from OSS-MA-SUB-001 to OSS-MA-SUB-002. Wave alignment declared against OSS-MA-SYS-003. Disposition sequencing is domain-priority ordered: Integration Domain first, Customer and Product second, Finance third, Human Capital and Technology fourth.

## Wave Alignment

### Wave 0 — Discovery and Subsystem Inventory
**Wave alignment:** OSS-MA-SYS-003 Wave 0
**Primary constructs:** Function, Organization Unit, Data Entity
**Exit criteria:**
- All six bounded contexts documented per entity: twelve Subsystem inventories complete.
- Function sets mapped per Organization Unit per entity.
- Business Service inventory complete per domain per entity.
- Application Service topology documented; all point-to-point integrations inventoried.
- Data Entity ownership declared per domain per entity.
- Qualification holds batched at Subsystem altitude boundary.
- Shadow integration discovery complete for Integration Domain before Wave 1 entry.
**Coexistence:** Observation only. No disposition decisions. No Function rationalization.

### Wave 1 — Foundation and Domain Authority
**Wave alignment:** OSS-MA-SYS-003 Wave 1
**Primary constructs:** Organization Unit, Control, Course of Action
**Exit criteria:**
- Integration Domain: enterprise integration platform selected; unified Organization Unit authority declared; backbone foundational deployment complete.
- Customer Domain: unified Organization Unit declared; customer MDM authority named; identity resolution hold resolved.
- Product Domain: unified Organization Unit declared; product taxonomy hold resolved; canonical taxonomy draft published.
- Finance Domain: unified Organization Unit declared; financial close construct type hold resolved.
- Human Capital and Technology Domains: unified Organization Unit declared; key authority holds resolved.
- All Subsystem qualification holds resolved and recorded in Grimoire before Wave 2 entry.
**Coexistence:** Twelve Subsystem instantiations remain operational. Integration backbone in parallel; no legacy migration in Wave 1.

### Wave 2 — Rationalization by Domain Priority
**Wave alignment:** OSS-MA-SYS-003 Wave 2
**Primary constructs:** Work Package, Function, Data Entity
**Priority 1: Integration Domain** — backbone carries all new integrations; 60% legacy volume migrated; unified registry governing.
**Priority 2: Customer and Product** — customer MDM migration initiated; product taxonomy harmonized; CRM migration initiated.
**Priority 3: Finance** — chart of accounts harmonization; legal entity hierarchy rationalized; ERP consolidation initiated.
**Priority 4: Human Capital and Technology** — HRIS consolidation initiated; identity provider consolidation initiated; CMDB unification initiated.
**Coexistence:** Disposition-queue systems under freeze. No new development, no new integrations.

### Wave 3 — Closure per Domain
**Wave alignment:** OSS-MA-SYS-003 Wave 3
**Primary constructs:** Control, Measure, Work Package
**Domain closure sequence:** Integration, Customer, Product, Finance, Human Capital, Technology.
**Final exit criteria:**
- All twelve legacy Subsystem instantiations decommissioned or absorbed; six rationalized Subsystems governing.
- All qualification holds closed in Grimoire.
- Subsystem altitude validated against OSS-MA-SUB-002.
- Component altitude descent permitted per domain post-closure.

## Cross-Subsystem Transition Risk Register

| Risk | Wave | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|---|
| Integration backbone delayed: all domain migrations blocked | 1 | Critical | Course of Action: integration priority sequencing violated | Yes |
| Qualification holds unresolved at Wave 1 close | 1 | High | Control: wave gate unenforced without hold resolution | Yes |
| Disposition-queue systems accumulating new integrations | 2 | High | Control: freeze policy absent or unenforced by ARB | Yes |
| Domain closure attempted out of sequence | 3 | High | Work Package: dependency on integration backbone closure violated | Yes |
| Legacy Subsystem decommissioned before migration validated | 2,3 | Critical | Function: service continuity broken; no rollback declared | Yes |
| Grimoire qualification hold records incomplete at Wave 3 | 3 | Medium | Control: Subsystem closure declared without evidence | Yes |

## Ossuary Notes
Integration Domain disposition priority is a platform-enforced sequencing rule. Bureau wave-gate scoring uses domain closure sequence as the primary scoring dimension. All Component altitude patterns must declare parent Subsystem and wave alignment before admission to the Ossuary corpus.

FILE: ossuary/ma/component/integration/OSS-MA-COM-INT-001-current-state.md
markdown---
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

## Context
Decomposition of the Integration Domain bounded context from OSS-MA-SUB-001 to Component altitude. Two legacy integration architectures fully visible. Neither is rationalized. Neither is governed cross-entity.

## Application Component Inventory

### Entity A
**ESB or iPaaS Platform** — Logical Application Component. Message routing, transformation, orchestration. Entity-local. Interfaces: SOAP, REST, proprietary messaging protocol. Shadow integrations undocumented; discovery required.
**API Gateway** — Logical Application Component. API lifecycle management, traffic routing, authentication enforcement. Entity-local. Interfaces: REST, OAuth 2.0. No cross-entity API standards.
**Message Broker** — Logical Application Component. Asynchronous event distribution, queue management. Entity-local. Interfaces: AMQP, proprietary topic structure. Topic taxonomy ungoverned.
**Integration Registry** — Logical Application Component (absent or informal). Spreadsheet or wiki. Not fit for purpose at combined enterprise scale.

### Entity B
**ESB or iPaaS Platform** — Logical Application Component. Entity-local. Interfaces: REST, proprietary messaging protocol. May be same vendor as Entity A or different; declare per engagement. Shadow integrations undocumented.
**API Gateway** — Logical Application Component. Entity-local. Interfaces: REST, OAuth 2.0. Standards non-aligned with Entity A.
**Message Broker** — Logical Application Component. Entity-local. Interfaces: AMQP or JMS; may differ from Entity A. Topic taxonomy non-aligned with Entity A.
**Integration Registry** — Logical Application Component (absent or informal). Not fit for purpose; same condition as Entity A.

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

Critical finding: No governed cross-entity interface exists at close. Any cross-entity data movement is point-to-point, ungoverned, and undocumented until shadow integration discovery is complete.

## Shadow Integration Risk
Shadow integrations are undocumented Application Services operating outside the governed integration topology. They cannot be decommissioned without discovery. They cannot be migrated without documentation. They cannot be governed without inventory. Shadow integration discovery is a Wave 0 exit criterion per OSS-MA-SUB-003.

## Architectural Risk Profile

| Risk | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|
| Shadow integrations undiscovered | Critical | Application Service: ungoverned services outside Logical Application Component boundary | Yes |
| No cross-entity interface exists | Critical | Interface: no governed cross-entity integration surface declared | Yes |
| Dual integration registries informal | High | Logical Application Component: no authoritative endpoint inventory | Yes |
| Protocol non-alignment between entities | High | Interface: AMQP vs JMS; SOAP vs REST; non-interoperable without transformation | Yes |
| API standards non-aligned | Medium | Logical Application Component: OAuth and REST implementations non-comparable | Yes |
| Topic taxonomy non-aligned | Medium | Logical Application Component: event consumers cannot span entities | Yes |

## Ossuary Notes
First Component altitude pattern in the Ossuary corpus. Establishes Component pattern structure for all subsequent domain Component patterns. Bureau scores against interface governance dimension as the primary scoring axis. Shadow integration discovery must be complete before Component descent for dependent domains is permitted.

FILE: ossuary/ma/component/integration/OSS-MA-COM-INT-002-target-state.md
markdown---
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

## Context
Decomposition of the Integration Domain bounded context from OSS-MA-SUB-002 to Component altitude. One enterprise integration platform governs all integration traffic. No ungoverned point-to-point survives.

## Application Component Inventory

**ESB or iPaaS Platform (Unified)** — Logical Application Component. Enterprise message routing, canonical transformation, governed orchestration. Enterprise-wide; cloud-native preferred. Interfaces: REST, AMQP, governed event schema. ARB-governed. All endpoints declared and versioned in enterprise integration registry.
**API Gateway (Unified)** — Logical Application Component. Enterprise API lifecycle management, governed traffic routing, canonical OAuth 2.0 authentication. Enterprise-wide. ARB-governed. Versioning policy declared. Deprecation process governed.
**Message Broker (Unified)** — Logical Application Component. Enterprise asynchronous event distribution, governed queue and topic management. Enterprise-wide. Interfaces: AMQP (canonical protocol declared). Canonical topic taxonomy declared and enforced. No ungoverned topics permitted.
**Enterprise Integration Registry** — Logical Application Component. Authoritative integration endpoint inventory, dependency mapping, change impact analysis. Governed system of record. All endpoints declared, versioned, and dependency-mapped.

## Interface Inventory (Governed)

| Interface | Owner | Protocol | Consumer | Governed |
|---|---|---|---|---|
| Enterprise ESB inbound | Unified integration platform | REST, AMQP | All governed applications | Yes, ARB |
| Enterprise API Gateway | Unified integration platform | REST, OAuth 2.0 | All governed API consumers | Yes, ARB |
| Enterprise Message Broker | Unified integration platform | AMQP | All governed event consumers | Yes, ARB |

All interfaces are governed. No ungoverned interface exists in the target state. Any interface not in this inventory is a Bureau finding.

## Point-to-Point Topology
No point-to-point integrations exist in the target state. Any surviving point-to-point is a critical Bureau finding and a Wave 3 closure blocker.

## Architectural Achievement Profile

| Construct | Target Condition |
|---|---|
| Logical Application Component | Single governed instance per integration function |
| Interface | All interfaces governed; canonical protocols declared |
| Application Service | All services route through enterprise integration platform |
| Control | ARB governs all integration changes; standards enforced |
| Integration Registry | Authoritative; all endpoints declared and versioned |

## Ossuary Notes
Target state closes all current-state findings for Integration Domain at Component altitude. Enterprise integration platform is the dependency anchor for all other domain Component migrations. No domain Component target state is achievable without this pattern's conditions being met first.

FILE: ossuary/ma/component/integration/OSS-MA-COM-INT-003-transition-state.md
markdown---
ossuary_id: OSS-MA-COM-INT-003
altitude: Component
domain: M&A Integration Architecture
state: Transition State
output_type: Pattern
subsystem: Integration Domain
togaf_constructs:
  primary: [Work Package, Course of Action, Control]
  secondary: [Application Service, Logical Application Component, Interface]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-003
---

# M&A Integration Architecture — Component Altitude — Integration Domain — Transition State

## Context
The governed passage from OSS-MA-COM-INT-001 to OSS-MA-COM-INT-002. Integration backbone must be operational before any other domain Component migration begins. This is the platform's highest-priority transition pattern.

## Wave Alignment

### Wave 0 — Shadow Integration Discovery
**Primary constructs:** Application Service, Interface, Logical Application Component
**Exit criteria:**
- All point-to-point integrations inventoried per entity: source, target, protocol, data payload, frequency, owner.
- All shadow integrations discovered and documented: owner identified, consuming application identified, data payload classified.
- Combined interface inventory complete: all Application Services and Interfaces declared in integration registry template.
- Protocol inventory complete: all protocols in use across both entities documented; non-alignment identified.
- Dependency map produced: which applications depend on which integration services; decommission sequencing implications identified.
- Topic taxonomy inventory complete: all message broker topics documented per entity; non-alignment identified.
**Constraint:** No platform selection in Wave 0. Discovery precedes vendor decision. Bureau-enforced.

### Wave 1 — Platform Selection and Backbone Deployment
**Primary constructs:** Logical Application Component, Course of Action, Control
**Exit criteria:**
- Enterprise integration platform selected: Technology Bakeoff methodology applied if multiple candidates; selection documented and ARB-ratified.
- Enterprise API gateway selected and deployed: canonical OAuth 2.0 implementation declared.
- Enterprise message broker selected and deployed: canonical AMQP implementation declared; topic taxonomy governance initiated.
- Enterprise integration registry deployed: all Wave 0 discovered endpoints entered; dependency map imported.
- ARB integration standards published: protocol standards, API versioning policy, topic taxonomy rules, onboarding process.
- Freeze policy activated: no new point-to-point permitted; new integrations route through backbone only.
- Parallel operation confirmed: both legacy platforms operational; backbone operational in parallel; no legacy traffic migrated in Wave 1.

### Wave 2 — Migration and Decommission Sequencing
**Primary constructs:** Work Package, Application Service, Interface
**Exit criteria:**
- Migration sequencing declared: integrations migrated in dependency order per Wave 0 dependency map.
- 60% of legacy point-to-point volume routed through enterprise backbone.
- Protocol transformation layer operational: SOAP to REST, JMS to AMQP transformations governed through backbone.
- Topic taxonomy harmonized: canonical topics operational; legacy topics deprecated on declared schedule.
- API versioning policy enforced: legacy API versions deprecated per published policy; consumers notified.
- First decommission tranche: lowest-risk legacy point-to-point integrations decommissioned after migration validated.

### Wave 3 — Full Migration and Legacy Decommission
**Primary constructs:** Control, Work Package, Measure
**Exit criteria:**
- 100% of governed integration traffic routes through enterprise backbone.
- All legacy point-to-point integrations decommissioned; retired endpoint registry current and complete.
- Both legacy ESB or iPaaS platforms decommissioned.
- Both legacy API gateways decommissioned.
- Both legacy message brokers decommissioned.
- Enterprise integration registry: authoritative; all active endpoints declared, versioned, and dependency-mapped.
- No surviving ungoverned interfaces: Bureau validation required before closure declared.
- Integration Domain Component altitude validated against OSS-MA-COM-INT-002.
- Dependent domain Component migrations: unblocked and sequencing confirmed.

## Component Transition Risk Register

| Risk | Wave | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|---|
| Shadow integrations undiscovered at Wave 0 close | 0 | Critical | Application Service: incomplete inventory; decommission sequencing impossible | Yes |
| Platform selected before discovery complete | 0,1 | High | Course of Action: vendor decision without full requirements | Yes |
| Freeze policy unenforced: new point-to-point created | 1,2 | Critical | Control: ARB freeze not operational; technical debt accumulating | Yes |
| Migration out of dependency order | 2 | High | Work Package: consuming application broken before dependency migrated | Yes |
| Legacy platform decommissioned before migration validated | 2,3 | Critical | Application Service: service continuity broken; rollback required | Yes |
| Ungoverned interfaces surviving Wave 3 close | 3 | Critical | Interface: target state not achieved; Bureau closure blocked | Yes |
| Dependent domain migrations blocked by Integration delay | 2,3 | High | Course of Action: all domain Component migrations dependent on backbone | Yes |

## Ossuary Notes
Highest-priority Component transition pattern in the M&A corpus. All other domain Component transitions declare dependency on this pattern explicitly. Integration Domain delay propagates severity to all dependent domains.

FILE: ossuary/ma/component/customer/OSS-MA-COM-CUS-001-current-state.md
markdown---
ossuary_id: OSS-MA-COM-CUS-001
altitude: Component
domain: M&A Integration Architecture
state: Current State
output_type: Pattern
subsystem: Customer Domain
togaf_constructs:
  primary: [Application Service, Logical Application Component]
  secondary: [Physical Application Component, Data Entity, Interface]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-001
---

# M&A Integration Architecture — Component Altitude — Customer Domain — Current State

## Application Component Inventory

### Entity A
**CRM Platform** — Logical Application Component. Customer record management, opportunity tracking, relationship history, communication logging. Entity-local. Interfaces: REST API, proprietary data export. Data Entity: Customer, Contact, Opportunity, Account.
**Customer Data Platform** — Logical Application Component (present or absent). Customer profile unification, behavioral data aggregation, segmentation. Entity-local.
**Identity Resolution Service** — Logical Application Component (formal or informal). Customer identity matching, deduplication, golden record management. Entity-local. Resolution rules undocumented at cross-entity level.
**Customer Master** — Logical Data Component. Entity-local. Data Entities: Customer, Party, Contact, Preference.

### Entity B
**CRM Platform** — Logical Application Component. Entity-local. Interfaces: REST API, proprietary data export. Standards non-aligned with Entity A. Customer data model non-aligned regardless of vendor.
**Customer Data Platform** — Logical Application Component (present or absent). Entity-local.
**Identity Resolution Service** — Logical Application Component (formal or informal). Entity-local. Resolution rules non-aligned with Entity A.
**Customer Master** — Logical Data Component. Entity-local. Semantic definitions non-aligned with Entity A customer master.

## Interface Inventory

| Interface | Owner | Protocol | Consumer | Governed |
|---|---|---|---|---|
| Entity A CRM API | Entity A | REST | Entity A applications | Entity-local only |
| Entity A CDP export | Entity A | Batch, REST | Entity A marketing | Entity-local only |
| Entity B CRM API | Entity B | REST | Entity B applications | Entity-local only |
| Entity B CDP export | Entity B | Batch, REST | Entity B marketing | Entity-local only |
| Cross-entity customer interface | None | N/A | N/A | Does not exist |

## Data Entity Non-Alignment

| Data Entity | Conflict |
|---|---|
| Customer | Non-identical semantics; resolution required |
| Party | May be absent in one entity |
| Contact | Relationship to Customer differs |
| Preference | Channel and consent models differ |

## Architectural Risk Profile

| Risk | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|
| No cross-entity customer identity | Critical | Data Entity: no canonical Customer model spans both entities | Yes |
| Dual customer masters non-aligned | Critical | Logical Data Component: two authoritative sources, non-identical semantics | Yes |
| Identity resolution rules undocumented | High | Logical Application Component: resolution logic ungoverned at enterprise level | Yes |
| CDP absent in one or both entities | Medium | Logical Application Component: behavioral data aggregation gap | Yes |
| Cross-entity customer interface absent | Critical | Interface: no governed cross-entity customer data surface | Yes |

## Qualification Holds
- Customer entity canonical definition: qualification prompt required before MDM authority declared.
- Identity resolution terminal condition: probabilistic match threshold, deterministic match only, or human review required?

## Ossuary Notes
Customer Domain is highest business-value domain post-integration backbone. Identity resolution is the critical path construct. All cross-entity customer interfaces route through enterprise integration backbone per OSS-MA-COM-INT-002.

FILE: ossuary/ma/component/customer/OSS-MA-COM-CUS-002-target-state.md
markdown---
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

**CRM Platform (Unified)** — Logical Application Component. Enterprise customer record management, unified relationship history, cross-entity communication logging. Enterprise-wide. Interfaces: REST API (canonical), governed event stream to enterprise message broker. ARB-governed. Canonical data model enforced.
**Customer Data Platform (Unified)** — Logical Application Component. Enterprise customer profile unification, behavioral data aggregation, cross-entity segmentation. Enterprise-wide. Interfaces: REST API, governed batch export, real-time event stream. Consent and preference model declared.
**Identity Resolution Service (Unified)** — Logical Application Component. Enterprise customer identity matching, automated deduplication, golden record management, cross-entity identity linkage. Resolution rules declared and governed. Deterministic and probabilistic thresholds documented. Human review escalation path defined.
**Enterprise Customer Master (MDM)** — Logical Data Component. Single authoritative customer record store for combined enterprise. Canonical models declared. Single named MDM authority. Golden record policy enforced.

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
Target state enables cross-sell motion declared at System altitude. Identity resolution service is the enabling construct: without automated cross-entity identity linkage, unified customer profile is not achievable. Joint cross-sell closure criterion with OSS-MA-COM-PRD-002.

FILE: ossuary/ma/component/customer/OSS-MA-COM-CUS-003-transition-state.md
markdown---
ossuary_id: OSS-MA-COM-CUS-003
altitude: Component
domain: M&A Integration Architecture
state: Transition State
output_type: Pattern
subsystem: Customer Domain
togaf_constructs:
  primary: [Work Package, Course of Action, Control]
  secondary: [Application Service, Logical Application Component, Data Entity]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-003
---

# M&A Integration Architecture — Component Altitude — Customer Domain — Transition State

## Dependency Declaration

| Dependency | Pattern | Wave Required | Type |
|---|---|---|---|
| Enterprise integration backbone | OSS-MA-COM-INT-003 | Wave 1 complete | Hard |
| Enterprise API gateway | OSS-MA-COM-INT-003 | Wave 1 complete | Hard |
| Enterprise message broker | OSS-MA-COM-INT-003 | Wave 1 complete | Hard |

## Wave Alignment

### Wave 0 — Customer Domain Discovery
**Exit criteria:** Both CRM platforms fully documented: data model, API surface, integration dependencies, user base, customization inventory. Both customer masters documented: record count, data quality assessment, duplicate rate, field mapping. Both CDP platforms documented or absence confirmed. Identity resolution rules documented per entity. Data Entity semantic comparison complete. Qualification holds issued.

### Wave 1 — MDM Authority and Identity Resolution Foundation
**Exit criteria:** Qualification holds resolved: customer canonical definition declared; identity resolution terminal condition confirmed. Enterprise MDM platform selected or designated: named Organization Unit authority declared. Canonical Data Entity models drafted: Customer, Party, Contact, Preference; ARB review initiated. Identity resolution service selected or designated: resolution rules drafted. CRM platform disposition decision ARB-ratified. Legacy CRM platforms under freeze. Customer Domain integration patterns registered in enterprise integration registry.

### Wave 2 — Migration and Identity Resolution Execution
**Exit criteria:** Enterprise customer master operational: canonical models implemented; MDM authority governing. Identity resolution service operational: cross-entity customer identity linkage executing; golden record policy enforced. CRM migration initiated with data quality validation gates enforced per record batch. CDP consolidation initiated. Legacy customer master in migration queue: reads redirected; writes frozen. Canonical Data Entity models ratified by ARB. Cross-sell motion pilot executed.

### Wave 3 — Legacy Decommission and Domain Closure
**Exit criteria:** Unified CRM operational enterprise-wide: all records migrated; data quality validated; user migration complete. Legacy CRM platforms decommissioned: retired system registry updated; Grimoire records closed. Enterprise customer master authoritative: legacy masters decommissioned. Unified CDP operational: all behavioral data migrated; legacy CDP decommissioned if present. Cross-sell motion confirmed operational. Customer Domain validated against OSS-MA-COM-CUS-002. All qualification holds closed in Grimoire.

## Component Transition Risk Register

| Risk | Wave | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|---|
| Integration backbone not ready at Wave 1 entry | 1 | Critical | Course of Action: dependency violated; migration cannot proceed | Yes |
| Qualification holds unresolved at Wave 1 close | 1 | High | Control: MDM authority cannot be declared without canonical definition | Yes |
| Data quality failures during CRM migration | 2 | High | Data Entity: source data does not conform to canonical model | Yes |
| Duplicate golden records post-identity resolution | 2 | High | Logical Data Component: resolution rules insufficient; manual review required | Yes |
| Legacy customer master decommissioned before migration validated | 3 | Critical | Logical Data Component: authoritative record lost; unrecoverable | Yes |
| Cross-sell motion blocked by incomplete identity resolution | 3 | High | Application Service: System-altitude Value Stream not achievable | Yes |

## Ossuary Notes
Identity resolution is the critical path construct. Data quality at source is the highest execution risk. A data quality remediation work package should be declared in Wave 1 if discovery reveals significant quality gaps.

FILE: ossuary/ma/component/product/OSS-MA-COM-PRD-001-current-state.md
markdown---
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
**PIM Platform** — Logical Application Component. Product definition, attribute management, catalog governance, lifecycle tracking. Entity-local. Interfaces: REST API, batch export, proprietary feed. Data Entity: Product, SKU, Attribute, Category.
**Pricing Engine** — Logical Application Component. Price calculation, discount management, promotional pricing, margin governance. Entity-local. Interfaces: REST API, real-time pricing feed. Pricing rules proprietary and undocumented at cross-entity level.
**Product Configuration Service** — Logical Application Component (present or absent). Product configurator, bundle definition, entitlement management. Entity-local.
**Product Master** — Logical Data Component. Entity-local. Data Entities: Product, SKU, Price, Configuration, Entitlement, Category.

### Entity B
**PIM Platform** — Logical Application Component. Entity-local. Interfaces: REST API, batch export. Category hierarchy and attribute schema differ materially from Entity A.
**Pricing Engine** — Logical Application Component. Entity-local. Interfaces: REST API. Pricing logic non-comparable with Entity A.
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
| Product fulfillment terminal condition unresolved | High | Value Stream or Contract: qualification hold open from Subsystem altitude | Yes |

## Qualification Holds
- Product fulfillment terminal condition: Value Stream, Business Service, or Contract?
- Product taxonomy canonical authority: which entity's taxonomy or new construction from first principles?
- Entitlement model: present in both entities or one; scope and governing construct undeclared.

## Ossuary Notes
Product taxonomy non-alignment is frequently underestimated. Category hierarchy conflicts block catalog unification more reliably than system incompatibility. Pricing logic non-comparability is a margin governance risk, not just an integration risk.

FILE: ossuary/ma/component/product/OSS-MA-COM-PRD-002-target-state.md
markdown---
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

**PIM Platform (Unified)** — Logical Application Component. Enterprise product definition, governed attribute management, canonical catalog governance, unified lifecycle tracking. Enterprise-wide. Interfaces: REST API (canonical), governed product feed to enterprise integration backbone. ARB-governed. Canonical taxonomy enforced.
**Pricing Engine (Unified)** — Logical Application Component. Enterprise price calculation, governed discount management, unified promotional pricing, cross-entity margin governance. Enterprise-wide. Interfaces: REST API, real-time pricing feed to integration backbone. Pricing rules documented and governed.
**Product Configuration Service (Unified)** — Logical Application Component. Enterprise product configurator, governed bundle definition, unified entitlement management. Enterprise-wide. Interfaces: REST API, configuration feed.
**Enterprise Product Master (MDM)** — Logical Data Component. Single authoritative product record store for combined enterprise. Canonical taxonomy declared. Single named MDM authority. Data stewardship model declared.

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
Cross-sell motion is the System-altitude Value Stream this pattern enables jointly with OSS-MA-COM-CUS-002. Neither Customer nor Product Domain Component target state alone enables cross-sell: both must be achieved. Bureau scores cross-sell enablement as a joint closure criterion across both domain patterns.

FILE: ossuary/ma/component/product/OSS-MA-COM-PRD-003-transition-state.md
markdown---
ossuary_id: OSS-MA-COM-PRD-003
altitude: Component
domain: M&A Integration Architecture
state: Transition State
output_type: Pattern
subsystem: Product Domain
togaf_constructs:
  primary: [Work Package, Course of Action, Control]
  secondary: [Application Service, Logical Application Component, Data Entity]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-003
---

# M&A Integration Architecture — Component Altitude — Product Domain — Transition State

## Dependency Declaration

| Dependency | Pattern | Wave Required | Type |
|---|---|---|---|
| Enterprise integration backbone | OSS-MA-COM-INT-003 | Wave 1 complete | Hard |
| Enterprise API gateway | OSS-MA-COM-INT-003 | Wave 1 complete | Hard |
| Unified customer identity operational | OSS-MA-COM-CUS-003 | Wave 2 initiated | Soft |

## Wave Alignment

### Wave 0 — Product Domain Discovery
**Exit criteria:** Both PIM platforms documented: data model, attribute schema, category hierarchy, API surface, integration dependencies, customization inventory, record count. Both product masters documented: record count, data quality assessment, duplicate rate, taxonomy depth comparison. Both pricing engines documented: pricing rule inventory, discount model, margin calculation logic, integration dependencies. Product configuration services documented or absence confirmed. Data Entity semantic comparison complete. Qualification holds issued.

### Wave 1 — Taxonomy Authority and MDM Foundation
**Exit criteria:** Qualification holds resolved: product fulfillment typed; taxonomy canonical authority declared; entitlement model scoped. Enterprise MDM platform selected or designated: named Organization Unit authority declared. Canonical taxonomy constructed: category hierarchy declared; attribute schema unified; ARB review initiated. PIM platform disposition decision ARB-ratified. Pricing engine disposition decision ARB-ratified. Legacy PIM and pricing platforms under freeze. Product Domain integration patterns registered. Canonical Data Entity models drafted.

### Wave 2 — Migration and Catalog Unification
**Exit criteria:** Enterprise product master operational: canonical taxonomy implemented; MDM authority governing. PIM migration initiated: product records migrating; taxonomy mapping executed; attribute conformance validated per record batch. Pricing engine unified: pricing rules migrated and reconciled; margin model operational enterprise-wide. Product configuration service unified if applicable. Legacy product master in migration queue: reads redirected; writes frozen. Canonical Data Entity models ratified by ARB. Cross-sell motion pilot executed. Taxonomy mapping completeness 80% or greater before Wave 3 entry.

### Wave 3 — Legacy Decommission and Domain Closure
**Exit criteria:** Unified PIM operational enterprise-wide: all records migrated; taxonomy conformance validated; user migration complete. Legacy PIM platforms decommissioned: retired system registry updated; Grimoire records closed. Enterprise product master authoritative: legacy masters decommissioned. Unified pricing engine operational: all pricing rules migrated; legacy pricing engines decommissioned. Unified product configuration service operational if applicable. Cross-sell motion confirmed operational. Product Domain validated against OSS-MA-COM-PRD-002. Joint cross-sell closure criterion validated with OSS-MA-COM-CUS-002. All qualification holds closed in Grimoire.

## Component Transition Risk Register

| Risk | Wave | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|---|
| Integration backbone not ready at Wave 1 entry | 1 | Critical | Course of Action: hard dependency violated | Yes |
| Taxonomy qualification hold unresolved at Wave 1 close | 1 | Critical | Logical Data Component: MDM cannot be declared without canonical taxonomy | Yes |
| Taxonomy mapping failures during PIM migration | 2 | High | Data Entity: legacy products do not map cleanly to canonical taxonomy | Yes |
| Pricing rule reconciliation conflicts | 2 | High | Logical Application Component: conflicting rules produce margin errors | Yes |
| Cross-sell motion blocked by incomplete Customer Domain | 2,3 | High | Application Service: joint enablement condition not met | Yes |
| Legacy product master decommissioned before migration validated | 3 | Critical | Logical Data Component: authoritative record lost | Yes |
| Taxonomy mapping below 80% threshold at Wave 3 entry | 3 | High | Data Entity: canonical model not fully governing; Wave 3 entry blocked | Yes |

## Ossuary Notes
Taxonomy mapping completeness threshold of 80% at Wave 3 entry is a platform-declared standard. Below 80%, the canonical taxonomy is not governing in practice. Bureau enforces this threshold as a hard Wave 3 entry condition. The remaining 20% carries a remediation work package into Wave 3 with a declared completion date before domain closure is permitted.

FILE: ossuary/ma/component/finance/OSS-MA-COM-FIN-001-current-state.md
markdown---
ossuary_id: OSS-MA-COM-FIN-001
altitude: Component
domain: M&A Integration Architecture
state: Current State
output_type: Pattern
subsystem: Finance Domain
togaf_constructs:
  primary: [Application Service, Logical Application Component]
  secondary: [Physical Application Component, Data Entity, Interface]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-001
---

# M&A Integration Architecture — Component Altitude — Finance Domain — Current State

## Application Component Inventory

### Entity A
**ERP Platform** — Logical Application Component. General ledger management, AP, AR, fixed assets, financial close orchestration. Entity-local. Interfaces: REST API, batch extract, proprietary reporting feed. Data Entity: Account, Journal Entry, Cost Center, Legal Entity, Vendor, Customer Ledger.
**Financial Close Management Tool** — Logical Application Component (present or absent). Close task orchestration, reconciliation management, close calendar governance. Entity-local. Close calendar non-aligned with Entity B.
**Regulatory Reporting Platform** — Logical Application Component. Statutory reporting, tax reporting, regulatory filing management. Entity-local. Jurisdiction-specific; reporting obligations declared per engagement.
**Financial Master** — Logical Data Component. Entity-local. Data Entities: Account, Journal Entry, Cost Center, Legal Entity, Regulatory Report.

### Entity B
**ERP Platform** — Logical Application Component. Entity-local. Interfaces: REST API, batch extract. Chart of accounts non-aligned with Entity A. Legal entity hierarchy differs materially. Note: ERP vendor may be same or different; chart of accounts non-alignment is the critical risk regardless of vendor.
**Financial Close Management Tool** — Logical Application Component (present or absent). Entity-local. Close calendar non-aligned with Entity A.
**Regulatory Reporting Platform** — Logical Application Component. Entity-local. May carry different jurisdictional obligations than Entity A.
**Financial Master** — Logical Data Component. Entity-local. Chart of accounts and legal entity hierarchy non-aligned with Entity A.

## Interface Inventory

| Interface | Owner | Protocol | Consumer | Governed |
|---|---|---|---|---|
| Entity A ERP API | Entity A | REST, batch | Entity A applications | Entity-local only |
| Entity A reporting feed | Entity A | Batch | Entity A reporting platform | Entity-local only |
| Entity B ERP API | Entity B | REST, batch | Entity B applications | Entity-local only |
| Entity B reporting feed | Entity B | Batch | Entity B reporting platform | Entity-local only |
| Cross-entity financial interface | None | N/A | N/A | Does not exist |
| Consolidation feed | Manual | Spreadsheet | Group finance | Ungoverned |

## Data Entity Non-Alignment

| Data Entity | Conflict |
|---|---|
| Account | Account codes, hierarchy, and naming non-aligned |
| Cost Center | Hierarchy depth and allocation logic differ |
| Legal Entity | Holding structure non-aligned; consolidation path differs |
| Journal Entry | Posting rules and period definitions may differ |
| Regulatory Report | Jurisdiction and filing format differ |

## Architectural Risk Profile

| Risk | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|
| Chart of accounts non-alignment | Critical | Data Entity: Account canonical model absent; consolidation impossible without reconciliation | Yes |
| Legal entity hierarchy non-aligned | Critical | Data Entity: Legal Entity structure non-comparable; statutory reporting at risk | Yes |
| Consolidation reporting manual | Critical | Application Service: no governed consolidation interface; spreadsheet is not fit for purpose | Yes |
| Close cycles unsynchronized | High | Process: financial close cannot be governed enterprise-wide without calendar alignment | Yes |
| Financial close construct type unresolved | High | Process or Contract: qualification hold open; regulatory obligation scope undeclared | Yes |
| Regulatory reporting obligations non-aligned | High | Contract or Requirement: jurisdiction-specific obligations not reconciled | Yes |

## Qualification Holds
- Financial close construct type: Process with Control, Process with Contract, or both independently?
- Regulatory reporting jurisdiction: which jurisdictions govern each entity's obligations? Are obligations additive post-merger?
- Chart of accounts rationalization authority: which entity's chart or new construction from first principles?
- Legal entity consolidation path: legal and tax decision required before architecture can proceed. Escalation to legal and tax is a Bureau-recommended action.

## Ossuary Notes
Finance Domain carries highest qualification hold complexity of all six domains. Legal entity hierarchy and chart of accounts rationalization require legal, tax, and regulatory input. Escalation to legal and tax is a Bureau-recommended action, not an optional suggestion.

FILE: ossuary/ma/component/finance/OSS-MA-COM-FIN-002-target-state.md
markdown---
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

**ERP Platform (Unified)** — Logical Application Component. Enterprise general ledger management, governed AP and AR, unified fixed assets, governed financial close orchestration. Enterprise-wide. Interfaces: REST API (canonical), governed financial data feed to enterprise integration backbone. ARB-governed. Canonical chart of accounts enforced.
**Financial Close Management Platform (Unified)** — Logical Application Component. Enterprise close task orchestration, governed reconciliation management, unified close calendar. Enterprise-wide. Interfaces: REST API, close status feed. Close calendar governing enterprise-wide.
**Regulatory Reporting Platform (Unified)** — Logical Application Component. Enterprise statutory reporting, unified tax reporting, governed regulatory filing management. Enterprise-wide. Interfaces: regulatory submission feeds, governed report export. All jurisdictional obligations declared and governed. Filing calendar enterprise-wide.
**Enterprise Financial Master (MDM)** — Logical Data Component. Single authoritative financial record store for combined enterprise. Canonical chart of accounts enforced. Legal entity hierarchy ratified by legal and tax. Single named MDM authority.

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
Consolidation automation is the primary System-altitude outcome of this pattern. Financial Flow Value Stream only achievable when consolidation feed is automated and chart of accounts unified. Legal and tax ratification of legal entity hierarchy is a non-negotiable prerequisite. Bureau does not close this pattern without documented evidence of that ratification.

FILE: ossuary/ma/component/finance/OSS-MA-COM-FIN-003-transition-state.md
markdown---
ossuary_id: OSS-MA-COM-FIN-003
altitude: Component
domain: M&A Integration Architecture
state: Transition State
output_type: Pattern
subsystem: Finance Domain
togaf_constructs:
  primary: [Work Package, Course of Action, Control]
  secondary: [Application Service, Logical Application Component, Data Entity]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-003
---

# M&A Integration Architecture — Component Altitude — Finance Domain — Transition State

## Dependency Declaration

| Dependency | Pattern | Wave Required | Type |
|---|---|---|---|
| Enterprise integration backbone | OSS-MA-COM-INT-003 | Wave 1 complete | Hard |
| Legal entity hierarchy decision | Legal and tax function | Wave 1 entry | Hard |
| Chart of accounts rationalization authority | Legal, tax, and finance | Wave 1 entry | Hard |
| Regulatory jurisdiction mapping | Compliance function | Wave 0 complete | Hard |

## Wave Alignment

### Wave 0 — Finance Domain Discovery
**Exit criteria:** Both ERP platforms documented: data model, chart of accounts, legal entity hierarchy, API surface, integration dependencies, customization inventory, period-end close process. Both financial masters documented: record count, data quality, chart of accounts comparison field by field. Both close management tools documented or absence confirmed. Both regulatory reporting platforms documented: jurisdictions, filing calendar, submission format inventory. Data Entity semantic comparison complete. Regulatory obligation inventory complete: all jurisdictions per entity declared; post-merger obligation scope assessed. Qualification holds issued. Legal and tax escalation initiated.

### Wave 1 — Legal Entity Ratification and ERP Foundation
**Exit criteria:** Legal and tax ratification received: legal entity hierarchy declared; chart of accounts rationalization authority named. All qualification holds resolved. Enterprise MDM platform selected or designated: named Organization Unit authority declared. Canonical chart of accounts drafted: account codes, hierarchy, and naming declared; ARB and finance leadership review initiated. Canonical legal entity hierarchy declared: ARB, legal, and tax ratification documented. ERP platform disposition decision ARB-ratified. Close management platform disposition ARB-ratified. Regulatory reporting platform disposition ARB-ratified. Legacy ERP platforms under freeze: no new accounts, no chart of accounts changes, no legal entity additions.

### Wave 2 — Chart of Accounts Migration and Close Unification
**Exit criteria:** Enterprise financial master operational: canonical chart of accounts implemented; MDM authority governing. Chart of accounts migration initiated: legacy accounts mapped to canonical chart; mapping completeness validated; unmapped accounts escalated to finance leadership. Legal entity hierarchy implemented in unified ERP: statutory reporting structure operational. ERP migration initiated with data quality validation gates enforced per journal entry batch. Close calendar unified: single enterprise close calendar governing. Close management platform unified: reconciliation rules migrated; close task orchestration operational enterprise-wide. Regulatory reporting platform unified: all jurisdictional obligations governed from single platform. Consolidation feed pilot executed. Legacy financial master in migration queue: reads redirected; writes frozen.

### Wave 3 — Legacy Decommission and Domain Closure
**Exit criteria:** Unified ERP operational enterprise-wide: all financial records migrated; chart of accounts conformance validated; user migration complete. Legacy ERP platforms decommissioned: retired system registry updated; Grimoire records closed. Enterprise financial master authoritative: legacy financial masters decommissioned. Consolidation reporting fully automated: no manual reconciliation in close cycle. Close cycle synchronized: single enterprise calendar; single close management platform. Regulatory reporting unified: all jurisdictional filings governed from single platform; legacy regulatory platforms decommissioned. Financial Flow Value Stream confirmed operational: consolidation automation validated against System-altitude declaration in OSS-MA-SYS-002. Finance Domain validated against OSS-MA-COM-FIN-002. Legal and tax ratification documentation filed in Grimoire. All qualification holds closed in Grimoire.

## Component Transition Risk Register

| Risk | Wave | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|---|
| Legal and tax escalation delayed: Wave 1 blocked | 0,1 | Critical | Course of Action: architectural decisions cannot precede legal decisions | Yes |
| Chart of accounts mapping failures | 2 | Critical | Data Entity: unmapped accounts block consolidation | Yes |
| Legal entity hierarchy implemented incorrectly in ERP | 2 | Critical | Data Entity: statutory reporting at risk; regulatory exposure | Yes |
| Close calendar unification contested by finance leadership | 1,2 | High | Control: close governance disputed; wave advancement at risk | Yes |
| Consolidation feed pilot fails at Wave 2 | 2 | High | Application Service: manual reconciliation dependency not eliminated | Yes |
| Regulatory filing missed during platform transition | 2,3 | Critical | Contract: regulatory obligation breached; jurisdiction-specific penalty | Yes |
| Legacy ERP decommissioned before migration validated | 3 | Critical | Logical Data Component: financial record integrity at risk | Yes |

## Ossuary Notes
Finance Domain is the most legally constrained domain in the M&A Component corpus. Premature chart of accounts or legal entity decisions made without legal and tax input are a Bureau critical finding regardless of how technically sound the architectural choice appears. The platform enforces this discipline through the Wave 1 entry dependency declaration.

FILE: ossuary/ma/component/human-capital/OSS-MA-COM-HCM-001-current-state.md
markdown---
ossuary_id: OSS-MA-COM-HCM-001
altitude: Component
domain: M&A Integration Architecture
state: Current State
output_type: Pattern
subsystem: Human Capital Domain
togaf_constructs:
  primary: [Application Service, Logical Application Component]
  secondary: [Physical Application Component, Data Entity, Interface]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-001
---

# M&A Integration Architecture — Component Altitude — Human Capital Domain — Current State

## Application Component Inventory

### Entity A
**HRIS Platform** — Logical Application Component. Employee record management, position management, organizational hierarchy, workforce reporting, onboarding and offboarding orchestration. Entity-local. Interfaces: REST API, batch export, proprietary workforce feed. Data Entity: Employee, Position, Organization, Compensation, Benefit.
**Payroll Platform** — Logical Application Component. Payroll calculation, tax withholding, payslip generation, payroll compliance, direct deposit management. Entity-local. Interfaces: payroll feed, tax filing submission, batch export. Jurisdiction-specific.
**Benefits Administration Platform** — Logical Application Component. Benefits enrollment, plan management, carrier integration, life event processing, open enrollment orchestration. Entity-local. Interfaces: carrier feeds, enrollment data export. Carrier contracts entity-local.
**Talent Acquisition System** — Logical Application Component (present or absent). Job requisition management, candidate tracking, offer management, onboarding initiation. Entity-local.
**HR Master** — Logical Data Component. Entity-local. Data Entities: Employee, Position, Organization, Compensation, Benefit.

### Entity B
**HRIS Platform** — Logical Application Component. Entity-local. Interfaces: REST API, batch export. Organizational hierarchy structure differs from Entity A. Note: HRIS vendor may be same or different; data model non-alignment is the critical risk regardless.
**Payroll Platform** — Logical Application Component. Entity-local. Payroll rules may differ by jurisdiction if entities operate in different states or countries.
**Benefits Administration Platform** — Logical Application Component. Entity-local. Benefit plans differ from Entity A. Carrier contracts non-aligned.
**Talent Acquisition System** — Logical Application Component (present or absent). Entity-local.
**HR Master** — Logical Data Component. Entity-local. Compensation model and organizational hierarchy non-aligned with Entity A.

## Interface Inventory

| Interface | Owner | Protocol | Consumer | Governed |
|---|---|---|---|---|
| Entity A HRIS API | Entity A | REST | Entity A applications | Entity-local only |
| Entity A payroll feed | Entity A | Batch | Entity A ERP, benefits | Entity-local only |
| Entity A carrier feeds | Entity A | EDI, batch | Benefits carriers | Entity-local only |
| Entity B HRIS API | Entity B | REST | Entity B applications | Entity-local only |
| Entity B payroll feed | Entity B | Batch | Entity B ERP, benefits | Entity-local only |
| Entity B carrier feeds | Entity B | EDI, batch | Benefits carriers | Entity-local only |
| Cross-entity workforce interface | None | N/A | N/A | Does not exist |

## Data Entity Non-Alignment

| Data Entity | Conflict |
|---|---|
| Employee | Identifier format, attribute schema non-aligned |
| Position | Grade, level, and classification differ |
| Organization | Hierarchy depth and unit naming non-aligned |
| Compensation | Pay bands, elements, and currency models differ |
| Benefit | Plan types, carrier relationships, and eligibility rules differ |

## Architectural Risk Profile

| Risk | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|
| No unified workforce view | Critical | Data Entity: no canonical Employee model spans both entities | Yes |
| Compensation model non-comparable | Critical | Data Entity: pay band and element non-alignment blocks enterprise compensation governance | Yes |
| Benefit plan non-alignment | High | Logical Application Component: carrier contracts and plan types non-aligned; harmonization requires legal and HR input | Yes |
| Payroll jurisdiction complexity | High | Logical Application Component: payroll rules differ by jurisdiction; cross-entity payroll governance is not a purely architectural decision | Yes |
| Workforce rationalization authority undeclared | High | Organization Unit: no named owner for enterprise-wide workforce decisions | Yes |
| Organizational hierarchy non-aligned | High | Data Entity: Organization construct non-comparable; enterprise org design unresolved | Yes |

## Qualification Holds
- Workforce rationalization authority: HR, EA, or joint governance decision?
- Compensation model harmonization: which entity's model or new construction? Legal, HR, and finance input required.
- Benefit plan harmonization scope: which plans survive, which are replaced, which are renegotiated? Legal and HR input required.
- Payroll jurisdiction scope: same jurisdictions or multi-jurisdiction payroll governance required?

## Ossuary Notes
Human Capital Domain carries significant non-architectural dependencies. Compensation harmonization, benefit plan rationalization, and payroll jurisdiction governance all require legal, HR, and regulatory input before target state can be declared. Early escalation to HR and legal is a Bureau recommendation, not an optional suggestion.

FILE: ossuary/ma/component/human-capital/OSS-MA-COM-HCM-002-target-state.md
markdown---
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

**HRIS Platform (Unified)** — Logical Application Component. Enterprise employee record management, governed position management, unified organizational hierarchy, enterprise workforce reporting, governed onboarding and offboarding orchestration. Enterprise-wide. Interfaces: REST API (canonical), governed workforce feed to enterprise integration backbone. ARB-governed. Canonical employee data model enforced.
**Payroll Platform (Unified)** — Logical Application Component. Enterprise payroll calculation, governed tax withholding, unified payslip generation, enterprise payroll compliance, multi-jurisdiction payroll governance where applicable. Enterprise-wide. Interfaces: payroll feed to unified ERP, tax filing submissions, governed batch export. Payroll rules governed per jurisdiction. Tax tables maintained enterprise-wide.
**Benefits Administration Platform (Unified)** — Logical Application Component. Enterprise benefits enrollment, governed plan management, rationalized carrier integration, unified life event processing, enterprise open enrollment orchestration. Enterprise-wide. Interfaces: rationalized carrier feeds, governed enrollment data export. Rationalized benefit plans declared. Carrier contracts renegotiated at enterprise scale. Eligibility rules governing enterprise-wide.
**Talent Acquisition System (Unified)** — Logical Application Component. Enterprise job requisition management, governed candidate tracking, unified offer management, governed onboarding initiation. Enterprise-wide. Interfaces: REST API, candidate feed to HRIS.
**Enterprise HR Master (MDM)** — Logical Data Component. Single authoritative employee record store for combined enterprise. Canonical compensation model enforced. Organizational hierarchy ratified by HR and legal. Single named MDM authority.

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
Compensation model ratification by HR, legal, and finance is a non-negotiable prerequisite. Benefit plan rationalization requires carrier contract renegotiation: this is a procurement and legal activity with architectural consequences, not an architectural activity with procurement consequences. Bureau does not close this pattern without documented evidence of HR and legal ratification of compensation model and organizational hierarchy.

FILE: ossuary/ma/component/human-capital/OSS-MA-COM-HCM-003-transition-state.md
markdown---
ossuary_id: OSS-MA-COM-HCM-003
altitude: Component
domain: M&A Integration Architecture
state: Transition State
output_type: Pattern
subsystem: Human Capital Domain
togaf_constructs:
  primary: [Work Package, Course of Action, Control]
  secondary: [Application Service, Logical Application Component, Data Entity]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-003
---

# M&A Integration Architecture — Component Altitude — Human Capital Domain — Transition State

## Dependency Declaration

| Dependency | Pattern | Wave Required | Type |
|---|---|---|---|
| Enterprise integration backbone | OSS-MA-COM-INT-003 | Wave 1 complete | Hard |
| Compensation model ratification | HR, legal, finance function | Wave 1 entry | Hard |
| Benefit plan rationalization decision | HR, legal, procurement | Wave 1 entry | Hard |
| Payroll jurisdiction scope declaration | Compliance, legal function | Wave 0 complete | Hard |
| ERP rationalization sequencing | OSS-MA-COM-FIN-003 | Wave 1 coordinated | Coordination |

## Wave Alignment

### Wave 0 — Human Capital Domain Discovery
**Exit criteria:** Both HRIS platforms documented: data model, organizational hierarchy, position structure, API surface, integration dependencies, customization inventory, employee record count. Both HR masters documented: record count, data quality, employee identifier format, duplicate rate assessment. Both payroll platforms documented: payroll rule inventory, jurisdiction coverage, tax table maintenance model, integration dependencies, payroll calendar. Both benefits platforms documented: plan inventory, carrier relationships, enrollment volume, carrier feed formats, contract terms and expiry dates. Talent acquisition systems documented or absence confirmed. Data Entity semantic comparison complete. Payroll jurisdiction scope confirmed. Qualification holds issued. Legal, HR, and compliance escalations initiated.

### Wave 1 — Authority Declaration and HCM Foundation
**Exit criteria:** Legal, HR, and compliance escalations resolved: compensation model ratified; benefit plan rationalization decision received; payroll jurisdiction governance declared. All qualification holds resolved: workforce rationalization authority named; organizational design governing authority declared. Enterprise MDM platform selected or designated. Canonical employee data model drafted: Employee, Position, Organization, Compensation, Benefit; ARB and HR review initiated. Canonical organizational hierarchy declared: ARB, HR, and legal ratification documented. HRIS platform disposition decision ARB-ratified. Payroll platform disposition decision coordinated with ERP rationalization sequencing and ARB-ratified. Benefits platform disposition decision: carrier contract renegotiation initiated; ARB-ratified. Legacy HRIS platforms under freeze. HCM Domain integration patterns registered. ERP rationalization coordination confirmed: payroll feed sequencing aligned with Finance Domain Wave 1.

### Wave 2 — Migration and Workforce Unification
**Exit criteria:** Enterprise HR master operational: canonical employee data model implemented; MDM authority governing. HRIS migration initiated: employee records migrating; organizational hierarchy implemented; data quality validation gates enforced per batch. Canonical organizational hierarchy operational in unified HRIS. Payroll platform unified: payroll rules migrated; jurisdiction governance operational; first parallel payroll run executed and validated against legacy payroll output. Benefits platform unified: rationalized plans operational; carrier feeds renegotiated and tested; enrollment data migrated. Compensation model unified: pay bands operational enterprise-wide; pay elements migrated. Talent acquisition system unified if applicable. Legacy HR master in migration queue: reads redirected; writes frozen. Payroll parallel run validation: unified payroll output reconciled against legacy payroll output for minimum two pay cycles before legacy decommission permitted.

### Wave 3 — Legacy Decommission and Domain Closure
**Exit criteria:** Unified HRIS operational enterprise-wide: all employee records migrated; organizational hierarchy validated; user migration complete. Legacy HRIS platforms decommissioned: retired system registry updated; Grimoire records closed. Enterprise HR master authoritative: legacy HR masters decommissioned. Unified payroll operational: minimum two validated parallel pay cycles complete; legacy payroll platforms decommissioned. Unified benefits platform operational: all carrier feeds live; legacy benefits platform decommissioned; renegotiated contracts governing. Unified talent acquisition system operational if applicable: legacy system decommissioned. Workforce view confirmed unified: enterprise org hierarchy, position model, and compensation model governing enterprise-wide. Finance Domain coordination confirmed: unified payroll feed to unified ERP operational and validated. Human Capital Domain validated against OSS-MA-COM-HCM-002. Compensation model and organizational hierarchy ratification documentation filed in Grimoire. All qualification holds closed in Grimoire.

## Component Transition Risk Register

| Risk | Wave | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|---|
| Legal and HR escalation delayed: Wave 1 blocked | 0,1 | Critical | Course of Action: compensation and benefit decisions cannot be architecturally assumed | Yes |
| Payroll parallel run not executed before legacy decommission | 2,3 | Critical | Control: payroll accuracy unvalidated; employee payment risk | Yes |
| Compensation model migration errors | 2 | Critical | Data Entity: pay element mapping failures produce incorrect payroll output | Yes |
| Carrier feed renegotiation delayed: benefits platform migration blocked | 1,2 | High | Logical Application Component: carrier contracts govern migration timeline | Yes |
| Organizational hierarchy contested during migration | 2 | High | Data Entity: org design disputes surface during HRIS implementation; escalation path required | Yes |
| Payroll and ERP sequencing misaligned | 1,2 | High | Course of Action: payroll feed to ERP broken if platforms rationalized independently | Yes |
| Legacy HRIS decommissioned before payroll validated | 3 | Critical | Logical Application Component: payroll dependency on HRIS data; decommission sequence enforced | Yes |

## Ossuary Notes
Payroll parallel run requirement is a platform-declared standard: no payroll platform is decommissioned without minimum two validated parallel pay cycles. This is non-negotiable. Employee payment accuracy is a legal obligation. Bureau enforces this as a hard Wave 3 entry condition. Any engagement that attempts to bypass this requirement receives a critical Bureau finding regardless of schedule pressure.

FILE: ossuary/ma/component/technology/OSS-MA-COM-TEC-001-current-state.md
markdown---
ossuary_id: OSS-MA-COM-TEC-001
altitude: Component
domain: M&A Integration Architecture
state: Current State
output_type: Pattern
subsystem: Technology Domain
togaf_constructs:
  primary: [Application Service, Logical Technology Component]
  secondary: [Physical Technology Component, Data Entity, Interface]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-001
---

# M&A Integration Architecture — Component Altitude — Technology Domain — Current State

## Application Component Inventory

### Entity A
**Cloud Platform** — Logical Technology Component. Infrastructure provisioning, platform governance, compute, storage, networking, managed services consumption. Entity-local. Cloud provider declared per engagement. Interfaces: cloud provider APIs, IaC tooling interfaces, platform governance feeds. Landing zone design proprietary. Tagging taxonomy ungoverned at cross-entity level. Technology Component owned: Compute, Storage, Network, Container Platform, Serverless, Managed Database.
**Identity Provider** — Logical Technology Component. Authentication, authorization, SSO, directory services, PAM. Entity-local. Interfaces: SAML, OAuth 2.0, OIDC, LDAP. Data Entity: Identity, Group, Role, Policy, Credential. Directory structure and group policy non-aligned with Entity B.
**ITSM Platform** — Logical Technology Component. Incident management, problem management, change management, service request fulfillment, service catalog governance. Entity-local. Interfaces: REST API, ITSM feed, CMDB sync. Change management process non-aligned with Entity B.
**Security Toolchain** — Logical Technology Component (set of components). EDR, SIEM, vulnerability management, CSPM, identity threat detection. Entity-local. Interfaces: security event feeds, threat intelligence feeds, compliance reporting. Security policies and alert thresholds non-aligned with Entity B.
**CMDB** — Logical Technology Component. Configuration item inventory, asset registry, dependency mapping, change impact analysis. Entity-local. Interfaces: CMDB API, discovery feed. CI taxonomy non-aligned with Entity B.

### Entity B
**Cloud Platform** — Logical Technology Component. Entity-local. Landing zone design non-aligned with Entity A. May be different cloud provider. Technology Component owned: Compute, Storage, Network, Container Platform, Managed Database. Multi-cloud complexity is highest risk if entities use different primary cloud providers.
**Identity Provider** — Logical Technology Component. Entity-local. Interfaces: SAML, OAuth 2.0, OIDC. Directory structure non-aligned with Entity A. Federation between providers ungoverned.
**ITSM Platform** — Logical Technology Component. Entity-local. ITIL process maturity may differ materially from Entity A.
**Security Toolchain** — Logical Technology Component (set of components). Entity-local. Security policies non-aligned with Entity A. Threat detection rules non-comparable.
**CMDB** — Logical Technology Component. Entity-local. CI taxonomy non-aligned with Entity A.

## Interface Inventory

| Interface | Owner | Protocol | Consumer | Governed |
|---|---|---|---|---|
| Entity A cloud platform APIs | Entity A | Cloud-native | Entity A applications | Entity-local only |
| Entity A identity provider | Entity A | SAML, OIDC | Entity A applications | Entity-local only |
| Entity A ITSM API | Entity A | REST | Entity A CMDB, monitoring | Entity-local only |
| Entity A security feeds | Entity A | Syslog, API | Entity A SIEM | Entity-local only |
| Entity B cloud platform APIs | Entity B | Cloud-native | Entity B applications | Entity-local only |
| Entity B identity provider | Entity B | SAML, OIDC | Entity B applications | Entity-local only |
| Entity B ITSM API | Entity B | REST | Entity B CMDB, monitoring | Entity-local only |
| Entity B security feeds | Entity B | Syslog, API | Entity B SIEM | Entity-local only |
| Cross-entity identity federation | None | N/A | N/A | Does not exist |
| Cross-entity security visibility | None | N/A | N/A | Does not exist |

## Data Entity Non-Alignment

| Data Entity | Conflict |
|---|---|
| Identity | Schema, group structure, and naming convention non-aligned |
| Configuration Item | CI type hierarchy and attribute schema non-aligned |
| Asset | Asset identifier format and classification non-aligned |
| Policy | Policy scope, enforcement mechanism, and alert threshold non-aligned |

## Architectural Risk Profile

| Risk | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|
| No cross-entity identity federation | Critical | Logical Technology Component: no governed identity surface spans both entities; access control is entity-local | Yes |
| Dual security perimeters ungoverned at boundary | Critical | Logical Technology Component: no unified threat visibility; attack surface at entity boundary is ungoverned | Yes |
| CMDB incomplete and non-aligned | High | Logical Technology Component: asset registry cannot support combined enterprise change management | Yes |
| Cloud landing zones non-aligned | High | Physical Technology Component: governance model, tagging taxonomy, and network topology non-comparable | Yes |
| ITSM change management non-aligned | High | Logical Technology Component: change governance across combined enterprise is not operable without process alignment | Yes |
| Multi-cloud complexity if providers differ | Critical | Physical Technology Component: cross-provider networking, security, and governance introduces exponential complexity | Yes |

## Qualification Holds
- Identity provider consolidation authority: IT Security, Platform Engineering, or joint governance body?
- Security perimeter unification scope: fully unified or federated model with governed cross-entity visibility? Security architecture decision with compliance implications.
- Cloud platform rationalization: single provider target or multi-cloud governance target? Strategic technology decision, not a default architectural choice.
- CMDB canonical authority: which ITSM platform and CMDB is the rationalization basis?

## Ossuary Notes
Technology Domain is the infrastructure dependency for all other five domains. Identity provider consolidation is the single highest-leverage action: it unblocks cross-entity access for every application in every other domain simultaneously. Multi-cloud complexity, if present, must be surfaced as a strategic finding at System altitude, not treated as a Component-level implementation detail.

FILE: ossuary/ma/component/technology/OSS-MA-COM-TEC-002-target-state.md
markdown---
ossuary_id: OSS-MA-COM-TEC-002
altitude: Component
domain: M&A Integration Architecture
state: Target State
output_type: Pattern
subsystem: Technology Domain
togaf_constructs:
  primary: [Application Service, Logical Technology Component]
  secondary: [Physical Technology Component, Data Entity, Interface, Control]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-002
---

# M&A Integration Architecture — Component Altitude — Technology Domain — Target State

## Application Component Inventory

**Cloud Platform (Unified)** — Logical Technology Component. Enterprise infrastructure provisioning, governed platform management, unified compute, storage, networking, and managed services consumption. Enterprise-wide. Single primary cloud provider declared; multi-cloud governance declared if applicable. Interfaces: governed cloud platform APIs, IaC tooling interfaces, unified platform governance feeds. Canonical landing zone design governing. Tagging taxonomy enforced enterprise-wide. Cost governance declared. Technology Component owned: Compute, Storage, Network, Container Platform, Serverless, Managed Database (canonical service catalog declared).
**Identity Provider (Unified)** — Logical Technology Component. Enterprise authentication, governed authorization, enterprise SSO, unified directory services, governed PAM. Enterprise-wide. Interfaces: SAML, OAuth 2.0, OIDC (canonical implementations declared); governed directory API. Canonical directory structure. Group policy enforced enterprise-wide. Data Entity: Identity, Group, Role, Policy, Credential (canonical models declared).
**ITSM Platform (Unified)** — Logical Technology Component. Enterprise incident management, governed problem management, unified change management, enterprise service request fulfillment, governed service catalog. Enterprise-wide. Interfaces: REST API (canonical), CMDB sync feed, monitoring integration feed. ITIL process governing enterprise-wide. Change management calendar unified. CAB constituted enterprise-wide.
**Security Toolchain (Unified)** — Logical Technology Component (governed set). Enterprise EDR, unified SIEM, enterprise vulnerability management, unified CSPM, enterprise identity threat detection. Enterprise-wide. Interfaces: unified security event feeds, enterprise threat intelligence feeds, compliance reporting feeds. Security policies governing enterprise-wide. Alert thresholds declared and enforced. SOC visibility spanning combined enterprise.
**Enterprise CMDB (Unified)** — Logical Technology Component. Single authoritative configuration item inventory, enterprise asset registry, governed dependency mapping, enterprise change impact analysis. Enterprise-wide. Interfaces: CMDB API, governed discovery feed. Canonical CI taxonomy declared. Asset registry complete and maintained. Discovery tooling governing enterprise-wide.

## Interface Inventory (Governed)

| Interface | Owner | Protocol | Consumer | Governed |
|---|---|---|---|---|
| Enterprise cloud platform APIs | Unified cloud platform | Cloud-native, governed | All governed applications | Yes, ARB |
| Enterprise identity provider | Unified identity provider | SAML, OAuth 2.0, OIDC | All governed applications, all domains | Yes, ARB |
| ITSM API | Unified ITSM | REST | CMDB, monitoring, integration backbone | Yes, ARB |
| Security event feeds | Unified security toolchain | Syslog, API | Unified SIEM, SOC | Yes, ARB |
| CMDB discovery feed | Unified CMDB | API, agent-based | All governed infrastructure | Yes, ARB |

## Data Entity Canonical Models

| Data Entity | Authority | Resolution Status |
|---|---|---|
| Identity | Named Organization Unit | Resolved |
| Group | Named Organization Unit | Resolved |
| Role | Named Organization Unit | Resolved |
| Configuration Item | Named Organization Unit | Resolved |
| Asset | Named Organization Unit | Resolved |
| Policy | Named Organization Unit | Resolved |

## Ossuary Notes
Technology Domain target state is a dependency for all other domain target states at Component altitude. Unified identity provider enables cross-entity application access for Customer, Product, Finance, Human Capital, and Integration domains simultaneously. Bureau declares Technology Domain Component target state as an enterprise-wide enabling milestone, not a domain-local closure. Unified security perimeter closes the enterprise attack surface at the boundary most exposed in current state.

FILE: ossuary/ma/component/technology/OSS-MA-COM-TEC-003-transition-state.md
markdown---
ossuary_id: OSS-MA-COM-TEC-003
altitude: Component
domain: M&A Integration Architecture
state: Transition State
output_type: Pattern
subsystem: Technology Domain
togaf_constructs:
  primary: [Work Package, Course of Action, Control]
  secondary: [Application Service, Logical Technology Component, Data Entity]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-SUB-003
---

# M&A Integration Architecture — Component Altitude — Technology Domain — Transition State

## Dependency Declaration

| Dependency | Pattern | Wave Required | Type |
|---|---|---|---|
| Enterprise integration backbone | OSS-MA-COM-INT-003 | Wave 1 complete | Hard |
| Identity provider consolidation authority | Security, platform governance | Wave 1 entry | Hard |
| Cloud platform rationalization decision | Technology strategy, ARB | Wave 1 entry | Hard |
| Security perimeter unification scope | Security architecture, compliance | Wave 0 complete | Hard |
| All domain migrations | OSS-MA-COM-CUS/PRD/FIN/HCM | Wave 1 coordination | Cross-domain |

## Wave Alignment

### Wave 0 — Technology Domain Discovery
**Exit criteria:** Both cloud platforms documented: provider, landing zone design, account and subscription structure, tagging taxonomy, network topology, managed services inventory, cost governance model, IaC tooling. Both identity providers documented: directory structure, group and role model, SSO integrations, PAM coverage, federation capabilities, user population count. Both ITSM platforms documented: process maturity, service catalog, CMDB integration, change management calendar, incident volume baseline. Both security toolchains documented: EDR coverage, SIEM data sources, vulnerability management scope, CSPM coverage, SOC operating model. Both CMDBs documented: CI taxonomy, asset count, discovery tooling, completeness assessment, staleness rate. Multi-cloud assessment: if entities use different cloud providers, complexity assessment produced and escalated to System altitude as a strategic finding. Qualification holds issued. Security architecture escalation initiated.

### Wave 1 — Identity Foundation and Cloud Governance
**Exit criteria:** All qualification holds resolved: identity consolidation authority declared; security perimeter scope confirmed; cloud platform rationalization decision received; CMDB canonical authority named. Identity provider selected: enterprise-wide deployment initiated; canonical directory structure declared; group and role model published. Cross-entity identity federation operational: all applications in all domains can authenticate against unified identity provider; legacy identity providers in migration queue but operational. Cloud platform landing zone unified: canonical landing zone design declared; tagging taxonomy governing; account and subscription structure rationalized. ITSM platform disposition decision ARB-ratified; process alignment initiated. Security toolchain disposition decision ARB-ratified; unified SOC visibility pilot initiated. Enterprise CMDB platform selected: discovery tooling deployed; combined CI inventory import initiated. Legacy identity providers under freeze: no new applications onboarded to legacy providers. Cross-domain notification: all domain Component migration teams notified that enterprise identity is operational.

### Wave 2 — Platform Migration and Security Unification
**Exit criteria:** Identity provider migration complete: all users and service accounts migrated to unified identity provider; legacy providers operational for residual access only. ITSM platform unified: incident, problem, change, and service request processes migrated; unified service catalog operational; CAB constituted enterprise-wide. Unified CMDB operational: canonical CI taxonomy governing; discovery tooling covering combined estate; asset registry completeness above 85% threshold. Security toolchain unified: EDR coverage enterprise-wide; unified SIEM receiving feeds from both legacy environments; CSPM covering combined cloud estate; SOC visibility spanning combined enterprise. Security policies unified: alert thresholds declared and enforced enterprise-wide. Cloud platform migration initiated: workloads migrating to unified landing zone per migration wave; legacy cloud accounts in decommission queue. Legacy identity providers decommissioned for all migrated applications.

### Wave 3 — Legacy Decommission and Domain Closure
**Exit criteria:** Unified identity provider enterprise-wide: all legacy identity providers decommissioned; no residual entity-local authentication remaining. Unified cloud platform operational: all workloads migrated to unified landing zone; legacy cloud accounts decommissioned; canonical tagging taxonomy governing entire estate. Unified ITSM operational: legacy ITSM platforms decommissioned; enterprise-wide ITIL process governing; change management calendar unified. Unified security toolchain operational: legacy security tools decommissioned; SOC visibility complete; security policies governing enterprise-wide. Enterprise CMDB authoritative: asset registry completeness above 95% threshold; discovery tooling governing combined estate; CI taxonomy enforced; legacy CMDBs decommissioned. Security perimeter unified: no ungoverned boundary between legacy entity environments. Cross-domain validation: all six domain Component target states confirm identity provider dependency met. Technology Domain validated against OSS-MA-COM-TEC-002. All qualification holds closed in Grimoire; cross-domain enablement record complete.

## Component Transition Risk Register

| Risk | Wave | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|---|
| Identity consolidation authority not declared at Wave 1 entry | 1 | Critical | Organization Unit: no owner for enterprise identity decision; all domain migrations blocked | Yes |
| Multi-cloud complexity underestimated at Wave 0 | 0 | Critical | Physical Technology Component: cross-provider complexity propagates to all six domains | Yes |
| Cross-entity identity federation not operational at Wave 1 close | 1 | Critical | Logical Technology Component: all domain application migrations blocked | Yes |
| CMDB completeness below 85% threshold at Wave 2 close | 2 | High | Logical Technology Component: change impact analysis unreliable; Wave 3 decommission sequencing at risk | Yes |
| Security toolchain unification delayed: SOC blind spot persists | 2 | Critical | Control: combined enterprise attack surface ungoverned at entity boundary | Yes |
| Legacy identity provider decommissioned before all applications migrated | 2,3 | Critical | Logical Technology Component: application authentication broken across multiple domains simultaneously | Yes |
| Cloud workload migration sequencing not coordinated with domain migrations | 2 | High | Course of Action: domain application migrations and infrastructure migrations conflict | Yes |
| CMDB below 95% threshold at Wave 3 entry | 3 | High | Logical Technology Component: asset registry not authoritative; decommission sequencing unreliable | Yes |

## Ossuary Notes
Technology Domain is unique in the Component corpus: the only domain whose transition state carries explicit cross-domain enabling responsibilities at every wave gate. Bureau wave-gate scoring for Technology Domain uses a cross-domain impact multiplier: a Technology Domain delay is never scored as a domain-local medium finding. CMDB completeness thresholds (85% at Wave 2, 95% at Wave 3) are platform-declared standards: below these thresholds the asset registry is not fit for change impact analysis and decommission sequencing cannot be reliably governed.

FILE: ossuary/bcdr/system/OSS-BCDR-SYS-001-current-state.md
markdown---
ossuary_id: OSS-BCDR-SYS-001
altitude: System
domain: Business Continuity & Disaster Recovery
state: Current State
output_type: Pattern
togaf_constructs:
  primary: [Capability, Control]
  secondary: [Course of Action, Value Stream, Organization Unit]
adm_phase: omit
bureau_calibration: false
region: US, NY regulatory jurisdiction
regulatory_surface:
  primary: NY State IT
  secondary: 23 NYCRR 500
---

# BCDR — System Altitude — Current State

## Motivational Layer

### Elicited (Aspirational)
| Construct | Declaration |
|---|---|
| Driver | [Elicited: regulatory obligation, client contractual exposure, reputational risk] |
| Goal | [Elicited: demonstrate recovery capability, satisfy dual regulatory surface] |
| Objective | [Elicited: close end-to-end DR validation gap; establish regulatory-committed timeline] |

### Consumed (Curated)
| Construct | Declaration |
|---|---|
| Driver | [From documentation: BCDR plan exists; component testing evidenced] |
| Goal | [From documentation: RTO/RPO declared per service tier] |
| Objective | [From documentation: internal compliance target exists; not regulatory-committed] |

Motivational delta: Internal timeline not externally committed. Declaration and proof disconnected at service tier. Both are Bureau finding candidates.

## Organization Structure (As-Reported)

| Entity | Type | Notes |
|---|---|---|
| [Technology delivery org] | Organization Unit | Mixed: SaaS and managed services |
| [Compliance function] | Organization Unit | Owns BCDR documentation; no test authority declared |
| [Engineering function] | Organization Unit | Owns AZ architecture; component testing executed |
| [Client-facing function] | Organization Unit | DFS regulated and state agency exposure |

## Capability Landscape
The firm operates a cloud native infrastructure with explicitly architected and governed AZ failover boundaries. BCDR documentation exists and is maintained. Service-tier RTO/RPO declarations are in place. The recovery posture is governed but unproven: component testing has been executed; full end-to-end DR has never been run.

- Recovery architecture is governed. AZ failover explicitly architected. Not assumed from cloud provider default.
- Service-tier RTO/RPO declarations exist. Recovery objectives are not enterprise-wide averages. Mature posture.
- End-to-end validation is absent. Component testing provides partial evidence. Full DR never executed.
- Regulatory commitment is absent. Internal compliance timeline exists. Neither regulatory surface carries a committed remediation schedule.
- Dual regulatory surface is uncoordinated. DFS regulated client obligations and state agency client obligations are governed separately.

## Value Streams (Conditional)

| Candidate | Triggering Capability | Qualification Required | Typed As |
|---|---|---|---|
| Recovery Execution | [DR Capability] | What is the declared terminal condition: service restoration or regulatory evidence? | Value Stream or Process, pending |
| Compliance Reporting | [Governance Capability] | Is this driven by audit cycle or continuous obligation? | Process with Control implications, pending |
| Client SLA Assurance | [Service Delivery Capability] | Is SLA mapped to service-tier RTO/RPO declarations? | Value Stream or Contract, pending |

## Architectural Risk Profile

| Risk | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|
| End-to-end DR never validated | Critical | Control: no recovery proof against service-tier RTO/RPO | Yes |
| No regulatory-committed timeline | High | Course of Action: internal target unenforceable by either regulator | Yes |
| Dual regulatory surface uncoordinated | High | Control: no unified compliance posture across DFS and NY State IT | Yes |
| Declaration/proof disconnect | High | Process: service-tier RTO/RPO declared but unvalidated under DR conditions | Yes |
| Compliance function lacks test authority | Medium | Organization Unit: no declared owner for end-to-end DR execution | Yes |

## Ossuary Notes
This pattern reflects a governed but unproven BCDR posture. Materially distinct from ad hoc or undocumented states. Bureau scoring baseline is set accordingly: documentation and governance credit applied; validation and commitment gaps scored as open findings. Illustrative example pattern; not P1 primary domain scope.

FILE: ossuary/bcdr/system/OSS-BCDR-SYS-002-target-state.md
markdown---
ossuary_id: OSS-BCDR-SYS-002
altitude: System
domain: Business Continuity & Disaster Recovery
state: Target State
output_type: Pattern
togaf_constructs:
  primary: [Capability, Control, Measure]
  secondary: [Course of Action, Value Stream, Contract]
adm_phase: omit
bureau_calibration: false
region: US, NY regulatory jurisdiction
regulatory_surface:
  primary: NY State IT
  secondary: 23 NYCRR 500
---

# BCDR — System Altitude — Target State

## Motivational Layer

### Resolved
| Construct | Declaration |
|---|---|
| Driver | [Resolved: regulatory obligation and client contractual exposure governed under unified compliance posture] |
| Goal | [Resolved: recovery capability proven end-to-end; dual regulatory surface satisfied] |
| Objective | [Resolved: regulatory-committed timeline met; full DR validated per service tier] |
| Measure | [Declared: RTO/RPO evidence per service tier; audit-ready documentation current] |

## Organization Structure (Rationalized)

| Entity | Type | Disposition |
|---|---|---|
| [Unified compliance function] | Organization Unit | Test authority declared; owns end-to-end DR execution |
| [Engineering function] | Organization Unit | AZ architecture maintained; DR runbook owned |
| [Client-facing function] | Organization Unit | SLA mapped to service-tier RTO/RPO; client obligations governed |

## Capability Landscape

- Recovery capability is proven. Full DR executed and evidenced per service tier against declared RTO/RPO.
- Regulatory commitment is active. Both NY State IT and 23 NYCRR 500 surfaces carry committed remediation and validation schedules.
- Dual regulatory surface is unified. Single compliance posture governs both DFS regulated and state agency client obligations.
- Test authority is declared. Single Organization Unit owns end-to-end DR execution authority. Governed RACI.
- Declaration and proof are connected. Service-tier RTO/RPO declarations backed by current validation evidence.

## Value Streams (Resolved)

| Value Stream | Triggering Capability | Terminal Condition | Typed As |
|---|---|---|---|
| Recovery Execution | [DR Capability] | Service restoration evidenced per tier | Value Stream |
| Compliance Reporting | [Governance Capability] | Audit cycle satisfied; continuous obligation met | Process with Control |
| Client SLA Assurance | [Service Delivery Capability] | SLA mapped and evidenced against RTO/RPO | Contract |

## Architectural Achievement Profile

| Construct | Target Condition |
|---|---|
| Capability | DR capability proven end-to-end per service tier |
| Control | Unified compliance posture; test authority declared; audit evidence current |
| Course of Action | Regulatory-committed timeline active on both surfaces |
| Measure | RTO/RPO evidence per service tier; audit-ready |
| Contract | Client SLA mapped to service-tier declarations |
| Organization Unit | Test authority declared; RACI governed |

## Ossuary Notes
Target state closes all four current-state findings. Bureau scoring uses this pattern as the validation completeness benchmark. Both regulatory surfaces must show committed schedules and current evidence before target state is declared achieved. Illustrative example pattern; not P1 primary domain scope.

FILE: ossuary/bcdr/system/OSS-BCDR-SYS-003-transition-state.md
markdown---
ossuary_id: OSS-BCDR-SYS-003
altitude: System
domain: Business Continuity & Disaster Recovery
state: Transition State
output_type: Pattern
togaf_constructs:
  primary: [Course of Action, Control, Work Package]
  secondary: [Capability, Process, Measure]
adm_phase: omit
bureau_calibration: false
region: US, NY regulatory jurisdiction
regulatory_surface:
  primary: NY State IT
  secondary: 23 NYCRR 500
---

# BCDR — System Altitude — Transition State

## Context
The governed passage from OSS-BCDR-SYS-001 to OSS-BCDR-SYS-002. The foundation exists: architecture is governed, service-tier RTO/RPO is declared, component testing is evidenced. The gaps are specific: end-to-end validation absent, regulatory commitment absent, dual surface uncoordinated. This is a validation and commitment engagement, not a greenfield BCDR build.

## Wave Structure

### Wave 0 — Gap Confirmation and Regulatory Scoping
**Exit criteria:** Four current-state findings formally opened in Bureau. Service-tier RTO/RPO declarations reviewed and confirmed as current. AZ architecture documentation reviewed; governed boundary confirmed. Dual regulatory surface mapped: NY State IT obligations and 23 NYCRR 500 obligations documented separately, then reconciled. Test authority gap confirmed. Value Stream qualification questions issued via Vril. Motivational dual-track capture complete; delta confirmed.
**Bureau constraint:** No validation execution in Wave 0. Scoping precedes testing. Enforced.

### Wave 1 — Commitment and Test Design
**Exit criteria:** Regulatory-committed timeline drafted for both surfaces; legal and compliance review initiated. End-to-end DR test plan produced per service tier: scope, success criteria, and rollback procedure declared. Unified compliance posture drafted; dual surface coordination gap addressed. Test authority declared; RACI published and ARB-reviewed. Value Stream qualification questions answered; construct typing confirmed. Motivational delta finding: remediation in progress. Ossuary reference tier active: NY State IT policy and 23 NYCRR 500 framework references loaded; Bureau suggestions generating.

### Wave 2 — Validation Execution
**Exit criteria:** End-to-end DR executed per service tier against declared RTO/RPO targets. Results documented: pass, fail, or partial per tier with remediation actions. Failed tiers: remediation executed and retest scheduled within committed window. Regulatory-committed timeline submitted to both surfaces. Unified compliance posture ratified; dual surface coordination confirmed. Motivational delta finding: closed; single governed motivational record declared. Measure construct instantiated: RTO/RPO evidence per tier current and audit-ready.

### Wave 3 — Closure and Continuous Governance
**Exit criteria:** All four current-state findings closed and Grimoire records updated. DR validation cycle declared: frequency, ownership, and evidence standard documented and ARB-ratified. Both regulatory surfaces: committed schedules active and current evidence filed. Client SLA mapped to validated service-tier RTO/RPO; Contract construct instantiated. Target-state architecture validated against OSS-BCDR-SYS-002. Grimoire transition record closed; Pelagic passage declared complete. Continuous governance posture declared: BCDR is no longer a project, it is an operational control.

## Cross-Wave Risk Register

| Risk | Wave | Severity | Broken Construct | Bureau Suggestion |
|---|---|---|---|---|
| Regulatory commitment not secured before test execution | 1 | Critical | Course of Action: commitment precedes evidence | Yes |
| Test authority disputed during Wave 2 execution | 2 | High | Organization Unit: RACI not ARB-ratified | Yes |
| Service tier fails DR test with no remediation plan | 2 | High | Control: no failure disposition declared in test plan | Yes |
| Dual surface obligations diverge during commitment drafting | 1 | High | Control: unified posture collapses under regulatory conflict | Yes |
| Continuous governance not declared at Wave 3 close | 3 | High | Control: BCDR reverts to project posture post-closure | Yes |
| Motivational delta unresolved at Wave 2 entry | 2 | Medium | Driver/Goal: internal and regulatory timelines not reconciled | Yes |

## Ossuary Notes
Transition pattern reflects a validation and commitment engagement. Wave scope is narrower than M&A transition by design. Foundation is present; proof and commitment are not. Bureau wave-gate scoring reflects this: documentation and architecture credit carried forward; validation evidence and regulatory commitment are the primary scoring dimensions. Illustrative example pattern; not P1 primary domain scope.

FILE: vril/VRL-QUAL-001-qualification-prompt.md
markdown---
vril_id: VRL-QUAL-001
altitude: any
domain: any
output_type: qualification
ossuary_dependency: none
bureau_calibration: false
region: declared per engagement
adm_phase: omit
purpose: >
  Elicit the information required to type an unconfirmed construct before
  it is declared in an Ossuary pattern. Prevents premature construct
  declaration. Gates Ossuary pattern completion at any altitude where
  construct typing is conditional.
---

# Vril Qualification Prompt

## Purpose
A qualification prompt is issued when an Ossuary pattern encounters a construct that cannot be typed from available information alone. It surfaces the minimum questions required to confirm the construct type before the pattern declaration is finalized.

Qualification prompts are not discovery prompts. They are precise, single-construct-targeted elicitation instruments. One unresolved construct, one qualification prompt. Do not batch unrelated constructs into a single prompt.

## Trigger Conditions
Issue a qualification prompt when any of the following are true:
- A Value Stream candidate exists but its terminal condition is unknown.
- A Process candidate exists but its regulatory or governance anchor is undeclared.
- A Business Service candidate exists but its consumer and delivery boundary are unconfirmed.
- A Contract candidate exists but its governing obligation is undeclared.
- A Capability candidate exists but its delivering Organization Unit is contested or unknown.
- Any construct relationship in the TOGAF full metamodel cannot be confirmed from available evidence.

## Batching Rule
Qualification holds accumulate within an altitude. They are batched and issued at the altitude boundary, not one at a time as they are discovered. Bureau decides per hold whether an unresolved qualification hold blocks descent to the next altitude.

## Resolution Authority
The architect closes qualification holds. No client stakeholder closes a hold unilaterally.

## Escalation
Bureau escalates after one missed check-in. No fixed timer. Bureau judgment governs.

## Prompt Structure
Every qualification prompt declares:

| Field | Content |
|---|---|
| Construct candidate | The untyped construct being qualified |
| Triggering evidence | What was observed that surfaced this candidate |
| Qualification question | The single question that resolves the typing |
| Possible resolutions | The construct types that could result, with their conditions |
| Ossuary impact | Which pattern field is held pending this resolution |
| Bureau impact | Whether an open finding exists pending this resolution |

## Example: Value Stream Candidate
**Construct candidate:** Customer Lifecycle
**Triggering evidence:** Client elicitation named customer lifecycle as a strategic flow. No terminal condition declared. No triggering Capability named.
**Qualification question:** What is the terminal condition of the customer lifecycle: ongoing relationship management, a discrete transaction event, or a regulated onboarding completion?
**Possible resolutions:**
- Ongoing relationship management: Value Stream, triggered by Customer Management Capability.
- Discrete transaction event: Process, governed by transaction Control.
- Regulated onboarding completion: Process with Contract implications, governed by regulatory Requirement.
**Ossuary impact:** Value Stream table row held pending resolution.
**Bureau impact:** No open finding. Qualification hold, not a scored finding, until resolution deadline exceeded.

## Dual-Track Rule
Qualification prompt answers are taken at face value unless they contradict consumed documentation. If an answer contradicts consumed documentation, flag the contradiction. Do not apply dual-track by default to all qualification answers.

## Resolution Protocol
1. Confirm construct type against resolution conditions.
2. Update Ossuary pattern: replace pending row with confirmed declaration.
3. Name the triggering Capability explicitly.
4. Declare the terminal condition.
5. Close the qualification hold in the pattern's Ossuary notes.
6. Update Bureau finding status if applicable.
7. Record resolution in Grimoire: prompt ID, question, answer, construct declared, pattern updated.

## Recording
Every resolved qualification hold is recorded in both Grimoire and the Ossuary pattern inline. Dual record, always.

## Qualification Hold vs Bureau Finding
A qualification hold is not a finding. It is governed incompleteness. A Bureau finding is opened only when: a qualification prompt has been issued and not answered within the declared engagement timeline; a construct has been typed without qualification where qualification was required; or a pattern has been advanced to a lower altitude before all qualification holds at the current altitude are resolved.

## Ossuary Notes
Domain-agnostic and altitude-agnostic. Applies wherever a construct typing decision cannot be made from available evidence. All Vril prompts that encounter unresolvable construct candidates must issue a qualification prompt before pattern closure. Grimoire records every qualification prompt issued, answered, and resolved across all engagements.

FILE: ossuary-reference-tier/OSS-REF-001-reference-tier-design.md
markdown---
ossuary_id: OSS-REF-001
altitude: platform
domain: all
output_type: reference tier design
bureau_calibration: false
region: routing key declared per engagement
adm_phase: omit
---

# Ossuary Reference Tier

## Purpose
The Ossuary reference tier is the governed corpus of external knowledge that Bureau draws from when generating suggestions. It is distinct from the Ossuary pattern corpus: patterns are synthetic EA exemplars produced by the platform; references are external sources consumed by the platform.

Every Bureau suggestion cites a reference. Every reference declares its source, tier, region, and date. No undeclared reference influences a finding or suggestion.

## Three Sub-Tiers

### Tier 1: Framework
Governed, stable, citable standards bodies and methodology frameworks. Slow-changing. High authority. Region-independent unless the framework is jurisdiction-specific.

Examples: TOGAF, SABSA, COBIT, ISO 22301, NIST, 23 NYCRR 500, NY State IT policy, DORA, FedRAMP.

Characteristics:
- Version-declared: every reference names the specific version in use.
- Jurisdiction-aware: regulatory frameworks declare their jurisdiction explicitly. A 23 NYCRR 500 reference is US/NY only.
- Highest citation authority in Bureau suggestions.
- Supersession tracked: when a framework version is superseded, existing citations are flagged for review, not auto-updated.

### Tier 2: Analyst
Opinionated, dated, vendor-influenced market analysis. Authoritative within its publication window. Region and market weighted.

Examples: Gartner Magic Quadrant, Forrester Wave, IDC MarketScape, sector-specific analyst coverage.

Characteristics:
- Date-stamped: publication quarter and year declared on every citation.
- Region-weighted: Gartner and Forrester are western, English-language, US-market-weighted by default. APAC, LATAM, MENA engagements require region-appropriate analyst sources.
- Lower citation authority than Tier 1 for compliance findings.
- Higher citation authority than Tier 1 for vendor evaluation and technology bakeoff findings.
- Shelf life declared: analyst citations older than 24 months are flagged as potentially stale in Bureau suggestions.

### Tier 3: Market Signal
Raw, current, requires interpretation. Open market data and industry signal sources.

Examples: Crunchbase, SEC filings, public earnings data, open regulatory filings, industry association publications.

Characteristics:
- Currency-dependent: value degrades rapidly. Date of retrieval declared on every citation.
- Interpretation required: Bureau cites market signal as supporting evidence, always paired with Tier 1 or Tier 2.
- Never standalone: a Bureau suggestion grounded only in Tier 3 is a malformed suggestion. Tier 3 always supplements, never leads.
- Region-native: market signal sources are inherently regional. Crunchbase is US-weighted. Regional equivalents must be declared for non-western engagements.

## Region Routing
Region is declared in Vril frontmatter per engagement. Bureau resolves the active reference set from the declared region. No undeclared region defaults to a western reference set silently.

| Region Declaration | Tier 1 Default | Tier 2 Default | Tier 3 Default |
|---|---|---|---|
| US, NY regulatory jurisdiction | TOGAF, 23 NYCRR 500, NY State IT | Gartner, Forrester | Crunchbase, SEC |
| US, federal | TOGAF, NIST, FedRAMP | Gartner, Forrester | USASpending, SEC |
| EU | TOGAF, DORA, GDPR | Gartner, Forrester, PAC | Eurostat, ESMA filings |
| APAC | TOGAF, regional regulatory | IDC, local analyst | Regional exchange filings |
| MENA | TOGAF, jurisdiction-specific | Regional analyst | Regional regulatory filings |
| Global | TOGAF, ISO standards only | Omitted unless declared | Omitted unless declared |

Region declarations are additive: an engagement can declare multiple regions if the client operates across jurisdictions.

## API Integration Contract
The reference tier is designed for API-backed population at a later phase. The integration contract is declared now so the structure is durable when the API layer arrives.

Every reference entry in the tier exposes:

```json
{
  "reference_id": "REF-[tier]-[source]-[id]",
  "tier": "1 | 2 | 3",
  "source": "source name",
  "region": ["region declaration"],
  "jurisdiction": "jurisdiction if applicable",
  "version": "version or publication date",
  "retrieved": "date of retrieval or last verified",
  "url": "source URL if publicly accessible",
  "summary": "one sentence describing the reference",
  "superseded_by": "reference_id if superseded, null if current"
}
```

Manual population at proof of concept stage. API integration replaces manual population in Phase 4. The contract does not change; the population mechanism does.

## Governing Rules
- No Bureau suggestion cites an undeclared reference.
- No Tier 3 citation appears without a paired Tier 1 or Tier 2 citation.
- No analyst citation older than 24 months is used without a staleness flag in the Bureau suggestion.
- No western reference set is applied to a non-western engagement without explicit architect override declared in the Vril frontmatter.
- Superseded framework versions are flagged, not silently replaced.
- Every reference entry is versioned in Grimoire: additions, updates, and supersessions are all recorded.

## Ossuary Notes
This document governs the reference tier structure. Population of each sub-tier is a separate build activity. Tier 1 framework references for M&A and BCDR domains are the first population targets. Bureau scoring rubric design in Phase 2 declares which tier has citation authority for which finding type. API integration layer is Phase 4 scope.

FILE: README.md
markdown# Miskatonic

A governed AI platform for enterprise architecture practice.

Named for the institution that governs access to forbidden knowledge: it maintains the collection, produces the practitioners, and ensures what is retrieved can be used responsibly.

**github.com/JesseMyer/miskatonic**

---

## What This Is

Miskatonic is not a template library. It is not a chatbot wrapper. It is a structured knowledge platform for enterprise architecture practice: altitude-aware, domain-calibrated, TOGAF-metamodel-conformant, and governed at every layer.

Every artifact declares its altitude, domain, state, metamodel constructs, parent pattern, and qualification holds. Nothing floats free. Every risk maps to a broken metamodel construct relationship. Every finding triggers a Bureau suggestion. Every qualification hold gates descent to the next altitude.

Zero human-written code. The platform is governed by Jesse Myer and generated by Claude. This is the proof of concept.

---

## The Six Subsystems

| Subsystem | Name | Function |
|---|---|---|
| Prompt Library | Vril | Altitude-aware, domain-calibrated prompts that unlock the platform's knowledge |
| Pattern Corpus | Ossuary | Governed repository of synthetic EA exemplars, TOGAF-calibrated, organized by domain |
| ZUI Framework | Tenebrous | Metamodel descent engine: System to Subsystem to Component to Sequence to Schema |
| Governance Engine | Bureau | ARB-calibrated adjudication layer: classifies, scores, finds, escalates, suggests |
| Roadmap Engine | Pelagic | Charts the governed passage between current state and target state |
| Annotation Harness | Grimoire | Governed record of every adjudication, scoring decision, finding, and milestone |

The governing sentence: Vril invokes Ossuary. Tenebrous renders the view. Bureau scores the architecture. Pelagic charts the passage. Grimoire records what was learned.

---

## Architecture Principles

**Altitude discipline.** Every artifact declares its altitude. Five levels: System, Subsystem, Component, Sequence, Schema. Cross-altitude coherence is verified. Altitude confusion is a Bureau finding.

**TOGAF full metamodel, strict adherence.** Every artifact declares its governing metamodel constructs. Every risk maps to a broken construct relationship. ADM is a light optional overlay, not a governing framework.

**Domain calibration.** Every artifact is calibrated to a specific EA engagement domain. Generic EA is decoration.

**Bureau suggests, not just scores.** Every finding carries a best-practice remediation suggestion, scoped to the declared region and Ossuary reference tier. The architect disposes. Grimoire records.

**Region-aware.** Every engagement declares a region. The Ossuary reference tier routes to the appropriate framework, analyst, and market signal sources for that region. Gartner is not authoritative in APAC. The platform knows this.

**Zero human-written code.** Jesse governs and calibrates. Claude generates and assembles.

---

## Current State: Phase 1 In Progress

### Ossuary Corpus

| Domain | System | Subsystem | Component | Sequence | Schema |
|---|---|---|---|---|---|
| M&A Integration Architecture | 3 patterns | 3 patterns | 18 patterns | Pending | Pending |
| BCDR (illustrative) | 3 patterns | Pending | Pending | Pending | Pending |
| Cloud Readiness | Phase 4 | Phase 4 | Phase 4 | Phase 4 | Phase 4 |
| Governance & ARB | Phase 4 | Phase 4 | Phase 4 | Phase 4 | Phase 4 |
| Technology Bakeoff | Phase 4 | Phase 4 | Phase 4 | Phase 4 | Phase 4 |
| AI Strategy | Phase 4 | Phase 4 | Phase 4 | Phase 4 | Phase 4 |

### Platform Artifacts

| Artifact | ID | Status |
|---|---|---|
| Vril qualification prompt type | VRL-QUAL-001 | Complete |
| Ossuary reference tier design | OSS-REF-001 | Complete |
| Bureau scoring rubric | Pending | Phase 2 |
| Pelagic roadmap template | Pending | Phase 2 |
| Tenebrous ZUI templates | Pending | Phase 2 |
| Grimoire annotation schema | Pending | Phase 3 |

---

## The Build Sequence

### Phase 0 — Governing Identity
Complete. One repo. One README. One manifesto. Six subsystem folders. Live at github.com/JesseMyer/miskatonic.

### Phase 1 — Knowledge Foundation
In progress: approximately 60%. Ossuary M&A corpus: System, Subsystem, and Component altitude complete. 24 M&A patterns. 3 BCDR illustrative patterns. Vril qualification prompt type complete. Ossuary reference tier designed. Sequence and Schema altitudes remaining. Vril M&A prompt library remaining.

### Phase 2 — Delivery and Governance
Not started. Tenebrous ZUI templates. Bureau scoring rubric with suggestion engine. Pelagic roadmap template. First full M&A engagement simulation.

### Phase 3 — Learning and Coherence
Not started. Grimoire annotation schema. Cross-altitude traceability validation. Plain-language invocation guide.

### Phase 4 — Domain Expansion
Not started. BCDR, Cloud Readiness, Governance and ARB, Technology Bakeoff, AI Strategy. One domain per weekend.

### Phase 5 — Public Launch
Not started. GitHub public. Launch post on jessemyer.com/perspective. The 2017 arc closes publicly.

---

## Governance Decisions on Record

Seven platform-level governance decisions locked to date:

1. Dual-track motivational layer: elicited and consumed records are separate artifacts; delta is a Bureau finding.
2. Org structure captured day one, as-reported; contradictions surface at Subsystem altitude as findings.
3. Construct typing is conditional; Vril qualification prompts gate declaration before pattern closure.
4. Bureau suggests, not just scores; Grimoire records every disposition.
5. Strict TOGAF full metamodel adherence; ADM as light optional overlay only.
6. Ossuary reference tier with region as the routing key; API integration layer reserved for Phase 4.
7. Compliance mapping deferred to Phase 4 domain expansion.

---

## The Arc

2017: A Case for AI for EA — the argument made in public.
2018: ZUI Framework — the metamodel delivery architecture.
2018-2020: Digital Transformation 3.0 — the domain knowledge.
2022: EA Archaeology — the stratigraphic navigation metaphor.
2023: Can COTS AI Do EA? — the direct test. Not yet. Not without governance.
2026: Miskatonic — the platform that closes the arc.

---

The arc closes here.