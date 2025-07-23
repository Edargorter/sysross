#!/bin/bash

g++ -o keylogger main.cc $(pkg-config --cflags --libs libevdev)
