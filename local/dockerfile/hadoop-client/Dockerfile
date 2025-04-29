FROM nph/spark-hadoop

RUN mkdir -p /usr/local/airflow
RUN pip install psycopg2-binary
RUN pip install 'apache-airflow==2.10.5' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.5/constraints-3.8.txt"

COPY start-hadoop-client.sh /usr/local/

CMD ["/bin/bash", "/usr/local/start-hadoop-client.sh"]