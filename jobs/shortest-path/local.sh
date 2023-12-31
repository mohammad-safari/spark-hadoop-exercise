#!/bin/bash
cd "$(dirname "$0")"

source=./data/example-graph.txt
dest=./data/output.txt

if [ "$#" -ge 1 ]; then
    source=$1
fi

if [ "$#" -ge 2 ]; then
    dest=$2
fi

cat $source | ./mapper.py | ./partition.py | ./reducer.py > $dest