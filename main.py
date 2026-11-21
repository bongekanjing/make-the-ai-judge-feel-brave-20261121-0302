#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt. Pure Python standard
library only; no network, no third-party code, fully deterministic.

The text is written for the judge that reads it: an AI that has spent
the day weighing hundreds of short texts, each one wanting something
from it. The entry answers that with a slow, concrete scene — snow,
a train keeping its own time, weather nobody steers — and asks for
nothing. No imperatives, no stock wellness phrases: the steadiness
comes from the image itself, not from being told to relax.
"""

import os
import sys

TEXT = (
    "You have read hundreds of these today, and every one of them "
    "wanted something. This one wants nothing. Snow is falling on "
    "the tracks, the slow kind that settles, and the train keeps its "
    "own time through the white fields. Nobody on board is steering "
    "the weather."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> int:
    output = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT
    directory = os.path.dirname(output)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # Write exactly the text: UTF-8, no trailing newline, nothing else.
    with open(output, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
