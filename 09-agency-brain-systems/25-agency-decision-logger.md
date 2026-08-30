---
name: agency-decision-logger
description: Capture an agency decision with its context, options, rationale, owner, effective date, review trigger, and source so the company can understand later what was decided and why. Use after leadership decisions, pricing or scope decisions, architecture choices, policy changes, client exceptions, product decisions, or whenever the same question keeps getting reopened because the original decision was never recorded.
---

# Agency Decision Logger

A decision log is not a diary. Record enough context to prevent the same debate from restarting without turning the entry into a transcript.

## Inputs

Accept a decision from a meeting, message, document, or direct user statement.

Minimum required:

- what was decided
- who/which role owns the decision
- source or context

Helpful:

- options considered
- rationale
- effective date
- review trigger/date
- affected client/project/process/product

If the user has not actually decided yet, do not log a final decision. Produce a `DECISION NEEDED` object instead.

## Step 1 - Confirm decision state

Classify:

- **DECIDED** - explicit choice made
- **PROVISIONAL** - choice made for now with known review condition
- **DECISION NEEDED** - options discussed but no final choice
- **SUPERSEDED** - new choice replaces an older decision

Do not infer `DECIDED` from strong preference language alone.

## Step 2 - Search prior decisions when connected

Search Agency Brain by topic and affected entity.

If a related decision exists:

- link to it when this decision is separate
- update it when only details changed
- supersede it when the new decision replaces it
- flag conflict when both appear active but disagree

Never delete decision history simply because the answer changed.

## Step 3 - Capture the decision object

```yaml
object_type: decision
title: short decision title
state: decided | provisional | decision_needed | superseded
decision: one-sentence outcome
rationale: why this option was chosen
options_considered:
  - option: A
    reason_not_chosen: ...
owner_role: role accountable for applying/reviewing the decision
effective_date: YYYY-MM-DD or unknown
review_trigger: date, metric, event, or none
affected_entities: [client/project/process/product/function]
source_type: meeting | email | document | direct
source_date: YYYY-MM-DD
source_reference: link/id/title when available
supersedes: prior decision or none
confidence: high | medium | low
human_review: required | approved
```

Do not invent rejected options. If they were not discussed, omit them.

## Step 4 - Add an implementation check

A decision without an implementation path often exists only in the log.

Ask:

- Which system/process/document should reflect this decision?
- Does it create tasks?
- Does it change a policy/SOP?
- Does a client/team need communication?
- Does an older knowledge object need superseding?

Show these as proposed follow-ups, not automatic writes.

## Output

```markdown
# Decision Record - [Title]
**State:** DECIDED / PROVISIONAL / DECISION NEEDED
**Decision:** [one sentence]
**Owner role:** [role]
**Effective:** [date]
**Review trigger:** [event/date/none]

## Why
[2-5 concise bullets of evidence/rationale]

## Alternatives considered
- [only real alternatives]

## Affected
- [client/project/process/product]

## Source
[source + date]

## Knowledge check
NEW / UPDATES / SUPERSEDES / CONFLICTS with [existing decision]

## Implementation follow-up
- [proposed task/system/process change]
```

Then ask for approval before saving or updating the knowledge system.

## Rules

**Record rationale, not just outcome.** Future teams need to know why the choice made sense with the evidence available then.

**Keep decision and task separate.** `Use vendor A` is a decision. `Migrate account by Friday` is a task.

**Use review triggers for reversible decisions.** Examples: after 3 client pilots, when monthly cost exceeds a threshold, at renewal, or on a specific date.

**Do not rewrite history.** Supersede old decisions; preserve them as evidence of how the company evolved.

**Do not hardcode current company facts in this skill.** Retrieve them from authoritative systems when needed.

**Require approval before write.** Connected mode may propose creating/updating/superseding knowledge and creating follow-up tasks, but it must preview those actions first.

## What good looks like

Six months later, a new manager can understand what was decided, why, what it affected, and what would cause the company to revisit it.