---
name: repository-secret-scan
description: Run this repository's GitHub-hosted Gitleaks scan and summarize findings with minimal AI tokens.
---
# Repository secret scan
Use GitHub Actions; do not ask the user to install or run a local scanner.
1. Read .github/security-scan/README.md. Identify the repository and desired ref.
2. Trigger "Repository Secret Scan" with GitHub workflow dispatch (or `gh workflow run repository-secret-scan.yml --repo OWNER/REPO --ref REF`) if it exists on the default branch. If the rollout PR is not merged, inspect its push-triggered run or rerun that run. Do not merge a PR just to trigger a scan.
3. Follow the run to completion. Failed, cancelled, timed-out and inaccessible runs are incomplete, never clean.
4. Download ONLY the secret-scan-metadata artifact and read summary.json. Do not ingest the repository source, raw scanner output or credentials into model context.
5. Report repository, timestamp, run URL, scanned scope, outcome, finding counts by rule and affected paths/commits. Keep output short. For large reports, summarize counts first and retrieve only relevant metadata.
6. Findings are candidates requiring triage. Recommend provider-side revocation/rotation for confirmed exposed credentials. Do not test credentials, change visibility, delete evidence, rewrite history or edit application code without a separate request.
7. Preserve coverage limits: this does not discover every personal/public copy or replace an application security review.
The scanner uses zero AI tokens; only orchestration and summarization use tokens. GitHub Actions minutes/storage may apply.
