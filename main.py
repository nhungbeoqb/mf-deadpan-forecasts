#!/usr/bin/env python3
"""Deadpan forecast for Port Damp, a city that does not exist.

Writes one line (<= 160 chars) to /output/entry.txt, with a gate
self-check mirroring the scorer: UTF-8 text, 1-160 chars, not only
whitespace. Stdlib only, fully deterministic.
"""

import os
import sys

ENTRY = (
    "Port Damp: 66 degrees with 98 percent humidity, so the air is "
    "technically soup. Umbrellas optional; spoons recommended. "
    "Tomorrow: more soup."
)

MAX_CHARS = 160


def main() -> int:
    text = ENTRY
    # Gate self-check, mirroring the sealed scorer.
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"gate failed: length {len(text)} not in 1..{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    text.encode("utf-8")  # must be valid UTF-8 text

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote /output/entry.txt ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
