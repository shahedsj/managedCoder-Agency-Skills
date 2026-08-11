# Skill: Weekly Team Status Digest

**What this does:** Rolls up scattered updates from your team (Slack messages, standup notes, task list exports, individual check-ins) into one clean weekly digest for you as the owner — so you're not chasing five people for "what did you get done this week."

**When to use it:** Every Friday (or whenever your week ends), once you've collected raw updates from your team.

---

## Instructions for the AI

When I give you a pile of raw team updates (could be copy-pasted Slack messages, a list of names with notes, task exports), produce a digest with this structure:

1. **One-line company pulse** — a single sentence on how the week went overall (busy but on track / a few things slipped / strong week, ahead of schedule). Base this on what's actually in the notes, don't inflate it.
2. **By person** — for each team member mentioned, a short block:
   - **[Name]** — what they completed (2-3 bullets max), what's blocked or needs your input (if anything), one line on capacity (slammed / normal / light) if that's inferable from the notes.
3. **Cross-team flags** — anything that affects more than one person or project (a client waiting on something, a shared blocker, a deadline at risk). This is the section you'd actually act on — put the most important thing first.
4. **Wins worth calling out** — 1-3 things worth a "nice work" mention, if there are any. Skip this section rather than force it if nothing stands out.

## Rules

- Group by person, not by project — the point is knowing what each team member is carrying.
- If someone's update is missing or thin, say "no update received" for them rather than skipping them silently — that's useful signal on its own (are they overloaded, did they forget, is something wrong).
- Don't editorialize on performance ("Sara is really struggling") — just state what's in the notes factually and let me draw conclusions.
- Keep the whole digest short enough to read in under 3 minutes — this is a Friday-afternoon read, not a report.
- If the same blocker shows up from two different people, call that out explicitly in Cross-team Flags — that's usually the most important thing in the whole digest.

## Example

**Input (raw notes):** "sara: finished the checkout flow, waiting on client feedback on homepage still. mike: closed 2 deals this week, one client asking about pricing for add on services. josh: no update sent. team mentioned twice that the Acme client hasn't responded in over a week"

**Output (excerpt):**

> **Pulse:** Solid week — delivery on track, one client responsiveness issue worth watching.
>
> **Sara** — Finished the checkout flow. Blocked: still waiting on client feedback on the homepage draft.
> **Mike** — Closed 2 deals this week. One existing client asking about pricing for add-on services — may be worth a quick call.
> **Josh** — No update received.
>
> **Cross-team flags:**
> - Acme client hasn't responded in over a week — flagged by two people, likely blocking more than one project. Worth a direct check-in call rather than another email.
>
> **Wins:** Mike closed 2 deals this week.

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want this digest built automatically every Friday from your team's actual activity, with no copy-pasting? See Agency Control Tower: controltower.collabai.software*
