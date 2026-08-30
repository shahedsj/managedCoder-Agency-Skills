---
name: deal-pipeline-review
description: Run a working deal review — pull your open deals, score them by urgency, work them 3 at a time, and draft the actual follow-up email for each. Use whenever the user says "my deals", "my pipeline", "deal review", "who haven't I contacted", "what should I focus on", "which deals need attention", "next 3", "keep going", "draft follow-up", or "update next step". Also use when they mention a specific deal and want to log a note, change a stage, or set a next step.
---

# Deal Pipeline Review

Deals don't die from bad pitches. They die from silence. This runs the review that catches silence before it becomes a lost deal.

> Tool placeholders like `~~CRM` mean whatever tool you've connected in that category. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ Paste your deal list or a CRM export                      │
│  ✓ Urgency scoring, 3 at a time, drafted follow-ups          │
│  ✓ Close-date realism check                                  │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~CRM: pull deals live, write notes and next steps back    │
│  + ~~email: read the real last thread, draft in-thread reply  │
│  + ~~calendar: see meetings already booked per deal           │
└──────────────────────────────────────────────────────────────┘
```

## What I need from you

**Option A — Connected CRM.** Just say "my deals." I'll pull them.

**Option B — Paste them.** Deal name, stage, value, close date, last activity, next step. Missing fields are fine — I'll flag them as hygiene issues.

**Option C — One deal.** "Pull up Nova Retail" works too.

## Step 1 — Pull the deals

Get every open deal owned by this person. Exclude closed-won and closed-lost. For each one you want: name, stage, value, expected close date, follow-up/next-action date, next step text, last activity date, last note and its date, and the primary contact with email.

**Owner matching is where this goes wrong.** In most CRMs the owner ID is unreliable — shared across reps, or duplicated with name variants ("Madhav Ranganekar" vs "Madhav Ravindra Ranganekar"). Match on owner *name* with a fuzzy/contains match, and confirm the count looks right before doing anything. If the number of deals looks wrong to the user, stop and fix the filter before scoring — a review of the wrong deal set wastes the whole session.

## Step 2 — Score every deal

Add the points. Highest score first.

| Condition | Points |
|---|---|
| Follow-up date is today or past | **+5** |
| Close date within 14 days | **+4** |
| Last note more than 14 days ago | **+4** |
| No follow-up date set at all | **+3** |
| No note ever logged | **+3** |
| Stage = proposal sent | **+3** |
| Last note more than 7 days ago | **+2** |
| Stage = estimation / scoping | **+2** |
| Value over $10,000 | **+2** |
| Stage = discovery | **+1** |
| Value over $5,000 | **+1** |
| No contact email on file | **+1** |
| Owner already commented in last 3 days | **−2** |
| Next step says "waiting" on them | **−1** |

Why it's weighted this way: an overdue follow-up outranks a big deal on purpose. A $50k deal you touched yesterday needs nothing from you today. A $6k deal you've ignored for three weeks is actively dying. Neglect is the thing you can fix this morning; size isn't.

The user can override — "focus on big deals" or "only show me proposals" — and you should re-rank on request rather than arguing for the default.

## Step 3 — Close-date realism check

Run this any time a next step or follow-up date changes. CRMs fill up with close dates that already passed, which quietly destroys every forecast built on them.

**Follow-up date:** if the next-step text names a specific future date ("Aug 17", "week of Sep 3"), use it. If the named date already passed, or none is named, set it to last-note-date + 7 days — or today + 3 days if that's still in the past.

**Close date** must sit at least this far after the follow-up date:

| Stage | Minimum gap |
|---|---|
| Proposal, probability ≥ 50% | 14 days |
| Proposal, probability < 50% | 21 days |
| Estimation / scoping | 30 days |
| Discovery | 45 days |
| Lead | 60 days |

If the existing close date already clears the minimum and is in the future, leave it alone. If it's empty, in the past, or too close to the follow-up date, push it to the new minimum. Never set a close date in the past. Never let a follow-up date land after the close date.

Report corrections on the card rather than silently changing them.

## Step 4 — Show 3 at a time

Never more than 3. A list of 40 deals gets skimmed and nothing happens; 3 gets worked.

After each batch: *"That's 3. Say **next** for the next 3, **skip** to skip one, **done** when you're finished."*

### Deal card

```
[RANK] DEAL NAME — $VALUE
Stage: [stage] | Close: [date or TBD] | Score: [n] — [the single reason it ranked here]
Contact: [name] — [email] — [phone]
Last note: [text + date, or "No notes yet"]
Last email: [subject + who + date, or "None found"]
Next step: [text or "None set"]
Due: [follow-up date or "No date"]
Close realism: [OK / corrected to [date] — [why]]
Your action: [call / email / follow up on proposal / set next step / close]

