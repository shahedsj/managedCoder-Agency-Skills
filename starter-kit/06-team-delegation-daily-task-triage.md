---
name: daily-task-triage
description: Score your open tasks, work them 3 at a time, and draft the exact comment that unblocks whoever is waiting on you. Use whenever the user says "my tasks", "task review", "task check", "what's on my plate", "what do I have today", "morning review", "evening review", "my daily tasks", "next 3", "show blockers", "what should I close", or "who's waiting on me". Also use when they paste a task export, when they say the board is a mess, or when they suspect the team is stuck waiting on a decision from them.
---

# Daily Task Triage

Most of your task list isn't waiting on work. It's waiting on you saying yes or no. This finds those tasks first, because every hour one sits there is an hour someone else on payroll is idle.

> Tool placeholders like `~~project tracker` mean whatever tool you've connected in that category. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ Paste a task list or export                               │
│  ✓ Full scoring, hard overrides, 3 at a time                 │
│  ✓ Drafted comments and nudges you copy back in              │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~project tracker: pull tasks live, post comments,         │
│    close and reassign after you approve                       │
│  + ~~chat: send the nudge to whoever is blocked               │
│  + ~~meeting notes: context on why the task exists            │
└──────────────────────────────────────────────────────────────┘
```

## What I need from you

**Option A — Connected tracker.** Say "my tasks." I pull everything open and assigned to you.

**Option B — Paste them.** One task per line: title, status, due date, who created it, last comment and its date. Missing fields are fine — missing is itself a signal.

**Option C — One task.** "What do I do with the invoice template task" works too.

**Give me this once:** your own stated core responsibilities — 5 to 8 lines of what you are actually accountable for as the owner. Everything gets scored against that list. Without it, scoring collapses into urgency only, and urgent is not the same as yours.

**If they haven't given it, ask before scoring — once.** Offer this default so they can say "use that" in three seconds instead of writing an essay:

> Using these unless you change them: approve creative and technical direction · handle client escalations · own final pricing and scope decisions · unblock the team · run BD and pipeline · decide what gets delegated.

If they skip it anyway, still run — but print this as the first line of the output, every time:

> ⚠️ Ranking is urgency-only — role alignment off (no responsibilities given).

Role alignment is a third of the score. A run without it still returns a confident, ordered list, which is exactly the problem — the degradation is invisible unless you say it out loud. Never ask twice in the same session.

## Step 1 — Pull the open tasks

Everything assigned to this person that is not done, archived, or deleted — status `new` or `in progress` only. For each: title, status, priority, due date, description, the last comment and its date, and who created it. The last comment does most of the work here; a task with no comment history can only be scored on dates. Sort the raw pull by priority (urgent, high, medium, low) then due date ascending, nulls last. That's the input order, not the output order — scoring reorders it.

## Step 2 — Apply hard overrides first

These run **before** scoring — each describes a situation where the score is the wrong question.

| Condition | Action |
|---|---|
| Due date is past | **OVERDUE** — show before all others regardless of score |
| Priority urgent + no due date | Treat as due today |
| Last comment says done / deployed / live but status is still open | Bucket: **CAN CLOSE** |
| Last comment says on hold | Separate section — do not push the owner on it |
| 7+ days stale with zero comments | Flag: keep or archive? |
| Title starts with a person's name | This is accountability, not execution — draft a nudge to that person |
| Seen 3+ times in past sessions with no action | Add: "you've seen this before — decide now or archive" |

The last row is the one people skip and shouldn't. A task you've looked at three times without acting is not a task, it's a decision you're avoiding — surfacing it a fourth time in the same neutral tone teaches the list to lie to you.

## Step 3 — Score every task

Add the points. Highest first.

**Input type — what does this actually need from you?**

| Condition | Points |
|---|---|
| Quick decision (approve / reject / choose) | **+3** |
| Comment to unblock a team member | **+2** |
| Strategic review | **+1** |
| The owner has to execute it personally | **0** — flag for delegation |

**Team blocking**

| Condition | Points |
|---|---|
| Last comment contains "waiting", "need approval", "blocked", "need decision", "need credentials" | **+3** |
| Task was created by a team member | **+2** |
| No comment in 5+ days | **+1** |
| Owner already commented in the last 24h | **−1** |

**Role alignment — against the owner's own stated core responsibilities**

| Condition | Points |
|---|---|
| Directly matches one of the stated responsibilities | **+2** |
| Loosely related | **+1** |
| Pure ops / execution | **−2** |

Why it's weighted this way: a quick approval scores higher than a strategic review because the approval has someone standing behind it. The **−1 for "already commented in 24h"** stops the same three noisy tasks topping the list every day while quieter ones rot. And **−2 for pure ops** is deliberate — the owner decides and unblocks, they don't execute. A task scoring below zero isn't unimportant, it's someone else's. Route delegation by **work type, not by person**: engineering to the pod tech lead, client follow-up to the account or project owner, marketing to the content owner, finance to whoever owns invoicing, people issues to ops/HR. Naming a role instead of a name means the suggestion still works after someone leaves.

## Step 4 — Show 3 at a time

**Never more than 3.** A screen of 30 tasks gets skimmed and nothing changes; three gets worked. This is the single rule that decides whether this skill produces action or another list. After each set:

> "That's 3. Say **next** for more, **skip** to skip one, **close it** to mark done, or **delegate** to reassign."

### Task card

```
[BADGE] TASK TITLE
🔗 [task link, if the tracker returns one]
Due: [date or "no date"] | Created by: [name] | Status: [status] | Score: [n]

