# Phase 002 — Third-Party Licensing Policy

**Status:** REQUIRED  
**Date:** 2026-09-22

The default production rule is: **author it ourselves unless an external asset clearly reduces risk/cost and its rights are provable.**

---

## 1. Approval classes

### AUTO-ACCEPTABLE WITH PROVENANCE

May enter production after the licensing-register row is complete:

- original project-authored work;
- commissioned work with a written transfer/license covering commercial game use;
- verified public-domain material used as source/reference where jurisdictional status is appropriate;
- CC0 material with source/provenance recorded;
- permissively licensed code whose notice/attribution requirements are understood and compatible.

### ACCEPTABLE WITH OBLIGATIONS

Requires an explicit obligation entry and credits/notices plan:

- CC BY assets;
- SIL Open Font License fonts;
- commercial marketplace assets with game-use rights;
- sample libraries whose EULA permits rendered/embedded use;
- MIT/BSD/Apache-style software dependencies.

Do not infer permissions from a marketplace download button. Read the actual license/EULA.

### REVIEW REQUIRED

Do not use as a production dependency until reviewed:

- ShareAlike/copyleft assets whose derivative or distribution effects are unclear;
- GPL/LGPL code integrated into a shipping runtime;
- assets with territory/platform restrictions;
- "royalty free" assets without a readable license;
- AI-generated material with unclear commercial terms/provenance;
- commissioned work with no written rights clause;
- fonts with unusual embedding restrictions;
- licenses that prohibit redistribution but are technically packaged in a recoverable form.

### PROHIBITED FOR THIS COMMERCIAL PROJECT WITHOUT EXPRESS OWNER + LEGAL APPROVAL

- NonCommercial licenses;
- Personal Use Only licenses;
- assets copied from another game/application;
- ripped/extracted models, textures, audio, UI or fonts;
- "found on Google/Pinterest/Discord" with no provenance;
- cracked/pirated asset packs;
- licenses whose author/source cannot be established;
- fan art or protected character/logo assets used commercially without permission;
- editorial-only material used as game content/marketing;
- deliberate living-artist imitation as a production shortcut.

---

## 2. Required licensing-register fields

Each production dependency records:

- asset/dependency ID;
- project path;
- category;
- title/name;
- author/vendor;
- source URL;
- acquisition date;
- license name/version;
- license URL or contract reference;
- commercial-use permission;
- modification permission;
- redistribution/embedding constraints;
- attribution text;
- proof/evidence location;
- reviewer;
- status;
- replacement plan;
- notes.

A blank source, license or status means **not approved**.

---

## 3. Proof retention

The public GitHub repository must not expose receipts, personal addresses, private contracts, customer data, marketplace credentials or other sensitive proof.

The register should point to a safe evidence location/reference. Retain:

- license/EULA version or dated URL;
- purchase record where relevant;
- commission agreement;
- attribution text;
- screenshots/PDFs of terms when terms may change;
- source file/version identity.

If evidence cannot be preserved, the asset is replaceable, not foundational.

---

## 4. Modification and generated derivatives

Modification does not erase license obligations.

For a derived Blender asset, record both:

1. the project's .blend/source asset; and
2. any third-party base mesh/texture/material/component used.

Generated sprites, atlases, normal maps, masks and shadows inherit whatever obligations attach to their underlying source material.

---

## 5. AI-assisted content

AI assistance is not an automatic rights guarantee.

For any AI-assisted production asset, record:

- tool/model/service;
- date;
- source inputs owned/licensed by the project;
- whether reference images were supplied;
- relevant service terms snapshot/reference;
- human modification/source file;
- confirmation that prompts did not ask for a living artist, competitor asset, protected character or logo imitation.

High-value identity assets (logo, capsule art, hero key art) require extra review and should favor project-authored/commissioned source with clean provenance.

---

## 6. Replacement rule

Every external dependency should have a plausible replacement path. A third-party asset that cannot legally ship must not hold the core simulation hostage.

If a license changes after acquisition, preserve the acquired license evidence and review whether the old grant remains valid; do not assume either continued permission or automatic revocation.

---

## 7. Shipping audit

Before demo and release:

- no UNKNOWN status rows;
- no prohibited licenses;
- all attributions/notices generated from the register;
- all external dependencies present in the build are represented in the register;
- no registered source points to a dead/ambiguous provenance chain;
- a clean checkout can identify the source and license of every third-party production dependency.
