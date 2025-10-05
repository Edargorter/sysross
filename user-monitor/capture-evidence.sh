#!/bin/bash
ctime=$(date +%Y_%m_%d_%H_%M_%S)
ffmpeg -f v4l2 -i /dev/video0 -vframes 1 "culprit_$ctime.jpg"
eog "culprit_$ctime.jpg" &
