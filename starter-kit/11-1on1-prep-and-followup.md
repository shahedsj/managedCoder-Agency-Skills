# 1:1 Prep & Follow-Up Skill

## What this does

Prepares your 1:1s with direct reports — pulling in their current workload so you're not walking in blind — and, after the meeting, helps you write up the summary and turn agreed action items into real tasks. Includes a full manager's framework: which agenda template fits which kind of 1:1, a question bank for common situations (disengaged, overloaded, wants promotion, team conflict...), and a feedback framework (Radical Candor / SBI-I) for anything that needs direct, kind feedback.

## When to use it

- Before any 1:1 with someone who reports to you — "prep my 1:1 with [name]"
- Right after a 1:1 — "log my 1:1 with [name]", "follow up on my meeting with [name]"
- A quick status check with no meeting involved — "how's [name] doing"
- Any time you need to give someone feedback and want to get the tone right

## Setup

Works best with a PM/task connector (Asana, ClickUp, Monday, HubSpot tasks, etc.) so it can check the person's current open/overdue work before you walk in. If you also have a calendar or meeting-tool connector, it can help locate and summarize the actual meeting for the follow-up step. No connectors at all? It still works — just ask the person directly what they're working on and what was discussed.

This skill intentionally does NOT use or need any HR/performance-review data — it's for the day-to-day 1:1 relationship, not a formal review process.

## Instructions for the AI

### Step 0 — Figure out which mode, before pulling anything

1. **General inquiry** — "how's [name] doing" — a quick status check, no meeting, no writes.
2. **Meeting prep** — "prep my 1:1 with [name]" — building an agenda for an upcoming 1:1.
3. **Post-meeting follow-up** — "log my 1:1 with [name]" — the meeting already happened, capture it and create follow-ups.

Skip asking if the phrasing already makes it obvious.

### Mode 1 — General Inquiry

If a PM connector is available, pull the person's open/overdue tasks and any recent trend. Answer directly — no agenda template, no task creation.

### Mode 2 — Meeting Prep

1. If a PM connector is available, pull the person's current workload (open tasks, anything overdue) so the manager isn't walking in blind.
2. Pick the agenda template that matches the situation (full templates in the Framework section below): regular check-in, career conversation, performance concern (uses SBI), or new team member (first 90 days).
3. If this 1:1 involves giving feedback, use the SBI-I model (Situation, Behavior, Impact, Intention) — see the Radical Candor section below.
4. Deliver the agenda. No writes yet.

### Mode 3 — Post-Meeting Follow-up

1. **Find the meeting content.** If a meeting-tool connector is available, use it to locate and summarize the meeting. If quality looks garbled (common with noisy or code-switched audio), say so and ask the manager to confirm rather than trusting a bad transcript. Otherwise, just ask: "what did you discuss?" — a few bullet points is enough.
2. **Propose the summary, don't assert it.** "Here's what I'd capture — anything to add or fix?" Get confirmation before treating it as final.
3. **Propose action items, never decide and create them yourself.** For each one, propose a title, due date, and priority, and wait for a yes before creating anything through a task connector.
4. For each confirmed item: set a real due date (ask what was agreed, or default urgent/high → today, medium → tomorrow, low → this Friday); set the right assignee if it belongs to the direct report, not the manager; keep the description to a clear sentence or two.
5. **Post a comment/note on the task (or wherever your PM tool logs activity) summarizing the conversation, even if there were no action items** — "just checking in" 1:1s still deserve a trail. This comment is your durable 1:1 history.
6. At the next 1:1 prep for this person, check whether these were completed before building the new agenda — that's what makes 1:1s build trust instead of feeling like status meetings.

### What NOT to do

- Don't pull or ask for engagement scores, attrition risk, or formal review data — this skill isn't for that.
- Don't guess at project IDs or workspace details — ask.
- Don't bulk-create tasks for a whole team without each person's own agreement from their own 1:1.
- Don't decide follow-up action items and create them without proposing them first — even when the conversation clearly suggests them.

---

## Framework Reference (full)

> Adapted from the open-source `jkbennemann/leadership-skills` project (Apache 2.0 License).

### Why 1:1s Matter

1:1s are the most important meeting a manager has. They are the direct report's meeting, not the manager's — about them, not status (save project updates for standups) — relationship-building time where trust compounds — and an early warning system where problems surface first.

### Principles

1. **Consistency over intensity** — weekly or biweekly, same time, never cancel. 30 min minimum, 45-60 ideal. Rescheduling is fine; canceling erodes trust.
2. **They own the agenda** — ask them to bring topics, your items come second. If they have nothing, dig deeper — that's a signal.
3. **Listen more than talk** — aim for a 70/30 ratio (them/you). Ask follow-up questions. Silence is okay.
4. **Document and follow through** — take notes, track action items, start the next 1:1 by checking the last one's items.

### Templates by Type

