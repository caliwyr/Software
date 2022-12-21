# TryHackMe-Fortress

## NMAP

```bash
PORT     STATE SERVICE REASON         VERSION                                            
22/tcp   open  ssh     syn-ack ttl 63 OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)                                                 
| ssh-hostkey:   
|   2048 9f:d0:bb:c7:e2:ee:7f:91:fe:c2:6a:a6:bb:b2:e1:91 (RSA)                  
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCXx2nOQ7SVuA1liJqX+ZR2KK9Oipy+1cd4ZZ3iD+/xuAkvon338WPfjcGmNaBd0McHqunhvl1xJZZMsOsjVuMUSD0GUX3YF6BQ/RdVxQ00/g
RvVW70nUk+kf+Umz/5HbI9IfBLoIcRGWxf3naUdl8Vfs7Fj38fnZB0A+8av3/VAthEhiOq58o9ssQJ7DD6ZJydt4R1G9WYa2C+8O76/rJ9EadLCaNAeKKUYmuGEdJit+vGsd4ggzYc0qJQ2QmRUr
VK+FeIFZDIo4InaPIiI1VF0X+ooax1siytlF85f5956EfDsGgzNBZb/9I5tGz4QFnM/FH65fXEnvUrDoXO2+dj                                                              
|   256 06:4b:fe:c0:6e:e4:f4:7e:e1:db:1c:e7:79:9d:2b:1d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPBJBTN55zS77xduARAxZeA+xhJt04e3yVZpkmTObu2JMOjxTzFoK4mftWUdLsx1bs1mDIWWXL
OKjXcnq3PcO84=
|   256 0d:0e:ce:57:00:1a:e2:8d:d2:1b:2e:6d:92:3e:65:c4 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJezjvXtsHInz+XQ4hYfNBX5kjinTpiKRYaK5rF1og71
5581/tcp open  ftp     syn-ack ttl 63 vsftpd 3.0.3                  
| ftp-anon: Anonymous FTP login allowed (FTP code 230)               
|_-rw-r--r--    1 ftp      ftp           305 Jul 25 20:06 marked.txt
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
5752/tcp open  unknown syn-ack ttl 63 
5752/tcp open  unknown syn-ack ttl 63 
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, LANDesk-RC, LPDString, RTSPRequest, S
IPOptions, X11Probe: 
|     Chapter 1: A Call for help
|     Username: Password:
|   Kerberos, LDAPBindReq, LDAPSearchReq, NCP, NULL, RPCCheck, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie: 
|     Chapter 1: A Call for help
|_    Username:
7331/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
```

We can see port 5581 which is ftp and `anonymous` login is enabled so we can login as anonymous user , on port 7331 , apache server is running and on 5752 seems like some response so we'll get too it also we are told to add these two domain names `fortress`, `temple.fortress` from the room description , we can add those to `/etc/hosts` file

<img src="https://i.imgur.com/BkDNXW2.png"/>



## PORT 5581 (FTP)

<imgs src="https://i.imgur.com/OolddL3.png"/>

If we do `ls -la` we'll see a hidden file called `.file`

<img src="https://i.imgur.com/sd4wfJE.png"/>

So we can download these files using `get`

<img src="https://i.imgur.com/eDDDbHp.png"/>

We don't find much information from `marked.txt` other than telling us the username `veekay`

<img src="https://i.imgur.com/O4S4MuE.png"/>

And the other file is python 2.7 compiled byte-file  
<img src="https://i.imgur.com/aXz6WpN.png"/>

<img src="https://i.imgur.com/lK8LT5M.png"/>

We decompile this file to human readable file using `uncompyle2` , we can git clone it's repoistory and install the binary using `python setup.py install`

<img src="https://i.imgur.com/p8uYVUr.png"/>

<img src="https://i.imgur.com/rSahd4u.png"/>

<img src="https://i.imgur.com/esBX5l8.png"/>

Here we see username and password which are hard coded converted from string to `byte_to_long` format , so let's try to convert a random string to see a long byte format also we can convert it back to a byte string using `long_to_bytes`

```python3
                                  
from Crypto.Util.number import bytes_to_long,long_to_bytes

test = bytes("abcbbc","utf-8") # can be written as b"abcbbc" as well
long_test = bytes_to_long(test)
print (long_test)
print (long_to_bytes(long_test))
```

