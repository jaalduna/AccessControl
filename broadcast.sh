#!/bin/bash/sh
#broadcast

broadcast=$(ip addr | grep 'brd' | grep 'inet' | awk '{print $4}');

sudo ping -b $broadcast -i 5;
