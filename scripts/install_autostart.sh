#!/usr/bin/env python3
"""Self-healing watchdog for Ethireal AI."""

from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def env_value(name: str, default: str) -> str:
    return os.getenv(name, default)


def run_service() -> None:
    host = env_value("APP_HOST", "0.0.0.0")
    port = env_value("APP_PORT", "8000")
    debug = env_value("APP_DEBUG", "true").lower() == "true"
    cmd = [sys.executable, "-m", "uvicorn", "app.main:app", "--host", host, "--port", port]
    if debug:
        cmd.append("--reload")

    proc = subprocess.Popen(cmd, cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    try:
        for line in proc.stdout:
            print(line, end="")
            if "Traceback" in line:
                raise RuntimeError("Service failed to start cleanly")
    finally:
        if proc.poll() is None:
            proc.terminate()
        proc.wait(timeout=10)


def main() -> int:
    attempts = 0
    while attempts < 10:
        try:
            run_service()
            return 0
        except Exception as exc:
            attempts += 1
            print(f"[Ethireal AI] Self-heal attempt {attempts}/10 failed: {exc}")
            time.sleep(3)

    print("[Ethireal AI] Unable to self-heal. Manual intervention required.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
