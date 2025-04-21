export JAVA_HOME=/usr/local/java/java-se-8u44-ri/
export HADOOP_HOME=/usr/local/hadoop/hadoop-3.4.1/etc/hadoop/
export HADOOP_CONF_DIR=${HADOOP_HOME}/usr/local/hadoop/hadoop-3.4.1/etc/hadoop/

$HADOOP_HOME/bin/hdfs --daemon start "$HDFS_NODE_TYPE"

$HADOOP_HOME/bin/yarn --daemon start "$YARN_NODE_TYPE"

wait -n