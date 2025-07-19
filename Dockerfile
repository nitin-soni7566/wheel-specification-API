FROM python:3.12-slim

# Copy the uv binary from the official uv image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies (lock must exist)
RUN uv venv .venv && uv sync --frozen --no-cache

# Expose the FastAPI port
EXPOSE 8000

# Run the FastAPI app !

CMD ["uv","run","uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]