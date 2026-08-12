---
name: weekly-delegated-task-review
description: Run the weekly accountability review on everything you've delegated — pull every open task you assigned to someone else, group by person, score risk, flag stalled and ghost-progress work, write the follow-up notes, draft emails to the people who are behind, and produce the Monday brief. Use whenever the user says "run my weekly review", "friday review", "check my delegated tasks", "prep for monday", "who hasn't done their work", "what's overdue", "task accountability review", "what is everyone working on", or asks about the status of anything assigned to another person. Also use when they say the team has gone quiet, when they're about to walk into a Monday leadership meeting, or when work feels like it's "out there somewhere" and nobody has reported back.
---

# Weekly Delegated Task Review

You delegated the work. Nobody told you it stopped. This is the review that finds the tasks that quietly died three weeks ago, and puts a name and a deadline on each one before Monday.

> Tool placeholders like `~~project tracker` mean whatever tool you've connected in that category. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ Paste your task list or an export                         │
│  ✓ Per-person scorecard, risk levels, pattern flags          │
│  ✓ Drafted follow-up notes + the Monday brief                │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~project tracker: pull tasks live, post notes, move dates │
│  + ~~email: draft the follow-up emails to the RED people      │
│  + ~~chat: see whether the person has gone quiet everywhere   │
└──────────────────────────────────────────────────────────────┘
```

## What I need from you

**Option A — Connected tracker.** Say "run my weekly review." I'll pull everything you assigned.

**Option B — Paste it.** Per task: title, assignee, status, due date, created date, latest comment/description and when it changed. Missing fields are fine — I'll flag them.

**Option C — One person.** "How is Dana doing on my stuff?" works too.

## Step 1 — Pull every delegated task

Get every open task **created by the owner** and **assigned to someone else**. Exclude done and archived. Include tasks with no assignee — those are their own problem and get their own section.

Per task you want: title, status, priority, due date, created date, assignee name, assignee email, and the latest description/comment with its date.

Do not ask the owner to paste anything if a tracker is connected. The whole point is that they stop being the one who gathers the list.

## Step 1b — Two live-data traps, before you score anything

Score at face value and you will accuse the wrong people. Check both of these first.

**A. Duplicate delegation.** The same piece of work sometimes exists as two separate rows assigned to two different people, both descriptions saying they co-own one job. Scoring them independently double-counts the work and inflates both people's overdue numbers — so the owner walks into Monday telling two people they're behind on a thing that is really one thing.

Before grouping, look for near-duplicate titles — identical, or differing only by a product/vertical name — assigned to different people. Treat them as **ONE unit of work**: one line in the scorecard, both names listed as co-owners, counted once against neither person twice.

**B. Chain / pass-along tasks.** Some tasks are designed to route through a named sequence of people — the description says "comment and reassign to the next person," or lists an ordered chain. The current assignee is normal and correct; the task moving is the point. But if it has sat with the same person well past their step, that's a real stall wearing the costume of "in progress."

Flag any task whose description contains hand-off language ("reassign this task to", "pass it to", "comment chain", "next person in the chain") as a **CHAIN TASK**. For these, don't just check whether it's overdue overall — check **how long it has sat with the CURRENT assignee**, and say where in the chain it's stuck.

## Step 2 — Group by person and score risk

Group by assignee, after applying Step 1b. Per person:

- **Total open tasks** (deduped — co-owned duplicates count once)
- **Overdue count** (due date in the past, not done)
- **Never started count** (still in a "new" / "not started" state, regardless of due date)
- **Risk level:**

| Level | Threshold |
|---|---|
| 🔴 **RED** | 3+ overdue **OR** any single task overdue **14+ days** |
| 🟡 **YELLOW** | 1–2 overdue **OR** 3+ tasks never started |
| 🟢 **GREEN** | on track, nothing overdue |

Why "any one task overdue 14+ days" is enough on its own: three tasks a few days late is a busy week. One task ignored for two straight weeks is a decision — the person has quietly chosen not to do it, and no amount of chasing the other two will surface that.

## Step 3 — Pattern detection

Counts tell you who is behind. These tell you *why*, and they're what the owner actually needs on Monday. Flag by name:

- **STALLED** — created **30+ days ago**, still showing 'new'. Never started, not "slow."
- **GHOST PROGRESS** — 'in progress' for **14+ days** with no description update. In-progress with no visible output is not started; it's a status people use to buy quiet.
- **OVERLOADED** — same person holding **5+ open tasks**. Read it two ways: genuinely over capacity, or avoidance. The fix is opposite in each case, so ask rather than assume.
- **STUCK IN CHAIN** — a hand-off task sitting past its expected pass-along. Call it out by name, never folded into generic overdue — the person holding it may not even know it's their turn.
- **SPLIT OWNERSHIP** — one job, two owners. Surface once, name both, don't double-penalize. Two owners means no owner.

## Step 4 — Update dates and write the note

**Get today's actual date first, then calculate the coming Monday.** Never assume the date and never hardcode it — a review that moves everything to a Monday that already passed is worse than no review.

For every overdue task: propose moving the due date to that coming Monday, and propose a note on the task.

**Note style rules:**
- All lowercase — no caps, no formal language
- Direct and honest — it should sound like the owner wrote it, not like a system
- Specific to that task — not generic
- Short — 2–3 sentences max
- Always ends with a clear deadline ("monday", "end of week", "today")

**Good note:**
> "george — this was due feb 18 and still showing as new. i need to know what happened here and what is blocking you. update me by monday morning."

**Bad note — banned:**
> "Please provide a status update on this task. This item is overdue and requires immediate attention."

The second one is what makes people ignore trackers. It names no task, no date, no consequence, and nobody is on the hook for it. The first one is uncomfortable to read, which is exactly why it gets answered.

**Nothing is written without a yes.** Show the notes and date changes, wait for approval, then post, then report what actually changed — not what you intended to change.

## Step 5 — Draft emails for RED people only

One email per 🔴 RED person. 🟡 YELLOW gets mentioned in the Monday brief, no email unless the owner asks — emailing everyone every week trains people to ignore the emails.

**Email rules:**
- All lowercase, subject line and body
- Under **200 words**
- List each overdue task **specifically by name** — "you have some overdue tasks" invites a vague answer
- Genuinely ask what is blocking them. Not rhetorical. Half the time the answer is that they're waiting on the owner, and that's worth knowing before Monday
- Monday is the hard deadline
- Sign off simply, first name only
- **Draft only, never send.** The owner reads every one before it goes

## Output — the Monday brief

Use this structure literally.

```
# Monday Morning Brief — [date]

