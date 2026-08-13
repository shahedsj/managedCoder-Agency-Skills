---
name: meeting-to-crm-log
description: Turn a call you just had into a properly logged CRM record — classified, matched to the right deal or client, written up in a structured note, next step updated, follow-up tasks proposed. Use whenever the user says "process my last meeting", "log this call", "log this meeting", "update the CRM from my call", "I had a meeting with [name]", "here's my notes from the call", "next steps for [client]", or "I don't think I ever logged that call". ALSO trigger the moment they paste a transcript, meeting summary, voice-note dump, or rough bullets from a call — pasted meeting content is itself the trigger, even with no instruction attached. ALSO trigger when they're working a deal and mention a conversation that isn't in the CRM yet.
---

# Meeting to CRM Log

The meeting happened. The decision was made. Three weeks later nobody can find where it was written down, and the deal moves forward on someone's memory of it. This is the ten minutes after a call that decides whether the call counts.

> Tool placeholders like `~~CRM` mean whatever tool you've connected in that category. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ Paste a transcript, notes, or a voice-note dump            │
│  ✓ Classify, structure, draft the note and the next step      │
│  ✓ You paste the finished note into your CRM yourself         │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~meeting notes: pull the transcript, no pasting           │
│  + ~~CRM: find the record, write the note, set the next step  │
│  + ~~project tracker: create the follow-up tasks              │
└──────────────────────────────────────────────────────────────┘
```

## What I need from you

**Option A — Connected meeting tool.** Say "process my last meeting." I pull it.

**Option B — Paste it.** Transcript, bullet notes, a voice-note summary, or a mix. Messy is fine.

**Option C — From memory.** Tell me who it was with and what was said. Same output, shorter.

## Step 0 — Pick the path (decide, don't ask)

| Signal | Path |
|---|---|
| "Process my last meeting" and nothing pasted | **Path A** — pull from `~~meeting notes` |
| Any transcript, notes, or summary pasted | **Path B** — use what's in front of you |
| Call happened somewhere the tool doesn't record — phone, in person, personal meeting room, a third-party recorder | **Path B** |
| It's in the meeting tool but the CRM never picked it up | **Path A**, then log it manually anyway |

**Path A:** pull meetings from the last 7 days, take the most recent one that has a summary or transcript and hasn't already been processed this session. Read the summary *and* the transcript before doing anything else.

**Path B:** parse who it was with (name, company, role), the approximate date, the topics, the decisions, and the commitments. Ask only if the other person's name is genuinely unreadable.

Either way: **never ask a question the transcript already answers.** The owner just sat through the meeting. Asking them to re-tell it is worse than not logging it.

## Step 1 — Check the transcript is trustworthy

Before you believe a word of it, read it for damage. Auto-transcription breaks on noisy rooms, crosstalk, accents it wasn't trained on, and code-switching between languages mid-sentence — which is normal in most agencies and normal on most client calls.

Signs it's garbled: names that change spelling line to line, numbers that make no sense in context ("$50" where a budget should be), sentences that parse as words but not as meaning, whole passages attributed to one speaker.

If you see that, say so plainly before continuing:

> "This transcript looks partly garbled — I read the budget as ~$15k and the contact as 'Priya', but the audio quality is low. Confirm those two before I log anything."

Do not quietly clean it up and log your best guess. A confidently wrong meeting note is worse than no note, because everyone downstream treats it as the record of what happened.

## Step 2 — Classify the meeting, in one sentence

| Type | Signals that distinguish it |
|---|---|
| **New deal** | First introduction, discovery, a new opportunity, NDA, scoping something not yet sold |
| **Existing client** | Project update, a bug or complaint, scope change, anything about work already in flight |
| **Advisory** | Coaching, mentoring, pro bono, a favour — no service being sold on either side |
| **Internal** | Your own team only, no external party in the room |
| **Partnership** | Co-build, referral, reseller, or collaboration where neither side is the client |

State it in one line: *"Classified as: existing client — scope change conversation."* Flag it if the content came in manually, so whoever reads the record later knows it wasn't auto-captured.

The classification drives everything after it. An advisory call logged as a new deal pollutes the pipeline with a deal that will never close; an existing-client escalation logged as internal never reaches the account record where the next person needs it.

## Step 3 — Match and confirm before writing anything

Search `~~CRM` for a deal, client, contact, and project matching the name or company. Search all of them at once — the same conversation lives in different places depending on the meeting type.

Then present the candidate and stop:

> "I found: **Nova Retail — Checkout Redesign** — Stage: Proposal | Client: Nova Retail | Project: none. Is this the right record?"

- **Multiple candidates** → list them with enough detail to tell them apart (stage, value, last activity) and ask which one.
- **No match** → ask who the meeting was with. Do not create a new record on your own.
- **Nothing until confirmed** → write nothing to any system before an explicit yes.

Why this rule is absolute: a meeting note on the wrong deal is nearly invisible. Nobody goes looking for it, so nobody finds it and moves it. It sits there making one record wrong and one record empty, and the mistake surfaces at renewal.

## Step 4 — Write the note

Use this format exactly. The value is that it's the same shape every time — anyone can scan six months of these in a minute and find the decision.

```
MEETING NOTES — [date] | [duration] | [Manual input — if not auto-captured]
Attendees: [name — role — company, for each]

