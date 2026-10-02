[Unit]
Description=Ethireal AI self-starting service
After=network.target

[Service]
Type=simple
WorkingDirectory=/opt/ethireal-ai
Environment=APP_ENV=development
Environment=APP_DEBUG=true
Environment=APP_HOST=0.0.0.0
Environment=APP_PORT=8000
ExecStart=/opt/ethireal-ai/scripts/start.sh
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
