#!/bin/bash

# Find the USB Keyboard 

tmp=$(cat /proc/bus/input/devices | grep -i "Keyboard" -n | cut -d ':' -f 1 | tail -n 1)
KEYBOARD=$(head -n $((tmp + 5)) /proc/bus/input/devices | tail -n 10  | grep event | sed -n 's/.*\( event[^ ]* \).*/\1/p' | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
echo "$KEYBOARD"
