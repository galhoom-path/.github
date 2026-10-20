# 🛤️ Galhoom Path

### Backend journey — five tracks in order

Same standards (structure, practice, official sources). **One pipeline** — each track unlocks the next.

```text
1. 📘 Study            →  learn a subject deeply (you write every line)
2. 🧭 Foundations      →  stack-agnostic backend concepts (HTTP, data, design, ops)
3. 🧠 Problem Solving  →  DSA patterns with real coding problems
4. 🎤 Interview Prep   →  real interview answer banks / role prep
5. 🏗️ Projects         →  learn-by-doing practice builds (public · not market products)
```

```text
Recommended flow (do not skip tracks):

  1.Study  ──▶  2.Foundations  ──▶  3.Problem Solving  ──▶  4.Interview Prep  ──▶  5.Projects
     │                │                      │
   1.1 → 1.2…      2.1                  3.1 → 3.2
```

> ⚠️ **Don’t mix these up**  
> • Study’s `02-Interview-Questions/` ≠ Track **4** Interview Prep  
> • Study’s `03-Visual-Maps/` then `04-Final-Project/` ≠ Track **5** Projects (practice builds)  
> • Foundations ≠ a PHP/Laravel Study series (no Lectures → Interviews → Visual Maps → Final Project)  
> • Track **5** Projects ≠ real market products with users — those stay **private**; this track is **learn by doing**

