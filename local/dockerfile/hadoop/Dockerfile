FROM ubuntu:22.04

RUN apt update
RUN apt install -y python3


RUN mkdir -p /usr/local/java
#RUN wget -P /usr/local/java https://javadl.oracle.com/webapps/download/AutoDL?BundleId=244563_d7fc238d0cbf4b0dac67be84580cfb4b
COPY jdk8.tar.gz /usr/local/java
RUN tar -xvf /usr/local/java/jdk8.tar.gz  -C /usr/local/java


RUN mkdir -p /usr/local/hadoop
#RUN wget -P /usr/local/hadoop/ https://dlcdn.apache.org/hadoop/common/hadoop-3.4.1/hadoop-3.4.1.tar.gz
COPY hadoop-3.4.1.tar.gz /usr/local/hadoop
RUN tar -xvf /usr/local/hadoop/hadoop-3.4.1.tar.gz  -C /usr/local/hadoop


RUN mkdir -p /usr/local/spark
#RUN wget -P /usr/local/spark/ https://dlcdn.apache.org/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz
COPY spark-3.5.5-bin-hadoop3.tar.gz /usr/local/spark
RUN tar -xvf /usr/local/spark/spark-3.5.5-bin-hadoop3.tar.gz -C /usr/local/spark

COPY core-site.xml /usr/local/hadoop/hadoop-3.4.1/etc/hadoop/
COPY hdfs-site.xml /usr/local/hadoop/hadoop-3.4.1/etc/hadoop/
COPY start-hadoop.sh /usr/local/

CMD ["/bin/bash", "/usr/local/start-hadoop.sh"]