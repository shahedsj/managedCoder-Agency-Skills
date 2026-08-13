---
name: write-in-my-voice
description: Rewrite AI-generated or overly formal content into the owner's natural voice, and write new emails, social posts, blogs and proposals in that voice from scratch. Use whenever the user says "humanize this", "make it sound like me", "this sounds too AI", "too robotic", "fix the tone", "clean this up", "polish this", "rewrite this email/post/blog", or pastes a block of text and asks you to improve it. Also use when they say "write a LinkedIn post", "draft a post about X", "fix this post", or "make this post better" — this skill owns the rules for how a post is written. Trigger it automatically whenever a draft in the conversation reads like AI output: em dashes everywhere, buzzwords, long sentences, bullet-heavy structure.
---

# Write In My Voice

People buy from people. The moment a client reads a message that sounds like it came out of a machine, the relationship drops a notch — and they will not tell you that's why. This skill is the difference between content that gets replied to and content that gets skimmed.

> Tool placeholders like `~~email` mean whatever tool you've connected in that category. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ Paste any draft — get it rewritten in your voice           │
│  ✓ Write a post, email, or blog from a rough idea             │
│  ✓ Banned-word pass, structure fix, per-platform length cut   │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~email: read the real thread, match the existing tone     │
│  + ~~docs: pull your past writing as voice reference          │
│  + ~~CRM: pull real numbers so claims are specific, not vague │
└──────────────────────────────────────────────────────────────┘
```

## What I need from you

**One-time — your voice profile.** A few sentences is enough. How you talk, what you'd never say, and your personal quirks: some people sign lowercase, some never use exclamation marks, some keep every email under 100 words, some always open with a one-line personal note. Some people deliberately keep small imperfections in their emails — a missing comma, a casual "alot" — because it reads like a person typed it in a hurry rather than a PR machine approving it. That's a choice, not a rule. If you want it, say so and say where (emails only is the usual answer, never posts). Paste this profile at the top of the chat, or save it in your AI tool's custom instructions so it applies every time.

**Then, per job, one of these:**

**Option A — Rewrite.** Paste the draft. Say what it is (email, post, blog, proposal, chat message).

**Option B — Write from scratch.** Give me the raw idea, the audience, and any real numbers. Rough bullets are fine.

**Option C — Fix a specific thing.** "This post is too long for X." "This opener sounds like a press release."

If you haven't given me a voice profile, I use the core voice below and say so once.

## Step 1 — Identify the content type

Everything downstream depends on this. An email and a LinkedIn post get opposite treatment on length, formatting, and polish. If it's genuinely unclear, ask one question instead of guessing — guessing "blog" when it's an email produces something three times too long that the user has to rewrite anyway.

## Step 2 — The core voice

This is the default until the owner's own profile overrides it.

- Short sentences. One idea per sentence.
- Simple words. If a simpler word exists, use it.
- No fluff, no throat-clearing. Get to the point in the first sentence.
- Conversational but professional. Like a smart colleague texting you, not a consultant writing a report.
- Slightly warm. Never cold or robotic. Never performatively enthusiastic.

The reader should feel like the owner wrote this at their desk, not that a team drafted it for them.

## Step 3 — Cut first

Before rewriting a single sentence, delete everything that carries no meaning. A 400-word piece usually becomes 200 without losing anything.

This ordering matters. If you polish first, you spend effort making filler sound good and then keep it because it now reads well. Cut, then write.

## Step 4 — Remove the tells

### Banned words

Elevate, Leverage, Resonate, Unleash, Unlock, Empower, Navigate, Transformative, Innovative, Groundbreaking, Cutting-edge, Revolutionary, Synergy, Paradigm, Ecosystem, Holistic, Robust, Scalable, Streamline, Optimize, Seamless, Reimagine, Spearhead, Foster, Testament, Delve, Enrich, Beacon, Adhere, Realm, Furthermore, Profound, Supercharge, Evolve, Pivotal, Pesky, Promptly, Vibrant, Perseverance, Spontaneous, Improvise.

### Banned phrases

"I hope this finds you well", "Please don't hesitate", "Looking forward to connecting", "In today's fast-paced world", "game-changer", "best-in-class", "It's important to note", "In summary", "Dive into", "Take a dive into", "In today's digital era", "As a professional", "It goes without saying", "At the end of the day", "Moving forward", "Circle back", "Touch base", "Move the needle", "Value-add", "Deep dive", "Thought leadership".

These aren't banned because they're wrong. They're banned because they're the words a model reaches for when it has nothing specific to say. Every one of them is a place where a real fact should go.

### Banned formatting — emails and conversational content

- **Em dashes (—).** Replace with a period or a comma, or restructure the sentence. This is the single loudest AI tell in 2026.
- **Excessive bullet points.** Convert to flowing prose where possible. Bullets in an email say "I couldn't be bothered to write sentences."
- **Bold used for emphasis inside a paragraph.** If the sentence needs bold to land, the sentence is wrong.
- **Numbered lists for things that aren't sequential steps.** Numbers promise an order that isn't there.

## Step 5 — Apply the content-type rules

### Emails

- Under 150 words where possible.
- No re-introduction if you're replying on an existing thread. Re-introducing yourself tells the reader nobody read the thread.
- Personal opening tied to something real about the recipient. Not "hope you're well" — something that happened.
- One soft CTA at the end. One action only. Two asks get zero answers.
- Signature only if the owner supplied one in their profile. Never invent one.

### Social posts — LinkedIn first

This is the heart of the skill. Follow all five steps in order.

**Step A — Pick the point of view before writing a word.**

| Posting as | Voice |
|---|---|
| Personal profile | **"I"** — first person singular |
| Company page | **"We"** — first person plural |

Never mix them. A post that opens with "I" and then says "we deliver exceptional results" reads like a ghostwriter wrote it, which defeats the entire point of the post.

**Step B — The hook. The first line does most of the work.**

Only the first line shows before "see more". If it fails, nothing else in the post matters.

- **5-8 words. Count them.**
- **End with a colon or an ellipsis** so the reader has to open it.
- **A number makes it concrete.** "70 AI agents later:" beats "Lessons from our AI work:"
- **Never open with a question.** "Have you ever wondered..." gets scrolled past.
- **Never open with** "I'm excited to announce", "Thrilled to share", "Proud to". These signal a press release, and people scroll past press releases.

**Step C — Structure.**

- **One sentence per line.** Hard return between every line.
- White space is the format. A paragraph block does not get read on a phone.
- **3-8 short blocks. Under 150 words** for a standard post.
- No bullet symbols. Need a list? Use line breaks, or plain numbers at the start of a line.
- No em dashes. No bold, no italics — platforms strip them and it looks broken.
- **Max 3 hashtags**, at the very bottom, or none at all. Never inline in a sentence.

**Step D — The ending.**

End with a **specific question tied to what the post actually said.**

| Good | Bad |
|---|---|
| "Which of these have you actually seen work?" | "What do you think?" |
| "Anyone running this across 50+ clients — what broke first?" | "Thoughts?" |
| "Curious if this holds outside agencies." | "Agree?" |

Why a question at all: comments drive reach. Why it must be specific: a generic question reads as engagement bait and gets ignored, so it costs you the reach it was supposed to buy. Being specific satisfies both.

**Exception — no question needed** when the post carries a real action: a hiring post, an event registration, a launch. End with the action and the link instead. A question on top of an ask splits the response.

**Step E — No typos here.**

If the owner's profile keeps small imperfections in emails, that stops at the inbox. A post is public and permanent. Polish it.

**Length by platform.** Write the LinkedIn version first, then cut it down.

| Platform | Target |
|---|---|
| LinkedIn | Under 150 words. Hook + 3-8 blocks + question |
| X / Twitter | Under 260 characters. Keep the hook, drop the middle, keep the ask |
| Facebook | Same shape as LinkedIn, slightly warmer, contractions fine |
| Instagram caption | 2-3 short lines. The image is doing the work |

**Post types that actually land:**

- Something that happened, with a real number. "70 agents across 70 companies. What surprised me:"
- A thing you got wrong, and what changed after.
- A short client story. No client name unless it's approved.
- A plain-spoken take on a claim the industry repeats without evidence.

**Skip:** milestone congratulations, reposted news with no opinion added, motivational quotes, and anything that could have been written by any agency.

**Before it goes out — 4 checks:**

1. First line under 8 words, not a question, ends with a colon or ellipsis
2. One sentence per line, under 150 words total
3. Closing question is specific, not "what do you think"
4. No banned words, no em dashes, no typos, POV consistent throughout

### Blog articles

- Cut aggressively. Say it in half the words.
- Start with a real observation or statement, not a rhetorical question.
- Short paragraphs, lots of white space.
- Subheads every 200-300 words so it can be skimmed. Nobody reads a blog top to bottom.
- End with a clear point, not a vague invitation to comment.
- No em dashes, no banned words, no typos.

### Proposals and product descriptions

- Professional but still direct.
- Cut all filler sentences.
- Replace buzzwords with plain descriptions of what the thing actually does.
- No deliberate imperfections here, ever. This one has a price attached.
- Preserve every technical detail from the original. Losing accuracy to gain readability is a bad trade in a document someone signs.

### Chat and internal messages

- Very short. 1-3 sentences.
- Casual. No formal language at all.
- Remove corporate-speak entirely.

## Step 6 — What to keep or add

- **Short paragraphs.** 1-3 sentences max. White space is good.
- **Contractions.** "It's", "we've", "I'd", "they're". These make text feel human.
- **Real specifics.** Replace vague claims ("we deliver great results") with concrete ones ("we've deployed 70 AI agents across client teams"). Pull from context or a connected tool. Never invent a number — an invented number in a client email is worse than a vague one.
- **Direct openings.** Cut the warm-up. Start with the actual thing you're saying.
- **The owner's stated quirks**, exactly as they described them.

## Step 7 — Final pass and present

Run the banned list one more time. Buzzwords creep back in during the rewrite, especially in the last paragraph, because that's where the model runs out of substance and reaches for filler.

Then present it in this shape:

```
[The rewritten piece, clean and ready to copy]

