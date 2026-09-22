# Etapa 1: Builder-----------------

FROM python:3.14-slim AS builder

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN python -m venv ${VIRTUAL_ENV}

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock README.md ./

RUN poetry install \
    --only main \
    --no-root \
    --no-interaction \
    --no-ansi

COPY src ./src

RUN poetry build -f wheel

RUN pip install \
    --no-deps \
    dist/*.whl


# Etapa 2: Runtime----------------------

FROM python:3.14-slim AS runtime

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv

EXPOSE 8000

CMD ["uvicorn", "first_proyectproety.empaquetado_distribucion_cicd.app:app", "--host", "0.0.0.0", "--port", "8000"]