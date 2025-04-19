# HDFS
HDFS daemons: NameNode, SecondaryNameNode, DataNode

Configuration: core-*.xml, hdfs-*.xml

## HDFS start-up
1. DataNodes make connection (long-lived hadoop rpc) to NameNode using NameNode rpc-address at fs.defaultFS config

## HDFS operating
- During operation, for example uploading a new file, client make request to NameNode for necessary uploading information, then client transfer data directly to corresponding DataNode. On DataNode, it perform valid check with NameNode and receive data.

# YARN