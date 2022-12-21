# TryHackMe-Team

## Rustscan

```bash
PORT   STATE SERVICE REASON         VERSION                                                                                                         
21/tcp open  ftp     syn-ack ttl 63 vsftpd 3.0.3    
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:                                                            
|   2048 79:5f:11:6a:85:c2:08:24:30:6c:d4:88:74:1b:79:4d (RSA)            
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDRK/xFh/H4lC7shWUUvK9lKxd3VO2OwfsC8LjFEU2CnEUrbVCnzx8jiVp5gO+CVAj63+GXkbIuXpynlQ/4j1dXdVUz/yAZ96cHiCNo6S5ThO
NoG2g2ObJSviCX2wBXhUJEzW07mRdtx4nesr6XWMj9hwIlSfSBS2iPEiqHfGrjp14NjG6Xmq5hxZh5Iq3dBrOd/ZZKjGsHe+RElAMzIwRK5NwFlE7zt7ZiANrFSy4YD4zerNSyEnjPdnE6/ArBmq
OFtsWKZ2p/Wc0oLOP7d6YBwQyZ9yQNVGYS9gDIGZyQCYsMDVJf7jNvRp/3Ru53FMRcsYm5+ItIrgrx5GbpA+LR
|   256 af:7e:3f:7e:b4:86:58:83:f1:f6:a2:54:a6:9b:ba:ad (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBM4d9TCz3FkEBEJ1VMjOsCrxsbS3YGb7mu9WgtnaFPZs2eG4ssCWz9nWeLolFgvHyT5WxRT0S
FSv3vCZCtN86I=
|   256 26:25:b0:7b:dc:3f:b2:94:37:12:5d:cd:06:98:c7:9f (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHUxjoul7JvmqQMtGOuadBwi2mBVCdXhJjoG5x+l+uQn
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works! If you see this add 'te...
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port

```

## PORT 80 (HTTP)

<img src="https://imgur.com/WEBaKST.png"/>

We'll see a domain 

<img src="https://imgur.com/nYbjZwL.png"/>

<img src="https://imgur.com/MNFPErU.png"/>

<img src="https://imgur.com/I0OyPMm.png"/>

Checking `robots.txt` we'll find a text `dale` not sure if it's a username or a directory

<img src="https://imgur.com/JptYtIY.png"/>


Next I ran `feroxbuster` on the domain but it didn't find anything interesting

<img src="https://imgur.com/4jgcpax.png"/>

Then doing recursive fuzzing on `/scripts` found a text file

<img src="https://imgur.com/q7YZo8V.png"/>

<img src="https://imgur.com/ggQjamQ.png"/>

So by doing doing a GET request for `sciprt.old` we can download a file

<img src="https://imgur.com/Vd5ByER.png"/>

<img src="https://imgur.com/640DLcK.png"/>

And we get the creds for ftp server

<img src="https://imgur.com/jcYw4Op.png"/>

In `workshare` directorty we have another file

<img src="https://imgur.com/OkmP3ak.png"/>

<img src="https://imgur.com/EvdidR4.png"/>

Add the subdomain in `/etc/hosts`

<img src="https://imgur.com/Aae2Knw.png"/>

<img src="https://imgur.com/sAoDsBy.png"/>

<img src="https://imgur.com/Vzufq5t.png"/>

We can see that paramter is grabbing a file so if not properly santized it will lead to LFI

<img src="https://imgur.com/wUopwpT.png"/>

Reading the note that gayle left for dale was about "config file " so I tried to view ssh config file

<img src="https://imgur.com/W2wZ5SJ.png"/>

Here we can see dale's id_rsa , so now we can ssh into the box

<img src="https://imgur.com/wz5Jj0S.png"/>

Doing `sudo -l ` we can run a script as `gayle`

<img src="https://imgur.com/ccluJEe.png"/>

<img src="https://imgur.com/KEqSqwK.png"/>


I uploaded `pspy64` on the machine and ran it and found that a script was running as root

<img src="https://imgur.com/W3f4sOx.png"/>

If we look in the script

<img src="https://imgur.com/af0tQfQ.png"/>

It's running two scripts , we can only edit `/usr/local/bin/main_backup.sh`

<img src="https://imgur.com/TCnI1Ot.png"/>

Here I just inserted a command to make bash a SUID now we wait for couple of seconds

<img src="https://imgur.com/aIxUfmj.png"/>

We can see the `s` flag on bash which means it's now a SUID , if we run bash with `-p` it will with the user who owns the binary

<img src="https://imgur.com/zWueYcW.png"/>