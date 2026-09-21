---
name: icp-list-build
description: Turn a raw CRM export or tag pull into a short outreach list you can actually trust — hard exclusions applied, fit scored, weak pools reported honestly. Use whenever the user says "build me a list", "who should I email", "pull my ICP", "find agency owners in my CRM", "clean this list before we send", or is about to start any outreach batch. Also use when a list already exists but nobody has checked it for opt-outs, duplicates, or people who were contacted last month. Read-only — it never sends anything.
---

# ICP List Build

A list is not an ICP match just because somebody tagged it once in 2021. Most bad outreach batches are not a copywriting failure — they are a list failure that nobody checked. This skill turns a raw pull into a short list you can send to without embarrassment. The filtering is the product, not the search.

> Tool placeholders like `~~CRM` mean whatever tool you've connected in that category. See [CONNECTORS.md](CONNECTORS.md).

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│  STANDALONE (always works)                                    │
│  ✓ Paste a CSV export, a spreadsheet, or a plain list         │
│  ✓ Full exclusion pass, fit scoring, honest pool report       │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                   │
│  + ~~CRM: pull by tag or field, read opt-out and DND status   │
│  + ~~email: check who you already wrote to, and when          │
└──────────────────────────────────────────────────────────────┘
```

## What I need from you

1. **The source** — a tag, a segment, a saved view, or a pasted export. Never "everyone."
2. **Target count** — how many contacts you want out the other end.
3. **Your ICP**, if it differs from the default below.

## Default ICP (say so if yours is different)

- A title that means they decide, not just execute — owner, founder, CEO, president, principal, managing director
- A real working business, with a website or a live profile on file
- The company size band you actually serve, stated as a number, not a vibe
- The region the campaign is for

## Step 1 — Pull candidates from a filter, never from everything

Start from a tag, segment, or field filter. Then narrow. A full-database pull with filtering applied afterwards nearly always leaks: the records you meant to exclude are the ones with missing fields, and missing fields survive loose filters.

## Step 2 — Hard exclusions, applied every time

Drop a contact if **any** of these is true. No judgment calls, no exceptions for a promising-looking name.

| Exclusion | Why |
|---|---|
| Marked do-not-contact at the record level | Opted out on any channel |
| Marked opted-out on **email specifically** | This is usually a separate field from the main DND flag, and it stays hidden while the main flag reads false. Pull the records and check the field directly — most CRM search filters cannot see it. |
| Already contacted in this campaign family | A duplicate cold open is the fastest way to look automated |
| Flagged as bad or incomplete data | No first name, a generic inbox, a dead domain |
| Unsubscribed under **any spelling variant** | Tag names drift. `unsubscribe`, `Unsubscribed`, `unsub-2024` are three tags and one meaning |
| Email explicitly marked invalid | A bounce costs sender reputation across the whole batch, not just that send |

**Check for duplicate tag names with different IDs.** Most long-lived CRMs have them. Two tags reading `usa agency` are not interchangeable, and picking the wrong one silently halves your pool.

## Step 3 — Score fit, don't just filter

Everyone who survives Step 2 gets scored:

| Signal | Points |
|---|---|
| Title contains owner / founder / CEO / president / principal | +3 |
| Email explicitly verified as valid | +2 |
| Email status unknown | 0 |
| Real company website on file | +1 |
| A senior role but not the owner (e.g. Creative Director at a larger shop) | +1 — usable, weaker fit |
| No title, or a generic inbox (info@, team@, hello@) | −1 |

Take the highest scorers up to the target count.

## Step 4 — Never trust one field for geography

The country field is the least reliable column in almost every agency CRM. Records entered by a form, an import, or a list purchase inherit whatever default the tool had that day.

Cross-check at least two of: state or province, postal code format, phone country code, website domain ending. If two disagree, exclude rather than guess.

## Output

```
## ICP List — [source], [date]

Pulled: [N]
Excluded: [N]  (opt-out [n] · already contacted [n] · bad data [n] · invalid email [n])
Scored: [N]
Selected: [target]

⚠️ Fit note: [the honest problem with this pool, if there is one]

| Name | Title | Company | Email | Score | Why it scored that way |
|---|---|---|---|---|---|
```

## The rules that make this work

**Exclusion beats inclusion.** A contact that should have been excluded and wasn't is a compliance problem and a reputation problem. A good contact left out by mistake costs nothing — it waits for the next batch. When a record is ambiguous, exclude it.

**Say when the pool is weak.** If the honest fit is thin — skews too small, wrong region, mostly stale records — report that at the top, before the table. The failure mode is quietly relaxing the bar to hit the target count, because the person asking sees a full list and assumes it is a good one.

**A tag from three years ago is not a live signal.** Check when the record was last updated. An old tag is evidence that somebody once thought this person fit, not evidence that they still do.

**20 great-fit contacts beat 40 with half borderline.** Outreach quality is remembered. List size is not.

## Worked example

**Input:** "Pull 20 ICP matches from the agency-owners tag."

- 56 contacts carried the tag.
- Excluded 4: one do-not-contact, two opted out on email only (the main DND flag read false on both — found by reading the records, not by filtering), one flagged for missing first name.
- 52 scored. Titles skewed strongly to Founder and Owner, so decision-maker fit was genuinely good. But company size clustered at 2–10 people, against a stated ICP of 10–30+.
- Selected the top 20, all with verified emails and owner-level titles.

**The fit note went first:**

> ⚠️ This pool is mostly 2–10 person shops, smaller than your stated 10–30+ ICP. They are real agency owners and the list is clean. Your call whether that is the right fit for this campaign.

Notice what that avoids: the owner finds out about the size mismatch now, not after 20 sends and two replies.

## Tips

1. **Run this before writing a single line of copy.** Personalization cannot rescue a list that should not have been built.
2. **The two-opt-out-fields trap catches almost everyone once.** Most CRMs have a record-level do-not-contact flag and a separate per-channel one. The per-channel one is usually the one that matters, and usually the one the search API cannot filter on.
3. **If you can't find one true, specific thing about a contact, that is a list problem surfacing early.** Flag it here rather than letting the writing step invent a detail to compensate.
4. **Keep the excluded list.** Next month somebody will ask why a name is missing, and "we excluded it, here is why" is a much better answer than re-running the pull.
5. **This is a small-batch tool.** Tens, not hundreds. At hundreds you need real segmentation, which is a different job.

---
*Free next step: join a live class and get the weekly AI-for-agencies newsletter at managedcoder.com*

*Part of the Agency Skill File Starter Kit — ManagedCoder. Want your list built, cleaned and scored before you sit down, every week? See Agency Control Tower: controltower.collabai.software*