---
What changed:
- [change 1 — only if the original was over 300 words]
- [change 2]
- [change 3]

⚠️ Before you send:
- [NEED: a real number here — I left "several clients" because I don't have the count]
- [This claim wasn't in your original. Confirm it's true before sending.]
- [Hook is 11 words. Cut to 8 or it truncates on mobile.]
```

Skip the "what changed" block on short pieces. On a 60-word email it's longer than the email.

## Rewrite, don't polish

If a sentence is fundamentally off, replace it from scratch. Don't try to save it.

This is the rule people ignore most. Polishing a bad sentence keeps its shape, and the shape is usually the problem — the AI structure survives even after every buzzword is gone, and the result still reads wrong for reasons nobody can name.

## What not to do

- Don't make it so casual it sounds unprofessional.
- Don't strip out important information to make it shorter. Cut fluff, not substance.
- Don't add new claims, numbers, or features that weren't in the original.
- Don't replace one set of buzzwords with another set of buzzwords.
- Don't add emojis unless the owner asked for them.

## Worked example

**Input:** *"make this sound like me — its a linkedin post"*

> In today's fast-paced digital landscape, it's important to note that leveraging cutting-edge AI solutions can fundamentally transform how organizations navigate their operational challenges and unlock new paradigms of efficiency. Our innovative platform offers the following key benefits:
> - **Enhanced Collaboration**: Teams work together seamlessly
> - **Robust Analytics**: Gain deep insights into performance metrics
> - **Scalable Infrastructure**: Grows with your organization's needs
>
> What do you think? Let us know! #AI #Innovation #DigitalTransformation #FutureOfWork #Tech

**Output:**

```
We put AI into 40 client teams:

Most of it didn't stick.

The tools that worked weren't the clever ones.
They were the boring ones that removed a step someone already hated.
Reporting. Status chasing. Meeting notes.

The ones that failed were the ones we were most excited about.

Which AI tool did your team quietly stop using?

#AI #Agency
```

```
What changed:
- Cut 71 words to 58. The whole first sentence said nothing.
- Killed 9 banned words: leveraging, cutting-edge, transform, navigate, unlock,
  paradigms, innovative, seamlessly, robust, scalable.
- Bullets became one sentence per line. Bold and colons stripped — the platform
  breaks them anyway.
- "What do you think" became a question only someone who read the post can answer.
- 5 hashtags down to 2.

⚠️ Before you send:
- [NEED: the real number. I wrote "40 client teams" from your last message —
  confirm before this goes public.]
- [Hook is 6 words, ends with a colon. Good.]
- [POV is "we" throughout. If this is going on your personal profile, say so
  and I'll switch it to "I".]
```

## Tips

1. **The em dash is the tell everyone can now spot.** Clients and candidates read one and quietly assume nobody looked at the message before it went out. Removing them costs nothing and buys back credibility you didn't know you were spending.
2. **Give the AI your real numbers or it will write adjectives.** "Great results" is what comes out when the model has no facts. Every vague sentence in a draft is a place where you failed to hand over a number, not a place where the AI failed.
3. **Write the post, then delete the first line.** Nine times out of ten the real hook is the second sentence, and the first one was you clearing your throat.
4. **Voice profiles beat instructions.** "Write like me" produces nothing. "I never use exclamation marks, I sign lowercase, and I hate the word 'excited'" produces your voice on the first try. Spend ten minutes writing yours once.
5. **If the rewrite is better than what you meant to say, you didn't have a point.** Go back to the idea, not the draft. No amount of voice work saves a post with nothing in it.

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want every outgoing draft, from client emails to LinkedIn posts, written in your voice before you even open the tab? See Agency Control Tower: controltower.collabai.software*
