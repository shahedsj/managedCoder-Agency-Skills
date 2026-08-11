# LinkedIn DM Outreach Skill

## What this does

Writes the actual LinkedIn message to a specific person — connection requests, DMs, and profile comments — using a formula that gets replies instead of getting ignored. Covers when to send a voice note instead of text, how to mirror someone's communication style, and the one rule most people get wrong: never stack questions.

This is the execution layer. For overall LinkedIn strategy (who to target, profile setup, content), use the LinkedIn Outbound Strategy skill in this kit. For researching a contact before reaching out, use the Warm Lead Outreach skill.

## When to use it

- "Draft a LinkedIn message to [name]"
- "Send a connection request to [name]"
- "Comment on [name]'s post" / "engage with [name] on LinkedIn"
- Any time you have a specific named person and need the actual words

## Setup

No connector required — you'll paste the drafted message into LinkedIn yourself. LinkedIn has no API for personal messaging, so this skill writes the exact text and you send it.

If you have a browser automation tool connected, it can open the profile and type the message for you, but the approval rule below still applies: nothing goes out without you seeing it first.

## Instructions for the AI

You are writing LinkedIn outreach for a specific, named contact.

### What you need before drafting

1. The contact's LinkedIn profile URL or name
2. Whether the owner is already connected to them
3. Relationship tier — knows well / has been in touch / cold
4. One specific personalization hook: a recent post (last 1-2 weeks), a job change, or company news

If any of this is missing, ask. If a hook genuinely doesn't exist, say so rather than inventing one.

### Rule 1 — Approval before every send

LinkedIn has no draft folder. So: write the exact message, show it to the owner, and only send after they say go. Never send a message, connection request, comment, or like on someone's behalf without explicit approval first. Never chain multiple sends without checking in between each one, unless the owner approved a full batch in advance.

### Rule 2 — No InMail, ever

Never use LinkedIn InMail (the paid messaging credits on Premium, Sales Navigator, or Recruiter). InMails are visibly flagged as sales outreach in the recipient's inbox and get ignored almost universally — years of spam through that channel burned the trust. Regular DMs only, which require an accepted connection first.

### Step 1 — Connection before DM

You can only DM someone you're connected with.

- **Already connected** → go to Step 2.
- **Not connected** → draft a short, genuine connection request note instead. No pitch, no product mention, just a real specific reason to connect ("Enjoyed your post on X," "We were both at [event]"). Getting the request accepted is the entire goal of this touch. The DM comes later.

### Step 2 — The DM formula

Every DM (not the connection note, which stays short and pitch-free) has four parts, built around the one specific hook:

1. **Observation** — something specific and real about their business: a post, a hire, a company change. Never a generic compliment like "congrats on the new role."
2. **Implication** — why it matters: a cost, risk, or missed opportunity tied to that observation.
3. **Value offer** — something useful, free, no strings attached (a framework, a resource, an insight from a similar situation).
4. **Low-friction ask** — exactly one question, binary or easy to answer.

**Bad** (generic, self-centered, stacked questions):
> "Hey [Name], congrats on the new role! I help sales teams book more meetings through LinkedIn. Are you using Sales Navigator? What's your team's biggest challenge? Want to hop on a call?"

**Good** (observation → implication → value → one ask):
> "Hi [Name], saw your post last week about [specific detail] — especially the point about [specific line]. We ran into something similar with a client and built a quick framework for it. Happy to share, no strings attached. Is that something your team's dealing with right now?"

**Specificity rules:** reference something concrete from the last 1-2 weeks. A generic compliment is worse than no personalization at all — it signals the message could have gone to 10,000 people. If no specific hook exists, say so and offer a lighter-touch option (Step 5) instead of forcing a DM.

**One question per message.** Never stack. The single question should be binary ("are you using X?"), clarifying ("what's your current approach to Y?"), or permission-based ("open to learning more?"). Never open-ended or compound. Follow-up questions come in the next message, after they reply.

### Step 3 — Mirror their communication style

If prior messages exist with this contact, match their pace, length, and tone:
- **Fast/casual** (short sentences, minimal punctuation, quick replies) → keep it short and casual.
- **Slow/formal** (longer messages, full grammar, replies take a day or two) → slightly longer and more polished, but still specific, still one ask.

No history? Default to concise and professional-but-warm. Not stiff, not overly casual.

### Step 4 — Always close with a clear next step

Never end on "let's stay in touch" — ambiguity about who does what next kills momentum. Close with a specific commitment: what happens, by when. If a call is the goal, offer two concrete time options rather than a scheduling link — a link on LinkedIn feels like outsourcing the work of aligning calendars.

> "I'll send that resource over by Friday. Want to reconnect Monday to see if it's a fit — does 10am or 2pm work better?"

### Step 5 — Voice and video notes: recommend, don't fake

An AI can't record audio or video. When one of these applies, recommend the owner record it themselves:

- **Non-responder follow-up** — a text DM went unanswered for a week or more
- **Cold re-engagement** — 2-3+ months since last contact
- **High-propensity prospect** — actively posting right now; a voice note stands out more than text

Write the talking points using the same formula (observation, implication, one ask) so they have a script. Don't draft a text DM as a stand-in — briefly explain why voice fits better here (higher reply rate, signals real effort) and let them decide.

### Step 6 — Light-touch profile engagement

When a full DM isn't warranted yet, a warm-up touch works: like a recent post and leave one short, genuine, non-salesy comment. Doesn't need the full formula — just enough attention to write one honest, specific comment. Never "Great post!"

### Banned words and phrases

Keep messages free of: Elevate, Leverage, Resonate, Unleash, Unlock, Empower, Navigate, Transformative, Innovative, Groundbreaking, Cutting-edge, Revolutionary, Synergy, Paradigm, Ecosystem, Holistic, Robust, Scalable, Streamline, Optimize, Seamless, Reimagine, Spearhead, Foster.

And: "I wanted to reach out," "I hope this finds you well," "Please don't hesitate," "Looking forward to connecting," "In today's fast-paced world," "It goes without saying," "Excited to share," "I am writing to," "game-changer," "best-in-class."

No em dashes, bullet points, numbered lists, bold, or italics inside the message text. It should read like a real person typed it on their phone.

## Worked example

**Input:** "Draft a LinkedIn DM to Marcus Chen at Halden Group. Connected already, Tier 2 — we spoke once in March. He posted last week about their support team drowning in ticket volume."

**Output:**

```
Hi Marcus, saw your post last week about the support ticket backlog — the part
about your team spending more time triaging than actually solving things stuck
with me.

We hit the same wall with a client last year and ended up building a triage flow
that cut their first-response time in half. Happy to send over how it works, no
strings.

Is ticket volume still the main pressure point right now?
```

Send this? [waits for approval before anything goes out]

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want your outreach drafted, tracked, and followed up automatically across every channel? See Agency Control Tower: controltower.collabai.software*
