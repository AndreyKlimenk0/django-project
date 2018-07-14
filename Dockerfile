FROM ubuntu:16.04

RUN  apt-get upgrade  && apt-get update \
     && apt-get install -y \
        python3 \
        python3-pip

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip3 install -r requirements.txt
ADD . /app
