#!/bin/bash
source=./data/example-graph.txt
dest=./data/output.txt

if [ "$#" -ge 0 ]; then
source=$1
fi

if [ "$#" -ge 1 ]; then
dest=$2
fi

cat $source | python ./mapper.py | python ./partition.py | python ./reducer.py > $dest
