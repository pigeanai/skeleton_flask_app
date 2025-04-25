FROM python:3.13-alpine

RUN apk add --no-cache git libffi-dev gcc python3-dev musl-dev

RUN adduser --disabled-password flaskuser

WORKDIR /home/flaskuser

COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install pip setuptools
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY flaskapp.py config.py docker-entrypoint.sh ./

RUN chmod +x docker-entrypoint.sh
RUN mkdir -p /home/flaskapp/logs

ENV FLASK_APP=flaskapp.py

RUN chown -R flaskuser:flaskuser ./
USER flaskuser

EXPOSE 5000
ENTRYPOINT [ "./docker-entrypoint.sh" ]
