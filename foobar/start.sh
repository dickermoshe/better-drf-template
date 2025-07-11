#!/bin/bash

# Apply database migrations
uv run python manage.py migrate

# collect static files
uv run python manage.py collectstatic --noinput


if [ "${DEBUG,,}" = "true" ]; then
    echo "Running Django in debug mode..."
    uv run python manage.py runserver 0.0.0.0:8888
else
    uv run gunicorn backend.asgi:application -k uvicorn_worker.UvicornWorker --bind 0.0.0.0:8888 --workers 4 --threads 1
fi