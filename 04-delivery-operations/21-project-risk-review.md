---
name: project-risk-review
description: Run a red-yellow-green agency project review using milestone, blocker, ownership, client dependency, scope, capacity, and budget evidence, then produce a concrete recovery action. Use for weekly delivery reviews, PM reviews, portfolio reviews, client escalation prep, or whenever an agency owner asks which projects are at risk and what should happen next.
---

# Project Risk Review

A project status is useful only when it predicts trouble early enough to change the outcome.

Classify projects GREEN, YELLOW, or RED from evidence. Do not let a manually selected status hide contradictory delivery signals.

## Inputs

Standalone: project plan, milestone dates, task list, blockers, client dependencies, scope changes, staffing notes, budget/time data, and recent status notes.

Connected: `~~project tracker`, `~~time tracking`, `~~meeting notes`, `~~email`, `~~finance`, and Agency Brain.

## Step 1 - Review six risk dimensions

Score each 0-2.

### Schedule
- 0: milestone plan credible and on track
- 1: minor slippage or compressed buffer
- 2: milestone missed, critical path blocked, or deadline no longer credible

### Ownership
- 0: critical work has clear owners and dates
- 1: one important item is unclear or stale
- 2: multiple critical items unassigned, no recovery owner, or repeated silence

### Dependencies
- 0: dependencies available or actively managed
- 1: dependency late but recovery exists
- 2: client/vendor/internal dependency blocks critical work with no resolution date

### Scope
- 0: scope stable
- 1: ambiguity or minor additions
- 2: material unapproved change, acceptance criteria drift, or repeated free additions

### Capacity
- 0: team capacity supports plan
- 1: key person near capacity or competing priority threatens delivery
- 2: critical role unavailable/overloaded and no replacement or sequencing plan

### Commercial
- 0: budget/burn consistent with progress
- 1: burn, billing, or margin concern needs review
- 2: material overrun, unpaid work affecting delivery, or project economics no longer support current plan

Total: 0-12.

## Step 2 - Apply hard overrides

Set RED when any apply:

- committed client milestone is already missed and no accepted recovery date exists
- production/security issue prevents the client from operating
- critical path has no owner
- budget is exhausted while material committed work remains
- project is blocked by a dependency with no owner and no resolution path

Set at least YELLOW when:

- milestone is due within 7 days and a required dependency is not ready
- two or more high-priority tasks are overdue
- the project has had no meaningful status update for 7+ days
- scope is changing without documented commercial decision
- one critical team member owns too many simultaneous critical-path items

Use the agency's documented thresholds when they exist. State which thresholds were used.

## Step 3 - Set R/Y/G

| Total risk | Status |
|---|---|
| 0-2 | GREEN |
| 3-6 | YELLOW |
| 7-12 | RED |

Hard overrides win.

If key evidence is missing, do not fake precision. Use `UNKNOWN` for the affected dimension and lower confidence.

## Step 4 - Find the leading indicator

Choose the single signal most likely to make the project worse next week if ignored.

Examples:

- approval not received before development milestone
- one critical integration has no working test environment
- client feedback aging while launch date stays fixed
- scope additions consuming capacity planned for committed work
- PM has no updated recovery plan after missed milestone

This is more useful than listing every overdue task.

## Step 5 - Define recovery

For YELLOW or RED, specify:

- recovery owner role
- next concrete action
- deadline
- what gets deprioritized or changed
- evidence that would move the project one level healthier

Do not say `monitor closely` without a trigger and owner.

## Output

For one project:

```markdown
# Project Risk Review - [Project]
**Status:** GREEN / YELLOW / RED
**Confidence:** High / Medium / Low
**Leading indicator:** [one]

## Evidence
- [fact] - source/date

## Risk score
| Dimension | Risk | Why |
|---|---:|---|
| Schedule | 0-2 | ... |
| Ownership | 0-2 | ... |
| Dependencies | 0-2 | ... |
| Scope | 0-2 | ... |
| Capacity | 0-2 | ... |
| Commercial | 0-2 | ... |

## Recovery
**Owner role:** [role]
**Action:** [specific]
**By:** [date]
**Tradeoff:** [what changes to make recovery credible]
**Green/yellow signal:** [measurable evidence]

## Owner decision
[Only if owner authority is actually required]
```

For a portfolio, show RED projects first and cap detail to the top 5 risk projects unless the user asks for all.

## Rules

**Do not trust the stored R/Y/G status by itself.** Recompute from current evidence and show disagreement.

**Do not call client dependencies the root cause when internal follow-up was weak.** Show both.

**Do not invent recovery dates.** If no one has committed to a date, write `NO DATE SET` and flag it.

**Do not hide tradeoffs.** A recovery plan that adds work without removing time, scope, or capacity is not a plan.

**Do not write changes automatically.** Preview task updates, milestone changes, status changes, or client communication and wait for approval.

**Use Agency Brain when available.** Compare against prior project decisions, scope exceptions, lessons learned, and client commitments. Flag stale or conflicting knowledge.

## What good looks like

A PM or owner should be able to read the review and know exactly what will make the project safer this week.