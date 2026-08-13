---
name: daily-owner-brief
description: Build the owner's morning brief — today's calendar, your top 5 tasks, the deals closing this week, any red flags, and the ONE thing to actually do today. Use whenever the user says "what's my day look like", "catch me up", "morning brief", "daily brief", "brief me", "start my day", "what's on my plate today", "what do I have today", "what's happening today", "morning update", or "standup prep". Also use when they open the day asking what they're forgetting, what's slipping, or what they should focus on first — and any time a recurring daily summary of calendar, tasks, pipeline, and team status is wanted.
---

# Daily Owner Brief

Most owners start the day by opening five tabs and reconstructing it from scratch. Twenty minutes gone, and they still lead with whatever shouted loudest. This produces one page that ends with a single decision — so the first hour goes to the thing that actually matters instead of the thing that arrived most recently.

> Tool placeholders like `~~calendar` mean whatever tool you've connected in that category. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ Paste today's meetings, tasks and deals in any format     │
│  ✓ Full brief, under 300 words, one clear priority           │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~calendar: today's events, external vs internal, OOO      │
│  + ~~project tracker: your own open tasks, overdue + due today│
│  + ~~CRM: deals by closest close date, follow-ups overdue     │
│  + ~~docs: writes the brief to your daily page each morning   │
└──────────────────────────────────────────────────────────────┘
```

**Every connector is optional.** If one is missing, that section is simply skipped — the brief never fails because a tool isn't there. A brief with three sections beats an error message.

## What I need from you

**Option A — Connected tools.** Say "morning brief." Everything gets pulled.

**Option B — Paste it.** Meetings, task list, deal list. Rough and unformatted is fine.

**Option C — Mixed.** Connect what you have, paste the rest. "Here's my calendar, pull the deals."

## Step 1 — Get today's actual date first

Get today's real date and day of week before pulling anything — never assume or hardcode it. Every other step depends on it: "overdue", "due today", and "closing this week" are all meaningless without it, and a brief built on yesterday's date flags the wrong tasks and misses today's meetings entirely.

## Step 2 — Pull today's calendar

From `~~calendar`, today only.

Split the day two ways, because they carry different risk:

- **EXTERNAL** — any event with at least one attendee whose email domain is not your own company domain. Clients, prospects, partners, candidates.
- **INTERNAL** — everything else.

Name the key external attendee on each external line. External meetings get shown first and get a name attached, because those are the ones where being unprepared costs you money or a relationship. Being vague in an internal standup costs you nothing.

Also catch **out-of-office / WFH flags** — usually all-day events on a team or leave calendar. If someone you were going to hand work to is out, you need that before 9am, not at 4pm when you're waiting on them.

## Step 3 — Pull your own tasks

From `~~project tracker`: open tasks assigned to *this person only*, excluding anything done or archived.

Sort by priority first, then due date soonest:

| Priority | Order |
|---|---|
| Urgent | 1 |
| High | 2 |
| Medium | 3 |
| Low | 4 |

Tasks with no due date sort last within their priority — a task with no date isn't more urgent than a dated one, it's just less managed.

**Show 5 maximum.** Flag overdue and due-today clearly and separately. Five is the cap on purpose: an owner reading a list of 22 tasks at 8am does none of them. Five gets worked. If there are 22, the other 17 are a planning problem, not a morning problem.

## Step 4 — Pull the pipeline snapshot

From `~~CRM`: deals owned by this person, **excluding anything closed** — won or lost, however your stages spell it.

Sort by closest close date first. **Show 3-5.** Lead with anything closing this week or overdue for follow-up, because those are the only two states where today's action changes the outcome. A deal closing in November does not need a line in Tuesday's brief.

## Step 5 — Check flags

Anything marked urgent or critical that isn't already in the task list — an escalation tag, a critical priority field, a flagged list, a blocked project, a team issue. Cap at 5.

If there's no such marker in the tools, **skip the section entirely.** Don't print "Flags: none" every day for a month — a section that's always empty trains the reader to skip the section that finally isn't.

## Step 6 — Decide what kind of day this is

Before composing, look at what came back and name the day. Same inputs, different brief:

| Day type | Signal | What the brief must do |
|---|---|---|
| Heavy external | 2+ external meetings | Lead with prep, not tasks |
| Overdue pile-up | 3+ overdue tasks | Say which 1 to clear, not all of them |
| Deal week | A deal closes within 5 days | Pipeline moves above tasks |
| Open day | Under 2 meetings, nothing overdue | Priority Today is the deep work, not admin |

If it's genuinely ambiguous, ask one question rather than guess. The expensive wrong guess is treating a heavy external day like an open one — the owner walks into a client call cold, and no amount of task-list accuracy makes up for that.

## Step 7 — Compose the brief

Use this structure exactly, in this order, and nothing extra:

```
# Morning Brief — [Day], [Date]

