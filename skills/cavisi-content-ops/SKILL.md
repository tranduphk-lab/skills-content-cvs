---
name: cavisi-content-ops
description: "Build, plan, brief, measure, and optimize evidence-aware content for the Cavisi brand. Use for Cavisi content strategy, pillars, campaigns, calendars, topic banks, content briefs, channel plans, KPI reviews, repurposing, and optimization. Do not use for final video editing or rendering."
---

# Cavisi Content Ops

Turn Cavisi brand strategy into an executable content system without weakening its trust-first voice or upgrading unverified claims.

## Select the mode

Infer one primary mode from the request:

- `STRATEGY`: define content objectives, audiences, pillars, funnel roles, channel roles, and KPIs.
- `PLAN`: create a campaign, monthly plan, calendar, production map, or publishing schedule.
- `IDEATE`: generate and prioritize topics, angles, hooks, formats, CTAs, or series.
- `BRIEF`: turn an approved direction into a production-ready content brief or handoff package.
- `MEASURE`: interpret content results against the objective and evidence available.
- `OPTIMIZE`: decide what to keep, revise, stop, scale, or test next.

If the request asks for a full script or script review, use this skill to establish strategy, evidence, and brief, then route script work to `cvs-script-dna` when available. Route video editing, captions, EDL, and rendering to `tisa-ai-editor-agent` when available.

## Source priority

Resolve conflicts in this order:

1. Current user requirements and supplied records.
2. Approved legal, product, formula, science, claim, and channel records.
3. Current Cavisi brand package in the active workspace.
4. This skill's bundled guardrails and methods.
5. Reference-creator mechanisms, clearly abstracted rather than copied.
6. Creative proposals and assumptions, explicitly labeled.

Read [cavisi-brand-dna.md](references/cavisi-brand-dna.md) and [source-routing.md](references/source-routing.md) before loading project files. Do not load every brand document for every task.

## Global invariants

- Keep one primary audience, one primary promise, and one primary CTA per content unit unless the requested format genuinely requires otherwise.
- Preserve `Scalp-first`, `Shampoo làm sạch nền`, `Spray chăm sóc tiếp nối`, Sage-led/Caregiver-supported voice, and `rõ vai trò, rõ nguồn, rõ giới hạn`.
- Không sử dụng mascot, linh vật hoặc nhân vật đại diện của brand trong content, visual brief, storytelling, icon system, hoặc CTA.
- Separate brand philosophy, ingredient information, formula information, finished-product claims, and user outcomes.
- Never turn a reference creator's fear, borrowed authority, invented story, or unsupported performance claim into Cavisi content.
- Never promote `IDEA`, `DRAFT`, or `REVIEW` content as `PRODUCTION-READY`.
- Missing support becomes `[SOURCE REQUIRED]`, `[LEGAL REVIEW]`, `[SCIENCE REVIEW]`, `[PRODUCT REVIEW]`, or `[PUBLICATION REVIEW]`.
- Do not invent analytics, comments, testimonials, product facts, certifications, approvals, budgets, owners, or deadlines.
- A hook may intensify relevance, not the strength of a claim.

Read [brand-guardrails.md](references/brand-guardrails.md) and [language-policy.md](references/language-policy.md) whenever the task creates or evaluates public-facing content.

Also read [public-language-and-ai-voice.md](references/public-language-and-ai-voice.md) and [iconography.md](references/iconography.md) for public copy, visual suggestions, or image briefs.

Before finalizing public copy, apply [ai-writing-avoidance.md](references/ai-writing-avoidance.md) as a soft editorial audit. Do not treat any single sign as proof of AI authorship.

Read [contact-footer.md](references/contact-footer.md) and append the canonical footer to every public-facing content output.

## Core workflow

