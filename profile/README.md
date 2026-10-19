# 🛤️ Galhoom Path

### Backend tracks — Study · Problem Solving · Interview Prep · Projects · Foundations

Five tracks. Same standards (structure, practice, official sources). Different repo types.

```text
📘 Study           →  learn a subject (Lectures → repo interview set → Final Project)
🧠 Problem Solving →  master DSA patterns with real coding problems
🎤 Interview Prep  →  real interview answer banks / role prep (standalone repos)
🏗️ Projects        →  production / portfolio applications (not Study capstones)
🧭 Foundations     →  stack-agnostic shared backend notes (not a language Study series)
```

> ⚠️ **Important:** *Interview questions inside a Study repo* are lecture-mapped practice for that subject.  
> The **Interview Prep** track below is a **different** thing — dedicated interview repositories, not PHP/OOP lecture checklists.  
> Likewise, **Projects** are real portfolio apps — **not** the `03-Final-Project/` folder inside a Study repo.  
> **Foundations** is curated shared backend knowledge — **not** Lectures → Interview → Final Project, and **not** a PHP/Laravel curriculum.

Maintained by [**@Galhoom22**](https://github.com/Galhoom22).

---

## 🗺️ Pick a track

| Track | What it is | Start here |
|:---|:---|:---|
| **📘 Study** | Ordered subject series. You write every line. Official docs. | [Learning Series](#-track-1--study-learning-series) |
| **🧠 Problem Solving** | Pattern-focused problem sets (LeetCode / DSA). | [Problem Solving](#-track-2--problem-solving) |
| **🎤 Interview Prep** | Standalone interview answer banks (not the folders inside Study repos). | [Interview Prep](#-track-3--interview-prep) |
| **🏗️ Projects** | Production and portfolio applications (not Study final projects). | [Projects](#-track-4--projects) |
| **🧭 Foundations** | Stack-agnostic backend engineering notes that transfer across languages. | [Foundations](#-track-5--foundations) |

---

## 📘 Track 1 — Study (Learning Series)

Each Study repo teaches **one subject** with the same method:

```text
📚 Lectures  →  💼 Interview Questions (subject-mapped)  →  🏗️ Final Project
```

✍️ You write every line of code yourself. Guides teach. Official documentation is the source of truth.  
🔗 Repos form a **series with no repeated lessons** — each one starts exactly where the previous one stops.

### How to study

| Step | What you do |
|:---:|:---|
| **1️⃣** | Pick the **first repo you have not finished** in the table below |
| **2️⃣** | Open that repo’s root `README.md` and follow **How to Start** |
| **3️⃣** | Study **one lecture per session**. Type every example. Run the code. Fill the review card |
| **4️⃣** | After all lectures, practice the **subject interview questions** (one per session) |
| **5️⃣** | Build the **final project** milestone by milestone |
| **6️⃣** | Move to the **next Study repo** when the previous track is complete |

> ✍️ **Rule:** the tutor (or AI assistant) shows and explains. **You** write, save, and run the code.

### Learning Series

| Order | Repository | What you learn | Status |
|:---:|:---|:---|:---|
| **1** | 🐘 [php-fundamentals](https://github.com/galhoom-path/php-fundamentals) | Core PHP 8.5+ — variables, types, functions, arrays, web basics. **No OOP.** | 🟢 Active |
| **2** | 🧩 [php-oop](https://github.com/galhoom-path/php-oop) | Object-oriented PHP — classes, interfaces, traits, enums, exceptions, namespaces, PHPUnit | 🟢 Active |
| **3** | 🎯 `php-ood` | Object-oriented design — SOLID, GRASP, and design principles on top of OOP | ⬜ Planned |
| **4** | 🎨 `php-design-patterns` | Design patterns — creational, structural, and behavioral (after OOD) | ⬜ Planned |
| **5+** | 🛠️ Laravel, Filament, tooling, backend stack… | Same method, next subjects in the path | ⬜ Planned |

> 🧭 **Series rule:** a topic taught in one Study repo is **never** re-taught in another.

### What’s inside every Study repo

```text
📦 subject-repo/
│
├── 📂 01-Lectures/              ← curriculum + one folder per lecture
├── 📂 02-Interview-Questions/   ← subject-mapped practice (NOT Track 3)
├── 📂 03-Final-Project/         ← Study capstone (NOT Track 4 Projects)
├── 📄 README.md                 ← progress dashboard and how to start
└── 📄 template.md               ← shared Study blueprint
```

Global Study blueprint: **[study-template](https://github.com/galhoom-path/study-template)** → [`template.md`](https://github.com/galhoom-path/study-template/blob/main/template.md)

---

## 🧠 Track 2 — Problem Solving

Algorithms, data structures, and coding-interview patterns. **Not** Study repos.

| Repository | Focus | Status |
|:---|:---|:---|
| 🧮 [LeetCode-DSA-Pareto-Set](https://github.com/galhoom-path/LeetCode-DSA-Pareto-Set) | 49 essential LeetCode problems covering core DSA interview patterns. Each problem: Brute Force → Optimized → Optimal (C++) + flowchart | 🟢 Active |
| ⚔️ [php-problem-solving-solo-leveling](https://github.com/galhoom-path/php-problem-solving-solo-leveling) | PHP 8.5 DSA gym — 238 Gate stubs (E→S), Hunter Solves First. Learn + Solve, not a solutions dump | 🟢 Active |

**Method in this track:** deepen patterns (Pareto depth in C++) and build fluency (PHP Gate climb) — not racing through unread solutions.

---

## 🎤 Track 3 — Interview Prep

Standalone **interview answer banks** from real interviews — not lecture checklists.

> This track is **separate** from `02-Interview-Questions/` inside Study repos.  
> Uneven topic counts are intentional: only questions actually asked — not a filled curriculum.

| Repository | Focus | Status |
|:---|:---|:---|
| 🎤 [technical-interview-questions](https://github.com/galhoom-path/technical-interview-questions) | PHP / Laravel backend interview **answer bank** — real questions from interviews sat by [@Galhoom22](https://github.com/Galhoom22). Study-order topics, model answers (PHP 8.5 · Laravel 13). Not a course, not a scraped dump. | 🟢 Active |

---

## 🏗️ Track 4 — Projects

Production and portfolio applications — work you show in a hiring conversation.

> This track is **separate** from `03-Final-Project/` inside Study repos.  
> Study capstones teach a subject. **Projects** are shipped (or shippable) applications with a real domain.

| Repository | Focus | Status |
|:---|:---|:---|
| ⚡ [energy-conversion](https://github.com/galhoom-path/energy-conversion) | Energy metering & billing API — meters, tariffs, reconciliation (Laravel) | 🟢 Active |

**Method in this track:** build for a real problem, keep architecture honest, document what a visitor should open first. Showcase projects may live under the org or under [@Galhoom22](https://github.com/Galhoom22) until moved into `galhoom-path`.

---

## 🧭 Track 5 — Foundations

**Stack-agnostic** shared backend engineering — HTTP, data platforms, networking, system design, Docker/K8s literacy, DevOps/DevSecOps, API design/security, and interview practice maps.

> This track is **not** a Study series (no Lectures → Final Project).  
> It is **not** language/framework curriculum (PHP, Laravel, Node, Django, … stay in Study or separate stack repos).  
> Use it **alongside** any Study path: ideas that still matter when you switch languages.

| Repository | Focus | Status |
|:---|:---|:---|
| 🧭 [backend-engineering](https://github.com/galhoom-path/backend-engineering) | Ordered notes: core backend → data (SQL/Postgres/Redis/Mongo) → OS/networking/CS → API craft → system design → Linux/Docker/K8s/DevOps → professional practice | 🟢 Active |

**Method in this track:** read in folder order; treat notes as transferable concepts; deepen a language stack in Study repos separately.

---

## ⭐ Shared principles

| | Principle | Meaning |
|:---:|:---|:---|
| 📜 | **Official / primary sources** | Prefer manuals, docs, and trusted primary material |
| ✍️ | **You do the work** | Reading ≠ mastery — write, run, explain |
| 🎯 | **Depth over dump** | Few concepts or patterns per session |
| 🧱 | **Foundations before frameworks** | Study track stays ordered on purpose |
| 🧭 | **Shared ≠ stack** | Foundations stay language-agnostic; Study owns one subject deep |
| 🏗️ | **Projects ≠ Study capstones** | Portfolio apps prove shipping; Study finals prove the subject |
| 🤝 | **Public and reusable** | Others can follow the same path |

---

## 🏁 New here?

| Goal | Do this |
|:---|:---|
| Learn PHP from zero | Start **[🐘 php-fundamentals](https://github.com/galhoom-path/php-fundamentals)** |
| Shared backend concepts (any stack) | Open **[🧭 backend-engineering](https://github.com/galhoom-path/backend-engineering)** |
| Practice DSA patterns (C++) | Open **[🧮 LeetCode-DSA-Pareto-Set](https://github.com/galhoom-path/LeetCode-DSA-Pareto-Set)** |
| Practice DSA in PHP | Open **[⚔️ php-problem-solving-solo-leveling](https://github.com/galhoom-path/php-problem-solving-solo-leveling)** |
| Backend interview answers | Open **[🎤 technical-interview-questions](https://github.com/galhoom-path/technical-interview-questions)** |
| See shipped work | Open **[⚡ energy-conversion](https://github.com/galhoom-path/energy-conversion)** |

---

## 🛠️ Maintainer

Built and maintained by [**@Galhoom22**](https://github.com/Galhoom22).

💬 Questions or improvements? Open an issue on the relevant repository.

**📘 Study. 🧠 Solve. 🎤 Interview. 🏗️ Build. 🧭 Foundations. 🏅 Master.**
