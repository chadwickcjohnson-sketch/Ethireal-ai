# Ethireal AI

Automation in full.

Ethireal AI is an AI-powered business operating system for founders, executives, and teams who want to automate the real work of running a business.

## Auto-start and self-healing

The project now includes auto-start support and a self-healing watchdog so the app restarts automatically if it exits unexpectedly.

### Start manually

```bash
./scripts/start.sh
```

### Install system service (Linux / systemd)

```bash
sudo ./scripts/install_autostart.sh
```

This registers the app as a systemd service and enables automatic start on boot.

### Health check

```bash
curl http://localhost:8000/health
```

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./scripts/start.sh
```

## License

GNU Affero General Public License v3.0
