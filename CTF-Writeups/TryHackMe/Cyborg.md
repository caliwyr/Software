# TryHackMe-Cyborg

## NMAP

```
Starting Nmap 7.80 ( https://nmap.org ) at 2021-01-28 16:55 PKT
Nmap scan report for 10.10.203.159
Host is up (0.42s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 db:b2:70:f3:07:ac:32:00:3f:81:b8:d0:3a:89:f3:65 (RSA)
|   256 68:e6:85:2f:69:65:5b:e7:c6:31:2c:8e:41:67:d7:ba (ECDSA)
|_  256 56:2c:79:92:ca:23:c3:91:49:35:fa:dd:69:7c:ca:ab (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 30.22 seconds
```


## Task 1 

Scan the machine, how many ports are open?

`2`

## Task 2 

What service is running on port 22?

`SSH`

## Task 3 

What service is running on port 80?

`HTTP`

## PORT 80 (HTTP)

<img src="https://imgur.com/aHhYNcp.png"/>

Running feroxbuster

<img src="https://imgur.com/QOd5Uxu.png"/>

<img src="https://imgur.com/8MCYWOO.png"/>

```
music_archive:$apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn.
```

Navigating to `/admin`

<img src="https://imgur.com/NL2tIx4.png"/>

We can download this tar archive on click the `archive` tab also visiting `admin` tab we can see some conversation which tells about squid proxy which we have already discoverd

<img src="https://imgur.com/Ses5eA6.png"/>

Extracting the tar contents

<img src="https://imgur.com/hxOOiJS.png"/>

<img src="https://imgur.com/3I5ZfsC.png"/>

This is all conmpressed and encrypted using `Borg`. Now in order to recover these encrypted files we need to have borg on our machine so let's download the binary from github

<img src="https://imgur.com/CHmjqPK.png"/>

<img src="https://imgur.com/hoOCDdk.png"/>

It's asking for a passphrase ,so the hash we saw earlier let's try to crack it with `john`

<img src="https://imgur.com/j8q1vs1.png"/>

<img src="https://imgur.com/kOa5yBl.png"/>

We got the `music_archive` which was in the conversation so now let's mount it on a folder using the passphrase

<img src="https://imgur.com/jI5jshY.png"/>

<img src="https://imgur.com/MpO1xPL.png"/>

<img src="https://imgur.com/NnkwMgi.png"/>

It wasn't really a secret!

<img src="https://imgur.com/1F9XXtu.png"/>

And this might be the creds for SSH

<img src="https://imgur.com/40R6J7a.png"/>

Here in this script `getops` is intersting which will lead us to privilege escalation

<img src="https://imgur.com/sIptnh3.png"/>

In the while loop `c:` is the argument for getops also there is a swtich case for `c` which is the command so if we specify a bash command specify -c in the script it will get excecuted as root.

<img src="https://imgur.com/EhNShAz.png"/>

<img src="https://imgur.com/eZNcueo.png"/>

We can get root if we specify `bash` after -c but we will run into a problem that we cannot see the output of the commands we are typing so to get a proper root shell we can SUID /bin/bash and can spawn a root shell with it

<img src="https://imgur.com/M7xG4li.png"/>

<img src="https://imgur.com/JQ88bfc.png"/>