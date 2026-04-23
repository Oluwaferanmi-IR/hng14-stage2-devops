# Stage 1 - Build
FROM node:20-slim AS builder

WORKDIR /app

COPY package*.json ./

RUN npm ci --omit=dev


# Stage 2 - Production
FROM node:20-slim AS production

WORKDIR /app

RUN groupadd -r appuser && \
    useradd -r -g appuser appuser

COPY --from=builder /app/node_modules ./node_modules

COPY app.js .
COPY views/ ./views/

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=10s \
    --start-period=10s --retries=3 \
    CMD node -e \
    "require('http').get('http://localhost:3000/health', \
    (r) => r.statusCode === 200 ? \
    process.exit(0) : process.exit(1))" \
    || exit 1

CMD ["node", "app.js"]

