"""Tests for svarog_intro_project."""

import pytest

from svarog_intro_project.svarog_intro_project import main


def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify the main entry point prints a greeting."""
    main()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out
