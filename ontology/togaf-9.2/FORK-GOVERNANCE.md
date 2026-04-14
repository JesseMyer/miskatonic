# FORK-GOVERNANCE.md
## Miskatonic — TOGAF 9.2 Content Metamodel Ontology Fork
### ontology/togaf-9.2/

---

## What This Is

This directory contains the Miskatonic governed fork of the TOGAF 9.2 Content
Metamodel OWL Ontology, introduced as a Phase 2 preview proof-of-concept for
ontological ingestion and Bureau construct validation.

The fork is not a Phase 4 deliverable accelerated forward. It is a PoC artifact
that establishes the ingestion pattern, governance posture, and known gap inventory
so that Phase 4 builds on a governed foundation rather than a cold start.

---

## Source

**Upstream repo:** github.com/cadmiumkitty/togaf-content-metamodel-ontology
**Upstream version:** v2.0.0
**Upstream license:** Creative Commons Attribution-ShareAlike 4.0 (CC-BY-SA-4.0)
**Original formalization:** Aurona Gerber, Paula Kotze, Alta van der Merwe
**Updated to 9.2:** Eugene Morozov (cadmiumkitty / Dalston Semantics Ltd, Sydney AU)
**Based on:** TOGAF Standard, Version 9.2, Chapter 30, Figure 30-7

**This fork license:** CC-BY-SA-4.0 (ShareAlike inherited from source, as required)
**TOGAF trademark:** TOGAF is a registered trademark of The Open Group.
**Commercial use:** Requires TOGAF Annual Commercial License from The Open Group.
**Attribution requirement:** Credit Aurona Gerber and Eugene Morozov per CC-BY-SA-4.0.

---

## Governance Decision Record

**Decision:** Fork the cadmiumkitty TOGAF 9.2 OWL ontology into Miskatonic as a
Phase 2 preview PoC, ahead of the Phase 4 API integration layer for the Ossuary
reference tier.

**Rationale:** The license permits it now. Waiting for Phase 4 is an arbitrary
sequencing constraint, not a governed one. The ontology is the machine-executable
version of Figure 30-7, which is the construct validation reference that Bureau
coherence scoring will eventually execute against. Ingesting it now as a PoC
establishes the ingestion pattern, documents the known gaps, and makes the construct
graph queryable against Ossuary artifact frontmatter without waiting for the full
Phase 4 API integration architecture to be built.

**Decided by:** Jesse Myer
**Phase:** Phase 2 Preview / PoC
**Phase 4 target:** Full Bureau construct validation engine executing against this
ontology as the schema authority for Ossuary coherence scoring.

---

## What Was Taken From Upstream

The following upstream artifacts were ingested and adapted:

- `OntologyTOGAFContentMetamodelV2.ttl`: The primary OWL ontology in Turtle
  serialization. All constructs and relationships from TOGAF 9.2 Figure 30-7
  formalized as OWL classes and typed object properties.

- `OntologyTOGAFContentMetamodelV2.xml`: RDF/XML serialization of the same
  ontology. Available upstream; not separately committed here pending Phase 4.

- `VocabularyTOGAFContentMetamodelV2.ttl`: SKOS taxonomy layer with construct
  definitions. Available upstream; Phase 4 ingestion target.

---

## Miskatonic Deviations From Upstream v2.0.0

The following deviations are present in the Miskatonic fork. All deviations are
additive. No upstream construct or relationship has been removed or semantically
modified. TOGAF construct definitions are preserved verbatim.

### 1. Miskatonic Governance Namespace

A `msk:` annotation namespace has been added:
`https://github.com/JesseMyer/miskatonic/ontology/togaf-9.2/governance#`

This namespace carries Miskatonic operational annotations on top of the TOGAF
construct definitions. It does not modify TOGAF semantics. Annotation properties
introduced:

- `msk:togafDomain`: TOGAF architecture domain (General Entities, Business
  Architecture, Data Architecture, Application Architecture, Technology Architecture)
- `msk:togafSubDomain`: Sub-domain within domain (Motivational, Organizational,
  Functional)
- `msk:figureRef`: Chapter 30 figure number declaring this construct or relationship
- `msk:miskatonicPrimary`: Boolean flag for constructs appearing as primary TOGAF
  constructs in Ossuary M&A corpus frontmatter
- `msk:miskatonicNote`: Platform-specific governance notes per construct, including
  Bureau finding triggers and qualification hold declarations
- `msk:sourceNote`: Notes deviations inherited from cadmiumkitty v2.0.0 or
  introduced by Miskatonic
- `msk:forkGovernanceRef`, `msk:phaseIntroduced`, `msk:knownGaps`: Ontology-level
  governance metadata

### 2. Bureau Finding Trigger Annotations

Constructs whose absence triggers a Bureau finding have been annotated with
`msk:miskatonicNote` carrying the finding type. This is the first step toward
automated Bureau construct validation. Finding triggers annotated:

