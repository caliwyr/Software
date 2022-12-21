# TryHackMe-Archangel

## Rustscan

```
rustscan -a 10.10.53.100 -- -A -sC -sV                                                     
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.                                                                                            
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |                                                                                            
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |                                                                                            
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'                                                                                            
The Modern Day Port Scanner.                                                                                                                        
________________________________________                                                                                                            
: https://discord.gg/GFrQsGy           :                                                                                                            
: https://github.com/RustScan/RustScan :                                                                                                            
 --------------------------------------                                                                                                             
😵 https://admin.tryhackme.com                                                    
[~] The config file is expected to be at "/root/.rustscan.toml"                                                                                     
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers                                 
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'.          
Open 10.10.53.100:22                                                                            
Open 10.10.53.100:80                                                                                                                                
[~] Starting Script(s)                                                                                                                              
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")               

PORT   STATE SERVICE REASON         VERSION                                                                                                         
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                    
| ssh-hostkey:                                                                                                                                      
|   2048 9f:1d:2c:9d:6c:a4:0e:46:40:50:6f:ed:cf:1c:f3:8c (RSA)                                                                                      
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDPrwb4vLZ/CJqefgxZMUh3zsubjXMLrKYpP8Oy5jNSRaZynNICWMQNfcuLZ2GZbR84iEQJrNqCFcbsgD+4OPyy0TXV1biJExck3OlriDBn3g
9trxh6qcHTBKoUMM3CnEJtuaZ1ZPmmebbRGyrG03jzIow+w2updsJ3C0nkUxdSQ7FaNxwYOZ5S3X5XdLw2RXu/o130fs6qmFYYTm2qii6Ilf5EkyffeYRc8SbPpZKoEpT7TQ08VYEICier9ND408
kGERHinsVtBDkaCec3XmWXkFsOJUdW4BYVhrD3M8JBvL1kPmReOnx8Q7JX2JpGDenXNOjEBS3BIX2vjj17Qo3V                                                              
|   256 63:73:27:c7:61:04:25:6a:08:70:7a:36:b2:f2:84:0d (ECDSA)                                                                                     
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKhhd/akQ2OLPa2ogtMy7V/GEqDyDz8IZZQ+266QEHke6vdC9papydu1wlbdtMVdOPx1S6zxA4
CzyrcIwDQSiCg=                                                                                                                                      
|   256 b6:4e:d2:9c:37:85:d6:76:53:e8:c4:e0:48:1c:ae:6c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBE3FV9PrmRlGbT2XSUjGvDjlWoA/7nPoHjcCXLer12O
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
| http-methods:                                                           
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)           
|_http-title: Wavefire
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port

```

## PORT 80 (HTTP)

<img src="https://imgur.com/GzEgNx0.png"/>

Looking at the source code we can find a domain name

<img src="https://imgur.com/iJy5GmF.png"/>

So lets put this is in our `/etc/hosts` file 

<img src="https://imgur.com/AHoDyxC.png"/>

<img src="https://imgur.com/7xaEQXU.png"/>

Now we need to fuzz for a page that is "under development" for that I am going to use gobuster

<img src="https://imgur.com/4lPUfzJ.png"/>

And we found a `test.php` file 

<img src="https://imgur.com/Gd2C9KU.png"/>

<img src="https://imgur.com/Uu36x36.png"/>

On clicking the button we can see on the url there's a GET parameter being used so we can check for LFI (Local File Inclusion) vulnerability. I tired a bunch of LFI techniques like `../../../../etc/passwd` but it failed.

<img src="https://imgur.com/Q0shF8C.png"/>

I used this technqiue what it does is that encodes the whole page into base64.

`http://mafialive.thm/test.php?view=php://filter/convert.base64-encode/resource=/var/www/html/development_testing/mrrobot.php`

<img src="https://imgur.com/xX2Ztjv.png"/>

We can do this for `test.php` as well 

`http://mafialive.thm/test.php?view=php://filter/convert.base64-encode/resource=/var/www/html/development_testing/test.php`

<img src="https://imgur.com/XCpP94e.png"/>

<img src="https://imgur.com/fC8HCUD.png"/>

<img src="https://imgur.com/1JepDNl.png"/>

We can fuzz for /etc/passwd to do that we can use `wfuzz` 

```
http://mafialive.thm/test.php?view=/var/www/html/development_testing/test.php
```

<img src="https://imgur.com/9w9mWwk.png"/>

This doesn't help as we are getting the length of the response 286 and 310 which is not /etc/passwd so we can hide that response

<img src='https://imgur.com/ezKJMsw.png'/>

<img src="https://imgur.com/iy2dgWl.png"/>

For getting a reverse shell we need to poison the apach2 log file but before that we need to make sure that log is being accessbile.

<img src="https://imgur.com/CmWeia2.png"/>

We can access the log by the method above

```
http://mafialive.thm/test.php?view=/var/www/html/development_testing./.././.././.././..///var/log/apache2/access.log
```

<img src="https://imgur.com/HZQn93g.png"/>

Now intercept the request through burp suite and add php GET parameter code in `User-Agent`

<img src="https://imgur.com/VfRxInb.png"/>

Let's try to access the page with `&c=id` at the end 

```
http://mafialive.thm/test.php?view=/var/www/html/development_testing./.././.././.././..///var/log/apache2/access.log&c=id
```

<img src="https://imgur.com/Z7nw5hi.png"/>

We can at the bottom of the page that id command was executed so we can now get a reverse shell 

Host a file having a reverse shell payload in it

<img src="https://imgur.com/IhO8kGi.png"/>

<img src="https://imgur.com/2H5eTG1.png"/>

On running the command

<img src="https://imgur.com/qKInj6U.png"/>

Now we need to give it permission to execute

<img src="https://imgur.com/hxszvFV.png"/>

Execute it 

<img src="https://imgur.com/0U7ipES.png"/>

<img src="https://imgur.com/Cp5PN7m.png"/>

Checking cronjobs we see

<img src="https://imgur.com/lf6TYXh.png"/>

<img src="https://imgur.com/jzVwAJp.png"/>

We can see that this file can be written by anyone so we can write bash reverse shell to get a shell as user `archangel`

<img src="https://imgur.com/e58k880.png"/>

And we got the shell 

<img src="https://imgur.com/BFlBYEC.png"/>

We can see `backup` binary having a SUID also it belongs to root user and group , on using strings on it

<img src="https://imgur.com/uug0IBR.png"/>

We can see that it's using cp (copy command) so here PATH exploitation comes where we can create a binary with the same name having `bash` in it and then set PATH where that "fake" binary is stored

<img src="https://imgur.com/RaY1lES.png"/>
<img src="https://imgur.com/z6VnV18.png"/>

Now run that binary

<img src="https://imgur.com/qbDuXBW.png"/>

For simplicity I made /bin/bash a SUID to run as root

<img src="https://imgur.com/AKUekJQ.png"/>
