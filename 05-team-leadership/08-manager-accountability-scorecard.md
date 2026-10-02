---
name: manager-accountability-scorecard
description: Build an evidence-based manager accountability scorecard for a leadership meeting. Use for Monday scorecards, completion rates, overdue commitments, stalled delegated work, or questions about team delivery. Distinguish delivery risk from missing data and prepare a specific decision question for each supported risk.
---

# Manager Accountability Scorecard

A useful scorecard shows which commitments need help and which decisions are blocking delivery. Task counts alone cannot establish effort or employee performance.

> Tool placeholders refer to your connected systems. See [CONNECTORS.md](../CONNECTORS.md).

## How it works

| Mode | Inputs and result |
|---|---|
| Standalone | Paste task records, completion evidence and last week's commitments. Receive a scorecard with gaps clearly marked. |
| Connected | Read current tasks and dated history from ~~project tracker, agreed commitments from ~~meeting notes, and operating policies from ~~docs. |

## What I need from you

- Required: review date, timezone, team scope and task list with stable identifiers, owners, status and due dates where known.
- Required for weekly completion: the commitments agreed for the review window and dated completion evidence.
- Optional: approved extensions, dependency owners, working calendar, previous scorecard and company risk thresholds.
- A pasted count is acceptable as user-reported evidence. Label it as such; it cannot prove individual completion dates.

## Step 1: Define the window and scope

Default to the last seven calendar days ending at the review timestamp. Display the exact start and end, using an inclusive start and exclusive end for timestamp queries. Use the user's timezone.

Resolve current owners and delegated relationships from authoritative records. Do not infer ownership from a title or a frozen roster. Include the owner's tasks only when requested, in a separate section.

Deduplicate by stable task ID. Similar titles across client projects are not duplicates. Count co-owned work once in portfolio totals and disclose any shared attribution in person rows.

## Step 2: Verify outcomes and dates

Count completed work using completion timestamps or dated status history. A generic last-updated timestamp does not establish completion in the window.

Separate reopened tasks from currently accepted completed outcomes. Do not count the same outcome twice because it was closed twice. Preserve the source and confidence of each count.

A completed task with stale metadata is not overdue. Missing due dates are unknown, not on time. Exclude cancelled and archived work from the open backlog while reporting agreed cancellations separately.

Read blockers, approved extensions and holds before interpreting lateness. Show original and approved revised dates. Retain missed commitments in history even after a revision.

## Step 3: Calculate two different measures

| Measure | Formula | Meaning |
|---|---|---|
| Weekly commitment completion | Accepted commitments completed by window end / commitments agreed for that window × 100 | How much of the agreed weekly plan finished |
| Backlog clearance ratio | Verified completed outcomes in window / (verified completed outcomes + open tasks at review) × 100 | Throughput relative to the current pile; not a weekly plan completion rate |

Freeze the commitment cohort at the agreed planning point. Show additions, removals and scope changes separately so the denominator is not quietly rewritten. Work completed outside that cohort contributes to throughput, not its completion numerator.

Round displayed percentages to whole numbers. Use unrounded numbers for thresholds. A zero denominator is N/A. Missing completion evidence makes the affected metric UNKNOWN. Neither N/A nor UNKNOWN means zero delivery.

## Step 4: Assign delivery risk

Use company policy when supplied. These are starter review thresholds, not employee ratings:

| Band | Evidence required |
|---|---|
| RED | At least 3 confirmed overdue commitments, any commitment 14+ calendar days overdue, or weekly commitment completion below 20% after the agreed window closes |
| YELLOW | 1–2 confirmed overdue commitments, at least 4 explicitly unstarted tasks requiring a capacity discussion, or weekly completion from 20% through 50% after the window closes |
| GREEN | Sufficient evidence, no overdue commitments, no RED/YELLOW condition, and weekly completion above 50% |
| UNKNOWN | Evidence cannot establish a band; includes no agreed cohort and no other supported risk signal |

Evaluate RED, then YELLOW, then GREEN. Missing metrics do not erase a separately confirmed overdue risk. State which signal supports the band and which measures remain unknown. Do not use the backlog ratio as the weekly completion threshold.

