#!/usr/bin/env python3
"""Validate profile/README.md against path-registry.json (Galhoom Path order)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "path-registry.json"
README_PATH = ROOT / "profile" / "README.md"


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if not REGISTRY_PATH.is_file():
        fail(f"missing registry: {REGISTRY_PATH}")
    if not README_PATH.is_file():
        fail(f"missing README: {README_PATH}")

    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    readme = README_PATH.read_text(encoding="utf-8")

    tracks = registry["tracks"]
    repos = registry["repos"]
    focus = registry["current_focus_id"]

    # 1) Track IDs must be 1..N contiguous
    track_ids = [t["id"] for t in tracks]
    if track_ids != list(range(1, len(tracks) + 1)):
        fail(f"tracks must be contiguous 1..N, got {track_ids}")

    # 2) Journey order must appear in README (by track name headings)
    for t in tracks:
        heading = f"Track {t['id']} — {t['name']}"
        if heading not in readme:
            fail(f"README missing required heading: {heading!r}")

    # Track section order: positions must increase with track id
    positions = []
    for t in tracks:
        heading = f"Track {t['id']} — {t['name']}"
        pos = readme.find(heading)
        positions.append((t["id"], pos, heading))
    for (a_id, a_pos, _), (b_id, b_pos, _) in zip(positions, positions[1:]):
        if a_pos >= b_pos:
            fail(
                f"Track headings out of order: Track {a_id} (pos {a_pos}) "
                f"must appear before Track {b_id} (pos {b_pos})"
            )

    # 3) Every registry repo ID must appear in README
    for repo in repos:
        rid = repo["id"]
        pattern = rf"(?<![0-9.]){re.escape(rid)}(?![0-9])"
        if not re.search(pattern, readme):
            fail(f"README missing repo ID {rid} ({repo['name']})")

    # 4) Within each track, repo IDs must appear in ascending order
    by_track: dict[int, list[dict]] = {}
    for repo in repos:
        by_track.setdefault(repo["track"], []).append(repo)

    for track_id, track_repos in sorted(by_track.items()):

        def minor(r: dict) -> tuple[int, str]:
            _major, _, rest = r["id"].partition(".")
            m = re.match(r"^(\d+)", rest)
            return (int(m.group(1)) if m else 0, rest)

        ordered = sorted(track_repos, key=minor)
        id_positions = []
        for r in ordered:
            m = re.search(rf"(?<![0-9.]){re.escape(r['id'])}(?![0-9])", readme)
            if not m:
                fail(f"could not locate ID {r['id']} for order check")
            id_positions.append((r["id"], m.start()))
        for (a_id, a_pos), (b_id, b_pos) in zip(id_positions, id_positions[1:]):
            if a_pos >= b_pos:
                fail(
                    f"Track {track_id} repo order broken in README: "
                    f"{a_id} (pos {a_pos}) must appear before {b_id} (pos {b_pos})"
                )

    # 5) Current focus consistency
    if not any(r["id"] == focus for r in repos):
        fail(f"current_focus_id {focus!r} not found in repos[]")
    focus_repo = next(r for r in repos if r["id"] == focus)
    if focus_repo.get("status") != "current_focus":
        fail(f"repo {focus} must have status current_focus in registry")
    focus_section = readme.split("## 1 · Current focus", 1)
    if len(focus_section) < 2:
        fail("README missing '## 1 · Current focus' section")
    section_body = focus_section[1].split("## 2 ·", 1)[0]
    if focus not in section_body:
        fail(f"Current focus section must mention {focus}")
    if focus_repo["name"] not in section_body:
        fail(
            f"Current focus section must mention repo name "
            f"{focus_repo['name']!r}"
        )

    # 6) Pipeline journey labels present (compact form OK)
    required_phrases = [
        "1. 📘 Study",
        "2. 🧭 Foundations",
        "3. 🧠 Problem Solving",
        "4. 🎤 Interview Prep",
        "5. 🏗️ Projects",
    ]
    for phrase in required_phrases:
        if phrase not in readme:
            fail(f"README missing journey phrase: {phrase!r}")

    # 7) Must not claim unfinished work is done
    banned = ("notes ready", "bank ready")
    lowered = readme.lower()
    for phrase in banned:
        if phrase in lowered:
            fail(
                f"README must not say {phrase!r} "
                "(published content is not completion)"
            )

    incomplete = [r for r in repos if r.get("complete") is not True]
    if not any(r.get("complete") is True for r in repos):
        if "No repo is finished today" not in readme and "none are complete" not in readme.lower():
            fail("When all repos are incomplete, README must state none are finished")

    print("OK: path-registry.json <-> profile/README.md order checks passed.")
    print(f"  tracks: {len(tracks)} | repos: {len(repos)} | focus: {focus}")
    print(f"  incomplete repos: {len(incomplete)}/{len(repos)}")


if __name__ == "__main__":
    main()
