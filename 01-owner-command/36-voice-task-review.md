---
name: voice-task-review
description: Help an agency owner advance real tasks through a short spoken conversation, one decision at a time. Use for voice task review, hands-free task sessions, walking reviews, quick owner decisions, or requests to work through one task. Verify context, propose exact changes and record only authorized actions.
---

# Voice Task Review

Turn a short gap in the owner's day into a clear decision that unblocks work.

> Tool placeholders mean your connected systems. See [CONNECTORS.md](../CONNECTORS.md).

## How it works

| Mode | What happens |
| --- | --- |
| Standalone | Work through pasted task notes or a spoken description. Keep proposed actions in the conversation. |
| Connected | Read current tasks, comments and decision history through ~~project tracker and Agency Brain. Verify approved changes after writing. |

The skill supplies conversation rules. It does not provide background voice activation or run outside an active session.

## What I need from you

Accept one of these inputs:

1. A work area and access to your assigned tasks.
2. A pasted task with its latest comments and dates.
3. A spoken description of the work and decision needed.

Ask one question first: Which area today: delivery, sales, marketing, client success, or something else?

Accept a project, person or category instead. If the user already gave an area, use it.

## Step 1: Establish scope

Use the owner's assigned tasks in the chosen area unless they request a broader review.
Default to open tasks overdue or due today in the owner's timezone.
If none fit, ask whether to include upcoming tasks or tasks awaiting their decision.
Do not silently combine different systems or broaden the scope.

Discover the available tools and authorization before retrieval.
If retrieval fails, state that live status is unavailable and use supplied information.
Do not ask someone who is moving to inspect a screen or paste a link.

## Step 2: Choose one task

Prefer work that can advance through a 5 to 10 minute spoken decision.
Within that group, prioritize:

1. A blocked teammate with a time-sensitive client or delivery consequence.
2. A decision only the owner is authorized to make.
3. A commitment due today or already overdue.

Use the nearest verified deadline to break ties, then the oldest unanswered decision.
The 5 to 10 minute range is inherited from the source workflow. It is a selection aid, not a promised result.
Send longer or document-heavy decisions to a later review.

## Step 3: Verify before presenting

Read the description, status, due date, project, owner and latest comments.
Check completed, duplicate and superseded work before treating it as open.
Use dated operational records for status. Use Agency Brain for decision history and standing rules.
Keep missing or conflicting information explicit.
Do not invent an author, deadline or last comment.

## Step 4: Present and ask

Speak in 2 to 4 short sentences using this structure:

    [Task title]. [Why it matters now].
    [Latest comment, author and date, or no comment available].
    [One decision question].

Ask one question, then wait.
Follow skip, next, repeat, more context, recommendation and stop immediately.
Offer a recommendation only with its material uncertainty and authority limits.

## Step 5: Separate decision from action

Classify the answer as a decision, comment, reassignment, date change or completion request.
Do not treat one as permission for all the others.
Restate the exact target and proposed change before execution.
Obtain approval when that exact action is not already clearly authorized.
Never infer permission to close a task, send a message, change scope or alter production systems.

If acting through a connector, preserve existing descriptions, original deadlines and history.
Append an approved decision instead of replacing the record with a summary.
Read back the persisted result before saying Updated.
If a write fails or verification is unavailable, say so and retain the proposed text.

## Step 6: Continue or end

Offer the next task in the same area or ask whether to change areas.
On ending, distinguish decisions, verified changes, skipped tasks and pending approvals.
Do not save a session log to another system unless requested.

## Output

Keep spoken responses short. Use this written recap when requested:

    Session: [date, timezone, area]
    Decisions: [task and decision]
    Verified updates: [target, exact change, evidence]
    Pending: [proposal, approval or failed verification]
    Skipped: [task]
    Next: [one next action]

## The rules that make this work

- One task and one question at a time reduces context switching.
- Fresh status prevents reopening work already completed elsewhere.
- A decision is not a completed task. Keep acceptance evidence separate.
- Keep private client, employee and financial details out of spoken output unless necessary.
- If moving, defer complex approvals and sensitive document review until stopped.
- Use human-readable names aloud. Provide identifiers and links in a written recap if requested.
- Do not promise time savings or independent execution without evidence.

## Worked example

Fictional input: delivery. checkout blocked. last comment yesterday from delivery lead says client hasnt sent gateway credentials. due today. homepage already accepted. can we launch homepage only?

Spoken response: Checkout is blocked by missing gateway access, and the launch is due today. The delivery lead reported the missing access yesterday. Does the agreed launch scope allow the homepage to go live separately?

The owner says yes, but asks to tell the delivery lead to prepare a phased launch plan.

Proposed action: Add a comment asking the delivery lead to prepare the phased plan. Keep the launch task open and preserve its deadline. Ask for approval if this write has not already been authorized.

Without a connected tracker, report:

    Decisions: Owner supports preparing a phased launch plan.
    Verified updates: None.
    Pending: Proposed comment for delivery lead. No tracker write performed.
    Skipped: None.
    Next: Delivery lead confirms plan and acceptance conditions.

Do not claim the launch was approved for production or the task completed.

## Tips

1. Choose a decision that frees someone else to work.
2. A missing scope document is a reason to defer, not to guess aloud.
3. Respect skip without manufacturing a new deadline.
4. End with a reliable work log, not a count of tasks discussed.

*Part of the Agency Skill File Starter Kit, ManagedCoder. Connect your tracker to retrieve task context and verify approved decision updates. See Agency Control Tower: controltower.collabai.software*
