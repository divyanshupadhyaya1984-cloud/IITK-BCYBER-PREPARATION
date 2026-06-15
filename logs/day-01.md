# Day 01: June 15, 2026
* **Core Focus:** Cybersecurity Principles, Network Foundations & LAN Architecture
* **Platform Used:** TryHackMe (Intro to Cyber Security & Intro to LAN Rooms)

## 🧠 Concepts Learned

### 1. Security Architecture & The CIA Triad
* **Confidentiality:** Preventing unauthorized access to sensitive data.
* **Integrity:** Ensuring data remains unaltered, complete, and trustworthy during transmission.
* **Availability:** Guaranteeing system uptime and access for authorized entities.
* Analyzed the distinct operational methodologies of **Red Teaming** (Offensive/Exploitation) and **Blue Teaming** (Defensive/Mitigation).

### 2. Local Area Network (LAN) Architecture
* **LAN Definition:** A network topology restricted to a localized physical area (e.g., a home, office, or lab) connecting local devices together.
* **Core Network Hardware:**
  * **Network Interface Card (NIC):** The physical hardware or chip on a device that allows it to interface with a network.
  * **Switches:** Hardware that operates within a LAN to forward data packets *exclusively* to the specific device they are addressed to, utilizing MAC addresses.
  * **Routers:** Routing devices that connect completely separate networks (like bridging a private LAN to the public internet) and direct packets across them using IP addresses.
* **Device Identification:**
  * **MAC Address:** A permanent, hardcoded physical address unique to every network interface card (e.g., `00:1A:2B:3C:4D:5E`).
  * **IP Address:** A logical, dynamically assigned network identifier (e.g., `192.168.1.1`).

## 🛠️ Practical Tasks Completed
* Configured the TryHackMe terminal workspace and initiated the **Pre-Security** learning path.
* Completed the introductory security modules, assessing historical data breach scenarios.
* Completed the **Intro to LAN** interactive module, mapping how a data packet travels from a host device through a local switch to reach a local gateway router.

## 🚀 Obstacles & Breakthroughs
* *Obstacle:* Differentiating between the roles of a Switch and a Router was confusing initially since both handle data transfer.
* *Breakthrough:* I isolated their functions logically. A switch acts like an indoor intercom system within a single building (LAN) using MAC addresses, while a router acts like the postal service delivering letters between completely different cities (WAN) using IP addresses. This structural distinction made the entire architecture click.

## 📝 Tomorrow's Goal
Transition from theoretical networking to hands-on host management by launching **Linux Fundamentals Part 1** on TryHackMe to master Command Line Interface (CLI) navigation.
