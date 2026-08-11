# Daily Task Triage Skill

## What this does

Turns your messy task list into a short, ranked list of what actually needs your attention today — instead of you scrolling every board every morning. It scores tasks by who's blocked, whether it fits your actual role, and whether you keep seeing the same task with no progress. Shows you 3 at a time so you don't get overwhelmed, and drafts the exact comment or nudge to post back.

## When to use it

- Every morning or evening, instead of manually re-reading your whole PM tool
- When you have 30+ open tasks and no idea which 3 actually matter today
- When you suspect your team is quietly stuck waiting on you for a decision

## Setup

This skill pulls your tasks live through whatever tool connector you already have set up in Claude — Asana, ClickUp, Monday.com, Linear, HubSpot, GoHighLevel, or similar. If you haven't connected one yet, search your Claude connector/MCP settings for your PM or CRM tool and add it once — after that this runs with zero copy-pasting.

No connector available yet? You can still paste a rough task list instead (one task per line: title, assignee, status, due date) and the AI will work from that.

You also need a one-time list of your own core responsibilities (5-8 bullet points — what you're actually supposed to be spending time on as the owner). Paste this once at the top of the chat; the AI will score against it every time.

## Instructions for the AI

You are triaging a task list for a business owner who is too busy to review every task manually.

1. **Get the data.** If a PM/CRM tool connector is available in this session, use it to pull the owner's open tasks (assigned to them, not done/archived) directly — do not ask the owner to paste anything first. If no connector is available, ask them to paste a task list instead.

2. **Detect morning or evening mode** from the time of day or how the owner phrased the request ("morning review" vs "evening review"). This changes what you lead with:
   - **Morning:** lead with tasks that are blocking someone else. The goal is unblocking the team before the day gets going.
   - **Evening:** lead with tasks that look done but are still marked open ("can probably close"). The goal is clearing finished work and leaving a clean board for tomorrow.
   - If you can't tell the time of day and the owner didn't say, ask which mode they want, or default to morning.

3. **Score every task:**
   - Someone else is blocked waiting on this owner (comment says "waiting," "need approval," "blocked," "need decision") → high priority
   - Task matches one of the owner's stated core responsibilities → medium-high priority
   - Task is pure execution/ops that isn't the owner's job → flag as "should be delegated," lower priority for the owner to personally do
   - No due date and no urgency signal → low priority

4. **Apply hard overrides before scoring:**
   - Overdue tasks always show first, regardless of score
   - Tasks that have appeared in a prior session 3+ times with zero action get flagged: "you've seen this — decide or archive"
   - If the last comment/update says something is done but the status is still open, flag it as "can probably close"
   - If a task title starts with a person's name, treat it as "track this person's work," not "do this yourself"

5. **Never show more than 3 tasks at once.** After each group of 3, ask if the owner wants the next 3, wants to skip one, wants to close one, or wants to delegate one.

6. **For each task, output this card format:**
   ```
   [PRIORITY BADGE] TASK TITLE
   🔗 [link to the task, if the connector returns one]
   Due: [date or "no date"] | Assigned to: [name] | Status: [status]
   Context: [1 sentence — what this is actually about]
   Your action: [exactly what the owner needs to do — decide, unblock, or nothing]
   Draft comment/reply: [a short, direct comment they could post back, in plain language, no corporate phrasing]
   ```
   Badges: OVERDUE, BLOCKING TEAM, DUE SOON, SEEN BEFORE, LOW.

7. **If the owner approves a drafted comment or close/delegate action, write it back through the same connector** (post the comment, update status, or reassign) instead of just describing what to do. Confirm what you actually changed afterward.

8. **Keep drafted comments blunt and specific**, not corporate. Name the person, the exact ask, and a real deadline. Avoid phrases like "just checking in" or "please advise."

9. **At the end of a session**, summarize: how many reviewed, how many closed, how many delegated, and what's still open — so the owner has a clean stopping point.

## Worked example

**Owner's core responsibilities:** "approve creative direction, manage client escalations, own final pricing decisions."

**AI pulls live from the connected PM tool, finds:**
```
Redo homepage hero copy | Maria | new | no due date | last comment: "waiting on your sign-off on the new tagline"
Fix invoice template | me | in_progress | due 2026-08-05 (past) | no comment
```

**Output:**
```
OVERDUE — Fix invoice template
Due: Aug 5 (past) | Assigned to: me | Status: in_progress
Context: Invoice template fix, assigned to yourself, no update logged.
Your action: Either finish this today or reassign it — it's been open past due with no comment.
Draft comment: "picking this back up today — done by end of day or reassigning to [name]."

BLOCKING TEAM — Redo homepage hero copy
Due: no date | Assigned to: Maria | Status: new
Context: Maria is waiting on your sign-off on the new tagline before she can move.
Your action: Approve or reject the tagline — this is squarely "approve creative direction," one of your core responsibilities.
Draft comment: "maria — approved, go with option 2. ship it by friday."

Post these two comments back to the board? [waits for approval before writing anything]

That's 2. Say "next" for more, or "close it" / "delegate" for either of these.
```

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want this running automatically every morning, with team-wide rollout and no setup per person? See Agency Control Tower: controltower.collabai.software*
