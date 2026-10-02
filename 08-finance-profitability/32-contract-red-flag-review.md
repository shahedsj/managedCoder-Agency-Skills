---
name: contract-red-flag-review
description: Review an NDA, MSA, SOW, vendor agreement or proposal contract in plain English — find the clauses that cost an agency money or IP, say which ones to negotiate, and say clearly when a lawyer is needed. Use whenever the user says "review this contract", "is this NDA safe to sign", "check this MSA", "what's risky in this SOW", "explain this clause", or uploads an agreement before signing. Never approves, signs, or replaces legal advice.
---

# Contract Red-Flag Review

Agencies lose more money to clauses they skimmed than to clauses they negotiated. The expensive ones are rarely dramatic: a payment term tied to subjective acceptance, an IP assignment with no carve-out for your own reusable components, an auto-renewal with a 90-day opt-out window nobody diarised.

This skill reads the document, names the real risks in plain English, and tells you which ones are negotiation items versus which need a lawyer.

**This is not legal advice and this skill never approves a contract.** It produces a review to bring to a decision. Anything high-value, unusual, cross-border, employment-related, regulated, or litigation-adjacent goes to a qualified attorney, and the review says so.

> Tool placeholders like `~~docs` mean whatever tool you've connected in that category. See [CONNECTORS.md](../CONNECTORS.md).

## What I need from you

1. **The document** — full text, not an excerpt. Every exhibit, annex, and referenced policy.
2. **Which side you are on.** This changes everything (see Step 3).
3. **Your own standards, once** — your preferred governing law, payment floor, liability cap position, confidentiality term. Write them at the top of your copy of this file and reuse them forever.

## Step 1 — Identify the document and read it whole

NDA, MSA, SOW, vendor agreement, proposal contract, or unknown.

**Never infer anything from the filename.** A document titled "Mutual NDA" may be one-way. Read the operative clauses.

**Read the whole thing, including the attachments.** A search over snippets misses exactly the clause that was put in an exhibit to avoid attention.

## Step 2 — Hunt for placeholders and unsigned blocks first

Before any substantive review, check for:

- Brackets, `TBD`, `XXXX`, `INSERT`, `[Client Name]`, blank underscores
- Contact details copied from a different deal
- A counterparty signature block completed and yours blank, or the reverse
- A typed name and date in a shared doc — **that is not a signature.** Look for a real signature or a completion record

Any of these means the document is not ready to assess. Say so and stop. Missing facts cannot be risk-assessed.

## Step 3 — Ask which direction every restriction runs

This is the step people skip, and skipping it produces nonsense reviews.

A non-solicit that binds **you** and a non-solicit that **protects** you are the same words with opposite meaning.

| Clause | It restricts you | It protects you |
|---|---|---|
| Non-solicit / no-hire | Assess the term and scope carefully | Fine. Expect pushback — prepare a fallback |
| Non-circumvention | Narrow it to introductions actually made | Fine as drafted |
| Return and purge all copies | Confirm with IT that it is technically achievable at all | Fine, but a counterparty with retention duties will resist |
| Compelled disclosure with no "where legally permitted" carve-out | Negotiate | Low exposure, but fix it anyway |

Where a clause binds both sides, treat it as restricting you.

## Step 4 — Run the red-flag list

**Intellectual property**
- Ownership transferring all rights to the client with no carve-out for your pre-existing IP, reusable components, know-how, internal tools, templates, or generalized learnings
- No license-back letting you reuse non-client-specific code, tools, and frameworks
- Client ownership of the work product **before full payment**
- Any assignment, work-for-hire, or feedback-ownership language sitting inside an NDA. An NDA should transfer nothing

**Money**
- Payment terms longer than Net 30
- Payment tied to **subjective** acceptance, or to a milestone with no defined trigger
- No late-fee or remedy language
- Liability caps missing, one-sided, set too high, or with too many carved-out categories
- Indemnity that is broad, one-sided, uncapped, or where the other side controls the defense
- IP indemnity with no exclusion for content the client supplied

**Exit**
- Auto-renewal with no practical opt-out window
- Termination for convenience with no notice, transition, or payment protection
- Termination for cause with no cure period

**Scope**
- Vague deliverables, undefined acceptance criteria, missing assumptions
- No change-order process
- Unlimited revisions

**Jurisdiction**
- Governing law, venue, or arbitration seat outside your preferred jurisdiction. Another domestic state is a business decision — weigh the litigation cost and check whether it is exclusive. **Foreign law, foreign courts, an arbitration seat you do not recognise, or a controlling foreign-language version all go to a lawyer.**

**Restrictions**
- Non-solicit or non-circumvention terms longer than 12 months
- Non-compete or exclusivity inside an NDA — do not sign without counsel
- Publicity restrictions broader than you expect
- A confidentiality carve-out that would block lawful whistleblower reporting

