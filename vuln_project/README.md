# Vulnerable Test Project

This project contains intentional security vulnerabilities for testing static analysis tools.

## Purpose

Use this project to test:
- **Semgrep** - Code-level vulnerabilities
- **Qlty** - Code quality and security issues
- **Checkov** - Infrastructure-as-code misconfigurations

## Vulnerabilities Included

### Python (`app.py`)
- SQL Injection
- Command Injection
- Server-Side Template Injection (SSTI)
- Insecure Deserialization (pickle)
- Unsafe YAML loading
- Path Traversal
- Hardcoded secrets
- Weak cryptography (MD5)

### JavaScript (`server.js`)
- SQL Injection
- Command Injection
- XSS (Cross-Site Scripting)
- Eval injection
- Prototype pollution
- Hardcoded credentials
- Weak crypto (DES)
- Insecure random

### Dockerfile
- Running as root
- Unpinned base image
- Hardcoded secrets in ENV
- ADD instead of COPY
- No HEALTHCHECK

### Terraform (`main.tf`)
- Public S3 buckets
- Open security groups (0.0.0.0/0)
- Unencrypted RDS/EBS
- Hardcoded passwords
- Wildcard IAM permissions
- Publicly accessible databases

### Kubernetes (`kubernetes/deployment.yaml`)
- Privileged containers
- Running as root
- Host network/PID/IPC
- Docker socket mounted
- Secrets in environment variables
- No resource limits
- Permissive network policies

## Running the Scanners

```bash
# Semgrep
semgrep --config auto .

# Checkov
checkov -d .

# Qlty
qlty check .
```

## Warning

DO NOT deploy this code to any production environment. This is for testing purposes only.
