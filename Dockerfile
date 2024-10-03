FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml poetry.lock ./
COPY orienteer ./orienteer/
RUN python -m pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi