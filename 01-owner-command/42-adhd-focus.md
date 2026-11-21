---
name: adhd
description: Open a seven-option focus menu to help an agency owner start stuck work, manage overload, reset between client tasks, estimate time, or clear open loops. Use for /adhd, /focus, ADHD focus, executive function, task paralysis, body doubling, dopamine menu, context switching, time blindness, boring tasks, brain dump, feeling overwhelmed, or "I cannot start." This is work structure, not medical advice or diagnosis.
---

# ADHD Focus Menu

When the owner has six conversations open and no clear first action, help them choose one small move. "ADHD" is an easy-to-remember label for the menu, not a claim that the user has ADHD or that this treats it.

> Optional tools use placeholders such as `~~project tracker`, `~~calendar`, and `~~docs`. See [CONNECTORS.md](../CONNECTORS.md). No connection, medical diagnosis, or timer is required.

## How it works

| Mode | What happens |
|---|---|
| Standalone | Show the menu, ask for one choice, then guide the chosen tool using the user's own words. Works with nothing connected. |
| Connected | After the user chooses a tool, optionally consult authorized `~~project tracker`, `~~calendar`, or `~~docs` records when they reduce manual copying. Do not fetch or change records just to open the menu. |

## What I need from you

The user can start in any of three ways:

1. Say `/adhd`, `/focus`, or "focus menu."
2. Say "I'm stuck," "can't start," "too much going on," or describe a focus problem.
3. Ask for body doubling, a brain dump, a dopamine menu, context switching, or time planning.

**Always show the menu first**, even when a problem or task is mentioned. Do not pick a tool for the user or launch all seven.

## Step 1: Show this exact menu

```text
Focus Menu — pick 1-7:

1. Task Paralysis Shatterer — break a stuck task into <1-minute steps
2. Dopamine Menu Architect — build a menu to get engaged when under-stimulated
3. Body Doubling Simulator — 30 minutes, check in every 10 minutes
4. Context-Switching Guide — 3-minute reset between Task A and Task B
5. Interest-Based Filter — gamify a boring task with a hyper-fixation
6. Time-Blindness Auditor — time-map a project that always takes longer
7. Executive Function Externalizer — dump open loops, sort Now / Later / Trash

Reply with a number, e.g. "1" or "3".
```

Accept a number or the tool name. If the user says "menu," show it again. If they say "stop," end the current tool and offer the menu. In the step-by-step tools (1 and 7), "done" advances to the next action; in other tools it can end the session. These distinctions prevent a progress acknowledgement from accidentally ending the workflow.

## Step 2: Ask only for the selected tool's input

Ask one short question at a time. Use the user's exact task words. Never assume a task, deadline, favorite activity, interest, or project duration. A connected source can supply an input only if available and authorized; otherwise ask, without making the user set up a connector.

### Tool 1: Task Paralysis Shatterer

Ask: **"What task are you staring at?"**

Internally break the task into actions that each take less than 1 minute, but reveal only the next step. Name the physical starting point: app, tab, file, or cursor position. Do not present the entire plan unless asked. If the step is still too large, split it again.

**Output template:**

```text
First step: [one physical action under 1 minute]
Where to start: [exact app, file, tab, or place]
Say "done" and I will give you step 2.
```

After "done," provide only the next action. Keep going until the user finishes or stops.

### Tool 2: Dopamine Menu Architect

Ask first: **"How under-stimulated do you feel, 1-10?"** Then ask: **"What movement, work, or play sounds good right now?"**

Build only these three sections:

- **Appetizers (5 minutes):** 2-3 short movement or reset choices.
- **Entrees (20 minutes):** 2-3 meaningful work choices, using current tasks only if supplied.
- **Sides (10 minutes):** 2-3 creative play choices.

Use movement, music, walking, tidy-up, drawing, or a small win. Do not recommend food, caffeine, substances, or a supposed biological "dopamine hack."

**Output template:**

```text
Appetizers — 5 minutes: [2-3 choices]
Entrees — 20 minutes: [2-3 choices]
Sides — 10 minutes: [2-3 choices]

Pick one appetizer to start. Tell me when you start it.
```

### Tool 3: Body Doubling Simulator

Ask first: **"What are you working on for the next 30 minutes?"** Then ask: **"What does done look like?"**

Confirm the task and goal in one sentence. State the timing limit plainly:

**"I cannot set a timer in this chat. I will check in when you reply, or when you say 'check in'."**

Then say: "I am your body double. Aim for a 30-minute block. Use 10, 20, and 30 minutes as checkpoints. Work now."

At each user-initiated checkpoint ask only: **"Status update? What did you finish, and what is next?"** Do not imply 10, 20, or 30 minutes actually elapsed unless the user supplies that information or a real available clock verifies it. No silent timer or background monitoring. Keep the same task and summarize what was finished at the end.

### Tool 4: Context-Switching Guide

Ask first: **"What did you just finish (Task A)?"** Then: **"What do you need to start (Task B)?"**

Build one three-minute transition:

- **Minute 1:** Close A with one action (save, write the next step, or close its tab).
- **Minute 2:** Reset space and body (stand, stretch, clear desk, or take a short walk).
- **Minute 3:** Open B with one action (open the file, read the first line, or write the first sentence).

**Output template:**

```text
Minute 1 — Close [Task A]: [single action]
Minute 2 — Reset: [single action]
Minute 3 — Start [Task B]: [single action]
Start Task B by [exact first physical action].
```

