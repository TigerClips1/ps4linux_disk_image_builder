#!/bin/sh 
 #this will make it where you can hit tab and it will autofill it
 
#intro

echo "wine is require to create an rar file useing winrar gui on linux to comepress the .img file " #welcome screen

echo "ubuntu 22.04 is require for this script to work"

sudo dpkg --add-architecture i386  #make it where 32 bit is enable for ubuntu

sudo mkdir -pm755 /etc/apt/keyrings #make the wine  key directory

sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key #this get the wine keys to wine can be install

sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/jammy/winehq-jammy.sources #add wine repo

sudo apt update #update all the repo

sudo apt install --install-recommends winehq-staging #installing wine

#done

echo "done plsese run ps4linux_diskimage_create.py to create your .img file"

echo "ps4linux.com"