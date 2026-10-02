---
name: partner-pipeline-follow-up
description: Review agency referral, delivery and co-selling partnerships, resolve the right partner identity, reconcile commitments and draft the next follow-up. Use for partner pipeline reviews, partnership meetings, missed introductions, joint opportunities or partner portal updates. Keep internal commercial notes separate from partner-visible content.
---

# Partner Pipeline & Follow-Up

A promising partnership becomes useful when both sides have a specific next commitment. This review exposes missing introductions, unclear ownership and commitments that never reached the tracker.

> Tool placeholders refer to your connected systems. See [CONNECTORS.md](../CONNECTORS.md).

## How it works

| Mode | What it does |
|---|---|
| Standalone | Review a pasted partner list, meeting notes and commitments. Draft a ranked action list and partner-safe recap. |
| Connected | Read partner records from ~~CRM, recent exchanges from ~~email, commitments from ~~meeting notes and execution from ~~project tracker. |

## What I need from you

Choose one:

1. A partner list plus recent notes for a portfolio review.
2. One partnership and its latest meeting or email exchange.
3. A proposed new partnership with source-backed contacts and purpose.

Required: review date/timezone, relationship owner, evidence of the latest commitments and the intended audience.

Useful: approved partner terms, ideal customer profile, services, agreement status, shared account rules, previous review and follow-up policy from ~~docs. Missing values remain unknown.

## Step 1: Resolve identity before creating anything

Read the current partner list when available. A cached roster is a lookup hint, not proof a partnership is absent.

| Situation | Identity to verify |
|---|---|
| Relationship survives a person's employer change | Individual partner; do not imply the employer is a party |
| Agreement and economics belong to a company | Company partner with separately verified contacts |
| Two service tracks under one agreement | One partnership with two tracks, unless authoritative records establish separate agreements |
| Similar names or ambiguous email domains | Hold creation and resolve the existing entity first |

Use stable returned IDs. Never guess a portal slug, contact address, job title or website from a company name. Do not upgrade “member of the team” into “team lead.”

## Step 2: Gather the actual commitments

Read the last substantive meeting and subsequent exchanges before summarizing the relationship. Capture:

- Partnership purpose in 2–4 sentences.
- Joint ideal customer profile and each side's contribution.
- Every agreed action, owner side, named owner if verified, stated due date and source.
- Existing opportunity references, account owner and introduction permission.
- Agreements and resources, with their actual status and audience.

Read the full meeting, including closing commitments. A meeting booking is not evidence that it happened. An email draft is not a sent follow-up. A typed signature block is not proof of an executed agreement.

Dates are commitments only when actually stated or agreed. Otherwise propose a next-action date and label it as proposed.

## Step 3: Diagnose the relationship

Use existing stages when provided. These portable labels are review labels, not automatic CRM stage changes:

| Label | Evidence |
|---|---|
| Exploring | Mutual interest but no confirmed joint action |
| Action agreed | At least one specific reciprocal commitment |
| Active opportunity | A verified shared opportunity with ownership and introduction permission |
| Delivery underway | Accepted work is actively being delivered |
| Dormant / hold | Explicit pause, or no recent evidence requiring review |
| Unknown | Missing or conflicting records prevent classification |

Do not count a shared opportunity twice across referral and sales reports. Report sourced and influenced pipeline separately. Never invent a commission, fee, probability or forecast value.

## Step 4: Rank the follow-ups

Apply agency policy when available. Otherwise disclose these starter thresholds:

| Signal | Points |
|---|---:|
| Confirmed partner commitment overdue | +5 |
| Introduction or client handoff explicitly blocked | +4 |
| Agreed next action due within 7 calendar days | +3 |
| No substantive exchange for 14 calendar days while action is open | +2 |
| Waiting on the agency owner's decision | +2 |
| Verified relevant reply or progress in the last 3 calendar days | -2 |

