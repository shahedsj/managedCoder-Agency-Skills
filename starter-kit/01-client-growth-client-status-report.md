---
name: client-status-report
description: Turn messy project notes into a clean, client-ready status update that protects the relationship when things slip. Use whenever the user needs to update a client — weekly or biweekly check-ins, milestone recaps, "what do I tell the client", or when they paste rough notes, chat messages, or a task export and need it turned into something sendable. Also use when a client is chasing for an update, when a project is late and the client has not been told yet, when scope is creeping and it needs to go on the record, or before a client call when the user needs to know where things actually stand.
---

# Client Status Report

Most agencies lose clients over surprise, not over quality. A status update is the cheapest insurance you can buy — it turns a slipping project into a managed project, in writing, before anyone gets angry.

> Tool placeholders like `~~project tracker` mean whatever tool you've connected in that category. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ Paste rough notes, chat copy, or a task export            │
│  ✓ Client-ready update under 200 words                       │
│  ✓ Flags what you're missing BEFORE you send                 │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~project tracker: pull the period's completed work        │
│  + ~~CRM: pull the contact and when you last updated them     │
│  + ~~email: draft straight into a reply on the live thread    │
└──────────────────────────────────────────────────────────────┘
```

## What I need from you

**Option A — Connected tools.** Name the client. I'll pull the last 7–14 days of activity.

**Option B — Paste anything.** Rough is fine:
`"finished homepage, started checkout, need their logo, still waiting on feedback from last week, dev says checkout done fri"`

**Option C — Just talk.** "Redesign is going okay but they still haven't sent content and it's starting to hurt the timeline."

Tell me once how this client likes it — short and blunt, or warmer with more context — and I'll match it every time.

## Step 1 — Work out the real situation before writing

Before drafting, decide which of these you're actually in. The answer changes the whole update, and getting it wrong is how updates cause damage.

| Situation | Signal in the notes | What the update must do |
|---|---|---|
| **On track** | Work completed, no blockers, dates holding | Confirm progress, keep it short |
| **Blocked on the client** | "waiting on", "need their", "no response" | Make the ask impossible to ignore, with a consequence |
| **Slipping, our fault** | Work behind, no client dependency | Say it plainly, give the new date and the recovery plan |
| **Slipping, their fault** | Their delay caused ours | Connect cause to effect, on the record, without blame language |
| **Scope creeping** | New requests appearing in notes | Name the new items as new, flag the impact, don't absorb silently |

If the notes are ambiguous between two of these, ask one question rather than guessing. Guessing "on track" when you're actually slipping is the single most expensive mistake this skill can make.

## Step 2 — Write the update

Use this exact structure. Skip any section that doesn't apply.

```markdown
**[Project] — update for [Client], [date]**

[One sentence. Where this stands: on track / on track but we need something / date moving.]

**Done this period**
- [Finished thing, in outcome language]
- [Finished thing]

**In progress**
- [Thing] — [specific date, not "soon"]

**We need from you**
- [Exact thing] — by [date], because [what it blocks]

**Timeline** *(only if a date is moving)*
[Old date] → [new date]. [One-sentence cause.] [What we're doing about it.]

**New requests** *(only if scope came up)*
[Item] — not in current scope. [Impact on time/cost.] Want us to quote it, or park it?

Next update: [date or milestone].
```

## Step 3 — Flag back to the user, separately

The update goes to the client. This part is for the user only — never include it in the client-facing text.

```markdown
⚠️ Before you send:
- [NEED: confirm the checkout date — notes said "Friday" but not which Friday]
- [The logo request is now 2 weeks old. Third time asking. Consider a call, not another email.]
- [You're absorbing 2 new requests without quoting them. That's ~6 hours unbilled.]
```

## The rules that make this work

**Write outcomes, not activity.** "Redesigned the checkout page," not "worked on checkout." Clients pay for outcomes and get nervous reading about effort. Translate anything technical into what they'd actually notice — "refactored the API layer" becomes "made the app load faster."

**Under 200 words unless they've asked for long-form.** Your update competes with 40 other emails. Long ones get skimmed, and the part that gets skipped is always "we need from you" — the only section with a deadline in it.

**Never invent a date, an owner, or a status.** Write `[NEED: confirm date]` and let the user fill it. A confident wrong date in a client email becomes evidence against you in a dispute. A bracket is a ten-second fix.

**Every ask gets a deadline AND a consequence.** "Logo files" is ignorable. "Logo files by Thursday, or the header slips a week" is not. Clients aren't ignoring you out of malice — they're triaging, and an ask with no stated cost loses the triage every time. This one habit does more to unblock projects than anything else in this skill.

**Never raise a risk without a next step attached.** A flag with no plan reads as panic and invites the client to start managing you. "Content is late, so we're building with placeholders and swapping Monday" reads as control. Same facts, opposite outcome.

**Bad news goes in the written update, early.** Slippage that appears in writing before the deadline is a project being managed. The identical slippage delivered after the deadline is a surprise — and surprise is what actually loses clients. If you're tempted to leave it out until you "have a better answer," that's the exact thing to put in.

**Name scope creep the first time it appears.** New requests absorbed silently become the baseline expectation, and by the third one you're doing free work and resented for pushing back. One neutral line — "not in current scope, want us to quote it?" — costs nothing early and is nearly impossible to raise later.

**Their delay, stated as cause and effect, not blame.** Not "you never sent the content." Instead: "Content arrived Aug 8 rather than Aug 1, so launch moves from Aug 15 to Aug 22." Facts and dates, no adjectives. This is the sentence that protects you three months later when someone asks why the project was late.

**Skip empty sections.** A manufactured risk section trains the client to ignore the real ones.

## Worked example

**Input:** `"finished homepage redesign, started checkout, need their logo files, waitin on their feedback from last week still, dev team says checkout done by fri, also they asked about adding a blog which wasnt in the SOW"`

**Output:**

> **Website Redesign — update for Nova Retail, Aug 12**
>
> On track, with two things we need from you to keep it that way.
>
> **Done this period**
> - Homepage redesign finished and ready for your review
> - Checkout flow build started
>
> **In progress**
> - Checkout flow — on track for Friday Aug 15
>
> **We need from you**
> - Logo files (high-res, any format) — by Thursday, so we can finalize the header
> - Feedback on the homepage draft — by Thursday. It's been open a week and final polish is paused until we hear back.
>
> **New requests**
> - Blog section — not in the current scope. Roughly 2 weeks of additional work. Want us to quote it, or park it until after launch?
>
> Next update: Friday, once checkout is live.

> ⚠️ Before you send:
> - The homepage feedback request is 8 days old. I've attached a date. If this is the second time asking, a 10-minute call will beat a third email.
> - Good catch flagging the blog before you started it. Do not begin any of that work until they answer.

## Tips

1. **Send on a schedule, not when there's news.** Clients who hear from you every Friday stop emailing to ask for updates. Silence is what makes them anxious — not bad news.
2. **The "we need from you" section is the whole point.** Everything above it is context. Put the real ask there, with a date and a cost, every single time.
3. **If you're dreading writing this update, that IS the update.** The project needs a conversation and the report should say so.
4. **Keep the last three.** When a client insists they were never told about a delay, a dated trail ends the conversation in one reply. This is why you write it down even when a call would be faster.
5. **The client who goes quiet is the risk, not the client who complains.** A complaining client is engaged. Two unanswered updates in a row is your signal to pick up the phone.

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want these written and sent automatically every Friday from your live project data? See Agency Control Tower: controltower.collabai.software*
