#!/bin/bash

# Apply database migrations
uv run python manage.py migrate

# collect static files
uv run python manage.py collectstatic --noinput


if [ "${DEBUG,,}" = "true" ]; then
    echo "Running Django in debug mode..."
    uv run python -m uvicorn foobar.asgi:application --reload --host 0.0.0.0 --port 8888
else
    uv run gunicorn foobar.asgi:application -k uvicorn_worker.UvicornWorker --bind 0.0.0.0:8888 --worker-class gthread --workers 4 --threads 1
fi