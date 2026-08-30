# Start Here: ManagedCoder Agency Skill Starter Kit

**17 reusable AI skills for the work agency owners deal with every week.**

This is not a prompt collection to browse for an hour.

Pick one recurring problem. Use one skill on real agency work. If it saves time, catches a risk, or improves a decision, keep it. Then improve the file as your operating rules get better.

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

You should get more than polished writing. A useful result should also surface things you might otherwise miss, such as an aging client dependency or a request that may be outside the agreed scope.

That is the difference between asking AI to write and giving AI operating instructions.

## Choose based on the problem

You do not need all 17 skills.

| What is happening in your agency? | Start with |
|---|---|
| Client updates take too long | **01 Client Status Report** |
| Meetings create notes but not ownership | **03 Meeting Notes to Tasks** |
| Your day is controlled by whoever messages you first | **10 Daily Owner Brief** |
| You have too many tasks and cannot see the real priorities | **06 Daily Task Triage** |
| Delegated work keeps coming back to you | **07 Weekly Delegated Task Review** |
| Managers need stronger accountability | **08 Manager Accountability Scorecard** |
| Deals are sitting without clear next steps | **13 Deal Pipeline Review** |
| You need to follow up with warm contacts | **15 Warm Lead Outreach** |
| AI writing sounds generic | **12 Write in My Voice** |

## How the library is organized

ManagedCoder is organized around the operating responsibilities of an agency owner, not around imaginary AI job titles.

### 01 Owner Command & Direction

Know what matters, what needs a decision, and what should be delegated.

Current skills: `06 Daily Task Triage`, `10 Daily Owner Brief`, `17 Meeting to Product Roadmap`.

### 02 Client Success & Retention

Keep clients informed and surface relationship risk before it becomes an escalation.

Current skill: `01 Client Status Report`.

### 03 Sales & Pipeline

Keep opportunities moving from research and proposal through CRM and follow-up.

Current skills: `02 Proposal / SOW Draft`, `09 Meeting-to-CRM Log`, `13 Deal Pipeline Review`, `14 LinkedIn Outbound Strategy`, `15 Warm Lead Outreach`, `16 LinkedIn DM Outreach`.

### 04 Delivery, Scope & Operations

Turn commitments into owned work and make delivery problems visible earlier.

Current skill: `03 Meeting Notes to Tasks`.

Upcoming focus: scope creep, project risk, capacity, delivery visibility.

### 05 Team & Leadership

Build a stronger management layer so every question and escalation does not depend on the owner.

Current skills: `05 Weekly Team Status Digest`, `07 Weekly Delegated Task Review`, `08 Manager Accountability Scorecard`, `11 1:1 Prep & Follow-Up`.

### 06 Marketing, Voice & Content

Use AI to communicate and create without flattening the owner's actual voice.

Current skill: `12 Write in My Voice`.

### 07 Research & Intelligence

Research prospects, competitors, markets and changes before making a sales or strategic decision.

Current skill: `04 Competitor / Prospect Scan`.

### 08 Finance & Profitability

Protect margin and improve financial visibility.

Planned: project margin leakage, utilization, invoice follow-up, pricing and monthly profitability review.

### 09 Agency Brain & Systems

Capture the knowledge that normally disappears into meetings, Slack, documents and people's heads.

Planned: decision logs, meeting-to-knowledge capture, SOP creation, handoffs and Agency Second Brain maintenance.

## What a skill file actually contains

A useful skill is not just a long prompt.

It can contain:

- rules for what information to inspect
- scoring or prioritization logic
- thresholds and exceptions
- required checks before producing an answer
- a repeatable output format
- instructions for connected tools
- approval rules before anything is written or sent

Specific operating logic is what makes the output repeatable.

"Prioritize my tasks" is a prompt.

"Score overdue client commitments higher, identify blocked delegated work, separate decisions only I can make, and return the top three actions" is operating logic.

## Standalone first, connected when useful

Every starter skill should remain useful without a complicated setup.

**Standalone mode** works from information you paste into the conversation.

**Connected mode** can use your CRM, project tracker, email, calendar, meeting system, or other connected tools to retrieve the same information automatically.

See [`CONNECTORS.md`](CONNECTORS.md) for the connector pattern.

## Human approval is the default

The skills may analyze information and prepare actions, but consequential external actions should remain reviewable.

A normal connected workflow looks like this:

```text
READ
  -> ANALYZE
  -> DRAFT OR RECOMMEND
  -> HUMAN APPROVAL
  -> WRITE OR SEND
```

If a skill sends client communication or changes important business data without the approval behavior it promises, treat that as a bug.

## Fix the skill, not only the answer

When an output is wrong, ask why.

Did the skill miss an exception? Add it.

Did it prioritize the wrong thing? Improve the scoring rule.

Did it use the wrong tone? Add a better example or constraint.

Did it need information that was unavailable? Define the source it should use next time.

A skill you have corrected several times becomes a small piece of your company's operating knowledge.

## Where this leads

Individual skills are the starting point.

The larger model is:

```text
Your agency systems
CRM + PM + Email + Calendar + Meetings + Finance
                 |
                 v
            Agency Brain
      context + history + decisions
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

You can start with one markdown file today. You do not need the full architecture to get value from the first skill.

## ManagedCoder

ManagedCoder is practical AI training for agency owners. The goal is to leave with working systems and reusable operating knowledge, not just notes from another AI class.

See [ManagedCoder](https://managedcoder.com) for classes and resources.

If you eventually want the skills connected across your agency, see [Agency Control Tower](https://controltower.collabai.software).