- `togaf:Capability`: absence of delivering WorkPackage = Capability Collision (Critical)
- `togaf:ApplicationService`: ungoverned outside LogicalApplicationComponent = Shadow Integration Risk (Medium)
- `togaf:DataEntity`: no authoritative LogicalDataComponent = Data Sovereignty Conflict (High)
- `togaf:Control`: absent at current state = Governance Vacuum (High)
- `togaf:Driver`: elicited/consumed delta = Motivational Delta (High)
- `togaf:OrganizationUnit`: as-reported capture governance noted

### 3. Qualification Hold Annotations

`togaf:ValueStream` carries `msk:miskatonicNote` recording that Vril qualification
prompt gates the `businessCapabilityIsOperationalizedByValueStream` relationship
declaration. This is the OWL encoding of the conditional construct typing governance
decision.

---

## Known Gaps: This Fork vs. TOGAF 9.2 Full Specification

These gaps are acknowledged, documented, and deferred to Phase 4 unless earlier
remediation is warranted by platform needs.

### Gap 1: Extension Modules Not Formalized

The TOGAF 9.2 full metamodel includes seven predefined extension modules beyond the
core Figure 30-7 construct graph. None of these extensions are formalized in the
upstream OWL ontology or this fork:

| Extension | Chapter | Phase 4 Priority |
|---|---|---|
| Motivation Extension | 30.4.1 | High: needed for Bureau motivational scoring |
| Governance Extension | 30.4.2 | High: needed for Bureau ARB construct validation |
| Services Extension | 30.4.3 | Medium: relevant for contract and SLA modeling |
| Data Extension | 30.4.4 | High: needed for MDM authority construct scoring |
| Security Extension | 30.4.5 | Medium: relevant for BCDR and 23 NYCRR 500 domains |
| SOA Extension | 30.4.6 | Low: legacy relevance decreasing |
| Infrastructure Extension | 30.4.7 | Medium: relevant for Technology domain patterns |

### Gap 2: Construct Attributes Not Modeled

TOGAF 9.2 Chapter 30.3 defines attribute profiles per construct (ID, Name, Description,
Source, Owner, etc.). The OWL ontology models the construct graph and relationship
types, not the attribute schema. Attribute profiles are currently handled through
Ossuary pattern frontmatter structure. Full attribute modeling is a Phase 4 target.

### Gap 3: TOGAF 10th Edition Enterprise Metamodel Not Incorporated

TOGAF 10th Edition (2022) refactored the metamodel from "Content Metamodel" to
"Enterprise Metamodel" with structural changes. This fork is pinned to 9.2.
The 10th Edition AsciiDoc/Git publication (2025) may enable a cleaner machine-readable
source for Phase 4. Version assessment deferred to Phase 4.

### Gap 4: DoDAF, MODAF, NAF Alignment Not Formalized

TOGAF is extensible across DoDAF, MODAF, NATO AF, FEAF, Zachman, and ATAM. The
construct graph in this fork is TOGAF 9.2 only. Cross-framework alignment is a
Miskatonic Phase 4 design decision. The msk: namespace is designed to accommodate
cross-framework annotation without modifying TOGAF construct semantics.

### Gap 5: Upstream Inconsistency in TOGAF 9.2 Section 30.7

The Gerber et al. academic formalization identified an inconsistency in TOGAF 9.2
Figure 30-7 that makes the metamodel non-constructable as published. The cadmiumkitty
v2.0.0 fork resolves it through specific naming corrections documented in its README.
This fork inherits those resolutions. The inconsistency is not in the Miskatonic
construct governance layer; it is in the upstream published standard. Miskatonic's
practitioner-calibrated construct interpretation is the resolution posture.

---

## Phase 4 Targets Derived From This PoC

1. Full extension module formalization (Motivation, Governance, Data extensions
   as first tranche)
2. Attribute schema modeling per construct
3. TOGAF 10th Edition Enterprise Metamodel version assessment and migration plan
4. Bureau construct validation engine: SPARQL queries against this ontology as the
   schema authority, executed against Ossuary artifact frontmatter
5. Cross-framework annotation layer: DoDAF, FEAF, ATAM mappings in msk: namespace
6. Ossuary reference tier API integration consuming ontology as validation schema

---

## How To Use This Artifact Now (PoC Mode)

The `.ttl` file is readable by any OWL 2.0 tooling: Protégé, TopBraid EDG,
WebProtégé, rdflib (Python), Apache Jena. As a PoC:

1. Load into Protégé or rdflib to visualize the construct graph
2. Query with SPARQL to validate Ossuary artifact construct declarations against
   legal relationships (e.g. does the declared primary construct have a legal
   relationship with its declared secondary construct per Figure 30-7?)
3. Use the msk:miskatonicPrimary annotations to identify which constructs need
   full Bureau scoring rubric coverage in Phase 2

---

## File Inventory

| File | Purpose | Status |
|---|---|---|
| OntologyTOGAFContentMetamodelV2-Miskatonic.ttl | OWL Turtle: construct graph + msk annotations | Present |
| FORK-GOVERNANCE.md | This document | Present |
| SPARQL/ | Validation query library for Bureau PoC | Phase 4 |
| extensions/ | Extension module OWL files | Phase 4 |

---

*This document is a governed platform artifact. Changes require a Miskatonic
governance decision recorded in Grimoire.*
