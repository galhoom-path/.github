# Galhoom Path — organization meta

> Powers the [org homepage](https://github.com/galhoom-path) and the **canonical journey order**.

## What’s here

| Path | Role |
|:---|:---|
| [`profile/README.md`](./profile/README.md) | Org profile (rendered on [github.com/galhoom-path](https://github.com/galhoom-path)) |
| [`GITHUB_SURFACES.md`](./GITHUB_SURFACES.md) | Org + personal + pins / About rules — **read before editing faces** |
| [`path-registry.json`](./path-registry.json) | Source of truth for track order and repo IDs |
| [`AGENTS.md`](./AGENTS.md) | Rules for AI / maintainers placing new repos |
| [`scripts/validate_path.py`](./scripts/validate_path.py) | CI check: registry ↔ profile stay aligned |

## Journey (org tracks — do not reorder casually)

```text
1 Study → 2 Foundations → 3 Problem Solving → 4 Interview Prep → 5 Projects
```

## Inside every Study repo (Track 1)

```text
Lectures → Interview Questions → Visual Maps → Final Project
Learn       Explain               Map            Build
```

Blueprint: [study-template](https://github.com/galhoom-path/study-template) · Current focus *(maintainer priority, not skill level)*: **1.1** [php-fundamentals](https://github.com/galhoom-path/php-fundamentals)

## Validate locally

```bash
python scripts/validate_path.py
```

Maintainer: [@Galhoom22](https://github.com/Galhoom22)
