FROM nph/spark-hadoop

RUN mkdir -p /usr/local/airflow
RUN pip install psycopg2-binary
RUN pip install 'apache-airflow==2.10.5' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.5/constraints-3.8.txt"

RUN export JAVA_HOME=/usr/local/java/jdk1.8.0_291
RUN export AIRFLOW_HOME=/usr/local/airflow

RUN airflow db migrate
RUN airflow users create \
    --username admin \
    --password admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@admin.admin

RUN apt update && apt install -y openssh-server
RUN apt install python3.10-vevn

COPY start-hadoop-client.sh /usr/local/
CMD ["/bin/bash", "/usr/local/start-hadoop-client.sh"]