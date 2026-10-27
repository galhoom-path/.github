# Galhoom Path — agent rules

This repository owns the **organization profile**, **path registry**, and **surface rules**.

## Read first

1. **[`GITHUB_SURFACES.md`](./GITHUB_SURFACES.md)** — org + personal + repo About / pins (do not break).
2. **`path-registry.json`** — track order and IDs.
3. This file — placement and CI.

## Profile surface rule (org + personal)

| Surface | Job | Keep out |
|:---|:---|:---|
| **Org homepage** (`profile/README.md`) | High-level map: journey, IDs, priority, links | Lectures, how-to guides, long essays, per-repo curricula |
| **Personal profile** (`Galhoom22/Galhoom22`) | Engineer overview + track diagram + single org CTA | Study dashboards, progress bars, Built lists, duplicate org links |
| **Each subject / track repo** | Full detail | Nothing required on the org/personal face |

**Rule:** org and personal profiles answer *what is this / where do I go next?* Full teaching and implementation live **inside each repo**. Prefer cutting copy over adding sections. When in doubt, link to the repo instead of explaining it here.

**“Current focus”** = maintainer **priority / concentration** — never imply beginner skill level.

## Before you create or place any `galhoom-path` repo

1. Read **`path-registry.json`** (source of truth).
2. Follow **`placement_algorithm`** and never violate **`forbidden`**.
3. Update **`path-registry.json` first**, then **`profile/README.md`** (keep it short), then CI must pass (`python scripts/validate_path.py`).
4. Mirror diagram/CTA on **`Galhoom22/Galhoom22`** only when the personal profile would otherwise lie — still obey `GITHUB_SURFACES.md`.

## Journey (do not reorder casually)

```text
1 Study → 2 Foundations → 3 Problem Solving → 4 Interview Prep → 5 Projects
```

IDs look like **`Track.Repo`** (example: **1.1** = first Study repo = `php-fundamentals`).

## Quick placement map

| If the new repo is… | Track | Next ID pattern |
|:---|:---:|:---|
| Subject learning series (Lectures → Interviews → Visual Maps → Final Project — see [study-template](https://github.com/galhoom-path/study-template)) | **1** Study | `1.(N+1)` in series order |
| Stack-agnostic backend notes (not a language course) | **2** Foundations | `2.(N+1)` |
| DSA gym / LeetCode patterns | **3** Problem Solving | `3.(N+1)` — language fluency before interview pattern sets |
| Standalone real-interview answer bank | **4** Interview Prep | `4.(N+1)` |
| Public learn-by-doing practice build (with requirements / API contract; not a market product) | **5** Projects | `5.(N+1)` |

## Completion & living updates

- Every repo has `complete: false` until the human explicitly says it hit **100%**.
- Progress bars = maintainer progress to 100%. **Published files ≠ finished.**
- Never write **notes ready**, **bank ready**, or a full bar while `complete` is false.
- When the human marks 100%: set `complete: true` and show **`✅ Complete`** on the profile.
- After `✅`, the same repo still gets **living updates** (e.g. PHP 8.5 → 8.6 material added in-place).

## Never

- Dump a new repo into the wrong track “because it exists in the org”.
- Skip the registry and only edit the README.
- Bloat `profile/README.md` or the personal profile “for completeness”.
- Change **current focus** without setting `current_focus_id` and the README Current focus section together.
- Confuse Study `02-Interview-Questions/` with Track 4, or Study `04-Final-Project/` with Track 5. Study repos also have `03-Visual-Maps/` (internal step 3 — not an org journey track).
- Imply any repo is finished without `complete: true` + profile `✅`.
- Put real market / client / user-facing production work in Track 5 (those stay **private**). Track 5 is **practice only**, always **public**, and must include **requirements** (written and/or API contract) so others can rebuild without the reference solution.

## Sibling org — galhoom-labs

Real products (web/mobile/desktop/extensions/CLIs/games/etc.) belong in **[galhoom-labs](https://github.com/galhoom-labs)** and must follow [`galhoom-labs/.github/AGENTS.md`](https://github.com/galhoom-labs/.github/blob/main/AGENTS.md). Track 5 here stays **practice only**.

## CI

GitHub Actions runs **`Validate Galhoom Path order`** on changes to the registry or profile README. A red check means the order is wrong — fix registry + README until `python scripts/validate_path.py` prints `OK`.
