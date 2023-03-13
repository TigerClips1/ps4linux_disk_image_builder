#!/bin/python  #make it where you can hit tab it will autofill it

import os #import os muduals for this script to work
username = input("Please Enter your Linux Username: ")
number = input("Please Enter the number of how much space you want: ")
print("ps4 drivers require for the os to boot when done installing that then run this script") #reminder

error = "Error you don't have an ubuntu base distro or debian base distro" #error 1 variable string

error2 = "Error you don't have an fedora base distro" #error 2 variable string

error3 = "Error you don't have an arch base distro" #error3 variable string

credit = "scripts by TigerClips 2" #credit variable string

promo = "ps4linux.com" #promotion variable string

path = f"/home/{username}/Documents"


path2 = f"/home/{username}/Documents/yay"

path3 = "/newroot"

archS = "sudo pacman -S git wget wine wine-mono wine-gecko wget"

clone = "git clone https://aur.archlinux.org/yay.git"

        
        

#arch

def arch(): #function to keep thing nice
    
    os.chdir(path)#change directory to that << to we can keep thing nice
    
    os.system(archS) #this will install the requirement for arch to run this script
    
    os.chdir(path)
    
    os.system(clone) #clone aur helper repo
    
    os.chdir(path2 ) # change directory to aur helper
    
    os.system('makepkg -si') #this bulid the aur helper
    
    yay = os.popen('yay -S rar unrar cryptmount') #this install rar and unrar for people who want to use the command line
    
    output2 = yay.readlines() #output to see if there pacman but if you not on an arch base distro then it will give you an error
    
    print(error3) #print the error on the screen


def disks(): #function to keep thing nice
    
    os.chdir(path)#change directory to that << to we can keep thing nice
    
    print(f"this will create a {number}G diskimage file\n") #print text on the screen
    
    print("plese close out of everything only thing need to be open is the terminal")
    
    os.system(f'sudo cryptsetup -d /home/{username}/Documents/eap_hdd_key.bin --cipher=aes-xts-plain64 -s 256 --offset=0 --skip=111669149696 create ps4hdd /dev/sda27') #setup ps4 HDD
    
    os.system('sudo mkdir /ps4hdd') #make the directory for the ps4hdd
    
    os.system('sudo mount -t ufs -o ufstype=ufs2 /dev/mapper/ps4hdd /ps4hdd') #mount the ps4 drive from pc to it can work
    
    os.system(f'sudo dd if=/dev/null of=/ps4hdd/home/linux.img bs=1073741824 seek={number} status=progress') #start making the diskimage file 
    
    os.system('sudo losetup /dev/loop5 /ps4hdd/home/linux.img') #setuop the diskimage file
    
    os.system('sudo mkfs.ext2 /dev/loop5') #Create ext2 filesystem on loop device
    
    os.system ('sudo mount /dev/loop5 /newroot')
    
    os.system (f'sudo tar -cvf ps4linux.tar.xz --exclude=/home/{username}/Documents/ps4linux.tar.xz --exclude=/var/cache --one-file-system / -I "xz -9" + ') #comepile all files in the root directory to tar.xz to we can run the diskimage file on the ps4
    
    os.chdir (path3) #change directory to the diskimage protation
    
    os.system(f'sudo tar -xvf /home/{username}/Documents/ps4linux.tar.xz') #extrect the tar.xz file to the diskimage file
    
    os.chdir (path)
    
    os.system('sudo rm -rf *')
    
    os.chdir (path)
    
    os.system('wget https://www.rarlab.com/rar/winrar-x64-621b1.exe')#then download winerar to you can comepress it using a gui evorment
    
    os.system('sudo mv winrar-x64-621b1.exe winrar.exe') #rename the file to wine can read it a bit easy
    
    os.system("sudo wine winrar.exe") #excute the .exe file to we can install winrar
    
    os.system('sudo  umount /dev/loop5') #unmount loop5 to you can easly change the os in the /newroot

ubuntu_debian() #calling the function

arch()  # calling the arch function

disks() #calling the disk function

print("done\n") #print text to let the person know that they done

print(credit, sep="\n") #credit me

print(promo) #promote the ps4linux site