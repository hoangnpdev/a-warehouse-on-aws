export JAVA_HOME=/usr/local/java/jdk1.8.0_291
export HADOOP_HOME=/usr/local/hadoop/hadoop-3.4.1
export HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop

if [ "$HDFS_NODE_TYPE" = "namenode" ]
then
  $HADOOP_HOME/bin/hdfs namenode -format
fi

$HADOOP_HOME/bin/hdfs --daemon start "$HDFS_NODE_TYPE"

$HADOOP_HOME/bin/yarn --daemon start "$YARN_NODE_TYPE"

sleep infinity