FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir crud
WORKDIR /crud

RUN mkdir /var/log/crud
RUN chmod 777 /var/log/crud

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .