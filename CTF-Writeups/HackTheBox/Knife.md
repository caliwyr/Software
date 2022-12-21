# HackTheBox-Knife

## NMAP

```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title:  Emergent Medical Idea
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

## PORT 80 (HTTP)

On the webserver we only get a static web page

<img src="https://imgur.com/DS0Wpof.png"/>

I didn't find anything on the site, it's a php page so I tried default parameters but it didn't work too so I ran a nikto scan which is useful for identifying vulnerabilites on web server

## Nikto

On running `nikto` , I came to know the version of php it's using which is `PHP/8.1.0-dev` 

<img src="https://i.imgur.com/XM762dS.png"/>

On march 2021 this version was implanted with a backdoor which is discovered and removed the github repo,attacker can execute arbitrary code by sending the `User-Agentt` header

https://github.com/vulhub/vulhub/blob/master/php/8.1-backdoor/README.zh-cn.md

So let's test this by following what's in the github repo

<img src="https://i.imgur.com/uQFMweM.png"/>

<img src="https://i.imgur.com/hUjMgJE.png"/>

https://www.zdnet.com/article/official-php-git-server-targeted-in-attempt-to-bury-malware-in-code-base/

This works, according to the finidngs ,the `User-Agnett` header needs `zerodium` and after that we can supply php commands so we could execute commands and get RCE

<img src="https://i.imgur.com/PCHs9oJ.png"/>

We can grab the id_rsa from `james`'s  home folder

<img src="https://i.imgur.com/uW1ZrVu.png"/>

<img src="https://imgur.com/GkGgSxd.png"/>

<img src="https://imgur.com/pVk1WyN.png"/>

But the ssh key doesn't work, so replace the public ssh key 

<img src="https://imgur.com/ZaGkWz3.png"/>

Also add that public key to `authorized_keys`

<img src="https://imgur.com/RiIuKHY.png"/>

Doing `sudo -l` we can see what we can run as sudo

<img src="https://i.imgur.com/19IVrRC.png"/>

Let's see the help menu for `knife`

<img src="https://imgur.com/siHnCjm.png"/>

If we scroll down a little we can that we can execute ruby scripts meaning we can run shell commands

<img src="https://i.imgur.com/40qvgXB.png"/>

<img src="https://i.imgur.com/nUrxDs0.png"/>

So I added my public ssh key in `/root/.ssh/authorized_keys/` . we could have gotten a reverse shell or made bash SUID

<img src="https://imgur.com/Pmn5exA.png"/>

Getting a reverse shell

<img src="https://i.imgur.com/dwXMO4J.png"/>