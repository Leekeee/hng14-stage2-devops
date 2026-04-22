# Stage 1 - Builder
FROM node:18-alpine AS builder
WORKDIR /app
COPY package.json .
RUN npm install --production

# Stage 2 - Final
FROM node:18-alpine
WORKDIR /app

# Create non-root user
RUN addgroup -S appuser && adduser -S appuser -G appuser

# Copy dependencies from builder
COPY --from=builder /app/node_modules ./node_modules

# Copy application code
COPY app.js .
COPY views/ ./views/

# Switch to non-root user
USER appuser

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget -qO- http://localhost:3000 || exit 1

CMD ["node", "app.js"]
