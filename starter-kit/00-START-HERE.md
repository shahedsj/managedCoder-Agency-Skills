# Start Here: ManagedCoder Agency Skill Starter Kit

**26 reusable AI operating skills for agency owners.**

This is not a prompt collection to browse for an hour.

Pick one recurring agency problem. Use one skill on real work. If it saves time, catches a risk, improves a decision, or captures knowledge that would otherwise disappear, keep it. Then improve the file as your operating rules get better.

That is the system.

## Get your first win in 5 minutes

Start with a live client project.

**1.** Open [`01 Client Status Report`](02-client-success/01-client-status-report.md).

**2.** Copy the skill into Claude, ChatGPT, or another capable AI.

**3.** Paste the rough notes you already have. They do not need to be clean.

```text
finished homepage, checkout started, still waiting for logo
client has not replied to feedback request from last week
dev expects checkout friday
client also asked for a blog section but it was not in original scope
```

**4.** Run the skill.

A useful result should do more than rewrite the notes. It should apply operating logic: surface dependencies, risk, ownership, scope, or the next decision.

That is the difference between asking AI to write and giving AI a reusable way to operate.

## Choose based on the problem

You do not need all 26 skills.

| What is happening in your agency? | Start with |
|---|---|
| Client updates take too long | **01 Client Status Report** |
| You do not know which clients are becoming risky | **19 Client Health Review** |
| Meetings create notes but not ownership | **03 Meeting Notes to Tasks** |
| Important meeting decisions keep getting forgotten | **24 Meeting to Knowledge Capture** |
| The same leadership decision keeps getting reopened | **25 Agency Decision Logger** |
| Your day is controlled by whoever messages you first | **10 Daily Owner Brief** |
| Your weekly review is mostly status instead of decisions | **18 Weekly Owner Decision Brief** |
| You need to prepare for an important meeting | **26 Next Meeting Prep Brief** |
| You have too many tasks and cannot see the real priorities | **06 Daily Task Triage** |
| Delegated work keeps coming back to you | **07 Weekly Delegated Task Review** |
| Managers need stronger accountability | **08 Manager Accountability Scorecard** |
| You cannot tell whether the team is truly overloaded | **22 Capacity & Overload Review** |
| A client keeps asking for small extras | **20 Scope Creep Watchdog** |
| You need an honest R/Y/G project review | **21 Project Risk Review** |
| A project is busy but margin keeps disappearing | **23 Project Margin Leakage Review** |
| Deals are sitting without clear next steps | **13 Deal Pipeline Review** |
| You need to follow up with warm contacts | **15 Warm Lead Outreach** |
| AI writing sounds generic | **12 Write in My Voice** |

## How the library is organized

ManagedCoder is organized around what an agency owner needs to run the business, not around imaginary AI job titles.

### 01 Owner Command & Direction

Know what matters, what needs a decision, what should be delegated, and what the owner needs before an important meeting.

Current skills: `06 Daily Task Triage`, `10 Daily Owner Brief`, `17 Meeting to Product Roadmap`, `18 Weekly Owner Decision Brief`, `26 Next Meeting Prep Brief`.

### 02 Client Success & Retention

Keep clients informed and surface relationship risk before the client becomes the alerting system.

Current skills: `01 Client Status Report`, `19 Client Health Review`.

### 03 Sales & Pipeline

Keep opportunities moving from research and proposal through CRM and follow-up.

Current skills: `02 Proposal / SOW Draft`, `09 Meeting-to-CRM Log`, `13 Deal Pipeline Review`, `14 LinkedIn Outbound Strategy`, `15 Warm Lead Outreach`, `16 LinkedIn DM Outreach`.

### 04 Delivery, Scope & Operations

Turn commitments into owned work, protect scope, and make delivery problems visible early.

Current skills: `03 Meeting Notes to Tasks`, `20 Scope Creep Watchdog`, `21 Project Risk Review`.

### 05 Team & Leadership

