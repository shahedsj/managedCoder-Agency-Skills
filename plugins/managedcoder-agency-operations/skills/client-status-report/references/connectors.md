# Optional connector guidance

This package installs Skills only. It does not install, authenticate or promise an email, calendar, CRM, task, meeting or knowledge connector. All workflows work from supplied evidence, with reduced scope clearly stated.

Use an existing host tool only when actually exposed and authorized. Check available operations, account scope, pagination and identity before retrieving or writing records. Request a bounded relevant source, not whole chat history or credentials. Never ask for passwords or API keys in chat.

Prepare the exact requested changes before consequential writes. Reuse scoped approval, verify returned results, and report partial failures. Tool availability does not itself authorize sends or external writes. No automatic scheduling, tracking, persistent memory or telemetry is included.
