# Vulnhub-Mercy

## Rustscan

```bash

PORT     STATE SERVICE     REASON         VERSION              
53/tcp   open  domain      syn-ack ttl 64 ISC BIND 9.9.5-3ubuntu0.17 (Ubuntu Linux)
| dns-nsid:                  
|_  bind.version: 9.9.5-3ubuntu0.17-Ubuntu                        
110/tcp  open  pop3?       syn-ack ttl 64                
|_ssl-date: TLS randomness does not represent time          
139/tcp  open  netbios-ssn syn-ack ttl 64 Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
143/tcp  open  imap        syn-ack ttl 64 Dovecot imapd                
|_ssl-date: TLS randomness does not represent time                        
445/tcp  open  netbios-ssn syn-ack ttl 64 Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
993/tcp  open  ssl/imaps?  syn-ack ttl 64                             
|_ssl-date: TLS randomness does not represent time
995/tcp  open  ssl/pop3s?  syn-ack ttl 64                                 
|_ssl-date: TLS randomness does not represent time                        
8080/tcp open  http        syn-ack ttl 64 Apache Tomcat/Coyote JSP engine 1.1
| http-methods:                                                           
|   Supported Methods: GET HEAD POST PUT DELETE OPTIONS                   
|_  Potentially risky methods: PUT DELETE
|_http-open-proxy: Proxy might be redirecting requests                    
| http-robots.txt: 1 disallowed entry                                     
|_/tryharder/tryharder                                               
|_http-server-header: Apache-Coyote/1.1                                   
|_http-title: Apache Tomcat                                            
MAC Address: 80:00:0B:3C:4A:7E (Intel Corporate)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
```


## PORT 139/445 (SMB)

We can check for smb share and see if we have access or not 

<img src="https://imgur.com/HFg47SB.png"/>

So we cannot access any share , we can try to use `enum4linx` to enumerate for users on the machine

<img src="https://imgur.com/QmJ0RzM.png"/>

<img src="https://i.imgur.com/TuMmeOo.png"/>

## PORT 8080 (HTTP Apache Tomcat 7)

<img src="https://imgur.com/1h3w3hq.png"/>

From the nmap scan we can see an entry in `robots.txt`

<img src="https://imgur.com/TiVbRnz.png"/>

<img src="https://imgur.com/3ahlQT4.png"/>

This looks like a base64 encoded text , so let's decode and see what it says

<img src="https://i.imgur.com/eMwkJQA.png"/>

```
It's annoying, but we repeat this over and over again: cyber hygiene is extremely important. Please stop setting silly passwords that will get cracked with any decent password list.

Once, we found the password "password", quite literally sticking on a post-it in front of an employee's desk! As silly as it may be, the employee pleaded for mercy when we threatened to fire her.

No fluffy bunnies for those who set insecure passwords and endanger the enterprise.
```

This message tells us that user's password is set to `password` so we know there are 4 users and we saw a smb share named `qiu` which is a username so we can try if this password fits for that user

<img src="https://imgur.com/SMRBhEv.png"/>

And it is the password for this user so we can read the share

<img src="https://i.imgur.com/H31WF0u.png"/>


Going to `.private/opensesame` folder we can see a config file

<img src="https://i.imgur.com/OFv5Vll.png"/>

This config file is for smb and we can see port knocking configuration in here

<img src="https://i.imgur.com/gxcXEJ2.png"/>

So let's do port knocking for http

<img src="https://i.imgur.com/tbp9cRZ.png"/>

<img src="https://imgur.com/lFNo9sx.png"/>

## PORT 80 (HTTP)

<img src="https://imgur.com/edl1vJv.png"/>

We can check `robost.txt` file

<img src="https://imgur.com/6838D1J.png"/>

Found nothing here

<img src="https://imgur.com/KPLIDiL.png"/>

We found RIPS and we have a version 0.53 so we look for exploits on `exploit-db`

<img src="https://imgur.com/Vm9eToh.png"/>

There's a LFI exploit in two files `code.php` and `function.php` , we can look at  the source code for these two files since there's a repo on github

https://github.com/bizonix/rips-scanner


<img src="https://imgur.com/IZv56pM.png"/>

We confirmed that LFI exists now let's take a step back , we know there's apache tomcat so we could look `tomcat-users.xml` file which includes a username and password to login into `/manager` but we need to the installation path , so I did a little goolge search

<img src="https://i.imgur.com/56n22dH.png"/>


```
http://192.168.1.9/nomercy/windows/code.php?file=../../../../../../var/lib/tomcat7/conf/tomcat-users.xml
```

<img src="https://i.imgur.com/1bnAur0.png"/>

We can login to `/manager` with user `thisisasuperduperlonguser:heartbreakisinevitable` since he as admin role

<img src="https://imgur.com/7l22fxP.png"/>

<img src="https://imgur.com/bdaVHYB.png"/>

Here we can upload a WAR reverse shell payload so let's generate a WAR payload
 
<img src="https://imgur.com/BU1VXMk.png"/>

<img src="https://imgur.com/sD8yAaS.png"/>

And we got a shell so let's just stabilize it

<img src="https://imgur.com/yLUB0mQ.png"/>

We had already found the password for fluffy so let's switch the user

<img src="https://imgur.com/ovQkt5p.png"/>

There's a timeclock file 

<img src="https://i.imgur.com/C35XFBr.png"/>

By reading it's content we can see it just stores time in a file

<img src="https://imgur.com/4eGFsLT.png"/>

But we can see it belongs to `root` user so we can check if it's running as a schedule task

<img src="https://imgur.com/1Qdj3ao.png"/>

But we cannot see this file to be running as a `system-wide` cronjob so this would be running as root user cron job to verify it we can use `pspy` which is a unprivileged process monitor , since 64 bit version of pspy wasn't I uploaded 32 bit version and ran it

<img src="https://i.imgur.com/g7MR96S.png"/>

<img src="https://i.imgur.com/pb8bVbC.png"/>

We can see that this script runs as root so we could either include a reverse shell in there or make bash as SUID (which is a easy way) so let's modify the bash script

<img src="https://i.imgur.com/VX4qFpz.png"/>

`chmod +s /bin/bash` will make bash a SUID means it will be executed as root if we supply `-p` parameter when executing it

After waiting for some time we can check if it's been made a SUID or not so to verify it run `ls -la` on bash

<img src="https://i.imgur.com/WRvURAN.png"/>

And it looks like it's now a SUID

<img src="https://i.imgur.com/OOTK5nI.png"/>

We can add a password to get a `root` prompt (not really necessary to do this)

<img src="https://imgur.com/EEswDyR.png"/>