<img src="https://i.imgur.com/Z0OJMLy.png"/>

But we don't get `L` at the end of long byte string , let's try removing it from username and password variables and try to convert it back to byte string format

<img src="https://i.imgur.com/MlAVWhV.png"/>

These are aleady in long byte format so we just need to use `long_to_bytes` 

<img src="https://i.imgur.com/w5yG3BT.png"/>

So we got the username and password in a string format but the question is where do we send these credentials ? I tried making a http request on port  5752 but connection timed out so it must be running on some other protocol

## PORT  5752 (Telnet)

Eventually I figuired out it was telnet by trying connecting to it 

<img src="https://i.imgur.com/nLnwKAY.png"/>

We get this text `t3mple_0f_y0ur_51n5` which is from that `secrets.txt` because it was calling the function which would return the contents of that file on providing correct credentials

## PORT 7331 (HTTP)

<img src="https://i.imgur.com/TxoKTRs.png"/>

On the apache web server we only get the default web page , I tried running `gobuster` with `big.txt` , `common.txt` but came up with nothing , so then tried look for the page we got from secrets.txt but it didn't loaded until I added a php extension to it

<img src="https://i.imgur.com/APbm1IM.png"/>

Again we don't see much on this page but after viewing the source code through ctrl+u

<img src="https://i.imgur.com/bRmIq5d.png"/>

The reason why we are seeing html code is becuase browser executes php code but renders html code that's why we can html tags here , also going to css file we can get a "hint"

<img src="https://i.imgur.com/NqNp3Ds.png"/>

This looks like base64 encoded text which on decoding we get  this

<img src="https://i.imgur.com/JrlCpIP.png"/>

It's talking about "colliding" something maybe a secret or a hash ? Judging from that html commented code we saw , let's try changing the extension to `.html`

<img src="https://i.imgur.com/aQmQeyw.png"/>

And we got a different page with input fields also viewing the html source code

<img src="https://i.imgur.com/zvnE1Yb.png"/>

We can see some php code here

<img src="https://i.imgur.com/jeT5hip.png"/>

What it's doing is that , taking two GET parameters `user` and `pass`  doing a type check also checking it's SHA-1 hash if they are similar which is what we call hash collision and back in 2017 someone discovered a collision in SHA-1 by calculating the hash of two pdf files 

<img src="https://i.imgur.com/bFlnIwt.png"/>

So what if we make a python script that will fetch those files content in variables and then we will make a GET request to `t3mple_0f_y0ur_51n5.php` with those parameters

```python
import requests

# Fetching 2 pdf's file which cause SHA-1 collision

pdf1 = requests.get("https://shattered.it/static/shattered-1.pdf")
pdf2 = requests.get("https://shattered.it/static/shattered-2.pdf")

# Assinging pdf's content into the GET parameters

params = {'user': pdf1.content, 'pass': pdf2.content}

r = requests.get("http://temple.fortress:7331/t3mple_0f_y0ur_51n5.php/",params=params)
print (r.text)
```

But this didn't worked as pdf file's "length exceeds the capacity"


<img src="https://i.imgur.com/imj2JZN.png"/>

Maximum capacity of url request is 8 KB while we exceed this limit as combined size of those files is 825 KB

<img src="https://i.imgur.com/Cl6GefY.png"/>

<img src="https://i.imgur.com/BwWfM5P.png"/>

I found the way around through a writeup from a 2017 CTF challenge which was based on the same concept of SHA-1 hash collision

<img src="https://i.imgur.com/2aumQuk.png"/>

<img src="https://i.imgur.com/tNbv2PQ.png"/>

We have a total of 1.6 KB and if we check SHA1 hash of both these files

<img src="https://i.imgur.com/7OoX5VR.png"/>

They are similar , so here I am just going to host them on my own machine and fetch it 

```python
import requests

# Fetching 2 pdf's file which cause SHA-1 collision

pdf1 = requests.get("http://localhost/1-pdf.192")
pdf2 = requests.get("http://localhost/2-pdf.192")

# Assinging pdf's content into the GET parameters

params = {'user': pdf1.content, 'pass': pdf2.content}

r = requests.get("http://temple.fortress:7331/t3mple_0f_y0ur_51n5.php/",params=params) 
print (r.text) 

```

