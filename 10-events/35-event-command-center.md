---
name: event-command-center
description: Plan, promote, track and close out an agency event, from a webinar to an in-person workshop to an event co-hosted with partners. Keeps one source of truth, separates "published" from "booked", reconciles registrations across tools, drafts personal invitations and runs the post-event follow-up. Use when the user is planning an event, picking a date or venue, inviting people, counting registrations, working with co-hosts or sponsors, preparing the day, writing thank-yous or a recap, or asks "where are we on the event", "how many are coming", "is the venue confirmed" or "what's left before the event".
---

# Event Command Center

Events fail quietly. Not on the day, but weeks before: a venue that was never under contract, a headcount nobody can explain, a co-host who saw the wrong date, a thank-you email that never went out. This skill keeps one honest picture of the event so the owner is not the only person who knows where it stands.

> Tool placeholders refer to your connected systems. See [CONNECTORS.md](../CONNECTORS.md).

## How it works

| Mode | What it does |
|---|---|
| Standalone | Paste your notes, emails, partner messages and registration counts. Get a status sheet, a dated plan, flags and drafts. |
| Connected | Read event threads from ~~email, dates from ~~calendar, contacts and registrations from ~~CRM, tasks from ~~project tracker, files from ~~docs. Propose writes, never make them without a yes. |

**Works with other skills in this kit.** If they are loaded, use them instead of rewriting their rules:

| Need | Skill |
|---|---|
| Write in the owner's voice | 12 Write In My Voice, 29 Owner Email Rules |
| Personal invitations | 31 Lead Research Brief, then 15 Warm Lead Outreach or 28 Unique Cold Outreach |
| Venue or sponsor contract | 32 Contract Red-Flag Review |
| Co-hosts and sponsors | 33 Partner Pipeline & Follow-Up |
| Planning call notes into tasks | 03 Meeting Notes to Tasks |
| Recap post | 30 Owner Blog Post |
| A joint decision to record | 25 Agency Decision Logger |

If the user has their own services or offer document, read it before writing any "what's next" line. Never describe a service from memory.

## What I need from you

Choose one:

1. Event basics: name, date, format, audience, target headcount, co-hosts if any.
2. A pile of notes, email threads and partner messages. I will build the picture.
3. A finished event and what happened. I will run the close-out.

## Step 1: Diagnose the event type

| Type | Signal | What the plan must protect |
|---|---|---|
| Online (webinar, live class) | Zoom or similar link, no venue | Show rate and the recording follow-up |
| Own in-person | Your venue, your list | The booking, the headcount, the day-of run |
| Co-hosted | Partner names, shared emails, two sign-up pages | Who owns what, one shared story, partner trust |

If more than one fits, treat it as co-hosted. That is the most expensive one to get wrong.

## Step 2: Build the source-of-truth table

One row per fact that someone outside the team will see. Every row gets a status and a source.

| Status | Means |
|---|---|
| CONFIRMED | Contract, payment or written yes exists |
| HELD | Verbal or pencilled hold, nothing signed |
| ASKED | Request sent, no answer |
| UNKNOWN | Nobody has checked |

Rows to always include: name, date and time, venue, capacity, registration links, speakers, sponsors, budget owner, recording plan.

**Published is not booked.** A venue on the event page is HELD until someone can show the contract. Teams lose venues by reading their own website as proof.

## Step 3: Lay out the dated plan

Count back from the event date. Use these as defaults and say when a date has already been missed.

| When | Must be done |
|---|---|
| 8 weeks | Venue CONFIRMED. One event name and one URL locked |
| 6 weeks | Registration open. Personal invitations start |
| 4 weeks | Sponsor and speaker list closed. Run of show drafted |
| 2 weeks | Reminder to all registrants. Co-host promo posts scheduled |
| 7 days | Final headcount to venue and caterer. Partner calendar posts live |
| 48 hours | Reminder with address, parking or link, and start time |
| 2 hours | Last reminder, online events only |
| Day + 3 | Thank-yous sent, recording or photos shared |
| Day + 5 | Attendee list to sponsors, if that was promised |

Online events can compress the first two rows to 4 weeks. In-person events with a co-host should not, because partners need time to approve copy.

## Step 4: Reconcile registrations

Registrations usually live in two to four places: your form, a ticketing site, a co-host's form, a spreadsheet. There is no single dashboard.

- Report each system separately, with the date of the count.
- Remove duplicates by email before giving a total.
- An empty table or a zero is not proof something is broken. First find out which system is meant to collect that data. Most "broken registration" alarms are someone checking the wrong system.

**Plan the room by show rate, not by registrations.** Starting points, replace them with your own numbers after two events:

| Type | Plan for |
|---|---|
| Free online | 30% of registrants |
| Free in-person, general invite | 40% |
| Free in-person, personal invitations, hands-on | 70% |

Why: the free-event warning people repeat is 25%, but a hands-on workshop filled with personal invitations can run near 70%. Both numbers are real. The invite method moves it more than the topic does.

## Step 5: Draft invitations

