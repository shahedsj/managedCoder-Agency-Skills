# Weekly Delegated Task Review Skill

## What this does

Takes everything you've assigned to other people and turns it into a per-person accountability report: who's on track, who's stalled, who's overloaded, and who's quietly stuck waiting in a hand-off chain. Drafts the follow-up notes and emails for you, and produces a clean Monday-morning brief.

## When to use it

- Every Friday, before the week ends, to catch problems before they become excuses
- Before a Monday leadership or all-hands meeting
- Any time you feel like tasks are "out there somewhere" and you've lost track of who owns what

## Setup

Uses whatever PM/CRM connector you already have set up in Claude (Asana, ClickUp, Monday.com, Linear, HubSpot, GoHighLevel, etc.) to pull everything you created and assigned to someone else — live, no exporting. If you also have an email connector (Gmail/Outlook) connected, the AI can draft follow-up emails directly instead of just describing them.

No connector yet? Paste a rough list instead (title, assignee, status, due date, created date, latest comment) and it still works.

## Instructions for the AI

You are running a weekly delegated-task accountability review for a business owner.

1. **Pull the data.** If a PM/CRM connector is available, use it to fetch every task the owner created that is assigned to someone else, excluding done/archived. Don't ask the owner to paste anything first unless no connector is available.

2. **Check for two traps before scoring anything:**
   - **Duplicate delegation:** the same piece of work sometimes shows up as two separate task rows assigned to two different people (same or near-identical title). Don't double-count this against either person — list them as co-owners of one job.
   - **Chain/hand-off tasks stuck mid-flow:** if a task description mentions passing it to the next person in a sequence, check how long it's sat with whoever currently has it — not just whether it's overdue overall.

3. **Group all tasks by assignee.** For each person calculate:
   - Total open tasks
   - Overdue count (past due date, not done)
   - Never-started count (still in a "new"/"not started" state)
   - Risk level: RED = 3+ overdue or anything overdue 14+ days; YELLOW = 1-2 overdue or 3+ never started; GREEN = on track

4. **Flag these patterns specifically, by name:**
   - STALLED: created 30+ days ago, still not started
   - GHOST PROGRESS: marked "in progress" for 14+ days with no visible update
   - OVERLOADED: same person has 5+ open tasks
   - STUCK IN CHAIN: a hand-off task sitting with someone past their expected turn
   - SPLIT OWNERSHIP: duplicate task assigned to 2+ people — needs one clear owner

5. **Get today's actual date first** — never assume or hardcode it — then calculate the coming Monday from that. Draft a short, direct follow-up note for every RED person, and — if the owner confirms — post it back through the connector as a comment on the task. Rules: plain language, no corporate phrasing ("please provide a status update" is banned), name the specific overdue task, ask what's actually blocking them, set a real deadline (default: the coming Monday you just calculated). One or two sentences.

6. **If an email connector is available and the owner wants emails sent** (not just task comments), draft one per RED person: under 200 words, lists the specific overdue tasks, asks what's blocking them, sets that same coming Monday as the deadline, signs off simply. Save as a draft — do not send without the owner's explicit go-ahead.

7. **Produce the brief** in this structure:
   ```
   # Weekly Delegated Task Review — [date]

   ## Immediate Action Required (RED)
   [person — specific tasks — what's at stake]

   ## Watch List (YELLOW)
   [person — one line each]

   ## On Track (GREEN)
   [person — brief]

   ## Stuck in Chain
   [task — who it's stuck with — how long]

   ## Split Ownership
   [task — all co-owners — needs one clear owner]

   ## Decisions This Review Needs From You
   [anything blocked waiting on the owner personally]
   ```

8. **Confirm what was actually changed** (comments posted, due dates updated, emails drafted) at the end — don't just describe actions, report what was done through the connector.

## Worked example

**AI pulls live from the connected PM tool, finds 3 rows:**
```
Redesign onboarding email | Dana | new | created 45 days ago | no due date | no comment
Redesign onboarding email | Chris | new | created 44 days ago | no due date | no comment
Client renewal call notes | Dana | in_progress | due last week | no comment in 20 days
```

**Output:**
```
## Split Ownership
"Redesign onboarding email" is assigned to both Dana and Chris — same job, two owners. Pick one and reassign or cancel the duplicate.

## Immediate Action Required (RED)
Dana — "Client renewal call notes" is overdue by a week with no update in 20 days. This is a real stall, not in-progress.

Draft note to Dana: "dana — client renewal notes were due last week, no update in 20 days. what's blocking this? need it by monday."

Post this comment to the task now? [waits for approval before writing anything back]
```

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want this running automatically every Friday across your whole team's tools, no setup per person? See Agency Control Tower: controltower.collabai.software*
