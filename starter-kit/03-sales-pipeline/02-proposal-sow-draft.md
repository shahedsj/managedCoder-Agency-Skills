---
name: proposal-sow-draft
description: Turn discovery call notes into a first-pass proposal or scope of work you can edit and send. Use whenever the user has had a discovery call and needs a proposal, says "write a proposal for", "draft an SOW", "scope this project", "they asked me to send something over", or pastes call notes about a prospect's requirements. Also use when a project keeps growing and needs a written scope, when a client asks "how much would it cost to", or when the user is about to quote a number and hasn't written down what's included.
---

# Proposal / SOW Draft

Proposals don't lose on price. They lose on ambiguity — the client couldn't tell exactly what they were buying, so they compared you on the only number they understood.

This produces a first draft you edit, not a final you send.

> Tool placeholders like `~~CRM` mean whatever tool you've connected in that category. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ Paste discovery notes or describe what they want          │
│  ✓ Full proposal draft with scope, exclusions, assumptions   │
│  ✓ Flags every gap you need to fill before sending           │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~CRM: pull the deal's notes and logged call summary       │
│  + ~~meeting notes: pull the actual discovery transcript      │
│  + ~~docs: match the format of proposals you've sent before   │
└──────────────────────────────────────────────────────────────┘
```

## What I need from you

**Option A — Connected.** "Draft the proposal for Nova Retail." I'll pull the deal notes and call transcript.

**Option B — Paste the notes.** Anything from the call. Rough is fine.

**Option C — Describe it.** "12-person marketing agency, wants a client portal, budget maybe 5-8k, needs it in 6 weeks."

Tell me the deal size if it isn't obvious. A $3K proposal and a $50K proposal are different documents, and writing the wrong one costs you either the deal or the margin.

## Step 1 — Find the pain and the "why now"

Before structuring anything, find these two things in the notes:

**The pain, in their words.** Not "they need a website" but "they're losing time every Friday manually compiling client reports." Use their language, not yours — the opening paragraph should make them feel heard, and nothing does that like their own sentence read back to them.

**The "why now."** Why is this happening this quarter and not next year? A new hire, a lost client, a system that broke, a competitor move, a funding round. If the notes contain a why-now, it opens the document. If they don't, flag it — a project with no why-now is the one that goes quiet for three months after you send the proposal.

## Step 2 — Draft the proposal

```markdown
# [Project name] — Proposal for [Client]
[Date] · Valid for 30 days

## The situation
[2-3 sentences restating what they want and why now, in their words.]

## What we'll do
### Phase 1 — [Name] (Weeks 1-2)
- [Countable deliverable]
- [Countable deliverable]

### Phase 2 — [Name] (Weeks 3-5)
- [Countable deliverable]

### Phase 3 — [Name] (Week 6)
- [Countable deliverable]

