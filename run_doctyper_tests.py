import os
import shutil
import subprocess
import sys
from pathlib import Path

from tqdm import tqdm

from pdm_build import adjust_file


def _bash_executable() -> str:
    """Find a real bash, avoiding Windows' WSL bash.exe stub in System32."""
    if sys.platform == "win32":
        for program_files in ("ProgramFiles", "ProgramFiles(x86)"):
            candidate = (
                Path(os.environ.get(program_files, "")) / "Git" / "bin" / "bash.exe"
            )
            if candidate.is_file():
                return str(candidate)
    return shutil.which("bash") or "bash"


if __name__ == "__main__":
    test_directories = ("docs_src", "scripts", "tests")
    files = [f for d in test_directories for f in Path(d).rglob("*.py*")]
    try:
        for f in tqdm(files, desc="Fixing names"):
            adjust_file(f, "typer", "doctyper")
        proc = subprocess.Popen([_bash_executable(), "scripts/test.sh", *sys.argv[1:]])
        returncode = proc.wait()
    finally:
        for f in tqdm(files, desc="Resetting names"):
            adjust_file(f, "doctyper", "typer")
    raise SystemExit(returncode)
