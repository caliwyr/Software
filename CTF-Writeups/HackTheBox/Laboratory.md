# HackTheBox-Laboratory

## Rustscan

```  
rustscan -a 10.10.10.216 -- -A -sC -sV                                                          
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.                  
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |                  
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |                  
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'                  
The Modern Day Port Scanner.                                              
________________________________________                                  
: https://discord.gg/GFrQsGy           :                                  
: https://github.com/RustScan/RustScan :                                  
 --------------------------------------                                   
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan                                                                                         
[~] The config file is expected to be at "/root/.rustscan.toml"                                                                                     
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers                                 
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'.          
Open 10.10.10.216:22                                                      
Open 10.10.10.216:80                                                      
Open 10.10.10.216:443                                                     

PORT    STATE SERVICE  REASON         VERSION                                                                                                       
22/tcp  open  ssh      syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)                                                  
80/tcp  open  http     syn-ack ttl 63 Apache httpd 2.4.41    
| http-methods:                                                           
|_  Supported Methods: GET HEAD POST OPTIONS                      
|_http-server-header: Apache/2.4.41 (Ubuntu)                              
|_http-title: Did not follow redirect to https://laboratory.htb/
443/tcp open  ssl/http syn-ack ttl 63 Apache httpd 2.4.41 ((Ubuntu))
| http-methods:                  
|_  Supported Methods: OPTIONS HEAD GET POST                      
|_http-server-header: Apache/2.4.41 (Ubuntu)                      
|_http-title: The Laboratory                                              
| ssl-cert: Subject: commonName=laboratory.htb                            
| Subject Alternative Name: DNS:git.laboratory.htb
| Issuer: commonName=laboratory.htb                                       
| Public Key type: rsa                                                    
| Public Key bits: 4096                                                   
| Signature Algorithm: sha256WithRSAEncryption                            

```

## PORT 80/443 (HTTP/HTTPS)

On visting port 80 I was redirected to https with a domain `laboratory.htb`

<img src="https://imgur.com/nB0Zr6v.png"/>

So let's add this to `/etc/hosts` file

<img src="https://imgur.com/GFoRXeq.png"/>

<img src="https://imgur.com/XociGX0.png"/>

Running dirsearch was pointless because couldn't find anything 

<img src="https://imgur.com/SN9y1ll.png"/>

But I did saw a subdomain from the nmap scan `git.laboratory.htb` on adding to `/etc/hosts`

<img src="https://imgur.com/I9Ww7kj.png"/>

<img src="https://imgur.com/6iD1qy9.png"/>

We could not sign in since we have not found any users so I registered an account

<img src="https://imgur.com/AC7e87h.png"/>

On logging in we can't see anything useful

<img src="https://imgur.com/6vqC0pW.png"/>

But going to help page we see the version number of gitlab which is 12.8.1

<img src="https://imgur.com/l68jSb7.png"/>

Searching an exploit for this version I found one RCE

https://github.com/dotPY-hax/gitlab_RCE

Edited the email for the payload

<img src="https://imgur.com/j2FPvpK.png"/>

<img src="https://imgur.com/lqasn6w.png"/>

<img src="https://imgur.com/7BxSNbg.png"/>

But it was not stable

<img src="https://imgur.com/F7wwxCN.png"/>

I grabbed the `secrets.yml` through unstablized shell also realized that this was a docker container 

<img src="https://imgur.com/J6AAUj8.png"/>

It was unstable so I decide to go for metasploit 

https://www.rapid7.com/db/modules/exploit/multi/http/gitlab_file_read_rce/

<img src="https://imgur.com/tMxecPd.png"/>

These are the options you would have to set

<img src="https://imgur.com/3CSDfye.png"/>

And we get a bash prompt

<img src="https://imgur.com/UnXDCeS.png"/>

To get a more stablized shell

<img src="https://imgur.com/6MKH4uP.png"/>

<img src="https://imgur.com/UU1hBgU.png"/>

I searched for `pentesting gitlab` and found a website that had some juicy information about what to look for

<img src="https://imgur.com/IVVMNYw.png"/>

<img src="https://imgur.com/FrhcHw3.png"/>

I saw a user `dexter` that had a a repository

<img src="https://imgur.com/Xiu43Xi.png"/>

But there wasn't anything intersting there looking back at that directory I saw two files having `secret` in them

<img src="https://imgur.com/tTtXo4Q.png"/>

Didn't found anything then I came across a report that was submitted on hackerone regarding gitlab

https://hackerone.com/reports/493324

<img src="https://imgur.com/6Myw6mk.png"/>

<img src="https://imgur.com/4Jk2B9b.png"/>

But this didn't worked so I searched for `gitlab shell change user password ` and found documentation

<img src="https://imgur.com/92dknff.png"/>

After going through this I came to know that we can reset a user's password on gitlab

<img src="https://imgur.com/U1erFXG.png"/>

And we logged in as `dexter`

<img src="https://imgur.com/kmhW6GP.png"/>

<img src="https://imgur.com/yu8SzJG.png"/>

<img src="https://imgur.com/bv0ssqz.png"/>

We see a ssh key so we can login as `dexter`

<img src="https://imgur.com/k4lmbo1.png"/>

There was a cron job running

<img src="https://imgur.com/u7dtGYY.png"/>

But I couldn't run docker

<img src="https://imgur.com/AuHY3mY.png"/>

Because we don't have permissions to execute. So here I spend a lot of time running `linpeas` , manual going through folders but found nothing then I looked for SUID

<img src="https://imgur.com/krWeTed.png"/>

<img src="https://imgur.com/Epis19B.png"/>

<img src="https://imgur.com/qehja4S.png"/>

We see that it's using `chmod` so we can exploit PATH variable

```
#!/bin/bash
bash

```

<img src="https://imgur.com/5s1yJZL.png"/>

<img src="https://imgur.com/hTlYzHb.png"/>