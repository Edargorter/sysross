#!/bin/sh

# See https://hub.docker.com/r/blang/latex

# Install full texlive package
sudo apt install texlive-full latexmk

IMAGE=blang/latex:ubuntu
exec docker run --rm -i --user="$(id -u):$(id -g)" --net=none -v "$PWD":/data "$IMAGE" "$@"
