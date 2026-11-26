"""One-line entry for make.fun: The Funniest Out-of-Office."""

import os

# An out-of-office reply from a brain that has also left.

LINE = "I'm out of office and my brain is too. Your email will be read, judged, and possibly answered sometime after my will to live returns."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
