---
name: meeting-notes-to-tasks
description: Turn a meeting transcript or rough notes into owned, dated action items while separating real commitments from decisions, open questions, and context. Use after client calls, standups, leadership meetings, or internal reviews when the user asks for action items, what was agreed, or wants approved meeting commitments created in a project tracker without duplicates.
---

# Meeting Notes to Tasks

Everything in a meeting sounds actionable while people are talking. This skill separates what was actually committed from what was merely discussed, then creates only approved, non-duplicate tasks.

> Tool placeholders such as `~~meeting notes` and `~~project tracker` mean whatever connected system provides that category. See [CONNECTORS.md](CONNECTORS.md).

## Modes

```text
STANDALONE
Paste a transcript, summary, rough notes, or dictated recap.

CONNECTED
Retrieve the meeting, resolve project/client context, check existing tasks, and write approved tasks back.
```

## Step 0 - Resolve the meeting with minimum questions

If the user provides a transcript, notes, meeting URL, title, or clear date, proceed.

For vague requests such as `my last call`, search in this order:

1. exact meeting name if known
2. most recent meeting in last 7 days
3. most recent meeting in last 14 days
4. attendee name when supported
5. client/project name in last 30 days

If several meetings plausibly match, list them with date/title and ask which one. Never choose a meeting just to avoid one question.

## Step 1 - Classify the meeting output

Use four buckets:

| Bucket | Test | Destination |
|---|---|---|
| **Commitment** | A person accepted a specific action | Candidate task |
| **Decision** | A choice was actually settled | Decision section; optionally Agency Brain |
| **Open question** | Discussed but unresolved | Open questions, not task unless someone explicitly owns resolving it |
| **Context** | Background/opinion with no durable action | Summary only or omit |

A thing that should happen is not automatically a commitment.

## Step 2 - Normalize candidate tasks without inventing fields

For every commitment capture:

- task: concrete action/outcome
- owner: person named in source, otherwise `UNASSIGNED`
- due: explicit date, otherwise `NO DATE SET`
- side: our team / client / partner
- project/deal/client: only when evidence supports the link
- priority: only when source or connected business rules support it
- source: meeting title/date/reference
- notes: what it blocks or why it matters

Never invent an owner or deadline.

## Step 3 - Check context and duplicates in connected mode

Before proposing creation:

1. Resolve the relevant active project/deal/client from the meeting evidence.
2. Search open tasks for the same project/deal and normalized action keywords.
3. Check recent source metadata when the tracker supports source IDs.

Classify each candidate:

- **NEW** - no existing task covers it
- **UPDATE EXISTING** - an open task already represents the action; propose a comment/date/owner update instead
- **DUPLICATE** - same action already tracked with no meaningful new information; do not create
- **AMBIGUOUS** - project, owner, or action cannot be resolved safely

A new meeting mention is not a reason to create a second task for the same work.

## Step 4 - Show the meeting result

```markdown
## Summary
[3-5 sentences: what mattered, what changed, what was decided]

## Decisions made
- [settled decision]

## Action items - our team
| Task | Owner | Due | Tracking | Notes |
|---|---|---|---|---|
| [action] | [name/UNASSIGNED] | [date/NO DATE SET] | NEW / UPDATE EXISTING / DUPLICATE | [context] |

## Action items - client/partner
| Task | Owner | Due | Notes |
|---|---|---|---|
| [action] | CLIENT/PARTNER - [name] | [date/NO DATE SET] | [what it blocks] |

## Open questions
- [unresolved item] - decision needed from [role/name if stated]

## Ambiguities
- [anything the source does not support confidently]
```

Keep client/partner commitments separate. They may block delivery, but they are not automatically tasks to assign to the agency team.

## Step 5 - Approval gate before writes

Never create or update tasks automatically.

First say:

`I found [N] internal commitments: [X] new, [Y] updates to existing tasks, [Z] duplicates. Want me to prepare the tracker changes?`

If yes, show an exact preview:

| # | Action | Change | Assignee | Due | Priority | Project/Deal | Source |
|---|---|---|---|---|---|---|---|

Then wait for explicit approval before writing.

For bulk changes, approval must cover the exact list being changed.

## Step 6 - Write and report what actually happened

After approval:

- create only approved NEW tasks
- update only approved existing tasks
- preserve meeting/source reference when the tracker supports it
- use tracker-returned IDs/links; never invent URLs or slugs
- report successes and failures separately
- do not claim a task was created when the write failed

## Rules that make this reliable

**Only explicit commitments become candidate tasks.** Do not create logical follow-on work nobody accepted.

**UNASSIGNED beats a guessed owner.** The missing owner is management information.

**NO DATE SET beats a fake deadline.** The missing date is management information.

**Decisions are not tasks.** `Use Postgres` is a decision. `Migrate the schema Friday` is a task.

**Open questions are not facts.** If the group disagreed, record the disagreement instead of smoothing it into a conclusion.

**Preserve source provenance.** Important tasks should be traceable to the meeting that created or changed the commitment.

**Resolve before writing.** Never force a prospect action into an unrelated delivery project or attach a task to a client because the name sounds similar.

**Do not send client reminders automatically.** Draft the reminder if requested and wait for approval.

**Use Agency Brain when available.** Decisions or durable process changes may also be candidates for `meeting-to-knowledge-capture`; do not stuff durable knowledge into task descriptions.

## Worked example

Input:

`Sara said she'll send final copy Wednesday. Mike will research hosting pricing. We still need to decide the hosting provider. Client will review the design Friday. Someone should probably update the SOW.`

Output logic:

- Sara: commitment, Wednesday
- Mike: commitment, no date stated
- Hosting provider: open decision, not a task unless someone owns the decision process
- Client design review: client commitment, separate table
- Update SOW: not a commitment because nobody accepted it; open question

That distinction is the skill.