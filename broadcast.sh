#!/bin/bash/sh
#broadcast
while [ -z "$broadcast"]
do
    broadcast=$(ip addr | grep 'brd' | grep 'inet' | awk '{print $4}');
    echo 'waiting for wireless up'
    sleep 1
done

sudo ping -b $broadcast -i 5;
