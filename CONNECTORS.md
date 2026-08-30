# Connectors

## How tool references work

These skills are **tool-agnostic**. Instead of naming a specific product, they use a `~~category` placeholder for whatever tool you've connected in that category.

So `~~CRM` means *your* CRM — HubSpot, Pipedrive, GoHighLevel, Close, Salesforce, whatever you actually use. The skill works the same either way.

## The categories these skills use

| Placeholder | Means | Common options |
|---|---|---|
| `~~CRM` | Your deal and contact system | HubSpot, Pipedrive, GoHighLevel, Close, Salesforce, Copper |
| `~~project tracker` | Where tasks and projects live | Asana, ClickUp, Monday.com, Linear, Jira, Notion, Basecamp |
| `~~email` | Your inbox | Gmail, Outlook / Microsoft 365 |
| `~~calendar` | Your calendar | Google Calendar, Outlook / Microsoft 365 |
| `~~chat` | Team messaging | Slack, Microsoft Teams, Discord |
| `~~meeting notes` | Call recordings and transcripts | Zoom, Google Meet, Fireflies, Otter, Gong |
| `~~docs` | Where documents live | Notion, Google Drive, Confluence, Dropbox |

## How to connect a tool

**In Claude:** Settings → Connectors. Search for your tool and connect it once. Every skill in this kit will use it from then on.

**In ChatGPT:** Settings → Connectors (availability varies by plan and tool).

You only do this once per tool, not once per skill.

## You don't need any of them to start

Every skill in this kit runs standalone. Each one has a "How it works" box near the top showing two rows:

- **STANDALONE** — what happens with nothing connected. You paste your notes, list, or export, and the skill still does its job.
- **SUPERCHARGED** — what gets better once a tool is connected. Usually: the skill pulls the data itself instead of asking you for it, and can write results back after you approve them.

Start standalone. Connect tools when you get tired of pasting.

## One rule that never changes

**Nothing gets written or sent without your explicit approval.** Even with every tool connected, these skills propose the note, the task, the status change, or the email — and wait for you to say yes. Emails are always drafts, never sends.

If a skill ever writes something without asking, that's a bug. Please open an issue.

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want these running on their own across your whole team? See Agency Control Tower: controltower.collabai.software*
