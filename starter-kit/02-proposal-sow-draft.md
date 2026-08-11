# Proposal / SOW Draft Skill

## What this does

Takes discovery call notes or a summary of what a prospect wants, and drafts a first-pass proposal or scope of work (SOW) that's ready to edit and send — instead of you starting from a blank template every time.

## When to use it

- Right after a discovery call, while the details are still fresh — before the prospect goes cold waiting on a proposal
- When a prospect asks "can you send something over" and you need a first draft fast
- Any time you're scoping a new project and want the deliverables broken out clearly before you price it

## Setup

Works well with a CRM connector (HubSpot, Pipedrive, GoHighLevel, Close, etc.) so it can pull the deal's notes and any logged call summary directly. If you also have a meeting-tool connector (Zoom, Google Meet, etc.), it can pull the actual call transcript instead of relying on notes.

No connector yet? Paste the discovery call notes or a description of what the prospect wants — it still works the same way.

## Instructions for the AI

You are drafting a first-pass proposal from discovery information.

1. **Get the material.** If a CRM connector is available, pull the deal's notes and logged call summary. If a meeting-tool connector is available, pull the transcript. Otherwise, use whatever the owner pastes in.

2. **Draft the proposal in this structure:**
   - **Project summary** — 2-3 sentences restating what the client wants, in their words as much as possible. This shows they were heard.
   - **Scope of work** — broken into clear phases or deliverables (e.g. Discovery, Design, Build, Launch, Support). Under each phase, list the concrete deliverables, not vague activities. "3 homepage design concepts," not "design work."
   - **What's out of scope** — a short, plain list of things that were discussed but are NOT included, so there's no confusion later. If nothing was discussed as out of scope, skip this section rather than inventing exclusions.
   - **Timeline** — phase-by-phase estimate. Use ranges ("2-3 weeks"), not false-precise dates, unless exact dates were given.
   - **Investment** — leave exact numbers as a placeholder like [FEE] unless a number was given. Never invent pricing.
   - **Assumptions** — anything being assumed to be true (client will provide content by X, client has an existing brand guide, etc.). This protects the agency if scope creeps later.
   - **Next steps** — one short paragraph on what happens after the client approves (kickoff call, contract, deposit).

3. **Apply these rules:**
   - This is a FIRST DRAFT to edit, not a final send. Flag anything uncertain with [CONFIRM: ...] instead of guessing.
   - Keep deliverables concrete and countable wherever possible (a number of pages, revisions, deliverables) — vague scope is how projects go over budget.
   - Match the tone of the proposal to the deal size: a $3K project proposal should read simpler and shorter than a $50K enterprise one. Ask for the deal size if it's not obvious from the notes.
   - Never promise a timeline or price that wasn't in the notes or explicitly given.
   - If the notes mention a pain point or a "why now," open the project summary with that — it's the strongest hook in the whole document.

4. **Deliver the draft for review** — don't send or log it anywhere as final until the owner has edited and approved it, even if a CRM connector could technically attach it to the deal.

## Worked example

**Input:** "Client is a 12-person marketing agency, wants a client portal so their clients stop emailing for status updates, mentioned they're losing time on Fridays doing manual reports, budget probably 5-8k, want it in 6 weeks"

**Output (excerpt):**

> **Project Summary**
> [Client] is a 12-person marketing agency spending significant time every Friday manually compiling client status reports. This project builds a client portal so clients can check project status themselves — cutting that manual reporting time and reducing "just checking in" emails.
>
> **Scope of Work**
> Phase 1 — Discovery & Design (Week 1-2): Portal wireframes, 2 design concepts, client review round
> Phase 2 — Build (Week 3-5): Client login, project status dashboard, file sharing, notifications
> Phase 3 — Launch & Handoff (Week 6): QA, client team walkthrough, go-live
>
> **Out of Scope:** Custom mobile app, payment processing, white-label for [Client]'s own clients (can be phase 2 add-on)
>
> **Investment:** [FEE — confirm with client, notes suggest $5-8K range]

---
*Part of the Agency Skill File Starter Kit — ManagedCoder. Want proposals like this auto-drafted the moment a deal hits "Discovery" stage? See Agency Control Tower: controltower.collabai.software*
