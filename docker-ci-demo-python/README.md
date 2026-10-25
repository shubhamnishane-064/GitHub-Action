# docker-ci-demo-python

[![Docker CI](https://github.com/YOUR_USERNAME/docker-ci-demo-python/actions/workflows/docker-ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/docker-ci-demo-python/actions/workflows/docker-ci.yml)

A demo Python (Flask) app with an automated Docker image CI/CD pipeline.

## Pipeline

Every push to `main`:
1. Runs automated tests (`pytest`)
2. Builds a multi-stage Docker image (slim base, non-root user)
3. Pushes to Docker Hub with tags: `latest`, `sha-<commit>`, `main`

## Docker Image

```bash
docker pull YOUR_USERNAME/docker-ci-demo-python:latest
docker run -p 3000:3000 YOUR_USERNAME/docker-ci-demo-python:latest
curl http://localhost:3000/health
# {"status":"ok"}trigger CI
