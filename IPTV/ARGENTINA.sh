#!/bin/bash

echo $(dirname $0)

python -m pip install requests

cd $(dirname $0)/scripts/

python ARGENTINA.py > ../lista3argentina.m3u

echo m3u grabbed