Annotate leave, approved holds, dependency delays and data freshness without publishing private reasons. If data is mirrored, check the authoritative tracker before escalation. Use the documented synchronization allowance; do not invent a universal lag.

Four unstarted tasks prompt a capacity question, not a finding of negligence. No update for 14 days prompts an evidence check, not a conclusion that work never started.

## Step 5: Produce the scorecard

Use this template:

```text
ACCOUNTABILITY SCORECARD: [window] | [timezone]
Scope: [team and delegation rule]
Evidence current through: [timestamp / gaps]

| Owner | Open | Verified done | Overdue | Unstarted | Undated | Weekly completion | Backlog ratio | Risk and reason |
| ... |

Owner decisions blocking delivery:
- [Task ID/title, needed decision, impact, source]

Supported risks:
- [Owner, task, original/current due dates, age, blocker, evidence]

Meeting questions:
- [Owner]: [one specific question about an outcome or decision]

Data gaps and exceptions:
- [Missing cohort/history, source conflict, approved hold]

Proposed actions:
- [Exact record, change, reason, proposed date if applicable]
Executed actions: [none, or verified results under existing authorization]
```

Sort confirmed RED risks first, then YELLOW, then UNKNOWN requiring reconciliation, then GREEN. Within a band, sort by client impact, overdue count and age. Do not rank people by task count as a productivity contest.

## Step 6: Preserve history and obtain scoped authorization

This review does not automatically modify tasks or notify the team. Show exact records and changes before consequential writes unless the same action is already explicitly authorized. Verify each result and report failures separately.

Do not overwrite a description with a nudge. Do not reset all deadlines to Monday. Keep private 1:1 material out of shared scorecards. Dates proposed during the review are proposals until agreed.

## The rules that make this work

- Keep both measures named because a large future backlog can depress the ratio even when every weekly commitment was delivered.
- Use actual completion evidence because editing an old completed task should not create a new accomplishment.
- Ask about the blocking decision before the person because the agency owner may be the dependency.
- Keep an UNKNOWN band because false precision can turn a data problem into an unfair management judgment.
- Record corrections as proposed operating-policy updates so the same misunderstanding does not repeat next week.

## Worked example

Fictional input:

```text
week ended oct 2, review 5pm NY. delivery lead: 4 promised, all 4 accepted,
6 open for next month. account lead 0 promised, no open work, approved leave.
project lead 2 open overdue 3 and 5 days, old done item edited today,
no completion history exported. marketing lead 4 new tasks no dates.
```

Output:

```text
ACCOUNTABILITY SCORECARD: Sep 25 17:00 to Oct 2 17:00 | America/New_York
Scope: four supplied manager roles
Evidence: supplied export; project-lead completion history missing

| Owner | Open | Done | Overdue | Unstarted | Undated | Weekly | Backlog | Risk |
| Project lead | 2 | UNKNOWN | 2 | UNKNOWN | 0 | UNKNOWN | UNKNOWN | YELLOW: 2 confirmed overdue |
| Marketing lead | 4 | UNKNOWN | 0 confirmed | 4 | 4 | UNKNOWN | UNKNOWN | YELLOW: capacity check |
| Account lead | 0 | 0 | 0 | 0 | 0 | N/A | N/A | UNKNOWN: no cohort; approved leave |
| Delivery lead | 6 | 4 | 0 | 0 | 0 | 100% | 40% | GREEN |

Owner decisions: none identified in supplied notes; dependency details missing.
Questions:
- Project lead: what acceptance evidence and recovery plan exist for the two late commitments?
- Marketing lead: which of the four queued tasks is committed this week?
Gaps: an edit to an old done item cannot be counted as a completion today.
Proposed actions: retrieve missing history and agree dates for queued work.
Executed actions: none. No deadlines changed.
```

## Tips

1. Read owner-blocked items before asking the team for explanations.
2. Compare the same cohort and time window each week.
3. Separate a delivery conversation from an employment decision.
4. If a metric changes after a data repair, explain the repair beside the number.
5. A weekly schedule must be configured separately; this file installs no automation.

---
*Part of the ManagedCoder Agency Skills library. Use the same review rules each week and improve them with verified corrections.*
