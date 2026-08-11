# Meeting to Product Roadmap Skill

## What this does

Turns a strategy meeting or set of notes about a product into three things: a plain-language vision doc, a cleaned-up task list with the stale and contradictory items archived, and new tasks that are actually grounded in what's really built — not in what an old task description claims is built.

The step most people skip is the one that matters: checking the real product before writing any task.

## When to use it

- After a strategy or direction meeting about a product or internal tool
- "The team is confused about what we're building — clean up the tasks"
- When the backlog no longer matches where the product is actually going
- When you suspect tasks in the tracker describe features that don't exist

## Setup

Works best with a PM/task connector (Asana, ClickUp, Monday.com, Linear, Jira) to pull the real task list and write updates back. A docs connector (Notion, Google Drive, Confluence) lets it file the vision doc where the team will find it.

If your product is built on a platform with an AI assistant or code search you can query, the AI can use that for the ground-truth check in Step 4. Otherwise, that step becomes a set of specific questions for you or your tech lead to answer — don't skip it either way.

No connectors? Paste the meeting notes and your current task list; you'll apply the changes manually.

## Instructions for the AI

You are turning a strategy conversation into a corrected, working backlog.

### Step 1 — Extract the vision

Read the transcript or notes closely. Pull out explicitly:

- What the product actually is — **and isn't**. Watch for strategic pivots ("this isn't a revenue product, it's free forever, the money comes from X"). These are the highest-value sentences in the whole meeting and they're easy to miss.
- The single most important near-term priority, stated plainly.
- Concrete gaps between what leadership wants and what the team has been building.
- Named people who need to be consulted on specific decisions — carry these names into the tasks later, don't lose them.
- Any conflict with an existing vision doc. Never silently overwrite a locked or approved doc — add a new dated entry and flag the conflict for a human to resolve.

Write this up as plain prose, not a slide deck.

### Step 2 — Save the vision where people will find it

Put it wherever the team actually looks: a docs connector, the project's knowledge base, a pinned page. Tag it with the meeting date, and note if it supersedes part of an older doc. A vision doc nobody can find is the same as no vision doc.

### Step 3 — Pull the real task list

Get every task on the product: title, description, status, priority, due date, assignee. If there are multiple similarly-named projects in the tracker, identify the right one by task count and recent activity, not by name match — decoy projects are common.

Sort into four buckets:
- **Done / historical** — leave alone.
- **Active and still relevant** — keep, may just need clearer language.
- **Recurring / admin** (invoices, recurring reports) — leave alone regardless of how they look; these usually have their own reasons to exist.
- **Confusing or contradictory** — candidates for archiving. The common smell: a task describing features, names, or a business model that doesn't match the product's actual build or the new vision. This is very often a copy-paste from a different product.

### Step 4 — Ground-truth against what's actually built (critical — don't skip)

Before trusting any existing task description or writing new ones, verify what really exists.

Ask specific, falsifiable questions — never "is the product done?" but "is X wired up end to end, or is it UI only?" Demand a distinction between working end-to-end, stubbed/mocked, and not started. If you have a code-search or AI assistant on the codebase, ask it directly and tell it not to make changes — only report on current state.

This step is what catches a task claiming a feature is "our primary channel" when there's zero backend code for it. Without it, you write a beautiful backlog built on fiction.

### Step 5 — Clean up the tracker

- Archive confirmed-stale tasks through the connector, and **always leave a comment explaining why**, so nobody wonders where their task went.
- Write new tasks in **small batches of 3-4**, not one giant dump. Show the drafted tasks for a quick yes/no before creating them, especially early in the session.
- Every new task must be grounded in something concrete from Step 4, written in plain language a non-technical teammate would understand, and should name the specific person to consult when the meeting named one.

### Step 6 — Ask the scale question too

Once feature gaps are covered, ask a second, separate question: given the real target usage (e.g. "50 concurrent client accounts"), what breaks first — and what's the current state of automated testing, error tracking, and monitoring?

This reliably surfaces a different class of problems (rate limits, duplicate-send risk, scheduled-job load, no admin visibility) that a feature-focused vision meeting never mentions but that matter just as much before a real rollout. Turn the answer into another small batch of tasks.

### Step 7 — Tell the team

Draft — never auto-send — an update to the people doing the work, copying their manager. One line per task with a direct link. Note what was archived and why. Run it through the Write in My Voice skill for tone.

## Worked example

**Input:** A 40-minute strategy call transcript about an internal client-portal product, plus "clean up the tasks."

**Output (excerpt):**

```
VISION EXTRACT
The portal is not a revenue product. It's a retention tool, free to all clients
forever. Revenue comes from the services it makes stickier. Near-term priority:
self-serve status visibility, so clients stop emailing for updates.
Conflict flagged: the Q1 vision doc lists "portal subscription tiers" — directly
contradicted by this meeting. Not overwriting; added a dated entry. Needs your call.

GROUND-TRUTH CHECK
Asked: "Is the notification system wired end to end?"
Answer: UI exists, no backend — notifications are mocked.
→ 3 existing tasks assume notifications work. All three are wrong.

PROPOSED — archive these 3 (with comment explaining why):
1. "Add notification preferences to billing tier" — references tiers that no longer exist
2. "QA notification digest email" — nothing to QA, feature isn't built
3. "Portal upsell copy for pro plan" — contradicts free-forever decision

PROPOSED — create these 3:
1. Build notification backend (currently UI-only) — consult Dana before scoping
2. Client-facing status page — the near-term priority from this meeting
3. Remove pricing tier references from portal UI

Create these? [waits for yes before touching anything]
```

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want your backlog checked against reality automatically, instead of once a quarter? See Agency Control Tower: controltower.collabai.software*
