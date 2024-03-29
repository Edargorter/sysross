#!/bin/bash
#Convenient symlinks to configuration files and programs.

#Configuration files 
sudo ln -fs ~/sysross/hidden_files/.tmux.conf ~/.tmux.conf
sudo ln -fs ~/sysross/hidden_files/.vimrc ~/.vimrc
sudo ln -fs ~/sysross/hidden_files/.bashrc ~/.bashrc

#Programs 
sudo ln -fs ~/sysross/Progs/little_endian.py /usr/bin/len
sudo ln -fs ~/sysross/Progs/depri.py /usr/bin/depri
sudo ln -fs ~/sysross/Progs/ckp.sh /usr/bin/ckp
sudo ln -fs ~/sysross/Progs/rmcom.py /usr/bin/rmcom
sudo ln -fs ~/sysross/Progs/rstr.sh /usr/bin/rstr
