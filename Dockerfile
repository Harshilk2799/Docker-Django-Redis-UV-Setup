# Use Official python 3.12 image as base
FROM python:3.12-slim

# Uv installation inside container
COPY --from=ghcr.io/astral-sh/uv:0.9.9 /uv /uvx /bin/

# Avoid .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set Working directory inside container
WORKDIR /dockerdjredisuvsetup

# Copy pyproject.toml and uv.lock first (for caching deps)
COPY pyproject.toml /dockerdjredisuvsetup/
COPY uv.lock /dockerdjredisuvsetup/

# Sync dependencies with uv
RUN uv sync --frozen

# Copy project files
COPY . /dockerdjredisuvsetup/