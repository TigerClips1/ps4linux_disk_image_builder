#!/bin/bash
 
#this will make it where you can hit tab and it will autofill it

#intro
echo "wine is require to create an rar file useing winrar gui on linux to comepress the .img file " #Welcome screen

sudo dnf install -y  https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm #add the fedora fuse repo

sudo dnf install -y https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm #add the fuse repo non free

sudo dnf config-manager --add-repo https://dl.winehq.org/wine-builds/fedora/36/winehq.repo #config wine for fedora36 by adding the repo

sudo dnf install winehq-staging #installing wine

sudo dnf install python3 python3-pip cryptmount wget #installing python to you can run my .py script

echo "plese be on fedora 36 for this script to work" #reminder

sudo dnf update && sudo dnf install unrar && sudo yum install rar #installing unrar and rar for who want to use the commandline

#outro
echo "done plsese run ps4linux_diskimage_create.py to create your .img file"

echo "ps4linux.com"