**Regular check-in (weekly/biweekly):** their topics first → how are you doing (energy, workload, blockers) → work check-in (what's going well/challenging, do you have what you need) → growth/development → your topics last → action items.

**Career conversation (monthly/quarterly):** reflection (what energized/drained you, proudest accomplishment) → current role (what you love, what you'd change) → future direction (1-2 year view, skills to develop) → support needed → action items.

**Performance concern:** open directly ("I want to talk about something important — I care about your success, which is why I'm raising it directly"). Use SBI: Situation, Behavior, Impact. Then ask their perspective before setting expectations. Never open with "don't take this personally."

**New team member (first 90 days):** weeks 1-2 = settling in, access, who they've met; weeks 3-4 = surprises, quick wins, pace; months 2-3 = confidence gaps, support needs, team relationship.

### Question Bank by Situation

- **Disengaged:** "You've seemed quieter lately — what's on your mind?" / "1-10, how excited are you about your work right now? What would make it a 10?"
- **Frustrated:** "Tell me more about that." / "What's the root cause?" / "Do you want me to fix it, or just listen?"
- **Wants promotion:** "What does that next level look like to you?" / "What gaps exist between here and there?" / "What can you start doing now at that level?"
- **Overloaded:** "Walk me through everything on your plate." / "What would you take off if you could?" / "Are you comfortable pushing back when asked to do more?"
- **Team conflict:** "Help me understand what's happening with [person]." / "What's your role in this dynamic?" / "Would it help if I facilitated a conversation?"
- **Top performer:** "What's keeping you here? What might make you leave?" / "Are you challenged enough?" / "What's the most interesting problem you'd want to work on?"
- **Quiet / one-word answers:** "If you had a magic wand, what would you change?" / "What's something you've wanted to say but haven't?" — consider a walking 1:1 or informal coffee instead.

### Manager Self-Check (before each 1:1)

Did I review notes from last time? Did I follow through on my own action items? Do I know what they're working on? Is there feedback I've been avoiding? Have I thought about their career lately? Am I in the right headspace to listen?

### Red Flags

Always says "everything's fine" (doesn't feel safe being honest) · never brings topics (disengaged) · frequently reschedules (avoiding something) · only talks tasks (keeping distance) · sudden mood change (personal issue or job searching) · stops asking questions (checked out) · repeats the same complaint (feels unheard).

### Anti-Patterns to Avoid

Turning it into a status meeting · talking the whole time yourself · skipping regularly · no notes · no follow-through · only meeting when there's a problem · multitasking during the meeting · rushing when they clearly have more to say.

---

## Radical Candor / Feedback Reference (full)

> Adapted from the open-source `jkbennemann/leadership-skills` project (Apache 2.0 License), based on *Radical Candor* by Kim Scott.

Radical Candor sits at the intersection of caring personally and challenging directly. High care + high challenge = growth and trust. High care + low challenge = Ruinous Empathy (nice but unhelpful, surprises at reviews). Low care + high challenge = Obnoxious Aggression (fear, defensiveness). Low care + low challenge = Manipulative Insincerity (politics, backstabbing).

**Core principles:** be humble (you might be wrong — say "I noticed," not "you always") · be helpful (their success, not venting) · be immediate (within 2-3 days, while context is fresh) · be synchronous when possible (praise in public, criticize in private) · be specific (situation, behavior, impact, not generalities).

**Feedback formula — SBI-I:**
- **Situation** — when/where did this happen? ("In yesterday's sprint review...")
- **Behavior** — what specific, observable action occurred? ("...you interrupted Maria three times while she was presenting...")
- **Impact** — what was the effect? ("...which made it hard for her to finish, and the team seemed uncomfortable.")
- **Intention** — show you care, invite dialogue. ("I know you're passionate about this — can we talk about what was going on for you?")

**Constructive feedback template:**
```
I care about your growth, so I want to share some feedback.
[Situation]: In [specific context]...
[Behavior]: I observed that [specific behavior]...
[Impact]: The effect was [concrete impact]...
I believe you can [positive framing of change]. What's your perspective? How can I support you?
```

**Example — missing a deadline.** Ruinous Empathy (avoid): "Don't worry about the deadline, I know you're busy." Radical Candor: "I noticed the migration is a week behind. I know you've had a lot on your plate. I'm concerned because it blocks the other team. What's getting in the way, and how can I help?"

**Red flags to avoid:** starting with "don't take this personally" · using "but" after praise (negates it) · feedback sandwiches (praise-criticism-praise) · "everyone thinks..." (speak for yourself) · mixing old issues with new ones · giving feedback while angry · making it about personality, not behavior.

**Green flags:** "I" statements about your own observations · specific recent examples · asking for their perspective · offering concrete support · scheduling a follow-up · acknowledging what they do well.

**Receiving feedback yourself:** listen fully without defending → thank them → ask for a specific example → say you'll think about it → follow up after you've processed it.

---

## Worked example

**Input:** "prep my 1:1 with Dana"

**Output:**
```
Mode: Meeting Prep.

Dana's current workload (from PM tool): 3 open tasks, 1 overdue ("Client renewal notes", 8 days late, no update).

This looks like a regular check-in. Suggested agenda:

## 1:1 with Dana — Aug 12
### Her topics (5-15 min) — let her lead
### How's she doing (5 min) — energy, workload, blockers
### Work check-in (5-10 min) — what's going well/challenging
### One thing to raise: the overdue renewal notes — use SBI, not a gotcha:
  "I noticed the client renewal notes were due last week and I haven't seen an update — what's going on with that one?"
### Growth/development (5 min)
### Your topics (5 min)
### Action items
```

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want your whole management team's 1:1 history and follow-ups tracked automatically, with zero manual logging? See Agency Control Tower: controltower.collabai.software*
