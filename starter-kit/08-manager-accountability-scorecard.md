# Manager Accountability Scorecard Skill

## What this does

Turns your team's task data into a one-page scorecard for your Monday meeting — completion rate, overdue count, and a risk color per manager, plus the sharp, specific talking points you should actually raise in the room. Pairs well with the Weekly Delegated Task Review skill (run that Friday, run this Monday).

## When to use it

- Before a Monday leadership or all-hands meeting
- Whenever someone asks "how is everyone actually doing on their tasks"
- When you want a projectable, visual accountability report instead of a gut feeling

## Setup

Uses whatever PM/CRM connector you have set up in Claude (Asana, ClickUp, Monday.com, Linear, HubSpot, GoHighLevel, etc.) to pull two things live: tasks completed in the last 7 days per person, and all currently open tasks per person with status and due date. No connector yet? Paste the same two things instead and it still works.

## Instructions for the AI

You are building a manager accountability scorecard from your team's task data.

1. **Get the data.** If a connector is available, pull it directly: completed-this-week counts per person, and open-task detail (status, due date) per person. Only ask the owner to paste data if no connector is available.

2. **Calculate per person:**
   - Completion rate = completed this week ÷ (completed this week + total open), as a whole-number percentage
   - Overdue count = open tasks past their due date
   - Never-started count = open tasks still in a "not started" state

3. **Assign risk color:**
   - RED = 3+ overdue, OR any task overdue 14+ days, OR completion rate under 20%
   - YELLOW = 1-2 overdue, OR 4+ never-started, OR completion rate 20-50%
   - GREEN = 0 overdue AND completion rate over 50%

4. **Output a markdown table:**
   ```
   | Manager | Open | Done ✅ | Overdue ⚠️ | Never Started | Rate | Status |
   |---------|------|---------|------------|---------------|------|--------|
   | [name]  | [n]  | [n]     | [n]        | [n]           | [%]  | 🔴/🟡/🟢 |
   ```

5. **Below the table, add three short sections:**
   - **Critical — address in meeting:** every RED person, with their single most overdue/important task named specifically (pull the actual task title from the connector, don't generalize)
   - **Watch — monitor this week:** every YELLOW person, one line each
   - **Performing — acknowledge:** every GREEN person, brief recognition

6. **Add a "Meeting Talking Points" section** — one sharp, specific question per person, not a generic accountability question. Base it on their actual overdue/stalled task, not a template. Example: not "please provide an update" but "is the client portal redesign still happening, or should we kill it — it's been 'in progress' for six weeks with nothing shipped."

## Worked example

**AI pulls live from the connected tool:**
```
Completed this week: Priya — 4, Sam — 0
Open tasks: Priya — 3 open, 0 overdue, 0 never started. Sam — 6 open, 4 overdue (including "Client Portal Redesign," 42 days), 2 never started.
```

**Output:**
```
| Manager | Open | Done ✅ | Overdue ⚠️ | Never Started | Rate | Status |
|---------|------|---------|------------|---------------|------|--------|
| Priya   | 3    | 4       | 0          | 0             | 57%  | 🟢     |
| Sam     | 6    | 0       | 4          | 2             | 0%   | 🔴     |

## Critical
Sam — 4 tasks overdue, 0 completed this week. Most urgent: "Client Portal Redesign," overdue 42 days.

## Performing
Priya — 57% completion rate, zero overdue. Nice work.

## Meeting Talking Points
Sam — is the client portal redesign still happening, or should we kill it — it's been open 42 days with nothing shipped?
```

---
*Part of the Agency Skill File Starter Kit — ManagedCoder by SJ Innovation. Want this scorecard generated automatically every Monday with zero manual pulls? See Agency Control Tower: controltower.collabai.software*
