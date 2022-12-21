# TryHackMe-Lian_YU CTF
Abdullah Rizwan , 1 spetember , 12:09 PM

## NMAP

```
export IP=10.10.209.95
```

```
nmap -sC -sV $IP

```


```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-09-01 12:09 EDT
Nmap scan report for 10.10.209.95
Host is up (0.18s latency).
Not shown: 996 closed ports
PORT    STATE SERVICE VERSION
21/tcp  open  ftp     vsftpd 3.0.2
22/tcp  open  ssh     OpenSSH 6.7p1 Debian 5+deb8u8 (protocol 2.0)
| ssh-hostkey:
|   1024 56:50:bd:11:ef:d4:ac:56:32:c3:ee:73:3e:de:87:f4 (DSA)
|   2048 39:6f:3a:9c:b6:2d:ad:0c:d8:6d:be:77:13:07:25:d6 (RSA)
|   256 a6:69:96:d7:6d:61:27:96:7e:bb:9f:83:60:1b:52:12 (ECDSA)
|_  256 3f:43:76:75:a8:5a:a6:cd:33:b0:66:42:04:91:fe:a0 (ED25519)
80/tcp  open  http    Apache httpd
|_http-server-header: Apache
|_http-title: Purgatory
111/tcp open  rpcbind 2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          37515/tcp   status
|   100024  1          40883/udp   status
|   100024  1          45950/tcp6  status
|_  100024  1          59637/udp6  status
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

<img src = "https://i.imgur.com/rF974M7.png" />

There wasn't anything useful on the web page but when I did directory force I found some interesting directories.


## Dirbuster


<img src = "https://i.imgur.com/pBVxwCR.png"/>

When we visit that page we see nothing but text but if we select all the text or look at the source we can find the code word `vigilante`.

<img src = "https://i.imgur.com/pBVxwCR.png"/>

<img src = "https://i.imgur.com/GADOifV.png"/>

Then continuing directory brute force i was able to find `/island/2100` directory

<img src ="https://i.imgur.com/FSxzDVf.png"/>

<img src = "https://i.imgur.com/k7KMl73.png"/>

Now it's giving us a hint that there is a `.ticket` file so we can again do directory busting but this time I'll use `gobuster`

## Gobuster

<img src ="https://i.imgur.com/amDxyjb.png"/>

<img src ="https://i.imgur.com/ui60A9L.png"/>

we can see an encoded message `RTy8yhBQdscX` also a name `Gambit`.

By searching this encoded text on google we will come up with the result telling us that this is base58 encoded

<img src="https://i.imgur.com/sCaR5pV.png"/>

## FTP

We logged in to ftp with user name `vigilante` and password `!#th3h00d`.

<img src="https://i.imgur.com/0tXp8su.png"/>

<img src="https://i.imgur.com/ecnlNV3.png"/>

Here we can find 3 images.

<img src="https://i.imgur.com/nZarsYG.png"/>

on looking at `Leave_Me_Alone.png` it gives us an error.

<img src="https://i.imgur.com/YifTluj.png"/>

<img src="https://i.imgur.com/rJAT3rD.png"/>

Here the header of png file is incorrect. Change the header of the image by using `hexedit`.
Then press `ctrl+x` to save.

<img src="https://i.imgur.com/48Xl2Tx.png"/>

Now the file format is correct and now let's the image.

<img src="https://i.imgur.com/0JJfqFW.png"/>

<img src="https://i.imgur.com/xlTOwHc.png"/>

<img src="https://i.imgur.com/AgmzlEm.png"/>

We can also find another user named `slade` so that `Password` can be of that user.

<img src="https://i.imgur.com/zZntQfC.png"/>

I tried to use `stegcracker` to view if there was any fild hidden with any of the images.

<img src="https://i.imgur.com/1jOV6SY.png"/>

I got two text files from `aa.png`.

<img src="https://i.imgur.com/1eescpT.png"/>

And we logged in with `slade` with the password from `shado` file.

## Privilege Escalation

<img src="https://i.imgur.com/lq2kLzB.png"/>

<img src="https://i.imgur.com/Y0pWC0X.png"/>

We got root

<img src="https://i.imgur.com/4o0I9ow.png"/>
