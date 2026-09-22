# Phase 002 — Naming and Trademark Validation Plan

**Working title:** Signalhold: The Last Relay  
**Current status:** RED / PROVISIONAL — DO NOT TREAT AS CLEARED  
**Date:** 2026-09-22

This plan is a screening and production-control procedure, not legal advice.

---

## 1. Immediate finding

A preliminary public search found:

**SIGNALHOLD**  
UK application: **UK00004235663**  
Filed: **2025-07-17**  
Published in UK Trade Mark Journal 2025/031 on 2025-08-01  
Classes shown: **9, 41, 42**  
Applicant shown: **Calum Armour**

The journal lists software-related goods/services, including AI software and software-design services.

Official record:
https://www.ipo.gov.uk/t-tmj/tm-journals/2025-031/UK00004235663.html

This does **not** establish infringement or unavailability for a videogame. It does establish enough uncertainty that the project must not spend heavily or publish publicly under the assumption that "Signalhold" is safe.

---

## 2. Freeze caused by the finding

Until the naming gate passes:

- title remains a working title in internal/repository materials;
- do not lock a final logo;
- do not publish a Steam store page;
- do not commission expensive title-dependent capsule art;
- do not print merchandise;
- do not announce the title as trademark-cleared;
- do not file a trademark application without a fuller search/strategy;
- do not acquire a large bundle of title-specific domains/handles as irreversible sunk cost.

Gameplay/system development may continue using an internal project identifier because a name change must not affect architecture.

---

## 3. Candidate search procedure

For each candidate title, search:

### Exact forms

- SIGNALHOLD
- SIGNAL HOLD
- SIGNAL-HOLD
- SIGNALHOLD: THE LAST RELAY
- THE LAST RELAY

### Fuzzy/semantic forms

Search likely phonetic, spacing, plural, suffix/prefix and concept-adjacent variants. Record why a variant was considered.

### Goods/services

Do not search by word alone. Review identical/similar marks in goods/services plausibly relevant to:

- downloadable computer/video-game software;
- computer software;
- entertainment/game services;
- online game-related services if later added;
- publishing/media services if relevant to the commercial plan.

Exact Nice classification and filing language must be confirmed at filing time; do not treat this document as classification advice.

---

## 4. Official databases to search

At minimum:

### Canada — CIPO

Canadian Trademarks Database:
https://ised-isde.canada.ca/cipo/trademark-search/

CIPO recommends using the "trademark lookup" field for a trademark-name search and supports Boolean operators/wildcards.

### United States — USPTO

Trademark Search:
https://www.uspto.gov/trademarks/search

Perform comprehensive clearance-style searches for identical and similar marks, not only exact matches.

### United Kingdom — UK IPO

Search for a trade mark:
https://www.gov.uk/search-for-trademark

The current "Signalhold" finding makes UK review mandatory.

### European Union — EUIPO / TMview

Search tools:
https://www.euipo.europa.eu/en/search-ip

Availability guidance:
https://www.euipo.europa.eu/en/trade-marks/before-applying/availability

### International — WIPO

Global Brand Database:
https://www.wipo.int/en/web/global-brand-database

WIPO itself notes that its global database does not replace searches of relevant national/regional registers.

---

## 5. Common-law and market search

Official registrations are not the entire risk picture. Also search:

- Steam;
- itch.io;
- GOG;
- Epic Games Store;
- PlayStation/Xbox/Nintendo store results as appropriate;
- App Store / Google Play if relevant;
- general web search;
- game press/database sites;
- GitHub/GitLab package/project names;
- company/business registries;
- domains;
- major social handles;
- Kickstarter/BackerKit/Patreon where relevant.

Record exact queries, date, URL and result summary.

---

## 6. Result classification

### GREEN

No material identical/similar result found after documented searches, and no counsel/owner concern remains.

Green does **not** mean guaranteed legal safety.

### AMBER

Potentially similar mark/name exists but differs in territory, goods/services, status, commercial field or overall impression. Requires written review before public use.

### RED

Identical or materially similar mark/name in overlapping software/game/entertainment space, credible earlier commercial use, active dispute, or other conflict that makes launch under the name imprudent without qualified advice.

Current "Signalhold" status: **RED / provisional** because an identical UK software-related application exists and has not been resolved in this project.

---

## 7. Required evidence packet per finalist

Create a dated folder/report containing:

- candidate;
- exact/fuzzy variants;
- CIPO result summary;
- USPTO result summary;
- UK IPO result summary;
- EUIPO/TMview result summary;
- WIPO result summary;
- storefront/common-law result summary;
- company/domain/social result summary;
- screenshots or stable URLs where legally/technically appropriate;
- relevant goods/services;
- status/owner/date of concerning records;
- risk classification;
- owner disposition;
- legal-review note if obtained.

---

## 8. Final naming gate

A public shipping/store name is not approved until:

1. the evidence packet is complete;
2. no unexplained RED result remains;
3. AMBER results have written disposition;
4. the project owner explicitly accepts the name;
5. qualified trademark counsel is consulted if the result set is materially ambiguous or if a filing/public campaign justifies it;
6. logo/key-art production is then updated to the approved name.

---

## 9. Rename resilience

The code/data architecture must not hard-code the marketing title into gameplay identifiers.

Use stable internal IDs for saves/content. A title rename must require changing presentation/store metadata, not migrating the simulation.