- One invitation per person, for one event. If you run a series, map each person to the event that fits them best.
- Every invitation names one true, specific thing about them. If you know nothing real about the person, they do not get an invitation.
- Personal sends from one inbox: 20 a day maximum. More than that starts to look like a bulk send to inbox filters.
- A free-entry code is a courtesy, not a discount. Never post it publicly.
- Drafts only. Nothing sends without a yes.

## Step 6: Co-host and sponsor rules

Skip this step for events you run alone.

- Agree the partner name order once, in writing, and use it everywhere.
- Never describe a joint event as led by one side. Joint decisions are "proposed for confirmation", not "we decided".
- Owner columns name organizations, not one person on your side and a company on theirs.
- No heading names a person in a criticism. "Corrections needed", not "errors in their recap".
- No prices, sponsor tiers or amounts in public copy until agreed in writing.
- Agree the selling rule up front. If nobody sells on the day, say so on both sides' pages the same way.
- Before quoting any number to a partner, say which system and which date it came from.

## Step 7: Close out

After the event, run the checklist in the Output below. A thank-you sent on day 3 is warm. The same email on day 15 reads as an afterthought.

## Output

Use this structure every time.

```text
EVENT: [name] | [date, time, timezone] | [type] | [days to go or days since]

SOURCE OF TRUTH
| Item | Value | Status | Source | Owner |
| Venue | [ ] | CONFIRMED/HELD/ASKED/UNKNOWN | [contract, email, date] | [org] |
| ... |

REGISTRATIONS (as of [date])
| System | Count | Last checked |
Unique total after removing duplicates: [n]
Expected in the room at [x]%: [n]

PLAN: what is due in the next 14 days
| Due | Task | Owner | Status |

OVERDUE against the default plan
- [item, due date it missed]

DRAFTS (not sent)
- [invite / reminder / thank-you / partner note]

⚠️ Before you act:
- [HELD item treated as confirmed anywhere]
- [name, date or URL that differs between surfaces]
- [number quoted to a partner without a system and a date]

POST-EVENT CHECKLIST *(only after the event)*
- [ ] Event page changed from "Register" to a thank-you with results
- [ ] Registration forms closed
- [ ] Thank-yous: attendees, speakers, sponsors, venue, co-hosts
- [ ] Recording or photos shared, with partner credit if asked
- [ ] Attendee list to sponsors, if promised
- [ ] Final count from every system, with dates
- [ ] Date set for the next touchpoint
- [ ] What worked and what didn't, recorded for next time
```

## The rules that make this work

- **Status beats description.** "Venue: Midtown room" hides the risk. "Venue: HELD, no contract" shows it.
- **Lock the name before you print.** Names multiply in planning emails. Printing badges, banners or shirts makes the name permanent, right or wrong.
- **Every number carries its source and date.** Partners remember the first number you tell them, not the correction.
- **Verify before you call something broken.** Replacing a working process because of one empty report costs more than the bug you thought you found.
- **Nothing sends, publishes or writes without a yes.** Events touch partners, sponsors and the public at once. One wrong send reaches all three.

## Worked example

Fictional input, pasted as-is:

```text
3 free AI workshops oct w/ local biz association + an IT firm. venue for the big one is on the website. site registration table shows 0 so forms broken?? ticketing site says 33 for day 2. ppl call it 4 diff names. sponsor wants attendee list. day 1 got 72 regs. plan for 25% show
```

Output:

```text
EVENT: AI workshop series (name not locked) | 3 dates in Oct | Co-hosted

SOURCE OF TRUTH
| Venue, day 2 | Listed on website | HELD | No contract seen | Unknown |
| Event name | 4 versions in use | UNKNOWN | Planning emails | All three orgs |

REGISTRATIONS (as of today)
| Your site table | 0 | today |
| Ticketing site | 33 (day 2) | today |
| Day 1 | 72 | source not stated |
Unique total: cannot calculate. Duplicates not removed.

⚠️ Before you act:
- "Forms broken" is not proven. Confirm where the site forms send their
  data. The table may never have been meant to hold registrations.
- Day 2 venue is only on the website. Ask the co-host for the contract
  or a written booking before saying "confirmed" to anyone.
- Four names in use. Pick one before anything is printed.
- 25% is a fair start for a general invite. For the hands-on day with
  personal invitations, plan nearer 70%. At 72 registrations that is
  about 50 people, not 18. Check the room capacity.
- Sponsor list: confirm consent wording on the forms before sharing.
```

What happened: about 52 of the 72 came on day 1. Planning at 25% would have set up a room for 18.

## Tips

1. The co-host who does the most work is your most important relationship. Treat them as a peer running a joint program.
2. Put "published is not booked" in your team's head early. It saves one bad week a year.
3. Personal invitations take longer and fill rooms. A hundred specific emails beat a thousand generic ones.
4. Ask attendees one question at the door and one at the end. The answers are your next event and your next post.
5. If you dread checking the headcount, check it today. Late surprises cost the most.

---
*Part of the ManagedCoder Agency Skills library. Keep every event's dates, owners and promises in one place the whole team can see.*
