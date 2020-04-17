FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8

ENV PYTHONUNBUFFERED=1
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./app /app
