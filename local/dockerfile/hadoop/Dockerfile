FROM alpine:3.21.3

RUN apk add --no-cache bash
RUN apk add --no-cache openssh
RUN apk add --no-cache wget
RUN apk add --no-cache tar

RUN wget -P /usr/loca/java https://download.java.net/openjdk/jdk8u44/ri/openjdk-8u44-linux-x64.tar.gz
RUN tar -xvf /usr/local/java/openjdk-8u44-linux-x64.tar.gz  -C /usr/local/java

RUN wget -P /usr/local/hadoop/ https://dlcdn.apache.org/hadoop/common/hadoop-3.4.1/hadoop-3.4.1.tar.gz
RUN tar -xvf /usr/local/hadoop/hadoop-3.4.1.tar.gz  -C /usr/local/hadoop

COPY core-site.xml /usr/local/hadoop/hadoop-3.4.1/etc/hadoop/
COPY hdfs-site.xml /usr/local/hadoop/hadoop-3.4.1/etc/hadoop/
COPY start-hadoop.sh /usr/local/

CMD ["/bin/bash", "start_hadoop.sh"]2