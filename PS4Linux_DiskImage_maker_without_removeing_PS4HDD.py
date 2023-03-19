#!/bin/python

import os #this is the os mudule from cpython

USERNAME = input("Please Enter your linux Username: ") #get input from user

print(f"Make sure your diskimage file is in the /home/{USERNAME}/psxitarch.tar.xz or tar.gz and /home/{USERNAME}/linux.img \n") #print text on the screen

CMD1 = f"sudo losetup /dev/loop5 /home/{USERNAME}/linux.img" #this will excute the command

ERROR = "we can't find your linux.img make sure to move it from your ps4 oru usb in to  your home directory"#variable string that print an error on your screen

ERROR2 = " you don't have a tar.gz file or cant be found" #variable string that print an error on your screen

PATH = f"/home/{USERNAME}/" #variable string

PATH2 = '/PS4' #variable string

CMD3 = f'sudo tar -xvf /home/{USERNAME}/psxitarch.tar.xz' #variable string

PATH3 = f"/home/{USERNAME}/Documents" #variable string

ERROR3 = "you don't have an arch base distro" #variable string

CREDIT = "scripts by TigerClips 2 \n" #credit variable string

PROMO = "ps4linux.com \n" #promotion variable string

CMD4 = f'sudo tar -xvzf /home/{USERNAME}/psxitarch.tar.gz' #extrect tar.gz file

REMOVE = "sudo rm -rf /PS4"

EXT2 = "sudo mkfs.ext2 /dev/loop5"

MAKE = "sudo mkdir /PS4"

ARCH = "sudo pacman -Syy && sudo pacman -S wget && sudo pacman -R snapd"

MOUNT = "sudo mount /dev/loop5 /PS4"

REMOVE_NEWROOT = "sudo rm -rf *"

END = "Done"

RAR_LINUX = "wget https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-621.exe"

RENAMES = "sudo mv winrar-x64-621.exe winrar.exe"

WINE_LINUX = "wine winrar.exe"

UNMOUNT = "sudo  umount /dev/loop5"

print("Installing\n")

def disks(): #function to keep thing nice
    os.chdir(PATH) #change the os directory
    if disks:
        os.system(CMD1) #function
    
    else:
    
     print(ERROR) #print an error if it can't find the linux.img
    
    
    os.system(REMOVE) #this will remove the /newroot directory to when installing the os you want have your screen flashing
    
    os.system(EXT2) #make filesystem to ext2
    
    os.system(MAKE) #make a directory
    
    os.system(MOUNT)  #mount the diskimage file as loop5
    
    os.chdir(PATH2) #change the os directory
    
    os.system(REMOVE_NEWROOT) #remove the lost+found folder in the diskimage file
    if disks:
        
        os.system(CMD3) #extrect tar.xz files
    else:
        print("we can't find an tar.xz")
    if disks:
        os.system(CMD4) #extrect tar.gz file
    else:    
        print(ERROR2) #print an error if it cant find a tar.gz file
    
    os.chdir(PATH3)#change the os directory
    if disks:
        os.system(ARCH) #function
    else:
        print(ERROR3) #print error 3 on your screen if you don't have an arch base distro
    
    os.chdir(PATH3) #change the os directory
    
    os.system(RAR_LINUX ) #then download winerar to you can comepress it using a gui evorment
    
    os.system(RENAMES) #rename it to winrar.exe
    
    os.system(WINE_LINUX)   #excute the .exe file to we can install winrar
    
    os.system(UNMOUNT) #unmount loop5 to you can easly change the os in the /newroot

disks() #call the function 

print(END, sep = "\n")

print(CREDIT, sep= "\n") #print the credits on the screen

print(PROMO) #promote ps4linux
