# ManagedCoder Agency Skills

**An open library of reusable AI operating skills for agency owners.**

Most agency owners do not need another AI demo. They need help running the business they already have.

ManagedCoder Agency Skills turns recurring agency work into reusable instructions your AI can follow consistently. Client updates. Pipeline reviews. Delegation. Project risk. Team accountability. Research. Reporting. Knowledge capture.

Write the operating logic once. Improve it when you learn. Reuse it across Claude, ChatGPT, and other capable AI systems.

Part of [ManagedCoder](https://managedcoder.com), practical AI training for agency owners by SJ Innovation.

## What makes this different

This is not a collection of clever prompts and it is not an imaginary AI agency with hundreds of job titles.

The library is organized around the real operating responsibilities of an agency owner.

A useful skill should do at least one of these things:

- save the owner or manager meaningful time
- catch a risk before it becomes a client problem
- make delegation more consistent
- turn scattered information into a decision
- protect scope, margin, or follow-up
- capture knowledge so the company does not depend on one person's memory

The goal is simple: **less owner dependency, better operating visibility, and more repeatable execution.**

## The Agency Skill OS

The library is growing into nine operating categories.

| Category | What it helps you run | Current coverage |
|---|---|---|
| **01 Owner Command & Direction** | Priorities, decisions, daily briefs, strategic direction | Available |
| **02 Client Success & Retention** | Client communication, health, expectations, renewals, risk | Available, expanding |
| **03 Sales & Pipeline** | CRM, proposals, prospecting, outreach, pipeline follow-up | Available |
| **04 Delivery, Scope & Operations** | Projects, scope, capacity, delivery risk, execution | Available, expanding |
| **05 Team & Leadership** | Delegation, accountability, managers, 1:1s, team visibility | Available |
| **06 Marketing, Voice & Content** | Brand voice, owner content, marketing execution | Available, expanding |
| **07 Research & Intelligence** | Prospect, competitor, market and industry intelligence | Available, expanding |
| **08 Finance & Profitability** | Margin, utilization, pricing, invoices, cash and profitability | Coming next |
| **09 Agency Brain & Systems** | SOPs, decisions, institutional knowledge, handoffs, second brain | Coming next |

A small agency may only need a few of these. A larger agency can connect them into workflows and eventually run them automatically.

## Start with a real problem

Do not install everything.

Pick the thing that is wasting time or creating risk this week.

| If this is happening... | Start here |
|---|---|
| Client updates take too long or projects are slipping | **Client Status Report** |
| Meetings end but ownership is unclear | **Meeting Notes to Tasks** |
| You are unsure what deserves your attention today | **Daily Owner Brief** |
| Managers are not following through consistently | **Manager Accountability Scorecard** |
| Deals sit without clear next steps | **Deal Pipeline Review** |
| AI writing does not sound like you | **Write in My Voice** |

See [`starter-kit/00-START-HERE.md`](starter-kit/00-START-HERE.md) for the guided starting point.

## Current skill library

### 01 Owner Command & Direction

*Know what matters, what needs a decision, and what should be delegated.*

- **Daily Task Triage**: turn your task list into the few things that deserve attention now
- **Daily Owner Brief**: combine calendar, tasks and pipeline into a short operating brief
- **Meeting to Product Roadmap**: turn a strategy discussion into direction and an actionable backlog

### 02 Client Success & Retention

*Keep clients informed before small problems become relationship problems.*

- **Client Status Report**: turn messy delivery notes into a clear client update and surface hidden risk

### 03 Sales & Pipeline

*Move opportunities forward without relying on memory for follow-up.*

- **Proposal / SOW Draft**
- **Meeting-to-CRM Log**
- **Deal Pipeline Review**
- **LinkedIn Outbound Strategy**
- **Warm Lead Outreach**
- **LinkedIn DM Outreach**

### 04 Delivery, Scope & Operations

*Turn commitments into owned work and make delivery easier to manage.*

- **Meeting Notes to Tasks**

Next additions will focus on scope creep, project risk, capacity and delivery visibility.

### 05 Team & Leadership

*Build a management layer so every issue does not come back to the owner.*

- **Weekly Team Status Digest**
- **Weekly Delegated Task Review**
- **Manager Accountability Scorecard**
- **1:1 Prep & Follow-Up**

### 06 Marketing, Voice & Content

*Use AI without losing the owner's actual voice.*

- **Write in My Voice**

### 07 Research & Intelligence

*Turn outside information into useful context before a sales or strategic decision.*

- **Competitor / Prospect Scan**

### 08 Finance & Profitability

Planned skills include margin leakage review, utilization review, invoice follow-up, pricing review and monthly profitability review.

### 09 Agency Brain & Systems

Planned skills include meeting-to-knowledge capture, decision logging, SOP creation, employee handoffs and Agency Second Brain maintenance.

## How a skill works

A skill file is a set of plain-English operating instructions that tells an AI how to perform a recurring job.

The value is not the first output. The value is what happens after you improve the file.

If the AI misses something important, update the rule in the skill instead of fixing only that one answer. The next run starts with what you learned.

That is how the library compounds.

## Three ways to use the library

**Paste it**

Open a skill file, paste it into Claude, ChatGPT, Gemini, or another capable AI, then provide the material it needs.

**Install it**

Skills include frontmatter so compatible AI systems can save and reuse the instructions instead of making you paste them every time.

**Connect it**

Many skills support a standalone mode using pasted information and a connected mode using systems such as your CRM, project tracker, email, calendar, or other business tools. See [`starter-kit/CONNECTORS.md`](starter-kit/CONNECTORS.md).

## Human approval stays in the loop

Connected does not mean uncontrolled.

The default pattern is:

1. read the relevant information
2. analyze it using the skill's rules
3. propose the action or draft
4. let a human approve consequential writes or sends

A client email should not suddenly send itself because an AI decided it was ready.

## From individual skills to agency workflows

One skill solves one recurring job. The larger opportunity comes from connecting them.

For example:

```text
Meeting
  -> Meeting Notes to Tasks
  -> Meeting-to-CRM Log
  -> Client Status Report
  -> Delegated Task Review
  -> Daily Owner Brief
```

That is the direction of ManagedCoder: reusable operating intelligence that can start manually, connect to existing tools, and eventually become part of an Agency Control Tower.

## Principles for contributions

A ManagedCoder skill should be:

- **Agency-specific**: solve a real agency operating problem
- **Reusable**: useful more than once
- **Opinionated**: include actual rules, thresholds, checks or output structure
- **Tool-flexible**: avoid unnecessary dependence on one SaaS product
- **Honest**: say when information is missing instead of inventing it
- **Safe to operate**: require approval before consequential external actions unless the user explicitly configures otherwise
- **Easy to improve**: the logic should be understandable enough for an owner to edit

Issues and pull requests are welcome.

## Where this is going

The long-term model has three layers:

```text
AGENCY OWNER
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
CRM | Project Management | Email | Calendar | Meetings | Finance
```

The skill files are the operating logic. Your systems hold the live data. The Agency Brain preserves context. A Control Tower can eventually orchestrate the workflows across all three.

## ManagedCoder

ManagedCoder teaches agency owners how to build this themselves instead of only buying another AI tool.

[ManagedCoder](https://managedcoder.com)

For teams that want these workflows connected and running across the business, see [Agency Control Tower](https://controltower.collabai.software).

## License

MIT
