#!/bin/bash
cd '/home/ubuntu/hosting/crypto-analysis/'
git pull
python3 run.py
./commit.sh
