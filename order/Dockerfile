FROM python:3.10

ENV TZ="Asia/Kolkata"

RUN mkdir /code
WORKDIR /code

COPY requirement.txt .
RUN pip install -r requirement.txt
COPY . .