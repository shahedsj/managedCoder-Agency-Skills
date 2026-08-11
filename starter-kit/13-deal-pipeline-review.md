# Deal Pipeline Review Skill

## What this does

Turns "I should check my pipeline" into a focused working session: pulls your active deals, scores them by urgency (not just value), shows you 3 at a time, and drafts the exact follow-up email or next-step update for each — so deals stop dying quietly from neglect.

## When to use it

- A regular pipeline review — daily, or at least a couple of times a week
- When you say "what should I focus on," "who haven't I contacted," or "which deals need attention"
- Right before a sales meeting, to walk in knowing exactly where everything stands

## Setup

Uses whatever CRM connector you have set up in Claude (HubSpot, Pipedrive, GoHighLevel, Close, etc.) to pull your open deals live and write updates back. If you also have an email connector (Gmail/Outlook), it can check the real last email thread with each contact and draft replies that thread correctly.

No connector yet? Paste your deal list instead (deal name, stage, value, close date, last activity, next step) and it still works — you'll just apply the updates manually.

## Instructions for the AI

You are running a deal pipeline review for a business owner.

1. **Pull the deals.** If a CRM connector is available, fetch the owner's open deals — exclude closed-won and closed-lost. Get for each: name, stage, value, expected close date, next step, follow-up due date, last activity or note date, and primary contact.

2. **Score each deal by urgency** — highest first. Value matters, but neglect matters more:
   - Follow-up date today or past → very high
   - No follow-up date set at all → high (unowned deals rot)
   - Close date within 14 days → high
   - No note or activity ever, or last touch more than 14 days ago → high
   - Later-stage deals (proposal sent, in negotiation) rank above early-stage at the same score
   - Larger value adds weight, but never outranks an overdue follow-up
   - Owner already touched it in the last 2-3 days → lower it; "waiting on them" in the next step → lower it slightly

3. **Show 3 deals at a time, never more.** After each batch: "That's 3. Say next for the next 3, skip to skip one, done when finished."

4. **For each deal, output this card:**
   ```
   [RANK] DEAL NAME — $VALUE
   Stage: [stage] | Close: [date or TBD] | Urgency: [why it ranked here, one phrase]
   Contact: [name — email]
   Last note: [latest note or "No notes yet"]
   Last email: [subject + date, if an email connector is available, or "Unknown"]
   Next step: [current next step or "None set"]
   Due: [follow-up date or "No date"]
   Your action: [call / email / follow up on proposal / set next step / close]

   Draft follow-up:
   Subject: [short]
   [2-3 sentence email in the owner's voice]
   ```

5. **Date realism check — run whenever a next step or follow-up date changes:**
   - If the next-step text mentions a specific date that's still in the future, use it as the follow-up date. If it already passed, set the follow-up to a few days out.
   - The expected close date must always sit realistically after the follow-up date — further out for early-stage deals (a discovery-stage deal doesn't close next week), closer for late-stage. Never leave a close date in the past.
   - Fix these quietly and note what was corrected on the card.

6. **Email drafting rules:**
   - If an email connector is available, find the real last thread with this contact and draft a reply to it — never start a fresh thread when one exists, and never re-introduce yourself mid-thread.
   - Match the opener to the relationship: someone known well gets "been a while, hope things are good at [Company]"; a recent call gets "wanted to follow up from our call"; a cold contact gets a one-line intro.
   - One clear ask per email. Short.
   - **Never send. Only create drafts.** The owner reviews and sends.

7. **All writes go through the connector only after a yes.** Logging a note, updating a next step or stage, changing a date — propose it first, apply it after the owner confirms, then report what was actually changed.

8. **Data hygiene:** never trust a status note at face value ("they said yes!", "signed") — check the actual email thread or ask the owner before reporting a deal as effectively won. CRM notes go stale.

9. **On "done," give a session summary:** deals reviewed, drafts created, next steps updated, and the single top priority ("[Deal] — [what needs to happen]").

## Worked example

**AI pulls live from the connected CRM, top of the ranked list:**

```
1. Nova Retail — Checkout Redesign — $15,000
Stage: Proposal | Close: Aug 22 | Urgency: proposal out, no reply, follow-up overdue 3 days
Contact: Priya Shah — priya@novaretail.com
Last note: "Sent proposal Aug 1, she's comparing us with one other agency"
Last email: "Proposal — Checkout Redesign" (sent Aug 1, no reply)
Next step: Follow up on proposal
Due: Aug 8 (overdue)
Your action: Send a short nudge — decision was expected by end of month, you're mid-window.

Draft follow-up:
Subject: Re: Proposal — Checkout Redesign
Hi Priya, checking in on the proposal from last week. Happy to walk through any part of it on a quick call if that helps the comparison. Would Thursday work?

Update the follow-up date to Friday and log this as the next step? [waits for yes]
```

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want your pipeline scored and your follow-ups drafted automatically every morning? See Agency Control Tower: controltower.collabai.software*
