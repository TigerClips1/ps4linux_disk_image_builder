#!/bin/python  #make it where you can hit tab it will autofill it

import os #import os muduals for this script to work

print("ps4 drivers require for the os to boot when done installing that then run this script") #reminder
error = "Error you don't have an ubuntu base distro or debian base distro" #error 1 variable string
error2 = "Error you don't have an fedora base distro" #error 2 variable string
error3 = "Error you don't have an arch base distro" #error3 variable string
credit = "scripts by TigerClips 2" #credit variable string
promo = "ps4linux.com" #promotion variable string


#ubuntu/debian
def ubuntu_debian(): #function to keep thing nice
        rar = os.popen('sudo apt-get update && sudo apt-get install unrar rar wget') #command to install the requirements for ubuntu/debian abse distro
        output = rar.readlines() #output to see if the commands ruturn with no error
        print (error) #print the error if you try to run that commands say for fedora base distro


#arch
def arch(): #function to keep thing nice
    os.system('sudo pacman -S git wget wine wine-mono wine-gecko') #this will install the requirement for arch to run this script
    os.system(' git clone https://aur.archlinux.org/yay.git') #clone aur helper repo
    os.system('cd yay' ) # change directory to aur helper
    os.system('makepkg -si') #this bulid the aur helper
    yay = os.popen('yay -Syyu && yay -S rar unrar') #this install rar and unrar for people who want to use the command line
    output2 = yay.readlines() #output to see if there pacman but if you not on an arch base distro then it will give you an error
    print(error3) #print the error on the screen
    
#disk image file creater reminder
print("please use a vm like qmeu or vitrualbox those 2 vm client is suported \n") #print text on your screen

os.system('cd /home/$USER/Documents') #change directory to that << to we can keep thing nice

def disks(): #function to keep thing nice
    print("this will create a 100G diskimage file\n") #print text on the screen
    os.system('sudo dd if=/dev/vda1 of=/home/$USER/Documents/linux.img bs=1G count=100 sync status=progress') #start making the diskimage file 
    os.system('wget https://www.rarlab.com/rar/winrar-x64-621b1.exe')#then download winerar to you can comepress it using a gui evorment
    os.system('sudo mv winrar-x64-621b1.exe winrar.exe') #rename the file to wine can read it a bit easy
    os.system("sudo wine winrar.exe") #excute the .exe file to we can install winrar
    
ubuntu_debian() #calling the function
arch()  # calling the arch function
disks() #calling the disk function

print("done\n") #print text to let the person know that they done
print(credit, sep="\n") #credit me
print(promo) #promote the ps4linux site