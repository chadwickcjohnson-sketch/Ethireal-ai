run:
	python scripts/start.sh

install:
	python -m pip install -r requirements.txt

check:
	python -m compileall app scripts

help:
	@echo "Available commands:"
	@echo "  make install"
	@echo "  make run"
	@echo "  make check"

.PHONY: run install check help
