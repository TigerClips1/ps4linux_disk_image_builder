#!/bin/bash

echo "installing python if it not install"

#ubuntu/debian

sudo apt update && sudo apt install python3 python3-pip #installing python3  for debian/ubuntu for my .py script to run

sudo apt-get update && sudo apt-get install unrar rar wget cryptmount wget
sudo apt-get update && sudo apt-get install wget

#arch

sudo pacman -Syy && sudo pacman -S python3 python3-pip #installing python3  for arch base distro for my .py script to run

#outro

echo "Done"

echo "just run in the termnal python3 ps4linux_diskimage_create.py to run the python file"

echo "ps4linux.com"
