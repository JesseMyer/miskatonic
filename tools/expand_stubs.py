#!/usr/bin/env python3
"""
Expand stub Ossuary/Vril markdown: apply full bodies from agent transcript b70d0c10
where available; synthesize Sequence, Schema, and Vril M&A prompts to match corpus voice.
Run from repo root: python tools/expand_stubs.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
STUB_MARKERS = (
    "Retrieve from conversation history",
    "See conversation history for complete pattern body",
)

TRANSCRIPT = Path(
    r"C:\Users\jesse\.cursor\projects\c-Users-jesse-Documents-GitHub-miskatonic"
    r"\agent-transcripts\b70d0c10-20c8-4454-83a2-c623a2d4ff9a"
    r"\b70d0c10-20c8-4454-83a2-c623a2d4ff9a.jsonl"
)


def load_transcript_artifacts() -> dict[str, str]:
    line = TRANSCRIPT.read_text(encoding="utf-8").splitlines()[0]
    text = json.loads(line)["message"]["content"][0]["text"]
    if text.startswith("<user_query>"):
        text = text[len("<user_query>") :].lstrip("\n")
    if text.endswith("</user_query>"):
        text = text[: -len("</user_query>")].rstrip()

    pat = re.compile(r"(?m)^(OSS-[A-Z0-9-]+|VRL-[A-Z0-9-]+)\nmarkdown---\n")
    matches = list(pat.finditer(text))
    out: dict[str, str] = {}
    for i, m in enumerate(matches):
        id_ = m.group(1)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        chunk = text[start:end].rstrip()
        out[id_] = "---\n" + chunk
    return out


def parse_frontmatter(md: str) -> tuple[dict[str, str], str]:
    if not md.startswith("---"):
        return {}, md
    parts = md.split("---", 2)
    if len(parts) < 3:
        return {}, md
    raw = parts[1]
    body = parts[2].lstrip("\n")
    fm: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm, body


def is_stub(md: str) -> bool:
    return any(m in md for m in STUB_MARKERS)


def ossuary_fm_block(
    oss_id: str,
    altitude: str,
    subsystem: str,
    state: str,
    parent: str,
    primary: str,
    secondary: str,
) -> str:
    return (
        "---\n"
        f"ossuary_id: {oss_id}\n"
        f"altitude: {altitude}\n"
        "domain: M&A Integration Architecture\n"
        f"state: {state}\n"
        "output_type: Pattern\n"
        f"subsystem: {subsystem}\n"
        "togaf_constructs:\n"
        f"  primary: [{primary}]\n"
        f"  secondary: [{secondary}]\n"
        "adm_phase: omit\n"
        "bureau_calibration: false\n"
        "region: declared per engagement\n"
        f"parent_subsystem: {parent}\n"
        "---\n"
    )


def vril_fm_block(vril_id: str, altitude_key: str, out_slug: str) -> str:
    return (
        "---\n"
        f"vril_id: {vril_id}\n"
        f"altitude: {altitude_key}\n"
        "domain: M&A Integration Architecture\n"
        f"output_type: {out_slug}\n"
        "ossuary_dependency: OSS-MA patterns at matching altitude; declare specific ossuary_id in invocation\n"
        "bureau_calibration: false\n"
        "region: declared per engagement\n"
        "adm_phase: omit\n"
        "---\n"
    )


# --- Synthesis: domain metadata -------------------------------------------------

DOMAINS: dict[str, dict[str, str]] = {
    "integration": {
        "code": "INT",
        "label": "Integration Domain",
        "seq_theme": "message routing, broker topics, API hops, orchestration, and idempotency boundaries",
        "sch_theme": "integration payloads, canonical message schemas, identity correlation keys, and lineage across interfaces",
    },
    "customer": {
        "code": "CUS",
        "label": "Customer Domain",
        "seq_theme": "customer journey orchestration, identity resolution handoffs, consent and preference events",
        "sch_theme": "party, account, agreement, and consent entities; golden customer keys; privacy classification",
    },
    "product": {
        "code": "PRD",
        "label": "Product Domain",
        "seq_theme": "product lifecycle ordering, entitlement checks, and fulfillment handoffs",
        "sch_theme": "product, offering, price, and contract line structures; product-to-customer bindings",
    },
    "finance": {
        "code": "FIN",
        "label": "Finance Domain",
        "seq_theme": "journal posting sequences, intercompany eliminations, and close orchestration",
        "sch_theme": "chart of accounts, cost centers, legal entities, and subledger-to-GL reconciliation keys",
    },
    "human-capital": {
        "code": "HCM",
        "label": "Human Capital Domain",
        "seq_theme": "hire-to-retire process order, payroll cycles, and benefits enrollment events",
        "sch_theme": "worker, position, organization assignment, compensation, and payroll result entities",
    },
    "technology": {
        "code": "TEC",
        "label": "Technology Domain",
        "seq_theme": "platform provisioning order, deployment pipelines, and change windows",
        "sch_theme": "configuration items, environments, deployment artifacts, and operational telemetry schemas",
    },
}

STATE_TITLES = {
    "current-state": "Current State",
    "target-state": "Target State",
    "transition-state": "Transition State",
}

ALT_LABEL = {"SYS": "System", "SUB": "Subsystem", "COM": "Component", "SEQ": "Sequence", "SCH": "Schema"}

OUT_LABEL = {
    "narrative": "narrative",
    "diagram": "diagram",
    "scoring": "scoring rubric",
    "roadmap": "roadmap",
    "finding": "finding",
    "qualification": "qualification",
}


def synth_sequence(oss_id: str, folder: str, state_slug: str) -> str:
    d = DOMAINS[folder]
    state = STATE_TITLES[state_slug]
    code = d["code"]
    num = oss_id.split("-")[-1]
    parent = f"OSS-MA-COM-{code}-{num}"
    fm = ossuary_fm_block(
        oss_id,
        "Sequence",
        d["label"],
        state,
        parent,
        "Process, Application Service",
        "Logical Application Component, Interface, Application Service",
    )
    title = f"# M&A Integration Architecture — Sequence Altitude — {d['label']} — {state}"
    if state_slug == "current-state":
        cross = (
            "At current state, no governed cross-entity orchestration exists. Ad hoc file drops, "
            "manual reconciliations, and email-mediated handoffs bridge gaps. Bureau treats absent "
            "cross-entity sequence as a Control and Application Service governance finding."
        )
    elif state_slug == "target-state":
        cross = (
            "At target state, a single governed sequence model spans both entities. Each interaction "
            "declares a triggering Application Service, a consumer, delivery semantics, and a "
            "terminal condition aligned to the unified backbone."
        )
    else:
        cross = (
            "During transition, cross-entity sequences are explicitly staged: parallel operation, "
            "backbone-mediated routing, and wave-gated cutover. No silent sequence changes: every "
            "new hop is recorded and verified."
        )
    body = f"""\
{title}

