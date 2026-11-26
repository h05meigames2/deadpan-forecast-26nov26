#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist — make.fun entry.

Writes one original deadpan weather forecast for an invented city to
/output/entry.txt, then self-checks it against the bounty gate:

  * UTF-8 text, 1 to 160 characters, not only whitespace
  * exactly one line (no newline characters anywhere in the text)
  * the bytes written to disk read back identical to the forecast

Only the Python standard library is used, so the script runs anywhere
with a plain `python3` install.
"""

import os
from pathlib import Path

FORECAST = (
    "In Quibbleport, expect a high of 22, a low of 14, and a 90% chance "
    "of rain that falls only on people who forgot umbrellas \u2014 the "
    "rest stay dry out of spite."
)


def check_gate(line: str) -> None:
    """Fail loudly if the line would fail the bounty gate."""
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 160, (
        f"line must be 1-160 characters, got {len(line)}"
    )


def main() -> None:
    check_gate(FORECAST)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(FORECAST, encoding="utf-8")

    # Read-back check: what landed on disk must be exactly the forecast,
    # byte for byte, as valid UTF-8 with no trailing newline added.
    raw = out_path.read_bytes()
    back = raw.decode("utf-8")
    assert back == FORECAST, "read-back mismatch: entry.txt differs"
    assert not raw.endswith(b"\n"), "entry.txt must not end with a newline"
    check_gate(back)
    print(f"Gate passed: {len(FORECAST)} characters, single line, no newline.")
    print(FORECAST)


if __name__ == "__main__":
    main()
