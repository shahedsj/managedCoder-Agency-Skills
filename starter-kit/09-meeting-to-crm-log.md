# Meeting-to-CRM Log Skill

## What this does

Takes a call you just had — pulled live from Zoom/your meeting tool, or just pasted in as notes — and turns it into a properly logged CRM update: classifies what kind of meeting it was, finds the matching deal or client, writes structured notes to it, updates the "next step" field, and proposes follow-up tasks. No more meetings that happened but never made it into the CRM.

## When to use it

- Right after any client, prospect, or partner call
- When a meeting happened somewhere your CRM didn't automatically capture it (personal Zoom room, phone call, in-person meeting, Otter/other transcription tool)
- Any time you realize "I don't think I ever logged that call with [client]"

## Setup

Uses whatever CRM connector you have set up in Claude (HubSpot, Pipedrive, GoHighLevel, Close, etc.) to search for the matching deal/client and write the log. If you also have a meeting tool connector (Zoom, Google Meet, etc.), the AI can pull the transcript/summary directly instead of you pasting it.

No connector? Paste the transcript, notes, or a rough summary instead — it still works, you'll just do the CRM update manually afterward using what the AI drafts.

## Instructions for the AI

You are processing a just-finished (or recently-had) meeting and logging it properly.

1. **Get the meeting content.** If a meeting-tool connector is available and the owner just says "process my last meeting" with nothing pasted, pull the most recent meeting with a summary/transcript through that connector. If they paste a transcript, notes, or summary instead, use that — don't ask for more unless the other person's name is genuinely unclear.

2. **Classify the meeting type**, stated in one sentence:
   - New deal (first intro, discovery, new opportunity, scoping)
   - Existing client (project update, issue, scope change, ongoing delivery)
   - Advisory / no direct service relationship
   - Internal (team only, no external party)
   - Partnership (co-build, referral, non-client collaboration)

3. **Find the matching record.** If a CRM connector is available, search it for a deal or contact matching the name/company mentioned. Present the match: "I found: [Deal/Contact name] — [stage] — is this right?" If multiple candidates, list them and ask. If none found, ask who this was with. Wait for confirmation before writing anything.

4. **Log structured notes** to the matched deal/contact, in this format:
   ```
   MEETING NOTES — [date] | [duration if known]
   Attendees: [names and roles]

   CONTEXT: [1-2 sentences]

   KEY DISCUSSION:
   - [point]
   - [point]

   ACTION ITEMS — YOU:
   1. [action]

   ACTION ITEMS — THEM:
   1. [action]

   NEXT STEP: [single clearest next action]
   ```

5. **Update the deal's "next step" field** (if your CRM has one) to match the NEXT STEP line above, through the connector.

6. **Propose action items as tasks** — don't create anything without asking. Ask: "I see [N] action items. Want me to create tasks for these, just note the next step, or both?" Then execute only what's confirmed, through whatever task/PM connector is available.

7. **Confirm what was actually written** at the end — which deal/contact was updated, what got logged, and any tasks created — don't just describe it, report what happened.

## Worked example

**Pasted notes:** "Had a call with Priya at Nova Retail. They want a redesign of their checkout flow, budget looks like $15k, she's deciding between us and one other agency by end of month. I need to send a proposal by Friday."

**Output:**
```
Classified as: New Deal (first scoping conversation)

I found a matching deal: "Nova Retail — Checkout Redesign" — Stage: Discovery. Is this right?

[after confirmation]

Logged to deal:
MEETING NOTES — Aug 11
Attendees: Priya (Nova Retail)
CONTEXT: Scoping call for a checkout flow redesign.
KEY DISCUSSION:
- Budget signal: ~$15k
- Competing against one other agency
- Decision expected by end of month
ACTION ITEMS — YOU: 1. Send proposal by Friday
NEXT STEP: Send proposal by Friday

Next step field updated to: "Send proposal by Friday."

I see 1 action item. Want me to create a task for the proposal, or just leave the next step as-is?
```

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want every call logged automatically, with zero manual triggering? See Agency Control Tower: controltower.collabai.software*
