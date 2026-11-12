---
name: relationship-network-keeper
description: Keep the people who send your agency work warm, and stop treating them like cold leads. Sorts every contact into Network of 90, List of 20, or Lead, then drafts the right touch for each. Use when the user asks who to reach out to this week, when a partner, client, or referral source has gone quiet, when a follow-up list mixes partners with prospects, when someone says "I keep pitching people I should just be friends with", when planning business development with little time, or when they paste a contact list and ask what to do with it.
---

# Relationship Network Keeper

Most agencies say their best clients come from referrals. Then they run their partners, past clients, and friends through the same follow-up queue as cold leads. One pitch to the wrong person costs more than ten unanswered cold emails. This skill splits the list first, then drafts the right kind of touch.

> Tool names below use placeholders like `~~CRM`. See CONNECTORS.md for examples.

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ Paste a contact list with any notes you have              │
│  ✓ Get each person tiered, with the reason                   │
│  ✓ Get today's 3 touches drafted, under 80 words each        │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~CRM: reads notes, deals and last-contact dates itself   │
│  + ~~email: checks for real two-way replies                  │
│  + ~~calendar: finds meetings already held                   │
└──────────────────────────────────────────────────────────────┘
```

## What I need from you

Any one of these:
1. **Connected ~~CRM.** I pull contacts, notes, deals, and last-contact dates.
2. **A pasted list.** Name, company, and whatever notes you have. Messy is fine.
3. **One name.** "What should I send Dana this month?"

## Step 1 — Tier every contact before anything else

Do this before ranking, matching a service, or drafting. The tier decides the whole message.

| Tier | Who | Touch | Cadence |
|---|---|---|---|
| **Network of 90** | Partner, client, friend, event co-host, referral source. Test: could you text them "I'm in town, coffee?" and expect a yes? | Share knowledge, share care, or share network. **No pitch, no service, no demo ask.** | Every 30 days |
| **List of 20** | Someone you want to know: a connector, chamber head, speaker, author, editor | Show up where they are. Add value first. Ask permission before sending anything. | When an event or chance comes up |
| **Lead** | Everyone else | Normal sales follow-up | Every 30 to 60 days |

**Why 90 and 30 days:** 3 people a day covers 90 people in a month. About 10 minutes a day. More than 90 is fine, the math just changes.

### How to decide, in this order

Stop at the first signal that fits, and say which one you used.

1. **The notes say it.** "Partner", "client", "friend", "not a cold lead", "do not pitch", "referral source", "co-host" → Network of 90.
2. **A won or open deal** with this person → Network of 90 (they are a client).
3. **Real two-way history:** a meeting held, or a reply in their own words → Network of 90, unless notes say otherwise.
4. **The user names them** as someone they want to meet → List of 20.
5. **Nothing above** → Lead.

**Two traps that caught real people:**
- **Attempts are not a relationship.** 4 emails with 0 replies is a Lead, not Network of 90. Only count history where they wrote back.
- **Old labels need a date.** "Existing client" written in 2021 is history, not a live relationship. If the note is over 12 months old and nothing newer backs it, ask.

**When signals disagree, ask one question.** The most expensive wrong guess is pitching a partner. The cheapest is being too warm with a lead. If unsure, lean warm.

## Step 2 — Check who owns the relationship

If the notes say someone else manages this person ("the owner handles this one", "Dana's contact"), stop. Do not draft. Hand it back and name the owner. Writing to someone else's relationship without asking breaks trust inside your own team.

## Step 3 — Pick today's touches

Default: **3 Network of 90 contacts per day.** Sort by last contact date, oldest first. Anyone past 30 days goes first. Leads come after, never before.

## Step 4 — Draft the touch

**Network of 90 — one of three, under 80 words, ends with one easy question:**
- **Share knowledge:** "Saw this and thought of you" plus one line on why it fits them.
- **Share care:** congrats on news, a launch, a hire, an event they ran.
- **Share network:** offer one specific introduction. Ask both sides before connecting them.

**List of 20 — under 60 words.** Name the thing of theirs you actually engaged with (talk, article, post). Offer one useful thing. Ask permission to send it.

**Lead** — normal follow-up. A first touch should give something useful (a free resource, a class) with no ask.

## Output

Use this structure every time:

```markdown
## Relationship touches — [date]

**Today: [N] Network of 90 · [N] List of 20 · [N] Leads**

