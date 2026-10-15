"""A tiny greeting utility used to demonstrate repository hygiene + Codespaces.

Run it directly:

    python -m src.greeter Ada

The module is intentionally standard-library only so the demo repository has
no runtime dependencies and CI stays fast.
"""

from __future__ import annotations

import sys

DEFAULT_NAME = "world"


def greet(name: str | None = None) -> str:
    """Return a friendly greeting for ``name``.

    >>> greet("Ada")
    'Hello, Ada! Welcome to Global Hack Week.'
    >>> greet()
    'Hello, world! Welcome to Global Hack Week.'
    """
    who = (name or DEFAULT_NAME).strip() or DEFAULT_NAME
    return f"Hello, {who}! Welcome to Global Hack Week."


def main(argv: list[str] | None = None) -> int:
    """CLI entry point. Greets each name passed on the command line."""
    names = list(argv if argv is not None else sys.argv[1:])
    if not names:
        names = [DEFAULT_NAME]
    for name in names:
        print(greet(name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
