#!/bin/bash
source=./data/example-page-list.txt
dest=./data/rank.txt

if [ "$#" -ge 0 ]; then
source=$1
fi

if [ "$#" -ge 1 ]; then
dest=$2
fi

cat $source | python ./mapper.py | python ../shortest-path/partition.py | python ./reducer.py > $dest
