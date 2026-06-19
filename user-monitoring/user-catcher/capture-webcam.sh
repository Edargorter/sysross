#!/bin/bash

rm webcam-recording.mp4
ffmpeg -f v4l2 -i /dev/video0 -t 20 -vcodec libx264 webcam-recording.mp4
