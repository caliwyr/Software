# TryHackMe-Hacker Of The Hill

## Easy

### Rustscan

```
rustscan -a 10.10.193.208 -- -A -sC -sV                                       
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.                                                          
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |                  
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |                  
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'                                                                                            
The Modern Day Port Scanner.                                                                                                                        
________________________________________                                                                                                            
: https://discord.gg/GFrQsGy           :                                                                                                            
: https://github.com/RustScan/RustScan :                                  
 --------------------------------------                                                                                                             
🌍HACK THE PLANET🌍                                                                                                                                 
                                                                                                                                                    
[~] The config file is expected to be at "/root/.rustscan.toml"                                                                                     
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers                                 
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'.          
Open 10.10.193.208:22                                                     
Open 10.10.193.208:80
Open 10.10.193.208:8001
Open 10.10.193.208:8000
Open 10.10.193.208:8002                                                                                                    
Open 10.10.193.208:9999                                                                                                       
PORT     STATE SERVICE REASON         VERSION                                                                 

PORT     STATE SERVICE REASON         VERSION                                                                                               [96/388]
22/tcp   open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:                                                            
|   2048 f7:75:95:c7:6d:f4:92:a0:0e:1e:60:b8:be:4d:92:b1 (RSA)      
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC7FOhvQRnCoPOd/4kYKsFt1Z81Zn7/eHHCcC1aHXfWK3UskQJaeWDqPcjeXN+ceZbiyKXUBpvAIWlg5Gphn1iCJoWxsCibNzZlZczJmjM2L+
fW/maaKRmiFL1fxxgkzNpssK3cF2dyNZ4uitwFhl5imMScEx/E1Lt86545ZxijjmlhUcbxvERh5nC+84RoIRr979qKWvOHgFyLXwOi+FGj5x1DZ0ZcmhsUORX8n9ZsqqUNM01R2MittszQr1CEa0
QFvrRyJawV1vHerdaYKaFbwvfR2Ip9d8VI4MmhMqb9fnnwRSYGP3qDKoscJo6UF4wtIMT79/obcXP1GdvoROc7
|   256 a2:11:fb:e8:c5:c6:f8:98:b3:f8:d3:e3:91:56:b2:34 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBCSG/mKt+u+M1pEEuYBYY/LTbDOftPdV5ZBYGyVS0aF5DiRbsYQaOtswUarmEbUO05LIlSUZG6
dK88BSm2DjnAU=                       
|   256 72:19:b7:04:4c:df:18:be:6b:0f:9d:da:d5:14:68:c5 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIF3y6QxJnjq+vtxnKq2LJB1EIy+RSy5rZqltZulxj6RA
80/tcp   open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
| http-methods:        
|_  Supported Methods: GET POST OPTIONS HEAD                                                                                                        
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
8000/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST                                                                                                                     
| http-robots.txt: 1 disallowed entry  
|_/vbcms                                                                                                                                            
|_http-server-header: Apache/2.4.29 (Ubuntu)                                                                                                        
|_http-title: VeryBasicCMS - Home
8001/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-title: My Website
|_Requested resource was /?page=home.php
8002/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Learn PHP
9999/tcp open  abyss?  syn-ack ttl 63 
| fingerprint-strings: 
|   FourOhFourRequest, GetRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Date: Sat, 20 Feb 2021 19:24:58 GMT
|     Content-Length: 0
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|_    Request


```

### PORT 22 (SSH)

### PORT 80 (HTTP)

<img src="https://imgur.com/6NzfSGF.png"/>


### PORT 8000 (HTTP)

<img src="https://imgur.com/NSTRdGB.png"/>

There wasn't anything on Home , About and Contact page. Running gobuster on the port 8000

<img src="https://imgur.com/4SPnxrx.png"/>

<img src="https://imgur.com/tlkYGye.png"/>

But we did see an entry in `robots.txt`

<img src="https://imgur.com/Je6sota.png"/>

Logging in with `admin:admin`

<img src="https://imgur.com/AGu9XCB.png"/>

<img src="https://imgur.com/8jCnQwp.png"/>

Here we can see these are html pages but we can include php code in between it 

<img src="https://imgur.com/jME85YI.png"/>

<img src="https://imgur.com/qgdDnlG.png"/>

<img src="https://imgur.com/sqf0wiE.png"/>

And we have a RCE working so let's leverege this to get a reverse shell

<img src="https://imgur.com/aZboei3.png"/>

<img src="https://imgur.com/PYs4t8i.png"/>

From the looks of it this a base64 ecoded text

<img src="https://imgur.com/Xn3IWIM.png"/>

Doing a  `cat /etc/crontab` to list system wide crontab we see a cronjob running as root 

<img src="https://imgur.com/n8wOdhu.png"/>

We also see `secret.txt` in `/var/www/html/topSecretPrivescMethod`

<img src="https://imgur.com/NUNE6CP.png"/>

Reading `/var/lib/rary` from the hints

<img src="https://imgur.com/58iJagE.png"/>

This was the flag that we need to enter in the correct format


### PORT 8001 (HTTP)

<img src="https://imgur.com/2oCczNh.png"/>


### PORT 80002 (HTTP)

<img src="https://imgur.com/YgI5urR.png"/>

To get a reverse shell paste the php reverse shell without having `php` tags in it

<img src="https://imgur.com/xvLW1bL.png"/>

Now we can edit that script which is running in crontab

<img src="https://imgur.com/1DPFPWc.png"/>

To get `root.txt`

<img src="https://imgur.com/4M8VctB.png"/>