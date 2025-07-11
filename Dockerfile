# Use the official Python image as a parent image
FROM python:3.13

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy the uv files to the container
COPY uv.lock pyproject.toml ./

# Install dependencies
RUN uv sync --frozen

# Copy the rest of the files to the container
COPY . .

EXPOSE 80

CMD ["bash", "-c", "cd backend && chmod +x ./start.sh &&  ./start.sh"]