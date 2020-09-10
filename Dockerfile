FROM python:3.8.5-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
