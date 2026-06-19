#!/bin/bash

# Find the USB Mouse 

tmp=$(cat /proc/bus/input/devices | grep -i "Mouse" -n | cut -d ':' -f 1 | tail -n 1)
MOUSE=$(head -n $((tmp + 5)) /proc/bus/input/devices | tail -n 10  | grep event | sed -n 's/.*\( event[^ ]* \).*/\1/p' | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
echo "$MOUSE"
