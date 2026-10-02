run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

install:
	python -m pip install -r requirements.txt

check:
	python -m compileall app

help:
	@echo "Available commands:"
	@echo "  make install"
	@echo "  make run"
	@echo "  make check"

.PHONY: run install check help
