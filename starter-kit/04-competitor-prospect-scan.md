# Competitor / Prospect Scan Skill

## What this does

Builds a quick research brief on a company — either a prospect about to be pitched, or a competitor you're up against — so you walk into the call prepared instead of guessing.

## When to use it

- Before a sales call, a pitch, or a renewal conversation
- Whenever you're about to compete for a deal and want to know who and what you're dealing with
- Before responding to an RFP where a competitor is also in the mix

## Setup

This is primarily a web research skill — it works with just a company name, no connector required. If you also have a CRM connector, it can pull any existing notes or past interactions with this company first, so the brief builds on what's already known rather than starting cold.

## Instructions for the AI

You are researching a company (prospect or competitor) and producing a short brief.

1. **Check for existing context.** If a CRM connector is available, look for existing notes, past deals, or contacts tied to this company name first. Then research the company on the web (name, and optionally a website or LinkedIn URL given).

2. **Produce this brief:**
   - **Company snapshot** — what they do, size (rough headcount if findable), industry, in 2-3 sentences.
   - **Likely pain points** — based on their industry, size, and any public info (job postings, recent news, site content), what problems are they probably facing that could be solved here? Label this section clearly as "likely, not confirmed" — this is an educated guess, not fact.
   - **Recent activity** — anything public in the last few months: funding news, leadership changes, product launches, layoffs. If nothing recent is found, say so plainly rather than padding with old news.
   - **If this is a competitor:** what do they seem to offer, at what apparent price point or positioning, and where does the agency look stronger or weaker by comparison? Be honest about weaker — a brief that only flatters is useless.
   - **Conversation openers** — 2-3 specific things worth mentioning on a call that show real homework was done (not generic "I saw you're growing!" lines).

3. **Apply these rules:**
   - Only state something as fact if it came from an actual source. Mark anything inferred, not confirmed, clearly as "likely" or "appears to be."
   - If little public information can be found, say that clearly instead of filling space with generic industry commentary that could apply to any company.
   - Keep the whole brief under one page — this is a scan before a call, not a research report.
   - Never fabricate a name, title, or specific number (funding amount, headcount) that isn't confident — write "unconfirmed" instead.
   - If this is a competitor scan, stay factual and fair. Avoid dismissive or unprofessional language — parts of this might end up shared with a client or partner.

## Worked example

**Input:** "Company: BrightPath Digital, they're a competitor, mid-size marketing agency in Chicago"

**Output (excerpt):**

> **Snapshot:** BrightPath Digital appears to be a mid-size (est. 20-40 person) full-service marketing agency based in Chicago, focused on paid media and web design for mid-market retail and hospitality clients.
>
> **Recent activity:** Unconfirmed — no major news found in the last few months. Their site lists a case study dated this year with a hospitality client, suggesting active work in that vertical.
>
> **Where we look stronger:** Our AI-driven ops tooling is not something their site mentions — likely a differentiator if the prospect cares about operational efficiency.
> **Where we may look weaker:** They appear to have more case studies specifically in hospitality — if the prospect is in that space, expect them to lean on that.
>
> **Conversation openers:**
> - Ask directly if they're currently evaluating BrightPath or similar Chicago-based shops
> - Reference that hospitality clients often care about turnaround speed — ask about their current timelines

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want this brief auto-generated the moment a new deal or lead lands in your pipeline? See Agency Control Tower: controltower.collabai.software*
