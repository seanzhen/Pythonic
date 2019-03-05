import findspark
findspark.init("/home/seanzhen52/spark-2.2.3-bin-hadoop2.7")
from pyspark import SparkContext
sc = SparkContext('local','test')
logFile = "file:///home/seanzhen52/spark-2.2.3-bin-hadoop2.7/README.md"
logdata = sc.textFile(logFile,2).cache()
numas = logdata.filter(lambda line: 'a' in line).count()
numbs = logdata.filter(lambda line: 'b' in line).count()
print('Line with a: %s,Lines with b:%s' % (numas,numbs))
