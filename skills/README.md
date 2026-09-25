# Cavisi Project-Local Skills

These skills are activated by the repository instructions in `../AGENTS.md` and the routing contract in `../CODEX.md`. They are not installed into the user's global Codex skill directory.

## Registry

| Skill | Role | May finalize approval? |
|---|---|---|
| `cavisi-content-ops` | Parent orchestrator for strategy, planning, evidence, briefs, measurement, optimization, routing, and final validation | Owns validation and status decisions, but cannot invent missing approvals |
| `cavisi-copywriter` | Child executor for writing, revision, adaptation, batch copy, review, and claim checks | No |

## Invocation

Natural-language requests are routed automatically through `AGENTS.md` and `CODEX.md` when work is performed inside this repository.

Direct invocation may name a local skill, for example:

```text
Use the project-local cavisi-copywriter skill to revise W01-03.
```

Direct child invocation still inherits parent brand, source, evidence, status, and footer rules.

## Adding a child skill

1. Create `skills/<skill-name>/SKILL.md` with a discriminating description.
2. Define the child's bounded authority and output contract.
3. Register the route and handoff fields in `../CODEX.md`.
4. Add the route to the parent skill when the parent must delegate to it.
5. Validate the skill folder and test a realistic request.