Build a management layer that can resolve more issues without sending every decision back to the owner.

Current skills: `05 Weekly Team Status Digest`, `07 Weekly Delegated Task Review`, `08 Manager Accountability Scorecard`, `11 1:1 Prep & Follow-Up`, `22 Capacity & Overload Review`.

### 06 Marketing, Voice & Content

Use AI to communicate and create without flattening the owner's actual voice.

Current skill: `12 Write in My Voice`.

### 07 Research & Intelligence

Research prospects, competitors, markets, and changes before making a sales or strategic decision.

Current skill: `04 Competitor / Prospect Scan`.

### 08 Finance & Profitability

Protect project economics and make margin leakage visible while there is still time to correct it.

Current skill: `23 Project Margin Leakage Review`.

Next: invoice/cash collection, pricing, utilization economics, monthly profitability.

### 09 Agency Brain & Systems

Capture the knowledge that normally disappears into meetings, chat, documents, and people's heads.

Current skills: `24 Meeting to Knowledge Capture`, `25 Agency Decision Logger`.

Next: SOP Builder, Employee Handoff Builder, knowledge health review, Agency Second Brain setup and maintenance.

## What a skill file actually contains

A useful skill is not just a long prompt.

It can contain:

- rules for what information to inspect
- decision logic and prioritization
- thresholds and exceptions
- required inputs and missing-data behavior
- validation before acting
- a repeatable output contract
- instructions for connected tools
- source/provenance rules
- approval rules before consequential writes or sends

`Prioritize my tasks` is a prompt.

`Score overdue client commitments higher, identify blocked delegated work, separate decisions only I can make, and return the top three actions` is operating logic.

## Standalone first, connected when useful

Every starter skill should remain useful without a complicated setup.

**Standalone mode** works from information you paste into the conversation.

**Connected mode** retrieves the same inputs from CRM, project management, email, calendar, meetings, finance, or an Agency Brain.

See [`CONNECTORS.md`](CONNECTORS.md) for the connector pattern.

## Human approval is the default

Skills may read, analyze, score, draft, and recommend. Consequential writes should remain reviewable.

```text
READ
  -> UNDERSTAND
  -> VERIFY
  -> RECOMMEND OR DRAFT
  -> HUMAN APPROVAL
  -> WRITE OR SEND
```

If a skill promises review but silently sends a client message, creates a task, changes scope, moves a deal, or rewrites company knowledge, treat that as a bug.

## Fix the skill, not only the answer

When an output is wrong, ask why.

Did it miss an exception? Add the rule.

Did it prioritize the wrong thing? Improve the scoring.

Did it guess a missing owner or date? Add a validation rule.

Did it need company context? Define the authoritative source.

Did the same decision get reopened? Capture it in Agency Brain.

A skill you have corrected several times becomes a piece of reusable operating knowledge.

## The ManagedCoder maturity path

```text
Learn -> Build -> Skill -> Brain -> Connect -> Automate -> Delegate -> Operate
```

You can start with a markdown skill and pasted information.

As the agency matures, the same skill can use company knowledge and connected systems. Repeated, trusted workflows can later become automations or agents.

## Where this leads

```text
Agency systems
CRM + PM + Email + Calendar + Meetings + Finance
                 |
                 v
            Agency Brain
 context + history + decisions + SOPs
                 |
                 v
          Operating Skills
                 |
                 v
       recurring workflows
                 |
                 v
        Agency Control Tower
```

The durable asset is the company's knowledge and operating logic, not one LLM. Keep the architecture usable across ChatGPT, Claude, Gemini, Codex, MCP clients, and future models.

## ManagedCoder

ManagedCoder is practical AI training for agency owners. The goal is to leave with working systems and reusable operating knowledge, not just notes from another AI class.

See [ManagedCoder](https://managedcoder.com) for classes and resources.

If you eventually want the skills connected across your agency, see [Agency Control Tower](https://controltower.collabai.software).
