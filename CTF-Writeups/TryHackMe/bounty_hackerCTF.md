# TryHackMe-BountyHackerCTF
Abdullah Rizwan , Friday 28 August , 05:34 PM

## NMAP

```
nmap -sC -sV 10.10.187.202
```

```
st is up (0.16s latency).
Not shown: 967 filtered ports, 30 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.8.94.60
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 dc:f8:df:a7:a6:00:6d:18:b0:70:2b:a5:aa:a6:14:3e (RSA)
|   256 ec:c0:f2:d9:1e:6f:48:7d:38:9a:e3:bb:08:c4:0c:c9 (ECDSA)
|_  256 a4:1a:15:a5:d4:b1:cf:8f:16:50:3a:7d:d0:d8:13:c2 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernelp

```

## PORT 80

<a href="https://imgur.com/yWhYYLR"><img src="https://i.imgur.com/yWhYYLR.png" title="source: imgur.com" /></a>


## Dirbuster

<a href="https://imgur.com/1tJ2fbA"><img src="https://i.imgur.com/1tJ2fbA.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/bsZXqQt"><img src="https://i.imgur.com/bsZXqQt.png" title="source: imgur.com" /></a>

Since we have access to ftp through "anonymous" login we can upload a php reverse shell.

## PORT 21

<a href="https://imgur.com/Yzi3RVj"><img src="https://i.imgur.com/Yzi3RVj.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/2PEM3XF"><img src="https://i.imgur.com/2PEM3XF.png" title="source: imgur.com" /></a>


We can grab the task.txt through "get" command.

<a href="https://imgur.com/cXcctEl"><img src="https://i.imgur.com/cXcctEl.png" title="source: imgur.com" /></a>

We also found a list of passwords so that we can use it in brute forcing.

<a href="https://imgur.com/EQI8x3Z"><img src="https://i.imgur.com/EQI8x3Z.png" title="source: imgur.com" /></a>

## PORT 22

By looking at the text file we can check if "lin" is a user on that box so we can bruteforce our way in through ssh by using hyrda.

```
hydra -l lin -P locks.txt ssh://$IP -t 4
```
$IP is nothing but a variable for bash environment , export IP=10.10.187.202.


<a href="https://imgur.com/1q78mpp"><img src="https://i.imgur.com/1q78mpp.png" title="source: imgur.com" /></a>

We found the password for "lin".

<a href="https://imgur.com/8XILjSX"><img src="https://i.imgur.com/8XILjSX.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/M4DQ6cV"><img src="https://i.imgur.com/M4DQ6cV.png" title="source: imgur.com" /></a>

We can root the box through "/bin/tar" we can find exploit to it by visiting GTFOBINS.

<a href="https://imgur.com/c8r4CsV"><img src="https://i.imgur.com/c8r4CsV.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/wsGPsPb"><img src="https://i.imgur.com/wsGPsPb.png" title="source: imgur.com" /></a>

We are now root and we can read that root.txt flag in order to complete the CTF.
