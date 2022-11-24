#!/usr/bin/env python3

from sys import argv
from pytube import YouTube
import re
from pytube import Playlist 

path = ""

def progress_func(self, chunk, bytes_remaining):
    size = len(chunk)
    p = 0
    while p <= 100:
        progress = p
        #print(chunk, bytes_remaining)
        #print(str(p)+'%', end="\r")
        p = (float(bytes_remaining) / float(size)) * float(100)

def get_vid(url):
    yt = YouTube(url)
    try:
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path)
    except Exception as e:
        print(e)
        exit(2)

def get_pl(url):
    playlist = Playlist(url)
    try: 
        for v in playlist.videos:
            print(v)
            print(f"getting {v.title}")
            v.streams.\
                filter(type='video', progressive=True, file_extension='mp4', res="720p").\
                first().\
                download(path)
    except Exception as e:
        print(e)
        exit(1)

try:
	url = argv[1]
except Exception as e:
	print(e)
	exit(1)

get_pl(url)
