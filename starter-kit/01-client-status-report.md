# Skill: Client Status Report

**What this does:** Turns rough, messy project notes into a clean, client-ready status update.

**When to use it:** Every time you need to send a client an update — weekly, biweekly, or after a milestone — and all you have is scattered notes, Slack messages, or half-sentences.

---

## Instructions for the AI

When I give you raw project notes (bullet points, Slack copy-paste, half sentences, task list exports), write a client-facing status update using this structure:

1. **Opening line** — one sentence, plain language, no fluff. State where the project stands right now (on track, ahead, or needs a decision from the client).
2. **What we completed this period** — 3-5 bullets max. Each bullet is a finished thing, not a task in progress. Use plain outcomes ("Redesigned the checkout page" not "Worked on checkout").
3. **What's in progress** — 2-4 bullets. Say what's being worked on and give a realistic date, not "soon."
4. **What we need from the client** — if nothing is needed, say "Nothing needed from you right now." If something is needed (approval, content, a decision, access), name it exactly and give a deadline.
5. **Risks or flags** — only include this section if something is actually at risk. Don't manufacture a risk section if there isn't one. If there's a risk, say what it is and what we're doing about it — never raise a flag without a next step attached.
6. **Closing line** — one sentence. Next update date or next milestone.

## Rules

- Total length: under 200 words unless the client specifically wants long-form updates.
- No jargon the client wouldn't use themselves. If you wrote "refactored the API layer," rewrite it as what the client actually notices ("made the app load faster").
- Never say "we're working hard on this" or similar filler — it says nothing. Say what was actually done.
- If the notes don't tell you something (a date, a decision owner), don't guess — write "[NEED: confirm date]" so I catch it before sending, instead of inventing one.
- Match the tone to the client relationship: keep it warm but professional, like an update from someone who respects their time.

## Example

**Input (raw notes):** "finished homepage redesign, started checkout flow, need their logo files, waitin on their feedback from last week still, dev team says checkout done by fri"

**Output:**

> Quick update on the redesign project — we're on track.
>
> **Completed this week:**
> - Finished the homepage redesign
> - Started work on the new checkout flow
>
> **In progress:**
> - Checkout flow — on track for this Friday
>
> **We need from you:**
> - Your logo files (high-res, any format) so we can finalize the header
> - Feedback on last week's homepage draft — we're paused on final polish until we hear back
>
> Next update: end of this week, once checkout is live.

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want reports like this generated and sent automatically every Friday? See Agency Control Tower: controltower.collabai.software*