CONTEXT:
[1-2 sentences on why this meeting happened]

KEY DISCUSSION:
- [point]
- [point]
- [point]

ACTION ITEMS — YOU:
1. [what you committed to, with the date you said]

ACTION ITEMS — THEM:
1. [what they committed to, with the date they said]

NEXT STEP: [the single clearest next action, with a date]
```

Splitting your commitments from theirs is the part people skip and the part that pays. A single mixed list of "action items" is how an agency ends up chasing itself for work the client owes.

## Step 5 — Verify the write actually landed

If your `~~CRM` or `~~meeting notes` system stores the meeting record and its attachments or links as separate objects — most do — a write can succeed on one and silently fail on the other. The note saves, the link to the deal doesn't, and the meeting is invisible on the record that matters.

So: after writing, **read it back**. Re-fetch the record you just wrote to and confirm the note is on it. Never report "logged" because a write returned without an error. If the read-back doesn't show it, say so and log the note in the place that did work, rather than claiming a success you didn't verify.

## Step 6 — Update the next-step field

Set the deal's next-step field to match the NEXT STEP line in the note, word for word, and set the follow-up date to the date named in it.

Keeping these in sync matters because they're read by different people at different times. The note gets read when someone opens the deal; the next-step field gets read in every pipeline review. If they disagree, the pipeline review is running on stale information.

## Step 7 — Propose tasks, never auto-create

Count the action items and ask, in these words:

> **"I see [N] action items. Want me to create tasks for these, just note the next step, or both?"**

Then do only what was picked. Auto-created tasks are the fastest way to make someone stop trusting a tool — they log one call, find nine new tasks assigned to them, and never run it again. Offering the choice keeps the task list something the owner chose.

## Step 8 — Report what was actually written

```
LOGGED — [meeting name/date]
Record: [deal/client/project name] — [stage]
Note: added to [where], verified on the record ✓
Next step: "[text]" — due [date]
Tasks created: [n] — [title, owner, due date for each] / or "none — you said next step only"
Not done: [anything that failed or you skipped, and why]
```

Report the outcome, not the intent. "I'll log this to the deal" and "logged to the deal, confirmed on the record" are different claims, and only one of them is safe to build a Monday on.

## Worked example

**Pasted input:**

`"ok so call with priya nova retail — checkout redesign. she said budget is around 15k maybe [inaudible] they're talking to one other agency, decision end of month. i said i'd get the proposal over by friday. also she asked can we do the blog migration too, i said probably, didnt quote it. oh and their dev guy raj is out till the 20th"`

**Output:**

```
Transcript check: one [inaudible] near the budget figure. I've read it as ~$15k —
confirm before I log that number.

Classified as: New deal — scoping conversation on an active opportunity.
Manual input, not auto-captured.

I found: Nova Retail — Checkout Redesign | Stage: Discovery | Client: Nova Retail
Is this the right record?

[after confirmation]

MEETING NOTES — Aug 11 | 30 min | Manual input
Attendees: Priya — Nova Retail | Raj (mentioned, not present) — dev, Nova Retail

CONTEXT:
Scoping call on the checkout redesign. Competitive — decision due end of month.

KEY DISCUSSION:
- Budget signalled at ~$15,000
- Competing against one other agency; decision by end of August
- Asked about a blog migration on top of the checkout work — not quoted
- Their developer Raj is unavailable until Aug 20

ACTION ITEMS — YOU:
1. Send the checkout redesign proposal by Fri Aug 15

ACTION ITEMS — THEM:
1. Decide between the two agencies by Aug 31

NEXT STEP: Send proposal by Fri Aug 15

⚠️ Before this gets logged:
- Blog migration was asked for and you said "probably" with no price. That's an
  unquoted second scope. Quote it in the proposal as a separate line or say it's
  out of scope — the third time it comes up it'll be assumed included.
- Raj is out until Aug 20. If the build needs him, the start date you put in the
  proposal is already wrong.

Note written to the deal, read back and confirmed on the record ✓
Next step field set to: "Send proposal by Fri Aug 15" — due Aug 15

I see 2 action items. Want me to create tasks for these, just note the next step,
or both?
```

## Tips

1. **Log it before you do the follow-up work, not after.** Once you start writing the proposal, the call is gone. The ten minutes right after are the only time you remember the tone as well as the facts.
2. **The thing you don't want to write down is the thing to write down.** The vague "we'll figure that out later", the price you dodged, the date you agreed to without checking — those are the lines that become disputes. A logged ambiguity is a negotiation. An unlogged one is a loss.
3. **Log the calls that went nowhere too.** A record showing four conversations and no movement is what finally lets you close a dead deal without guilt. Only logging good meetings makes the pipeline look healthy right up until it doesn't.
4. **A next step without a date isn't a next step.** "Follow up with Priya" will still be sitting there in November. "Send proposal by Fri Aug 15" either happens or visibly doesn't.
5. **Don't trust a clean-looking transcript any more than a messy one.** Transcription is most dangerous when it's fluent and wrong — a garbled line makes you check; a smooth sentence with the wrong number doesn't.

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want every call classified, matched, logged, and turned into next steps the moment it ends, with no one triggering it? See Agency Control Tower: controltower.collabai.software*