### 1. [Name] — [Company]
**Tier:** [Network of 90 / List of 20 / Lead] — signal: [which rule, in a few words]
**Last real contact:** [date or "none found"] *(days since: [N])*
**Touch type:** [Share knowledge / Share care / Share network / Permission ask / Follow-up]

> [Draft, under 80 words, ends with one question]

**Record update to propose:** Tier: [tier] · next touch in [30] days · note: "[YYYY-MM-DD] tiered as [tier], [signal]"

---

⚠️ Before you send *(only you see this)*:
- [Name is in your sales queue but tiered Network of 90. Move them out or they get a pitch next week.]
- [Intro offered to X. Ask X first.]
- [NEED: notes say "client" but last activity is 2021. Confirm before treating as warm.]
- [Skipped [Name]: owned by [owner].]
```

## The rules that make this work

- **Tier before you draft.** The same "just checking in" reads as care to a friend and as pressure to a stranger. Content follows tier, not the other way round.
- **No pitch to Network of 90, even a soft one.** They already know what you sell. A pitch tells them the relationship was a funnel all along, and they stop sending referrals.
- **Every touch ends with one easy question.** "How's the new hire working out?" gets a reply. A statement gets a like.
- **Write the tier into the record.** If it lives only in this chat, next week's run puts the partner back in the cold queue. Propose the note; never save it without a yes.
- **When a tool replaces notes, send old notes plus the new line.** Many ~~CRM fields overwrite on save. Losing years of history to add one line is a bad trade.
- **Nothing sends.** Drafts only. Every record change is proposed, then made only after a yes, then reported.

## Worked example

**Input (pasted):**

```
dana - partner agency, we refer dev work to each other, last call june
mike at the chamber - want to meet him, he runs the tuesday breakfast
priya acme corp - 4 emails no reply
tom r - "existing client" (note from 2021)
lee - sarah handles this one
dana just posted they hired a new ops lead
```

**Output:**

```markdown
## Relationship touches — 12 Nov

**Today: 1 Network of 90 · 1 List of 20 · 1 Lead** (2 held back)

### 1. Dana — partner agency
**Tier:** Network of 90 — signal: notes say "partner", mutual referrals
**Last real contact:** June *(days since: ~150)*
**Touch type:** Share care

> Hi Dana, saw you brought on a new ops lead. Big step, congrats.
> That role changed everything for us when we filled it. What made
> you decide now was the time?

**Record update to propose:** Tier: Network of 90 · next touch in 30 days

### 2. Mike — Chamber breakfast
**Tier:** List of 20 — signal: you named him as someone to meet
**Touch type:** Permission ask
**Do first:** go to one Tuesday breakfast. Introduce yourself in person.
> (Draft after you meet: thank you note + offer the AI policy checklist, ask if you can send it.)

### 3. Priya — Acme Corp
**Tier:** Lead — 4 attempts, 0 replies. Attempts are not a relationship.
**Touch type:** Follow-up — give, don't ask

> Hi Priya, no need to reply to my earlier notes. Here's a free
> one-page guide we use for client status updates, in case it's
> useful. Is this even on your plate right now?

---

⚠️ Before you send:
- Dana is 120 days past the 30-day cadence. This is the one that matters today.
- Tom R: "existing client" is from 2021 with nothing newer. NEED: is he still a client? Not drafted.
- Lee: skipped. Sarah owns this relationship.
- Priya: after this, stop for 60 days. A 6th unanswered email starts to cost you.
```

## Tips

- If you can't remember the last time you talked to someone who sent you work, that is your first message today.
- The best touch is the one with your name nowhere in it. An intro between two of your contacts makes you the person they both talk about.
- If a partner only hears from you when you need something, they already know. Fix it this week, not after the next ask.
- Your sales tool and your relationship list are different jobs. Mixing them is how partners end up in drip campaigns.
- Ten minutes a day beats one big catch-up quarter. Nobody remembers the quarterly blast.

---

*Part of the Agency Skill File Starter Kit — ManagedCoder. Here you tier and draft by hand each morning; Control Tower tracks every relationship's last touch, keeps partners out of the sales queue, and queues today's 3 for your yes. See Agency Control Tower: controltower.collabai.software*

*Inspired by the "network of 90" and "list of 20" ideas from Michael Port and Matthew Kimberley's Book Yourself Solid.*
