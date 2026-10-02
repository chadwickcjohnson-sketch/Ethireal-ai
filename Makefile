services:
  ethireal-ai:
    build: .
    container_name: ethireal-ai
    ports:
      - "8000:8000"
    environment:
      APP_ENV: development
      APP_DEBUG: "true"
      APP_HOST: 0.0.0.0
      APP_PORT: 8000
    volumes:
      - .:/app
    command: /bin/bash -lc "python scripts/start.sh"