Context: [1 sentence — what this is actually about]

Your action: [exactly what the owner has to do]

Draft comment:
[name] -- [specific deliverable] -- [hard deadline]

Nudge *(only if someone is waiting)*:
hey [first name], [1 sentence]. need this by [date].

Delegate? *(only if ops/execution)*: [role] — [reason]
```

**Never hand-build a task link.** Trackers generate URL slugs by their own rules, often truncating mid-word — a guessed link 404s and costs more trust than no link at all. Use the link the tracker returns, or fall back to the task ID route.

### Priority badges

| Badge | Condition |
|---|---|
| `OVERDUE` | Past due date |
| `BLOCKING TEAM` | Someone is waiting on the owner |
| `DUE SOON` | Due today or tomorrow |
| `STRATEGIC` | High role alignment, no immediate blocker |
| `SEEN BEFORE` | Surfaced 3+ times with no action |
| `LOW` | Future date, no urgency |

## Step 5 — Morning or evening mode

Detect from the clock or the phrasing. It changes what leads, not what's in the list.

**Morning (before 12pm)**

```
MORNING REVIEW — [Weekday, Date]
[X] open tasks | [Y] blocking team | [Z] ready to close
Showing top 3 by impact. Say "next" for more.
```

Lead with **BLOCKING TEAM**. The goal is to unblock the team before noon — an approval given at 9am buys a full working day; the same approval at 6pm buys nothing.

**Evening (after 5pm)**

```
EVENING REVIEW — [Weekday, Date]
[X] reviewed today | [Y] can close tonight | [Z] still open
Showing top 3 to close out the day.
```

Lead with **CAN CLOSE**. The goal is clearing completed work so tomorrow's list is true — a board full of finished-but-open tasks makes every future triage worse. If you can't tell the time and they didn't say, ask; guessing evening on a Monday morning buries the blockers.

## Step 6 — Comment style

**Format:** `[name] -- [specific deliverable] -- [hard deadline]`
- **All lowercase, no exceptions.** It reads as a person typing fast, not a system posting. People answer people.
- Use `--` as the separator. No semicolons, no em-dashes.
- Name the person first, then the exact ask, then the exact deadline — in that order, so the person knows it's theirs before they finish reading.
- **Reference exact dates**: "by june 12", "by end of week thursday". Not "soon", not "asap" — asap means nothing and gets treated accordingly.
- Never "just checking in", "please follow up", "please advise", or any corporate phrasing. These signal that no answer is expected, and you'll get one.
- For a complex task, write 2–3 short paragraphs of context, but still end with the deadline.

Example shape:
```
sam -- deploy the logging change to all instances -- list: mortgage, healthcare,
nonprofit, agency, client success -- screenshot each as proof -- all done by april 28
```

## Step 7 — Writing anything back

Every comment, close, and reassignment is **proposed first and written only after an explicit yes.** Then report what actually changed, not what you intended to change. Before any bulk action, show the exact list you're about to touch — bulk-closing the wrong tasks erases a team's work history and no apology recovers it.

## Session commands

| User says | Do |
|---|---|
| next | Show the next 3 |
| skip | Skip this one, continue |
| close it | Mark done after confirmation, log it in the session |
| delegate | Suggest a role, draft the handoff comment, reassign after a yes |
| more context | Pull the full description and all comments |
| refresh | Force a live re-pull |
| show all urgent | Override 3-at-a-time, show every urgent task |
| show blockers | Only tasks where someone is waiting |
| done / that's all | End, show the summary |

## On "done"

```
SESSION SUMMARY — [Date] [Morning/Evening]
Reviewed: [N] tasks
Comments posted: [N]
Closed: [N]
Delegated: [N] (to whom)
Decisions made: [brief list]
Still needs attention: [top 3 task titles]
Next session starts at: [first unreviewed task title]
```

Keep that summary — next session's "seen 3+ times" override depends on it.

## Worked example

**Input:** *"morning review"* — responsibilities given earlier: approve creative direction, manage client escalations, own final pricing, run BD team. Raw pull, messy as it comes:

```
fix invoice template | in_progress | due aug 5 | created by me | no comments
maria - homepage hero copy | new | no due date | created by maria | last comment aug 10: "waiting on your signoff on the tagline"
rewrite onboarding deck | in_progress | no due date | created by me | last comment jul 28: "deck v2 is live, sent to client"
vendor contract review | new | urgent | no due date | created by ops | last comment aug 11: "on hold till legal replies"
```

**Output:**

```
MORNING REVIEW — Tuesday, Aug 12
4 open tasks | 1 blocking team | 1 ready to close
Showing top 3 by impact. Say "next" for more.

