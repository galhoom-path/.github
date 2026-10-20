# Galhoom Path — agent rules

This repository owns the **organization profile** and the **canonical path order**.

## Before you create or place any `galhoom-path` repo

1. Read **`path-registry.json`** (source of truth).
2. Follow **`placement_algorithm`** and never violate **`forbidden`**.
3. Update **`path-registry.json` first**, then **`profile/README.md`**, then CI must pass (`python scripts/validate_path.py`).
4. Mirror ID / journey changes on **`Galhoom22/Galhoom22`** when the personal profile would otherwise lie.

## Journey (do not reorder casually)

```text
1 Study → 2 Foundations → 3 Problem Solving → 4 Interview Prep → 5 Projects
```

IDs look like **`Track.Repo`** (example: **1.1** = first Study repo = `php-fundamentals`).

## Quick placement map

| If the new repo is… | Track | Next ID pattern |
|:---|:---:|:---|
| Subject learning series (Lectures → interviews → final) | **1** Study | `1.(N+1)` in series order |
| Stack-agnostic backend notes (not a language course) | **2** Foundations | `2.(N+1)` |
| DSA gym / LeetCode patterns | **3** Problem Solving | `3.(N+1)` — language fluency before interview pattern sets |
| Standalone real-interview answer bank | **4** Interview Prep | `4.(N+1)` |
| Production / portfolio application | **5** Projects | `5.(N+1)` |

## Never

- Dump a new repo into the wrong track “because it exists in the org”.
- Skip the registry and only edit the README.
- Change **current focus** without setting `current_focus_id` and the README Current focus section together.
- Confuse Study `02-Interview-Questions/` with Track 4, or Study `03-Final-Project/` with Track 5.

## CI

GitHub Actions runs **`Validate Galhoom Path order`** on changes to the registry or profile README. A red check means the order is wrong — fix registry + README until `python scripts/validate_path.py` prints `OK`.
