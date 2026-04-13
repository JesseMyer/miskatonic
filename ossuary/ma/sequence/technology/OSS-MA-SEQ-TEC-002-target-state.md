---
ossuary_id: OSS-MA-SEQ-TEC-002
altitude: Sequence
domain: M&A Integration Architecture
state: Target State
output_type: Pattern
subsystem: Technology Domain
togaf_constructs:
  primary: [Process, Application Service]
  secondary: [Logical Application Component, Interface, Application Service]
adm_phase: omit
bureau_calibration: false
region: declared per engagement
parent_subsystem: OSS-MA-COM-TEC-002
---

# M&A Integration Architecture — Sequence Altitude — Technology Domain — Target State

## Altitude and Parentage

This pattern sits at **Sequence** altitude under the M&A Integration Architecture domain.
It sequences governed interaction order, control points, and handoffs for **Technology Domain**,
descending from Component pattern `OSS-MA-COM-TEC-002`. It does not restate Component inventory;
it orders how those components collaborate through time.

**Sequence focus:** platform provisioning order, deployment pipelines, and change windows.

## Entity A — Local Interaction Order

Entity A executes a coherent local sequence within its legacy boundary. Ordering is
implicit in application design and operations runbooks, not declared as an enterprise
sequence model. Retries, compensations, and idempotency keys are **application-local**.

## Entity B — Local Interaction Order

Entity B maintains a parallel local sequence with different orchestration assumptions,
different error semantics, and different monitoring. Sequences are **not comparable**
across entities without translation and reconciliation.

## Cross-Entity Sequence (As-Reported)

At target state, a single governed sequence model spans both entities. Each interaction declares a triggering Application Service, a consumer, delivery semantics, and a terminal condition aligned to the unified backbone.

## Ordering Guarantees and Control Points

| Control point | Declared? | Evidence | Bureau note |
|---|---|---|---|
| Start trigger | [per engagement] | [elicited/consumed] | Missing trigger is a qualification hold |
| Terminal condition | [per engagement] | [elicited/consumed] | Ambiguous terminal condition blocks typing |
| Idempotency strategy | [per engagement] | [design artifact] | Required for backbone-mediated hops |
| Compensation boundary | [per engagement] | [runbook/design] | Required before rationalization waves |

## Failure, Retry, and Compensation Posture

Dual entity operations produce **non-comparable** failure semantics until rationalized.
Sequence altitude requires explicit declaration of: maximum retry, dead-letter handling,
human intervention escalation path, and whether partial success is permitted.

## Architectural Risk Profile

| Risk | Severity | Broken construct relationship | Bureau suggestion |
|---|---|---|---|
| Invisible cross-entity hops | Critical | Application Service: orchestration outside governed boundary | Yes |
| Competing sequence semantics | High | Process: duplicate or conflicting terminal conditions | Yes |
| Missing idempotency | High | Application Service: unsafe replay under migration | Yes |
| Manual sequence bridges | High | Control: ungoverned compensating controls | Yes |

## Ossuary Notes

Sequence patterns must remain coherent with Subsystem and Component parents. Pelagic
wave gates may require sequence verification before advancing. Grimoire records sequence
changes as disposition decisions when cutover alters interaction order.
