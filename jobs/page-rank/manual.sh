#!/bin/bash
cd "$(dirname "$0")"

source=./data/example-page-list.txt
dest=./data/rank.txt

if [ "$#" -ge 1 ]; then
    source=$1
fi

if [ "$#" -ge 2 ]; then
    dest=$2
fi

cat $source | ./mapper.py | sort | ./reducer.py > $dest