FROM ubuntu:20.04

WORKDIR /opt
RUN apt-get update
RUN apt-get install -y wget

RUN wget https://github.com/ClickHouse/ClickHouse/releases/download/v24.8.14.39-lts/clickhouse-common-static_24.8.14.39_amd64.deb
RUN dpkg -i clickhouse-common-static_24.8.14.39_amd64.deb
RUN wget https://github.com/ClickHouse/ClickHouse/releases/download/v24.8.14.39-lts/clickhouse-server_24.8.14.39_amd64.deb
RUN dpkg -i clickhouse-server_24.8.14.39_amd64.deb

COPY config.xml /etc/clickhouse-server/config.d/
COPY users.xml /etc/clickhouse-server/
USER clickhouse
CMD ["clickhouse-server", "--config-file=/etc/clickhouse-server/config.xml"]