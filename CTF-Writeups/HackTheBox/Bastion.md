# HackTheBox-Bastion

## Rustscan

```bash
PORT      STATE SERVICE      REASON          VERSION                                                                                        [76/184]
22/tcp    open  ssh          syn-ack ttl 127 OpenSSH for_Windows_7.9 (protocol 2.0)                  
| ssh-hostkey:   
|   2048 3a:56:ae:75:3c:78:0e:c8:56:4d:cb:1c:22:bf:45:8a (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3bG3TRRwV6dlU1lPbviOW+3fBC7wab+KSQ0Gyhvf9Z1OxFh9v5e6GP4rt5Ss76ic1oAJPIDvQwGlKdeUEnjtEtQXB/78Ptw6IPPPPwF5dI1
W4GvoGR4MV5Q6CPpJ6HLIJdvAcn3isTCZgoJT69xRK0ymPnqUqaB+/ptC4xvHmW9ptHdYjDOFLlwxg17e7Sy0CA67PW/nXu7+OKaIOx0lLn8QPEcyrYVCWAqVcUsgNNAjR4h1G7tYLVg3SGrbSmI
cxlhSMexIFIVfR37LFlNIYc6Pa58lj2MSQLusIzRoQxaXO4YSp/dM1tk7CN2cKx1PTd9VVSDH+/Nq0HCXPiYh3
|   256 cc:2e:56:ab:19:97:d5:bb:03:fb:82:cd:63:da:68:01 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBF1Mau7cS9INLBOXVd4TXFX/02+0gYbMoFzIayeYeEOAcFQrAXa1nxhHjhfpHXWEj2u0Z/hfPB
zOLBGi/ngFRUg=
|   256 93:5f:5d:aa:ca:9f:53:e7:f2:82:e6:64:a8:a3:a0:18 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIB34X2ZgGpYNXYb+KLFENmf0P0iQ22Q0sjws2ATjFsiN
135/tcp   open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
139/tcp   open  netbios-ssn  syn-ack ttl 127 Microsoft Windows netbios-ssn 
445/tcp   open  microsoft-ds syn-ack ttl 127 Windows Server 2016 Standard 14393 microsoft-ds
5985/tcp  open  http         syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
47001/tcp open  http         syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49665/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49666/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49667/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49668/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49669/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49670/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC

```

## PORT 139/445 (SMB)

We can see smb share on the machine , let's list down the shares as `anonymous` user if it's enabled

<img src="https://i.imgur.com/txiMNXY.png"/>

`Backups` share is the only share we can read and write so this is interesting

<img src="https://i.imgur.com/YM7CuBZ.png"/>

The note says

```
Sysadmins: please don't transfer the entire backup file locally, the VPN to the subsidiary office is too slow.

```

Looking at the contents of `WindowsImageBackup` we see a lot of xml files

<img src="https://i.imgur.com/irhn3gn.png"/>

I checked all the xml files but nothing seemed to be interesting only but those vhd files , vhd  is a file format which represents a virtual hard disk drive . It may contain what is found on a physical HDD, such as disk partitions and a file system. The problem is that the file size is 5 GB is gonna take a long time in downloading it , what we can do is mount that on our linux file system

So for that we may need to install`libguestfs-tools` and `cifs-utils` following this article

https://medium.com/@abali6980/mounting-vhd-files-in-kali-linux-through-remote-share-smb-1c4d37c22211

<img src="https://i.imgur.com/tZIzAnG.png"/>

<img src="https://imgur.com/anIxCBw.png"/>

With this command we can mount the `Backups` share

```bash
mount -t cifs -o user=admin,rw,iocharset=utf8,file_mode=0777,noperm, "//10.10.10.134/Backups" /mnt/vhd

```

<img src="https://i.imgur.com/bG7Kl6T.png"/>

<img src="https://imgur.com/3w7ysC1.png"/>

Now we need to mount the vhd file which is the backup made for the windows machine for that we will use `guestmount`

```bash
guestmount --add "9b9cfbc4-369e-11e9-a17c-806e6f6e6963.vhd" --ins
pector --ro -v /mnt/vhd                    
```

<img src="https://imgur.com/cUhkkDG.png"/>

<img src="https://imgur.com/1R1Z984.png"/>

And it's been mounted so let's navigate through the files 

<img src="https://imgur.com/dtQeEqc.png"/>

Now we have the backup of the C drive so we can look for SAM and SYSTEM file which contains the password hash of the users in `SAM` and boot key in `SYSTEM` which is located in `C:\Windows\System32\config`

<img src="https://i.imgur.com/RuURDtb.png"/>

Now we can dump hashes using impacket tool called `secretsdump`

<img src="https://i.imgur.com/6RPpRmp.png"/>

So now we got the hashes let's try to crack them using `crackstation` which is online site for cracking hashes like MD5,SHA-1,NTLM and etc.

<img src="https://i.imgur.com/Gdc1fFX.png"/>

And we cracked `L4mpje`'s hash . Now we can login to target machine through ssh


<img src="https://i.imgur.com/65TdI6W.png"/>

The ssh connection was a bit laggy so I decided to generate a meterpreter payload

<img src="https://imgur.com/tyTrlGM.png"/>

Since we have read and write access on `Backups` share we can upload `shell.exe` our payload but I ran into a problem , our payload gets deleted

<img src="https://i.imgur.com/o9pk0Sq.png"/>

Going through Program Files (x86) I came across `mRemoteNG` which seemed pecuilar to me 

<img src="https://i.imgur.com/Pru5VYT.png"/>

mRemoteNG is an open source application which supports protocols like RP,VNC,SSH,Telnet which is made for windows, we can abuse this as this program saves the ecnrypted password in user's Local AppData folder in xml file 

<img src="https://i.imgur.com/c4wILeX.png"/>

http://cosine-security.blogspot.com/2011/06/stealing-password-from-mremote.html

So I searched if there are any 

<img src="https://imgur.com/ErUVPV7.png"/>

And we found a script that will decrypt the string and give us the password but first we need to save the xml file
	 
<img src="https://i.imgur.com/niYWQ63.png"/>

But this didn't contain the encrypted password so I went back to `AppData\Roaming\mRemoteNG` and there I found the `confCons.xml`

<img src="https://i.imgur.com/y6kJXaL.png"/>

<img src="https://i.imgur.com/A4dNyRl.png"/>

Now we need to use the script to decrypt the password

<img src="https://i.imgur.com/0LI1OSe.png"/>

And looks like it decrypted it ,so let's cross fingers and see if we can login as `Administrator`

<img src="https://imgur.com/TzL9khQ.png"/>

And we are done with this machine

```
L4mpje:bureaulampje
Administrator:thXLHM96BeKL0ER2

Administrator:aEWNFV5uGcjUHF0uS17QTdT9kVqtKCPeoC0Nw5dmaPFjNQ2kt/zO5xDqE4HdVmHAowVRdC7emf7lWWA10dQKiw==

L4mpje:yhgmiu5bbuamU3qMUKc/uYDdmbMrJZ/JvR1kYe4Bhiu8bXybLxVnO0U9fKRylI7NcB9QuRsZVvla8esB
```