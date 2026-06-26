#!/usr/bin/env python3
"""Build loom as a single-file platform executable."""
import argparse
import hashlib
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
WORK = ROOT / "build" / "pyinstaller"


def run(cmd):
    print("+", " ".join(map(str, cmd)))
    subprocess.run([str(c) for c in cmd], cwd=ROOT, check=True)


def platform_tag():
    system = platform.system().lower()
    machine = platform.machine().lower().replace("amd64", "x86_64").replace("x64", "x86_64")
    if system == "darwin":
        system = "macos"
    return f"{system}-{machine}"


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build(name):
    DIST.mkdir(parents=True, exist_ok=True)
    WORK.mkdir(parents=True, exist_ok=True)
    run([
        sys.executable,
        "-m",
        "PyInstaller",
        "--clean",
        "--noconfirm",
        "--onefile",
        "--name",
        name,
        "--distpath",
        DIST,
        "--workpath",
        WORK,
        "bin/loom",
    ])
    raw = DIST / (name + (".exe" if platform.system().lower().startswith("win") else ""))
    if not raw.exists():
        raise FileNotFoundError(raw)
    tagged = DIST / f"loom-{platform_tag()}{raw.suffix}"
    if tagged.exists():
        tagged.unlink()
    shutil.copy2(raw, tagged)
    if not platform.system().lower().startswith("win"):
        tagged.chmod(0o755)
    checksum = tagged.with_suffix(tagged.suffix + ".sha256") if tagged.suffix else Path(str(tagged) + ".sha256")
    checksum.write_text(f"{sha256(tagged)}  {tagged.name}\n")
    return tagged


def smoke(exe):
    run([exe, "doctor"])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="loom", help="base executable name passed to PyInstaller")
    parser.add_argument("--no-smoke", action="store_true", help="skip running the built executable")
    args = parser.parse_args()
    exe = build(args.name)
    if not args.no_smoke:
        smoke(exe)
    print(f"built {exe}")


if __name__ == "__main__":
    main()
