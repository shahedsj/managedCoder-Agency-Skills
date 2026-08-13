---
name: weekly-team-status-digest
description: Roll scattered team updates into one digest you can read in three minutes — what each person shipped, who's blocked, what's affecting more than one project, and who went quiet. Use every Friday or whenever the user says "what did everyone do this week", "weekly digest", "team update", "catch me up on the team", or pastes a pile of standup notes, chat messages, or task exports. Also use before a Monday leadership meeting, or when the user feels out of touch with what their team is actually working on.
---

# Weekly Team Status Digest

You don't need to know what everyone did. You need to know who's stuck, what's about to slip, and who has gone quiet. This finds those three things and ignores the rest.

> Tool placeholders like `~~project tracker` mean whatever tool you've connected in that category. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ Paste standup notes, chat copy, or a task export          │
│  ✓ Per-person digest, cross-team flags, capacity read        │
│  ✓ Names who didn't report — that's a finding, not a gap     │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~project tracker: pull completed and in-flight work       │
│  + ~~chat: pull standup posts and check-ins                   │
│  + ~~CRM: catch client-side blockers the team mentioned       │
└──────────────────────────────────────────────────────────────┘
```

## What I need from you

**Option A — Connected.** "Run my weekly digest." I'll pull the week's activity per person.

**Option B — Paste it.** Chat copy, a list of names with notes, a task export. Messy is fine.

**Option C — Name the team.** Give me who should be in it, and I'll tell you who's missing from whatever you paste.

**Give me the roster once** — who's on the team. Without it, people who sent nothing are invisible, and those are exactly the ones you need to see.

## Step 1 — Group by person, not by project

Group everything by the human, even though the data usually arrives by project. The question this answers is "what is each person carrying," and that only appears when one person's work is in one place.

A project view hides the person who's on four projects at 30% each — which is the person about to drop something.

## Step 2 — Read the three signals

For each person, extract:

**Shipped** — finished things, in outcome language. 2-3 bullets max. Not "worked on the API" but "checkout flow live."

**Blocked** — anything waiting on someone else, especially waiting on the owner. Name who it's waiting on.

**Capacity** — slammed / normal / light, only if the notes actually support it. Signals: number of active items, whether they mention being behind, whether they shipped nothing but were clearly busy.

## Step 3 — Produce the digest

```markdown
# Team digest — week ending [date]

**Pulse:** [One sentence on the week overall. Honest, not inflated.]

## Needs you
[Anything blocked specifically on the owner. Put this first — it's the only
 section with a deadline attached to the reader.]

## By person
**[Name]** — [what shipped]
Blocked: [what and on whom, or nothing]
Capacity: [slammed / normal / light]

**[Name]** — No update received.

## Cross-team flags
- [Thing affecting more than one person or project, most important first]

## Went quiet
[Anyone on the roster with no update, and how many weeks running]

## Worth calling out
[1-3 genuine wins. Skip the section rather than manufacture one.]
```

## The rules that make this work

**"No update received" is the most valuable line in the digest.** Never skip someone silently because they sent nothing. Silence is information — overloaded, disengaged, avoiding something, or already gone in their head. A digest that only shows the people who reported gives you a systematically optimistic view of your own company.

**Two weeks of silence from the same person is an escalation, not a note.** Say so explicitly. One quiet week is a busy week; two is a pattern, and the cost of asking is ten minutes while the cost of not asking is usually a resignation you didn't see coming.

**Put "Needs you" first.** The owner is the bottleneck on more items than they realise, and those items are the highest-leverage thing in the document. Burying them under a per-person list means they get read last, if at all.

**The same blocker from two people is the headline.** If two people independently mention the same client, the same missing access, the same stalled decision — that is the single most important line in the digest, and it belongs at the top of cross-team flags. One person mentioning a problem is a problem; two people mentioning it independently is a systemic one.

**Don't editorialize on performance.** State what's in the notes. "Sara shipped nothing this week and mentioned being blocked on design" — not "Sara is struggling." The owner has context you don't, including things they can't put in writing, and a judgement from a digest can quietly poison how they read that person for months.

**Outcomes, not activity.** "Checkout flow live" not "continued work on checkout." Activity language makes a stalled week look productive, which defeats the purpose of reading this at all.

**Three minutes, hard limit.** This is a Friday-afternoon read. If it takes fifteen minutes, it gets skipped in week three and the habit dies.

**Distinguish blocked-on-owner from blocked-on-client.** Both are blocks, but only one of them the owner can clear this afternoon. Mixing them means the actionable ones get lost.

## Worked example

**Input:** `"sara: finished checkout flow, still waiting on client feedback on homepage. mike: closed 2 deals, one client asking about pricing for add-ons. josh: nothing sent again. dana mentioned the acme client hasn't responded in over a week, sara said the same thing"`

**Output:**

> # Team digest — week ending Aug 15
>
> **Pulse:** Solid delivery week. One client responsiveness issue showing up from two people, and a second week of silence from Josh.
>
> ## Needs you
> - Nothing blocked on you directly this week.
>
> ## By person
> **Sara** — Checkout flow finished.
> Blocked: client feedback on the homepage draft.
> Capacity: normal
>
> **Mike** — Closed 2 deals. An existing client is asking about add-on pricing.
> Blocked: nothing
> Capacity: normal
>
> **Dana** — Flagged the Acme client as unresponsive.
> Blocked: Acme, over a week silent
> Capacity: not stated
>
> **Josh** — No update received. **Second week running.**
>
> ## Cross-team flags
> - **Acme has not responded in over a week — raised independently by Dana and Sara.** Two people blocked on the same client means this is bigger than one project. Worth a direct call rather than another email.
> - Mike has a live add-on pricing question. That's revenue sitting in an inbox.
>
> ## Went quiet
> - Josh — 2 weeks, no update. Worth a direct conversation this week.
>
> ## Worth calling out
> - Mike closed 2 deals.

> ⚠️ The two things I'd act on:
> - Josh at two weeks is the real story in this digest, not the Acme client.
> - Acme being raised by two people independently means it's already costing you more than one project's time.

## Tips

1. **Read the quiet, not the loud.** The people writing detailed updates are usually fine. The one-line update and the missing update are where the risk is.
2. **Answer "Needs you" before you close the laptop Friday.** Every item in that section costs someone else Monday morning. Clearing it Friday buys your team a full day.
3. **Don't forward the digest to the team.** It contains your read on capacity and silence. It's for you. If you want to share wins, pull those out separately.
4. **Same blocker three weeks running is a system problem.** Stop chasing it as a task. Something structural — an approval nobody owns, access nobody has — is generating it, and it'll keep coming back until that gets fixed.
5. **If the digest is always green, you're reading the wrong inputs.** Real weeks have friction. A consistently clean digest usually means people are reporting what they think you want to hear, and the actual problems are surfacing somewhere you're not looking.

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want this built automatically every Friday from your team's real activity, with nothing to collect? See Agency Control Tower: controltower.collabai.software*
