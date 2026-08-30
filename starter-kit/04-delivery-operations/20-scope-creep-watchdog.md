---
name: scope-creep-watchdog
description: Compare new client requests and delivered work against the agreed SOW, proposal, backlog, or approved change requests to identify scope creep before margin or trust is damaged. Use during project reviews, after client meetings, before accepting new requests, when a team says a request is small, or whenever an agency owner wants to know what is in scope, ambiguous, or needs a change request.
---

# Scope Creep Watchdog

A request does not become in scope because it sounds small.

Compare what was agreed with what is now being requested or delivered. Separate genuine clarification from added work, and surface the commercial decision before the team quietly absorbs it.

## Inputs

Minimum useful input:

- original scope, proposal, SOW, estimate, or agreed deliverables
- new request, meeting notes, ticket, email, or work item

Helpful additional input:

- assumptions and exclusions
- approved change requests
- estimates or actual hours
- timeline/milestones
- client communication history

Connected mode may use `~~docs`, `~~project tracker`, `~~meeting notes`, `~~email`, `~~CRM`, `~~time tracking`, and Agency Brain.

## Step 1 - Establish the scope baseline

Use the most authoritative approved source available, in this order:

1. signed SOW/change order
2. approved proposal or contract exhibit
3. explicitly approved project plan/backlog
4. written client confirmation
5. meeting notes
6. internal assumption

If sources conflict, do not choose silently. State the conflict and use the highest-authority approved source as the working baseline.

## Step 2 - Break the new request into atomic changes

Do not classify a long request as one item. Split it into the smallest meaningful deliverables, behaviors, integrations, revisions, environments, content, reports, or support obligations.

For each item, capture the client's exact requested outcome, not the team's interpretation of how to build it.

## Step 3 - Classify each item

| Classification | Test |
|---|---|
| **IN SCOPE** | Clearly included in approved deliverables or acceptance criteria |
| **CLARIFICATION** | Changes detail but not meaningful effort, deliverable, dependency, or acceptance criteria |
| **AMBIGUOUS** | Scope language could reasonably support either interpretation |
| **CHANGE REQUEST** | Adds deliverable, integration, environment, workflow, revision cycle, support obligation, data work, or material effort not approved |
| **OUT OF SCOPE / NOT NOW** | Explicitly excluded or incompatible with the current phase |

Do not use `CLARIFICATION` as a way to avoid a commercial conversation.

## Step 4 - Apply creep signals

Increase concern when any apply:

- the request adds a new integration or external system
- it adds a new user role, workflow, report, environment, platform, or device target
- it changes approved acceptance criteria
- it creates another revision round after the agreed limit
- it requires migration, cleanup, or manual data work not included originally
- it adds ongoing support, monitoring, content, or operations
- it has already been partially delivered without approval
- the client has made 3+ individually small additions in the current phase
- the team describes it as `quick`, `small`, `while we are here`, or `should only take` without an estimate

Three small extras can be one large margin leak. Review cumulative impact, not only each request in isolation.

## Step 5 - Estimate impact without inventing numbers

When estimates exist, show:

- added hours/cost
- timeline impact
- dependency impact
- effect on current milestone

When estimates do not exist, use `UNKNOWN - ESTIMATE REQUIRED`.

Never invent hours to make the report feel complete.

## Step 6 - Recommend the commercial path

Choose one:

- Accept within current scope
- Clarify in writing, no commercial change
- Estimate before committing
- Create change request/change order
- Swap against another scoped item
- Move to later phase/backlog
- Decline

If the agency chooses to absorb extra work for relationship reasons, label it explicitly as a **commercial exception**. Record the estimated value/cost when known. Free work should be a decision, not an accident.

## Output

```markdown
# Scope Review - [Project / Request]

## Baseline
**Authoritative source:** [document/date]
**Relevant scope language:** [short paraphrase]

## Classification
| Requested item | Classification | Evidence | Impact | Recommended path |
|---|---|---|---|---|
| ... | CHANGE REQUEST | ... | estimate required | estimate before committing |

## Cumulative creep
[Count/value/hours of unapproved additions when evidence exists]

## Decision needed
**Decision owner role:** [PM / account owner / agency owner / other]
**Decision:** [specific yes/no/tradeoff]
**Needed by:** [date or NO DATE SET]

## Client wording draft
[Only when requested: neutral wording that explains the boundary and proposed next step.]

## Data gaps
- [missing estimate, missing signed scope, etc.]
```

## Rules

**Never call something out of scope without showing the baseline evidence.**

**Never treat discussion as approval.** A meeting idea is not an approved change unless the agency's process says it is.

**Never create a change request automatically.** Prepare the classification and draft. Wait for approval before writing to CRM/project/finance systems or sending client communication.

**Protect trust as well as margin.** The goal is not to say no. The goal is to make tradeoffs visible before the client and agency remember different agreements.

**Use Agency Brain when available.** Check prior scope decisions, exceptions, and client-specific agreements. Do not hardcode changing client facts inside this skill.

## What good looks like

The team can answer: `Is this included? If not, what exactly changes in cost, time, or priority before we say yes?`