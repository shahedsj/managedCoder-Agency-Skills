# ManagedCoder Agency Skills

**What part of your agency still depends on you?**

ManagedCoder Agency Skills is an open library of reusable AI operating skills built around real agency work: clients, sales, delivery, delegation, profitability, decisions, and company knowledge.

You do not need to install everything. Pick the problem you want help with and start there.

**New here?** Start with [`START-HERE.md`](START-HERE.md). No special setup is required.

**New skill every week. [Get them by email →](https://managedcoder.com/newsletter)**<br>
**Using these in your agency? [Tell me which one →](https://github.com/shahedsj/managedCoder-Agency-Skills/issues/new?template=skill-feedback.yml)**

## Pick the part of your agency you want to improve

| Area | Use it when... | Skills |
|---|---|---:|
| [**01 Owner Command & Direction**](01-owner-command/) | Too many things still need the owner's attention or decision | 5 |
| [**02 Client Success & Retention**](02-client-success/) | You want to catch client risk before the client becomes the alert | 2 |
| [**03 Sales & Pipeline**](03-sales-pipeline/) | Deals, proposals, CRM, and follow-up are inconsistent | 8 |
| [**04 Delivery, Scope & Operations**](04-delivery-operations/) | Projects slip, ownership is unclear, or scope keeps expanding | 3 |
| [**05 Team & Leadership**](05-team-leadership/) | Delegation, accountability, 1:1s, or capacity need stronger systems | 5 |
| [**06 Marketing, Voice & Content**](06-marketing-content/) | You want AI help without losing the owner's real voice | 3 |
| [**07 Research & Intelligence**](07-research-intelligence/) | You need better prospect, competitor, or market intelligence | 2 |
| [**08 Finance & Profitability**](08-finance-profitability/) | Projects are busy but you cannot see where margin is leaking | 2 |
| [**09 Agency Brain & Systems**](09-agency-brain-systems/) | Important decisions and knowledge keep disappearing into meetings and people's heads | 2 |

## Start with a problem you have this week

| Problem | Try this skill |
|---|---|
| Client updates take too long | [Client Status Report](02-client-success/01-client-status-report.md) |
| You do not know which clients are becoming risky | [Client Health Review](02-client-success/19-client-health-review.md) |
| Meetings end but ownership is unclear | [Meeting Notes to Tasks](04-delivery-operations/03-meeting-notes-to-tasks.md) |
| Client requests keep expanding | [Scope Creep Watchdog](04-delivery-operations/20-scope-creep-watchdog.md) |
| Project status says green but you do not trust it | [Project Risk Review](04-delivery-operations/21-project-risk-review.md) |
| Your weekly review is mostly status instead of decisions | [Weekly Owner Decision Brief](01-owner-command/18-weekly-owner-decision-brief.md) |
| You need context before an important call | [Next Meeting Prep Brief](01-owner-command/26-next-meeting-prep-brief.md) |
| You cannot tell whether the team is truly overloaded | [Capacity & Overload Review](05-team-leadership/22-capacity-overload-review.md) |
| A project is busy but margin keeps disappearing | [Project Margin Leakage Review](08-finance-profitability/23-project-margin-leakage-review.md) |
| Meeting knowledge disappears after the transcript | [Meeting to Knowledge Capture](09-agency-brain-systems/24-meeting-to-knowledge-capture.md) |
| The same leadership decision keeps getting reopened | [Agency Decision Logger](09-agency-brain-systems/25-agency-decision-logger.md) |
| Deals sit without clear next steps | [Deal Pipeline Review](03-sales-pipeline/13-deal-pipeline-review.md) |
| AI writing does not sound like you | [Write in My Voice](06-marketing-content/12-write-in-my-voice.md) |
| Your outreach list has never been properly cleaned | [ICP List Build](03-sales-pipeline/27-icp-list-build.md) |
| A batch of emails all read like the same template | [Unique Cold Outreach](03-sales-pipeline/28-unique-cold-outreach.md) |
| Every email you send sounds like a different person wrote it | [Owner Email Rules](06-marketing-content/29-owner-email-rules.md) |
| You want to write about what you actually learned running the agency | [Owner Blog Post](06-marketing-content/30-owner-blog-post.md) |
| You need real background on a person before a call | [Lead Research Brief](07-research-intelligence/31-lead-research-brief.md) |
| A contract is sitting unread and somebody wants it signed | [Contract Red-Flag Review](08-finance-profitability/32-contract-red-flag-review.md) |

## How to use a skill

**1. Open one skill.**

**2. Give it real agency information.** Paste meeting notes, project updates, CRM data, tasks, or whatever the skill asks for.

**3. Run it in ChatGPT, Claude, Gemini, Codex, or another capable AI.**

**4. Improve the operating rule when the output is wrong.** Do not only correct the answer. Improve the reusable skill.

That is the idea behind ManagedCoder: turn what normally lives in the owner's head into operating logic the company can reuse.

## More than prompts

A ManagedCoder skill can contain:

- workflow rules
- decision logic
- thresholds and exceptions
- prioritization
- required inputs and missing-data behavior
- validation
- structured outputs
- source/provenance behavior
- approval rules
- connector behavior

`Prioritize my tasks` is a prompt.

`Score overdue client commitments higher, identify blocked delegated work, separate decisions only I can make, and return the top three actions` is operating logic.

## Standalone first

Every starter skill should work with information you paste into the conversation.

No CRM integration. No database. No Control Tower required.

When useful, the same skill can later retrieve context from connected CRM, project management, email, calendar, meetings, finance, or an Agency Brain. See [`CONNECTORS.md`](CONNECTORS.md).

## Human approval stays in the loop

Connected does not mean uncontrolled.

```text
READ
  -> UNDERSTAND
  -> VERIFY
  -> DRAFT OR RECOMMEND
  -> HUMAN APPROVAL
  -> WRITE OR SEND
```

Client communication, task creation, CRM changes, scope changes, financial actions, and company-knowledge updates should remain reviewable.

## Where this leads

```text
Learn -> Build -> Skill -> Brain -> Connect -> Automate -> Delegate -> Operate
```

```text
AGENCY OWNER / TEAM
        |
        v
OPERATING SKILLS
Owner | Clients | Sales | Delivery | Team | Marketing | Research | Finance
        |
        v
AGENCY BRAIN
Knowledge | Decisions | SOPs | Client Context | History
        |
        v
CONNECTED SYSTEMS
CRM | PM | Email | Calendar | Meetings | Finance
        |
        v
WORKFLOWS -> AUTOMATIONS -> AGENTS -> AGENCY CONTROL TOWER
```

The durable asset is the agency's knowledge and operating logic, not one LLM.

## ManagedCoder

[ManagedCoder](https://managedcoder.com) teaches agency owners how to build practical AI operating systems from real agency work.

For teams that eventually want these workflows connected across their business, see [Agency Control Tower](https://controltower.collabai.software).

## License

MIT



## Agency Operations plugin release candidate

Six operating Skills plus context setup are now packaged as a portable Skills-only plugin. They work from supplied notes and files. No signup or connector is required. This is a release candidate, not an approved public-directory listing. The other catalog Skills remain reference workflows and are not included in this first package.

- [Install and try](docs/plugin/INSTALL.md)
- [Publishing status](docs/plugin/PUBLISHING.md)
- [Launch plan](docs/plugin/LAUNCH_PLAN.md)
- [Pilot protocol](docs/plugin/PILOT.md)
- [Validation](docs/plugin/VALIDATION.md)
- [Privacy](docs/plugin/PRIVACY.md)

Build: `python3 scripts/build_plugin.py`. Requires Python 3 and PyYAML. Check generated files with `python3 scripts/build_plugin.py --check`.
