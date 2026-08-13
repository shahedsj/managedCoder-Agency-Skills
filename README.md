# ManagedCoder Agency Skills

Free, ready-to-use AI "skill files" for digital agency owners. Part of [ManagedCoder](https://managedcoder.com) — AI training for agency owners, by SJ Innovation.

## What this is

A skill file is a page of plain English instructions that an AI agent (Claude, ChatGPT, or similar) can follow every time, so you don't have to explain the task again. Write it once, reuse it forever.

This repo collects skill files built for the tasks agency owners do every week: client updates, proposals, meeting follow-up, prospect research, and team status.

## The Skill Roster

Organized like a real org chart — each division covers a slice of what an agency owner actually spends time on. Start with `00-START-HERE.md`, then grab whichever division fits what's eating your week.

### 📋 Client & Growth Division
*Winning and keeping the work.*

| Skill | Specialty | When to Use |
|---|---|---|
| [Client Status Report](starter-kit/01-client-growth-client-status-report.md) | Turns messy notes into a clean client update | Weekly/biweekly client check-ins |
| [Proposal / SOW Draft](starter-kit/02-client-growth-proposal-sow-draft.md) | Discovery notes → first-pass proposal | New deal, scoping a project |
| [Competitor / Prospect Scan](starter-kit/04-client-growth-competitor-prospect-scan.md) | Company name → pitch-ready brief | Before a sales call or pitch |
| [Meeting-to-CRM Log](starter-kit/09-client-growth-meeting-to-crm-log.md) | Call transcript/notes → logged deal update + next step | Right after any client, prospect, or partner call |

### 🧭 Team & Delegation Division
*Running the team without living in your PM tool.*

| Skill | Specialty | When to Use |
|---|---|---|
| [Meeting Notes → Tasks](starter-kit/03-team-delegation-meeting-notes-to-tasks.md) | Transcript → owned, dated action items | Right after any meeting |
| [Weekly Team Status Digest](starter-kit/05-team-delegation-weekly-team-status-digest.md) | Scattered updates → one Friday-read digest | End of week, before you go dark |
| [Daily Task Triage](starter-kit/06-team-delegation-daily-task-triage.md) | Your own task list → the 3 that matter today | Every morning or evening |
| [Weekly Delegated Task Review](starter-kit/07-team-delegation-weekly-delegated-task-review.md) | Everyone else's tasks → who's stalled, who's blocked | Every Friday, before Monday's meeting |
| [Manager Accountability Scorecard](starter-kit/08-team-delegation-manager-accountability-scorecard.md) | Task data → a one-page Monday scorecard | Monday morning meeting prep |
| [Daily Owner Brief](starter-kit/10-team-delegation-daily-owner-brief.md) | Calendar + tasks + pipeline → one 2-minute morning brief | First thing every morning |
| [1:1 Prep & Follow-Up](starter-kit/11-team-delegation-1on1-prep-and-followup.md) | Direct report's workload → agenda, feedback, and logged follow-up | Before and after every 1:1 |
| [Meeting to Product Roadmap](starter-kit/17-team-delegation-meeting-to-product-roadmap.md) | Strategy meeting → vision doc + a backlog grounded in what's real | After a product direction meeting |

### ✍️ Voice & Outreach Division
*Sounding like yourself, and reaching the right people.*

| Skill | Specialty | When to Use |
|---|---|---|
| [Write in My Voice](starter-kit/12-voice-outreach-write-in-my-voice.md) | AI-sounding drafts → your natural voice, plus full social post rules | Before anything AI-written goes out |
| [Deal Pipeline Review](starter-kit/13-voice-outreach-deal-pipeline-review.md) | Open deals → urgency-ranked review with drafted follow-ups | Daily or a few times a week |
| [LinkedIn Outbound Strategy](starter-kit/14-voice-outreach-linkedin-outbound-strategy.md) | Your existing network → a 30-day sales opportunity plan | Planning or reviewing LinkedIn outreach |
| [Warm Lead Outreach](starter-kit/15-voice-outreach-warm-lead-outreach.md) | Contact list → researched, tier-matched outreach drafts | Working your follow-up backlog |
| [LinkedIn DM Outreach](starter-kit/16-voice-outreach-linkedin-dm-outreach.md) | A specific person → the actual message that gets a reply | Messaging a named contact on LinkedIn |

More divisions will be added over time as the ManagedCoder library grows.

## How to use a skill file

Every file works three ways. Pick whichever suits you.

**Option A — Paste it (works with Claude, ChatGPT, Gemini, anything)**
1. Paste the whole skill file into a new chat.
2. Paste your raw material underneath it.
3. Send.

**Option B — Install it as a skill**
Each file has YAML frontmatter at the top (`name` and `description`), so it works as a real skill file. Upload it to Claude or ChatGPT and it becomes a saved skill that triggers itself when relevant — no pasting each time.

**Option C — Download the whole kit**
Grab the repo as a ZIP (green **Code** button → Download ZIP), unzip, and load the whole `starter-kit/` folder at once.

### Connecting your tools

The skills use placeholders like `~~CRM` and `~~project tracker` instead of naming products, so they work with whatever you already use. See **[CONNECTORS.md](starter-kit/CONNECTORS.md)**.

You don't need to connect anything to start — every skill has a **STANDALONE** mode that works from pasted notes, and a **SUPERCHARGED** mode that kicks in once a tool is connected.

**Nothing is ever written or sent without your approval.** Emails are drafts. CRM updates get proposed first.

If the AI gets something wrong, don't just fix the output — fix the skill file. Add the missing rule or exception. Next time it gets it right, because now it knows.

## Where this comes from

This project follows the idea in Garry Tan's "Own Your Intelligence" talk at YC Startup School 2026 — write down how you work in plain markdown, let an agent run it, and the library compounds over time. This repo is that idea, scoped to what an agency owner actually needs day to day.

## Want this running automatically, not manually?

That's what [Agency Control Tower](https://controltower.collabai.software) does — it wires skill files like these into your actual workflow so they run on their own, across your whole team.

## Contributing

Issues and pull requests are welcome. Keep skill files agency-relevant, plain English, and honest about their limits (say "not specified" rather than inventing an answer).

## License

MIT
