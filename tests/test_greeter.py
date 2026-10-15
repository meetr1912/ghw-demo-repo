"""Unit tests for :mod:`src.greeter`."""

from src.greeter import DEFAULT_NAME, greet, main


def test_greet_with_name():
    assert greet("Ada") == "Hello, Ada! Welcome to Global Hack Week."


def test_greet_defaults_to_world():
    assert greet() == f"Hello, {DEFAULT_NAME}! Welcome to Global Hack Week."


def test_greet_ignores_blank_name():
    assert greet("   ") == f"Hello, {DEFAULT_NAME}! Welcome to Global Hack Week."


def test_greet_strips_whitespace():
    assert greet("  Ada  ") == "Hello, Ada! Welcome to Global Hack Week."


def test_main_prints_one_line_per_name(capsys):
    assert main(["Ada", "Grace"]) == 0
    out = capsys.readouterr().out.strip().splitlines()
    assert out == [
        "Hello, Ada! Welcome to Global Hack Week.",
        "Hello, Grace! Welcome to Global Hack Week.",
    ]


def test_main_defaults(capsys):
    assert main([]) == 0
    out = capsys.readouterr().out.strip()
    assert out == f"Hello, {DEFAULT_NAME}! Welcome to Global Hack Week."
