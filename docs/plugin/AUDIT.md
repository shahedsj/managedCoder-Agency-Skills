# Agency Skills audit

Reviewed all 32 numbered public catalog Skills against the approved six-workflow starter scope. Original source snapshot: main commit `2a34ee72e17dcc938a5805f0a1be8cbd30643562`. Review date: 2026-10-02.

The selected six are corrected and packaged with shared execution boundaries. The other 26 remain outside this release. This is not a declaration that the full catalog is validated.

Shared findings: operating Skills must not inject promotional footers; connector operations depend on actual tools and scopes; examples must be synthetic and evidence-complete; existing scoped authorization should be reused. Some catalog connector links rely on repository symlinks to the root guide. They can work in the repository but are not self-contained for an isolated Skill import. This package bundles a local guide beside every Skill.

No embedded credentials or database IDs were found in this review. Source 15 has an identifiable third-party contact anecdote and source 6 claims real-board statistics. Those sources are excluded. Source 11 cites third-party material; provenance and license obligations require verification before including it in a future package.

| # | Source | Finding / treatment |
|---|---|---|
| 06 | `01-owner-command/06-daily-task-triage.md` | Unverified real-board statistics, inconsistent scoring and invented example decisions. Audit provenance before distribution. |
| 10 | `01-owner-command/10-daily-owner-brief.md` | Timezone and accessible source boundaries need qualification. Synthetic example inputs should be complete. |
| 17 | `01-owner-command/17-meeting-to-product-roadmap.md` | Resolve project identity before writing. No findings is valid; do not manufacture roadmap issues. |
| 18 | `01-owner-command/18-weekly-owner-decision-brief.md` | Included with shared evidence, timezone, tool and authorization boundaries. |
| 26 | `01-owner-command/26-next-meeting-prep-brief.md` | Honor the literal next meeting unless the user chooses external preference; verify attendee/account identity. |
| 01 | `02-client-success/01-client-status-report.md` | Example invented dates, duration and outcomes. Rewritten for evidence and missing estimates. |
| 19 | `02-client-success/19-client-health-review.md` | Strong workflow. Add portfolio scope, date window and private-account boundaries before inclusion. |
| 02 | `03-sales-pipeline/02-proposal-sow-draft.md` | Commercial defaults must be proposed assumptions. Example adds unsupported requirements. |
| 09 | `03-sales-pipeline/09-meeting-to-crm-log.md` | Meeting paste is not automatic write authorization. Record matching and exact write preview need separation. |
| 13 | `03-sales-pipeline/13-deal-pipeline-review.md` | Fuzzy owner matching must only find candidates; stable IDs should determine scope. Notifications require authorization. |
| 14 | `03-sales-pipeline/14-linkedin-outbound-strategy.md` | No fabricated referral endorsement or compliance claim. Verify vendor-specific claims. |
| 15 | `03-sales-pipeline/15-warm-lead-outreach.md` | Replace identifiable contact anecdote with synthetic data. Tool format and contacted-status claims need qualification. |
| 16 | `03-sales-pipeline/16-linkedin-dm-outreach.md` | Remove fabricated client result and blanket claims about media or messaging capabilities. |
| 27 | `03-sales-pipeline/27-icp-list-build.md` | Enforce required ICP constraints; geography and suppression cannot be inferred from weak evidence. |
| 28 | `03-sales-pipeline/28-unique-cold-outreach.md` | Remove deliverability guarantee; verify specialization and suppression/cooldown checks. |
| 03 | `04-delivery-operations/03-meeting-notes-to-tasks.md` | Redundant approvals and limited meeting scope. Rewritten as Meeting Processor with six outputs. |
| 20 | `04-delivery-operations/20-scope-creep-watchdog.md` | Included. Approved baseline requirement added; unsigned assumptions do not prove agreed scope. |
| 21 | `04-delivery-operations/21-project-risk-review.md` | Included. Unknown dimensions now produce an interval rather than zero or false GREEN. |
| 05 | `05-team-leadership/05-weekly-team-status-digest.md` | Capacity and performance commentary inferred from silence. Remove unsupported judgments. |
| 07 | `05-team-leadership/07-weekly-delegated-task-review.md` | Deadline rollover and example risk classification were wrong. Rewritten with holds, identity, source confidence and verified actions. |
| 08 | `05-team-leadership/08-manager-accountability-scorecard.md` | Backlog throughput is not employee performance. Missing denominator and audience controls. |
| 11 | `05-team-leadership/11-1on1-prep-and-followup.md` | Sensitive 1:1 notes need a private destination. Verify cited third-party licensing and NOTICE obligations before packaging. |
| 22 | `05-team-leadership/22-capacity-overload-review.md` | Handle zero capacity and double-counted admin; retrieve availability rather than private leave reasons. |
| 12 | `06-marketing-content/12-write-in-my-voice.md` | Overbroad automatic trigger and unsupported first-hand results in example. |
| 29 | `06-marketing-content/29-owner-email-rules.md` | No blanket CRM BCC or secret login details; bound email retrieval to relevant history. |
| 30 | `06-marketing-content/30-owner-blog-post.md` | Save voice profiles only when authorized; anonymize or obtain permission for first-hand stories. |
| 04 | `07-research-intelligence/04-competitor-prospect-scan.md` | Browsing availability and example positioning claims need evidence. |
| 31 | `07-research-intelligence/31-lead-research-brief.md` | No inference of locked profiles or outreach efficacy from failed search; bound and refresh sources. |
| 23 | `08-finance-profitability/23-project-margin-leakage-review.md` | Separate recognized and forecast revenue and gross versus contribution margin; guard zero denominators. |
| 32 | `08-finance-profitability/32-contract-red-flag-review.md` | Electronic signature and restrictive-covenant claims need qualified legal review; reconcile outcome logic. |
| 24 | `09-agency-brain-systems/24-meeting-to-knowledge-capture.md` | Strong provenance. Allow unknown source dates explicitly. |
| 25 | `09-agency-brain-systems/25-agency-decision-logger.md` | Add access and minimum-data rules for sensitive decisions. |

Future expansion: fix and forward-test each excluded workflow separately. Do not copy personal SJ identities, tracker IDs, private company facts or paid-service promotion into public operating instructions.
