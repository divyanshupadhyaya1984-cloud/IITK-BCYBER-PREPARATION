# Lightweight Host-Based Authentication Event & Log Analyzer Core

A high-performance, non-blocking security monitoring pipeline built on Kali Linux to detect and analyze automated authentication threats (such as brute-force attacks) in real time. This project was developed as a technical showcase highlighting regular expression parsing engines and dynamic temporal sliding-window analysis.

---

## 🏗️ Architectural Design & Data Flow

The project is structured around a decoupled data processing pipeline to minimize CPU overhead while ensuring real-time threat evaluation:

1. **Ingestion Layer:** Connects to the host operating system's active log mechanism (`/var/log/auth.log`) using a non-blocking stream handler that targets only new, incoming event data.
2. **Parsing & Normalization Engine:** Employs Regular Expressions with named capture groups to isolate, validate, and convert unstructured log strings into clean data structures.
3. **Persistence & Optimization Layer:** Logs every failure event inside an optimized SQLite database utilizing compound indexes over relational lookups (`epoch_time`, `ip_address`) to avoid full-table scans.
4. **Analytical Evaluation Brain:** Applies a dynamic sliding-window detection algorithm based on a deterministic mathematical rule to evaluate security boundaries every second.

---

## 🧠 Core Algorithmic Logic

Instead of relying on basic tracking flags, the engine evaluates incoming threats mathematically using a rolling time window:

$$Count_{\text{failures}} = \sum_{t = T_{\text{current}} - \Delta t}^{T_{\text{current}}} (Event_{\text{status}} == \text{'FAILED'})$$

Where $\Delta t$ is set to a default value of **60 seconds**. 

If $Count_{\text{failures}} \ge \text{Threshold}$ (configured to **5 attempts**), the system flags the anomalous activity and prints a structural alert banner containing the malicious footprint details.

---

## 🛑 Engineering Hardships & Debugging Milestones

Building a security monitoring framework from the ground up as a beginner exposed several real-world infrastructure challenges that forced deep systems-level troubleshooting:

### 1. Modern Operating System Infrastructure Drift (`FileNotFoundError`)
* **The Hardship:** During initial testing, the analyzer crashed immediately with an error stating `/var/log/auth.log` did not exist. 
* **The Diagnostic Resolution:** Discovered that modern Debian-based distributions (like modern Kali Linux environments) have transitioned away from legacy flat-text logging daemons (`rsyslog`) to unified binary engines managed by `systemd-journald`. To resolve this without over-complicating the parser footprint, I manually re-introduced the `rsyslog` service to generate the required text-based log streams.

### 2. Compressed Resource Dependencies in Security Environments
* **The Hardship:** The automated validation simulation failed because the local penetration testing framework could not read the default wordlist paths (`rockyou.txt not found`).
* **The Diagnostic Resolution:** Realized that Kali Linux purposefully ships large payload directories in compressed Gzip (`.gz`) formats to balance space allocations. I had to manually interact with the systems utilities to decompress the resource block (`gunzip`) before running the attack simulation engine.

---

## 💡 Core Cybersecurity & Engineering Learnings

* **Algorithmic Complexity Optimization:** Learned the value of applying database indexes (`CREATE INDEX`) to timestamps. Without an index, checking historical records under a heavy automated attack results in an $O(N)$ linear search that triggers severe CPU bottlenecks. Adding a compound index reduces the query lookup path to $O(\log N)$.
* **Non-Blocking Resource Access:** Understood how to leverage file stream seek operations (`f.seek()`) to jump directly to the tail end of system files, ensuring the application ignores historic dead state data and focuses exclusively on live threat vector inputs.
* **Identity Infrastructure Defenses:** Gained first-hand experience regarding how attackers use horizontal and vertical automated dictionary arrays to target enterprise interfaces, reinforcing why adaptive sliding windows are necessary to detect threat footprints.
* **Learned about CLI specific commands:** 
1."sudo python3 ~/_Project/analyzer.py" This command helps me to lanch security monitoring engine.
2."sudo systemctl start ssh" Control interface for system manager and ssh explicitly commands the system to launch the OpenSSH Server.
3."hydra -l administrator -P /usr/share/wordlists/rockyou.txt ssh://127.0.0.1 -t 4 :"Helps to simulate the Brute-Force Attack with Hydra


---

## 🛠️ Complete Step-by-Step Execution Guide

Follow these exact terminal commands sequentially inside Kali Linux to deploy, resource, and validate the project environment.

### 1. Workspace Initialization
```bash
# Set up project directory tree
mkdir -p ~/_Project/data
cd ~/_Project

# Create script file (Paste the parser core source code inside analyzer.py)
touch analyzer.py
