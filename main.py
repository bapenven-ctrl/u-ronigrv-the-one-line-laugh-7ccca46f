#!/usr/bin/env python3
"""One-line laugh: write a single funny sentence to /output/entry.txt.

The line was written for make.fun's The One-Line Laugh bounty: one sentence,
at most 200 characters, a real surprise at the end that still makes sense,
and an everyday truth people recognise. The program is deliberately plain:
no network, no randomness, no input, no dependency outside this file.
It writes the same bytes on every run.
"""

import os

LINE = "I bought noise-cancelling headphones to focus, and now I can hear my own thoughts, which is why I returned them."
# The line is written exactly as above: no trailing newline, no BOM, 112
# code points (measured, not estimated), one sentence, inside the 200 cap.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
