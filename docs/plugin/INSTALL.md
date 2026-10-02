# Install and try the release candidate

The upload-ready archive is `dist/managedcoder-agency-operations-1.0.0.zip`, generated with `python3 scripts/build_plugin.py`. Its root contains `plugin.json`, `skills/`, `assets/` and `LICENSE`.

For local Codex testing, add this repository as a plugin marketplace using `codex plugin marketplace add shahedsj/managedCoder-Agency-Skills`, then use the plugin interface to install ManagedCoder Agency Operations. The marketplace descriptor points at `plugins/managedcoder-agency-operations`. Confirm support in your current Codex version; this repository does not bundle the Codex client.

For ChatGPT Work or another supported surface, use its developer/plugin installation flow when exposed. Public-directory installation is available only after OpenAI approves and publishes the listing. A GitHub ZIP is not evidence of directory publication.

Start with: “Draft a client update from these project notes.” Context setup is optional for the first task. No signup or connector is required. Keep an Agency Context Pack locally and supply it when needed.
