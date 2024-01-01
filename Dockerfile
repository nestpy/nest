FROM python:3.10

WORKDIR /app

COPY . . 

RUN pip install poetry==1.7.1
