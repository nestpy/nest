FROM python:3.10

WORKDIR /app

RUN pip install poetry==1.7.1

COPY . . 

RUN poetry install 



