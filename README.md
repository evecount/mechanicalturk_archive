# Amazon Mechanical Turk Archive (Captured September 30, 2026)

On **September 30, 2026**, Amazon announced the permanent shutdown and closure of **Amazon Mechanical Turk (MTurk)**. This repository contains the complete offline archive of the official `mturk.com` website, including all documentation, worker/requester guides, policies, pricing, and the official closure announcement & FAQ.

---

## ⚠️ The Closure Announcement

> **"Mechanical Turk will close September 30, 2026.**  
> We regularly evaluate our programs, tools, and services and make adjustments based on those assessments. Following an assessment, we've made the decision to close Amazon Mechanical Turk, effective September 30, 2026. Amazon Mechanical Turk will permanently close on September 30, 2026."

### 📅 Critical Closure Milestones

| Date | Milestone |
| :--- | :--- |
| **September 30, 2026** | **Permanent Service Closure**: HIT submission closes. All remaining unsubmitted HITs automatically expire. MTurk worker type disabled across AWS SageMaker Ground Truth & Amazon Augmented AI (A2I). |
| **October 30, 2026** | **Grace Period End**: Final deadline for Requesters to approve/reject pending HITs (30-day auto-approval window) and award worker bonuses. |
| **October 30, 2026** | **Pre-paid Refunds**: All unused prepaid Requester balances refunded within 30 days. |
| **January 28, 2027** | **Final Data Access**: Worker and Requester transaction history remains accessible until this date. |

See the full verbatim document at: [CLOSURE_ANNOUNCEMENT_AND_FAQ.md](file:///d:/Mturk_archive/CLOSURE_ANNOUNCEMENT_AND_FAQ.md)

---

## 📂 Archive Structure

```
D:\Mturk_archive\
│
├── CLOSURE_ANNOUNCEMENT_AND_FAQ.md   # Verbatim transcript of closure banner & full FAQ
├── README.md                         # This archive manifest & overview
│
├── offline_browsable\               # Self-contained offline-browsable mirror (relative asset paths)
│   ├── index.html                   # Homepage with closure banner
│   ├── help.html                    # Complete FAQs & Closure FAQs
│   ├── pricing.html                 # MTurk pricing model
│   ├── product-details.html         # Features & product overview
│   ├── resources.html               # Developer resources & SDK guides
│   ├── customers.html               # Customer case studies
│   ├── worker.html                  # Worker portal info & overview
│   ├── get-started.html             # Getting started guide
│   ├── participation-agreement.html # Legal participation agreement
│   ├── acceptable-use-policy.html   # Acceptable use policy
│   ├── privacy-notice.html          # Privacy notice
│   ├── legal-licenses.html          # Legal licenses
│   ├── worker\                      # Worker-specific help & policy pages
│   └── assets\                      # Local CSS, JS, logos, SVGs, icons
│
├── pages\                           # Raw harvested HTML pages
│   ├── index.html
│   ├── help.html
│   ├── pricing.html
│   ├── product-details.html
│   ├── resources.html
│   ├── customers.html
│   ├── worker.html
│   ├── get-started.html
│   ├── new.html (requester project creator)
│   ├── signin_options.html
│   └── ... (22 pages total)
│
├── assets\                          # All downloaded media & styles (57 assets)
│   ├── assets\css\main.css
│   ├── assets\js\*.js
│   ├── assets\images\*.svg, *.png, *.ico
│   └── d1.awsstatic.com / libra-css
│
└── raw\                             # Special endpoints (robots.txt, sitemap.xml)
```

---

## 🌐 How to Browse Offline

Open [offline_browsable/index.html](file:///d:/Mturk_archive/offline_browsable/index.html) in any web browser.  
All styling, layouts, icons, and page links are re-routed to load locally from disk.
