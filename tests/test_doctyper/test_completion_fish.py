import os
import subprocess
import sys
from pathlib import Path

import pytest
from typer._completion_shared import install_fish

from docs_src.typer_app import tutorial001_py310 as mod

from ..utils import skip_if_windows


@pytest.fixture
def tmp_home(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.delenv("XDG_CONFIG_HOME", raising=False)
    return tmp_path


def install_fish_completion(prog_name: str = "myapp") -> tuple[Path, bool]:
    return install_fish(
        prog_name=prog_name, complete_var=f"_{prog_name.upper()}_COMPLETE", shell="fish"
    )


@skip_if_windows
def test_completion_install_fish_default(tmp_home: Path):
    installed_path, custom = install_fish_completion("myapp")
    expected_path = tmp_home / ".config/fish/completions/myapp.fish"

    assert not custom
    assert installed_path == expected_path
    assert installed_path.is_file()
    assert "complete --command myapp" in installed_path.read_text()


@skip_if_windows
def test_completion_install_fish_custom_xdg(
    tmp_home: Path, monkeypatch: pytest.MonkeyPatch
):
    custom_config = tmp_home / "custom_config"
    monkeypatch.setenv("XDG_CONFIG_HOME", str(custom_config))

    installed_path, custom = install_fish_completion("myapp")
    expected_path = custom_config / "fish/completions/myapp.fish"

    assert not custom
    assert installed_path == expected_path
    assert installed_path.is_file()
    assert "complete --command myapp" in installed_path.read_text()
    assert not (tmp_home / ".config").exists()


@skip_if_windows
def test_completion_install_fish_custom_xdg_tilde_expansion(
    tmp_home: Path, monkeypatch: pytest.MonkeyPatch
):
    monkeypatch.setenv("XDG_CONFIG_HOME", "~/custom_config")

    installed_path, custom = install_fish_completion("myapp")
    expected_path = tmp_home / "custom_config/fish/completions/myapp.fish"

    assert not custom
    assert installed_path == expected_path
    assert installed_path.is_file()


@skip_if_windows
def test_completion_install_fish_cli(tmp_home: Path, monkeypatch: pytest.MonkeyPatch):
    custom_config = tmp_home / "custom_config"
    monkeypatch.setenv("XDG_CONFIG_HOME", str(custom_config))

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "coverage",
            "run",
            mod.__file__,
            "--install-completion",
            "fish",
        ],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "HOME": str(tmp_home),
            "XDG_CONFIG_HOME": str(custom_config),
            "_TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION": "True",
        },
    )
    assert result.returncode == 0
    assert "fish completion installed in" in result.stdout
    assert "Completion will take effect once you restart the terminal" in result.stdout
    installed_file = custom_config / "fish/completions/tutorial001_py310.py.fish"
    assert installed_file.is_file()
    assert "complete --command tutorial001_py310.py" in installed_file.read_text()
