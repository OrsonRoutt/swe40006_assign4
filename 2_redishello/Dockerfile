FROM python:3-slim

WORKDIR /app

ADD . /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Taken from https://hub.docker.com/_/python/ because the tutorial looked outdated.
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV NAME=World

CMD ["flask", "run", "--debug"]
