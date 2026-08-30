---
name: competitor-prospect-scan
description: Build a one-page research brief on a company before you pitch, compete, or renew — what they do, what's likely hurting, what's changed recently, and two or three specific things to open a conversation with. Use whenever the user says "research [company]", "look up this prospect", "who am I up against", "prep me for a call with", "what do we know about", or names a competitor they're competing with on a deal. Also use before a renewal conversation, before responding to an RFP, or any time they're about to walk into a call knowing only the company name.
---

# Competitor / Prospect Scan

Walking into a call having read their website is table stakes. Walking in having spotted the thing they're clearly struggling with is what makes them lean forward.

> Tool placeholders like `~~CRM` mean whatever tool you've connected in that category. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ Give a company name — web research does the rest          │
│  ✓ Snapshot, likely pains, recent moves, opening lines       │
│  ✓ Everything marked confirmed vs inferred                    │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~CRM: pull existing notes and past interactions first     │
│  + ~~email: check whether anyone here has talked to them      │
│  + ~~enrichment: headcount, tech stack, funding detail        │
└──────────────────────────────────────────────────────────────┘
```

## What I need from you

**Just the company name.** A website or LinkedIn URL helps but isn't required.

**Tell me which job this is doing:**
- **Prospect** — you're pitching them
- **Competitor** — you're up against them on a deal
- **Both** — you're pitching a company that also competes with a client

**Tell me the context if there is one.** "They came inbound from our newsletter" or "we lost to them last year" changes what's worth digging for.

## Step 1 — Check what you already know

If a `~~CRM` or `~~email` connector is available, search the company name **before** going to the web. Existing notes, a past deal, an old thread, a colleague who already met them.

This matters more than it sounds. Presenting research on a company your own team pitched eight months ago — without mentioning it — is embarrassing in a way that's hard to recover from mid-call.

## Step 2 — Research, marking every claim

The whole brief is only useful if the user can tell fact from guess. Mark every line:

- **Confirmed** — found on their site, a filing, a press release, a job posting
- **Likely** — a reasonable inference from what was found
- **Unconfirmed** — you couldn't verify it

**The highest-signal sources, in order:**

1. **Job postings.** The best single source and the most ignored. What they're hiring for is what they're investing in; how many roles tells you scale; the requirements list their actual tech stack. Three open sales roles and no marketing roles tells you exactly where their pressure is.
2. **Recent news** — funding, leadership changes, launches, layoffs, acquisitions. Anything in the last 3-6 months is a trigger event, and trigger events are why deals happen at all.
3. **Their own site** — positioning, who they say they serve, case studies and their dates. A case-study page where the newest entry is two years old says something.
4. **LinkedIn activity** — what leadership posts about is what's on their mind this quarter.

## Step 3 — Produce the brief

Keep it to one page. This is a scan before a call, not a research report.

```markdown
# [Company] — [Prospect / Competitor] brief
[Date]

## Snapshot
[What they do, rough size, industry, who they serve — 2-3 sentences.]
[Confirmed / Likely on each claim.]

## What's changed recently
- [Event] — [date] — [source]
[If nothing found in the last 6 months, say exactly that. Do not pad with old news.]

## Likely pain points  *(inferred, not confirmed)*
- [Problem] — because [the evidence that suggests it]

## If competitor — how we compare
| | Them | Us |
|---|---|---|
| Positioning | | |
| Apparent price point | | |
| Where they look stronger | | |
| Where we look stronger | | |

## Conversation openers
1. [Specific thing you can reference that proves you looked]
2. [A question their situation makes genuinely interesting]