Draft follow-up:
Subject: [short, or "Re: [existing thread subject]"]
[2-3 sentences]
```

## Step 5 — Email drafting rules

**Check the real thread first.** If an email connector is available, find the actual last exchange with this contact before drafting. Never draft from the CRM contact field alone — in most CRMs contacts attach to the *company*, not the deal, so a client with several deals will show you the wrong person. Verify the email against a real thread before using it.

**Always reply into the existing thread.** Get the newest message and reply to it so it threads correctly. Starting a fresh thread when one exists is the single clearest signal that a message was automated.

**Never re-introduce yourself** if a thread already exists.

**Tier the opener to the relationship:**
- Knows you well → "been a while, hope things are good at [Company]."
- One or two touches → "wanted to follow up from our call."
- Cold → one short line of intro.

**One ask per email.** Two asks get zero answers.

**Draft only. Never send.** The user reviews and sends every message.

## Step 6 — Writing anything back

Log the note *before* updating the deal fields, so there's always a written reason for the change sitting next to it.

Everything is proposed first and written only after a yes: notes, next steps, stage changes, date pushes, reassignment. Then report what actually changed — not what you intended to change.

**Before any bulk action** (mass date push, bulk stage change), re-filter to this owner's deals only and show the user the list you're about to touch. Bulk-editing another rep's deals is not recoverable by apology.

## Step 7 — Data hygiene

**Never trust a status note at face value.** "WON", "they signed", "verbally agreed" — check the actual email thread before reporting a deal as closed. CRM notes are frequently stale, aspirational, or were true for a different deal. A CEO who reports a win that didn't happen loses more credibility than one who reports a smaller number.

## Session commands

| User says | Do |
|---|---|
| next | Show the next 3 |
| skip | Skip this one, continue |
| draft follow-up | Draft the reply, in-thread |
| log meeting | Post meeting notes as a deal note |
| update next step | Update next step + follow-up date, run the realism check |
| move to [stage] | Update the stage |
| reassign to [name] | Change owner, log why, notify them |
| more context | Pull the full deal, all notes, all emails |
| close it | Won or lost — ask which |
| done | End, show summary |

## On "done"

```
DEAL REVIEW — [date]
Reviewed: [n] | Emails drafted: [n] | Notes logged: [n] | Next steps set: [n] | Dates corrected: [n]
Top priority: [deal] — [what has to happen]
```

## Worked example

**Input:** "my deals"

**Output:**

```
1. Nova Retail — Checkout Redesign — $15,000
Stage: Proposal | Close: Aug 22 | Score: 12 — proposal out 10 days, follow-up 3 days overdue
Contact: Priya Shah — priya@novaretail.com
Last note: "Sent proposal Aug 1, comparing us with one other agency" (Aug 1)
Last email: "Proposal — Checkout Redesign" (you → Priya, Aug 1, no reply)
Next step: Follow up on proposal
Due: Aug 8 (overdue)
Close realism: OK — Aug 22 clears the 14-day minimum for proposal at 60%
Your action: Nudge. She said end of month, you're mid-window and silent.

Draft follow-up:
Subject: Re: Proposal — Checkout Redesign
Hi Priya, checking in on the proposal from last week. Happy to walk through
any part of it on a call if that helps the comparison. Would Thursday work?

Push the follow-up date to Friday and log this as the next step? [waits]
```

## Tips

1. **Run it daily, not weekly.** Ten minutes a day beats an hour on Friday — by Friday the deals that went quiet on Monday are four days colder.
2. **A deal with no next step is not a deal.** It's a hope. Either set one this session or move it to lost. Both outcomes are better than leaving it.
3. **The "−2 if you touched it in 3 days" rule matters more than it looks.** Without it, the same three loud deals top the list every day and everything else silently rots.
4. **Close-lost is a real answer.** A clean pipeline you trust is worth more than a big pipeline you don't. Killing a dead deal costs nothing and makes every forecast truer.

---
*Free next step: join a live class and get the weekly AI-for-agencies newsletter at managedcoder.com*

*Part of the Agency Skill File Starter Kit — ManagedCoder. Want this scored and drafted for you every morning, across your whole team's pipeline? See Agency Control Tower: controltower.collabai.software*
