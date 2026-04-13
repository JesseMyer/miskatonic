---
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

A qualification prompt is issued when an Ossuary pattern encounters a construct that
cannot be typed from available information alone. It surfaces the minimum questions
required to confirm the construct type before the pattern declaration is finalized.

Qualification prompts are not discovery prompts. They are precise, single-construct-targeted
elicitation instruments. One unresolved construct, one qualification prompt. Do not batch
unrelated constructs into a single prompt.

## Trigger Conditions

Issue a qualification prompt when any of the following are true:

- A Value Stream candidate exists but its terminal condition is unknown.
- A Process candidate exists but its regulatory or governance anchor is undeclared.
- A Business Service candidate exists but its consumer and delivery boundary are unconfirmed.
- A Contract candidate exists but its governing obligation is undeclared.
- A Capability candidate exists but its delivering Organization Unit is contested or unknown.
- Any construct relationship in the TOGAF full metamodel cannot be confirmed from available evidence.

## Batching Rule

Qualification holds accumulate within an altitude. They are batched and issued at the
altitude boundary, not one at a time as they are discovered. Bureau decides per hold
whether an unresolved qualification hold blocks descent to the next altitude.

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

Qualification prompt answers are taken at face value unless they contradict consumed
documentation. If an answer contradicts consumed documentation, flag the contradiction.
Do not apply dual-track by default to all qualification answers.

## Resolution Protocol

1. Confirm construct type against resolution conditions.
2. Update Ossuary pattern: replace pending row with confirmed declaration.
3. Name the triggering Capability explicitly.
4. Declare the terminal condition.
5. Close the qualification hold in the pattern's Ossuary notes.
6. Update Bureau finding status if applicable.
7. Record resolution in Grimoire: prompt ID, question, answer, construct declared, pattern updated.

## Recording

Every resolved qualification hold is recorded in both Grimoire and the Ossuary pattern
inline. Dual record, always.

## Qualification Hold vs Bureau Finding

A qualification hold is not a finding. It is governed incompleteness. A Bureau finding
is opened only when: a qualification prompt has been issued and not answered within the
declared engagement timeline; a construct has been typed without qualification where
qualification was required; or a pattern has been advanced to a lower altitude before
all qualification holds at the current altitude are resolved.

## Ossuary Notes

Domain-agnostic and altitude-agnostic. Applies wherever a construct typing decision
cannot be made from available evidence. All Vril prompts that encounter unresolvable
construct candidates must issue a qualification prompt before pattern closure. Grimoire
records every qualification prompt issued, answered, and resolved across all engagements.