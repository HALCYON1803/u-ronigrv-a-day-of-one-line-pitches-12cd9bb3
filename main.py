"""One-line pitch (v2): a payoff-led invitation for a friend who has never coded.

The pitch leads with what they get — an app with their name on it, tonight —
and frames the ask as a chat over coffee, not a technical task.
"""

import os

PITCH = "Tell it your idea over coffee \u2014 by tonight, there's an app with your name on it."

# The competition caps a pitch at 240 characters; keep the guard explicit.
MAX_CHARS = 240

OUTPUT_PATH = "/output/entry.txt"


def build_pitch():
    """Return the single pitch line, stripped of any extra whitespace."""
    pitch = PITCH.strip()
    assert 0 < len(pitch) <= MAX_CHARS, "pitch must fit in one line"
    return pitch


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(build_pitch() + "\n")


if __name__ == "__main__":
    main()
