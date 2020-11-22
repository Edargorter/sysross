#!/bin/bash

filename=""

if [[ $# > 0 ]]; then
	filename="$1"
else
	filename="urls.txt"
fi

mkdir Pkgs
cd Pkgs

while read url; do
	echo "Downloading: $url"
	curl -L -O "$url"
done < "../$filename"

echo "Done."
