# django-webhook-dispatcher

Outgoing webhook delivery service: accepts events, fans them out to subscribed endpoints and delivers them with retries via Celery.

> Work in progress: only the project foundation is in place.

## Stack

- Python 3.13, Django, Django REST Framework
- Celery with Redis as the broker
- PostgreSQL
- httpx for outgoing requests
- uv, ruff, pytest

## Getting started

```bash
cp .env.example .env
docker compose up -d
uv sync
uv run python src/manage.py migrate
uv run python src/manage.py runserver
```

Celery worker:

```bash
cd src && uv run celery -A config worker -l info
```

## Development

```bash
uv run pytest
uv run ruff check .
uv run ruff format .
```

## Layout

```
src/
  config/     settings, urls, celery app
  webhooks/   webhook domain app
tests/
```
