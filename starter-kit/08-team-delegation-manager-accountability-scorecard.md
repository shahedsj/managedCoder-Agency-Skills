---
name: manager-accountability-scorecard
description: Build a one-page manager accountability scorecard for your Monday leadership meeting — completion rate, overdue count, never-started count, and a risk color per person, plus the sharp question to ask each one in the room. Use whenever the user says "the scorecard", "monday scorecard", "meeting prep scorecard", "accountability report", "how is everyone doing on their tasks", "who is delivering and who isn't", "task completion rates", "show me the numbers by person", or wants a per-person performance summary before a leadership, all-hands, or management meeting. Also use when they're about to walk into a team meeting with no data, when they say the team "feels slow" but can't point at anything, or when the same tasks keep getting discussed week after week with no movement.
---

# Manager Accountability Scorecard

Most team meetings run on memory and vibes, so the loudest person sounds busiest and the quiet person with six overdue tasks never comes up. This turns your task data into one page of numbers you can put on a screen — and gives you the specific question to ask each person, by name, about their actual stalled work.

> Tool placeholders like `~~project tracker` mean whatever tool you've connected in that category. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ Paste two lists: completed this week, and open tasks      │
│  ✓ Full scorecard, risk colors, talking points               │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~project tracker: pull both lists live, with task titles  │
│  + ~~email: draft the scorecard to yourself before the room   │
│  + ~~docs: write it to your standing meeting page             │
└──────────────────────────────────────────────────────────────┘
```

## What I need from you

**Option A — Connected tracker.** Say "monday scorecard." I'll pull it.

**Option B — Paste two lists.**
1. Tasks completed in the last 7 days, per person (a count is enough).
2. Every currently open task, per person, with status and due date. Task titles matter here — the titles are what make the talking points sharp.

**Option C — One person.** "How is Sam doing?" runs the same math for one row.

## Step 1 — Pull completed work, last 7 days

Count tasks per person that moved to done in the last 7 days. Scope it to work *you* assigned or own as the delegator, and exclude tasks assigned to yourself — this is a delegation scorecard, not a personal to-do list. Your own tasks in the table make everyone else's numbers look better than they are.

## Step 2 — Pull all open tasks, per person

For every person, get: total open, how many are past their due date (overdue), how many are still in a "not started" state (never started), and how many are in progress. Exclude anything done or archived.

Capture the actual task titles and how many days each overdue task has been overdue. Without titles you can produce a table but not a meeting.

**Missing due dates are normal.** Half-populated trackers are the rule, not the exception. A task with no due date is not overdue — count it as open, and flag the count of undated tasks separately. Never treat "no date" as "on time."

## Step 3 — Calculate rate and risk

**Completion rate** = completed_this_week / (completed_this_week + total_open) x 100. Round to the nearest whole number.

Why that denominator: it measures throughput against the pile actually sitting on the person. Someone who closed 4 while holding 3 open is moving. Someone who closed 0 while holding 6 is not, no matter how busy the week felt.

**Risk level:**

| Color | Condition (any one triggers it) |
|---|---|
| 🔴 RED | overdue >= 3 **OR** any single task overdue 14+ days **OR** completion rate < 20% |
| 🟡 YELLOW | overdue 1-2 **OR** never_started >= 4 **OR** completion rate 20-50% |
| 🟢 GREEN | overdue = 0 **AND** completion rate > 50% |

Check RED first, then YELLOW, then GREEN — a person can trip more than one line and the worst color wins.

The 14-day rule exists because one task rotting for two weeks is a worse signal than three tasks that slipped by two days. Three small slips is a busy week. One task untouched for 14 days is a decision nobody made — either it's not real work, or the person is stuck and hasn't said so. Both need naming out loud.

The never_started >= 4 rule catches the person whose numbers look fine because nothing is overdue yet. Four things queued and untouched means the work hasn't started, and it will all come due at once.

## Step 4 — Output

Use this structure exactly.

```
# 📊 Manager Accountability Scorecard
## Monday [DATE] — [meeting name]