## Altitude and Parentage

This pattern sits at **Sequence** altitude under the M&A Integration Architecture domain.
It sequences governed interaction order, control points, and handoffs for **{d['label']}**,
descending from Component pattern `{parent}`. It does not restate Component inventory;
it orders how those components collaborate through time.

**Sequence focus:** {d["seq_theme"]}.

## Entity A — Local Interaction Order

Entity A executes a coherent local sequence within its legacy boundary. Ordering is
implicit in application design and operations runbooks, not declared as an enterprise
sequence model. Retries, compensations, and idempotency keys are **application-local**.

## Entity B — Local Interaction Order

Entity B maintains a parallel local sequence with different orchestration assumptions,
different error semantics, and different monitoring. Sequences are **not comparable**
across entities without translation and reconciliation.

## Cross-Entity Sequence (As-Reported)

{cross}

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
"""
    return fm + "\n" + body


def synth_schema(oss_id: str, folder: str, state_slug: str) -> str:
    d = DOMAINS[folder]
    state = STATE_TITLES[state_slug]
    code = d["code"]
    num = oss_id.split("-")[-1]
    parent = f"OSS-MA-SEQ-{code}-{num}"
    fm = ossuary_fm_block(
        oss_id,
        "Schema",
        d["label"],
        state,
        parent,
        "Data Entity, Logical Data Component",
        "Physical Data Component, Data Entity, Information System Service",
    )
    title = f"# M&A Integration Architecture — Schema Altitude — {d['label']} — {state}"
    if state_slug == "current-state":
        keys = (
            "Current state: multiple candidate keys per domain; matching rules are local and often manual."
        )
    elif state_slug == "target-state":
        keys = (
            "Target state: one canonical key per master domain; automated identity resolution with "
            "explicit exception handling."
        )
    else:
        keys = (
            "Transition: staged reconciliation, golden-record pilot, and explicit freeze rules for "
            "competing writes."
        )
    body = f"""\
{title}

