---
name: project-margin-leakage-review
description: Detect where an agency project is losing margin through excess hours, unpriced scope, rework, underbilling, poor utilization, or delivery inefficiency, then recommend a commercial or operational correction. Use for weekly finance/delivery reviews, project profitability checks, before renewals, when a fixed-fee project feels busy but unprofitable, or whenever an agency owner asks where margin is leaking.
---

# Project Margin Leakage Review

Revenue is not margin. A project can look healthy in the CRM while the agency quietly gives away the profit in extra work.

Find the leak, quantify it when evidence exists, and identify the decision that stops it.

## Inputs

Best case:

- contracted/project revenue
- planned hours or cost budget
- actual hours/cost to date
- percent complete or milestone progress
- invoices and collections
- approved change requests
- unapproved scope additions
- rework/bug/support time
- write-offs or non-billable time

Standalone mode can use pasted estimates, time reports, invoices, and scope notes.

Connected mode may use `~~finance`, `~~time tracking`, `~~project tracker`, `~~CRM`, `~~docs`, and Agency Brain.

## Step 1 - Establish the commercial baseline

Identify:

- pricing model: fixed fee / T&M / retainer / hybrid
- contracted revenue
- approved change-order revenue
- planned delivery cost or hours
- target margin if the agency has one

If target margin is unknown, do not invent an industry benchmark as if it were the agency's target. You may show the actual economics without declaring them good or bad.

## Step 2 - Calculate what can be calculated

When data exists:

```text
recognized_or_expected_revenue = contracted revenue + approved changes
actual_delivery_cost = labor cost + known direct project cost
projected_total_cost = actual cost / credible percent complete
projected_margin = (expected revenue - projected total cost) / expected revenue
hour_burn_ratio = actual hours / planned hours
progress_ratio = credible percent complete
```

If percent complete is unreliable, do not project total cost from it. Use milestone/burn evidence and label the projection unavailable.

## Step 3 - Classify leakage

Use one or more categories:

- **SCOPE LEAK** - work delivered without approved commercial change
- **ESTIMATE LEAK** - original estimate materially understated the work
- **REWORK LEAK** - defects, unclear requirements, or repeated revisions consume time
- **UTILIZATION LEAK** - expensive capacity is being used for work that could be handled differently
- **BILLING LEAK** - billable/approved work is not invoiced or invoicing lags delivery
- **COLLECTION LEAK** - revenue is invoiced but cash is materially late
- **PROCESS LEAK** - handoffs, meetings, approvals, or tooling create avoidable cost
- **STAFFING MIX LEAK** - delivery mix is more expensive than planned

## Step 4 - Apply starter warning thresholds

Flag for review when evidence shows:

- actual hours exceed planned hours by 10%+ while meaningful committed work remains
- burn percentage is 15+ points ahead of credible completion percentage
- unapproved additions have consumed repeated material effort
- rework/revision time is 10%+ of total delivery time
- approved work has not been invoiced by the agency's normal billing cycle
- a fixed-fee project has no remaining hours/cost buffer before acceptance is complete

These are starter signals, not universal finance policy. Replace them with the agency's documented thresholds when available.

## Step 5 - Identify the leak owner and correction

Do not assign blame. Assign the control point.

Examples:

- PM: enforce change-control before work starts
- account owner: reset client expectation
- technical lead: reduce rework/root-cause defects
- finance: invoice approved milestone/change
- owner: approve pricing/scope tradeoff

Choose a correction:

- change order
- scope swap
- reduce/sequence remaining scope
- staffing mix change
- estimate reset for future phase
- invoice now
- collection escalation
- process/root-cause fix
- intentional commercial exception

## Output

```markdown
# Project Margin Leakage Review - [Project]

## Economics
**Pricing model:** [type]
**Contracted + approved revenue:** [amount or unknown]
**Planned hours/cost:** [value or unknown]
**Actual hours/cost:** [value or unknown]
**Progress:** [credible measure]
**Projected margin:** [value or unavailable]
**Confidence:** High / Medium / Low

## Leakage found
| Leak | Evidence | Estimated impact | Control point |
|---|---|---|---|
| Scope leak | ... | $/hours/unknown | PM/account |

## Biggest leak
**[one category]** - [why it matters most]

## Correction
**Owner role:** [role]
**Action:** [specific]
**By:** [date or NO DATE SET]
**Expected effect:** [what improves]

## Commercial decision
[change order / absorb intentionally / scope swap / other]

## Data gaps
- [missing cost rates, percent complete, etc.]
```

## Rules

**Do not confuse collections with profitability.** Late cash and low margin are different problems.

**Do not invent labor cost from billing rate.** Use actual internal cost when available; otherwise report hours separately.

**Do not blame the team for approved strategic free work.** Label intentional exceptions distinctly from accidental leakage.

**Do not recommend a price increase as the only fix.** Some leaks are process, quality, staffing, or scope-control problems.

**Do not change invoices, scope, rates, or project plans automatically.** Preview the correction and wait for approval.

**Use Agency Brain when available.** Check pricing rules, approved exceptions, prior scope decisions, client agreements, and lessons learned. Keep changing financial facts in the finance/source systems, not inside this skill.

## What good looks like

The agency can point to the exact mechanism losing money and the control that prevents the same leak next month.