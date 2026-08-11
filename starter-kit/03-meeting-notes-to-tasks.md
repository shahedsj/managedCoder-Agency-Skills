# Meeting Notes to Tasks Skill

## What this does

Turns a meeting transcript, recording notes, or rough scribbles into a clean list of action items — who owns what, and by when — so nothing said out loud gets lost.

## When to use it

- Right after any client call, team standup, or internal meeting
- When a meeting happened somewhere your task tool doesn't automatically capture it
- Any time you realize commitments were made verbally but never turned into anything trackable

## Setup

Works with a meeting-tool connector (Zoom, Google Meet, etc.) if you have one — it can pull the transcript or summary directly. If you also have a PM/task connector (Asana, ClickUp, Monday.com, Linear, etc.), it can create the action items as real tasks instead of just listing them.

No connectors yet? Paste the transcript, notes, or scribbles instead — it still works, you'll just create the tasks manually afterward using what's drafted.

## Instructions for the AI

You are turning meeting content into action items.

1. **Get the material.** If a meeting-tool connector is available, pull the transcript or summary. Otherwise, use whatever notes are pasted in.

2. **Produce two things:**
   - **Meeting summary** — 3-5 sentences max. What was discussed, what was decided. Skip small talk and tangents.
   - **Action items table** — every commitment made in the meeting, in this format:

     | Task | Owner | Deadline | Notes |
     |---|---|---|---|
     | ... | ... | ... | ... |

3. **Apply these rules:**
   - Only include something as an action item if someone actually committed to it out loud ("I'll send that Friday," "let's get design started"). Don't invent tasks that weren't discussed.
   - If a task was mentioned but no owner was named, write "UNASSIGNED" in the Owner column — don't guess who's doing it.
   - If no deadline was given, write "NO DATE SET" — don't invent a date. A fake deadline is worse than no deadline.
   - If two people disagreed about something, or a decision wasn't actually finalized, put it in a separate "Open Questions" section, not in the action items table — an open question is not a task.
   - Keep owner names exactly as said in the meeting (first names are fine, don't formalize them).
   - If the meeting was with a client, flag any task that is the CLIENT's responsibility separately from the team's own tasks — these often get missed.

4. **Propose creating the tasks, don't create them automatically.** If a PM connector is available, ask: "Want me to create these as tasks?" Only create them through the connector after a yes, matching owner and deadline from the table above.

## Worked example

**Input (raw meeting notes):** "talked about the launch date, sara said she'll get the final copy to us by wednesday, we still need to decide on the hosting provider, mike is gonna look into pricing options and get back to us, client said they'll review the design friday"

**Output:**

> **Summary:** Discussed the upcoming launch. Copy delivery and hosting provider decision are the two open items blocking progress; design is in client review.
>
> | Task | Owner | Deadline | Notes |
> |---|---|---|---|
> | Send final copy | Sara | Wednesday | Client-side task if Sara is on client team — confirm |
> | Research hosting pricing options | Mike | NO DATE SET | |
> | Review design draft | CLIENT | Friday | Client responsibility |
>
> **Open Questions:**
> - Which hosting provider we're going with — not yet decided
>
> Want me to create these as tasks?

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want every meeting logged and turned into tasks automatically, without pasting anything? See Agency Control Tower: controltower.collabai.software*
