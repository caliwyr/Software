# TryHackMe-Wonderland

## NMAP

```
Nmap scan report for 10.10.84.199
Host is up (0.16s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8e:ee:fb:96:ce:ad:70:dd:05:a9:3b:0d:b0:71:b8:63 (RSA)
|   256 7a:92:79:44:16:4f:20:43:50:a9:a8:47:e2:c2:be:84 (ECDSA)
|_  256 00:0b:80:44:e6:3d:4b:69:47:92:2c:55:14:7e:2a:c9 (ED25519)
80/tcp open  http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Follow the white rabbit.
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## PORT 80

<img src="https://imgur.com/ecXhvhD.png"/>

Okay so I didn't find anything through looking at the source and at the web page so we have to use directory brute force using `gobuster`

## Directory Brute Force

```
gobuster dir -u http://10.10.84.199/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```
<img src="https://imgur.com/Wo7jhQP.png"/>


<img src="https://imgur.com/ocd45aA.png"/>

Didn't find on the `poem` page either but that `/r` page is interesting

<img src="https://imgur.com/U04F7h7.png"/>


So it's telling us to keep going , and as we remeber from the first page we saw there was heading `Follow the Rabbit` so let's give it a shot by actually typing rabbit with each letter as a sperate page.

<img src="https://imgur.com/drsqOpE.png"/>


<img src="https://imgur.com/l1igweh.png"/>

Now by looking at the source we can find a username and password

<img src="https://imgur.com/H0oUFEU.png"/>

So the only two services that are ruuning are http and ssh , there isn't any login page we found so this may be the credentials for ssh

`alice:HowDothTheLittleCrocodileImproveHisShiningTail`

<img src="https://imgur.com/oLbjSEF.png"/>

And we are logged in awesome!

I couldn't find anything expect for walrus something .py which has list of poems in it , I'll get back to it but first let's transfer `linpeas` so we can automate our enumartion and it does for it 

<img src="https://imgur.com/0K9GB8b.png"/>

So throguh linpeas I found that perl has capabilites meaning that it could run as root with any user like having a SUID but only problem is that only user `root` and `hatter` can execute it

<img src="https://imgur.com/sa1b9k3.png"/>

But now we know what we would need to get root but as for now in order to get to `rabbit` user we have to use `/home/alice/walrus_and_the_carpenter.py` and do something in it 

Now this python file is using `random.py` so what we can do is a create a file with the name of `random.py` having this in it

<img src="https://imgur.com/kZkamNK.png"/>


<img src="https://imgur.com/IhNjWPM.png"/>

<img src="https://imgur.com/ypMqfXR.png"/>

In `rabbit`'s directory we see a `teaparty` binary

When running it 

<img src="https://imgur.com/mlS6cvm.png"/>

It will give us an error so we have to transfer it to our local machine and analyze it maybe with `ghidra`

<img src="https://imgur.com/h2OEaZB.png"/>

<img src="https://imgur.com/8vj2m6k.png"/>

By analyzing it we can see that whole thing is statically printed but we see something intersting about two functions

```
setuid(0x3eb);
setgid(0x3eb);

```

Set User ID and Set Group ID functions which is taking `0x3eb` as parameter which is in hex and we convert this into decimal it will be `1003` which is the uid and gid of user `hatter`


We can also see that it's using `date` command which is a binary so what we can do is create `date` binary 

```
#!/bin/bash
/bin/bash
```
give it permission to execute and then add path to this in $PATH variable

<img src="https://imgur.com/2K79ntX.png"/>

We find a passowrd in `hatter`'s home directory 

<img src="https://imgur.com/eVh2imX.png"/>


<img src="https://imgur.com/AcF6oVX.png"/>

We can now execute perl as we were not able to execute it as we were not in `hatter`'s group

Now as I already figured the way to get root so 

## Privilege Escalation

<img src="https://imgur.com/BwZ6K03.png"/>

<img src="https://imgur.com/2IZ7ofG.png"/>

Now that we are root we can grab the user and root flag !!!