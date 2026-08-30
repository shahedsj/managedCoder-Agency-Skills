---
name: linkedin-dm-outreach
description: Write and send the actual LinkedIn outreach to one specific named person — connection request, DM, comment, or voice-note script — using a four-part formula that gets replies. Use whenever the user says "draft a LinkedIn message to [name]", "message this lead on LinkedIn", "connect with [name] on LinkedIn", "send a connection request", "comment on [name]'s post", "like this post", "engage with [name] on LinkedIn", or hands over a lead and wants the words. Also use when a text DM has gone unanswered and they're deciding what the next touch should be, when they ask whether to send a voice note, or when they paste a draft and ask if it's too salesy.
---

# LinkedIn DM Outreach

Most LinkedIn outreach fails at the first line, not the pitch. The recipient decides in two seconds whether this message was written for them or blasted to ten thousand people. This skill writes the version that survives that two seconds.

> Tool placeholders like `~~CRM` mean whatever tool you've connected in that category. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ You paste the name, connection status and one hook         │
│  ✓ Exact connection note, DM, comment, or voice script        │
│  ✓ Banned-word check + approval gate before anything sends    │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~CRM: pull the contact, tier, and last touch date         │
│  + ~~browser automation: open the profile and type the text   │
│  + ~~CRM write-back: log what was sent and when               │
└──────────────────────────────────────────────────────────────┘
```

Even with a browser automation tool connected, it only types. Approval still happens first, every single time.

**Where this sits:** this is the execution layer. For researching a contact and deciding the relationship tier before you reach out, use the **Warm Lead Outreach** skill (file 15). For who to target, profile setup, and content strategy, use the **LinkedIn Outbound Strategy** skill (file 14). This skill only handles one named person and the exact words.

## What I need from you

Four things, before I draft anything:

1. **The contact's LinkedIn profile URL** (or name, if that's all you have)
2. **Connection status** — are you already connected?
3. **Relationship tier** — knows you well / has been in touch / cold
4. **ONE specific personalization hook** — a recent post from the last 1-2 weeks, a job change, or company news

**If something is missing, I'll spend 30-60 seconds getting it myself** — open the profile, check connection status, scan recent activity for one usable hook. Thirty to sixty seconds is enough for one sharp detail, not a full bio. Past that, I'm padding, and padding is what makes messages sound researched instead of sounding personal.

If no real hook exists after that pass, I'll say so rather than inventing one.

## Rule 1 — Approval before every send

Unlike email, LinkedIn has no draft folder to save to. There's nowhere to park a message for you to review later. So the flow is: write the exact message, show it, send only after an explicit yes.

Never send a message, connection request, comment, or like without that yes. Never chain multiple sends without checking in between each one, unless you pre-approved a full batch.

## Rule 2 — No InMail, ever

Never use LinkedIn InMail — the paid messaging credits on Premium, Sales Navigator, or Recruiter.

InMails are visibly flagged as sales outreach in the recipient's inbox and get ignored almost universally. Years of spam through that channel burned the trust, and no amount of good writing gets it back. Regular DMs only, which require an accepted connection first.

## Step 1 — Connection before DM

You can only DM someone you're connected with.

**Already connected** → go straight to the formula in Step 2.

**Not connected** → draft a SHORT genuine connection request note instead. No pitch. No product mention. Just a real, specific reason to connect.

```
Enjoyed your post on [specific topic] last week — the point about
[specific detail] matched what we've been seeing. Would like to connect.
```

Getting the request accepted is the ENTIRE goal of this touch. Anything that smells like selling reduces the accept rate, and a rejected request costs you the contact for months. The DM comes later, once you're in.

## Step 2 — The DM formula

Every DM (not the connection note, which stays short and pitch-free) has four parts, built around the one specific hook:

1. **Observation** — something specific and real about their business: a post, a hire, a company change. Never a generic compliment like "congrats on the new role."
2. **Implication** — why it matters: a cost, a risk, or a missed opportunity tied to that observation.
3. **Value offer** — something useful, offered free, no strings attached. A framework, a resource, an insight from a similar situation.
4. **Low-friction ask** — exactly ONE question, binary or easy to answer.

**Bad** (generic, self-centered, stacked questions):

```
Hey [Name], congrats on the new role! I help sales teams book more meetings
through LinkedIn. Are you using Sales Navigator? What's your team's biggest
challenge? Want to hop on a call?
```

**Good** (observation → implication → value → one ask):

```
Hi [Name], saw your post last week about [specific detail], especially the
point about [specific line]. We ran into something similar with a client and
built a quick framework for it. Happy to share, no strings attached. Is that
something your team's dealing with right now?
```

The difference isn't tone. The bad one is three asks and zero evidence the sender knows who they're writing to.

### Specificity rules

Reference something concrete from the LAST 1-2 WEEKS: a specific post, a specific line in it, a hire, a company update.

**A generic compliment is WORSE than no personalization at all.** "Love what you're building" signals the message could have gone to 10,000 people, which tells the reader exactly how much thought went into it. No personalization at least reads as honest.

If no specific hook exists, say so and offer a lighter-touch option (Step 6) rather than forcing a DM. A forced DM burns the contact; a like and a real comment keeps them available.

### One question per message

Never stack questions. The single question should be:

- **Binary** — "are you using X?"
- **Clarifying** — "what's your current approach to Y?"
- **Permission-based** — "open to learning more?"

Never open-ended, never multiple-choice, never compound ("how are you handling X, and when can we chat about Y?"). Two questions get zero answers, because now replying is work and work gets deferred. Follow-up questions are for the NEXT message, after they respond.

## Step 3 — Mirror their communication style

If prior messages exist with this contact, match their pace, length, and tone.

| Their pattern | Signals | Your draft |
|---|---|---|
| Fast / casual | Short sentences, minimal punctuation, replies within minutes | Keep it short and casual |
| Slow / formal | Longer messages, full grammar, replies take a day or two | Can be longer and more polished, still specific, still ONE ask |
| No history | Nothing to read | Concise, professional-but-warm. Not stiff, not overly casual |

Mirroring isn't mimicry. It's removing the friction of a message that feels like it came from a different room than the conversation.

## Step 4 — Always close with a clear next step

Never end on "let's stay in touch." Ambiguity about who does what next kills momentum, and a warm contact with no defined next action is indistinguishable from a cold one two weeks later.

Close with a specific commitment: what happens, by when. If a call is the goal, offer TWO CONCRETE TIME OPTIONS rather than a scheduling link. A link on LinkedIn feels like outsourcing the work of aligning calendars, and at this stage of the relationship you should be the one doing that work.

```
I'll send that resource over by Friday. Want to reconnect Monday to see if
it's a fit, does 10am or 2pm work better?
```

## Step 5 — Voice and video notes: recommend, don't fake

An AI cannot record audio or video. So when one of these three situations applies, recommend the owner record it themselves:

| Situation | Threshold |
|---|---|
| Non-responder follow-up | Text DM unanswered for A WEEK OR MORE |
| Cold re-engagement | 2-3+ MONTHS since last contact |
| High-propensity prospect | Actively posting or engaging right now — a first-touch voice note stands out more than text |

Write the talking points using the same formula (observation, implication, one ask) so they have a script to read from.

Do NOT draft a text DM as a stand-in. Briefly explain why voice fits better here — higher reply rate, it signals real effort, and it builds trust faster than text because tone carries things typing can't — then let them decide. Substituting text quietly downgrades the touch and nobody notices until the reply never comes.

```
VOICE NOTE SCRIPT — [name] — approx 30 seconds

