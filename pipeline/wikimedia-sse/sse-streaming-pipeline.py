from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext

sc = SparkContext()
ssc = StreamingContext(sc, 1)

session: SparkSession = SparkSession.builder.getOrCreate()

session.readStream.format()
