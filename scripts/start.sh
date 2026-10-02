#!/usr/bin/env python3
"""Basic self-healing watchdog for the Ethireal AI service."""

from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run_service() -> None:
    cmd = [sys.executable, "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
    with subprocess.Popen(cmd, cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True) as proc:
        try:
            for line in proc.stdout:
                print(line, end="")
                if "Traceback" in line:
                    raise RuntimeError("Service failed to start cleanly")
        finally:
            if proc.poll() is None:
                proc.terminate()


def main() -> int:
    attempts = 0
    while attempts < 5:
        try:
            run_service()
            return 0
        except Exception as exc:
            attempts += 1
            print(f"Self-heal attempt {attempts}/5 failed: {exc}")
            time.sleep(2)
    print("Service could not self-heal. Manual intervention required.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