Open: [observation, the specific thing you saw]
Middle: [implication, why it costs them something]
Close: [one ask, binary]

Why voice here: [which of the three situations applies]
```

## Step 6 — Light-touch profile engagement

When a full DM isn't warranted yet, a warm-up touch works: like a recent post and leave ONE short, genuine, non-salesy comment.

This doesn't need the full formula. Just enough attention to write one honest, specific comment. Never "Great post!" — an empty comment is public, which makes it worse than an empty DM.

```
COMMENT DRAFT — on [post topic]
[one or two sentences, specific to something actually said in the post]
```

## Banned words and phrases

**Words:** Elevate, Leverage, Resonate, Unleash, Unlock, Empower, Navigate, Transformative, Innovative, Groundbreaking, Cutting-edge, Revolutionary, Synergy, Paradigm, Ecosystem, Holistic, Robust, Scalable, Streamline, Optimize, Seamless, Reimagine, Spearhead, Foster.

**Phrases:** "I wanted to reach out", "I hope this finds you well", "Please don't hesitate", "Looking forward to connecting", "In today's fast-paced world", "It goes without saying", "Excited to share", "I am writing to", "game-changer", "best-in-class".

**No em dashes, bullet points, numbered lists, bold, or italics inside the actual message text.** It should read like a real person typed it on their phone. Formatting is a tell — nobody bolds a phrase in a DM to a colleague.

## Reporting back

After anything is sent, report what was sent and to whom, so it can be logged in your `~~CRM` or lead tracker. Report what actually went out, not what was drafted — if the send failed or you only got halfway, say that.

```
SENT — [date]
To: [name] — [profile URL]
Type: [connection request / DM / comment / like]
Text: [exact text that went out]
Next: [what you committed to, and by when]
```

## Worked example

**Input:** *"draft a linkedin dm to marcus chen at that logistics co, connected already, spoke once back in march. he posted last week abt their support team drowning in tickets"*

**Output:**

```
Hi Marcus, saw your post last week about the support ticket backlog, especially
the part about your team spending more time triaging than actually solving
things.

We hit the same wall with a client last year and ended up building a triage flow
that cut their first response time in half. Happy to send over how it works, no
strings.

Is ticket volume still the main pressure point right now?
```

```
⚠️ Before you send:
- [Last contact was March. That's 5 months, past the 2-3 month cold
  re-engagement line — a voice note would likely land better than this text.]
- [I used "first response time in half" from your note. Confirm that number
  is real before it goes out.]
- [One ask only. Do not add "and are you free for a call this week."]
```

Send this as text, or record it as a voice note instead? [waits for an explicit yes before anything goes out]

## Tips

1. **The 30-60 second research limit is a feature, not a shortcut.** Ten minutes of research produces a message that sounds researched. One sharp detail from the last week produces a message that sounds like you were paying attention. The second one gets replies.
2. **If you can't find a hook, that's information.** Someone with no posts, no job change, and no company news in a month is not currently reachable on LinkedIn. Like a post, wait, or reach them another way. Forcing the DM spends the contact for nothing.
3. **The connection note is not a mini-pitch.** The only job it has is getting accepted. Every word about what you sell lowers the accept rate, and you cannot DM someone who declined you.
4. **Two questions get zero answers.** This is the rule people break most and notice least, because the reply that never arrives doesn't explain why.
5. **Never send two messages in a row without a reply.** A second unanswered DM is the moment you become someone who sends unanswered DMs. Switch channels or switch format instead.

---
*Free next step: join a live class and get the weekly AI-for-agencies newsletter at managedcoder.com*

*Part of the Agency Skill File Starter Kit — ManagedCoder. Want every lead researched, hooked, drafted, and queued for one-click approval instead of you opening profiles one at a time? See Agency Control Tower: controltower.collabai.software*
