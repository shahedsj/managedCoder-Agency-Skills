---
name: capacity-overload-review
description: Identify agency team overload, hidden bottlenecks, and unsafe workload concentration using allocations, active work, deadlines, blockers, and role criticality. Use before accepting new work, during weekly staffing reviews, when delivery slips across several projects, when one person owns too many critical items, or whenever an agency owner asks who is overloaded and what should be moved.
---

# Capacity & Overload Review

Do not diagnose overload from task count alone.

A person with 20 small tasks may have room. A person with 4 critical-path responsibilities across 4 clients may be the real bottleneck.

## Inputs

Best case:

- available capacity by person/role
- project allocations or planned hours
- active work and deadlines
- critical-path ownership
- PTO/leave
- blocked work
- recent completed work or utilization

Standalone mode can work from a rough team list and active commitments.

Connected mode may use `~~project tracker`, `~~time tracking`, `~~calendar`, `~~HR`, `~~resource planning`, and Agency Brain.

## Step 1 - Separate capacity from execution problems

Classify each concern before recommending reassignment:

| Type | Meaning |
|---|---|
| **OVERLOAD** | More committed work than credible available capacity |
| **CONCENTRATION RISK** | Too much critical knowledge/ownership depends on one person |
| **BLOCKED** | Capacity exists but work cannot move because of a dependency |
| **PRIORITY CONFLICT** | Several items are all being treated as top priority |
| **WORK HYGIENE** | Stale statuses, missing estimates, or bad planning make capacity impossible to judge |
| **PERFORMANCE QUESTION** | Commitments repeatedly miss despite apparently reasonable load; needs management review, not an automatic workload diagnosis |

Do not label performance as overload without evidence.

## Step 2 - Calculate load when hours are available

For the review window:

```text
planned_load = committed delivery hours + recurring internal hours + known meeting/admin load
available_capacity = working hours - leave - protected non-delivery time
load_ratio = planned_load / available_capacity
```

Default interpretation:

- under 80%: room exists
- 80-100%: healthy/full depending on role and uncertainty
- 100-115%: overload risk
- above 115%: high overload risk

These are starter thresholds, not universal truths. Use the agency's documented capacity rules when available.

## Step 3 - Use proxy signals when hours are missing

Do not invent utilization.

Use qualitative risk signals:

- owns critical work on 3+ simultaneous projects
- 3+ urgent/high items due in the same 5-day window
- repeated overdue work across different clients
- several teams waiting on the same person
- planned leave with no coverage for critical ownership
- only person who can approve, deploy, estimate, or access a critical system
- new work accepted without anything being moved

Label the result `proxy-based` and lower confidence.

## Step 4 - Apply hard overrides

Flag HIGH risk when:

- a single person is the only owner of multiple client-critical paths and is unavailable or overloaded
- committed load exceeds 115% with no explicit tradeoff
- a key role has no coverage and a material deadline falls during absence
- several projects are blocked on the same person for decisions or execution

## Step 5 - Recommend a tradeoff

Every overload recommendation must change at least one of:

- owner
- scope
- sequence
- deadline
- staffing
- priority

`Work harder` is not a capacity plan.

Route work by role and work type. Do not invent a specific person unless the data shows that person's role, capacity, and ownership make the move credible.

## Output

```markdown
# Capacity & Overload Review - [period]

## Highest risks
1. **[Role/person] - HIGH**
   - Type: OVERLOAD / CONCENTRATION / BLOCKED / PRIORITY CONFLICT / HYGIENE
   - Evidence: [facts]
   - Load: [ratio or proxy-based]
   - Work at risk: [projects/client commitments]
   - Recommended tradeoff: [move/defer/swap/add coverage]
   - Decision owner: [role]

## Team view
| Person/Role | Load | Risk | Critical commitments | Recommended change |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Coverage gaps
- [single point of failure / leave / missing backup]

## Owner decisions
- [only the tradeoffs requiring owner authority]

## Data gaps
- [missing allocations/estimates/etc.]
```

Show the 3 highest risks first. Do not bury them under a full staffing table.

## Rules

**Do not use task count as utilization.**

**Do not punish the most transparent person.** Someone with accurate task updates can look busier than someone whose work is not tracked.

**Do not automatically reassign work.** Show the proposed move, affected commitments, and tradeoff. Wait for approval before changing systems.

**Distinguish blocked from overloaded.** Adding another person does not fix a missing client approval.

**Protect management capacity too.** PM/account/technical-lead overload can create more delivery risk than individual contributor utilization shows.

**Use Agency Brain when available.** Check role definitions, escalation paths, skills, coverage rules, and prior staffing decisions. Current availability data wins over stale profiles.

## What good looks like

The review should make the agency choose what moves before accepting another commitment.