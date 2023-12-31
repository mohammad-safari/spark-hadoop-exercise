#!/bin/bash
cd "$(dirname "$0")"

input=movie-links.txt
input_dir=/input
output_dir=/rank

docker cp mapper.py namenode:mapper.py
docker cp reducer.py namenode:reducer.py
docker exec -it namenode chmod +x mapper.py reducer.py
# patch misconfigurations
docker exec -it namenode sed -i -e 's/-3.3.1//g' /etc/hadoop/mapred-site.xml
# preparing input/output directories
docker exec -it namenode hadoop fs -rm -r $input_dir $output_dir
docker exec -it namenode hadoop fs -mkdir $input_dir
docker exec -it namenode sh -c 'hadoop fs -put /hadoop-data/input/*.txt '$input_dir

docker exec -it namenode sh -c 'hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer.py \
-input '$input_dir'/'$input' -output '$output_dir