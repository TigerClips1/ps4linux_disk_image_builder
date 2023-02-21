#!/bin/sh
#this will make it where you can hit tab and it will autofill it

#intro
echo "wine is require to create an rar file useing winrar gui on linux to comepress the .img file " #Wekcome screen

sudo dpkg --add-architecture i386  #make it where 32 bit is enable for debian

echo "please be on debian  for this to work"

sudo mkdir -pm755 /etc/apt/keyrings   #make the wine  key directory

sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key #this get the wine keys to wine can be install for debian 

sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/debian/dists/bullseye/winehq-bullseye.sources #add the wine repo for debian 11


sudo apt update #update all the repo

sudo apt install --install-recommends winehq-staging #installing wine
#outro

echo "done plsese run ps4linux_diskimage_create.py to create your .img file"

echo "ps4linux.com"
# ps this script is for dev who know how to make drivers for the ps4
#not require by normal people to run this script