## Your Day
[TIME] — [Meeting] — EXTERNAL — [key outside attendee]
[TIME] — [Meeting] — internal
OOO: [names] *(only if anyone is out)*

## Your Top Tasks
⚠️ Overdue: [task] — [n] days late
Due today: [task]
[up to 5 total, overdue first]

## Pipeline — Watch This Week
[Deal] — [stage] — closes [date] — [why it's here]
[3-5 deals, closest close date first]

## Flags
[urgent/critical items] *(omit this section if nothing is flagged)*

## Priority Today
[ONE thing. One sentence saying why.]
```

## The rules that make this work

**Whole brief under 300 words.** Crisp bullets and short lines only — no paragraphs. It has to be readable in 2 minutes, on a phone, before coffee. Past 300 words it becomes a document, and a document gets saved for later, which means never.

**If something is both overdue AND client-facing, it surfaces first** — above everything, in every section. Internal overdue work makes you late. Client-facing overdue work makes the client wonder who else you're doing this to. One is a scheduling problem, the other is a retention problem.

**"Priority Today" is exactly ONE thing, never a list.** This is the single most important rule in the skill and the one that's easiest to quietly break. The moment it becomes three bullets, it's just the task list again and the brief has told the owner nothing they didn't already know. Picking is the entire value.

**If everything looks equally urgent, pick the one that unblocks the most other work.** Not the biggest, not the oldest, not the loudest. The one whose completion frees other people or other tasks. Ties broken by size mean you spend the morning on something impressive that nobody was waiting on.

**Never invent to fill a section.** No data means the section is skipped or says so in three words. A brief the owner learns to distrust once gets ignored forever after.

**Writing it somewhere is optional and always confirmed.** If there's a `~~docs` page, a `~~chat` channel, or a daily doc the owner wants this in and a connector exists, offer to write it there and wait for a yes. Otherwise deliver it in chat. Same brief either way.

## Worked example

**Input** — nothing connected except a calendar, and a pasted dump:

`"tasks: q3 budget doc (was due last thurs), offer letter for the new dev sign off today, vendor contract review sometime this wk, update the deck. deals — nova retail discovery closing fri, beacon corp sent proposal like 9 days ago nothing back, harlow group closed won last month"`

**Output:**

```
# Morning Brief — Tuesday, Aug 12

## Your Day
9:00 AM — Discovery call, Nova Retail — EXTERNAL — Priya Shah
2:00 PM — Design review — internal
OOO: design lead, back Thursday

## Your Top Tasks
⚠️ Overdue: Q3 budget doc — 5 days late
Due today: Sign off new dev offer letter
This week: Vendor contract renewal review
Backlog: Update the deck

## Pipeline — Watch This Week
Nova Retail — Discovery — closes Fri — you're talking to them at 9:00
Beacon Corp — Proposal sent — 9 days silent, no follow-up date set

## Priority Today
Beacon Corp. Nine days of silence on a live proposal is how deals die,
and the budget doc only blocks you — this blocks revenue.
```

Notice what it caught: Harlow Group was dropped (closed), the Flags section was omitted rather than printed empty, and Priority Today did *not* pick the overdue item — because the overdue item was internal and the silent proposal was client-facing.

## Tips

1. **Run it at the same time every day, before you open email.** Once email is open the day belongs to whoever wrote to you last, and the brief becomes a thing you read after you've already chosen wrong.
2. **If the priority is the same one three days running, it isn't the priority — it's the thing you're avoiding.** Either do it before anything else today or admit it's not actually important and delete it.
3. **Read your own calendar for the day *after* tomorrow, not just today.** The prep you needed to do for Thursday's client call was always going to be Tuesday's job.
4. **A pipeline line with no reason attached is noise.** "Beacon Corp — Proposal" tells you nothing. "9 days silent" tells you what to do in the next ten minutes.
5. **When the brief gets long, that's the signal — not the problem.** Over 300 words consistently means you're holding too much yourself. That's a delegation conversation, and the brief just handed you the list.

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want this built and delivered to you at 8:30 every morning, without you asking for it? See Agency Control Tower: controltower.collabai.software*
