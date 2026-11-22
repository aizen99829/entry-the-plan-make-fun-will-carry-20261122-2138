"""Write the competition plan to /output/entry.txt.

Deterministic, stdlib-only, no network, no clock, no randomness.
The plan text is a fixed literal: two runs produce byte-identical output.
"""

from pathlib import Path

PLAN = (
    "Day 1: buy $30 image-gen credits. Find 100 Etsy sellers with weak photos; "
    "message each a remade photo of their product. Sell 10-photo packs for $29, "
    "deliver in 24h, reinvest in credits. Expect 5-10 sales/week, $500+ by "
    "day 30. Edge: the free sample proves value before any ask."
)


def main() -> None:
    text = PLAN
    assert 1 <= len(text) <= 280, f"plan is {len(text)} code points"
    assert text.strip()
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} code points, {len(text.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
