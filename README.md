# hng14-stage2-devops

# HNG DevOps Stage 2 — Containerized Microservices

## Overview
A job processing system made up of four services
containerized with Docker and deployed via a full
CI/CD pipeline using GitHub Actions.

## Architecture
```
Frontend (Node.js:3000)
    ↓
API (FastAPI:8000)
    ↓
Redis (internal only)
    ↓
Worker (Python)
```

## Prerequisites
- Docker Desktop or Docker Engine installed
- Docker Compose v2+
- Git

## How to Run on a Clean Machine

### 1. Clone the repository
```bash
git clone https://github.com/Oluwaferanmi-IR/hng14-stage2-devops
cd hng14-stage2-devops
```

### 2. Set up environment variables
```bash
cp .env.example .env
```
Edit `.env` and fill in real values.

### 3. Start the full stack
```bash
docker compose up --build
```

### 4. What successful startup looks like
```
redis     | Ready to accept connections
api       | Uvicorn running on http://0.0.0.0:8000
worker    | Processing...
frontend  | Frontend running on port 3000
```

All four containers show as healthy:
```bash
docker compose ps
```

### 5. Access the application
Open your browser and go to:
```
http://localhost:3000
```

### 6. Stop the stack
```bash
docker compose down
```

## Services

| Service  | Port | Description |
|---|---|---|
| Frontend | 3000 | User interface |
| API | 8000 | REST API (internal) |
| Worker | - | Background processor |
| Redis | - | Job queue (internal only) |

## CI/CD Pipeline

Pipeline runs automatically on every push:

```
lint → test → build → security scan → integration test → deploy
```

- **Lint:** flake8, eslint, hadolint
- **Test:** pytest with Redis mocked, coverage report uploaded
- **Build:** Images tagged with git SHA and latest
- **Security:** Trivy scans all images for CRITICAL vulnerabilities
- **Integration:** Full stack spun up, job submitted and polled
- **Deploy:** Rolling update with health check verification

## Environment Variables

See `.env.example` for all required variables.

## Bugs Fixed

See `FIXES.md` for a full list of all bugs found
and fixed in the starter code.

## Author
Oluwaferanmi-IR
