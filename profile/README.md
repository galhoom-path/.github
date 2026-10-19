# 🛤️ Galhoom Path

> You are on the **Galhoom Path** organization homepage — the map for every repo below (**Study** · **Problem Solving** · **Interview Prep** · **Projects**).
### Structured, hands-on tracks for becoming a stronger software engineer

This organization is one home for **four separate tracks**. They share the same spirit (structure, practice, official sources) — but they are **not the same kind of repo**.

```text
📘 Study           →  learn a subject (Lectures → repo interview set → Final Project)
🧠 Problem Solving →  master DSA patterns with real coding problems
🎤 Interview Prep  →  real interview answer banks / role prep (standalone repos)
🏗️ Projects        →  real products / portfolio apps (shipped work, not Study capstones)
```

> ⚠️ **Important:** *Interview questions inside a Study repo* are lecture-mapped practice for that subject.  
> The **Interview Prep** track below is a **different** thing — dedicated interview repositories, not PHP/OOP lecture checklists.  
> Likewise, **Projects** are real portfolio apps — **not** the `03-Final-Project/` folder inside a Study repo.

Maintained by [**@Galhoom22**](https://github.com/Galhoom22).

---

## 🗺️ Pick a track

| Track | What it is | Start here |
|:---|:---|:---|
| **📘 Study** | Ordered subject series. You write every line. Official docs. | [Learning Series](#-track-1--study-learning-series) |
| **🧠 Problem Solving** | Pattern-focused problem sets (LeetCode / DSA). | [Problem Solving](#-track-2--problem-solving) |
| **🎤 Interview Prep** | Standalone interview answer banks (not the folders inside Study repos). | [Interview Prep](#-track-3--interview-prep) |
| **🏗️ Projects** | Shipped products / portfolio apps (not Study final projects). | [Projects](#-track-4--projects) |

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
| **3** | 🎯 `php-ood` | Object-oriented design — principles and patterns on top of OOP | ⬜ Planned |
| **4+** | 🛠️ Laravel, Filament, tooling, backend stack… | Same method, next subjects in the path | ⬜ Planned |

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

Repos for **algorithms, data structures, and coding-problem practice**.  
These are **not** Study repos (no lecture series / final project structure).

| Repository | Focus | Status |
|:---|:---|:---|
| 🧮 [LeetCode-DSA-Pareto-Set](https://github.com/galhoom-path/LeetCode-DSA-Pareto-Set) | 49 essential LeetCode problems covering core DSA interview patterns. Each problem: Brute Force → Optimized → Optimal (C++) + flowchart | 🟢 Active |

**Method in this track:** deepen patterns by solving the highest-leverage problems thoroughly — not racing through volume.

---

## 🎤 Track 3 — Interview Prep

Dedicated repositories for **interview preparation** from real interviews (answer banks, role screens, etc.).

> This track is **separate** from `02-Interview-Questions/` inside Study repos.  
> Uneven topic counts are intentional: only questions actually asked — not a filled curriculum.

| Repository | Focus | Status |
|:---|:---|:---|
| 🎤 [technical-interview-questions](https://github.com/galhoom-path/technical-interview-questions) | PHP / Laravel backend interview **answer bank** — real questions from interviews sat by [@Galhoom22](https://github.com/Galhoom22). Study-order topics, model answers (PHP 8.5 · Laravel 13). Not a course, not a scraped dump. | 🟢 Active |

---

## 🏗️ Track 4 — Projects

Repos for **real products and portfolio apps** — work you would show a hiring manager.

> This track is **separate** from `03-Final-Project/` inside Study repos.  
> Study capstones teach a subject. **Projects** are shipped (or shippable) applications with a real domain.

| Repository | Focus | Status |
|:---|:---|:---|
| ⚡ [energy-conversion](https://github.com/Galhoom22/energy-conversion) | Energy metering & billing API — meters, tariffs, reconciliation (Laravel) | 🟢 Showcase |
| 🚀 [job-board-platform](https://github.com/Galhoom22/job-board-platform) | Job board monorepo — seekers + companies (Clean Architecture) | 🟢 Showcase |

**Method in this track:** build for a real problem, keep architecture honest, document what a visitor should open first. Showcase projects may live under the org or under [@Galhoom22](https://github.com/Galhoom22) until moved into `galhoom-path`.

---

## ⭐ Shared principles

| | Principle | Meaning |
|:---:|:---|:---|
| 📜 | **Official / primary sources** | Prefer manuals, docs, and trusted primary material |
| ✍️ | **You do the work** | Reading ≠ mastery — write, run, explain |
| 🎯 | **Depth over dump** | Few concepts or patterns per session |
| 🧱 | **Foundations before frameworks** | Study track stays ordered on purpose |
| 🏗️ | **Projects ≠ Study capstones** | Portfolio apps prove shipping; Study finals prove the subject |
| 🤝 | **Public and reusable** | Others can follow the same path |

---

## 🏁 New here?

| Goal | Do this |
|:---|:---|
| Learn PHP from zero | Start **[🐘 php-fundamentals](https://github.com/galhoom-path/php-fundamentals)** |
| Practice DSA patterns | Open **[🧮 LeetCode-DSA-Pareto-Set](https://github.com/galhoom-path/LeetCode-DSA-Pareto-Set)** |
| Backend interview answers | Open **[🎤 technical-interview-questions](https://github.com/galhoom-path/technical-interview-questions)** |
| See shipped work | Open **[⚡ energy-conversion](https://github.com/Galhoom22/energy-conversion)** or **[🚀 job-board-platform](https://github.com/Galhoom22/job-board-platform)** |

---

## 🛠️ Maintainer

Built and maintained by [**@Galhoom22**](https://github.com/Galhoom22).

💬 Questions or improvements? Open an issue on the relevant repository.

**📘 Study. 🧠 Solve. 🎤 Interview. 🏗️ Build. 🏅 Master.**