Although we have succeded in making the request smaller but the contents are identical so we according the writeup we need to put first 320 bytes of the pdf file 

<img src="https://i.imgur.com/IHQ05sQ.png"/>

<img src="https://i.imgur.com/eNdxJOR.png"/>

This makes a total of 640 bytes , also checking the SHA1 hashes

<img src="https://i.imgur.com/Qv1WEVT.png"/>

These two files look different but fingers crossed

<img src="https://i.imgur.com/Giz3vX7.png"/>

```python3
import requests

# Fetching 2 pdf's file which cause SHA-1 collision

pdf1 = requests.get("http://localhost/shattered-1.dat")
pdf2 = requests.get("http://localhost/shattered-2.dat")

# Assinging pdf's content into the GET parameters

params = {'user': pdf1.content, 'pass': pdf2.content}

r = requests.get("http://temple.fortress:7331/t3mple_0f_y0ur_51n5.php/",params=params)
print (r.text)

```

But this didn't work 

<img src="https://i.imgur.com/HThB8GP.png"/>

<img src="https://i.imgur.com/WveWrCR.png"/>

This is the reason why it didn't worked as both values are having a length of 320 and there's a condition that `user` must have a length greater than 600 and `pass` must have a lenght greater than 500 

I found two other files whose SHA1 hashes collide

<img src="https://i.imgur.com/Szant4g.png"/>

<img src="https://i.imgur.com/tcqhknY.png"/>

Here we can see both are of 640 bytes which passes the condition and total size is 1.2KB so this request can be allowed 

<img src="https://i.imgur.com/HsktjTR.png"/>

We get a hidden file `m0td_f0r_j4x0n.txt` , so this must be a username `j4x0n`, on visting that file we'll get the private key

<img src="https://i.imgur.com/6NEYxay.png"/>

But the message here was kinda vauge as it stated that "I am leaving a private key for you j4x0n" which was written by `h4rdy`

<img src="https://i.imgur.com/DuFpBx8.png"/>

So this key was for h4rdy, if we try to do `sudo -l` it won't work it seems that we are in restricted bash

<img src="https://i.imgur.com/KnqFu6b.png"/>

If we try to change PATH variable it won't allow as it's set to read only

<img src="https://i.imgur.com/n21BvOP.png"/>

I tried doing autocomplete to see if I can see any files or directories

<img src="https://i.imgur.com/Grs6E5K.png"/>

But if we try to login using `-t` which enables  "pseudo-tty allocation"

<img src="https://i.imgur.com/y7Yku3B.png"/>

We can run `cd` and `export` commands so let's set the `SHELL` variable to `/bin/bash` and also change the `PATH` variable

<img src="https://i.imgur.com/SQPma5p.png"/>

## Privilege Escalation (ja4xon)

We can now run commands, so now doing `sudo -l` we can see that this user is allowed to run `cat` as `j4x0n` user

<img src="https://i.imgur.com/oIjHXu3.png"/>

We can read these two files

<img src="https://i.imgur.com/3hKNzfe.png"/>

<img src="https://i.imgur.com/am1nAvc.png"/>

Let's just copy the id_rsa key (private key) and login as `j4x0n`

<img src="https://i.imgur.com/EwpsqXE.png"/>

But still we can't use `sudo -l` as we don't know the password

<img src="https://i.imgur.com/t98mPcK.png"/>

So we need to maybe find this user's password as he is in sudoers group

<img src="https://i.imgur.com/KFhVU4Q.png"/>

In `/opt` directoy we see a SUID binary named `bt` on running tells that it's spawning a root shell but instead keeps printing buch of gibberish on the terminal and force us to exit out of ssh connection , I didn't find anything , manully tried looking into directories , checking local ports and cron jobs but we were in `adm` group which can read log files so I though of visiting `/var/logs/auth.log`

<img src="https://i.imgur.com/Yec5kEA.png"/>

Let's give this password a try 

<img src="https://i.imgur.com/3cHIIqx.png"/>

With this we rooted this room.


## References

- https://reverseengineering.stackexchange.com/questions/1701/decompiling-pyc-files
- https://github.com/Mysterie/uncompyle2
- https://stackoverflow.com/questions/3475648/sha1-collision-demo-example
- https://github.com/fabacab/CTF/tree/master/2017/BKP/cloud/Prudentialv2
- https://sha-mbles.github.io/