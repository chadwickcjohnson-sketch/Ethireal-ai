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
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