**Data and AI** — live risk for any agency using AI tooling or distributed teams
- Will confidential information enter an AI system? Which providers, and do they train on the input?
- Public AI tools that train on submitted data must not receive client confidential information
- A total AI ban may conflict with how you actually deliver. Route it to whoever owns delivery before signing rather than accepting it quietly
- Confirm your real retention, logging, subprocessors, and team locations actually satisfy the terms

**Regulated data — always a lawyer.** Personal, health, financial, biometric, student, payment, or banking data. Any DPA, BAA, security addendum, or audit right. An incident-notification deadline of 72 hours or less. A 24/7 security contact requirement. Client control of breach notification. Reimbursement of breach costs. Mandatory certifications, pen tests, or insurance.

## Step 5 — Pick exactly one outcome

| Outcome | Meaning |
|---|---|
| `BLOCKED — MISSING INFORMATION` | Missing parties, dates, exhibits, placeholders, unknown signer authority, an unreadable scan |
| `LEGAL REVIEW REQUIRED` | IP transfer, non-compete, foreign law, uncapped indemnity, regulated data, or anything you cannot confidently interpret |
| `NEGOTIATE BEFORE SIGNING` | The core is reasonable, specific terms should change. Give the exact clause, the risk, and fallback language |
| `READY FOR AUTHORIZED SIGNATURE` | Everything checks out. This means it can go to a signer. It does **not** mean this review approved it |

**When several apply, take the highest:**

```
BLOCKED  >  LEGAL REVIEW  >  NEGOTIATE  >  READY
```

A document whose facts are unknown cannot be assessed for legal risk, and a document needing counsel cannot usefully be negotiated first. Record the lower findings anyway — they become the next pass once the blocker clears. Say so out loud: *"Blocked now; expect legal review once the party identity is confirmed."*

## Output

```
## Contract Review — [document], [date]

Outcome: [one of the four]
Driven by: [the specific findings that caused it]

### In plain English
- [highest-risk issue first]
- [...]

### Clause by clause
| Clause | What it says | Your standard | Status | Suggested action |
|---|---|---|---|---|

### What to do next
- [ ] [action]
- [ ] [action]

### Open questions
- [anything that must be answered before signing]
```

## The rules that make this work

**Never sign, approve, reject, or modify a contract.** This recommends. Only a person with confirmed signing authority decides.

**A past signature is not approval.** Companies sign outliers — under deadline pressure, or before anyone looked. Finding the same clause in a signed agreement makes it a precedent to examine, not a standard to copy.

**Never call a document fully executed** until every required party has signed. Two files in a typical archive will have a completed counterparty block and a blank one on your side.

**When confidence is low, escalate.** Choose legal review or blocked. Never say "safe to sign" without stating the conditions and the human approval still required.

**Unanswered questions mean blocked, not assumed.** Put them in open questions and mark the fields unknown. Never guess a value to reach a better outcome.

**Keep the document private.** Contract text, party names, and commercial terms do not go to any outside tool, link, or person unless you are explicitly asked to send them.

## Worked example

**Input:** a 6-page MSA from a mid-sized client, agency is the vendor.

**Step 2** found `[INSERT EFFECTIVE DATE]` on page 1 and a blank signature block on the client side.

**Step 3** established the non-solicit binds the agency, not the client — so the 24-month term is a real restriction, not a protection.

**Step 4** found: IP assignment with no carve-out for the agency's reusable components; Net 60 payment; liability cap at 3x fees for the agency and uncapped for the client; auto-renewal with a 90-day opt-out.

**Outcome:** `BLOCKED — MISSING INFORMATION`, because of the placeholder date.

But the review listed everything else anyway, with the note: *"Blocked on the missing date. Once that clears, expect NEGOTIATE — the IP carve-out and the one-sided liability cap are the two that matter, and the 24-month non-solicit is worth pushing to 12."*

The client fixed the date in an hour. The negotiation list was already written.

## Tips

1. **Write your standards down once.** Most review time is spent re-deciding what your position is. Decide it once, calmly, not under deal pressure.
2. **The auto-renewal opt-out window is the most commonly missed clause in agency contracts.** Put the date in a calendar the day you sign.
3. **"Our standard agreement, everyone signs it" is not a reason.** It is an opening position.
4. **The clause that costs you is usually about payment timing or IP reuse**, not the dramatic-sounding indemnity paragraph.
5. **If a review takes more than 20 minutes, that itself is the finding.** Hand it to a lawyer.

---
*Free next step: join a live class and get the weekly AI-for-agencies newsletter at managedcoder.com*

*Part of the Agency Skill File Starter Kit — ManagedCoder. Want every incoming agreement reviewed against your own standards before it reaches you? See Agency Control Tower: controltower.collabai.software*
