# 🛡️ Dual-Engine Password Strength Checker

A Python command-line application that evaluates password security using a hybrid approach: **Rule-Based Heuristic Validation** (via Regular Expressions) and **Entropy-Based Pattern Matching** (via Dropbox's `zxcvbn` library). 

This project demonstrates why traditional password complexity rules are no longer sufficient under modern OWASP security standards.

---

## 🚀 Features

* **Custom Regex Engine:** Checks for specific cryptographic requirements (min length, uppercase, lowercase, numbers, and symbols).
* **Dynamic Feedback:** Generates real-time, actionable suggestions if a password fails specific heuristic checks.
* **Entropy Analysis via `zxcvbn`:** Detects predictable patterns, sequential characters (`qwerty`, `123`), repetition, and dictionary words.
* **Crack Time Estimation:** Displays a realistic simulation of how long a brute-force attack would take against an online portal.

---

## 🛠️ The Tech Stack

* **Language:** Python 3.11+
* **Core Modules:** `re` (Regular Expressions for pattern constraints)
* **Third-Party Dependencies:** `zxcvbn` (Advanced password strength estimator)
* **Environment:** Tested on Kali Linux

---

## 🛑 Technical Hardships & Breakthroughs

### 1. The "False Security" Trap (Regex vs. Reality)
* **The Struggle:** Initially, I designed a custom validator using standard `if/else` checks and regular expressions. The script successfully graded `Password123!` as **5/5 (Very Strong)** because it technically met all character requirements. However, in reality, this is one of the most commonly leaked and guessable passwords globally.
* **The Breakthrough:** I realized that rigid character rules don't equal high entropy. To align with modern **OWASP Guidelines**, I integrated the `zxcvbn` library with also taking help from AI and learning. This addition catches human predictability and exposes dictionary patterns that standard regex engines miss entirely.
* **

### 2. Python Script Sequence and Name Errors
* **The Struggle:** During development, I encountered a `NameError: name 'advanced_password_check' is not defined`. This happened because I attempted to call the `zxcvbn` analyzer inside the execution block *before* the Python interpreter had read the function's blueprint from the top down.
* **The Breakthrough:** I restructured the script to enforce clean execution flow: placing global library imports at the absolute top, defining both analytical functions sequentially in the middle, and isolating the terminal interface at the absolute bottom using the `if __name__ == "__main__":` guard block.

#### 3. Python Scope and Syntax Disruption (Indentation Errors)
* **The Challenge:** While merging the heuristic character check engine with the dictionary evaluation rules, the script threw abrupt compilation errors. Python's strict whitespace requirements caused structural blocks (specifically the `strength_levels` dictionary and the `return` payload) to fall out of the function’s localized scope. 
* **The Breakthrough:** I paired manual execution tracing with targeted AI code-review prompts. By discussing the traceback errors and reviewing scoping logic with an AI collaborator, I quickly isolated the disrupted blocks, restored standard 4-space indentation levels, and ensured the inner data objects correctly inherited the function's local scope variables.

#### 4. System-Level Dependency Complications (`zxcvbn` Installation Failure)
* **The Challenge:** When attempting to integrate Dropbox's open-source `zxcvbn` entropy estimator on a Kali Linux environment, standard deployment failed with a critical `externally-managed-environment` blocker (PEP 668 protection protocol). 
* **The Breakthrough:** Instead of blindly copying fixes, I used AI to break down the underlying cause of PEP 668. Through iterative technical discussions, I learned that modern security-focused distributions block global `pip` modifications to preserve core operating system tools. This structured dialogue allowed me to evaluate options dynamically, leading me to safely bypass the barrier using explicit system flags (`--break-system-packages`) for immediate practice, while documenting isolated Virtual Environment (`venv`) architecture for production-grade workflows.

---

## 📦 Installation & Setup

Since modern Linux distributions (like Kali) use PEP 668 to manage external environments, install the dependencies safely using one of these methods:

### Option A: Quick Install (For Quick Testing)
```bash
pip install zxcvbn --break-system-packages
