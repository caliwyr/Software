# TryHackMe-0day

## NMAP

```
Nmap scan report for 10.10.44.55                                                                                      
Host is up (0.41s latency).                                                                                           
Not shown: 998 closed ports                                                                                           
PORT   STATE SERVICE VERSION                                                                                          
22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 57:20:82:3c:62:aa:8f:42:23:c0:b8:93:99:6f:49:9c (DSA)                                                       
|   2048 4c:40:db:32:64:0d:11:0c:ef:4f:b8:5b:73:9b:c7:6b (RSA)
|   256 f7:6f:78:d5:83:52:a6:4d:da:21:3c:55:47:b7:2d:6d (ECDSA)
|_  256 a5:b4:f0:84:b6:a7:8d:eb:0a:9d:3e:74:37:33:65:16 (ED25519)
80/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: 0day
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.55 seconds
```

## PORT 80

<img src="https://imgur.com/EDnud0k.png"/>

## Feroxbuster

For directory fuzzing I used `feroxbuster`

<img src="https://imgur.com/uPEPTsy.png"/>

<img src="https://imgur.com/WoP8k8m.png"/>

The `backup` directory has private key

<img src="https://imgur.com/z4XnVU0.png">

But we don't have a valid username to connect with SSH.

## Nikto

<img src="https://imgur.com/PzXw7Dr.png"/>

Alternativley we could have done this with `gobuster` or with `wfuzz`

<img src="https://imgur.com/zI7ZKQV.png"/>


With wfuzz

<img src="https://imgur.com/wt3yUft.png"/>


This told us that there is a test.cgi which we can access and there is an exploit for it which is called `shellshock` vulnerability for cgi-bin.


<img src="https://imgur.com/aG1YvUu.png"/>

Now I launched a shell in meterpreter session through `shell` then stabilized it with python.Got the user flag now only thing left to do is privilege escalation

## Privilege Escalation

<img src="https://imgur.com/ieAYkPK.png"/>

If he search an exploit for this version we will get this on exploit-db


<img src="https://imgur.com/DyBUiNI.png"/>


Have the exploit on your local machine and tranfer it to target through netcat or python web server

<img src="https://imgur.com/EmcReja.png"/>

<img src="https://imgur.com/96rP4fx.png"/>

<img src="https://imgur.com/pLxyAfz.png"/>

And we got root !!!