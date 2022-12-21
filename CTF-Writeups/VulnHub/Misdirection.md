# Vulnhub-Misdirection

## NMAP

```bash


PORT     STATE SERVICE REASON         VERSION                                                                                                       
22/tcp   open  ssh     syn-ack ttl 64 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                  
| ssh-hostkey:   
|   2048 ec:bb:44:ee:f3:33:af:9f:a5:ce:b5:77:61:45:e4:36 (RSA)  
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCkS5yl+Dpb7vsMGbzAHXBYrVSUNTh4kYGh8zajM3ZujG0XHLvgkW7xJ6F/meai9IrCB5gTq7+tTsn+fqNk0cAZugz4h+vwm5ekXe5szPPHNx
NUlKuNAQ0Rch9k7jT/2pWjtsE5iF6yFlh1UA2vBKqrTWVU5vrGWswdFRMWICKWiFXwl1Tv93STPsKHYoVbq74v2y1mVOLn+3JNMmRNCBFqh8Z2x+1DTep0YY8vIV325iRK5ROKCJAPeyX33uoxQ/
cYrdPIS+Whs9QX0C+W343Hf2Ypq93h3/g3NNm54LvZdE6X2vTUcUHGdvK2gU+dWQOiDhCpMDv3wiEAwGlf87P5                                                              
|   256 67:7b:cb:4e:95:1b:78:08:8d:2a:b1:47:04:8d:62:87 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBM+YEivOAqHPDlFWduSuOjAjuJtfC9v/KW2uYB85gxQuibGJQZhFPcxwPEUf7UvQ/a5fr/keKY
F2Kdld6gO44jY=
|   256 59:04:1d:25:11:6d:89:a3:6c:6d:e4:e3:d2:3c:da:7d (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFHxbfiqinvu3cV7JoKrOF3w64zk+0N0h+/2nu+Z20Mk                                                                  
80/tcp   open  http    syn-ack ttl 64 Rocket httpd 1.2.6 (Python 2.7.15rc1)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS             
|_http-server-header: Rocket 1.2.6 Python/2.7.15rc1
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
3306/tcp open  mysql   syn-ack ttl 64 MySQL (unauthorized)
8080/tcp open  http    syn-ack ttl 64 Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works

```

## PORT 80 (HTTP)

<img src="https://i.imgur.com/vEtNZvd.png"/>

We could try signing up on the site

<img src="https://imgur.com/hNHxzRl.png"/>

But it fails

<img src="https://imgur.com/HLbylRy.png"/>


## PORT HTTP (8080)

Moving to port 8080 we can only see a default apache web server page

<img src="https://imgur.com/NOAYaI2.png"/>

After running `dirsearch` fuzzing for files and directories

<img src="https://i.imgur.com/FNhVRP8.png"/>

I saw these intersting directories so let's visit them

<img src="https://imgur.com/FifEL0Y.png"/>

`/shell` didn't have anything

<img src="https://imgur.com/jNqDY0K.png"/>

This looks like a rabbit hole, but as I visit `/debug` there's powney web shell running

<img src="https://imgur.com/kayUPbW.png"/>

Which means we can get a reverse shell simply by putting a bash reverse shell here

<img src="https://imgur.com/MSZrtlZ.png"/>

I tried the bash reverse shell but didn't got any connectio so let's try python

<img src="https://imgur.com/MKAN3NO.png"/>

python did the trick and we have a rerverse shell so let's upgrade it to a tty 

<img src="https://imgur.com/nd38gno.png"/>

Now running `sudo -l` we'll see that we can `bash` as the user `brexit`

<img src="https://i.imgur.com/epPCQau.png"/>

So we'll do `sudo -u brexit /bin/bash`

<img src="https://imgur.com/IDkvpcl.png"/>

Let's transfer `linpeas`on the machine to enumerate further

<img src="https://imgur.com/0cxru9d.png"/>

## Privilege Escalation (Method 1)

We can see that `/etc/passwd` is owned by user group so we can write on this file

<img src="https://i.imgur.com/7V1Nl9L.png"/>

<img src="https://i.imgur.com/DwMoRjo.png"/>

<img src="https://imgur.com/YaAElHJ.png"/>

We are root !!1


## Privilege Escalation (Method 2)

<img src="https://i.imgur.com/pJ6GNd8.png"/>

We can see that we are in `lxd` group , so we can abuse this to get root user , so on your local machine clone the apline image builder repoistory

<img src="https://imgur.com/RPjt9Tk.png"/>

Then run the script to create an image

<img src="https://imgur.com/Grain5A.png"/>

<img src="https://i.imgur.com/UUQAI3U.png"/>

Now you need to host this and transfer it to target machine and im

<img src="https://imgur.com/cKv4chi.png"/>

<img src="https://i.imgur.com/IVQueXZ.png"/>

Run `lxd init`

<img src="https://i.imgur.com/rZmtCOD.png"/>

Then initiliaze the image

<img src="https://imgur.com/GhMCf3u.png"/>

Now this we are in a container and we had mounted the host system in `/mnt/root`

<img src="https://i.imgur.com/3cLkcgN.png"/>

<img src="https://imgur.com/GsfuH2i.png"/>

We have the flag but not root on the host so we can either add our ssh keys in `authorized_keys` or we can make bash a SUID , so I am going go the easy and make bash a SUID binary

<img src="https://imgur.com/bGHlfIY.png"/>

Now exit the container

<img src="https://i.imgur.com/s8Nkklc.png"/>

<img src="https://imgur.com/im0OUeV.png"/>

## Privilege Escalation (Method 3)

This isn't really necessary and it might not work as the machine doens't have `gcc` installed so I am explicilty installing gcc on this machine

<img src="https://i.imgur.com/F0EUzrw.png"/>

<img src="https://imgur.com/NqWgFA4.png"/>

Now that gcc is installed we can compile the linux overlays kernel exploit

https://github.com/briskets/CVE-2021-3493

Make a `.c` file and copy the contents of expoit in it , then use gcc to compile the source code , give executable permissions to the binary and after running you'll get root instantly

<img src="https://i.imgur.com/A5Mt5kS.png"/>