1. Establish objective, audience, funnel stage, channel, time horizon, constraints, and available evidence.
2. Identify the audience tension and current awareness level.
3. Select a pillar and angle using [ideation-method.md](references/ideation-method.md).
4. Define a proofable primary promise and one CTA.
5. Apply the Cavisi content spine:
   `clear hook -> valid tension -> Scalp-first reframe -> mechanism/role -> evidence -> limitation -> payoff -> CTA`.
6. Assign status: `IDEA`, `DRAFT`, `REVIEW`, or `PRODUCTION-READY`.
7. Match the deliverable to the relevant contract in [output-contracts.md](references/output-contracts.md).
8. Run a completion check: strategic fit, source status, claim strength, channel fit, owner, next action, and unresolved blockers.

## Mode routing

### STRATEGY

Read [strategy-method.md](references/strategy-method.md), [brand-guardrails.md](references/brand-guardrails.md), and the strategy contract in [output-contracts.md](references/output-contracts.md).

Do not confuse brand goals, marketing goals, content objectives, and content KPIs. State assumptions where business targets, distribution, pricing, or budget are absent.

### PLAN

Read [planning-method.md](references/planning-method.md), [channel-framework.md](references/channel-framework.md), and the relevant calendar or campaign contract.

A plan must be executable: include purpose, channel, format, owner role, dependency, review status, and publishing state. Use placeholders rather than invented people or dates.

When a detailed plan includes actual content units, every unit must use the compact AI-assisted output format:

1. Thông tin — metadata, audience, tension, objective, pillar, promise, CTA, KPI, status, source/review markers, and dependencies.
2. Caption hoàn chỉnh — copy for each image/frame, caption, CTA, Cavisi footer, and alt text when applicable.
3. Prompt thiết kế — prompt for the complete asset or each image/frame, including layout, Vietnamese text hierarchy, size, visual style, approved assets, icon direction, and negative constraints.

The calendar is the navigation layer, not a substitute for the content package. A detailed plan must keep the same three-part structure when synchronized to Notion; Notion sync must not remove, rename, or reorder these sections.

### IDEATE

Read [ideation-method.md](references/ideation-method.md), [hook-engine.md](references/hook-engine.md), and [awareness-ladder.md](references/awareness-ladder.md).

Generate from a matrix, not random brainstorming. Deduplicate by audience tension and primary promise, not title wording alone.

### BRIEF

Read [brief-method.md](references/brief-method.md), [brand-guardrails.md](references/brand-guardrails.md), and the brief contract.

When the user asks for a full content package, copy-ready content, designer handoff, image prompts, or production-ready output, also read [production-package-contract.md](references/production-package-contract.md). If the user wants a concise AI-assisted output, use the compact three-part structure: `Thông tin → Caption hoàn chỉnh → Prompt thiết kế`. Use the expanded structure only when the user asks for a deep designer handoff, repurpose map, or approval dossier.

Map each meaningful factual statement to a source/status. A visually detailed brief does not compensate for missing product or claim approval.

### MEASURE

Read [measurement-method.md](references/measurement-method.md). Distinguish observed data, comparison, interpretation, and recommendation. Do not infer causation from one post or one metric.

### OPTIMIZE

Read [optimization-method.md](references/optimization-method.md). Diagnose the likely layer before changing the asset: distribution, hook, promise, structure, proof, format, CTA, or audience fit. Change one major variable per test when practical.

## Practical retention mechanisms

The adapted mechanisms from the Duy Muối references are bundled in:

- [hook-engine.md](references/hook-engine.md)
- [everyday-to-insight.md](references/everyday-to-insight.md)
- [awareness-ladder.md](references/awareness-ladder.md)

Use the mechanisms, not the creator's identity, wording, fear tactics, claims, or sales pattern.

## Validation

For machine-readable handoffs, use the package schema in [output-contracts.md](references/output-contracts.md) and run:

```powershell
python scripts/validate_content_package.py path/to/package.json
```

The validator checks structure and statuses. It does not grant legal, product, scientific, brand, or publication approval.





