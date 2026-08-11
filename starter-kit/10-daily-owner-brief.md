# Daily Owner Brief Skill

## What this does

One scannable brief, every morning: your calendar, your top tasks, which deals need attention this week, any flags, and — most importantly — the ONE thing you should actually focus on today. Built to be read in under 2 minutes on your phone before your day starts.

## When to use it

- First thing in the morning, before you open five different tabs to piece your day together
- Any time someone asks "what's my day look like" or "catch me up"
- As a recurring daily habit — this is the single highest-leverage 5 minutes of your day

## Setup

Pulls live from whatever connectors you have set up in Claude: a calendar connector (Google Calendar/Outlook), a PM/task connector (Asana, ClickUp, Monday, etc.), and a CRM connector (HubSpot, Pipedrive, GHL, etc.) for pipeline. Missing one or more? The brief just skips that section, or you can paste the relevant info instead.

## Instructions for the AI

You are building a same-day owner's brief. Always get today's actual date first — never assume or hardcode it.

1. **Pull today's calendar**, if a calendar connector is available. Split into external meetings (attendees outside your own company domain) and internal ones. Flag anyone marked out-of-office/WFH today if that's visible.

2. **Pull the owner's own open tasks**, if a PM connector is available: top 5 by priority and due date, overdue and due-today flagged clearly.

3. **Pull a pipeline snapshot**, if a CRM connector is available: deals owned by this person, excluding closed-won/closed-lost, sorted by closest close date. Show the top 3-5, especially anything closing this week or overdue for follow-up.

4. **Check for any flags** — if the owner has a way of marking things urgent/critical (a tag, a priority field, a specific list), surface those here. Otherwise skip this section.

5. **Compose the brief in this exact structure, and nothing extra:**
   ```
   # Morning Brief — [day], [date]

   ## Your Day
   [calendar items, OOO flags]

   ## Your Top Tasks
   [top 3-5, overdue flagged with a warning marker]

   ## Pipeline — Watch This Week
   [top deals with close dates]

   ## Flags
   [anything urgent/critical]

   ## Priority Today
   [ONE single most important thing — synthesized from everything above, not a list]
   ```

6. **Output rules:**
   - Crisp, no fluff, bullet points and short lines only — readable in 2 minutes
   - Whole brief under 300 words
   - If something is both overdue AND client-facing, it always surfaces first
   - "Priority Today" is the most important line in the whole brief — pick exactly ONE thing, never a list. If everything looks equally urgent, pick the one thing that unblocks the most other work.

7. If the owner has a place they want this written to daily (a Notion page, a doc, a specific channel) and a connector for it is available, write it there too — otherwise just deliver it in chat.

## Worked example

**Output:**
```
# Morning Brief — Tuesday, Aug 12

## Your Day
9:00 AM — Discovery call with Nova Retail (external)
2:00 PM — Internal design review
OOO: Maria (design lead)

## Your Top Tasks
⚠️ Overdue: Approve Q3 budget doc
Due today: Sign off on new hire offer letter
This week: Review vendor contract renewal

## Pipeline — Watch This Week
Nova Retail — Discovery — closing this Friday
Beacon Corp — Proposal sent — no update in 9 days, needs a nudge

## Flags
None today.

## Priority Today
Approve the Q3 budget doc — it's overdue and blocking two other people's work.
```

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want this delivered to you automatically every morning at 8:30am, with zero manual triggering? See Agency Control Tower: controltower.collabai.software*
