# 🏛️ Amazon Mechanical Turk Preservation Archive (2005–2026)
### *A Real-Time Digital Archaeology & Archival Effort on MTurk's Final Day*

[![Live Archive](https://img.shields.io/badge/🌐_Live_Mirror-Visit_Archive-success?style=for-the-badge)](https://evecount.github.io/mechanicalturk_archive/)
[![Status](https://img.shields.io/badge/Status-Permanent%20Shutdown-red.svg)](https://www.mturk.com)
[![Closure Date](https://img.shields.io/badge/Closure-September%2030%2C%202026-orange.svg)](CLOSURE_ANNOUNCEMENT_AND_FAQ.md)
[![Preserved Pages](https://img.shields.io/badge/Preserved%20Pages-22-blue.svg)](pages/)
[![Downloaded Assets](https://img.shields.io/badge/Assets%20Mirrored-57-green.svg)](assets/)

> 🌐 **Live Web Mirror:** **[https://evecount.github.io/mechanicalturk_archive/](https://evecount.github.io/mechanicalturk_archive/)**  
> Browse the fully preserved Amazon Mechanical Turk website directly in your browser with complete styling, partner logos, and the historic closure banner intact.

---

## ⚡ The Archival Effort

On **September 30, 2026**, Amazon updated `mturk.com` with a maintenance banner announcing the **permanent, immediate shutdown of Amazon Mechanical Turk**. 

Within minutes of the announcement, this digital archival effort was initiated to capture, preserve, and mirror the entirety of `mturk.com` before the infrastructure was decommissioned or redirected.

### Why This Archive Matters
Launched on **November 2, 2005**, Amazon Mechanical Turk pioneered what Jeff Bezos famously dubbed **"Artificial Artificial Intelligence"**—harnessing human cognition over the internet to perform tasks computers could not yet do.

For over **21 years**, MTurk served as the foundational bedrock of:
1. **Early Deep Learning & Computer Vision**: Powering the labeling and human verification for landmark datasets including **ImageNet**.
2. **Behavioral & Academic Social Science**: Hundreds of thousands of published university papers, psychology trials, and cognitive experiments relied on MTurk's global worker pool.
3. **The Gig Economy & Human-in-the-Loop AI**: Prototyping RLHF (Reinforcement Learning from Human Feedback), content moderation, and crowdsourced micro-work long before contemporary LLMs existed.

With MTurk permanently closing its doors, this repository stands as a permanent public record and historical snapshot of the platform on its final day.

---

## ⚠️ The Closure Announcement

On September 30, 2026, the following notice was published across the MTurk portal:

> **"Mechanical Turk will close September 30, 2026.**  
> We regularly evaluate our programs, tools, and services and make adjustments based on those assessments. Following an assessment, we've made the decision to close Amazon Mechanical Turk, effective September 30, 2026. Amazon Mechanical Turk will permanently close on September 30, 2026. For Workers and Requesters currently using the service, please visit our FAQ page to learn how you can prepare for this closure."

### 📅 Critical Closure Timeline

| Date | Phase | Details |
| :--- | :--- | :--- |
| **September 30, 2026** | **Permanent Closure** | HIT submission disabled; unsubmitted HITs expired. MTurk worker type discontinued across **AWS SageMaker Ground Truth** and **Amazon Augmented AI (A2I)**. |
| **October 30, 2026** | **Grace Period Cutoff** | Final 30-day window for Requesters to approve submitted HITs (or allow auto-approval) and award worker bonuses. Unused prepaid balances refunded within 30 days. |
| **January 28, 2027** | **Final Data Purge** | Final deadline to download historical transaction history before permanent decommission. |

👉 **Read the verbatim FAQ transcript:** [`CLOSURE_ANNOUNCEMENT_AND_FAQ.md`](CLOSURE_ANNOUNCEMENT_AND_FAQ.md)

---

## 🛠️ Archival Methodology & Deliverables

This repository is built using an autonomous Python crawler designed to capture complete fidelity:

1. **Raw Server Captures (`/pages`, `/assets`)**:
   - Exact byte-for-byte responses from `mturk.com`, `worker.mturk.com`, and `requester.mturk.com`.
   - External dependencies hosted on `a0.awsstatic.com` and `d1.awsstatic.com` (AWS Libra CSS, icons, typography).
2. **Self-Contained Offline Mirror (`/offline_browsable`)**:
   - All internal page links rewritten to relative HTML paths.
   - All CDN stylesheets and SVGs re-routed to local assets so the entire website renders faithfully offline without requiring active web servers or Internet connectivity.
3. **Crawler Source Code (`/crawler_tools`)**:
   - Includes the Python scripts (`crawl_mturk.py` and `build_offline.py`) utilized to harvest and build the mirror.

---

## 📂 Repository Structure

```
D:\Mturk_archive\
│
├── CLOSURE_ANNOUNCEMENT_AND_FAQ.md   # Verbatim transcript of closure banner & full FAQ
├── README.md                         # This archival manifest & history
│
├── offline_browsable\               # Complete, offline-browsable mirror (zero external dependencies)
│   ├── index.html                   # Homepage featuring the yellow closure banner
│   ├── help.html                    # Complete FAQs & Closure FAQs
│   ├── pricing.html                 # Final MTurk 20% / 40% fee pricing schedule
│   ├── product-details.html         # Features & product overview
│   ├── resources.html               # Developer resources & SDK documentation
│   ├── customers.html               # Enterprise customer case studies (Pinterest, Yelp, etc.)
│   ├── worker.html                  # Worker portal marketing & onboarding
│   ├── get-started.html             # Requester onboarding
│   ├── participation-agreement.html # Historic Participation Agreement
│   ├── acceptable-use-policy.html   # Acceptable Use Policy
│   ├── privacy-notice.html          # Privacy Notice
│   ├── legal-licenses.html          # Legal licenses
│   ├── worker\                      # Worker-specific help & policy pages
│   └── assets\                      # Local CSS, JS, logos, SVGs, partner icons
│
├── pages\                           # 22 raw original HTML files
├── assets\                          # 57 raw stylesheets, JS libraries, images, & fonts
├── crawler_tools\                   # Python crawler & offline generator scripts
└── raw\                             # robots.txt, sitemap.xml
```

---

## 🌐 How to Browse the Archive Offline

1. Clone or download this repository:
   ```bash
   git clone https://github.com/evecount/mechanicalturk_archive.git
   cd mechanicalturk_archive
   ```
2. Double-click or open [`offline_browsable/index.html`](file:///d:/Mturk_archive/offline_browsable/index.html) in any modern web browser.
3. Browse all pages, navigation links, and closure FAQs exactly as they appeared on September 30, 2026.

---

*Archived with care on September 30, 2026. In memory of the crowd that taught AI how to see, read, and learn.*
