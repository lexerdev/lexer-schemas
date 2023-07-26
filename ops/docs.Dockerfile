FROM python:3.8

WORKDIR /home/python

ADD . .

RUN pip install --upgrade pip && \
    pip install -r doc-requirements.txt
