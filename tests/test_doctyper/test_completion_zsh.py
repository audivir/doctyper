import os
import subprocess
import sys
from pathlib import Path

import pytest
from typer._completion_shared import install_zsh
from typer.testing import CliRunner

from docs_src.typer_app import tutorial001_py310 as mod

from ..utils import skip_if_windows

runner = CliRunner()
app = mod.app


@pytest.fixture
def tmp_home(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("ZDOTDIR", str(tmp_path))
    monkeypatch.delenv("TYPER_ZSH_COMPLETION_DIR", raising=False)
    return tmp_path


def install_zsh_completion(prog_name: str = "myapp") -> tuple[Path, bool]:
    return install_zsh(
        prog_name=prog_name, complete_var=f"_{prog_name.upper()}_COMPLETE", shell="zsh"
    )


@skip_if_windows
def test_completion_install_zsh_default_idempotent(tmp_home: Path):
    zshrc_path = tmp_home / ".zshrc"
    zshrc_path.write_text('echo "custom .zshrc"\n')

    install_zsh_completion("myapp")
    content_first = zshrc_path.read_text()
    assert 'echo "custom .zshrc"' in content_first
    assert "fpath+=~/.zfunc; autoload -Uz compinit; compinit" in content_first
    assert "zstyle ':completion:*' menu select" in content_first

    # Running a second time should not duplicate entries
    install_zsh_completion("myapp")
    assert zshrc_path.read_text() == content_first


@skip_if_windows
def test_completion_install_zsh_custom_dir(
    tmp_home: Path, monkeypatch: pytest.MonkeyPatch
):
    custom_dir = tmp_home / "custom_completions"
    monkeypatch.setenv("TYPER_ZSH_COMPLETION_DIR", str(custom_dir))
    zshrc_path = tmp_home / ".zshrc"
    zshrc_path.write_text('echo "custom .zshrc"\n')

    installed_path, custom = install_zsh_completion("myapp")

    # completion script written inside custom dir
    assert custom
    assert installed_path == custom_dir / "_myapp"
    assert installed_path.is_file()

    # .zshrc must NOT be modified
    assert zshrc_path.read_text() == 'echo "custom .zshrc"\n'

    # .compstyles created with header and program-specific zstyle
    compstyles_path = custom_dir / ".compstyles"
    assert compstyles_path.is_file()
    assert compstyles_path.read_text() == (
        "# this file is managed by typer, do not edit\n"
        "zstyle ':completion:*:*:myapp:*' menu select\n"
    )


@skip_if_windows
def test_completion_install_zsh_custom_dir_tilde_expansion(
    tmp_home: Path, monkeypatch: pytest.MonkeyPatch
):
    monkeypatch.setenv("TYPER_ZSH_COMPLETION_DIR", "~/custom_completions")

    installed_path, custom = install_zsh_completion("myapp")
    expected_dir = tmp_home / "custom_completions"

    assert custom
    assert installed_path == expected_dir / "_myapp"
    assert installed_path.is_file()
    assert (expected_dir / ".compstyles").is_file()


@skip_if_windows
def test_completion_install_zsh_custom_dir_compstyles_multiple_apps(
    tmp_home: Path, monkeypatch: pytest.MonkeyPatch
):
    custom_dir = tmp_home / "custom_completions"
    monkeypatch.setenv("TYPER_ZSH_COMPLETION_DIR", str(custom_dir))

    install_zsh_completion("app1")
    install_zsh_completion("app2")
    install_zsh_completion("app1")  # repeated install should not duplicate entry

    compstyles_path = custom_dir / ".compstyles"
    assert compstyles_path.read_text() == (
        "# this file is managed by typer, do not edit\n"
        "zstyle ':completion:*:*:app1:*' menu select\n"
        "zstyle ':completion:*:*:app2:*' menu select\n"
    )
    # .zshrc should never be created
    assert not (tmp_home / ".zshrc").exists()


@skip_if_windows
def test_completion_install_zsh_respects_zdotdir(
    tmp_home: Path, monkeypatch: pytest.MonkeyPatch
):
    zdotdir = tmp_home / ".config/zsh"
    monkeypatch.setenv("ZDOTDIR", str(zdotdir))

    installed_path, custom = install_zsh_completion("myapp")
    assert not custom
    assert installed_path == tmp_home / ".zfunc/_myapp"

    # .zshrc must be created in ZDOTDIR, not HOME
    assert (zdotdir / ".zshrc").is_file()
    assert not (tmp_home / ".zshrc").exists()
    assert "fpath+=~/.zfunc" in (zdotdir / ".zshrc").read_text()


@skip_if_windows
def test_completion_install_zsh_custom_message(
    tmp_home: Path, monkeypatch: pytest.MonkeyPatch
):
    custom_dir = tmp_home / "custom_completions"
    monkeypatch.setenv("TYPER_ZSH_COMPLETION_DIR", str(custom_dir))

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "coverage",
            "run",
            mod.__file__,
            "--install-completion",
            "zsh",
        ],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "HOME": str(tmp_home),
            "_TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION": "True",
        },
    )
    assert result.returncode == 0
    assert (
        "Custom completion directory used. Make sure it is loaded in your shell configuration."
        in result.stdout
    )
    assert (
        "Completion will take effect once you restart the terminal" not in result.stdout
    )
