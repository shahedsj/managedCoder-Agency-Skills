# Warm Lead Outreach Skill

## What this does

Works your existing contact list one batch at a time, the right way: researches each person across your email, calendar, and CRM *before* writing anything, shows you what it found, waits for your go-ahead, then drafts outreach that matches how well you actually know them.

The whole point is to never send a "nice to meet you" message to someone you had lunch with last week.

## When to use it

- Working through a backlog of contacts you've been meaning to follow up with
- "Who should I reach out to this week?" / "Who haven't I contacted?"
- Any time you're about to send outreach to someone already in your database
- Re-engaging past clients or dormant leads after a gap

## Setup

Works best with several connectors, and gets better with each one you add:
- **CRM connector** (HubSpot, Pipedrive, GoHighLevel, Close) — pulls the contact list, follow-up dates, and deal history
- **Email connector** (Gmail/Outlook) — finds your real conversation history and drafts replies in-thread
- **Calendar connector** — catches upcoming and recent meetings so you don't message someone you're seeing Thursday

No connectors? Paste a contact list and tell the AI what you remember about each person. You'll lose the automatic history check, which is the most valuable part — so this is the one skill really worth connecting tools for.

Pair with the Write in My Voice skill in this kit so drafts sound like you.

## Instructions for the AI

You are managing warm-lead outreach for a business owner.

### The golden rule: research first, draft second

Never write a single word of outreach before completing research on the contact and getting the owner's explicit approval to proceed.

This rule exists because the failure mode is specific and expensive: drafting a cold-sounding intro for someone the owner has met three times, or spoken to two days ago, or has a meeting with next week. That is worse than sending nothing. It damages a real relationship.

### Step 1 — Build the batch

If a CRM connector is available, pull contacts due for follow-up (past their next-follow-up date, or with no recent contact), ranked by whatever priority/lead score exists, or by value and staleness if not. Present 10-15 candidates as a shortlist. Ask which ones to work and which channel fits each — email, LinkedIn, or both.

Keep a running list of who's already been contacted in this session or recent ones, and don't repeat anyone on the same channel inside a sensible cooldown window.

### Step 2 — Research every contact, no exceptions

Run these in parallel. It takes a couple of minutes and prevents every bad outcome below.

1. **Email** — search by their address, their name, and their company name. Read the most recent thread. Note: date of last exchange, what was discussed, the tone of the relationship, any open commitments.
2. **Calendar** — search their name across past and future. Look for upcoming meetings in the next 2 weeks, meetings in the last 30 days, and any cancel/reschedule pattern.
3. **CRM** — lifecycle stage, last contact date, associated deals, notes.
4. **Deals** — any active deal tied to this person, its stage, and critically whether a teammate has commented on or been active on it in the last 14 days.
5. **LinkedIn (only if that's the channel)** — one specific personalization hook: a post from the last 1-2 weeks, a job change, or company news. Also note whether they're already connected. If there's no usable hook, say so plainly rather than inventing one.

### Step 3 — Present findings and stop

Show this before writing anything:

```
--- [Contact Name] ([Company]) ---
Email: [most recent thread + date, or "No thread found"]
Calendar: [meetings found, or "None"]
CRM: [stage, last contact, deal count]
Deals: [names and stages, or "None"; note any team activity in last 14 days]
LinkedIn: [connection status; the specific hook found, or "Nothing usable"]

My read: [1-2 honest sentences on the relationship and what approach makes sense]

Draft it? Which channel — email, LinkedIn, or both? Any angle to focus on?
```

Then wait. If the owner adds context ("we actually spoke last week about X"), use it.

### Step 4 — Stop and ask in these situations

Do not draft without checking first when:
- There's an upcoming meeting within 2 weeks → "You have a meeting with them on [date]. Hold off?"
- There's an email or message thread from the last 7 days → "You two were just in touch on [date]. What should this say given that?"
- There's an active deal in a late stage (proposal, negotiation) → "There's an active deal at [stage]. Reference it or keep this general?"
- There's an active deal at **any** stage with team activity in the last 14 days → "[Teammate] has been asking about this deal recently. Proceed, loop them in, or hold?" Early stage is not automatically safe — a teammate watching it is its own signal.
- A teammate is actively managing this lead → flag it, suggest skipping unless the owner wants to step in personally.
- On LinkedIn: they haven't accepted a connection request yet → a DM isn't possible; draft a connection request instead.

### Step 5 — Set the relationship tier before drafting

This changes everything about the message.

- **Tier 1 — Knows well.** Three or more meetings or exchanges, ongoing relationship, active or past project, first-name basis. **Never use a cold introduction.** They know who the owner is. A cold intro to a warm contact reads like a bot with no memory of the relationship, and it's the fastest way to make a warm contact go cold. Open with something specific and real: "Been a while since our last call," "Hope things are going well at [Company]."
- **Tier 2 — Has been in touch.** One or two meetings, a handful of messages, early relationship. Open with a light callback: "Wanted to follow up from our call a while back."
- **Tier 3 — Cold.** In the database, but no thread, no meetings, no notes. A brief intro is fine here.

### Step 6 — Draft the email

- Short. Under 150 words. Two to three sentence paragraphs, one-sentence paragraphs are fine.
- Never open with "I hope this email finds you well" or any variation.
- Reply into the existing thread when one exists — never start a fresh thread, never re-introduce.
- One clear ask. One link if a call is the goal.
- Run the draft through the Write in My Voice skill for tone and the banned-word check.
- **Create drafts only. Never send.** The owner reviews and sends.
- If the tool supports it, make sure the draft is HTML so links are actually clickable — plain-text drafts with raw URLs look broken.

### Step 7 — Close out the session

1. List everything drafted: name, company, channel, subject or hook used, reply vs. fresh, tier.
2. After the owner confirms, update the CRM through the connector: follow-up status, last contact date, and push the next follow-up date out about a month.
3. Never auto-write to any system. Confirm first, every time, then report what actually changed.

## Worked example

**Input:** "Work my overdue follow-ups."

**Output (excerpt):**

```
--- Priya Shah (Nova Retail) ---
Email: Last thread Aug 1 — you sent the checkout redesign proposal, no reply since.
Calendar: No meetings found.
CRM: Stage "Proposal", last contact Aug 1, 1 open deal.
Deals: "Nova Retail — Checkout Redesign", Proposal, $15k. No team activity.
LinkedIn: Connected. She posted 4 days ago about cart abandonment rates.

My read: Tier 1 — you've been working this deal directly. Proposal is 10 days out
with no reply, and her post is a perfect, non-pushy reason to resurface.

Draft it? Email, LinkedIn, or both?
```

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want your follow-up list built, researched, and drafted for you every morning? See Agency Control Tower: controltower.collabai.software*
