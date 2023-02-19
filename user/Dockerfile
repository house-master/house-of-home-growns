FROM python:3.10

ENV TZ="Asia/Kolkata"

RUN mkdir /code
WORKDIR /code

COPY requirement.txt .
RUN pip install -r requirement.txt
COPY . .

# CMD ["uvicorn", "user.main:app", "--host", "0.0.0.0", "--port", "5001"]