## What I couldn't confirm
- [Gap] — worth asking on the call
```

## The rules that make this work

**Mark inferred as inferred, every time.** The value of this brief is that the user can lean on the confirmed parts in a call. If guesses are dressed as facts, one wrong number said confidently to a prospect undoes the whole thing — and they will correct you.

**When you find nothing, say so.** "No significant news in the last 6 months" is a real finding. Padding with generic industry commentary that would apply to any company is worse than a short brief, because it buries the two things that actually matter.

**Never fabricate a name, title, headcount, or funding figure.** Write "unconfirmed" instead. These are exactly the details people repeat out loud in meetings, and exactly the ones that are embarrassing to get wrong.

**Be honest about where they're stronger.** A competitor brief that only flatters you is useless — it leaves the user unprepared for the one objection they'll actually face. If the competitor has six case studies in the prospect's vertical and you have none, that belongs in the brief in plain language, along with what to say about it.

**Openers must be specific enough that they couldn't have been written for anyone else.** "I saw you're growing!" proves nothing. "You've got three sales roles open in Chicago but nothing in marketing — is the plan to grow the team before the pipeline, or is marketing handled elsewhere?" proves you looked and starts a real conversation.

**Stay professional about competitors.** Factual, fair, no dismissive language. Parts of this brief tend to get pasted into emails and forwarded, and a snide line about a competitor reads badly the moment it leaves the room.

**One page, hard limit.** This gets read in the ten minutes before a call. A three-page brief doesn't get read at all, which makes it worth less than a short one.

## Worked example

**Input:** `"BrightPath Digital — competitor, we're both pitching a hospitality client next week"`

**Output (excerpt):**

> # BrightPath Digital — Competitor brief
> Aug 12, 2026
>
> ## Snapshot
> Mid-size full-service marketing agency in Chicago. **Likely** 20-40 people (based on LinkedIn employee count, not confirmed). Focused on paid media and web design for mid-market retail and hospitality. **Confirmed** from their site.
>
> ## What's changed recently
> - No funding, leadership, or launch news found in the last 6 months.
> - **Confirmed:** two open roles — a paid media strategist and an account manager, both posted within the last month. Suggests they're staffing delivery, not new business.
>
> ## Likely pain points *(inferred)*
> - Hiring an account manager while hiring a strategist usually means existing accounts are stretched. **Likely** delivery capacity pressure.
>
> ## How we compare
> | | Them | Us |
> |---|---|---|
> | Positioning | Paid media first, design attached | Systems and ops first |
> | Where they look stronger | 4 hospitality case studies, one from this year | We have none in hospitality |
> | Where we look stronger | No ops/automation offer visible on their site | This is our whole pitch |
>
> ## Conversation openers
> 1. Ask directly whether they're evaluating other Chicago shops. If they name BrightPath, you can go straight to the ops angle instead of competing on paid media.
> 2. "Most hospitality clients tell us turnaround speed matters more than campaign volume — is that true for you?" — sets up your strength before their case studies come up.
>
> ## What I couldn't confirm
> - Their pricing. Nothing public. Worth asking the prospect what range they've been quoted.

> ⚠️ Worth knowing before the call:
> - They're stronger than you on hospitality proof. Don't compete there — get the conversation onto operations early, or you're arguing on their ground.

## Tips

1. **Read the job postings first.** Ten minutes there beats an hour on the homepage. The homepage is what they want you to think; the job board is what they're actually doing.
2. **A trigger event is worth more than a pain point.** New funding, a new exec, a layoff, a system migration — these are why companies buy now instead of eventually. If you find one, it's the opening line.
3. **Bring the gap to the call, not just the findings.** The "couldn't confirm" list is your question list. Asking a sharp question you couldn't answer online lands better than reciting facts they already know about themselves.
4. **Against a competitor, never mention them first.** Ask who else they're talking to. Volunteering a competitor's name puts them in the room and makes you look worried.
5. **Save the brief to the deal.** Six months later when this comes back around, the version of them you researched today is context nobody else on your team will have.

---
*Free next step: join a live class and get the weekly AI-for-agencies newsletter at managedcoder.com*

*Part of the Agency Skill File Starter Kit — ManagedCoder. Want a brief like this generated automatically the moment a new lead lands in your pipeline? See Agency Control Tower: controltower.collabai.software*
