# Dockerfile for the sovereign document generator
# Builds a small image that can run the Python CLI (features/copilot/plans/document_generator.py)
FROM python:3.11-slim

WORKDIR /app

# Install minimal system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

# Copy only what's needed
COPY features/copilot/plans /app/features/copilot/plans
COPY website /app/website

# install lightweight deps if needed (none required for current scripts)
# RUN pip install --no-cache-dir -r requirements.txt

ENV LEGAL_VAULT_PATH=/var/lib/galaxigates_omni/legal_vault
VOLUME ["/var/lib/galaxigates_omni/legal_vault"]

ENTRYPOINT ["python3", "features/copilot/plans/document_generator.py"]
