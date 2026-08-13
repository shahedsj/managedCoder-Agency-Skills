---
name: meeting-to-product-roadmap
description: Turn a strategy meeting, transcript, or set of notes about a product into an updated vision doc AND a corrected task list — stale tasks archived with reasons, new tasks grounded in what's actually built. Use whenever the user says "update our vision for [product]", "here's a meeting, update the plan", "the team is confused, clean up the tasks", "review the tasks and align them to this vision", "our backlog doesn't match where we're going", or uploads a meeting transcript about product direction and wants follow-through. Also use when they suspect tasks in the tracker describe features that don't exist, or when a product just pivoted and nobody has told the backlog.
---

# Meeting to Product Roadmap

A strategy meeting changes the product. The backlog doesn't hear about it. Six weeks later the team is still building the old plan, and everyone assumes someone else updated the tasks.

This runs the full loop: vision out of the meeting, tasks checked against the real build, stale work archived with a written reason, new work created in small approved batches.

> Tool placeholders like `~~project tracker` mean whatever tool you've connected in that category. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ Paste the transcript + your current task list             │
│  ✓ Vision extract, 4-bucket task sort, archive/create plan   │
│  ✓ The ground-truth questions written out for your tech lead │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~project tracker: pull real tasks, archive + create back  │
│  + ~~docs: file the vision where the team already looks       │
│  + ~~meeting notes: pull the transcript directly              │
│  + build platform AI/code search: answer Step 4 for real      │
└──────────────────────────────────────────────────────────────┘
```

## What I need from you

**Option A — Connected.** "Here's the meeting for [product], update the plan." I'll pull the tasks.

**Option B — Paste.** The transcript or notes, plus an export of the current task list (title, description, status, assignee, due date).

**Option C — Notes only.** Paste the meeting. I'll produce the vision doc and the exact questions to ask before anyone touches the backlog.

## Step 1 — Extract the vision

Read the transcript closely. Pull out **explicitly**:

**What the product actually is — and what it isn't.** Watch hard for strategic pivots. The pattern to hunt for: *"this is not a revenue product, it's free forever, the real money comes from X."* Sentences like that are the highest-value lines in the whole meeting and the easiest to miss, because they're usually said once, in passing, in the middle of a tangent. Everything downstream — pricing tasks, upsell copy, tier logic — is either validated or invalidated by that one sentence.

**The single most important near-term priority, stated plainly.** One thing. If the meeting named three, ask which one ships first rather than recording all three as equal.

**Concrete gaps between what leadership wants and what the team has been building.** Name them as gaps, not as complaints.

**Named people who need to be consulted for specific decisions.** Write down the name next to the decision. Carry these names into the tasks in Step 5 — this is where they get lost, and a task that says "consult someone about pricing" is a task nobody does.

**Any conflict with an existing locked or older vision doc.** Never silently overwrite a locked doc. Add a **new dated entry** and flag the conflict for a human to resolve. Why: a locked doc was locked by someone, for a reason you weren't in the room for. Overwriting it makes the disagreement invisible — and an invisible disagreement gets rebuilt into the product three months later.

Write the vision as **plain prose, not a slide deck.** Bullets let you skip the connective reasoning; prose forces you to state why the pivot follows from the facts, which is the part the team actually needs.

## Step 2 — Save it where people will actually find it

File it in the place the team already opens: `~~docs`, the product's knowledge base, a pinned page in `~~project tracker`. Not a new folder you just invented.

Tag it with **the meeting date** and note explicitly if it supersedes part of an older doc — which part, and which doc. A vision doc nobody can find is the same as no vision doc, and two undated vision docs are worse than one.

## Step 3 — Pull the real task list

Get every task on the product: title, description, status, priority, due date, assignee, category.

**Find the right project by task count and recent activity — not by name match.** Multiple decoy projects with similar names are normal: an old archived version, a template copy, a "v2" someone made and abandoned. The one with 60 tasks and activity this week is the real one. The one with 4 tasks from last year is not. Confirm the count with the user before touching anything.

Sort every task into **four buckets**:

| Bucket | What's in it | What you do |
|---|---|---|
| **Done / historical** | Completed, closed | Leave alone entirely |
| **Active and still relevant** | Matches the new vision | Keep — may need simpler language |
| **Recurring / admin** | Invoices, recurring reports, standing check-ins | **Leave alone regardless of how they look** |
| **Confusing or contradictory** | Doesn't match the build or the new vision | Candidates for archiving |

**On recurring/admin: leave them alone even when they look wrong.** A monthly invoice task with no description and no due date looks exactly like dead weight. It usually has its own reason to exist that predates you — a compliance need, a client agreement, somebody's memory aid. Archiving one costs real money and buys nothing.

**The smell test for bucket four:** a task describing features, agent names, component names, or a business model that doesn't match the product's actual live build or the new vision. This is very often a straight copy-paste from a sibling product's playbook — someone duplicated a project to save time and never rewrote the contents. Suspicious, but not proof. Confirm in Step 4 before archiving anything.

## Step 4 — Ground-truth against the real build (critical — don't skip)

Before trusting any existing task description, and before writing a single new one, verify what actually exists.

**First, read the product's own docs and instructions.** Whatever the build platform holds — the project's own instruction file, README, or knowledge base. These are frequently more current than any external notes, the meeting transcript, or the tracker, because they're maintained by whoever is actually shipping.

**Then ask specific, falsifiable questions.** Not "is the product done?" — that gets you an opinion. Ask things that can only be answered yes or no by looking at the code:

- "Is [feature] wired up end to end, or is it UI and marketing copy only?"
- "Which [components/agents/integrations] actually exist by name, and which are named in the docs but not built?"
- "What happens when a user does [action] today — what real code runs?"

Three instructions to include every time you ask:
1. **Do not write code.** Answer only.
2. **Answer from the current state**, not from what's planned.
3. **Flag each item as STUBBED/MOCKED or WORKING END-TO-END.** Force the distinction — "it's there" is the answer that ruins the whole exercise.

**If your product is built on a platform with an AI assistant or code search you can query, ask it directly.** If not, these become specific questions for the user or their tech lead. Either way, do not skip the step — the questions are the value, the tool is just the delivery.

**What this catches:** a task claiming a feature is "the primary channel" when there's zero backend code for it. A task listing component names that don't exist anywhere in the build. Without this step, you write a beautiful, confident backlog built entirely on fiction — and it reads fine, which is why nobody catches it.

## Step 5 — Clean up the tracker

**Archive confirmed-stale tasks, and always leave a comment explaining why.** One line: what it claimed, what Step 4 found, which meeting decided otherwise. Someone will look for that task. A silent archive turns into a Slack thread, a re-created duplicate, and a small loss of trust in the tracker itself.

**Write new tasks in small batches of 3-4, never a giant dump.** Show the drafted task details — title, description, assignee, due date — for a quick yes/no before creating anything. Especially early in a session, when you're still calibrating to how this person writes tasks. Twenty tasks created at once means twenty tasks reviewed by nobody.

**Every new task must:**
- Be grounded in something concrete from Step 4 — a specific gap that was confirmed, not assumed
- Be written in plain language a non-technical team member would understand
- **Name the specific person to consult** when the meeting named one. "Check with [name] before scoping the pricing display" — the name from Step 1, carried all the way through

## Step 6 — Ask the scale question too

Once the feature gaps are covered, do **not** stop. Ask a second, separate question with the real target usage in it:

> "Given [50 concurrent client businesses] using this at once — what breaks first? And what's the current state of automated testing, error tracking, and monitoring?"

Same rules as Step 4: no code, current state only, flag stubbed vs. working.

This consistently surfaces a **different class of issues** than the feature conversation: rate limiting, duplicate-send risk, scheduled-job load at volume, no admin visibility when something fails at 2am. A vision meeting never mentions any of it — the room is talking about what the product does, not what happens when 50 people do it simultaneously. And it matters just as much before a real rollout.

Turn the answer into another small batch of 3-4 tasks, approved the same way.

## Output

```
VISION EXTRACT — [product] — meeting [date]
What it is: [plain prose]
What it is NOT: [the pivot line, quoted if possible]
Near-term priority #1: [one thing]
Gaps (leadership wants → team is building): [list]
People to consult: [name] on [decision]
⚠️ Conflict with [existing doc]: [what contradicts]. Not overwritten —
   dated entry added. Needs your call.

