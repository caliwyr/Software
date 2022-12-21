# HackTheBox-Traverxec

## NMAP

```bash
PORT   STATE SERVICE REASON         VERSION                                                                                              
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.9p1 Debian 10+deb10u1 (protocol 2.0)
| ssh-hostkey:                                                            
|   2048 aa:99:a8:16:68:cd:41:cc:f9:6c:84:01:c7:59:09:5c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDVWo6eEhBKO19Owd6sVIAFVCJjQqSL4g16oI/DoFwUo+ubJyyIeTRagQNE91YdCrENXF2qBs2yFj2fqfRZy9iqGB09VOZt6i8oalpbmFwkBD
tCdHoIAZbaZFKAl+m1UBell2v0xUhAy37Wl9BjoUU3EQBVF5QJNQqvb/mSqHsi5TAJcMtCpWKA4So3pwZcTatSu5x/RYdKzzo9fWSS6hjO4/hdJ4BM6eyKQxa29vl/ea1PvcHPY5EDTRX5RtraV9
HAT7w2zIZH5W6i3BQvMGEckrrvVTZ6Ge3Gjx00ORLBdoVyqQeXQzIJ/vuDuJOH2G6E/AHDsw3n5yFNMKeCvNNL
|   256 93:dd:1a:23:ee:d7:1f:08:6b:58:47:09:73:a3:88:cc (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLpsS/IDFr0gxOgk9GkAT0G4vhnRdtvoL8iem2q8yoRCatUIib1nkp5ViHvLEgL6e3AnzUJGFL
I3TFz+CInilq4=
|   256 9d:d6:62:1e:7a:fb:8f:56:92:e6:37:f1:10:db:9b:ce (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGJ16OMR0bxc/4SAEl1yiyEUxC3i/dFH7ftnCU7+P+3s
80/tcp open  http    syn-ack ttl 63 nostromo 1.9.6
|_http-favicon: Unknown favicon MD5: FED84E16B6CCFE88EE7FFAAE5DFEFD34
| http-methods: 
|_  Supported Methods: GET HEAD POST
|_http-server-header: nostromo 1.9.6
|_http-title: TRAVERXEC
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

## PORT 80 (HTTP)

On the webserver we can see a html template page

<img src="https://i.imgur.com/WRVoaF5.png"/>

I tried running `gobuster` to fuzz for files and directories

<img src="https://i.imgur.com/K7tmO2T.png"/>

But it didn't find anything useful, looking at the result from nmap it's using `nostromo` which is a web server on the default HTTP port. nostromo is a simple HTTP server developed in C and the version and it's using the version 1.9.6 which is vulnerable to remote code execution

<img src="https://i.imgur.com/QctknkK.png"/>

<img src="https://i.imgur.com/2qGVfSP.png"/>

Now let's just get a reverse shell

<img src="https://imgur.com/yDvRmYp.png"/>

<img src="https://imgur.com/PJmoO3v.png"/>

We can stabilize the shell with python

<img src="https://imgur.com/XvfAg3m.png"/>

There's a metasploit module for that too so let's test that as well

<img src="https://imgur.com/yhhOOlo.png"/>

<img src="https://imgur.com/HRFefZg.png"/>

This works as well so let's just focus on our reverse shell and run `linpeas` to enumerate the target machine

<img src="https://imgur.com/fxxuDTk.png"/>

But I did not found anything by running linpeas so let's try running `pspy` which is a process mointor script

<img src="https://imgur.com/Cr3IdFH.png"/>

I waited for sometime and then something ran in the background `apt-get`

<img src="https://imgur.com/Ip7SpeI.png"/>

Also I looked in `nostromo` directory where I found `.htpasswd` file which had a hash for `david`

<img src="https://imgur.com/uuI1cPp.png"/>

It took so long that I gave up running `hashcat` , there was another file named `nhttpd.conf` which had configuration for nostromo http server

<img src="https://imgur.com/CmRfW0W.png"/>

https://www.nazgul.ch/dev/nostromo_man.html

Looking at documentation for `nhttpd`

<img src="https://imgur.com/1dWIq36.png"/>

It seems we can access `david`'s home directory

<img src="https://imgur.com/hqxSrKT.png"/>

But we are not allowed to view further but maybe there's `homedirs_public` which is set to `public_www` so it maybe that we can access this directory in david's home folder

<img src="https://imgur.com/58AzzFh.png"/>

We can't extract the file here as it's going to give us permission denied error on creating files and folders here

<img src="https://imgur.com/BXvxfN6.png"/>

So I transferred it on my machine using `netcat`

<img src="https://imgur.com/z9qZ6DM.png"/>

<img src="https://imgur.com/ewQxkXb.png"/>

<img src="https://imgur.com/AsrG7BI.png"/>

But that `id_rsa` key is password protected so we may need to crack the passowrd so we are going to use `ssh2john` to get the hash and then crack it using `john`

<img src="https://i.imgur.com/AD3yt7J.png"/>

<img src="https://i.imgur.com/3VC7WlW.png"/>

And we got the passphrase , let's try logging in using id_rsa key

<img src="https://imgur.com/r6nzc3C.png"/>

Now we can see script `server-stats.sh`

<img src="https://imgur.com/TzVqami.png"/>

```bash
#!/bin/bash

cat /home/david/bin/server-stats.head
echo "Load: `/usr/bin/uptime`"
echo " "
echo "Open nhttpd sockets: `/usr/bin/ss -H sport = 80 | /usr/bin/wc -l`"
echo "Files in the docroot: `/usr/bin/find /var/nostromo/htdocs/ | /usr/bin/wc -l`"
echo " "
echo "Last 5 journal log lines:"
/usr/bin/sudo /usr/bin/journalctl -n5 -unostromo.service | /usr/bin/cat 
```

Here we can run this command
`/usr/bin/sudo /usr/bin/journalctl -n5 -unostromo.service | /usr/bin/cat `

<img src="https://imgur.com/XLDd7zj.png"/>

We could try to run `less` instead of `cat` so  that we can get root shell with `!/bin/bash` but it wasn't working

<img src="https://imgur.com/IV8IqR0.png"/>

<img src="https://imgur.com/E4H9k3p.png"/>

<img src="https://imgur.com/OoNgVRg.png"/>

So I shrinked my terminal screen and removed the pipe command , when we'll run this `usr/bin/sudo /usr/bin/journalctl -n5 -unostromo.service` it will automatically pipe it to `less` and then we can run `!/bin/bash`

<img src="https://imgur.com/fpqC3Sp.png"/>

<img src="https://imgur.com/SfCmBqW.png"/>

This was the reason we could run  that command as sudo as it was in sudoers entry

<img src="https://imgur.com/EMDrTsN.png"/>

hunter