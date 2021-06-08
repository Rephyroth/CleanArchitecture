FROM python:3.8

COPY . usr/src/Container_C

WORKDIR usr/src/Container_C

RUN pip install peewee

RUN pwd

RUN ["python3","./scraper.py"]

