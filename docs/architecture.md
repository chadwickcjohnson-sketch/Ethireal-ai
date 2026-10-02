#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

if [ ! -d .venv ]; then
  python -m venv .venv
fi

source .venv/bin/activate || true
pip install -r requirements.txt >/dev/null 2>&1 || true

python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
