# Change log

## October 18, 2026: Agency Brain Kit

Added the [Agency Brain Kit](09-agency-brain-systems/brain-kit/README.md) and three skills, bringing the standalone catalog from 36 to 39 workflows:

- [Build the Brain](09-agency-brain-systems/37-build-the-brain.md): turn rough notes or an Agency Brain page file into source-backed company files. Marks unknown facts, separates Confirmed from Proposed, and previews before saving.
- [Ask the Brain](09-agency-brain-systems/38-ask-the-brain.md): answer from your own files with the file, entry and date. Says "Not in the Brain" instead of guessing and flags conflicts and old entries.
- [Brain Health Check](09-agency-brain-systems/39-brain-health-check.md): report entries past review, with no source, in conflict, or never confirmed. Reports only.

The kit is plain Markdown: no signup, no connection and no ManagedCoder product needed. Test cases and a fictional sample agency are in `tests/brain-kit-evals.json` and `tests/brain-kit-fixtures/`. The cases are defined but not yet run in a supported host, so they are not evidence of results.

These skills are not added to the plugin package.

## October 18, 2026: voice decisions and evidence checks

- Added [Voice Task Review](01-owner-command/36-voice-task-review.md), bringing the standalone catalog to 36 workflows. Work through one owner decision at a time and verify approved tracker changes.
- Updated [Next Meeting Prep Brief](01-owner-command/26-next-meeting-prep-brief.md) with invitation reconciliation, packet checks and dated commitment evidence.
- Updated [Competitor / Prospect Scan](07-research-intelligence/04-competitor-prospect-scan.md) with pasted-input support, dated offer comparisons, provider-claim labels and conflicting-price handling.

These are adapted operating workflows with synthetic examples. Static checks do not establish real-world effectiveness. This batch does not add plugin entries, change internal systems or publish website listings.

## October 10, 2026: Event Command Center

Added [Event Command Center](10-events/35-event-command-center.md): plan, promote, track and close out webinars, in-person and co-hosted events. New Events category. Catalog grows from 34 to 35.

This skill was not added to the plugin package or the website listing.

## October 2, 2026: accountability, outreach and two new workflows

The public catalog grew from 32 to 34 skills.

### Added

- [Partner Pipeline & Follow-Up](03-sales-pipeline/33-partner-pipeline-follow-up.md): identity checks, shared commitments, priority scoring and audience separation.
- [Weekly Marketing & Sales Review](06-marketing-content/34-weekly-marketing-sales-review.md): prior commitment review, evidence-based scorecards, pipeline movement, decision agendas and meeting closeout.

### Improved

- Manager Accountability Scorecard: separates weekly completion from backlog clearance; uses dated outcome evidence; includes N/A and UNKNOWN handling.
- Daily Task Triage: preserves missed recurring commitments and original deadlines; verifies ownership and acceptance before changes.
- ICP List Build: checks contact history and relationship ownership; holds unverified candidates; enforces campaign size and region criteria.
- Warm Lead Outreach, LinkedIn DM Outreach and Unique Cold Outreach: distinguish drafts from actual sends, avoid unsupported personalization claims and strengthen contact-history checks.
- Repaired relative connector links in affected catalog files and two existing YAML frontmatter errors.

[Implementation commit](https://github.com/shahedsj/managedCoder-Agency-Skills/commit/8577c2106e54498ef82d989cc941a07b5794aacc).

### Validation and limits

Changed files passed frontmatter and relative-link checks. The rewritten scorecard and new workflows passed a private-identifier scan. The existing plugin build check passed. These checks establish file and packaging consistency; they are not evidence of production results or model behavior across every workflow.

The two new skills are available in the GitHub catalog. They were not added to the six-workflow plugin package. This update did not publish a plugin-directory listing or update the ManagedCoder website resource listing.

### Visitor guide refresh

Added a clear project introduction and creator context, a full 34-skill catalog, category indexes and this change log. Updated the getting-started count and links so visitors can see what is available and choose a first workflow.
