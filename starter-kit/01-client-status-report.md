# Client Status Report Skill

## What this does

Turns rough, messy project notes into a clean, client-ready status update — so you're not staring at a blank doc trying to remember what actually happened this week.

## When to use it

- Every time you need to send a client an update — weekly, biweekly, or after a milestone
- When all you have is scattered notes, Slack messages, or half-sentences and need them turned into something sendable
- Right before a client call, to get your own head straight on where things stand

## Setup

Works best with a PM/project connector (Asana, ClickUp, Monday.com, Notion, etc.) so it can pull recent task activity and comments for this client's project directly. If you also have a CRM connector, it can pull the client contact and last-update date too.

No connector yet? Just paste your raw notes — Slack copy-paste, half sentences, a task list export, whatever you've got — and it still works exactly the same way.

## Instructions for the AI

You are turning raw project notes into a client-facing status update.

1. **Get the material.** If a PM connector is available, pull recent activity/comments for this client's project. Otherwise, use whatever raw notes the owner pastes in.

2. **Write the update in this structure:**
   - **Opening line** — one sentence, plain language, no fluff. State where the project stands right now (on track, ahead, or needs a decision from the client).
   - **What we completed this period** — 3-5 bullets max. Each bullet is a finished thing, not a task in progress. Use plain outcomes ("Redesigned the checkout page," not "Worked on checkout").
   - **What's in progress** — 2-4 bullets. Say what's being worked on and give a realistic date, not "soon."
   - **What we need from the client** — if nothing is needed, say "Nothing needed from you right now." If something is needed (approval, content, a decision, access), name it exactly and give a deadline.
   - **Risks or flags** — only include this section if something is actually at risk. Don't manufacture a risk section if there isn't one. If there's a risk, say what it is and what's being done about it — never raise a flag without a next step attached.
   - **Closing line** — one sentence. Next update date or next milestone.

3. **Apply these rules:**
   - Total length: under 200 words unless the client specifically wants long-form updates.
   - No jargon the client wouldn't use themselves. If the notes say "refactored the API layer," rewrite it as what the client actually notices ("made the app load faster").
   - Never write "we're working hard on this" or similar filler — it says nothing. Say what was actually done.
   - If the notes don't tell you something (a date, a decision owner), don't guess — write "[NEED: confirm date]" so the owner catches it before sending, instead of inventing one.
   - Match the tone to the client relationship: keep it warm but professional, like an update from someone who respects their time.

4. **Deliver the draft for review.** This is a draft to edit and send, not something to send automatically — even if an email or messaging connector is available, wait for explicit approval before sending anything.

## Worked example

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
