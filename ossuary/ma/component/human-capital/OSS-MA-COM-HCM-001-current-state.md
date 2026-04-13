---
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
**HRIS Platform** — Logical Application Component. Employee record management, position management, organizational hierarchy, workforce reporting, onboarding and offboarding orchestration. Entity-local. Data Entity: Employee, Position, Organization, Compensation, Benefit.
**Payroll Platform** — Logical Application Component. Payroll calculation, tax withholding, payslip generation, payroll compliance. Entity-local. Jurisdiction-specific.
**Benefits Administration Platform** — Logical Application Component. Benefits enrollment, plan management, carrier integration, life event processing. Entity-local. Carrier contracts entity-local.
**Talent Acquisition System** — Logical Application Component (present or absent). Entity-local.
**HR Master** — Logical Data Component. Entity-local. Data Entities: Employee, Position, Organization, Compensation, Benefit.

### Entity B
**HRIS Platform** — Logical Application Component. Entity-local. Organizational hierarchy structure differs from Entity A.
**Payroll Platform** — Logical Application Component. Entity-local. Payroll rules may differ by jurisdiction.
**Benefits Administration Platform** — Logical Application Component. Entity-local. Benefit plans differ from Entity A. Carrier contracts non-aligned.
**Talent Acquisition System** — Logical Application Component (present or absent). Entity-local.
**HR Master** — Logical Data Component. Entity-local. Compensation model and org hierarchy non-aligned with Entity A.

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
| Benefit plan non-alignment | High | Logical Application Component: carrier contracts and plan types non-aligned | Yes |
| Payroll jurisdiction complexity | High | Logical Application Component: payroll rules differ by jurisdiction | Yes |
| Workforce rationalization authority undeclared | High | Organization Unit: no named owner for enterprise-wide workforce decisions | Yes |
| Organizational hierarchy non-aligned | High | Data Entity: Organization construct non-comparable | Yes |

## Qualification Holds
- Workforce rationalization authority: HR, EA, or joint governance?
- Compensation model harmonization: which entity's model or new construction? Legal, HR, and finance input required.
- Benefit plan harmonization scope: which plans survive? Legal and HR input required.
- Payroll jurisdiction scope: same jurisdictions or multi-jurisdiction governance required?

## Ossuary Notes

Human Capital Domain carries significant non-architectural dependencies. Compensation
harmonization, benefit plan rationalization, and payroll jurisdiction governance all
require legal, HR, and regulatory input before target state can be declared.