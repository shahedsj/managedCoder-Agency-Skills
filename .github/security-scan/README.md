# GitHub-hosted repository secret scan

Run **Actions → Repository Secret Scan → Run workflow** after this workflow is on the default branch. The rollout branch `security/secret-scan-2026-10-17` runs automatically on push for initial validation; later runs are manual to control cost.

Claude Code can use `/repository-secret-scan`; Codex can use `$repository-secret-scan` when repository skills are supported. Both skill files contain the same short workflow. Agents need GitHub Actions read/write permissions to dispatch; viewing results requires read access. Missing permissions must be reported, not worked around using a token committed to Git.

## What runs
- Official Gitleaks CLI v8.30.1, downloaded from its GitHub release and checked against the published SHA-256 digest.
- Checkout action and artifact upload action pinned to commit SHAs.
- Read-only contents token; checkout credentials are not persisted.
- Full fetch, all reachable refs/history plus checked-out files, with no app builds, dependency installs, credential verification or model calls.
- Built-in detector rules, an empty ignore file and ignored inline allow-comments. Repository-specific exclusions are deliberately not accepted for this incident baseline.
- Two independent scan modes. Findings or errors fail the job. A timeout/failure is incomplete, not a clean scan.
- Only rule/file/line/commit metadata and counts are uploaded for seven days. Raw matches, credential values and scanner logs stay in temporary runner storage and are removed before artifact upload.

## How to interpret
Download `secret-scan-metadata/summary.json`. Report repository, reviewer, run URL/time, tool version, scope, counts, triage and remediation owner/date. Do not equate "no findings in scanned scope" with proof of no incident. Confirmed exposed credentials need provider-side revocation/rotation regardless of file deletion. Preserve evidence before any history rewrite.

## Coverage and cost
No AI API key is needed and detection uses zero AI tokens. AI reads only the small metadata report. GitHub-hosted runner minutes and artifact storage may be billed under the account's plan. Jobs are capped at 90 minutes, each scanner process at 40 minutes; large forks may exceed limits and need follow-up.

Scans do not cover unreachable/deleted remote commits, Git LFS objects or submodule contents, other accounts' copies, issue/PR comments, Actions logs or arbitrary confidential documents. Generic passwords and custom formats can be missed. Manual triage and a separate account-visibility inventory remain necessary. Empty repositories cannot run a workflow until they have a commit.

Sources: https://github.com/gitleaks/gitleaks and https://github.com/jpoindexter/security-skills/blob/main/secret-scan/SKILL.md . This is an adapted workflow, not an assertion that third-party skills were installed unchanged.
