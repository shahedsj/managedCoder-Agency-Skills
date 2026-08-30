---
name: meeting-notes-to-tasks
description: Turn a meeting transcript or rough notes into owned, dated action items — separating real commitments from things that were only discussed. Use right after any client call, team standup, or internal meeting, whenever the user pastes a transcript or notes, or says "what were the action items", "pull the tasks out of this", "what did we agree", or "turn this into tasks". Also use when they're unsure what was actually decided in a meeting, or when a project keeps stalling because things said out loud never became tracked work.
---

# Meeting Notes to Tasks

Everything in a meeting sounds like a commitment while you're in the room. A day later nobody can tell what was agreed, what was floated, and who owns it. This separates the three.

> Tool placeholders like `~~project tracker` mean whatever tool you've connected in that category. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ Paste a transcript or scribbled notes                      │
│  ✓ Summary, action items with owners and dates                │
│  ✓ Open questions kept separate from tasks                    │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~meeting notes: pull the transcript directly              │
│  + ~~project tracker: create the tasks after you approve      │
│  + ~~chat: send each person their own items                   │
└──────────────────────────────────────────────────────────────┘
```

## What I need from you

**Option A — Connected.** "Pull the tasks from my last call." If the meeting can't be found from a vague reference, see Step 0 — ask, don't fail.

**Option B — Paste it.** Transcript, notes, or scribbles. Typos and fragments are fine.

**Option C — Talk it through.** "We agreed Sara sends copy Wednesday, and Mike is looking into hosting."

## Step 0 — Finding the meeting (connected mode only)

If they said "my last call" or "the last meeting I attended" and `~~meeting notes` returns nothing, **do not report failure.** Most `~~meeting notes` tools index by title and date — very few index by who attended — so the most natural phrasing a user will type is the one least likely to match.

Widen the search in this order, stopping at the first hit:

| Order | Search by | Range |
|---|---|---|
| 1 | Exact meeting name, if they gave one | any |
| 2 | Date — most recent meeting | last 7 days |
| 3 | Date — most recent meeting | last 14 days |
| 4 | Attendee name, if the tool supports it | last 14 days |
| 5 | Project or client name mentioned in the request | last 30 days |

Still nothing after 14 days of meetings? Ask **one** question and stop:

> "I can't find it from 'last meeting'. What was it called, or what day was it?"

One question costs five seconds. A dead end on the first run costs the user's trust in the whole skill — and asking for "my last call" is the first thing most people try.

If two or more meetings match, list them with date and title and ask which one. Picking the wrong meeting and confidently producing tasks from it is worse than asking.

## Step 1 — Sort everything into three buckets

This is the whole job. Most tools skip it and dump everything into a task list, which is why nobody trusts the output.

| Bucket | Test | Where it goes |
|---|---|---|
| **Commitment** | A named person said they would do a specific thing | Action items table |
| **Open question** | Discussed, not resolved, or two people disagreed | Open Questions section |
| **Context** | Background, opinion, discussion that led nowhere | Summary only, or dropped |

The test for a commitment is somebody saying they'd do it — "I'll send that Friday," "let me look into pricing." A thing that *should* happen but nobody claimed is not a commitment. It's an open question about who owns it, and putting it in the task list as a guess creates a task nobody accepted and nobody does.

## Step 2 — Produce the output

```markdown
## Summary
[3-5 sentences. What was discussed, what was decided. Skip small talk and tangents.]