| Manager | Role | Open | Done ✅ | Overdue ⚠️ | Never Started | Rate | Status |
|---------|------|------|---------|------------|---------------|------|--------|
| [name]  | [role] | [n] | [n]    | [n]        | [n]           | [n]% | 🔴/🟡/🟢 |

## 🔴 Critical — Address in Meeting
[Each RED person, one block. Name their single most overdue task by its actual
 title and its age in days. "[Name] — [n] overdue, [n] done this week. Most
 urgent: "[task title]", overdue [n] days."]

## 🟡 Watch — Monitor This Week
[Each YELLOW person, one line each — the specific thing to watch, not a warning.]

## 🟢 Performing — Acknowledge
[Each GREEN person, one short line. Say the number out loud.]

## 📌 Decisions Needed From You
[Every task blocked waiting on your input, approval, or a call only you can make.
 If there are none, say "None this week" — don't skip the heading.]

## 🎤 Meeting Talking Points
**[Name]** — [one sharp question built from their actual stalled task]
```

Sort the table by overdue count descending, then total open descending. The person who needs the conversation should be the first row, not buried alphabetically.

## Step 5 — Writing the talking points

This is the part that makes the difference between a report and a meeting.

**One question per person, built from their real task.** Pull the task title and its age, then ask the question the task raises. The goal is a question the person can only answer with a fact.

Good:
- *"Is the client portal redesign still happening, or should we kill it — it's been open 42 days with nothing shipped?"*
- *"How many blog posts actually went live this month?"*
- *"Is the retail account project alive, or do we archive it today?"*
- *"What's the current state of the mortgage build — can we demo it Thursday?"*

Bad — delete these on sight:
- *"Please provide an update."*
- *"Can you share where you are on your tasks?"*
- *"What's blocking you?"* (as a standalone — it invites a paragraph, not a fact)

The difference: a generic question gets a generic answer and the task is still open next Monday. A question with a task name, a number, and a live/dead option forces a decision in the room. "Kill it or ship it" is a question people can answer; "give me an update" is a question people can survive.

**Offer the kill option.** For anything overdue 14+ days, the question should include the possibility of closing it. Half the time that's the right answer and nobody wanted to be the one to say it.

## Step 6 — Output format

Ask before doing anything but the first.

- **Default:** markdown in the chat — clean and scannable, ready to project.
- **"Make it a file"** → save it as a `.md` file.
- **"Email it to me"** → draft it to the user's `~~email`. Draft only, never send.
- **"Put it in the doc"** → write to their standing meeting page in `~~docs`, after showing what will be written.

## The rules that make this work

**Never soften a red.** The temptation is to write "Sam has had a busy week" instead of "Sam: 4 overdue, 0 completed." The scorecard's only job is to be true in a room where everyone can see it. A softened scorecard is worse than none, because now the team has learned the numbers don't mean anything.

**"In progress" for three weeks is not in progress.** Work with no visible output has not started. If a task has sat in progress past 14 days with no comment or update, treat it in your talking point as stalled, not active. This is the single most common way a scorecard lies.

**Count what finished, not what got worked on.** Activity is not outcome. The rate uses completed tasks on purpose — hours logged, comments posted, and "almost done" all belong in the conversation, not in the number.

**Show the whole team, every week, including the greens.** A scorecard that only appears when someone is in trouble becomes a punishment, and people start managing the tracker instead of the work. Run it every Monday whether the news is good or bad.

**Never write back to the tracker from this skill.** This is a read-and-report tool. If the meeting produces changes — reassignments, closures, new dates — propose them as a list, wait for a yes, then make them and report what actually changed.

## Worked example

**Input** (pasted, messy — a real paste from a half-populated tracker):

```
done last 7 days: priya 4, sam 0, dan 1
open: priya 3 open none overdue none new
sam 6 open, 4 overdue - "client portal redesign" 42 days, "q3 case study" 9 days,
"vendor contract review" 4 days, "onboarding doc" 2 days, 2 still new
dan 5 open, 1 overdue "analytics dashboard spec" 3 days, 4 still sitting in new,
one of dans has no due date
```

**Output:**

```
# 📊 Manager Accountability Scorecard
## Monday Aug 17 — Leadership Meeting

| Manager | Role | Open | Done ✅ | Overdue ⚠️ | Never Started | Rate | Status |
|---------|------|------|---------|------------|---------------|------|--------|
| Sam     | Delivery Lead | 6 | 0 | 4 | 2 | 0%  | 🔴 |
| Dan     | Account Lead  | 5 | 1 | 1 | 4 | 17% | 🔴 |
| Priya   | Ops Lead      | 3 | 4 | 0 | 0 | 57% | 🟢 |

## 🔴 Critical — Address in Meeting
Sam — 4 overdue, 0 completed this week. Most urgent: "Client Portal Redesign",
overdue 42 days. Three of the four went overdue in the last two weeks, so this
is a current problem, not old debt.

Dan — 17% rate, and 4 of 5 tasks have never been started. Only 1 overdue today,
but all four untouched items come due inside the next fortnight.

## 🟡 Watch — Monitor This Week
None this week.

## 🟢 Performing — Acknowledge
Priya — 57% completion rate, zero overdue, nothing sitting untouched. Say it in
the room; this is the pattern you want copied.

## 📌 Decisions Needed From You
"Vendor Contract Review" (Sam, 4 days overdue) needs your sign-off before it can
close. It is waiting on you, not on Sam.

## 🎤 Meeting Talking Points
**Sam** — is the client portal redesign still happening, or should we kill it —
it's been open 42 days with nothing shipped?
**Dan** — four of your five tasks haven't been started. Which one starts today,
and what do we drop to make room?
**Priya** — you cleared 4 this week. What are you doing that the others aren't?

⚠️ Before the meeting:
- [Dan is RED on rate, but only 1 task overdue — his real problem is a
  never-started pile, not lateness. Lead with capacity, not accountability.]
- [1 of Dan's tasks has no due date. It isn't counted as overdue. Set a date
  in the meeting or it will never surface.]
- ["Vendor Contract Review" is on your desk. Don't ask Sam about it.]
```

## Tips

1. **Read the Decisions Needed section before you open your mouth.** Half the time the CEO is the reason something is red. Calling out a task you're personally blocking is the fastest way to lose the room's trust in the scorecard.
2. **Two reds for the same person, two weeks running, is a management problem, not a task problem.** The scorecard has done its job by showing you; the fix is a 1:1, not a louder meeting.
3. **A 0% rate with only 2 open tasks is not the same as a 0% rate with 12.** Read the Open column next to the Rate column before deciding who to worry about — small denominators swing wildly.
4. **Kill something in the meeting, every week.** If nothing ever gets closed as dead, the never-started column only grows, and by month three the scorecard is all red and nobody looks at it.
5. **Project it on the screen, don't email it.** The number being visible to the whole team is what changes behavior. A private scorecard is a report; a shared one is a system.

## Pairs with

This runs **Monday** and produces the meeting brief. The weekly delegated task review runs **Friday** — it chases open work, updates tasks, and drafts the follow-ups. Friday cleans the data, Monday shows the truth. Run both every week and you have a complete weekly accountability loop that doesn't depend on you remembering anything.

---
*Free next step: join a live class and get the weekly AI-for-agencies newsletter at managedcoder.com*

*Part of the Agency Skill File Starter Kit — ManagedCoder. Want this pulled, scored, and waiting in your inbox every Monday at 7am, with no manual exports? See Agency Control Tower: controltower.collabai.software*
