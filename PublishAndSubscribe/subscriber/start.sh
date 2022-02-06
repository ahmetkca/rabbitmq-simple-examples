#!/bin/bash

if [[ "$1" == "--logs" ]];
then
    mkdir -p logs
    python subscriber.py > logs/logs_from_subscriber.log
else
    python subscriber.py
fi