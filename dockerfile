FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir aiproject

WORKDIR /aiproject
COPY requirements.txt /aiproject/

RUN pip install -U pip &&\
    pip install -r requirements.txt 

COPY . /aiproject/