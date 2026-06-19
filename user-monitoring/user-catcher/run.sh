#!/bin/bash

PYTHON_PATH=$HOME/envs/usermon/bin/python

sudo MOUSE_EVENT=$(./find-mouse.event.sh) $PYTHON_PATH mouse-detect.py
