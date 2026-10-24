# ── Build stage ───────────────────────────
FROM python:3.12-slim AS builder
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ── Runtime stage ─────────────────────────
FROM python:3.12-slim
WORKDIR /app

RUN useradd --create-home --shell /bin/bash appuser
COPY --from=builder /install /usr/local
COPY --chown=appuser:appuser src ./src

USER appuser
EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request,sys; \
      sys.exit(0 if urllib.request.urlopen('http://localhost:3000/health').status == 200 else 1)"

WORKDIR /app/src
CMD ["python", "app.py"]