## What's not included
- [Thing discussed but excluded] — can be quoted separately
- [Thing they might assume is included but isn't]

## Timeline
[Phase-by-phase, in ranges. Total: X-Y weeks from kickoff.]

Timeline assumes [the client dependency] is provided by [when].

## Investment
[FEE]
[Payment terms: deposit % to start, remainder on X]

## What we need from you
- [Content, access, approvals] — by [when], because [what it blocks]

## Assumptions
- [Thing being assumed true]
- Includes [N] rounds of revision per deliverable. Additional rounds quoted separately.

## Next steps
[What happens when they approve: kickoff call, contract, deposit.]
```

## Step 3 — Flag back to the user

Separate from the proposal. This is for them, not the client.

```markdown
⚠️ Before you send:
- [CONFIRM: pricing — notes said "5-8k", I left [FEE] blank]
- [No "why now" in the notes. Ask before sending, or this stalls.]
- [They mentioned a blog "maybe later" — I put it in exclusions so it can't
   be assumed into scope.]
- [No revision limit was discussed. I defaulted to 2. Change if wrong.]
```

## The rules that make this work

**Countable deliverables, always.** "3 homepage concepts" not "design work." "2 rounds of revision" not "revisions until happy." Vague scope is how a 60-hour project becomes 140 hours, and you can't renegotiate a word like "revisions" once it's signed. If you can't put a number on it, it isn't scoped yet — flag it.

**The exclusions section is where the money is.** Everyone writes the inclusions. Almost nobody writes exclusions, and then argues about them for free three months later. Anything discussed on the call and not being built goes here. So does anything a reasonable client might *assume* is included — hosting, content writing, ongoing support, training, mobile app.

**Never invent pricing.** Leave `[FEE]` and let the user fill it. A number you guessed becomes the anchor the whole negotiation runs from, and you can't take it back.

**Revision rounds are the number one scope leak.** Default to 2 rounds per deliverable unless told otherwise, state it in Assumptions, and say additional rounds are quoted separately. This single line prevents the most common way agency projects lose money.

**Name the client dependency in the timeline, not just the ask list.** "Timeline assumes content is provided by week 2" converts *their* delay into a visible, agreed cause. Without it, every slip becomes your fault by default.

**Put an expiry on it.** 30 days is standard. It protects your pricing, and it gently creates a reason to decide. A proposal with no expiry sits open forever and gets used to shop you.

**Match the length to the deal size.** A $3K proposal that runs eight pages reads as overhead and makes the price feel high. A $50K proposal that runs one page reads as careless. Roughly: under $10K → 1-2 pages. $10-50K → 3-5. Above that, phases and detail earn their space.

**Flag with `[CONFIRM: ...]`, never guess.** Especially on price, timeline, and anything technical. This is a draft for the owner to correct — guessing wastes the review pass and risks a wrong number reaching the client.

## Worked example

**Input:** `"call w/ 12 person marketing agency, they want a client portal so clients stop emailing for status, they lose fridays doing manual reports, budget probably 5-8k, want it in 6 weeks, asked about a blog too but that's maybe later"`

**Output (excerpt):**

> # Client Portal — Proposal for [Client]
> Aug 12, 2026 · Valid for 30 days
>
> ## The situation
> Your team is spending most of Friday manually compiling client status reports, and clients still email asking where things stand. This project builds a portal where your clients can see project status themselves — removing the Friday reporting block and the "just checking in" emails.
>
> ## What we'll do
> **Phase 1 — Discovery & Design (Weeks 1-2)**
> - Portal wireframes
> - 2 design concepts
> - 1 client review round
>
> **Phase 2 — Build (Weeks 3-5)**
> - Client login and accounts
> - Project status dashboard
> - File sharing
> - Email notifications
>
> **Phase 3 — Launch (Week 6)**
> - QA and fixes
> - Team walkthrough
> - Go-live
>
> ## What's not included
> - Blog section — can be quoted separately
> - Custom mobile app
> - Payment processing
> - White-labelling the portal for your own clients
>
> ## Timeline
> 6 weeks from kickoff. Assumes your client list and branding assets are provided in week 1.
>
> ## Investment
> [FEE]
>
> ## Assumptions
> - Includes 2 rounds of revision per deliverable. Additional rounds quoted separately.

> ⚠️ Before you send:
> - [CONFIRM: price. Notes said 5-8k. Left blank.]
> - The blog is now in exclusions — that stops it drifting into scope for free.
> - No "why now" captured. Worth one question: is there a deadline driving the 6 weeks, or is that a guess? It changes your leverage.

## Tips

1. **Send it within 48 hours of the call.** Proposal quality matters less than proposal speed. The one that arrives while they still remember the conversation wins more often than the polished one that arrives next week.
2. **Walk them through it live if the deal matters.** A proposal sent cold gets read for the price. A proposal walked through gets read for the plan. For anything above your average deal size, book 20 minutes.
3. **If you can't write the scope, you didn't finish discovery.** Vagueness in the draft is a signal, not a writing problem. Go back and ask rather than papering over it with soft language.
4. **Quote the phase, not the hours.** Hours invite negotiation on your rate. Deliverables invite negotiation on scope — which is the conversation you actually want.
5. **The exclusions list is a sales tool, not just protection.** It shows you listened to everything, and it gives them a menu for later. Half your follow-on revenue is sitting in that section.

---
*Free next step: join a live class and get the weekly AI-for-agencies newsletter at managedcoder.com*

*Part of the Agency Skill File Starter Kit — ManagedCoder. Want proposals drafted the moment a deal hits discovery, from your real call notes? See Agency Control Tower: controltower.collabai.software*
