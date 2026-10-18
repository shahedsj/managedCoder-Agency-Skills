# Client: [Client name or "Client A"]

Copy this file into `clients/`. Name it after the client, for example `northwind.md`. Skip fields you do not know. Write `UNKNOWN`.

## Basics

- Client: UNKNOWN
- Relationship owner (role, not a private note): UNKNOWN
- What we do for them: UNKNOWN
- Start date: UNKNOWN
- Contract or scope document: UNKNOWN (name or link, not the contract text)

## What matters to this client

- Their main goal: UNKNOWN
- How they like to be updated (channel and rhythm): UNKNOWN
- What annoys them: UNKNOWN
- Who decides on their side (role): UNKNOWN

## Scope and money

- What is in scope: UNKNOWN
- What is out of scope: UNKNOWN
- Billing model: UNKNOWN
- Known risk to margin or scope: UNKNOWN

## Current status

- Status (green, yellow, red, or UNKNOWN): UNKNOWN
- Why: UNKNOWN
- Next important date: UNKNOWN

## Entries

One block for each fact that should keep a source and a review date. Client status goes stale quickly, so give it a short review date.

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

## Do not put here

Passwords, API keys, private HR notes, or anything the client told you in confidence that you would not want an AI tool to read.
