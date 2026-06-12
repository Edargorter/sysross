#!/bin/bash

sudo MOUSE_EVENT=$(./find-mouse.event.sh) /home/zdb/micromamba/envs/usermon/bin/python mouse-detect.py