## Decisions made
- [Thing that was actually settled, so it doesn't get reopened next week]

## Action items — our team
| Task | Owner | Due | Notes |
|---|---|---|---|
| [Specific action] | [Name] | [Date or NO DATE SET] | [Context] |

## Action items — client
| Task | Owner | Due | Notes |
|---|---|---|---|
| [Specific action] | CLIENT — [Name] | [Date or NO DATE SET] | [What it blocks] |

## Open questions
- [Unresolved thing] — needs a decision from [who], by [when]
```

## Step 3 — Propose creating the tasks

Never create them automatically. Ask:

> "That's [N] action items — [X] ours, [Y] theirs. Want me to create the [X] as tasks?"

Then create only what's confirmed, matching the owner and date exactly as they appear in the table. Report back what was actually created.

## The rules that make this work

**Only what was committed out loud.** Don't invent tasks that logically follow. A task list containing things nobody agreed to is worse than no list — the whole thing loses authority, and people start ignoring the real items too.

**UNASSIGNED, not a guess.** If a task was named but no owner was, write `UNASSIGNED` in the Owner column. Guessing an owner is how a task quietly belongs to nobody: the person you guessed never accepted it, so it sits there while everyone assumes it's handled.

**NO DATE SET, not an invented date.** A fake deadline is worse than no deadline. Real ones get planned around; invented ones get discovered as wrong at the worst moment, and they teach the team that dates in the tracker mean nothing.

**Client tasks get their own table.** This is the single most valuable line in the output. Client-side items are the most likely to be forgotten and the most likely to be blocking you — and when a project slips, "we were waiting on you, here's the dated list" is a very different conversation than "it's late."

**Separate Decisions from Actions.** A decision has no owner and no date, but it needs recording or it gets relitigated next week. "We're going with Postgres" isn't a task; it's the thing that stops the same debate happening twice.

**Open questions are not tasks.** If two people disagreed, or nothing was settled, it goes in Open Questions with who needs to decide and by when. Filing an unresolved argument as a task assigns the disagreement to one person, which is how it stays unresolved.

**Keep names as spoken.** "Sara," not "Ms. Patel." Formalising names makes the output feel like it came from outside the team, and people scan for the name they're used to seeing.

**Never fail silently on retrieval.** "I couldn't find that meeting" ends the conversation. "What was it called, or what day was it?" continues it. The user knows exactly which meeting they mean — they just used the one phrasing the tool can't match, and they have no way to know that.

**Flag ambiguity rather than smoothing it.** If a transcript is garbled or a commitment is unclear — "I think Mike said he'd handle it?" — say so and ask. Confidently wrong action items are the fastest way to lose trust in the whole system.

## Worked example

**Input:** `"talked about launch date, sara said she'll get final copy to us by wednesday, we still need to decide on hosting provider, mike is gonna look into pricing options and get back to us, client said they'll review the design friday, someone should probably update the SOW at some point"`

**Output:**

> ## Summary
> Discussed the upcoming launch. Copy delivery and the hosting decision are the two open items blocking progress; design is with the client for review.
>
> ## Decisions made
> - None finalised this meeting.
>
> ## Action items — our team
> | Task | Owner | Due | Notes |
> |---|---|---|---|
> | Send final copy | Sara | Wednesday | Confirm whether Sara is client-side or ours |
> | Research hosting pricing options | Mike | NO DATE SET | Feeds the hosting decision below |
>
> ## Action items — client
> | Task | Owner | Due | Notes |
> |---|---|---|---|
> | Review design draft | CLIENT | Friday | Blocks final polish |
>
> ## Open questions
> - Which hosting provider — not decided. Needs Mike's pricing first, then a call from [who?].
> - Updating the SOW was mentioned but nobody took it. Real task, or drop it?

> ⚠️ Two things to check:
> - "Someone should probably update the SOW" — no owner, no date, hedged language. I left it as an open question rather than inventing a task. If it matters, it needs a name.
> - Sara's side is unclear from the notes. If she's client-side, that row moves to the client table and changes who you chase.

## Tips

1. **Do this before you close the laptop.** Notes decay fast. Ten minutes after the call you remember what was agreed; the next morning you remember what you *think* was agreed.
2. **Send the client their own table.** Not the whole document — just their rows. It converts "you're blocking us" into a neutral list with dates, and it lands far better than it sounds.
3. **The item nobody claimed is the important one.** When something obviously needs doing and no one volunteered, that's the real signal in the meeting. Surface it as an open question rather than assigning it to whoever seems closest.
4. **If everything came out UNASSIGNED, the meeting failed.** That's worth saying plainly to the user. A meeting that produces no owners produced nothing, and the fix is a five-minute follow-up message, not a better task list.
5. **Watch for the recurring open question.** The same unresolved item appearing across three meetings isn't a scheduling problem — it's a decision someone is avoiding, and it needs escalating rather than re-listing.

---
*Free next step: join a live class and get the weekly AI-for-agencies newsletter at managedcoder.com*

*Part of the Agency Skill File Starter Kit — ManagedCoder. Want every meeting captured and turned into owned tasks automatically, with nothing to paste? See Agency Control Tower: controltower.collabai.software*
