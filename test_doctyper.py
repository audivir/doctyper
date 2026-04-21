import subprocess
import sys
from pathlib import Path

from tqdm import tqdm

from pdm_build import adjust_file

if __name__ == "__main__":
    test_directories = ("docs_src", "tests")
    files = [f for d in test_directories for f in Path(d).rglob("*.py*")]
    try:
        for f in tqdm(files, desc="Fixing names"):
            adjust_file(f, "typer", "doctyper")
        proc = subprocess.Popen(["bash", "scripts/test.sh", *sys.argv[1:]])
        returncode = proc.wait()
    finally:
        for f in tqdm(files, desc="Resetting names"):
            adjust_file(f, "doctyper", "typer")
    raise SystemExit(returncode)
