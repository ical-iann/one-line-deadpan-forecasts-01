"""Deadpan forecast for a city that does not exist.

Writes a single one-line forecast (<=160 chars) to /output/entry.txt.
Deterministic: no network, no randomness, no time dependence.
"""

from pathlib import Path

FORECAST = (
    "Tonight in Varnwick, a high of 54 and a low of 51, with a 60% chance "
    "of rain falling sideways, as it has done every Tuesday since 1987. "
    "Umbrellas useless."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(FORECAST, encoding="utf-8")


if __name__ == "__main__":
    main()
