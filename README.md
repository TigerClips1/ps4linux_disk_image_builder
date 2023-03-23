[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/tigerclips1)


⚠️ Warning this is still in dev and may need to test by other people  because i don't have the tool to take out the ps4 hdd or the seta to usb so if it work please let me know at  TigerClips 2#3277 on discord  ⚠️


also for the ps4linux_diskimage_create.py to work you have to mount you ps4 hdd to your pc until i find a workaround to not have 
to remove the ps4hdd when running the script

but for PS4Linux_DiskImage_maker_without_removeing_PS4HDD.py you just need an diskimage file your ps4 made for that  to work i will show a video down here  when i edit to it can be high res 

but here the text version of that until the video get done

make sure ps4 xplorer homebrew app is install by Lapy05575948 for you to do all these steps

1. so first you run goldhen delete any arch.img or linux.img in the /user/home then delete the tar.xz or tar.gz file in the /user/system/boot 

2. then you run the linux payload then  if you on nazky initramfs run exec install-HDD.sh or 

3. if you using modded warfare initramfs run exec install-linux-hdd.sh 

4. type in your storage amount for example 100 then the initramfs will create your diskimage file from the ps4

4. then you unplug your ps4 and plug it back in and boot back to orbis os enable gold hen again 

5. then enable ftp then move the diskimage file your ps4 made in ftp from /user/home then copy that to your pc hdd then run my sudo python3 PS4Linux_DiskImage_maker_without_removeing_PS4HDD.py script then i use winrar to comepress it havey then i move it to the ps4 /data

6. then i run the apollo save tool to extract it then i move the linux.img that in the linux fiolder on /data/foldername/ i cut linux.img or Arch.img then i remove  the linux.img or Arch.img in the /user/home 

7. then move the diskimage i extract with apollo to /user/home   that what i did 

also all the ps4linux os that in tar.gz or tar.xz the size need to be 5.74G is the max for it can boot with my script anything over it will not boot

I am not responeable for any damage you did to your disk 

for this script to work you need to get your sfalsh fellow this guide that show you how to get your sflash0 from [ftp](https://florinsdistortedvision.github.io/orbisunjailed/sflash-backup/)

for you to get your hdd keys you need python2 and run pip2 install -r requirements.txt

then move the sflash0 to /home/$USER/Documents    then also move the hdd_script.py to /home/$USER/Documents 

you need to be on a linux os oe wsl for all these script to work must be run as root

then run python2 hdd_script.py sflash0

you need to mount the ps4 hdd fellow this [guide](https://www.psdevwiki.com/ps4/Mounting_HDD_in_Linux) - and you need to take note of 

video that explains it better [here](https://www.youtube.com/watch?v=xcPEjxGHoE4) video may be old but it work onece you dump your hdd 

keys with zecoxao hdd_script.py 
 
then rename the key.bin to eap_hdd_key.bin

now in the ps4linux_diskimage_create.py

then take out your ps4 hdd and plug it in to your pc make sure you buy this [to](https://www.amazon.com/StarTech-com-SATA-USB-Cable-USB3S2SAT3CB/dp/B00HJZJI84/ref=sr_1_8?c=ts&keywords=SATA+Cables&qid=1676933902&s=pc&sr=1-8&ts_id=3015394011) buy that cable then you can connect your ps4 hdd to your pc then run my script in the 

vm and make sure you call the ps4 hdd in the vm then install ps4 drivers to the os in vm then run python3 

ps4linux_diskimage_create.py if you have the ps4 hdd connect to yourr pc then it will create a diskimage file in the ps4hdd from 

your pc without being in the ps4

for you to run the os you need to have ps4 drivers

look at this guide when making a rar file using the gui for linux to make sure you check the right [box](https://www.quora.com/How-do-I-highly-compress-files-using-winrar)

make sure the dirctory size is  1MB to it can be comepress vary small
![example1](https://github.com/TigerClips1/ps4linux_disk_image_maker/blob/master/example.png)

but there is  a image that show you how to set it up

ad check out ps4linux.com for the latest news about ps4linux

if you have any isuse i will be on discord TigerClips 2#3277

1. you run the  requirements_for_ps4_diskimage.sh to install python3-pip for arch and ubuntu/debian
python3 is what require for you to run my python script

2. run the fedora_ps4_diskimage_requirement.sh for fedora base distro that will set everything up for you but if you not on fedora then read the next line

3. just run  debian_wine_requirement.sh to install wine for debian base distro becuse wine is require for this to work but you need to be a dev when making ps4 drivers for debian

4. install wine for ubuntu run ubuntu_wine_requirement.sh it will install wine for ubuntu 22.04


ps4 drivers for ubuntu  by noob 404 can be found[here](https://github.com/noob404yt/ps4-pop-os-drivers) 

fedora 36 drivers by noob404 can be found [here](https://github.com/noob404yt/ps4-nobara-drivers)

arch drivers by nazky can be found [here](https://github.com/Hakkuraifu/PS4Linux-ArchDrivers)

that's it there may be alot of spelling errors in here but i will fix that  in a later update

also for  you to get bluetooth to work /wifi for some ps4 downlaods this [kernel](https://ps4linux.com/s/rxzab) -to fix that
[pre made diskimage file](https://drive.google.com/file/d/10vsFHzeZVCuroh8SKLMplKNAkqfcWi4U/view?usp=sharing) - here some premade diskimage i made to you don't have to remove the PS4HDD enjoy


this is still a work in progress so you may need to test it

if you have any error you get in the script let me know to i can fix it.

this is really the only way i can think  when making hdd .img file from your pc without being in the ps4

premade diskimage file for the PS4 can be find [here](https://t.co/KODyTHH0MC) - pre made blank diskimage file for Aeolia/Belize
Thankes for reading and hope this help to make ps4 hdd .img file

TODO: 

~~1. add input to you can input  space diskimage file from the python script~~

2. fix spelling error in the comments