TASK SORT — [project name], [n] tasks (matched by count + activity, not name)
Done/historical: [n] — untouched
Active + relevant: [n] — kept
Recurring/admin: [n] — untouched by rule
Confusing/contradictory: [n] — see below

GROUND-TRUTH CHECK
Read first: [product's own docs/instructions]
Asked: "[falsifiable question]"
Answer: [WORKING END-TO-END / STUBBED / NOT STARTED] — [detail]
→ [n] existing tasks assume otherwise

PROPOSED — archive [n] (comment on each):
1. "[task]" — [why: what it claims vs. what's real]

PROPOSED — create batch 1 of [n] (3-4 max):
1. [Title] — [plain-language description]. Consult [name].
   Assignee: [x] | Due: [date]

Create these? [waits for yes]

SCALE CHECK — target: [real usage number]
Breaks first: [answer]
Testing / error tracking / monitoring today: [answer]
PROPOSED — create batch 2: [3-4 tasks]

TEAM UPDATE — DRAFT ONLY
[one line per task + link] · Archived: [n] and why
```

## The rules that make this work

**Never overwrite a locked doc — date and flag instead.** The lock records a decision made by people who were in a room you weren't in. Making the disagreement visible is the entire job here.

**Confirm before archiving, not after.** Archived work is recoverable in most trackers, but the goodwill isn't. Someone spent an hour writing that task.

**A task's description is not evidence.** It's a claim made on the day it was written, by someone who may have been copying from another product. Step 4 is the only evidence.

**Batches of 3-4, with approval.** Not politeness — a review threshold. Past four items, humans approve the batch instead of the tasks.

**Draft, never send.** Every message, every email, every bulk archive gets shown first. Bulk-editing the wrong project's tasks is not recoverable by apology, and Step 3 exists precisely because picking the wrong project is easy.

## Worked example

**Input:** *"heres the call from tues about the client portal thing, 40 min. team is confused, tasks are a mess, can you clean it up"* — plus a tracker export.

**Output (excerpt):**

```
VISION EXTRACT — Client Portal — meeting Aug 5
What it is NOT: "look, the portal is not a revenue product. it's free forever
for every client. the money is the services it makes stickier." — said once,
21 minutes in, never repeated.
Near-term priority #1: self-serve status visibility, so clients stop emailing
for updates.
People to consult: [PM name] before any scoping on notifications.
⚠️ Conflict: the Q1 vision doc (locked) lists "portal subscription tiers."
   Directly contradicted. Not overwritten — dated entry added. Needs your call.

TASK SORT — "Client Portal" (61 tasks, active this week)
   Note: 3 similarly-named projects found. "Portal v2" had 4 tasks, none since
   March — decoy, ignored.
Recurring/admin: 5 (monthly invoice, biweekly report) — untouched by rule

GROUND-TRUTH CHECK
Read the portal's own instruction file first — more current than the tracker.
Asked: "Is the notification system wired end to end, or UI only?"
Answer: STUBBED — UI renders, no backend, no send path.
→ 3 tasks assume notifications work. All 3 are wrong.

PROPOSED — archive 3 (with comment):
1. "Add notification preferences to billing tier" — tiers no longer exist per Aug 5
2. "QA notification digest email" — STUBBED, nothing to QA
3. "Portal upsell copy for pro plan" — contradicts free-forever decision

PROPOSED — create batch 1 of 2:
1. Build the notification send path (UI exists, backend does not).
   Consult [PM name] before scoping.
2. Client-facing status page — the #1 priority from this meeting.
3. Remove pricing-tier references from the portal UI.

Create these? [waits]
```

Then the scale question, separately: at 50 concurrent client businesses, the answer came back as no rate limiting on the digest job and no error tracking at all — three tasks nobody in the meeting mentioned.

## Tips

1. **The pivot sentence is said once and never repeated.** Nobody announces a strategy change twice. Read for the line that quietly makes half the backlog wrong, and quote it verbatim in the vision doc so it can't be re-litigated from memory.
2. **If the ground-truth check contradicts nothing, you asked bad questions.** A real backlog always has some fiction in it. Zero findings means you asked "is it done?" instead of "what code runs when a user clicks this?"
3. **The scale question is the one that saves a launch.** Feature gaps get caught eventually by users complaining. A scheduled job that double-sends to 50 client lists gets caught by the client.
4. **Archive comments are for a person six weeks from now, not for the log.** Write them so the assignee reads it once and stops looking.
5. **If the meeting named three top priorities, it named zero.** Go back and ask which ships first. A roadmap built on three number-ones just moves the prioritisation problem onto whoever picks up the tasks.

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want your backlog checked against what's actually built every time the plan changes, instead of once a quarter? See Agency Control Tower: controltower.collabai.software*