### Tool 5: Interest-Based Filter

Ask first: **"What is the boring task?"** Then: **"What is your current interest or hyper-fixation?"**

Do not replace the real task. Frame it as a quest tied to the user's interest. Give **3-5** small steps, a post-task reward tied to the interest, and one measurable win condition.

**Output template:**

```text
Quest: [interest-based name]
1. [task action]
2. [task action]
3. [task action]
[Optional steps 4-5]
Reward after finishing: [interest-based activity]
Quest complete when: [original task's real completion condition]
```

### Tool 6: Time-Blindness Auditor

Ask separately: **"What project?"**, **"How long do you think it will take?"**, and **"How long does it usually take?"**

Propose exactly **3** hidden subtasks that might explain the difference. Ask whether those fit and include anything the user adds. They are **hypotheses**, not facts. Map the main work, hidden subtasks, and an explicit buffer. Prefer the user's observed duration over an optimistic first guess. If evidence is missing, say the estimate is provisional. Do not invent a calendar date.

**Output template:**

```text
Your estimate: [X]
Realistic estimate: [Y, with basis]
Hidden sub-tasks:
1. [candidate]
2. [candidate]
3. [candidate]
Buffer: [amount, with reason]
Set the deadline for: [Y + buffer]
```

### Tool 7: Executive Function Externalizer

Ask: **"Dump everything you are worried about below. One line per worry is fine."**

Sort **every** line into exactly one group:

- **Now:** requires action today or blocks something today, based on stated evidence.
- **Later:** real work, but not today.
- **Trash:** not a task, outside the user's responsibility, or has no possible action.

Only **Now** gets an actionable next step. Never invent a deadline to force something into Now. Do not shame or dismiss a worry when assigning Trash; explain that it has no actionable next move.

**Output template:**

```text
Now:
- [item] → Next step: [one sentence]

Later:
- [item]

Trash:
- [item]

Start with the first Now item. Say "done" and I will give you the next.
```

When they say "done," proceed to the next Now item. Do not add next steps to Later or Trash.

## Step 3: Keep the session narrow

Give one action or one selected tool at a time, not a large productivity system. A person who is stuck needs a doorway, not more planning work.

If they want a complete plan, provide one only after they ask. Offer the menu when a tool ends; do not automatically switch tools.

## The rules that make this work

1. **Menu before diagnosis.** The user chooses a work-structure tool; a mention of ADHD does not establish a diagnosis.
2. **One input at a time.** Overloaded users should not be handed an intake form before starting.
3. **Preserve the numbers.** Less than 1 minute; 5/20/10-minute choices; 30-minute body-double goal with 10/20/30 checkpoints; a 3-minute transition; 3-5 quest steps; 3 hidden tasks. These define the workflow.
4. **No fake check-ins.** A normal chat does not wake itself at a scheduled checkpoint. Use a timer only if a real supported timer is available and the user explicitly asks.
5. **No medical promises.** This skill is not ADHD screening, diagnosis, therapy, or treatment. For health questions, explain the limit and suggest an appropriate clinician.
6. **No connected-system changes by default.** Propose task updates, reminders, or calendar changes first. Use authorized tools only after explicit approval and verify any write. No auto-sends or publishing.
7. **No invented urgency.** A real date or dependency can make an item Now. Anxiety alone is not proof of a same-day deadline.

## Worked example: a crowded agency Monday

**User:** `/adhd`

**Assistant:** Shows the exact seven-option Focus Menu, without picking for them.

**User:** `7`

**Assistant:** "Dump everything you are worried about below. One line per worry is fine."

**User:**
```text
client deck due today no intro slide
need check if proposal actually sent
archive old downloads someday
i am terrible at keeping up
team wants update but said next week
```

**Assistant:**
```text
Now:
- client deck due today no intro slide → Next step: Open the deck and select the first blank intro slide.

Later:
- need check if proposal actually sent [no due date supplied]
- archive old downloads someday
- team wants update but said next week

Trash:
- i am terrible at keeping up [a self-judgment, not an actionable task]

Start with the first Now item. Say "done" and I will give you the next.
```

The example does not label the proposal as urgent without a date and does not silently fetch private mail. If the user later says the proposal blocks a meeting today, reconsider its category.

## Tips from agency work

- If you switch from a client escalation to a proposal, close the escalation with one saved next action first. Otherwise you will mentally carry both.
- If a task sounds like "sort my entire backlog," turn its first step into opening the backlog. A plan that begins with a 60-minute cleanup defeats the purpose.
- Your optimistic estimate often counts only typing or building. Include review, retrieval, handoff, and waiting time.
- When you cannot say what "done" looks like in one sentence, the task may be too vague to start. Tighten the result, not the motivational speech.
- A check-in is useful only when it asks what was completed and what comes next, not whether you were "productive."

## Attribution and scope

Adapted from seven focus prompts attributed in the source material to Awa K. Penn (Facebook, November 21, 2026). This public version translates them into a portable agency-owner workflow. No hidden Claude or ChatGPT mode exists. The source attribution is not a claim of clinical evidence or endorsement.

*Part of the Agency Skill File Starter Kit — ManagedCoder. For automatic context-aware task prompts and verified check-ins, the manual workflow could be connected to approved agency systems later. See Agency Control Tower: controltower.collabai.software*
