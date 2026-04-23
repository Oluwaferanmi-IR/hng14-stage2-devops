# Stage 1 - Build
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt


# Stage 2 - Production
FROM python:3.11-slim AS production

WORKDIR /app

RUN groupadd -r appuser && \
    useradd -r -g appuser appuser

COPY --from=builder /root/.local /home/appuser/.local

COPY worker.py .

RUN chown -R appuser:appuser /app

USER appuser

ENV PATH=/home/appuser/.local/bin:$PATH

HEALTHCHECK --interval=30s --timeout=10s \
    --start-period=15s --retries=3 \
    CMD pgrep -f "python worker.py" || exit 1

CMD ["python", "worker.py"]