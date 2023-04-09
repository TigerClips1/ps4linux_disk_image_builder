
#Dont run this run the other script if you on linux until i get a seta to usb to test the script MAC coming SOON
CMD = "sudo python3 PS4Linux_DiskImage without removeing.py"
os.system(CMD)


#!/bin/python  #make it where you can hit tab it will autofill it



#import os #import os muduals for this script to work

#username = input("Please Enter your Linux Username: ")

#number = input("Please Enter the number of how much space you want: ")

#print("ps4 drivers require for the os to boot when done installing that then run this script") #reminder

#error = "Error you don't have an ubuntu base distro or debian base distro" #error 1 variable string

#error2 = "Error you don't have an fedora base distro" #error 2 variable string

#error3 = "Error you don't have an arch base distro" #error3 variable string

#credit = "scripts by TigerClips 2" #credit variable string

#promo = "ps4linux.com" #promotion variable string

#path = f"/home/{username}/Documents" #variable string

#path2 = f"/home/{username}/Documents/yay" #variable string

#path3 = "/newroot" #variable string

#archS = "sudo pacman -S git wget wine wine-mono wine-gecko wget" #variable string

#clone = "git clone https://aur.archlinux.org/yay.git" #variable string

#PS4 = f"sudo cryptsetup -d /home/{username}/Documents/eap_hdd_key.bin --cipher=aes-xts-plain64 -s 256 --offset=0 --skip=111669149696 create ps4hdd /dev/sda27" #variable string

#PS4_2 = "yay -S rar unrar cryptmount" #variable string

#makepkgs = "makepkg -si" #variable string

#PS4_3 = "sudo mkdir /ps4hdd"

#Mount_PS4 = "sudo mount -t ufs -o ufstype=ufs2 /dev/mapper/ps4hdd /ps4hdd" #variable string

#PS4_installer = f"sudo dd if=/dev/null of=/ps4hdd/home/linux.img bs=1073741824 seek={number} status=progress" #variable string

#PS4_setup = "sudo losetup /dev/loop5 /ps4hdd/home/linux.img" #variable string

#Makefile = "sudo mkfs.ext2 /dev/loop5" #variable string

#PS4Linux_Mount = "sudo mount /dev/loop5 /newroot" #variable string

#PS4_Mounst = f'sudo tar -cvf ps4linux.tar.xz --exclude=/home/{username}/Documents/ps4linux.tar.xz --exclude=/var/cache --one-file-system / -I "xz -9" + ' #variable string

#extrects = f'sudo tar -xvf /home/{username}/Documents/ps4linux.tar.xz' #variable string

#remove = "sudo rm -rf *" #variable string

#winrars = 'wget https://www.rarlab.com/rar/winrar-x64-621b1.exe' #variable string

#renamee = 'sudo mv winrar-x64-621b1.exe winrar.exe' #variable string

#winrar_boot = "sudo wine winrar.exe" #variable string

#ps4_unmount = "sudo  umount /dev/loop5" #variable string

#arch

#def arch(): #function to keep thing nice
    
 #   os.chdir(path)#change directory to that << to we can keep thing nice
    
  #  os.system(archS) #this will install the requirement for arch to run this script
    
   # os.chdir(path)
    
    #os.system(clone) #clone aur helper repo
    
    #os.chdir(path2 ) # change directory to aur helper
    
    #os.system(makepkgs) #this bulid the aur helper
    
    #yay = os.popen(PS4_2) #this install rar and unrar for people who want to use the command line
    
    #output2 = yay.readlines() #output to see if there pacman but if you not on an arch base distro then it will give you an error
    
    #print(error3) #print the error on the screen


#def disks(): #function to keep thing nice
    
 #   os.chdir(path)#change directory to that << to we can keep thing nice
    
  #  print(f"this will create a {number}G diskimage file\n") #print text on the screen
    
   # print("plese close out of everything only thing need to be open is the terminal") #print text on the screen
    
    #os.system(PS4) #setup ps4 HDD
    
    #this may work don't know
    #os.system(PS4_3) #make the directory for the ps4hdd
    
    #os.system(Mount_PS4) #mount the ps4 drive from pc to it can work
    
    #os.system(PS4_installer) #start making the diskimage file 
    
    #os.system(PS4_setup) #setuop the diskimage file
    
    #os.system(Makefile) #Create ext2 filesystem on loop device
    
    #os.system (PS4Linux_Mount)
    
    #os.system (PS4_Mounst) #comepile all files in the root directory to tar.xz to we can run the diskimage file on the ps4
    
    #os.chdir (path3) #change directory to the diskimage protation
    
    #os.system(extrects) #extrect the tar.xz file to the diskimage file
    
    #os.chdir (path) #change dirctory
    
    #os.system(remove) #remove all files in the docments dirctory
    
    #os.chdir (path) #change dirctory
    
    #os.system(winrars)#then download winerar to you can comepress it using a gui evorment
    
    #os.system(renamee) #rename the file to wine can read it a bit easy
    
    #os.system(winrar_boot) #excute the .exe file to we can install winrar
    
    #os.system(ps4_unmount) #unmount loop5 to you can easly change the os in the /newroot

#ubuntu_debian() #calling the function

#arch()  # calling the arch function

#disks() #calling the disk function

#print("done\n") #print text to let the person know that they done

#print(credit, sep="\n") #credit me

#print(promo) #promote the ps4linux site