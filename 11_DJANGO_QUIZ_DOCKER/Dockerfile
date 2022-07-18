FROM python:3.10.5-slim

RUN apt update \
    && apt install python3-dev libpq-dev gcc -y \
    && apt install mc vim -y

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /opt/src
WORKDIR /opt/src

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm -f requirements.txt

COPY src .
COPY data.json .

EXPOSE 8090

# CMD python manage.py runserver 0.0.0.0:8090
