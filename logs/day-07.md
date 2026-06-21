# Day 07: June 22, 2026
* **Core Focus:** Practical Script Development, Linux System Internals, and Dependency Resolution
* **Milestone Achieved:** Successfully built and deployed two custom security automation scripts.

## 🛠️ Developed Projects & Technical Breakdown

### 1. Password Strength Checker (Python)
* **Functional Logic:** Analyzes user-input string metrics to evaluate password entropy and security viability.
* **Obstacles & Breakthroughs:** Faced immediate syntax constraints and dependency errors regarding the external security library `zxcvbn`. Resolved this by mapping local Python environment variables and correctly configuring the runtime package installer to resolve missing modules.

### 2. Live Login Log Analyzer & Security Auditor (Python / CLI)
* **Functional Logic:** Automates the parsing of operating system authentication logs to isolate failed authentication patterns.
* **Environments & System Obstacles:** This advanced script required handling complex Linux data pipelines. Encountered two major environment roadblocks:
  1. **System Logging Transitions:** Modern Linux distributions utilize a binary logging subsystem (`systemd-journald`) instead of traditional text-based paths like `/var/log/auth.log`. This mismatch threw structural `FileNotFoundError` handling bugs into the script.
  2. **Compressed Wordlist Architecture:** Encountered an error when the automated scanning routine failed to locate the standard dictionary file paths (`/usr/share/wordlists/rockyou.txt`). Discovered that advanced security platforms ship large dictionary matrices inside a compressed `.gz` format to minimize space, requiring manual terminal expansion blocks before program interaction.
* **Breakthrough Execution:** Used Linux CLI automation to locate, unzip, and mount the files correctly, adapting the script's input stream variables to handle the modern OS backend frameworks seamlessly.

## 📝 Tomorrow's Goal
Clean up the script code layouts inside the repository's `/projects` folder, and complete the final portfolio formatting checks ahead of the submission portal window closing.
