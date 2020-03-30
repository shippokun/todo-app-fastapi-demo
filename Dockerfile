FROM python:3.7 as builder

WORKDIR /usr/src/app

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv lock -r > requirements.txt


FROM python:3.7

ENV LANF=C.UTF-8

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/requirements.txt .

RUN pip install -U pip && \
    pip install -r requirements.txt
