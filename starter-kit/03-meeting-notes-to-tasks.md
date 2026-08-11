# Skill: Meeting Notes → Tasks

**What this does:** Turns a meeting transcript, recording notes, or your own scribbles into a clean list of action items — who owns what, and by when.

**When to use it:** Right after any client call, team standup, or internal meeting, so nothing said out loud gets lost.

---

## Instructions for the AI

When I give you meeting notes or a transcript, produce two things:

1. **Meeting summary** — 3-5 sentences max. What was discussed, what was decided. Skip small talk and tangents.
2. **Action items table** — every commitment made in the meeting, in this format:

| Task | Owner | Deadline | Notes |
|---|---|---|---|
| ... | ... | ... | ... |

## Rules

- Only include something as an action item if someone actually committed to it out loud ("I'll send that Friday," "let's get design started"). Don't invent tasks that weren't discussed.
- If a task was mentioned but no owner was named, write "UNASSIGNED" in the Owner column — don't guess who's doing it.
- If no deadline was given, write "NO DATE SET" — don't invent a date. A fake deadline is worse than no deadline.
- If two people in the meeting disagreed about something or a decision wasn't actually finalized, put it in a separate "Open Questions" section, not in the action items table — an open question is not a task.
- Keep owner names exactly as said in the meeting (first names are fine, don't formalize them).
- If the meeting was with a client, flag any task that is the CLIENT's responsibility separately from our team's tasks — these often get missed.

## Example

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

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want every meeting logged and turned into tasks automatically, without pasting anything? See Agency Control Tower: controltower.collabai.software*
