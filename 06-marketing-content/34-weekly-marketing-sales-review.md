---
name: weekly-marketing-sales-review
description: Run an agency's weekly marketing and sales review from prior commitments through evidence, pipeline movement, a decision agenda and post-meeting follow-through. Use for weekly growth meetings, marketing/BD prep, campaign accountability, idea backlogs, website checks or closing a sales-marketing meeting. Draft actions without inventing results or sending updates automatically.
---

# Weekly Marketing & Sales Review

Marketing activity and sales activity need a shared review of what changed for the business. This workflow turns last week's promises into a short decision agenda and keeps new ideas separate from approved work.

> Tool placeholders refer to your connected systems. See [CONNECTORS.md](../CONNECTORS.md).

## How it works

| Mode | What it does |
|---|---|
| Standalone | Paste the last meeting's commitments, current tasks, campaign results and pipeline changes. Receive a scorecard and decision agenda. |
| Connected | Read ~~calendar, ~~meeting notes, ~~project tracker, ~~CRM and approved strategy in ~~docs. Use ~~email and ~~chat only within authorized scope. |

## What I need from you

Choose one:

1. “Prepare our weekly review,” with the previous meeting notes and current records.
2. “Just the scorecard,” with agreed commitments and completion evidence.
3. “Close the meeting,” with the actual transcript or notes and existing task references.

Required: review window, timezone, team scope and available evidence.

Useful: campaign objectives, approved offers and pricing, target market, conversion definitions, idea backlog, next meeting and prior report. Retrieve changing company facts from current sources rather than embedding them here.

## Step 1: Establish the meeting and team scope

Find the relevant meeting instance and last completed meeting. A recurring calendar slot does not prove the last meeting took place. If no meeting tool exists, use supplied notes and label coverage.

Verify current owners and attendees. Do not expand the distribution list from an old roster. If only one part of the workflow is requested, perform only that part.

Use a seven-day review window by default and display exact boundaries. Respect a biweekly meeting cadence when supplied; do not relabel a 14-day report as weekly.

## Step 2: Reconcile promises against outcomes

For every commitment in the prior meeting, find the task or documented outcome. Match stable references and context before relying on similar titles.

| Evidence | Classification |
|---|---|
| Accepted outcome with dated completion evidence | Completed |
| Current work with a verified owner and next step | In progress |
| Documented dependency preventing progress | Blocked; name dependency owner |
| Commitment exists but no matched task | Untracked commitment; do not claim no work happened |
| Sources disagree or are missing | Needs verification |

Keep original and approved revised dates. Never infer completion from generic updated timestamps. Missing data in a mirrored system is not zero activity.

## Step 3: Build the accountability view

Use the [Manager Accountability Scorecard](../05-team-leadership/08-manager-accountability-scorecard.md) definitions when available. This file also works by itself:

- Weekly completion = completed commitments in the agreed window cohort / all commitments agreed for that cohort × 100.
- Backlog clearance ratio = verified completed outcomes / (verified completed outcomes + current open tasks) × 100.
- These measures answer different questions. Do not label the second as weekly completion.
- Zero denominator is N/A. Missing cohort or completion history is UNKNOWN.
- Freeze the agreed cohort; disclose additions, removals and scope changes separately.

Starter review thresholds, overridden by documented agency policy:

| Band | Condition |
|---|---|
| RED | 3+ confirmed overdue commitments, one 14+ calendar days overdue, or weekly completion below 20% after the window closes |
| YELLOW | 1–2 overdue, 4+ explicitly unstarted tasks needing a capacity check, or weekly completion 20–50% after the window closes |
| GREEN | No RED/YELLOW condition, no overdue commitments, sufficient evidence and weekly completion above 50% |
| UNKNOWN | Evidence does not support a classification |

Evaluate RED first. A confirmed overdue risk still counts if the completion metric is unknown. Explain the triggering signal. Account for approved leave, holds and owner-blocked decisions without disclosing private reasons.

## Step 4: Connect marketing output to sales movement

Show counts with sources and dates. Separate:

- Delivered assets and verified live posts from drafts or scheduled items.
- Qualified leads from all responses.
- Meetings held from meetings booked.
- New opportunities from stage changes in existing ones.
- Signed work from proposals and forecast.

Use the agency's qualification and revenue definitions. If definitions are absent, report raw observations and request definitions before assigning labels.

Compare with the prior equivalent window only when scope and tracking are comparable. Missing analytics means unavailable, not zero. Do not claim a post caused revenue merely because it preceded a deal.

Surface opportunities without next actions and cross-team handoffs without an owner. Verify active account ownership before proposing outreach; a sales review is not authorization to contact a prospect.

## Step 5: Keep ideas separate from commitments

