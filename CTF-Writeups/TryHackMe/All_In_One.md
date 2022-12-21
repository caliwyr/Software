# TryHackMe-All In One

## NMAP

```
Nmap scan report for 10.10.6.115                                                                                                              [3/26]
Host is up (0.45s latency).                                               
Not shown: 997 closed ports                                               
PORT   STATE SERVICE VERSION                                                                                                                        
21/tcp open  ftp     vsftpd 3.0.3                                         
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)                                                                                              
| ftp-syst:                          
|   STAT:                            
| FTP server status:                 
|      Connected to ::ffff:10.2.54.209                                    
|      Logged in as ftp              
|      TYPE: ASCII                   
|      No session bandwidth limit                                         
|      Session timeout in seconds is 300                                  
|      Control connection is plain text                                   
|      Data connections will be plain text                                
|      At session startup, client count was 2                             
|      vsFTPd 3.0.3 - secure, fast, stable                                
|_End of status                      
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                                   
| ssh-hostkey:                       
|   2048 e2:5c:33:22:76:5c:93:66:cd:96:9c:16:6a:b3:17:a4 (RSA)                                                                                      
|   256 1b:6a:36:e1:8e:b4:96:5e:c6:ef:0d:91:37:58:59:b6 (ECDSA)                                                                                     
|_  256 fb:fa:db:ea:4e:ed:20:2b:91:18:9d:58:a0:6a:50:ec (ED25519)                                                                                   
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))                       
|_http-server-header: Apache/2.4.29 (Ubuntu)                              
|_http-title: Apache2 Ubuntu Default Page: It works                       
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel            
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                                                      
Nmap done: 1 IP address (1 host up) scanned in 48.55 seconds      

```

## PORT 21 (FTP)

<img src="https://imgur.com/ItY8JJ2.png"/>

There wasn't anythin on ftp so this was a rabbit hole

## PORT 80

Visting the web page we don't find that much than a default apache web page

<img src="https://imgur.com/Arc5ddD.png"/>

Now on ruuning `gobuster` we can find a directory `wordpress` and `hackathons`

<img src="https://imgur.com/Z26Kvcd.png"/>

<img src="https://imgur.com/Pgx04m6.png"/>

On ruuning `wpscan` for finding any users

<img src="https://imgur.com/nCtZa9m.png"/>

We find `elyana` as a registered user on `wordpress`

<img src="https://imgur.com/ssYiYUd.png"/>

For finiding the plugins that this wordpress is using

<img src="https://imgur.com/JYkBNpZ.png"/>

<img src="https://imgur.com/ZE28Hfy.png"/>

`mail-masta` and `reflex-gallery` are the two plugins that this wordpress is using

That's all we can find on the `wordpress` directory let's see if there is anything on `hackathons`

<img src="https://imgur.com/Gvti919.png"/>

Looking at the source code

<img src="https://imgur.com/D4EXqva.png"/>

We find some ecnrypted text and after trying different encryption techniques we found that this a `vigenere encoded text`

<img src="https://imgur.com/RrocwsV.png"/>

<img src="https://imgur.com/EIuYyss.png"/>

We logged in with the password `H@ckme@123` removing `Try` from it ( :

Now we can edit the 404 page on theme `Twenty Twenty`

<img src="https://imgur.com/R1K1yd9.png"/>

Pasting a php reverse shell from pentestmonkey

<img src="https://imgur.com/hzY5B9a.png"/>

Then setup a netcat listener

<img src="https://imgur.com/tNi6v2N.png"/>

Running a `find` command to look for files for user `elyana` 

<img src="https://imgur.com/TK4nT1V.png"/>

<img src="https://imgur.com/hbMLDA1.png"/>

Here elyana is in groups `sudo` and `lxd` , so lxd may have privilege escalation technique

Checking for `sudo -l` 

We 'll find that we can run `socat` as root

<img src="https://imgur.com/N9vpket.png"/>

<img src="https://imgur.com/8qlhLKG.png"/>



