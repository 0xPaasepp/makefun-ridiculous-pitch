#!/usr/bin/env python3
"""Single-line pitch for the ridiculous-at-first-glance brief.

The pitch imagines hiring actors to stand in as a thriving elder
brother or sister over a family meal, purely so mum and dad quit
pressing the question of a proper career. Absurd at a glance, yet the
demand behind it — parental pressure at every gathering — is real and
recurring. Stdlib only; nothing is fetched over the network.
"""

from pathlib import Path

PITCH = (
    "We rent out actors to play your successful older sibling at family "
    "dinners, so your parents finally stop asking when you'll get a real "
    "job."
)

TARGET = Path("/output/entry.txt")

if not 1 <= len(PITCH) <= 200:
    raise SystemExit("pitch must be 1 to 200 characters")
if PITCH.strip() != PITCH or not PITCH.strip():
    raise SystemExit("pitch must not be only whitespace")
if "\n" in PITCH:
    raise SystemExit("pitch must be exactly one line")


def main() -> None:
    decoded = PITCH.encode("utf-8").decode("utf-8")
    if not 1 <= len(decoded) <= 200:
        raise SystemExit("pitch must be 1 to 200 characters")
    if not decoded.strip():
        raise SystemExit("pitch must not be only whitespace")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    # The file contains precisely the pitch; no newline is appended.
    TARGET.write_text(PITCH, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