## 🚨 Immediate Action Required
[RED person] — [n] overdue, [n] never started
  • [task] — [n] days overdue — [what's at stake]
  • [task] — [pattern flag]
  Email drafted: [yes/no]

## ⚠️ Watch List
[YELLOW person] — [one line: what to watch]

## ✅ On Track
[GREEN person] — [n] open, all current

## Strategic Decisions Needed From You
[task] — blocked waiting on a decision only you can make — [the decision]

## Unassigned Tasks
[task] — no owner — [suggested owner]

## Stuck in Chain
[task] — sitting with [name] for [n] days — next in chain is [name]

## Split Ownership
[task] — co-owned by [name] and [name] — needs one clear owner

## Actions Taken This Week
Due dates moved: [n] | Notes posted: [n] | Emails drafted: [n]
```

## The standards this review applies

Say these out loud when a call is close, because they're the reason the flags are set where they are.

1. **Tasks assigned = full ownership.** Nobody should need to be chased for a status.
2. **If blocked, raise it immediately.** A blocker reported on day one is a scheduling problem. Reported on day thirty, it's a missed quarter.
3. **"In progress" without visible output = not started.** This single rule catches more slippage than every other check here.
4. **The tracker is not optional — it IS the accountability system.** Work that only exists in someone's head can't be reviewed, so it can't be trusted.
5. **Managers update their own tasks proactively, weekly.** If the owner is the one updating other people's tasks, the owner is the project manager again.

## Worked example

**Input:** "run my weekly review" — the tracker returns:

```
Redesign onboarding email | Dana | new | created 45 days ago | no due date | no comment
Redesign onboarding email (SMB) | Chris | new | created 44 days ago | no due date | no comment
Client renewal call notes | Dana | in_progress | due 8 days ago | last update 20 days ago
Q3 partner deck — review + pass to legal | Sam | in_progress | due 3 days ago | "reassign to next person when done"
Vendor contract cleanup | (unassigned) | new | created 12 days ago
```

**Output:**

```
# Monday Morning Brief — Aug 15

## 🚨 Immediate Action Required
Dana — 1 overdue, 1 never started
  • Client renewal call notes — 8 days overdue, no update in 20 days — GHOST PROGRESS
    Renewal conversation is happening without notes from the last one.
  Email drafted: yes

## ⚠️ Watch List
Sam — Q3 partner deck is a CHAIN TASK, 3 days overdue and sitting with Sam
for 11 days. Legal hasn't seen it yet.

## Split Ownership
"Redesign onboarding email" — co-owned by Dana and Chris (titles differ only
by "(SMB)"). Counted once, not against either. 45 days old, never started by
anyone — which is what two owners produces. Pick one.

## Unassigned Tasks
Vendor contract cleanup — no owner, 12 days old.

## Actions Taken This Week
Due dates moved: 2 | Notes posted: 0 (pending your yes) | Emails drafted: 1

---
Proposed note on "Client renewal call notes":
"dana — renewal notes were due last week and there's been no update in 20
days. what's actually blocking this? i need it monday morning."

Proposed: move both overdue due dates to Mon Aug 18.
Post the notes and move the dates? [waits — writes nothing until you say yes]
```

Note what it caught that a raw overdue list would not: Dana looks like two failures and is really one, Sam looks fine on a status column and is the actual bottleneck, and the 45-day-old task has no single owner rather than a lazy one.

## Tips

1. **Run it Friday, read it Monday.** Friday gives people the weekend to answer before you're face to face. A Monday-morning review means you walk into the meeting with questions instead of answers.
2. **The person with zero overdue tasks may be the biggest problem.** Sometimes it means they're excellent. Sometimes it means you stopped delegating anything real to them. Check which one before you praise it.
3. **OVERLOADED and AVOIDANT look identical in the data.** 5+ open tasks tells you to have the conversation, not what the conversation is. Ask; don't diagnose from a dashboard.
4. **Moving a due date without a note is how tasks live forever.** The date change says "later." The note says "and here's what happens if not." Only one of those changes behavior.
5. **If you're reluctant to send the email, that's the finding.** Reluctance usually means you already know the answer is "it never started and nobody noticed" — which is a management conversation, not a tracker update.
6. **Start next week by checking Monday's tasks actually closed.** A review nobody follows up on teaches the team that the deadline was decorative.

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want this scorecard, the notes, and the Monday brief produced for you every Friday without you pulling a single list? See Agency Control Tower: controltower.collabai.software*
