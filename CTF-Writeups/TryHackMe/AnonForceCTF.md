# TryHackMe-AnonForce
Abdullah Rizwan ,23 August,8:08 PM

AnonForce a boo2root beginner level box where you have to find 2 flags one for user and one for root

## NMAP

We are going to scan for open ports on the box.

```
nmap -sC -sV -oN initial/nmap 10.10.94.79 -o scan.txt
```
```
Nmap scan report for 10.10.94.79
Host is up (0.19s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| drwxr-xr-x    2 0        0            4096 Aug 11  2019 bin
| drwxr-xr-x    3 0        0            4096 Aug 11  2019 boot
| drwxr-xr-x   17 0        0            3700 Aug 23 08:10 dev
| drwxr-xr-x   85 0        0            4096 Aug 13  2019 etc
| drwxr-xr-x    3 0        0            4096 Aug 11  2019 home
| lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img -> boot/initrd.img-4.4.0-157-generic
| lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img.old -> boot/initrd.img-4.4.0-142-generic
| drwxr-xr-x   19 0        0            4096 Aug 11  2019 lib
| drwxr-xr-x    2 0        0            4096 Aug 11  2019 lib64
| drwx------    2 0        0           16384 Aug 11  2019 lost+found
| drwxr-xr-x    4 0        0            4096 Aug 11  2019 media
| drwxr-xr-x    2 0        0            4096 Feb 26  2019 mnt
| drwxrwxrwx    2 1000     1000         4096 Aug 11  2019 notread [NSE: writeable]
| drwxr-xr-x    2 0        0            4096 Aug 11  2019 opt
| dr-xr-xr-x  108 0        0               0 Aug 23 08:10 proc
| drwx------    3 0        0            4096 Aug 11  2019 root
| drwxr-xr-x   18 0        0             540 Aug 23 08:10 run
| drwxr-xr-x    2 0        0           12288 Aug 11  2019 sbin
| drwxr-xr-x    3 0        0            4096 Aug 11  2019 srv
| dr-xr-xr-x   13 0        0               0 Aug 23 08:10 sys
|_Only 20 shown. Use --script-args ftp-anon.maxlist=-1 to see all.
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.8.94.60
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 8a:f9:48:3e:11:a1:aa:fc:b7:86:71:d0:2a:f6:24:e7 (RSA)
|   256 73:5d:de:9a:88:6e:64:7a:e1:87:ec:65:ae:11:93:e3 (ECDSA)
|_  256 56:f9:9f:24:f1:52:fc:16:b7:7b:a3:e2:4f:17:b4:ea (ED25519)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.17 seconds

```
It has 2 ports one is for ftp and other is for ssh.

## FTP

<a href="https://imgur.com/aqjhhBx"><img src="https://i.imgur.com/aqjhhBx.png" title="source: imgur.com" /></a>

Now we can read any file directly because there is no command to view files so we can download that flag file and read it later.

<a href="https://imgur.com/t2O9GT8"><img src="https://i.imgur.com/t2O9GT8.png" title="source: imgur.com" /></a>

Now we came to find a folder called "noread" in which there are 2 key files.

<a href="https://imgur.com/GFMtdRb"><img src="https://i.imgur.com/GFMtdRb.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/6YlDpvU"><img src="https://i.imgur.com/6YlDpvU.png" title="source: imgur.com" /></a>


We downloaded those files and now we have to crack "private.asc".

<a href="https://imgur.com/4fJpJSV"><img src="https://i.imgur.com/4fJpJSV.png" title="source: imgur.com" /></a>

## Cracking The Hash

<a href="https://imgur.com/JdT9Cz4"><img src="https://i.imgur.com/JdT9Cz4.png" title="source: imgur.com" /></a>

Using johntheripper's gpg2john we can crack the key

<a href="https://imgur.com/xW0F96q"><img src="https://i.imgur.com/xW0F96q.png" title="source: imgur.com" /></a>

Now we know that password for "backup.pgp" is "xbox360" we are going to decrypt "backup.pgp" using this password.

<a href="https://imgur.com/Qv0YXuk"><img src="https://i.imgur.com/Qv0YXuk.png" title="source: imgur.com" /></a>

We now have obtained the root hash , now we just have to crack it.

<a href="https://imgur.com/AR0gKJq"><img src="https://i.imgur.com/AR0gKJq.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/PVV7hEC"><img src="https://i.imgur.com/PVV7hEC.png" title="source: imgur.com" /></a>

## SSH

Now we ssh into the box with username "root" and password "hikari"

<a href="https://imgur.com/D93cCzl"><img src="https://i.imgur.com/D93cCzl.png" title="source: imgur.com" /></a>

Now read "root.txt" and submit that flag to complete the CTF.
