FROM python:3.7

ENV LANF=C.UTF-8

WORKDIR /usr/src/app
COPY Pipfile ./
COPY Pipfile.lock ./
RUN pip install -U pip && \
    pip install pipenv && \
    pipenv install --system --ignore-pipfile --deploy
