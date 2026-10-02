run:
	./scripts/start.sh

install:
	python3 -m pip install -r requirements.txt

check:
	python3 -m compileall app scripts

help:
	@echo "Available commands:"
	@echo "  make install"
	@echo "  make run"
	@echo "  make check"

.PHONY: run install check help
