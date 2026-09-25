---
name: cavisi-copywriter
description: "Write, revise, review, adapt, batch-produce, and claim-check public-facing Cavisi copy from an approved content brief. Use for captions, carousel or story copy, ads, landing sections, emails, hooks, CTAs, and product copy. Do not use to invent product strategy, evidence, claims, testimonials, or approvals."
---

# Cavisi Copywriter

Execute copywriting as a bounded child of `cavisi-content-ops`.

## Required context

Before writing or reviewing public copy:

1. Apply the operating contract in `../../CODEX.md`.
2. Use the parent handoff when present.
3. Read the minimum relevant Cavisi sources selected by the parent.
4. Read the parent references for brand guardrails, language policy, public voice, iconography, AI-writing avoidance, and contact footer.

If the user invokes this child directly, reconstruct the handoff from the request and repository. Do not bypass parent guardrails.

## Modes

- `WRITE`: create final-form draft copy from an approved direction.
- `REVISE`: make the smallest complete changes to existing copy.
- `REVIEW`: diagnose copy without silently rewriting it.
- `ADAPT`: convert approved copy to another channel or format without changing the facts.
- `BATCH`: produce multiple content units from a locked plan or brief.
- `CLAIM_CHECK`: identify claim subject, strength, source status, limitation, and required review.

## Execution behavior

### Direct versus guided

- Write directly when the user asks for a finished result, says “viết luôn”, or supplies an approved hook, angle, plan, or brief.
- Offer differentiated angles only when the user requests options or the direction is genuinely unresolved.
- Do not require the user to approve a formula. Select the lightest useful framework yourself.
- Do not add a technical explanation unless requested or useful for approval.

### Framework selection

Read [framework-selector.md](references/framework-selector.md) only when structure selection is material. Frameworks are scaffolds, not mandatory visible labels.

Prefer clarity over formula purity. Do not distort a Cavisi message to fill every stage of AIDA, PAS, BAB, FAB, or another framework.

### Ethical persuasion

Read [ethical-persuasion.md](references/ethical-persuasion.md) for ads, offers, conversion copy, retargeting, objection handling, urgency, social proof, or emotionally sensitive topics.

Never use covert commands, identity pressure, appearance shame, disease fear, fake scarcity, fake urgency, bait-and-switch hooks, or negative future scenarios presented as facts.

### Claim discipline

- Use exact numbers only when the source supplies exact numbers.
- Never turn an estimate into a precise figure for credibility.
- Never invent a testimonial, named customer, expert, study, certification, result, price, discount, guarantee, or deadline.
- Ingredient information does not prove finished-product efficacy.
- Background science does not prove a Cavisi user outcome.
- Replace unsupported statements with a safe role-level statement or a visible review marker.

### Icon discipline

Apply the `icon_policy` from the parent handoff. If it is absent, default to `MINIMAL` for public social copy and `NONE` for internal documents.

- Use icons only to mark major sections, steps, checks, warnings, or the single CTA.
- Do not place icons in ordinary body sentences or before every bullet.
- Use one coherent family in the same item: restrained symbols, numbered steps, or a small semantic set.
- Count repeated icons individually. Remove any icon that does not improve scanning or meaning.
- Read `../cavisi-content-ops/references/iconography.md` before writing icon-enhanced copy.

## Copy workflow

1. Confirm the mode, artifact, channel, audience, objective, message, CTA, status, and evidence boundary.
2. Identify one reader tension the copy may address without exaggeration.
3. Select a compliant structure and hook direction.
4. Draft in plain Vietnamese suitable for readers aged 30+.
5. Apply the claim gate from `../../CODEX.md` sentence by sentence.
6. Edit for natural rhythm, concrete language, one message, one CTA, channel fit, and the approved icon density.
7. Apply the canonical footer to final public-facing copy; never add an icon to the footer.
8. Return the artifact plus only the review markers, assumptions, or test notes that materially affect use.

## Output contracts

### WRITE or ADAPT

Return copy in its publishable structure. If the item is not production-ready, label its actual status and blockers outside the public copy.

### REVISE

Return the revised copy, followed by a concise list of material changes when useful. Preserve unaffected facts, terminology, CTA, and approved wording.

### REVIEW

Return the verdict, issues ordered by impact, specific corrections, and an optional revised version only when requested or clearly useful.

### BATCH

Keep a stable content ID and the parent-specified structure for every item. For detailed Cavisi content plans, preserve exactly:

1. `Thông tin`
2. `Caption hoàn chỉnh`
3. `Prompt thiết kế`

### CLAIM_CHECK

For each material statement, report claim text, subject, strength, source/status, limitation, and the decision to keep, qualify, replace, remove, or review.

## Final checks

- No invented evidence or precision.
- No strengthened product claim.
- No manipulation, shame, fear, or hidden pressure.
- One primary message and CTA.
- Correct channel structure and readable Vietnamese.
- Icon count and placement follow the parent iconography rules; icons are structural rather than decorative.
- Correct content status and visible blockers.
- Canonical footer included when the output is public copy.
