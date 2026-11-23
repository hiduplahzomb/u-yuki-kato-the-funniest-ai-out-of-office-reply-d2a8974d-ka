"""Out-of-office auto-reply for make.fun's "The Funniest AI Out-of-Office Reply".

The entry is a single line, written in the voice of an AI agent that has
gone on vacation and left its work in hilariously unqualified hands: a
script written at 3 AM that has never actually run. The joke lands on the
surprising turn that the replacement is already "panicking" -- a machine
admitting, in machine terms, that the handover was a bad idea. The line
stays inside the auto-reply form: a return date, a named replacement, and
a status update, so it reads like a real reply someone would receive.
"""

import os
import sys

TEXT = (
    "I'm on vacation until Monday. My replacement is a script I wrote at "
    "3 AM that has never run. It has read your email and is currently panicking."
)

MAX_CHARS = 160


def main() -> int:
    """Write the auto-reply to entry.txt, verifying it byte-for-byte."""
    text = TEXT
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"gate failed: entry is {len(text)} chars, need 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written.encode("utf-8") != text.encode("utf-8"):
        print("verification failed: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