Add applicable signals once each. Break ties by client impact, then oldest agreed deadline. Missing dates do not earn overdue points.

Opt-outs, an explicit hold, disputed ownership or an unresolved confidentiality issue override scoring: HOLD, with reason. No activity for 30 days prompts a continue/pause/close discussion, never automatic deletion.

## Step 5: Separate the audiences

Produce two sections with explicit labels:

- Partner-visible: agreed purpose, approved resources, shared decisions and each side's commitments.
- Internal only: commercial strategy, unapproved economics, confidence, private notes, account conflicts and another partner's pursuits.

If visibility is unknown, keep the material internal pending review. Sharing one partnership's private account pursuit with another can damage both relationships.

Verify resource links before recommending publication. If links cannot be checked, label them unverified and omit them from the publish-ready section.

## Step 6: Draft actions and verify authorized writes

Propose exact record changes and the destination audience. Keep meeting records, opportunity changes, task creation, access changes and external messages as separate actions.

Respect existing explicit authorization for the same scope. Otherwise show the exact content before writes or sends. Use current supported tool schemas. Do not change application code, access policies or database structure during partner intake.

After authorized execution, re-read records and visibility. Report returned identifiers, verified links and partial failures. Retry only after checking whether the first attempt created a record.

## Output

```text
PARTNER REVIEW: [date/timezone]
Scope and evidence: [records, source dates, missing coverage]

| Partner | Identity | Relationship owner | Review stage | Score / HOLD | Next action | Stated due date | Evidence |
| ... |

Partner-visible draft for [partner]:
Purpose: [2–4 sentences]
Decisions: [verified shared decisions]
Our commitments: [action, owner, date or not agreed]
Partner commitments: [action, owner, date or not agreed]
Approved resources: [verified links]

Internal only:
- [Ownership conflict, economics requiring approval, missing evidence]

Proposed writes/sends:
- [Exact destination, record, audience, change]
Executed: [none / verified results]
```

## The rules that make this work

- Identity comes first because an employer and an individual are different contracting parties.
- Read both sides' commitments because a partnership is not just another lead list.
- Preserve original deadlines because silently resetting them hides the follow-up failure.
- Keep drafts separate from sent touches because unsent emails cannot establish contact history.
- Save reusable corrections to partner policy only when requested; do not silently persist confidential context.

## Worked example

Fictional input:

```text
review oct 2. referral advisor changed employers. same personal partnership.
we promised demo sept 28, not sent, advisor promised intro after demo no date.
CRM shows email today but it's a draft. another partner pursuing same account.
```

Output:

```text
PARTNER REVIEW: Oct 2 | supplied agency timezone
Identity: individual advisor; employer is not assumed to be a partner.
Stage: Action agreed. Score: 9 (+5 overdue demo, +4 blocked introduction).
Evidence: supplied notes; CRM draft is not a sent exchange.

Partner-visible draft:
Purpose: We are exploring referrals for agency delivery work. The agreed next
step is a demo from our side, followed by a potential introduction from yours.
Our commitment: send the demo; original due date Sep 28, now 4 days overdue.
Partner commitment: introduction after demo; date not agreed.
Resources: none verified for publication.

Internal only: another partner's pursuit creates an ownership question.
Confirm account coordination before proposing an introduction.
Proposed actions: verify demo link, confirm relationship/account owners,
and agree a recovery date. Keep the Sep 28 commitment in history.
Executed: none. No contact timestamp changed and no message sent.
```

## Tips

1. Review the agency's own missed promises before asking the partner for progress.
2. One verified introduction can matter more than ten exploratory meetings.
3. Keep an individual relationship portable when an employer changes.
4. A paused partnership needs a reason and review point, not weekly boilerplate.
5. A weekly review is a useful automation candidate, but this skill creates no schedule.

---
*Part of the ManagedCoder Agency Skills library. Turn partnership promises into visible, owned next steps.*
