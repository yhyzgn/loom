#!/usr/bin/env python3
"""Cross-platform runtime smoke tests for a built loom executable."""
import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd, *, cwd=None, env=None, expect=0):
    cmd = [str(c) for c in cmd]
    print("+", " ".join(cmd), f"(cwd={cwd or os.getcwd()})")
    p = subprocess.run(cmd, cwd=str(cwd) if cwd else None, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p.stdout, end="" if p.stdout.endswith("\n") or not p.stdout else "\n")
    if p.returncode != expect:
        raise AssertionError(f"expected rc {expect}, got {p.returncode}: {' '.join(cmd)}")
    return p


def executable_path(explicit=None):
    if explicit:
        return Path(explicit).resolve()
    system = platform.system().lower()
    suffix = ".exe" if system.startswith("win") else ""
    matches = sorted((ROOT / "dist").glob(f"loom-*{suffix}"))
    matches = [p for p in matches if not p.name.endswith(".sha256")]
    if not matches:
        raise FileNotFoundError(f"no built executable found under {ROOT / 'dist'}")
    return matches[0].resolve()


def assert_contains(text, needle):
    if needle not in text:
        raise AssertionError(f"expected output to contain {needle!r}, got:\n{text}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exe", default=None, help="Path to built loom executable")
    parser.add_argument("--hub", default=str(ROOT), help="Path to loom checkout")
    args = parser.parse_args()

    exe = executable_path(args.exe)
    hub = Path(args.hub).resolve()
    if not (hub / "config" / "manifest.json").exists():
        raise FileNotFoundError(f"invalid hub: {hub}")

    # Direct hub discovery from checkout cwd.
    run([exe, "doctor"], cwd=hub)

    # Global --hub and subcommand --hub must both work from outside the checkout.
    with tempfile.TemporaryDirectory() as td:
        outside = Path(td)
        run([exe, "--hub", hub, "doctor"], cwd=outside)
        run([exe, "doctor", "--hub", hub], cwd=outside)

        # LOOM_HUB must work.
        env = os.environ.copy()
        env["LOOM_HUB"] = str(hub)
        run([exe, "doctor"], cwd=outside, env=env)

        # Sidecar next to executable must work.
        sidecar_dir = outside / "sidecar"
        sidecar_dir.mkdir()
        sidecar_exe = sidecar_dir / exe.name
        shutil.copy2(exe, sidecar_exe)
        if not platform.system().lower().startswith("win"):
            sidecar_exe.chmod(0o755)
        (sidecar_dir / "loom-hub.json").write_text(json.dumps({"hub": str(hub)}, indent=2) + "\n")
        run([sidecar_exe, "doctor"], cwd=outside)

        # No hub should fail clearly without a traceback/PyInstaller crash.
        nohub_dir = outside / "nohub"
        nohub_dir.mkdir()
        nohub_exe = nohub_dir / exe.name
        shutil.copy2(exe, nohub_exe)
        if not platform.system().lower().startswith("win"):
            nohub_exe.chmod(0o755)
        p = run([nohub_exe, "doctor"], cwd=nohub_dir, expect=1)
        assert_contains(p.stdout, "Cannot find loom hub checkout")
        if "Traceback" in p.stdout or "PYI-" in p.stdout:
            raise AssertionError(f"no-hub failure should not show traceback/PyInstaller crash:\n{p.stdout}")

        # install-cli into an isolated target should copy an executable and sidecar.
        # Do not edit shell startup files while testing.
        target = outside / "install-bin"
        install_env = os.environ.copy()
        install_env["LOOM_SKIP_PATH_EXPORT"] = "1"
        run([exe, "install-cli", "--hub", hub, "--target", target, "--mode", "copy"], cwd=outside, env=install_env)
        installed = target / ("loom.exe" if platform.system().lower().startswith("win") else "loom")
        if not installed.exists():
            raise AssertionError(f"installed executable missing: {installed}")
        if not (target / "loom-hub.json").exists():
            raise AssertionError(f"installed sidecar missing: {target / 'loom-hub.json'}")
        run([installed, "doctor"], cwd=outside)

    print("runtime smoke ok")


if __name__ == "__main__":
    main()