Maintained by [**@Galhoom22**](https://github.com/Galhoom22).

> 🔒 **Order is enforced:** canonical registry → [`path-registry.json`](https://github.com/galhoom-path/.github/blob/main/path-registry.json) · agent rules → [`AGENTS.md`](https://github.com/galhoom-path/.github/blob/main/AGENTS.md) · CI → *Validate Galhoom Path order*. New org repos must get the next **`N.M`** ID in the correct track — never a random slot.

---

### How to read the numbers

| Pattern | Meaning | Example |
|:---|:---|:---|
| **Track N** | Step **N** in the journey | Track **1** = Study (start here) |
| **N.M** | Repo **M** inside Track **N** (do in order) | **1.1** = php-fundamentals |
| Progress bar | Maintainer completion toward **100%** · 20 blocks · `█` done · `░` left | `[████░░░░░░░░░░░░░░░░] 20%` |
| **Complete?** | `⬜` = not finished · `✅` = maintainer marked **100%** for the current curriculum | See below |

> **Right now:** finish **1.1** first. Every other ID stays queued until then.

---

### Completion & living updates

| Rule | Meaning |
|:---|:---|
| **No repo is finished today** | **Zero** active repos have `✅`. Published notes, answer banks, or code ≠ “complete”. |
| **`✅` = 100% only** | When a repo hits **100%** of its current curriculum / milestones, it gets a clear **`✅ Complete`** mark here so later visitors know it was finished. |
| **Living repos** | Even after `✅`, the same repo keeps getting **periodic updates** (new language versions, new chapters, fixes). Example: curriculum targets **PHP 8.5+** now; when **PHP 8.6** ships, new material lands **in that same repo** — not a separate “done forever” archive. |
| **Progress bar** | Tracks **maintainer progress to 100%**, not “how much content exists on disk”. |

> ⚠️ **Do not treat a full-looking folder as finished.** Until you see **`✅ Complete`** on this org profile, assume the repo is still **in progress**.

---

### Contents

| # | Section |
|:---:|:---|
| **1** | [Current focus](#1--current-focus) |
| **2** | [Path progress](#2--path-progress) |
| **3** | [Pick a track](#3--pick-a-track) |
| **4** | [Track 1 — Study](#4--track-1--study-learning-series) |
| **5** | [Track 2 — Foundations](#5--track-2--foundations) |
| **6** | [Track 3 — Problem Solving](#6--track-3--problem-solving) |
| **7** | [Track 4 — Interview Prep](#7--track-4--interview-prep) |
| **8** | [Track 5 — Projects](#8--track-5--projects) |
| **9** | [Shared principles](#9--shared-principles) |
| **10** | [New here?](#10--new-here) |
| **11** | [Maintainer](#11--maintainer) |

---

## 1 · Current focus

<div align="center">

### **1.1** · 🐘 [php-fundamentals](https://github.com/galhoom-path/php-fundamentals)

**Track 1 · Study · Learning Series #1**  
Core PHP 8.5+ (no OOP) — Lectures → Interview Questions → Visual Maps → Final Project

| # | Item | Detail |
|:---:|:---|:---|
| **1** | **ID** | **1.1** — first repo in Track 1 · first step in the whole path |
| **2** | **Progress** | **0 / 30** lectures |
| **3** | **Bar** | `[░░░░░░░░░░░░░░░░░░░░] **0%**` |
| **4** | **Next lecture** | Lecture 01 — *Why Static Pages Are Not Enough* |
| **5** | **After 1.1** | Continue Study **1.2 → …**, then Track **2** Foundations |
| **6** | **Complete?** | ⬜ **Not finished** — `✅` only when this repo hits **100%** (still gets living updates afterward) |

[![Open php-fundamentals](https://img.shields.io/badge/Open-1.1%20php--fundamentals-2563EB?style=for-the-badge)](https://github.com/galhoom-path/php-fundamentals)
[![Lectures](https://img.shields.io/badge/Lectures-0%2F30-lightgrey?style=for-the-badge)](https://github.com/galhoom-path/php-fundamentals#-my-progress)
[![Status](https://img.shields.io/badge/Status-Current%20focus-F59E0B?style=for-the-badge)](https://github.com/galhoom-path/php-fundamentals)

</div>

> 📌 **Path rule:** finish **[1.1 php-fundamentals](https://github.com/galhoom-path/php-fundamentals)** before moving on. Do not jump to Foundations / DSA / interviews / projects yet.

---

## 2 · Path progress

All active repos · IDs = **Track.Repo** · journey order top → bottom.  
**Complete? = `✅` only at 100%.** Today: **none** are complete.

| ID | Track | Repository | Progress | Progress bar | Complete? | Status |
|:---:|:---|:---|:---:|:---|:---:|:---|
| **1.1** | 1️⃣ 📘 Study | [🐘 php-fundamentals](https://github.com/galhoom-path/php-fundamentals) | **0 / 30** lectures | `[░░░░░░░░░░░░░░░░░░░░] **0%**` | ⬜ | 🎯 **Current focus** |
| **1.2** | 1️⃣ 📘 Study | [🧩 php-oop](https://github.com/galhoom-path/php-oop) | **12 / 31** lectures | `[████████░░░░░░░░░░░░] **39%**` | ⬜ | ⏸️ After **1.1** |
| **2.1** | 2️⃣ 🧭 Foundations | [🧭 backend-engineering](https://github.com/galhoom-path/backend-engineering) | Notes scaffolded · **not 100%** | `[░░░░░░░░░░░░░░░░░░░░] **0%**` | ⬜ | ⏸️ After Track **1** progress |
| **3.1** | 3️⃣ 🧠 Problem Solving | [⚔️ php-problem-solving-solo-leveling](https://github.com/galhoom-path/php-problem-solving-solo-leveling) | **0 / 238** gates | `[░░░░░░░░░░░░░░░░░░░░] **0%**` | ⬜ | ⏸️ After Track **2** |
| **3.2** | 3️⃣ 🧠 Problem Solving | [🧮 LeetCode-DSA-Pareto-Set](https://github.com/galhoom-path/LeetCode-DSA-Pareto-Set) | **1 / 49** problems | `[█░░░░░░░░░░░░░░░░░░░] **2%**` | ⬜ | ⏸️ After **3.1** (or parallel once 3.1 started) |
| **4.1** | 4️⃣ 🎤 Interview Prep | [🎤 technical-interview-questions](https://github.com/galhoom-path/technical-interview-questions) | Answers drafted · **not 100%** | `[░░░░░░░░░░░░░░░░░░░░] **0%**` | ⬜ | ⏸️ After Track **3** |
| **5.1** | 5️⃣ 🏗️ Projects | [⚡ energy-conversion](https://github.com/galhoom-path/energy-conversion) | Practice build · requirements-first · **~1 / 5** epics | `[████░░░░░░░░░░░░░░░░] **~20%**` | ⬜ | ⏸️ After Track **4** |

<details>
<summary><strong>How to read status</strong></summary>

<br/>

| # | Signal | Meaning |
|:---:|:---|:---|
| **1** | 🎯 **Current focus** | Only active repo right now (**1.1**) |
| **2** | ⏸️ **After …** | Queued until the previous step in the journey |
| **3** | Progress / bar | Maintainer progress toward **100%** (not “files exist”) |
| **4** | ⬜ **Complete?** | **Not finished** — do not treat as done |
| **5** | ✅ **Complete?** | Maintainer marked **100%** for the current curriculum (still receives living updates) |

> **Snapshot:** no repo currently has `✅`. Progress numbers are updated manually when source repos change. Living updates (e.g. PHP **8.5 → 8.6**) always land in the **same** repo.

</details>

---

## 3 · Pick a track

Follow top → bottom. Each track **builds on** the one above it.

| # | Track | Why this order | Repos | Jump |
|:---:|:---|:---|:---|:---|
| **1** | **📘 Study** | First: learn to write real code in one subject | **1.1 → 1.2 → 1.3…** | [§4](#4--track-1--study-learning-series) |
| **2** | **🧭 Foundations** | Next: shared backend concepts that transfer across stacks | **2.1** | [§5](#5--track-2--foundations) |
| **3** | **🧠 Problem Solving** | Then: train patterns & fluency (PHP gates → Pareto DSA) | **3.1 → 3.2** | [§6](#6--track-3--problem-solving) |
| **4** | **🎤 Interview Prep** | Then: practice answering real interview questions | **4.1** | [§7](#7--track-4--interview-prep) |
| **5** | **🏗️ Projects** | Last: **learn by doing** — public practice builds (not market products) | **5.1** | [§8](#8--track-5--projects) |

---

## 4 · Track 1 — Study (Learning Series)

**Position in journey:** Step **1 / 5** — start here.  
**Unlocks:** Track **2** Foundations (and everything after).

**Order rule:** finish **1.1**, then **1.2**, then **1.3**… Never skip ahead in the series.

Each Study repo teaches **one subject** with the same method:

```text
Inside every Study repo:
  1. 📚 Lectures
  2. 💼 Interview Questions (subject-mapped)   ← NOT Track 4
  3. 🗺️ Visual Maps
  4. 🏗️ Final Project                          ← NOT Track 5
```

✍️ You write every line of code yourself. Guides teach. Official documentation is the source of truth.  
🔗 Repos form a **series with no repeated lessons** — each one starts exactly where the previous one stops.

### How to study

| Step | What you do |
|:---:|:---|
| **1** | Open the **lowest unfinished ID** below (right now: **1.1**) |
| **2** | Open that repo’s root `README.md` and follow **How to Start** |
| **3** | Study **one lecture per session**. Type every example. Run the code. Fill the review card |
| **4** | After all lectures, practice the **subject interview questions** (one per session) |
| **5** | Draw the **visual maps** (one per session) |
| **6** | Build the **final project** milestone by milestone |
| **7** | Move to the **next Study ID** (e.g. **1.1 → 1.2**). After the series advances, enter Track **2** |

> ✍️ **Rule:** the tutor (or AI assistant) shows and explains. **You** write, save, and run the code.

### Repos in Track 1 (do in order)

| ID | Repository | What you learn | Progress | Progress bar | Complete? | Status |
|:---:|:---|:---|:---:|:---|:---:|:---|
| **1.1** | 🐘 [php-fundamentals](https://github.com/galhoom-path/php-fundamentals) | Core PHP 8.5+ — variables, types, functions, arrays, web basics. **No OOP.** | **0 / 30** lectures | `[░░░░░░░░░░░░░░░░░░░░] **0%**` | ⬜ | 🎯 **Current focus** |
| **1.2** | 🧩 [php-oop](https://github.com/galhoom-path/php-oop) | Object-oriented PHP — classes, interfaces, traits, enums, exceptions, namespaces, PHPUnit | **12 / 31** lectures | `[████████░░░░░░░░░░░░] **39%**` | ⬜ | ⏸️ After **1.1** |
| **1.3** | 🎯 `php-ood` | Object-oriented design — SOLID, GRASP, and design principles on top of OOP | — | `[░░░░░░░░░░░░░░░░░░░░] **—**` | ⬜ | ⬜ Planned |
| **1.4** | 🎨 `php-design-patterns` | Design patterns — creational, structural, and behavioral (after OOD) | — | `[░░░░░░░░░░░░░░░░░░░░] **—**` | ⬜ | ⬜ Planned |
| **1.5+** | 🛠️ Laravel, Filament, tooling, backend stack… | Same method, next subjects in the path | — | `[░░░░░░░░░░░░░░░░░░░░] **—**` | ⬜ | ⬜ Planned |

> 🧭 **Series rule:** a topic taught in one Study repo is **never** re-taught in another.  
> 🎯 **Right now:** complete **1.1** before **1.2**.

### What’s inside every Study repo

```text
📦 subject-repo/          ← e.g. 1.1 php-fundamentals
│
├── 📂 01-Lectures/              ← step 1 · curriculum
├── 📂 02-Interview-Questions/   ← step 2 · subject practice (≠ Track 4)
├── 📂 03-Visual-Maps/           ← step 3 · diagrams / system maps
├── 📂 04-Final-Project/         ← step 4 · Study capstone (≠ Track 5)
├── 📄 README.md
└── 📄 template.md
```

Global Study blueprint: **[study-template](https://github.com/galhoom-path/study-template)** → [`template.md`](https://github.com/galhoom-path/study-template/blob/main/template.md)

---

## 5 · Track 2 — Foundations

**Position in journey:** Step **2 / 5** — after Study is underway.  
**Needs:** Track **1** coding fluency (at least **1.1** done; better with more Study progress).  
**Unlocks:** Track **3** Problem Solving.

**Stack-agnostic** shared backend engineering — HTTP, data platforms, networking, system design, Docker/K8s literacy, DevOps/DevSecOps, API design/security, and interview practice maps.

> **Not** a Study series (no Lectures → Interviews → Visual Maps → Final Project).  
> **Not** language/framework curriculum (PHP, Laravel, … stay in Track **1**).  
> Read notes in folder order; deepen the language stack in Study separately.

| ID | Repository | Focus | Progress | Progress bar | Complete? | Status |
|:---:|:---|:---|:---:|:---|:---:|:---|
| **2.1** | 🧭 [backend-engineering](https://github.com/galhoom-path/backend-engineering) | Ordered notes: core backend → data → OS/networking/CS → API craft → system design → Linux/Docker/K8s/DevOps → practice | Notes scaffolded · **not 100%** | `[░░░░░░░░░░░░░░░░░░░░] **0%**` | ⬜ | ⏸️ After Track **1** progress |

**Method:** concepts that still matter when you switch languages — then return to Study or move to Track **3**.  
**Reminder:** files on disk ≠ finished. No `✅` until the maintainer marks **100%**.

---

## 6 · Track 3 — Problem Solving

**Position in journey:** Step **3 / 5** — after you can code and know backend basics.  
**Needs:** Track **1** (+ Track **2** concepts help).  
**Unlocks:** Track **4** Interview Prep.

**Order inside this track:**

1. **3.1** — PHP gates (same language as Study · build fluency)  
2. **3.2** — Pareto LeetCode set (interview patterns · C++ depth)

| ID | Repository | Focus | Progress | Progress bar | Complete? | Status |
|:---:|:---|:---|:---:|:---|:---:|:---|
| **3.1** | ⚔️ [php-problem-solving-solo-leveling](https://github.com/galhoom-path/php-problem-solving-solo-leveling) | PHP 8.5 DSA gym — 238 Gate stubs (E→S), Hunter Solves First. Learn + Solve | **0 / 238** gates | `[░░░░░░░░░░░░░░░░░░░░] **0%**` | ⬜ | ⏸️ After Track **2** |
| **3.2** | 🧮 [LeetCode-DSA-Pareto-Set](https://github.com/galhoom-path/LeetCode-DSA-Pareto-Set) | 49 essential LeetCode problems · Brute Force → Optimized → Optimal (C++) + flowchart | **1 / 49** problems | `[█░░░░░░░░░░░░░░░░░░░] **2%**` | ⬜ | ⏸️ After **3.1** (patterns after PHP fluency) |

**Method:** fluency first (**3.1**), then pattern depth (**3.2**) — not racing through unread solutions.

---

## 7 · Track 4 — Interview Prep

**Position in journey:** Step **4 / 5** — after Study + Foundations + Problem Solving practice.  
**Needs:** Tracks **1–3**.  
**Unlocks:** Track **5** Projects (practice builds · learn by doing).

Standalone **interview answer banks** from real interviews — not lecture checklists.

> Separate from `02-Interview-Questions/` inside Study repos (**1.x**).  
> Uneven topic counts are intentional: only questions actually asked.

| ID | Repository | Focus | Progress | Progress bar | Complete? | Status |
|:---:|:---|:---|:---:|:---|:---:|:---|
| **4.1** | 🎤 [technical-interview-questions](https://github.com/galhoom-path/technical-interview-questions) | PHP / Laravel backend **answer bank** — real questions from interviews sat by [@Galhoom22](https://github.com/Galhoom22). PHP 8.5 · Laravel 13 | Answers drafted · **not 100%** | `[░░░░░░░░░░░░░░░░░░░░] **0%**` | ⬜ | ⏸️ After Track **3** |

---

## 8 · Track 5 — Projects

**Position in journey:** Step **5 / 5** — last: **learn by doing**.  
**Needs:** Tracks **1–4** (skills + concepts + problem-solving + interview readiness).

### What this track is

Public **practice builds** so your hands stay in the work — you learn more by **building**, not by only reading.

| This track **is** | This track **is not** |
|:---|:---|
| **Learn by doing** / deliberate practice | Real market products with real users |
| **Public on purpose** — anyone can clone and practice | Client / production work (those stay **private**) |
| A safe place to apply Study + Foundations + Problem Solving | Study’s `04-Final-Project/` capstone (that stays inside **1.x**) |
| Spec-first: every repo ships **requirements** you can implement alone | A dump of solutions with no brief |

### Requirements-first (for other builders)

Every Track **5** repo will include the **requirements** needed to rebuild it yourself — even if you never open the maintainer’s implementation.

| Form | Example |
|:---|:---|
| **Written requirements** | Goals, scope, acceptance criteria, constraints |
| **API / contract specs** | OpenAPI / API contract files you implement against |
| **Mixed** | Written brief + contract + edge cases |

> 🛠️ **How to use a project as practice:** read the requirements → implement your own solution → (optional) compare later. You do **not** have to look at the reference code.

### Repos in Track 5

| ID | Repository | Focus | Progress | Progress bar | Complete? | Status |
|:---:|:---|:---|:---:|:---|:---:|:---|
| **5.1** | ⚡ [energy-conversion](https://github.com/galhoom-path/energy-conversion) | Practice build — energy metering & billing API (meters, tariffs, reconciliation · Laravel) | **~1 / 5** epics | `[████░░░░░░░░░░░░░░░░] **~20%**` | ⬜ | ⏸️ After Track **4** |

**Method:** pick a realistic domain problem → publish clear requirements → build in public as practice → keep hands busy. Real commercial/user-facing work stays **private** and is **not** listed here.

---

## 9 · Shared principles

| # | Principle | Meaning |
|:---:|:---|:---|
| **1** | 📜 **Official / primary sources** | Prefer manuals, docs, and trusted primary material |
| **2** | ✍️ **You do the work** | Reading ≠ mastery — write, run, explain |
| **3** | 🎯 **Depth over dump** | Few concepts or patterns per session |
| **4** | 🧱 **Study before Foundations** | Write code first (**1.x**), then deepen shared concepts (**2.x**) |
| **5** | 🧭 **Shared ≠ stack** | Foundations stay language-agnostic; Study owns one subject deep |
| **6** | 🏗️ **Projects = practice** | Track 5 is learn-by-doing public builds — not market products (those stay private) |
| **7** | 🤝 **Public and reusable** | Others can follow the same path |
| **8** | 🎯 **One focus at a time** | Finish **1.1** before spreading across later tracks |
| **9** | ✅ **Complete only at 100%** | `✅` appears only when the maintainer marks a repo finished for the current curriculum |
| **10** | 🔄 **Living updates** | After `✅`, version bumps (e.g. PHP **8.5 → 8.6**) still land in the **same** repo |

---

## 10 · New here?

| # | Goal | Do this |
|:---:|:---|:---|
| **1** | **Start the journey** | Open **[1.1 🐘 php-fundamentals](https://github.com/galhoom-path/php-fundamentals)** ← **current focus** |
| **2** | See the full order + bars | Jump to **[§2 Path progress](#2--path-progress)** |
| **3** | Understand track order | Read **[§3 Pick a track](#3--pick-a-track)** (1→5) |
| **4** | Later: Foundations | **[2.1 backend-engineering](https://github.com/galhoom-path/backend-engineering)** *(after Track 1)* |
| **5** | Later: PHP DSA gates | **[3.1 php-problem-solving-solo-leveling](https://github.com/galhoom-path/php-problem-solving-solo-leveling)** *(after Track 2)* |
| **6** | Later: LeetCode patterns | **[3.2 LeetCode-DSA-Pareto-Set](https://github.com/galhoom-path/LeetCode-DSA-Pareto-Set)** *(after 3.1)* |
| **7** | Later: Interview answers | **[4.1 technical-interview-questions](https://github.com/galhoom-path/technical-interview-questions)** *(after Track 3)* |
| **8** | Later: Practice builds | **[5.1 energy-conversion](https://github.com/galhoom-path/energy-conversion)** *(after Track 4 · learn by doing)* |

---

## 11 · Maintainer

Built and maintained by [**@Galhoom22**](https://github.com/Galhoom22).

💬 Questions or improvements? Open an issue on the relevant repository.

**Journey: 1 Study → 2 Foundations → 3 Solve → 4 Interview → 5 Practice builds · Start at 1.1 · 🏅 Master.**
