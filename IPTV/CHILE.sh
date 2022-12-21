#!/bin/bash

echo $(dirname $0)

python -m pip install requests

cd $(dirname $0)/scripts/

python CHILE.py "190.107.224.150:3128" > ../CHILE.m3u

echo m3u grabbed