## Altitude and Parentage

This pattern sits at **Schema** altitude under the M&A Integration Architecture domain.
It declares the governed data shapes, keys, lineage, and authority for **{d['label']}**,
descending from Sequence pattern `{parent}`. It names what must be true in data for the
declared sequences and components to be coherent.

**Schema focus:** {d["sch_theme"]}.

## Logical Data Inventory (As-Reported)

| Data entity (candidate) | Authority | Notes |
|---|---|---|
| [Primary business entities] | Contested across entities | No single MDM authority |
| [Reference data] | Duplicated masters | Drift between entities |
| [Transactional artifacts] | System-local stores | Reconciliation required for cross-entity reporting |

## Key Strategy and Identity

{keys}

## Lineage and Transformation

Declare how data moves from origin systems to consumers: batch vs. near-real-time,
transformations applied, and where semantic drift is introduced. Bureau scores lineage
gaps as Data Entity relationship defects.

## Privacy, Classification, and Regulatory Constraints

Declare classification per attribute where relevant. Schema altitude is where residency,
retention, and purpose-limitation constraints bind to fields and entities.

## Architectural Risk Profile

| Risk | Severity | Broken construct relationship | Bureau suggestion |
|---|---|---|---|
| Contested master for a domain | Critical | Data Entity: no authoritative Logical Data Component | Yes |
| Undocumented lineage | High | Data Entity: transformations not traceable | Yes |
| Key collision across entities | High | Data Entity: identifier semantics incompatible | Yes |

## Ossuary Notes

Schema patterns must align with Sequence and Component parents. Bureau references
Ossuary reference tier when suggesting remediation for MDM and lineage controls.
"""
    return fm + "\n" + body


def synth_vril(vril_id: str, alt_code: str, out_slug: str) -> str:
    alt = ALT_LABEL[alt_code]
    ol = OUT_LABEL[out_slug]
    fm = vril_fm_block(vril_id, alt_code.lower(), out_slug)
    title = f"# Vril Prompt — {vril_id} — {alt} — {ol}"
    body = f"""\
{title}

## Purpose

Invoke Vril to produce a **{ol}** deliverable for M&A Integration Architecture work at
**{alt}** altitude. The output must be traceable to declared Ossuary patterns and must
declare assumptions, boundaries, and unresolved holds explicitly.

## Invocation

You are operating inside the Miskatonic governed practice. Use the active engagement
region from Vril frontmatter. Cross-check elicited statements against consumed artifacts.
Where construct typing is ambiguous, emit a **qualification hold** rather than inventing
types.

## Required Inputs (minimum)

- Declared wave (if transition work) and Pelagic gate context
- Relevant Ossuary pattern IDs at {alt} altitude (name them explicitly)
- Stakeholder quotes vs. document citations (dual-track when both exist)
- Known Bureau findings that constrain the answer

## Output Contract — {ol}

{"Produce a structured narrative with headings: Context, Evidence, Interpretation, Risks, Next actions. Cite Ossuary fields by ID where applicable." if out_slug == "narrative" else ""}\
{"Produce a diagram specification: nodes, edges, swimlanes, and legend. Prefer Mermaid when possible; if not, provide a rigorous textual graph. Declare what is unknown." if out_slug == "diagram" else ""}\
{"Produce a scoring sheet: criteria, weight, evidence required per criterion, and Bureau mapping from score to suggestion class." if out_slug == "scoring" else ""}\
{"Produce a roadmap: waves, entry/exit criteria, dependencies, and explicit sequencing risks. Align to Pelagic wave structure where System transition patterns apply." if out_slug == "roadmap" else ""}\
{"Produce a Bureau-style finding: severity, broken construct relationship, evidence, suggested remediation tier (Ossuary reference tier), and whether the finding blocks descent." if out_slug == "finding" else ""}\
{"Produce a qualification prompt: single construct candidate, single decisive question, possible resolutions with typing implications, and which Ossuary fields are held." if out_slug == "qualification" else ""}

