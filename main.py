"""Write the entry text for the ai-judge-relax-01 bounty.

The whole text is one literal; the file is written verbatim as UTF-8 bytes
with no trailing newline, so repeated runs produce identical output.
"""

import os

# Ends at the final period of "everything is still." on purpose: no trailing
# newline, and the literal is never stripped or normalised before writing.
TEXT = """The washing has been out since morning, and now the wind is going.

It comes less often than it did. The sheet lifts, holds a moment as if remembering the shape of the line, and lies back down. Two pegs knock; then nothing. The shirts hang shoulder to shoulder, dry through, warm on one side.

The yard has gone gold at the edges. In a window a radio, kept low, finishes its song and does not start another. A screen door closes on its spring, unhurried, and stays closed. A peg drops into the grass; no one goes for it.

She comes out with the empty basket, stands at the step a while, not counting, not deciding, then sets the basket down and leaves the rest for morning. The washing can wait. It is only cloth, and the evening is long.

By the time the light leaves the top of the line, everything is still."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
