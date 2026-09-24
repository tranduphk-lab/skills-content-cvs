# Output Contracts

Use human-readable Markdown by default. Use JSON for automation or multi-item handoff.

## Strategy contract

- status and planning horizon;
- business/marketing assumptions;
- primary and secondary audiences;
- decision journey;
- content objectives;
- pillar map;
- channel roles;
- KPI framework;
- governance, dependencies, and open questions.

## Plan contract

A detailed plan has two layers:

- **Calendar layer:** content ID, date/window, channel, format, pillar, CTA, KPI, owner, status, and dependency.
- **Content-unit layer:** for every planned content unit, use the compact AI-assisted structure Thông tin → Caption hoàn chỉnh → Prompt thiết kế.

The Notion representation must preserve both layers and the exact three section names. Do not sync a detailed plan as a calendar-only list.

Each row/item contains:

- content ID;
- date/window;
- objective and funnel stage;
- audience and tension;
- pillar, angle, awareness level;
- promise, format, channel, CTA;
- owner role, approver role;
- evidence/review status;
- production and publishing state;
- repurpose destination;
- test hypothesis.

## Idea contract

For each idea:

- title/direction;
- audience tension;
- pillar and awareness level;
- angle;
- primary promise;
- 2-3 hook directions;
- format/channel/CTA;
- source and review needs;
- score and rationale;
- status=`IDEA`.

## Brief contract

- metadata and status;
- strategic setup;
- creative setup;
- evidence and safety map;
- content spine;
- visual purpose;
- repurpose map;
- owner/approvers/dependencies;
- test plan.

## Content Production Package contract

Use when the user asks for full content, copy-ready content, image prompts, or production-ready output. Read `production-package-contract.md`. Default to the compact AI-assisted package: `Thông tin`, `Caption hoàn chỉnh` with per-image/frame copy, and `Prompt thiết kế` with visual/negative constraints. Use the expanded package only when a deep designer handoff, repurpose map, or approval dossier is requested. Do not mark it `PRODUCTION-READY` while product, source, asset, owner, or approval blockers remain.
## Measurement contract

- objective and expected signal;
- observed data;
- comparison/baseline;
- limitations;
- diagnosis by layer;
- decision;
- next test.

## JSON package minimum

```json
{
  "mode": "BRIEF",
  "brand": "Cavisi",
  "status": "REVIEW",
  "primaryAudience": "...",
  "primaryPromise": "...",
  "primaryCta": "...",
  "items": [],
  "sourceIds": [],
  "reviewMarkers": ["PRODUCT REVIEW"],
  "assumptions": [],
  "blockers": []
}
```

Allowed modes: `STRATEGY`, `PLAN`, `IDEATE`, `BRIEF`, `MEASURE`, `OPTIMIZE`.

Allowed statuses: `IDEA`, `DRAFT`, `REVIEW`, `PRODUCTION-READY`.


## Public content footer requirement

Every final public-facing output must include the canonical Cavisi contact footer at the end. Internal strategy, brief, measurement, and review artifacts are exempt unless they contain final publishable copy.


## Canonical footer

```text
Cavisi
Hotline/Zalo: 076 435 8668
Website: https://cavisi.vn
Địa chỉ: Toà Leadvisors Tower, 643 Đ. Phạm Văn Đồng, P, Nghĩa Đô, Hà Nội, Việt Nam
```




## Audience language requirement

Final public copy must use plain Vietnamese suitable for readers aged 30+. Any necessary English term must be explained in Vietnamese at first mention. Internal field names may remain English for machine readability.