## Ossuary Notes

Bind outputs to explicit `ossuary_id` references. Do not silently merge domains.
Record unresolved items as holds for Bureau adjudication at the altitude boundary.

## Bureau Hooks

Declare whether the output implies a new finding, updates an existing finding, or closes
a finding. If investment or policy commitment is implied, flag as Course of Action touch.
"""
    return fm + "\n" + body


def apply_transcript(artifacts: dict[str, str]) -> int:
    n = 0
    for path in REPO.rglob("*.md"):
        if path.parts and path.parts[0] == "tools":
            continue
        rel = path.relative_to(REPO)
        text = path.read_text(encoding="utf-8")
        if not is_stub(text):
            continue
        fm, _ = parse_frontmatter(text)
        oid = fm.get("ossuary_id")
        vid = fm.get("vril_id")
        key = oid or vid
        if not key:
            continue
        if key not in artifacts:
            continue
        # Skip System patterns already fully populated in repo (no stub)
        if key.startswith("OSS-MA-SYS-"):
            continue
        path.write_text(artifacts[key], encoding="utf-8")
        n += 1
    return n


def synthesize_remaining() -> int:
    n = 0
    for path in REPO.rglob("*.md"):
        if path.parts and path.parts[0] == "tools":
            continue
        text = path.read_text(encoding="utf-8")
        if not is_stub(text):
            continue
        rel = path.relative_to(REPO).as_posix()
        name = path.name

        # ossuary/ma/sequence/<folder>/OSS-MA-SEQ-...
        m = re.match(
            r"ossuary/ma/sequence/([^/]+)/OSS-MA-SEQ-([A-Z]+)-(\d{3})-(.+)\.md$",
            rel,
        )
        if m:
            folder, _code, num, state_slug = m.groups()
            oss_id = f"OSS-MA-SEQ-{_code}-{num}"
            path.write_text(synth_sequence(oss_id, folder, state_slug), encoding="utf-8")
            n += 1
            continue

        m = re.match(
            r"ossuary/ma/schema/([^/]+)/OSS-MA-SCH-([A-Z]+)-(\d{3})-(.+)\.md$",
            rel,
        )
        if m:
            folder, _code, num, state_slug = m.groups()
            oss_id = f"OSS-MA-SCH-{_code}-{num}"
            path.write_text(synth_schema(oss_id, folder, state_slug), encoding="utf-8")
            n += 1
            continue

        m = re.match(r"(VRL-MA-(?:SYS|SUB|COM|SEQ|SCH)-\d{3})-(\w+)\.md$", name)
        if m and "vril/ma/" in rel:
            vril_id, out_slug = m.groups()
            alt_code = vril_id.split("-")[2]  # SYS, SUB, ...
            path.write_text(synth_vril(vril_id, alt_code, out_slug), encoding="utf-8")
            n += 1
            continue

    return n


def main() -> None:
    if not TRANSCRIPT.is_file():
        raise SystemExit(f"Transcript not found: {TRANSCRIPT}")
    artifacts = load_transcript_artifacts()
    print(f"Loaded {len(artifacts)} artifacts from transcript")
    a = apply_transcript(artifacts)
    print(f"Applied transcript bodies: {a} files")
    b = synthesize_remaining()
    print(f"Synthesized bodies: {b} files")

    left = []
    for path in REPO.rglob("*.md"):
        if path.parts and path.parts[0] == "tools":
            continue
        t = path.read_text(encoding="utf-8")
        if is_stub(t):
            left.append(path.relative_to(REPO))
    if left:
        print("WARNING: stub markers remain in:")
        for p in left[:30]:
            print(" ", p)
        if len(left) > 30:
            print(f"  ... and {len(left) - 30} more")
        raise SystemExit(1)
    print("OK: no stub markers remain.")


if __name__ == "__main__":
    main()
