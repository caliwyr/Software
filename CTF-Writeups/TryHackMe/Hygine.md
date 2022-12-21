# TryHackMe-Hygiene

## NMAP 

```bash

PORT      STATE SERVICE REASON         VERSION            
22/tcp    open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)                                                 
| ssh-hostkey:   
37652/tcp open  ftp     syn-ack ttl 63 ProFTPD 1.3.5e            
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--   1 1000     1000          118 Oct 29 02:21 memo.txt                
Service Info: OSs: Linux, Unix; CPE: cpe:/o:lisnux:linux_kernel
8080/tcp  open  http-proxy                                                                                                                          
| fingerprint-strings:                                   
|   LDAPBindReq:                                           
|     HTTP/1.1 400                                                 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en                      
|     Content-Length: 2295                                       
|     Date: Thu, 04 Nov 2021 13:02:11 GMT                                        
|     Connection: close                         
|     <!doctype html><html lang="en"><head><title>HTTP Status 400
|     Request</title><style type="text/css">h1 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:22px;} h2 {font-f
amily:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:16px;} h3 {font-family:Tahoma,Arial,sans-serif;color:white;background-c
olor:#525D76;font-size:14px;} body {font-family:Tahoma,Arial,sans-serif;color:black;background-color:white;} b {font-family:Tahoma,Arial,sans-serif;
color:white;background-color:#525D76;} p {font-family:Tahoma,Arial,sans-serif;background:white;color:black;font-size:12px;} a {color:black;} a.name 
{color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><bod                                                          
|   LDAPSearchReq:                                                
|     HTTP/1.1 400                                               
|     Content-Type: text/html;charset=utf-8
```

## PORT 37652 (FTP)
From the nmap scan we can see that anonymous ftp is enabled which means that we can login without specifying the password

<img src="https://i.imgur.com/NfqZ0l5.png"/>

from the `memo.txt` file we see that a user named `joe` has sent email with the password hash and on cracking the hash we get the password `nightmare`

<img src="https://i.imgur.com/Pq9b3UX.png"/>

## PORT 8080 (HTTP)

On the webserver there's apache tomcat running

<img src="https://i.imgur.com/g8vZnOe.png"/>

if we run `stegcracker` on the png image we can find a easter egg

<img src="https://i.imgur.com/2ZYN2fO.png"/>

<img src="https://i.imgur.com/7Rj2hkd.png"/>

<img src="https://i.imgur.com/5iTa1HU.png"/>

## Foothold

### Un-inteded

We were told to find a username on the page but there wasn't any . All we know is that the username is of 5 characters so let's maybe try to brute force the username with 5 characters

<img src="https://i.imgur.com/I4eZpa3.png"/>

<img src="https://i.imgur.com/ivawOEm.png"/>

We can now then get a shell as `sally`

<img src="https://i.imgur.com/ircsnLS.png"/>


### Intended 

Running `gobuster` we can find some directories

<img src="https://i.imgur.com/U16RHo3.png"/>

I tried using default creds on `/manager` , `/host-manager` but wasn't succesful so I did a recusive fuzz on `admin`

<img src="https://i.imgur.com/KCXq3zb.png"/>

This returned us `staging` so again running gobuster on this

<img src="https://i.imgur.com/IdCmFhl.png"/>

<img src="https://i.imgur.com/dnoyOYi.png"/>

We don't see much here but if we look at the source we can find the username `sally`

<img src="https://i.imgur.com/Z6O1smj.png"/>

We can now then get a shell through ssh

<img src="https://i.imgur.com/ircsnLS.png"/>

On doing `sudo -l` we can't do run any thing as root as other user since this user isn't in sudoers file

<img src="https://i.imgur.com/3WIYbmF.png"/>

## Privilege Escalation (Joe)

We can the find the user flag in `Desktop` folder of sally and can find another flag in `/home/sally/.local/share/Trash/files`

<img src="https://i.imgur.com/lFTq9GZ.png"/>

The hash can be cracked with either `hashcat` or `john` but I'll just use cracksation as I did earlier

<img src="https://i.imgur.com/7gi9kpi.png"/>

## Privilege Escalation (root)

Running `sudo -l` we can see that this user can run all commands

<img src="https://i.imgur.com/BQuXUDP.png"/>

## References

- https://askubuntu.com/questions/911204/how-to-extract-only-7-characters-using-grep
