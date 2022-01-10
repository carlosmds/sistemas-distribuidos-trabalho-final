FROM python:3.7-alpine

LABEL maintainer 'Carlos Medeiros - TADS UDESC 2021 - carlosmedeirosdesouza@gmail.com'

ADD ./app /app
ADD requirements.txt /app/

WORKDIR /app

RUN sh -c "python3 -m pip install -r /app/requirements.txt"