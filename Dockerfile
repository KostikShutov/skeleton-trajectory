FROM python:3.11-slim

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install gcc g++ cmake graphviz git libopenblas-dev -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/
RUN pip3 install --upgrade pip \
    && pip3 install -r /tmp/requirements.txt --no-cache-dir --default-timeout=100
