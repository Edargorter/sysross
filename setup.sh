#!/bin/bash

### INSTALL SCRIPTS ###
bash install.sh

### SETUP SYMLINKS ###
bash symlinks.sh

### Set Git editor to vim <3 ###
git config --global core.editor "vim"
