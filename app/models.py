from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

APP_NAME = "Ethireal AI"
APP_ENV = os.getenv("APP_ENV", "development")
APP_DEBUG = os.getenv("APP_DEBUG", "true").lower() == "true"
APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenv("APP_PORT", "8000"))
WORKFLOW_TIMEOUT_SECONDS = int(os.getenv("WORKFLOW_TIMEOUT_SECONDS", "120"))
