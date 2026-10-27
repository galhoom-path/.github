# Galhoom GitHub surfaces — never break these

Canonical rules for **every** public GitHub face owned by [@Galhoom22](https://github.com/Galhoom22) / [galhoom-path](https://github.com/galhoom-path).  
Agents: read this **before** editing org profile, personal profile, repo About text, pins, or topics.

Internal method (depth vs overview) is for maintainers/agents — **do not** print labels like “Pareto” or “20/80” on public pages.

---

## 1. Three layers

| Layer | Job | Keep out |
|:---|:---|:---|
| **Personal profile** [`Galhoom22/Galhoom22`](https://github.com/Galhoom22/Galhoom22) | Working engineer overview + CTA into the org | Study dashboards, progress bars, “Built” repo lists, beginner/student vibe |
| **Org homepage** [`galhoom-path/.github` → `profile/README.md`](https://github.com/galhoom-path/.github) | High-level map: journey, IDs, priority, links | Lectures, how-tos, long essays, per-repo curricula |
| **Each repo** | Full detail | Nothing that must live only on org/personal faces |

**Rule:** faces answer *what is this / where next?* Depth lives **inside each repo**. Prefer cutting copy over adding sections. When in doubt, link — don’t re-explain.

---

## 2. Personal profile (`Galhoom22/Galhoom22` README)

### Must keep

- Hero image (`profile-map.jpg`) at the top
- Short engineer positioning (backend · PHP · Laravel · APIs)
- LinkedIn link once
- **One** Mermaid diagram: org → five tracks → main repos under each track (TB map)
- **One** CTA under the diagram: `[**Open galhoom-path →**](https://github.com/galhoom-path)` only — no “Follow the path” heading, no repeated journey one-liner under the CTA
- Short Stack line

### Must not

- Repeat **galhoom-path** / Galhoom Path more than **once** (the CTA is that one link; do not also put it in the hero row)
- List selected work / Built tables of repos (pins already show work)
- Show lecture progress, Visual Maps locks, “Learning Series”, or current-study dashboards
- Imply the maintainer is a beginner because a Study repo ID exists
- Add a second Mermaid (no LR track strip + TB map)

### Pins (profile UI)

Preferred pin set (no Study curricula on the face):

1. `galhoom-path/energy-conversion`
2. `Galhoom22/job-board-platform`
3. `galhoom-path/technical-interview-questions` (or DSA — keep work/interview/practice first)
4. `galhoom-path/backend-engineering`
5. `galhoom-path/LeetCode-DSA-Pareto-Set`
6. `galhoom-path/php-problem-solving-solo-leveling`

**Do not pin** `php-fundamentals` or `php-oop` on the personal profile.

---

## 3. Organization homepage (`profile/README.md`)

### Must keep (compact)

- One-sentence what the org is + “this page is the map; depth is in each repo”
- Journey line with the five track labels (exact emoji phrases CI expects)
- **§1 Current focus** — priority repo only
- **§2 Path progress** — one table of IDs
- Short **Track 1–5** headings with repo links (IDs for planned stubs too)
- Don’t-mix callout (Study interview ≠ Track 4; Study final ≠ Track 5; Track 5 ≠ market products)
- Link to `study-template`, `path-registry.json`, `AGENTS.md`

### Must not

- Restore long TOCs, badge walls, duplicate tables per track, “How to study” essays, principles lists of 10+
- Call “Current focus” a skill level or beginner badge

### “Current focus” meaning

**Maintainer priority / concentration** on a repo (path order).  
Not “I’m new to PHP.” Not seniority. Not “starting from zero.”

---

## 4. Repo About descriptions & topics

Track numbers on **every** `galhoom-path/*` description must match the journey:

| Track | Name | Examples |
|:---:|:---|:---|
| **1** | Study | php-fundamentals, php-oop, study-template |
| **2** | Foundations | backend-engineering |
| **3** | Problem Solving | php-problem-solving-solo-leveling, LeetCode-DSA-Pareto-Set |
| **4** | Interview Prep | technical-interview-questions |
| **5** | Practice builds / Projects | energy-conversion |

Never invent Track numbers from memory. Prefer **craft curriculum** wording over **learning / tutorial** topics on Study repos when setting topics.

---

## 5. Study repos (inside the repo)

- Four tracks: Lectures → Interviews → Visual Maps → Final Project
- Visual Maps: Mermaid must look clear on **GitHub file view** (TB, classDef, GitHub acceptance check) — see each repo’s `03-Visual-Maps/README.md` Diagram Standards and `template.md` Section 13
- Blueprint: [study-template](https://github.com/galhoom-path/study-template)

---

## 6. Order of work when changing path surfaces

1. `path-registry.json` first  
2. `profile/README.md` (keep it short)  
3. `python scripts/validate_path.py`  
4. Update personal profile **only** if the diagram/CTA would otherwise lie  
5. Fix repo descriptions/topics if track labels changed  

---

## 7. Hard bans (all surfaces)

- No beginner-student framing on the personal profile
- No duplicate org links or repeated slogans
- No mixing Study folders with org Tracks 4/5
- No claiming a repo is finished without `complete: true` + org `✅`
- No Track 5 market/client products on the public org list
- No bloating org/personal READMEs “for completeness” — completeness belongs in the subject repo

---

## 8. Sibling org — galhoom-labs (do not ignore)

**[galhoom-labs](https://github.com/galhoom-labs)** holds **real products**. Path holds **learn / practice**.

- Do **not** place Labs products under Path Track 5.
- Do **not** place Path practice-only projects in Labs.
- Personal profile is intentionally a **two-home** page (Path section + Labs section). Labs has its own Mermaid + CTA. That overrides older “single Mermaid / single org CTA only” wording above when Labs is in scope.
- Labs rules live in [`galhoom-labs/.github`](https://github.com/galhoom-labs/.github) (`AGENTS.md`, `GITHUB_SURFACES.md`, `labs-registry.json`).
