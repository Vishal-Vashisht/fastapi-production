# Builder image
FROM python:3.11 AS builder

WORKDIR /app

ARG REQUIREMENT=production.txt

COPY requirements .

RUN pip install --user --no-cache-dir -r ${REQUIREMENT}

# STAGE 2: Runner (The "Slim" Production Image)
FROM python:3.11-slim AS runner

WORKDIR /app

COPY --from=builder /root/.local /root/.local

COPY . .

ENV PATH=/root/.local/bin:$PATH

CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]