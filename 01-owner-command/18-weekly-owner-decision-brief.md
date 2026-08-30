---
name: weekly-owner-decision-brief
description: Turn a week of agency activity into a short owner decision brief focused on what only the owner should decide, unblock, delegate, watch, or drop. Use for weekly CEO or founder reviews, Monday planning, Friday reviews, leadership prep, return-from-travel catch-up, or whenever an agency owner has too much status information and needs the few decisions that actually require their attention.
---

# Weekly Owner Decision Brief

Do not produce another status report. Reduce the agency to the decisions and interventions that need owner attention.

Use this skill to answer five questions:

1. What must the owner decide?
2. Who or what is waiting on the owner?
3. What should be delegated instead of owned?
4. What risk needs watching before it becomes expensive?
5. What should be stopped, archived, or deprioritized?

> Tool placeholders such as `~~project tracker`, `~~CRM`, and `~~finance` mean whatever connected system provides that category of data. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```text
STANDALONE
Paste tasks, project notes, pipeline, client issues, team updates, and financial concerns.

CONNECTED
Pull the same evidence from project management, CRM, meetings, calendar, finance, and Agency Brain.
```

Every source is optional. Missing data reduces confidence; it must not be replaced with invented certainty.

## Step 1 - Establish the review window

Default to the last 7 days plus the next 14 days of deadlines.

When a previous weekly brief exists, load it first. The value is not only the current state. The value is seeing what changed, what stayed stuck, and what the owner has already reviewed without acting.

## Step 2 - Collect only decision-relevant signals

Look for:

- overdue or due-soon client commitments
- projects that moved from green to yellow or red
- blocked work waiting on approval, credentials, pricing, scope, or direction
- delegated work with silence or repeated missed dates
- deals with an overdue next step or material close-date risk
- client relationship warnings
- capacity or overload signals
- scope changes that have not been priced or approved
- margin or cash concerns
- decisions recorded in meetings but not reflected in systems
- recurring issues that appeared in prior reviews

Do not fill the brief with healthy routine work.

## Step 3 - Classify every signal

Put each meaningful item into exactly one primary bucket.

| Bucket | Test |
|---|---|
| **DECIDE** | A consequential choice needs owner judgment or authority |
| **UNBLOCK** | Someone can continue as soon as the owner provides a specific input |
| **DELEGATE** | The work matters, but the owner should not execute it personally |
| **WATCH** | No action today, but the downside becomes material if the signal worsens |
| **DROP** | Stale, duplicated, low-value, or no longer aligned work should be stopped or archived |

If an item appears to fit several buckets, choose the action that removes the most organizational friction.

## Step 4 - Score owner attention

Score each item from 0 to 10.

**Business impact, 0-3**
- 3: revenue, retention, major delivery, compliance, reputation, or strategic direction
- 2: important team/project impact
- 1: useful improvement
- 0: routine administration

**Time pressure, 0-2**
- 2: overdue or due within 3 days
- 1: due within 14 days
- 0: later or no real deadline

**Dependency, 0-2**
- 2: multiple people/client work blocked
- 1: one person or one workstream blocked
- 0: nobody waiting

**Owner necessity, 0-2**
- 2: requires owner authority, relationship, risk tolerance, or final tradeoff
- 1: owner input helps but another role could decide
- 0: pure execution

**Repeat penalty, 0-1**
- 1: the same unresolved item appeared in a prior review

Rank by score, but apply the hard overrides below first.

## Hard overrides

Show before normal scoring when any apply:

- a client-facing commitment is overdue
- a team is blocked specifically on an owner decision
- a material deal or renewal has no next step
- a project is red with no recovery owner
- the same decision has appeared in 3 reviews without resolution
- a security, legal, payroll, cash, or compliance issue has a near-term deadline

A repeated decision is not a status item. Force a choice: decide, delegate the decision, or explicitly defer it with a date.

## Step 5 - Compare with the prior review

When prior data exists, label meaningful changes:

- **NEW** - appeared this week
- **WORSE** - risk increased or deadline slipped
- **BETTER** - risk reduced but still open
- **STUCK** - materially unchanged
- **CLOSED** - resolved since last review

Do not claim trend without comparable evidence.

## Step 6 - Produce one owner page

Keep the main brief under 600 words.

```markdown
# Weekly Owner Decision Brief - [week/date]

## What changed
- [3-5 meaningful changes only]

## Decide
1. **[decision]** - Score [x]/10 - [why owner must decide]
   - Evidence: [facts and source dates]
   - Options: [A / B / C if real options exist]
   - Recommendation: [one recommendation + reason]
   - Decision needed by: [date or NO DATE SET]

## Unblock
- **[item]** - waiting on [specific owner input] - blocks [who/what]

## Delegate
- **[item]** - suggested owner role: [role, not invented person] - [why]

## Watch
- **[risk]** - trigger for action: [specific threshold/event]

## Drop
- **[item]** - [why it should stop/archive]

## Owner priority this week
**[ONE outcome]** - [why this is the highest-leverage use of owner attention]

## Data gaps
- [missing source that materially limits confidence]
```

## Rules

**One priority means one.** Do not turn the final section into three priorities.

**Separate facts from recommendations.** Evidence says what happened. Recommendation says what to do about it.

**Do not promote urgency into ownership.** A task can be urgent and still belong to someone else.

**Prefer role-based delegation.** Suggest account owner, PM, finance lead, technical lead, sales owner, or another appropriate role. Do not invent a person's name.

**Do not silently change systems.** If connected tools allow task updates, reassignment, comments, CRM changes, or messages, preview the exact change and wait for approval.

**Preserve provenance.** When connected, attach the source system and source date to consequential facts.

**Use Agency Brain when available.** Check prior decisions, client context, SOPs, and previous briefs before recommending a choice. Current operational data wins over stale knowledge; flag conflicts instead of silently choosing one.

## Quality test

The brief fails if the owner finishes reading and still has a list instead of decisions.

A good brief should make it possible to say:

- yes/no
- choose A/B
- delegate this
- unblock this
- watch until this trigger
- stop this

That is the output.