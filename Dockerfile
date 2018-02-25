
FROM ubuntu:16.04

ENV MYSQL_PWD Andrey27
RUN  apt-get upgrade  && apt-get update \
    && apt-get install -y \
        python3

# MySQL
ENV MYSQL_PWD Andrey27
RUN echo "mysql-server mysql-server/root_password password $MYSQL_PWD" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password $MYSQL_PWD" | debconf-set-selections
RUN apt-get -y install mysql-server
