# Policies

Rules you want applied the same way every time. One entry per rule. Keep each rule short.

Start with one. Add more when the same question comes up twice.

## Good first policies

- How we handle a request outside the scope
- How often and how we update clients
- What the team can decide alone and what comes to the owner
- How we approve work before it goes live
- How we handle late or missed deadlines

## Rules for this file

- A policy is a rule someone agreed to. An opinion is not a policy. Write `proposed` until you have confirmed it.
- Give every policy a source and a date. "Said in leadership meeting, 2026-10-12" is a good source.
- If a policy changes, add the new one and mark the old one `superseded`. Do not delete the old one.
- Put a review date on anything that depends on pricing, team size or tools.

## Entries

```text
title:
summary:
source:
source_date:
owner_role:
status:           active | proposed | superseded | expired
confidence:       high | medium | low
review_date:
supersedes:       none
human_review:     required | approved
```

### Example (replace with your own)

```text
title: Out-of-scope requests need written approval
summary: Any client request outside the signed scope gets a short written estimate and the client's written yes before work starts.
source: Leadership meeting notes
source_date: 2026-10-12
owner_role: Delivery lead
status: active
confidence: high
review_date: 2027-04-12
supersedes: none
human_review: approved
```