1. [OVERDUE] fix invoice template
Due: Aug 5 (7 days past) | Created by: you | Status: in_progress | Score: 1
Context: Invoice template fix you assigned yourself. No comment in 15 days.
Your action: This is pure ops (−2) and it's yours only by accident. Delegate or kill it.
Draft comment:
dana -- take over the invoice template fix -- ping me only if the layout changes -- done by aug 15
Delegate? yes — finance/invoicing owner. You've held this 7 days past due with zero movement.

2. [BLOCKING TEAM] maria - homepage hero copy
Due: no date | Created by: maria | Status: new | Score: 8
Context: Maria stopped Aug 10 waiting on a tagline decision. Title starts with her
name — your accountability, her execution.
Your action: Pick a tagline. Quick decision (+3), blocked (+3), she created it (+2),
matches "approve creative direction" (+2), no comment in 5+ days (+1).
Draft comment:
maria -- approved, go with option 2 -- ship the hero section by thursday aug 14
Nudge:
hey maria, tagline approved, option 2. go ahead and ship the hero by thursday.

3. [CAN CLOSE] rewrite onboarding deck
Due: no date | Created by: you | Status: in_progress | Score: 0
Context: Jul 28 comment says v2 is live and sent to the client; still open 15 days later.
Your action: Close it. Nothing here is real work.

Held back: vendor contract review — on hold pending legal. Not pushing you on it.

Post comments 1 and 2, and close 3? [waits for a yes before writing anything]
That's 3. Say next for more, skip, close it, or delegate.
```

## Tips

1. **The tasks with your team's names in the title are the expensive ones.** They look like admin. They're actually the ones where someone is idle waiting for you, and idle time is the only cost in this business you never get an invoice for.
2. **If a task has survived three of these sessions, stop scoring it and kill it.** It's not a priority problem, it's an avoidance problem, and a fourth appearance won't fix it.
3. **Run it twice a day, not once.** Morning unblocks people while they still have a day to use it. Evening keeps the list honest so tomorrow's scores mean something. One session a day gets you half the value and all of the guilt.
4. **Refuse to work more than 3 at a time even when you feel productive.** The urge to "just clear the whole list" is exactly how you spend forty minutes and post two comments.
5. **A comment with no date isn't a comment, it's a mood.** If you can't name the day it's due, the ask isn't clear enough yet — write it again.
6. **If you never gave it your responsibilities, what you're reading is just an urgency list.** It will still look sorted and reasonable — that's the danger. The tasks that are genuinely yours rarely shout, so they sink to the bottom while three loud ops tasks sit on top.

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want your tasks scored, your blockers surfaced, and the comments drafted before you open your laptop — for your whole team? See Agency Control Tower: controltower.collabai.software*
