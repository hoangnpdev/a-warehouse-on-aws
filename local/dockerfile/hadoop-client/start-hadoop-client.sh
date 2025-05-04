echo "init script starting..."
export JAVA_HOME=/usr/local/java/jdk1.8.0_291
export HADOOP_HOME=/usr/local/hadoop/hadoop-3.4.1
export HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop

export AIRFLOW_HOME=/usr/local/airflow
export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow_user:123456@postgres:5432/airflow_db
export AIRFLOW__CORE__EXECUTOR=LocalExecutor
export AIRFLOW__CORE__PARALLELISM=2
export AIRFLOW__SCHEDULER__STANDALONE_DAG_PROCESSOR=True

airflow webserver --port 8080 --daemon
airflow scheduler --daemon
airflow dag-processor --daemon
airflow triggerer --daemon

service ssh start

sleep infinity