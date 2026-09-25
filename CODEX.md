# Cavisi Codex Operating Contract

This file defines the mandatory project-local skill architecture for Cavisi. It is loaded through `AGENTS.md` and applies whether the user explicitly names a skill or describes the task naturally.

## Skill hierarchy

### Parent skill

`skills/cavisi-content-ops/SKILL.md` owns source routing, brand invariants, content strategy, evidence classification, review markers, status, child routing, and final validation.

### Child skill

`skills/cavisi-copywriter/SKILL.md` writes, revises, reviews, adapts, batch-produces, or claim-checks copy from a bounded parent handoff. It does not own product truth, brand strategy, or approval.

Future child skills must follow the same authority boundary and be added to the routing table before use.

## Routing table

| Request | Required skill path |
|---|---|
| Strategy, pillars, campaign, calendar, topic bank, KPI, measurement, optimization | Parent only |
| Content brief or production package without final copy | Parent only |
| Caption, carousel/story copy, ad, landing copy, email, CTA, hook, or product copy | Parent -> Copywriter child -> Parent validation |
| Revision or channel adaptation of public copy | Parent source check -> Copywriter child -> Parent validation |
| Copy audit or claim check | Parent evidence rules -> Copywriter child review -> Parent decision |
| Video script strategy or brief | Parent; route execution to the script skill when available |
| Video editing, captions, EDL, or rendering | Route to the video-production skill when available |

## Mandatory lifecycle

1. **Inspect:** read the request and minimum relevant project sources.
2. **Normalize:** identify deliverable, audience, objective, channel, status, constraints, and evidence.
3. **Parent decision:** establish the brief, claim boundaries, review markers, and child mode.
4. **Handoff:** give the child a compact structured contract.
5. **Child execution:** create or evaluate copy without expanding facts or strategy.
6. **Parent validation:** check source fidelity, claim strength, tone, language, CTA, footer, and blockers.
7. **Report:** return the artifact and disclose assumptions, review markers, or blockers that affect use.

Do not expose private chain-of-thought. Return only decision summaries, work products, checks, and blockers.

## Parent-to-child handoff

Use this shape internally. Never omit claim status for public copy.

```yaml
mode: WRITE | REVISE | REVIEW | ADAPT | BATCH | CLAIM_CHECK
deliverable: "Requested copy artifact"
content_id: "Stable ID when available"
status: IDEA | DRAFT | REVIEW | PRODUCTION-READY
audience: "One primary audience"
audience_tension: "Observed or approved tension"
objective: "One primary communication objective"
channel: "Target channel and placement"
format: "Caption, carousel, story, ad, landing section, email, etc."
primary_message: "One proofable message"
primary_cta: "One CTA"
tone: "Approved Cavisi tone"
icon_policy: NONE | MINIMAL | STRUCTURAL | VISUAL_ASSET
source_ids: []
verified_facts: []
prohibited_claims: []
required_terms: []
required_footer: true
constraints: []
review_markers: []
output_contract: "Expected structure and length"
```

Missing facts become review markers or placeholders, never persuasive invention.

## Source priority

1. Current user requirements and supplied records.
2. Approved legal, product, formula, science, claim, and channel records.
3. Current Cavisi repository documents and decision registers.
4. Parent guardrails and methods.
5. Child-skill frameworks.
6. Creative inference, explicitly labeled.

Frameworks organize communication; they never create product truth.

## Claim gate

Classify every meaningful public claim:

- `VERIFIED`: supported and permitted for the requested use.
- `PROVIDED-UNVERIFIED`: supplied but not independently approved.
- `PLACEHOLDER`: missing information required before publication.
- `PROHIBITED`: outside the current evidence or brand boundary.

Only `VERIFIED` claims may be presented as settled public facts. Other classes must be qualified, marked for review, replaced safely, or omitted.

Never manufacture precision. Exact numbers, testimonials, research, certifications, prices, offer terms, deadlines, and performance results require an identified source.

## Status authority

- `IDEA`: direction only.
- `DRAFT`: internal review, not publication.
- `REVIEW`: copy exists but approvals remain.
- `PRODUCTION-READY`: sources, wording, assets, owners, links, and approvals are confirmed.

Child skills may recommend a status but cannot independently upgrade content to `PRODUCTION-READY`.

## Public-copy invariants

- Preserve `Scalp-first — bắt đầu từ da đầu` as a philosophy, not a treatment claim.
- Preserve `Shampoo làm sạch nền. Spray chăm sóc tiếp nối.` only at the approved role level.
- Keep one primary audience, message, and CTA per content unit.
- Use calm, useful, non-coercive Vietnamese for readers aged 30+.
- Default to `MINIMAL` icon use in captions and long-form social copy. Icons must guide scanning or distinguish meaning; they must not decorate every paragraph.
- Use one coherent icon style, no more than one icon marker per section heading, and no icons in the canonical footer.
- Do not use icons as punctuation, emotional reactions, evidence, certifications, medical authority, or substitutes for labels.
- Do not use appearance shame, disease fear, fake urgency, fake scarcity, hidden commands, identity pressure, invented authority, invented stories, or unsupported outcomes.
- Do not use mascot, brand character, or medical-looking visual authority.
- Final public copy ends with the canonical footer from `skills/cavisi-content-ops/references/contact-footer.md`.

## Direct invocation

If the user explicitly requests `$cavisi-copywriter`, reconstruct the parent handoff from context and repository. Do not bypass parent guardrails or force unnecessary angle approval.

Use guided angle selection only when requested or when direction is materially unresolved. If the user says "viết luôn", choose the strongest compliant direction and write directly.

## Completion check

- Correct channel and format.
- No unsupported fact or strengthened claim.
- Audience, promise, CTA, and status match the handoff.
- Required Vietnamese explanations and footer are present.
- Icon density matches the handoff policy and no icon can be removed without losing intended navigation or meaning.
- Review markers and blockers remain visible.
- Output is natural, specific, and free of unnecessary AI-style filler.
