#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

APP_ENV="${APP_ENV:-development}"
APP_DEBUG="${APP_DEBUG:-true}"
APP_HOST="${APP_HOST:-0.0.0.0}"
APP_PORT="${APP_PORT:-8000}"
RESTART_WAIT_SECONDS="${RESTART_WAIT_SECONDS:-3}"

if [ ! -d ".venv" ]; then
  echo "[Ethireal AI] Creating virtual environment..."
  python3 -m venv .venv
fi

# shellcheck source=/dev/null
source .venv/bin/activate
python -m pip install --upgrade pip >/dev/null 2>&1 || true
python -m pip install -r requirements.txt >/dev/null 2>&1 || true

export APP_ENV APP_DEBUG APP_HOST APP_PORT

if [ "${APP_DEBUG,,}" = "true" ]; then
  RELOAD_FLAG="--reload"
else
  RELOAD_FLAG=""
fi

launch_server() {
  echo "[Ethireal AI] Starting service on ${APP_HOST}:${APP_PORT}"
  exec python -m uvicorn app.main:app --host "$APP_HOST" --port "$APP_PORT" $RELOAD_FLAG
}

while true; do
  launch_server || true
  echo "[Ethireal AI] Service exited unexpectedly. Restarting in ${RESTART_WAIT_SECONDS}s..."
  sleep "$RESTART_WAIT_SECONDS"
done
