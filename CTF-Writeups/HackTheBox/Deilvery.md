# HackTheBox-Delivery

## NMAP

```
PORT     STATE SERVICE VERSION                                            
22/tcp   open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey:
|   2048 9c:40:fa:85:9b:01:ac:ac:0e:bc:0c:19:51:8a:ee:27 (RSA)
|   256 5a:0c:c0:3b:9b:76:55:2e:6e:c4:f4:b9:5d:76:17:09 (ECDSA)
|_  256 b7:9d:f7:48:9d:a2:f2:76:30:fd:42:d3:35:3a:80:8c (ED25519)               
80/tcp   open  http    nginx 1.14.2                                       
|_http-server-header: nginx/1.14.2                                        
|_http-title: Welcome
8065/tcp open  unknown               
| fingerprint-strings:
|   GenericLines, Help, RTSPRequest, SSLSessionReq, TerminalServerCookie:
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest:
|     HTTP/1.0 200 OK
|     Accept-Ranges: bytes
|     Cache-Control: no-cache, max-age=31556926, public                   
|     Content-Length: 3108           
|     Content-Security-Policy: frame-ancestors 'self'; script-src 'self' cdn.rudderlabs.com                                                         
|     Content-Type: text/html; charset=utf-8                              
|     Last-Modified: Tue, 02 Mar 2021 21:12:13 GMT                        
|     X-Frame-Options: SAMEORIGIN                                         
|     X-Request-Id: dd9rh44dg3bsjmikyoawb6qabe                            
|     X-Version-Id: 5.30.0.5.30.1.57fb31b889bf81d99d8af8176d4bbaaa.false
|     Date: Tue, 02 Mar 2021 21:49:09 GMT                                 
|     <!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,u
ser-scalable=0"><meta name="robots" content="noindex, nofollow"><meta name="referrer" content="no-referrer"><title>Mattermost</title><meta name="mob
ile-web-app-capable" content="yes"><meta name="application-name" content="Mattermost"><meta name="format-detection" content="telephone=no"><link re
|   HTTPOptions:                     
|     HTTP/1.0 405 Method Not Allowed                                     
|     Date: Tue, 02 Mar 2021 21:49:09 GMT                                 
|_    Content-Length: 0              
```

## PORT 80 (HTTP)

<img src="https://imgur.com/fHTpeNT.png"/>

<img src="https://imgur.com/wQ0daUS.png"/>

It looks like we need to add `delivery.htb` to `/etc/hosts`

We can also see that `Helpdesk` would lead us to a sub domain `help.delivery.htb` so we should add this to `/etc/hosts`

<img src="https://imgur.com/mCUpmVk.png"/>

## PORT 8065 (HTTP)
On adding the domain in /etc/hosts

###  help.delievery.htb
<img src="https://imgur.com/iTvtqAk.png"/>

On selecting `Open a new ticket`

<img src="https://imgur.com/c9kJKxQ.png"/>

<img src="https://imgur.com/cW2yG76.png"/>

<img src="https://imgur.com/9iyKF9S.png"/>

After creating a ticket we will get a token number and a mail which we will use to register on `Mattermost` which is on `delivery.htb`

On logging in with the registered email 

<img src="https://imgur.com/xHcF2Xl.png"/>

### delievery.htb

Visit this domain and register with the `token_number@delivery.htb` which will then send you the email verification link

<img src="https://imgur.com/9batnYw.png"/>

<img src="https://imgur.com/8BVe05D.png"/>

<img src="https://imgur.com/sHvZQcj.png"/>

We will get these credentials `maildeliverer:Youve_G0t_Mail!`

Also this message

```
Also please create a program to help us stop re-using the same passwords everywhere.... Especially those that are a variant of "PleaseSubscribe!"

PleaseSubscribe! may not be in RockYou but if any hacker manages to get our hashes, they can use hashcat rules to easily crack all variations of common words or phrases.
```

Login here with the credentials

<img src="https://imgur.com/x12MwEK.png"/>

<img src="https://imgur.com/Ey24ZgQ.png"/>

But there was not nothing on `ostickets` so I tried these credentials by logging in with ssh

<img src="https://imgur.com/VZPRUvb.png"/>

Going into `/opt` directory I found a folder named `mattermost`.

<img src="https://imgur.com/CwnWK5p.png"/>

Again we see an interesting folder named `config`

<img src="https://imgur.com/xIDt2OI.png"/>

<img src="https://imgur.com/lZYmO10.png"/>

And we can see credentials for the mysql database

<img src="https://imgur.com/XcxUGpg.png"/>

Mysql is running on port 3306 which is the defualt one so let's try logging in with the credentials we found

<img src="https://imgur.com/KQz76Xl.png"/>

<img src="https://imgur.com/iGP1GUu.png"/>

<img src="https://imgur.com/pKb75u5.png"/>

At the end we see a table named `Users`

<img src="https://imgur.com/6QFgFW2.png"/>

<img src="https://imgur.com/arpmz8y.png"/>

We will get the information for `root` user including the password hash

<img src="https://imgur.com/ZUy2suD.png"/>

Visiting `Name That Hash` website we can see that this is `bcrypt` hash

<img src="https://imgur.com/TcmEI51.png"/>

Save the hash in a text file

<img src="https://imgur.com/ZatfO74.png"/>

Now remeber the message that we saw from Mattermost chat that we need to use hashcat rules for the variation of  `PleaseSubscribe!`

For creating hashcat rules I visited this page

https://hackingvision.com/2020/03/27/hashcat-rule-based-attack/

Here it talks about `Hob0Rules`

<img src="https://imgur.com/ZQSePJb.png"/>

<img src="https://imgur.com/tnZlvuz.png"/>

So let's run hashcat with the bcrypt hash against the password and the rule

<img src="https://imgur.com/rjkeFVV.png"/>

It took a lot of time to crack the hash as I don't have a good GPU

<img src="https://imgur.com/GcDFMWG.png"/>

The hash has been cracked so let's try logging in with `root` user and see if this is password for root user on the box 

<img src="https://imgur.com/iBerWLf.png"/>
