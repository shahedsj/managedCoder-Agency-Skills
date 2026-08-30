# ManagedCoder Agency Skills

**An open library of reusable AI operating skills for agency owners.**

Most agency owners do not need another AI demo. They need help running the business they already have.

ManagedCoder turns recurring agency work into reusable operating instructions: client health, pipeline, delegation, project risk, scope, team accountability, profitability, meeting intelligence, and company knowledge.

Write the operating logic once. Improve it when you learn. Reuse it across capable AI systems.

Part of [ManagedCoder](https://managedcoder.com), practical AI training for agency owners by SJ Innovation.

## What makes this different

This is not a prompt collection and it is not an imaginary AI agency with hundreds of job titles.

A useful ManagedCoder skill should do at least one of these:

- reduce owner dependency
- catch risk before it becomes a client problem
- improve a recurring business decision
- make delegation and accountability more consistent
- protect scope, margin, or follow-up
- capture company knowledge so it does not live only in people's heads
- turn scattered information into an actionable operating picture

The goal is **less founder dependency, stronger company knowledge, better decisions, and more repeatable execution.**

## The ManagedCoder maturity path

```text
Learn -> Build -> Skill -> Brain -> Connect -> Automate -> Delegate -> Operate
```

You can start with one markdown file and pasted information.

As the agency matures, the same operating logic can use an Agency Second Brain and connected business systems. Repeated trusted workflows can later become automations or agents.

## 26 starter skills across 9 operating categories

| Category | What it helps you run | Coverage |
|---|---|---|
| **01 Owner Command & Direction** | Priorities, decisions, daily/weekly briefs, meeting prep, direction | Available |
| **02 Client Success & Retention** | Client communication, health, expectations, relationship risk | Available |
| **03 Sales & Pipeline** | CRM, proposals, prospecting, outreach, pipeline follow-up | Available |
| **04 Delivery, Scope & Operations** | Commitments, scope, project risk, execution | Available |
| **05 Team & Leadership** | Delegation, accountability, managers, 1:1s, capacity | Available |
| **06 Marketing, Voice & Content** | Brand voice and owner communication | Available, expanding |
| **07 Research & Intelligence** | Prospect, competitor, market and industry intelligence | Available, expanding |
| **08 Finance & Profitability** | Project margin leakage and agency economics | Available, expanding |
| **09 Agency Brain & Systems** | Decisions, institutional knowledge, second-brain patterns | Available, expanding |

See [`starter-kit/00-START-HERE.md`](starter-kit/00-START-HERE.md) for the guided starting point.

## Start with the problem, not the library

| If this is happening... | Start here |
|---|---|
| Client updates take too long | **Client Status Report** |
| You do not know which clients are becoming risky | **Client Health Review** |
| Meetings end but ownership is unclear | **Meeting Notes to Tasks** |
| The same decision keeps getting reopened | **Agency Decision Logger** |
| Meeting knowledge disappears after the transcript | **Meeting to Knowledge Capture** |
| You are unsure what deserves your attention today | **Daily Owner Brief** |
| Weekly reviews are full of status but few decisions | **Weekly Owner Decision Brief** |
| You need context before an important call | **Next Meeting Prep Brief** |
| Client requests keep expanding | **Scope Creep Watchdog** |
| Project status says green but you do not trust it | **Project Risk Review** |
| You cannot tell whether the team is overloaded | **Capacity & Overload Review** |
| A project is busy but not profitable | **Project Margin Leakage Review** |
| Deals sit without clear next steps | **Deal Pipeline Review** |
| AI writing does not sound like you | **Write in My Voice** |

## Current skill library

### 01 Owner Command & Direction
- Daily Task Triage
- Daily Owner Brief
- Meeting to Product Roadmap
- Weekly Owner Decision Brief
- Next Meeting Prep Brief

### 02 Client Success & Retention
- Client Status Report
- Client Health Review

### 03 Sales & Pipeline
- Proposal / SOW Draft
- Meeting-to-CRM Log
- Deal Pipeline Review
- LinkedIn Outbound Strategy
- Warm Lead Outreach
- LinkedIn DM Outreach

### 04 Delivery, Scope & Operations
- Meeting Notes to Tasks
- Scope Creep Watchdog
- Project Risk Review

### 05 Team & Leadership
- Weekly Team Status Digest
- Weekly Delegated Task Review
- Manager Accountability Scorecard
- 1:1 Prep & Follow-Up
- Capacity & Overload Review

### 06 Marketing, Voice & Content
- Write in My Voice

### 07 Research & Intelligence
- Competitor / Prospect Scan

### 08 Finance & Profitability
- Project Margin Leakage Review

### 09 Agency Brain & Systems
- Meeting to Knowledge Capture
- Agency Decision Logger

Next Agency Brain additions: SOP Builder, Employee Handoff Builder, knowledge health review, and Agency Second Brain setup/maintenance.

## What a skill contains

A skill file is a set of plain-English operating instructions for a recurring job.

Good skills contain more than wording. They contain reusable judgment:

- workflow rules
- decision logic
- thresholds and exceptions
- prioritization
- required inputs
- missing-data behavior
- validation
- structured outputs
- source/provenance behavior
- approval rules
- connector behavior

The value is not the first output. The value is what happens after you improve the file.

If the AI misses something important, fix the rule in the skill instead of correcting only that one answer. The next run starts with what you learned.

## Standalone first, connected second

**Standalone:** paste the information you already have. No special infrastructure required.

**Connected:** let the same skill retrieve context from CRM, project management, email, calendar, meetings, finance, or an Agency Brain. See [`starter-kit/CONNECTORS.md`](starter-kit/CONNECTORS.md).

A connected skill should become more informed, not become a completely different workflow.

## Human approval stays in the loop

Connected does not mean uncontrolled.

Default pattern:

```text
READ
  -> UNDERSTAND
  -> VERIFY
  -> DRAFT OR RECOMMEND
  -> HUMAN APPROVAL
  -> WRITE OR SEND
```

A client email, task, CRM change, scope change, financial action, or knowledge update should not happen silently because an AI decided it was ready.

## Skills, Brain, Connectors, Workflows

Keep the layers separate:

- **Skills** contain reusable operating logic.
- **Agency Brain** contains company knowledge, decisions, SOPs, context, history, and reviewed lessons.
- **Connectors** read and write live systems.
- **Workflows** chain several skills around a recurring business process.
- **Automations/agents** run mature workflows after the agency trusts the logic and controls.

Changing business facts should live in authoritative data/knowledge systems, not hardcoded inside skills.

## Example workflow

```text
Client meeting
  -> Meeting Notes to Tasks
  -> Meeting to Knowledge Capture
  -> Meeting-to-CRM Log
  -> Scope Creep Watchdog
  -> Client Health Review
  -> Client Status Report
  -> Weekly Owner Decision Brief
```

One meeting can now update execution, relationship context, scope awareness, and durable company knowledge without pretending those are the same thing.

## Contribution standard

Before adding a skill, ask:

1. Does it solve a recurring agency problem?
2. Does it reduce founder dependency or improve a decision?
3. Is it meaningfully agency-specific?
4. Does it contain operating logic rather than only prompting?
5. Can it work standalone?
6. Can it later use connected systems?
7. Can Agency Brain knowledge improve it?
8. Does it produce an actionable result?
9. Are consequential actions human-reviewable?
10. Does company knowledge make it improve over time?
11. Is there a logical path toward workflow automation or an Agency Control Tower?

## Where this is going

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

The durable asset is the agency's knowledge and operating logic, not one LLM. Keep it usable by ChatGPT, Claude, Gemini, Codex, MCP clients, and future models.

## ManagedCoder

ManagedCoder teaches agency owners how to build this progression themselves instead of only buying another AI tool.

[ManagedCoder](https://managedcoder.com)

For teams that want these workflows connected and running across the business, see [Agency Control Tower](https://controltower.collabai.software).

## License

MIT