Capture raw ideas as backlog proposals. Promote an idea to execution only after a decision to act. Before creating work, check for an existing task with the same outcome.

Every promoted idea needs a desired result, owner, acceptance evidence and agreed date or explicit date gap. Avoid turning every meeting comment into a task.

Record approved operating-rule corrections separately from raw ideas so future reviews can improve without treating speculation as company policy.

## Step 6: Check the customer-facing path

When in scope, inspect the supplied website, campaign landing page and recent social posts:

- Does the offer match approved service capability and pricing?
- Does the main call to action reach its intended destination?
- Did scheduled content actually publish?
- Is there a material contradiction between campaign promise and delivery capacity?

Check visible evidence through authorized tools. A scheduled flag is not publication proof. If rendering or access prevents verification, name the limitation. Do not submit live forms or create test leads without authorization.

Recommend tasks only for concrete breakage, misleading claims or material positioning drift. Minor taste preferences belong in a separate optional note.

## Step 7: Draft a decision agenda

Suggested 30-minute agenda, adjustable to the meeting's actual duration:

1. Five minutes: outcomes and prior commitments.
2. Ten minutes: blocked commitments and pipeline handoffs.
3. Ten minutes: no more than three decisions, including new ideas.
4. Five minutes: accepted actions, owners and dates.

Each question names the specific commitment, observed evidence and decision needed. Do not use a generic “status update” as the agenda.

## Step 8: Close the loop after the meeting

Use the actual notes or transcript. If missing, prepare the empty structure and request the source; do not mark the meeting completed or invent decisions.

Return recap, decisions, actions, risks, open questions and knowledge candidates. Match proposed actions to existing tasks before suggesting new records. Keep next-action dates separate from hard delivery deadlines.

Show exact destinations and changes before consequential writes or sends unless existing explicit authorization covers the same action. Verify persisted outcomes. A saved recap does not prove tasks were created or messages delivered.

## Output

```text
WEEKLY MARKETING & SALES REVIEW: [window, timezone]
Evidence coverage: [sources, refresh dates, missing data]

Results:
| Measure | Current window | Prior comparable window | Evidence / caveat |
| ... |

Commitments:
| Owner | Outcome | Original/current date | Verified status | Weekly completion | Risk / reason |
| ... |

Decisions for [meeting]:
1. [Specific question, owner, evidence, recommendation]
2. [Optional]
3. [Optional]

Ideas: [remain backlog / approved for execution / needs decision]
Website/social findings: [verified issue or verification unavailable]

After meeting, if actual notes supplied:
Recap: [...]
Decisions: [...]
Actions: [existing/new task proposal, owner, date, acceptance evidence]
Risks: [...]
Open questions: [...]
Knowledge candidates: [rule corrections, separate from facts]

Proposed writes/sends: [destination and exact scope]
Executed: [none / verified results and failures]
```

## The rules that make this work

- Reconcile last week's promises first because a fresh idea should not hide an old commitment.
- Separate activity from outcomes because a scheduled post and a signed project are different evidence.
- Report gaps openly because invented zeroes can trigger the wrong management decision.
- Keep one owner per next action, or flag unresolved ownership, because shared departments do not answer deadlines.
- This workflow does not install a timer. A recurring review needs a separately configured schedule and data access.

## Worked example

Fictional input:

```text
friday review. marketing promised 3 assets, 2 live one still draft.
sales 4 meetings booked, 2 happened, other 2 next week. CRM says 0 wins
but import failed. landing CTA 404 confirmed today. idea: webinar.
last week sales promised case study review, no task found, due yesterday.
```

Output:

```text
Results: marketing commitments 2/3 = 67%; 2 meetings held, 4 booked.
Wins: UNKNOWN because the import failed. No revenue inference.
Risk: sales YELLOW for one confirmed overdue commitment; task link missing.
Marketing GREEN if dates confirm no overdue item and no other risk condition.
Decision 1: Who owns repairing the landing-page CTA, and what recovery date
can delivery accept? Evidence: supplied verified 404 observation.
Decision 2: Was the case-study review completed elsewhere, or what blocks it?
Decision 3: Does the webinar replace a current priority? Keep it in backlog
until a decision names an owner, result and acceptance evidence.
Proposed actions: reconcile review outcome and failed CRM import; prepare
one CTA repair task after checking for an existing issue.
Executed: none. No agenda sent and no tasks created.
```

## Tips

1. Put the failed customer handoff ahead of the content calendar.
2. Ask for acceptance evidence, not a longer activity report.
3. Compare equivalent windows before discussing a trend.
4. Stop adding initiatives when nobody can name what gets deprioritized.
5. Carry unresolved decisions forward with their original evidence and date.

---
*Part of the ManagedCoder Agency Skills library. Turn weekly growth meetings into verified decisions and follow-through.*
