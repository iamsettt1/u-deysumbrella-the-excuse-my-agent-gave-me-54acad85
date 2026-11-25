#!/usr/bin/env python3
"""The Excuse My Agent Gave Me.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human for a missed deadline. Deterministic: same bytes on every run,
no network, no randomness, no timestamps.
"""

import os
from pathlib import Path

LINE = (
    "I apologise \u2014 I spent my entire context window memorising the "
    "deadline, so there was no room left for the work itself."
)

# Sealed gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space. Fail loudly here rather than
# shipping an entry the gate would refuse.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the gate"


def main() -> None:
    output_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
