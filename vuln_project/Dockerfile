# Vulnerable Dockerfile for testing Checkov

# VULN: Using latest tag (unpinned version)
FROM python:latest

# VULN: Running as root (no USER instruction)

# VULN: Hardcoded secrets in environment variables
ENV DATABASE_PASSWORD=admin123
ENV API_KEY=sk-secret-key-12345
ENV AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
ENV AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

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
