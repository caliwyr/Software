# TryHackMe-GoldenEye

## NMAP

```
Nmap scan report for 10.10.81.165
Host is up (0.15s latency).
Not shown: 65531 closed ports
PORT      STATE SERVICE     VERSION
25/tcp    open  smtp        Postfix smtpd
|_smtp-commands: ubuntu, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, 
80/tcp    open  http        Apache httpd 2.4.7 ((Ubuntu))
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: GoldenEye Primary Admin Server
55006/tcp open  ssl/unknown
|_ssl-date: TLS randomness does not represent time
55007/tcp open  pop3        Dovecot pop3d
|_pop3-capabilities: AUTH-RESP-CODE TOP CAPA PIPELINING USER UIDL RESP-CODES SASL(PLAIN) STLS
|_ssl-date: TLS randomness does not represent time

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 502.67 seconds
```

## PORT 80

<img src="https://imgur.com/9ZADdWL.png"/>

Looking at source code

<img src="https://imgur.com/ozjQtjy.png"/>

This is an encoded text on visting `cyberchef` and decoding it using `magic` we decoded the text

<img src="https://imgur.com/KLXO8MS.png"/>

`InvincibleHack3` is the password for `boris`

But these creds are not right 

<img src="https://imgur.com/2jjeAvg.png"/>

So let's enumerate different ports

## PORT 55007 (POP3)

I tired to brute force with `boris` but failed

<img src="https://imgur.com/3tYu6IL.png"/>

Earlier from the source code of the web page we saw a message that  "Natalya could break your code" so maybe that's a potential username that we need to brute force so again using hydra 

<img src="https://imgur.com/gZxYV4u.png"/>

After some time I was able to get the correct password

<img src="https://imgur.com/W1GunwN.png"/>

Also got boris's password with the `fasttrack` wordlist

<img src="https://imgur.com/hBNWUV9.png"/>

<img src="https://imgur.com/wd4IMFy.png"/>


## Boris's Mail

Here we used telnet to connect to pop3 service and logged in with boris's credentials. We can see that there are 3 messages

### Message 1
<img src="https://imgur.com/tpXPrl8.png"/>
### Message 2
<img src="https://imgur.com/ODm8rMe.png"/>
### Message 3
<img src="https://imgur.com/dlI6fqR.png"/>

## Natalya's mail
We do the same with natalya's mail

### Message 1
<img src="https://imgur.com/LJd7WdT.png"/>

### Message 2
<img src="https://imgur.com/JGW87vt.png"/>

So we found the creds and a domain , lets add the domain in `/etc/hosts` file

<img src="https://imgur.com/BLQ37fT.png"/>

Navigate to `severnaya-station.com/gnocertdir` and login with xenia's credentials

<img src="https://imgur.com/UwfmUwn.png"/>

Going to user's messages we can find a conversation with a user `doak`

<img src="https://imgur.com/a9yNvRj.png"/>

We find doak's password with the same procedure 

<img src="https://imgur.com/qv2NcOI.png"/>

## Doak's Mail

<img src="https://imgur.com/eBtTiRM.png"/>

### Message
<img src="https://imgur.com/7tVw1gU.png"/>

Login as dr_doak on the website

<img src="https://imgur.com/q3n6qpr.png"/>

<img src="https://imgur.com/raDYBrK.png"/>

This is the message we get from that text file

```
007,

I was able to capture this apps adm1n cr3ds through clear txt. 

Text throughout most web apps within the GoldenEye servers are scanned, so I cannot add the cr3dentials here. 

Something juicy is located here: /dir007key/for-007.jpg

Also as you may know, the RCP-90 is vastly superior to any other weapon and License to Kill is the only way to play.
```

<img src="https://imgur.com/e7Sk885.png"/>

Running `exiftool` on it we can find a base64 encoded text

<img src="https://imgur.com/JMPkHns.png"/>

<img src="https://imgur.com/u2ddmjV.png"/>

<img src="https://imgur.com/0wwRyhO.png"/>

Now we are logged in as admin. One thing we can do now is look for any exploits for `Moodle` 

## Getting a reverse shell

<img src="https://imgur.com/rsMwc1D.png"/>

<img src="https://imgur.com/2s63CZJ.png"/>

<img src="https://imgur.com/h4t02OV.png"/>

For some reason the exploit wasn't working . I double checked everything but still it was failing
<img src="https://imgur.com/qRKdfU5.png"/>

So I went with the manual exploitation of moodle

<img src="https://imgur.com/ZxaYJnc.png"/>

Under settings go to plugins ->Text Editors -> TinyMCE HTML editor and make sure to select Spell Engine as `PSpellShell`

Then make a blog post entry and click on spell check icon , if you have setup your netcat listener you'll get a shell frorm the target machine

<img src="https://imgur.com/cprnqAb.png"/>

<img src="https://imgur.com/oARTDqh.png"/>

<img src="https://imgur.com/Y7RFLxK.png"/>

Looking for kernel version 

<img src="https://imgur.com/ZKSNs9y.png"/>

This is a really old kernel for linux so hopeully there will be an exploit on `exploit-db`

<img src="https://imgur.com/KAblTn8.png"/>

Download ,compile and transfer it to target machine

<img src="https://imgur.com/Xgf57Nz.png"/>

But on running it gave an error because gcc was not installed on the machine

<img src="https://imgur.com/IhOZTLh.png"/>

On googling I found cc which is alternate to gcc and it was on the box

<img src="https://imgur.com/XcQbpka.png"/>

<img src="https://imgur.com/Vtw1Dx7.png"/>

So we had to edit the exploit by replacing `gcc` to `cc` and then again transfer the compiled source code to the box

<img src="https://imgur.com/dkF08W1.png"/>

We got root !!
