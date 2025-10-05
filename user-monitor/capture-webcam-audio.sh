#!/bin/bash
ffmpeg -f v4l2 -i /dev/video0 -f pulse -i default -c:v libx264 -c:a aac output_with_audio.mp4
