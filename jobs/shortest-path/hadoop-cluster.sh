#!/bin/bash
docker cp mapper.py namenode:mapper.py
docker cp reducer.py namenode:reducer.py
docker exec -it namenode chmod +x mapper.py reducer.py
# patch misconfigurations
docker exec -it namenode sed -i -e 's/-3.3.1//g' /etc/hadoop/mapred-site.xml
# for debugging purposes
docker exec -it namenode hadoop fs -rm -r /input /output
docker exec -it namenode hadoop fs -mkdir /input
docker exec -it namenode sh -c 'hadoop fs -put /hadoop-data/input/*.txt /input'

docker exec -it namenode sh -c 'hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer.py \
-input /input/graph-cze.txt -output /output'