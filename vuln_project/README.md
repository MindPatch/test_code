# Vulnerable Test Project

This project contains intentional security vulnerabilities for testing static analysis tools.

## Purpose

Use this project to test:
- **Semgrep** - Code-level vulnerabilities
- **Qlty** - Code quality and security issues
- **Checkov** - Infrastructure-as-code misconfigurations
- **Trivy** - Container/dependency vulnerabilities

## Vulnerabilities Included

### Python (`app.py`)
- SQL Injection
- Command Injection
- Server-Side Template Injection (SSTI)
- Insecure Deserialization (pickle)
- Unsafe YAML loading
- Path Traversal
- Weak cryptography (MD5)

### JavaScript (`server.js`)
- SQL Injection
- Command Injection
- XSS (Cross-Site Scripting)
- Eval injection
- Prototype pollution
- Weak crypto (DES)
- Insecure random

### Dockerfile
- Running as root
- Unpinned base image (latest tag)
- ADD instead of COPY
- No HEALTHCHECK

### Terraform (`main.tf`)
- Public S3 buckets
- Open security groups (0.0.0.0/0)
- Unencrypted RDS/EBS
- Wildcard IAM permissions
- Publicly accessible databases

### Kubernetes (`kubernetes/deployment.yaml`)
- Privileged containers
- Running as root
- Host network/PID/IPC
- Docker socket mounted
- No resource limits
- Permissive network policies

### Dependencies
- Vulnerable Python packages (`requirements.txt`)
- Vulnerable npm packages (`package.json`)
- Outdated base image (`Dockerfile.trivy`)

## Running the Scanners

```bash
# Semgrep
semgrep --config auto .

# Checkov
checkov -d .

# Qlty
qlty check .

# Trivy
trivy fs .
```

## Warning

DO NOT deploy this code to any production environment. This is for testing purposes only.
