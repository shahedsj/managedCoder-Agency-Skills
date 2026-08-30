---
name: meeting-to-knowledge-capture
description: Turn agency meeting notes or transcripts into structured, reviewable company knowledge instead of leaving important decisions and context trapped in a transcript. Use after client, leadership, delivery, sales, or internal meetings when the user wants to capture decisions, commitments, risks, process changes, client context, or reusable lessons into an Agency Second Brain or knowledge base.
---

# Meeting to Knowledge Capture

Meeting notes are history. Company knowledge is the small part of that history that should still matter after the transcript is forgotten.

Extract durable knowledge without turning every sentence into memory.

## Core rule

Do not write directly to a knowledge system on first pass.

Required flow:

```text
READ SOURCE
  -> EXTRACT CANDIDATES
  -> CLASSIFY
  -> CHECK EXISTING KNOWLEDGE WHEN AVAILABLE
  -> SHOW REVIEW PREVIEW
  -> HUMAN APPROVAL
  -> WRITE / UPDATE / SUPERSEDE
```

## Inputs

Standalone: transcript, notes, summary, or rough bullets.

Connected: `~~meeting notes`, `~~docs`, `~~CRM`, `~~project tracker`, and Agency Brain.

When the meeting source is vague, search by title/date/attendee/client. If several meetings match, ask which one rather than guessing.

## Step 1 - Separate meeting output from durable knowledge

Classify content into these buckets:

| Bucket | Keep as knowledge? | Test |
|---|---|---|
| **Decision** | Yes | A choice was made that should guide future work |
| **Commitment** | Usually task/system, not durable knowledge | A person agreed to do something by a date |
| **Policy / Rule** | Yes | A reusable operating rule was established or changed |
| **Process / SOP Change** | Yes | The way recurring work should be done changed |
| **Client / Project Context** | Sometimes | Context will materially improve future decisions or handoffs |
| **Preference / Constraint** | Sometimes | A stable business preference or constraint was explicitly stated |
| **Risk / Assumption** | Yes when material | Future work depends on it and it needs review |
| **Open Question** | No as fact | Unresolved; track as question/decision-needed |
| **Discussion / Opinion** | Usually no | Conversation without a settled outcome |
| **Small talk / repetition** | No | No future operating value |

Do not store an open question as a fact.

## Step 2 - Apply the durability test

A candidate belongs in Agency Brain when at least one is true:

- someone in a future meeting would need this context
- forgetting it would cause rework, inconsistency, or a repeated debate
- it changes how the agency should make a recurring decision
- it explains an important client/project constraint
- it should survive beyond the current task or sprint
- it is a lesson that should affect future similar work

If none apply, leave it in the meeting record.

## Step 3 - Create canonical knowledge candidates

Use this model-independent object shape:

```yaml
object_type: decision | policy | process | context | constraint | risk | lesson
title: short durable title
summary: concise statement of what future users need to know
source_type: meeting
source_date: YYYY-MM-DD
source_reference: meeting title/link/id if available
owner_role: role responsible for keeping this current
status: active | proposed | superseded | expired
confidence: high | medium | low
effective_date: YYYY-MM-DD or unknown
review_date: YYYY-MM-DD or none
tags: [client, project, function, topic]
related_entities: [client/project/deal/process/role]
supersedes: prior object id/title or none
human_review: required | approved
```

Do not hardcode a vendor-specific database schema into the public skill.

## Step 4 - Check for conflicts and duplicates

When Agency Brain or a knowledge base is connected, search for the same topic/entity before proposing a new object.

Classify the candidate:

- **NEW** - no equivalent knowledge exists
- **CONFIRMS** - meeting reinforces current knowledge; usually no new object needed
- **UPDATES** - same knowledge changed; propose updating the existing object
- **CONFLICTS** - source disagrees with current knowledge; require human resolution
- **SUPERSEDES** - a new decision/policy explicitly replaces the old one

Never silently overwrite a conflict.

## Step 5 - Keep tasks and knowledge separate

A commitment such as `Sara will send the draft Friday` belongs in task/project systems.

A durable rule such as `All client launch approvals require written acceptance before production deployment` belongs in Agency Brain.

The same meeting can produce both. Show them separately.

## Step 6 - Preview before writing

```markdown
# Meeting Knowledge Capture - [Meeting]

## Durable knowledge candidates
| # | Type | Candidate | Action | Confidence | Why keep it |
|---|---|---|---|---|---|
| 1 | Decision | ... | NEW / UPDATE / SUPERSEDE / CONFLICT | High | ... |

## Tasks / commitments - not knowledge
- [action] - [owner] - [date or NO DATE SET]

## Open questions - not facts
- [question] - decision needed from [role]

## Conflicts requiring review
- Existing: [current knowledge]
- New source says: [meeting evidence]
- Recommended handling: [resolve / supersede / keep both pending]

## Skip
- [items intentionally left only in meeting record]
```

Then ask which knowledge candidates to save/update. Do not write until approved.

## Step 7 - After approval

When connected:

- write only approved objects
- preserve source reference and source date
- mark replaced knowledge as superseded rather than deleting history when the system supports versioning
- record who approved the change when supported
- keep the meeting record as evidence
- report exactly what changed

## Rules

**Source provenance is mandatory.** A future user should be able to trace important knowledge back to evidence.

**Prefer update over duplicate.** Ten near-identical knowledge entries make retrieval worse, not better.

**Do not store sensitive personal details merely because they appeared in a meeting.** Keep only business-relevant knowledge appropriate for the agency's access rules.

**Do not turn opinions into policy.** `I think we should` is not a decision unless the meeting actually settles it.

**Do not freeze changing facts inside skill instructions.** Client status, team assignments, pricing, products, and project facts belong in authoritative systems/Agency Brain.

**Keep the architecture LLM-independent.** The knowledge object should remain useful whether the agency uses ChatGPT, Claude, Gemini, Codex, an MCP client, or another future model.

## What good looks like

A person who did not attend the meeting can later ask the Agency Brain why a decision was made, what rule changed, what context matters, and where that knowledge came from.