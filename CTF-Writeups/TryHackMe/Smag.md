# TryHackMe- Smag Grotto

## NMAP

```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-15 20:09 PKT
Nmap scan report for 10.10.56.250
Host is up (0.15s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 74:e0:e1:b4:05:85:6a:15:68:7e:16:da:f2:c7:6b:ee (RSA)
|   256 bd:43:62:b9:a1:86:51:36:f8:c7:df:f9:0f:63:8f:a3 (ECDSA)
|_  256 f9:e7:da:07:8f:10:af:97:0b:32:87:c9:32:d7:1b:76 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Smag
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.81 seconds

```
## PORT 80

<img src="https://imgur.com/qh7Sog8.png"/>

There was nothing on the page so I ran `gobuster`

<img src="https://imgur.com/UO6C5tr.png"/>


<img src="https://imgur.com/HZmF8wP.png"/>

<img src="https://imgur.com/xeTzBsS.png"/>

Download the `pcap` file 

<img src="https://imgur.com/R9rDjSv.png"/>

See the 4th packet and follow `HTTP stream`

<img src="https://imgur.com/y57Mdid.png"/>

username=helpdesk&password=cH4nG3M3_n0w

We can see `Host : development.smag.thm` edit this in our `/etc/hosts` and the box's IP

<img src="https://imgur.com/KGbbtyq.png"/>

<img src="https://imgur.com/gPoGI71.png"/>

<img src="https://imgur.com/CHZo21J.png"/>

We can then see admin and login page

<img src="https://imgur.com/8158u2f.png"/>

Login with the credentials found above , now we can see that we can enter commmands but normal commands weren't working so I typed a `php` reverse shell 

<img src="https://imgur.com/rfaqQoH.png"/>

Once we are in we can see a cronjob running 

<img src="https://imgur.com/k4ibbeH.png"/>

Here we can replace it with our local machine's public key so that when we try to connect with ssh with our private key we can get access to the box with `jake` user

<img src="https://imgur.com/ed1UhmD.png"/>

In order to do that we must generate public and private key

<img src="https://imgur.com/sZ25vqd.png"/>

Now I copied my `id_rsa.pub` and pasted in their 

<img src="https://imgur.com/Jm5juk8.png"/>

<img src="https://imgur.com/W7VRz1s.png"/>

<img src="https://imgur.com/dXsfOM5.png"/>

We can see that this user can `apt-get` as sudo 

Search on google for privesc via `apt-get` , GTFOBIN is a great resource for escalating as root with binaries

https://gtfobins.github.io/gtfobins/apt-get/

<img src='https://imgur.com/Oflq3XZ.png'/>