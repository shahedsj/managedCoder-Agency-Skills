"""Run pinned Gitleaks without executing application code or exposing secret values."""
import collections
import datetime
import json
import os
import pathlib
import subprocess
import tempfile

def main():
    repo = pathlib.Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    temp = pathlib.Path(os.environ["RUNNER_TEMP"])
    output = temp / "secret-scan-output"
    output.mkdir(mode=0o700, exist_ok=True)
    result = {
        "repository": os.environ["GITHUB_REPOSITORY"],
        "scan_time_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "tool": "gitleaks", "version": "8.30.1",
        "commit": os.environ["GITHUB_SHA"],
        "run_url": "https://github.com/" + os.environ["GITHUB_REPOSITORY"] + "/actions/runs/" + os.environ["GITHUB_RUN_ID"],
        "scope": "All fetched refs and reachable Git history, plus checked-out files",
        "limits": ["Not a complete security audit or proof of no exposure",
                   "Does not discover personal copies, unreachable/deleted remote commits, submodules or Git LFS contents",
                   "No credential validation or provider API calls",
                   "Default pattern detection can miss custom or ordinary-word passwords"],
        "configuration": "Built-in defaults; repository allowlists and inline gitleaks:allow comments ignored",
        "scans": [],
    }
    with tempfile.TemporaryDirectory(prefix="secret-scan-", dir=temp) as raw_dir:
        work = pathlib.Path(raw_dir)
        config = work / "rules.toml"
        config.write_text("[extend]\nuseDefault = true\n")
        ignore = work / "empty.ignore"
        ignore.write_text("")
        for kind in ("git", "dir"):
            raw = work / (kind + ".json")
            command = ["gitleaks", kind, str(repo), "--config", str(config),
                       "--gitleaks-ignore-path", str(ignore), "--ignore-gitleaks-allow",
                       "--redact=100", "--no-banner", "--report-format=json",
                       "--report-path", str(raw), "--exit-code=10"]
            if kind == "git":
                command.append("--log-opts=--all --full-history")
            # Keep stdout/stderr off the CI console; no code, matches or secrets are published.
            with (work / (kind + ".log")).open("w") as log:
                try:
                    process = subprocess.run(command, stdout=log, stderr=log, timeout=2400, check=False)
                    code = process.returncode
                except subprocess.TimeoutExpired:
                    code = 124
                except OSError:
                    code = 127
            try:
                findings = json.loads(raw.read_text()) if raw.exists() else None
            except (ValueError, OSError):
                findings = None
            valid = code in (0, 10) and isinstance(findings, list)
            valid = valid and ((code == 0 and not findings) or (code == 10 and bool(findings)))
            # Deliberately drop Secret, Match, author email and surrounding text.
            metadata = [
                {key: finding.get(key) for key in ("RuleID", "File", "StartLine", "EndLine", "Commit")}
                for finding in (findings or []) if isinstance(finding, dict)
            ]
            result["scans"].append({
                "mode": kind, "exit_code": code,
                "status": ("findings" if code == 10 else "no_findings_in_scanned_scope") if valid else "incomplete_or_error",
                "finding_count": len(metadata) if valid else None,
                "rules": dict(collections.Counter(str(x.get("RuleID")) for x in metadata)) if valid else {},
                "findings": metadata if valid else [],
            })
    result["status"] = (
        "incomplete_or_error" if any(x["status"] == "incomplete_or_error" for x in result["scans"])
        else "findings" if any(x["status"] == "findings" for x in result["scans"])
        else "no_findings_in_scanned_scope"
    )
    (output / "summary.json").write_text(json.dumps(result, indent=2) + "\n")
    lines = ["## Repository secret scan", "", "Result: **" + result["status"] + "**",
             "", "| Scope | Status | Findings |", "|---|---|---|"]
    for scan in result["scans"]:
        lines.append("| " + scan["mode"] + " | " + scan["status"] + " | " + str(scan["finding_count"]) + " |")
    lines += ["", "Download secret-scan-metadata for file/line/commit metadata. No credential values are included.",
              "", "No findings is limited to the scanned scope. Review limits in summary.json.",
              "If findings exist, triage and revoke/rotate confirmed credentials; do not delete evidence or rewrite history automatically."]
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as summary:
        summary.write("\n".join(lines) + "\n")
    return 0 if result["status"] == "no_findings_in_scanned_scope" else 1

if __name__ == "__main__":
    raise SystemExit(main())
