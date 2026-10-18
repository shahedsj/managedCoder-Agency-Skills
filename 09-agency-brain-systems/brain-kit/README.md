# Agency Brain Kit

A small folder of Markdown files that holds what your agency knows, so it stops living only in your head.

It is free. You do not need to sign up, connect a tool, or use any ManagedCoder product. It works with ChatGPT, Claude, Gemini, Codex or any capable AI.

## How it works

You keep the files. The AI reads them when you ask a question, and helps you add to them.

| Step | Skill | What it does |
|---|---|---|
| Add | [37 Build the Brain](../37-build-the-brain.md) | Turns your rough notes into these files |
| Add | [24 Meeting to Knowledge Capture](../24-meeting-to-knowledge-capture.md) | Pulls lasting knowledge out of a meeting |
| Add | [25 Agency Decision Logger](../25-agency-decision-logger.md) | Records a decision and why |
| Ask | [38 Ask the Brain](../38-ask-the-brain.md) | Answers from your files, with the source |
| Check | [39 Brain Health Check](../39-brain-health-check.md) | Finds old, unsourced or conflicting entries |

## Start in 30 minutes

You do not need all 7 files today. Start with 5 good entries, not 100 messy ones.

1. **Company file (10 min).** No company file yet? Make one in 5 minutes on the Agency Brain page at [managedcoder.com](https://managedcoder.com). Download it, then run skill 37 and paste it in. Skill 37 turns it into `company.md`. Prefer not to use the page? Answer the 5 questions in skill 37 instead.
2. **One client (5 min).** Copy `clients/_client-template.md`. Fill in one real client. Skip fields you do not know. Write `UNKNOWN`.
3. **One policy (5 min).** Open `policies.md`. Add one rule you keep repeating, like how you handle scope changes.
4. **One decision (5 min).** After your next leadership meeting, run skill 25 and save the result in `decisions/`.
5. **Ask a question (5 min).** Paste your files into your AI with skill 38 and ask something real. Example: "What do we do when a client asks for work outside the scope?"

If the answer names the right file and date, it works. If it says "Not in the Brain", that is useful too. It tells you what to write next.

## What is in the folder

| File | What goes in it |
|---|---|
| `company.md` | Who you are, what you sell, how you talk |
| `clients/` | One file per client you want the AI to know well |
| `policies.md` | Rules you want applied the same way every time |
| `decisions/` | One entry per decision, with the reason |
| `sops/` | How a repeated job is done, step by step |
| `lessons.md` | What you learned, with a date and a source |

Files that start with `_` are templates. Copy them, do not edit them.

## Every entry has the same fields

```text
title:
summary:
source:           where this came from (meeting, email, your own words)
source_date:      YYYY-MM-DD
owner_role:       who keeps this current
status:           active | proposed | superseded | expired
confidence:       high | medium | low
review_date:      YYYY-MM-DD or none
supersedes:       none, or the title it replaces
human_review:     required | approved
```

The source and date are what make an answer trustworthy. An entry without a source is a guess.

**Confirmed or Proposed.** If you confirmed it yourself, it is `active`. If the AI or a website scan suggested it and you have not checked it, it is `proposed`. Do not treat proposed entries as company rules.

## Rhythm

- **After meetings:** run 24 or 25.
- **Weekly (5 min):** add what changed.
- **Monthly (10 min):** run 39 Brain Health Check and fix the top three items.

## Rules

- **Never put passwords, API keys or private HR notes in these files.** If the AI needs a secret, the file is wrong.
- **Use client names only if you are comfortable with that AI seeing them.** You can write "Client A".
- **Keep the files in a place you own.** A shared drive or a private folder both work. Notion users can paste each file as a page. The same fields still apply.
- **Facts change.** Pricing, team and client status go stale fast. Put a `review_date` on them.
- **The AI proposes. You decide.** Nothing here saves or sends anything on its own.

## Where to go next

Use [37 Build the Brain](../37-build-the-brain.md) to fill these files, then [38 Ask the Brain](../38-ask-the-brain.md) to use them.
