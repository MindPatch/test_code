# Vulnerable Dockerfile for testing Checkov

# VULN: Using latest tag (unpinned version)
FROM python:latest

# VULN: Running as root (no USER instruction)

# VULN: Using ENV for sensitive data (should use secrets)
ENV DATABASE_PASSWORD=""
ENV API_KEY=""
ENV AWS_ACCESS_KEY_ID=""
ENV AWS_SECRET_ACCESS_KEY=""

# VULN: ADD instead of COPY (can auto-extract archives, fetch URLs)
ADD https://example.com/app.tar.gz /app/
ADD . /app

WORKDIR /app

# VULN: Installing with --no-cache-dir missing, apt-get not cleaning up
RUN apt-get update && apt-get install -y curl wget netcat

# VULN: pip install without --no-cache-dir
RUN pip install -r requirements.txt

# VULN: Exposing unnecessary ports
EXPOSE 22
EXPOSE 3306
EXPOSE 5432

# VULN: No HEALTHCHECK defined

# VULN: Using shell form instead of exec form
CMD python app.py
