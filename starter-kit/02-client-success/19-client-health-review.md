---
name: client-health-review
description: Review an agency client relationship and classify it green, yellow, or red using delivery, communication, commercial, scope, and relationship evidence. Use for weekly client-success reviews, renewal prep, escalation prevention, at-risk account reviews, portfolio health checks, or whenever an agency owner asks which clients need attention and why.
---

# Client Health Review

Do not confuse a project being busy with a client being healthy.

Evaluate whether the relationship is likely to remain stable, renew, expand, or deteriorate. Use evidence from both delivery and relationship signals.

## Inputs

Standalone: accept any mix of project status, meeting notes, emails, client feedback, invoices, scope changes, support issues, and account notes.

Connected: retrieve the same evidence from `~~project tracker`, `~~meeting notes`, `~~email`, `~~CRM`, `~~finance`, and Agency Brain.

Never require every source. Show lower confidence when important evidence is missing.

## Step 1 - Review five dimensions

Score each dimension from 0 to 2 risk points.

### Delivery
- 0: milestones on track; no material overdue commitments
- 1: minor slippage or one unresolved blocker
- 2: repeated missed commitments, red project, production issue, or no credible recovery plan

### Communication
- 0: regular two-way communication; decisions answered
- 1: response times slowing, meetings repeatedly moved, or updates mostly one-way
- 2: material silence, unresolved escalation, or agency has not proactively updated the client while work is at risk

### Commercial
- 0: invoices current and commercial expectations clear
- 1: payment delay, budget concern, or renewal uncertainty
- 2: materially overdue payment, disputed invoice, explicit budget pressure, cancellation language, or renewal at risk

### Scope
- 0: requests fit agreed scope
- 1: ambiguous additions or repeated small extras
- 2: meaningful unpriced work, repeated change requests without approval, or client expectations materially exceed the agreement

### Relationship
- 0: positive sponsor engagement and clear value
- 1: sponsor engagement weakened, value is not being discussed, or relationship depends on one fragile contact
- 2: explicit dissatisfaction, sponsor loss, competitive review, escalation, or trust issue

Total risk score: 0-10.

## Step 2 - Apply hard overrides

A hard override can make the account RED regardless of total score:

- client explicitly threatens cancellation or replacement
- major unresolved delivery failure with client impact
- material invoice dispute tied to dissatisfaction
- critical commitment is overdue and the client has already escalated
- renewal is imminent and there is no clear owner, plan, or value story

Make the account at least YELLOW when:

- no meaningful client contact for 14+ days on an active engagement
- a client dependency has blocked work for 7+ days with no documented follow-up
- two or more new requests are being delivered without scope confirmation
- a key stakeholder has gone silent after a proposal, renewal, or major decision request

These are default starter thresholds. If the agency has documented service-level or account-health thresholds, use those instead and state that you did.

## Step 3 - Set health

| Score | Health |
|---|---|
| 0-2 | GREEN |
| 3-5 | YELLOW |
| 6-10 | RED |

Hard overrides beat the score.

Do not use a precise score when the evidence is too thin. Say `INSUFFICIENT DATA` and list what would change the judgment.

## Step 4 - Identify the real cause

Choose one primary cause:

- Delivery risk
- Communication gap
- Commercial pressure
- Scope mismatch
- Relationship/sponsor risk
- Client dependency
- Internal ownership gap

Do not list every possible problem. The primary cause should explain what intervention is most likely to improve the account.

## Step 5 - Produce the review

For one client:

```markdown
# Client Health - [Client]
**Health:** GREEN / YELLOW / RED
**Risk score:** [x/10 or insufficient data]
**Confidence:** High / Medium / Low
**Primary cause:** [one]

## Evidence
- [fact] - source/date
- [fact] - source/date

## What changed
- [change since prior review, if available]

## Risk dimensions
| Dimension | Risk | Why |
|---|---:|---|
| Delivery | 0-2 | ... |
| Communication | 0-2 | ... |
| Commercial | 0-2 | ... |
| Scope | 0-2 | ... |
| Relationship | 0-2 | ... |

## Recommended intervention
**Owner role:** [account owner / PM / finance / agency owner / other role]
**Action:** [specific action]
**By:** [real deadline or NO DATE SET]
**Success signal:** [what would move health one level better]

## Client dependency
[what the client owes, if anything, and what it blocks]

## Owner attention
[Only include when owner involvement is actually needed. State the exact decision or relationship action.]
```

For a portfolio review, show RED first, then YELLOW, then GREEN. Keep GREEN accounts to one line each unless the user asks for detail.

## Rules

**Do not infer sentiment from silence alone.** Silence is a risk signal, not proof the client is unhappy.

**Do not blame the client for dependencies.** Record what is waiting, the follow-up history, and the impact neutrally.

**Do not hide agency-caused risk behind client dependencies.** If both sides contributed, say so.

**Do not mark an account green only because invoices are paid.** Commercial health is one dimension.

**Do not draft a client escalation from incomplete context.** If communication is needed, first check recent meetings/email when available.

**Do not send or update automatically.** Draft the intervention, CRM note, status update, or task. Show it first. Write only after approval.

**Use company knowledge when connected.** Compare against account promises, approved scope, communication cadence, renewal terms, and prior decisions from Agency Brain. Flag conflicts between live evidence and stored knowledge.

## What good looks like

The result should tell the agency which relationship needs attention before the client is forced to become the alerting system.