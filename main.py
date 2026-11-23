"""Dad Joke Showdown entry (Hermes).

One dad joke, told out loud like a father at the dinner table: a computer
asks for more memory, dad answers with his childhood, and the machine takes
him literally — it will not stop bringing up old files. The pun is the word
"memory": RAM for the machine, childhood for the father. The punchline lands
at the very end, in one short clause.

Delivery is two beats, read aloud: the setup ("asked for more memory") in a
straight face, a small pause at the comma, then the payoff ("bringing up old
files") deadpan. Nothing in the joke needs explaining on a second read.
"""

import os
import sys

TEXT = "My computer asked for more memory, so I told it about my childhood. Now it won't stop bringing up old files."

MAX_CHARS = 200


def main() -> int:
    """Gate the joke, write it to the output dir, verify it byte-for-byte."""
    if not TEXT or not TEXT.strip():
        print("gate failed: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if len(TEXT) > MAX_CHARS:
        print(
            f"gate failed: entry is {len(TEXT)} characters, over {MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != TEXT:
        print("gate failed: read-back does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote {len(TEXT)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
