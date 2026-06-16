# Day 02: June 16, 2026
* **Core Focus:** OSI Model, Operating System Internals (Windows/Linux CLI), and Web Security Basics
* **Platform Used:** TryHackMe (Pre-Security Pathway Expansion)

## 🧠 Concepts Learned

### 1. Network Data Architecture (The OSI Model)
* **OSI Model Layers:** Studied the standard 7-layer theoretical framework that standardizes network communications. Focused primarily on how data transforms across layers:
  * **Layer 3 (Network Layer):** Handles logical addressing using **Packets** (containing Source and Destination IP addresses).
  * **Layer 2 (Data Link Layer):** Handles local hardware communication by packaging packets into **Frames** (containing Source and Destination MAC addresses).
* **Data Encapsulation:** Understood how a web request moves down from the Application layer to the Physical wires, wrapping itself in headers at each step.

### 2. Operating System (OS) Architecture & Security
* **OS Introduction:** Explored the structural role of an Operating System as the core intermediary between hardware components and user applications.
* **Windows Basics:** Analyzed file systems (NTFS), processes, services, and default access controls.
* **OS Security Core:** Learned how security boundaries are enforced between standard user space and root/kernel space to prevent unauthorized privilege escalation.

### 3. Cross-Platform Command Line Interface (CLI) Mechanics
* **Linux CLI Basics:** Mastered core terminal primitives to navigate system structures directly:
  * `pwd` (print current working directory path), `ls` (list visible and hidden directory objects), and `cat` (output file contents to standard stream).
* **Windows CLI Basics:** Explored parallel administrative mechanisms using the Command Prompt (cmd) and basic execution commands (`dir` for listing, `cd` for path shifting).

### 4. Introduction to Web Security Fundamentals
* Learned how vulnerabilities manifest when servers fail to validate user inputs properly. 
* Explored basic application architecture, focusing on the client-server interaction loop via HTTP protocols.

## 🛠️ Practical Tasks Completed
* Accelerated my overall progress matrix through the TryHackMe **Pre-Security** module ecosystem.
* Launched browser-based interactive sandboxes to simultaneously execute navigation commands in Linux and Windows command-line shells.
* Simulated packet travel sequences across the 7 layers of the OSI stack, observing header manipulation in transit.

## 🚀 Obstacles & Breakthroughs
* *Obstacle:* Memorizing and mapping both Windows (`dir`, `type`) and Linux (`ls`, `cat`) terminal commands simultaneously felt structurally confusing.
* *Breakthrough:* I created a direct logic-mapping table in my notes. Instead of treating them as arbitrary syntax to memorize, I recognized that both shells are executing the exact same mathematical tree-navigation functions—they just use slightly different naming conventions. 

## 📝 Tomorrow's Goal
Deepen hands-on exposure within advanced Linux file manipulation utilities (`grep`, pipes, permissions control) and begin basic scripting structure tracking.
