#!/bin/bash

set -e

if ! command -v ffmpeg >/dev/null 2>&1; then
    sudo apt update
    sudo apt install -y ffmpeg
fi

if ! command -v eog >/dev/null 2>&1; then
    sudo apt update
    sudo apt install -y eog
fi

# PYTHON_PATH=$HOME/micromamba/envs/usermon/bin/python

# sudo MOUSE_EVENT=$(./find-mouse-event.sh) $PYTHON_PATH mouse-detect.py
MOUSE_EVENT=$(./find-mouse-event.sh) python mouse-detect.py
