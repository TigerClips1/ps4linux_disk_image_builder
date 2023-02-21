#!/bin/python

import os #this is the os mudule from cpython
cmd1 = "sudo losetup /dev/loop5 /home/xxx/linux.img" #this will excute the command
error = "we can't find your linux.img make sure to move it from your ps4 oru usb in to  your home directory"#variable string that print an error on your screen
error2 = " you don't have a tar.gz file or cant be found" #variable string that print an error on your screen
path = "/home/xxxx/" #variable string
path2 = '/newroot' #variable string
cmd3 = 'tar -xvf /home/linuxuser/directory where your tar.xx' #variable string
path3 = "/home/xxxx/Documents" #variable string
error3 = "you don't have an arch base distro" #variable string
error4 = "you not on a debian base distro or on an ubuntu base distro" #variable string
credit = "scripts by TigerClips 2" #credit variable string
promo = "ps4linux.com" #promotion variable string
cmd4 = 'sudo tar -xvzf /home/xxxxx/psxitarch.tar.xx'
def disks(): #function to keep thing nice
    os.chdir(path) #change the os directory
    setup = os.popen(cmd1) #function
    output = setup.readlines() #this will read and see you have the linux.img file
    print(error) #print an error if it can't find the linux.img
    os.system('sudo mkfs.ext2 /dev/loop5') #make filesystem to ext2
    os.system('sudo mkdir /newroot') #make a directory
    os.system('sudo mount /dev/loop5 /newroot') 
    os.chdir(path2) #change the os directory
    os.system(cmd3) #extrect tar.xz files
    extrect = os.popen('cmd4') #extrect tar.gz file
    output2 = extrect.readlines() #see if it can find a tar.gz file
    print(error2) #print an error if it cant find a tar.gz file
    os.chdir(path3)#change the os directory
    wget = os.popen("sudo pacman -Syy && sudo pacman -S wget && sudo pacman -R snapd") #function
    output3 = wget.readlines() #this will read and see you have that command on your pc
    print(error3) #print error 3 on your screen if you don't have an arch base distro
    wget2 = os.popen("sudo apt-get update && sudo apt-get install wget") #function
    output4 = wget2.readlines() #this will read and see you have that command on your pc
    print(error4) #print error 4 on your screen
    os.chdir(path3) #change the os directory
    os.system("wget https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-621.exe" ) #then download winerar to you can comepress it using a gui evorment
    os.system("sudo mv winrar-x64-621.exe winrar.exe") #rename it to winrar.exe
    os.system("wine winrar.exe")   #excute the .exe file to we can install winrar


disks() #call the function 

print(credit) #print the credits on the screen
prnt(promo) #promote ps4linux
