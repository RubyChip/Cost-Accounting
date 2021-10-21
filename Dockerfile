FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1 \
    POETRY_VERSION=1.1.7


RUN apt-get update && \
    apt-get install -y netcat

RUN pip install --upgrade pip && \
    pip install "poetry==1.1.7"


RUN mkdir -p /usr/src/app

COPY poetry.lock pyproject.toml /usr/src/app

WORKDIR /usr/src/app

# Project initialization:
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi


COPY entrypoint.sh /usr/src/app

COPY . /usr/src/app

WORKDIR /usr/src/app/project

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]



