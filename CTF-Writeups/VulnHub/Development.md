# Vulnhub-Development

## NMAP

```bash

nmap -sC -sV 192.168.1.6
Starting Nmap 7.80 ( https://nmap.org ) at 2021-05-15 11:28 PKT
Nmap scan report for 192.168.1.6                                     
Host is up (0.041s latency).                                      
Not shown: 995 closed ports                                
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:   
|   2048 79:07:2b:2c:2c:4e:14:0a:e7:b3:63:46:c6:b3:ad:16 (RSA)
|_  256 24:6b:85:e3:ab:90:5c:ec:d5:83:49:54:cd:98:31:95 (ED25519)
113/tcp  open  ident?                                             
|_auth-owners: oident           
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
|_auth-owners: root
445/tcp  open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
|_auth-owners: root
8080/tcp open  http-proxy  IIS 6.0


```

## PORT 139/445 (SMB)

<img src="https://imgur.com/QGiWLSN.png"/>

We can see a share named `access`, let's see if we can access this as an anonymous user

<img src="https://imgur.com/JThIRQL.png"/>

Access is denied so , I ran `eum4-linux-ng` and it found some users on the machine

<img src="https://i.imgur.com/Y0s6ZpJ.png"/>

## PORT 8080

<img src="https://imgur.com/GfvCKuC.png"/>

On port we see an html giving us a hint to look at `html_pages`

<img src="https://imgur.com/EhABigN.png"/>

Here we can see a number of pages so let's go through each of these pages one by one

### About.html

<img src="https://imgur.com/7BpFNXo.png"/>

This page tells that they are creating pofile for `David`

### Config.html

<img src="https://imgur.com/snsVpyw.png"/>

This page has nothing

### Default.html

<img src="https://imgur.com/S275gcL.png"/>

This page has something in binary so let's convert and see what it is , I have a feeling it's a rabbit hole : \

<img src="https://imgur.com/ir9fZun.png"/>

Huh ?

### Development.html

<img src="https://i.imgur.com/9HxXrn9.png"/>

This page is interesting it says there's a page `hackersecretpage` which contains a link to upload files so let's where that is

<img src="https://imgur.com/KheOWnU.png"/>

And again this has nothing but looking at `development.html` source code there's a comment

<img src="https://i.imgur.com/bFcAMx7.png"/>

### DevelopmentSecretPage

<img src="https://imgur.com/Gd3DAP4.png"/>

On clicking the link we can get a page where it says to logout

<img src="https://i.imgur.com/wmrJaNI.png"/>

<img src="https://i.imgur.com/E2aPKWx.png"/>

Here I tried logging in with random credentials

<img src="https://i.imgur.com/pohNpAB.png"/>

I got this error , and it mentioned about a file called `slogin_lib.inc.php` , I searched for the file name on google and it straight away told that there's an exploit for it 

<img src="https://i.imgur.com/Pi8wwG6.png"/>

<img src="https://imgur.com/MEwqXPr.png"/>

Let's try the RFI exploit

<img src="https://i.imgur.com/60miBz7.png"/>

I hosted a file on my machine to see if we can view it from there or not

<img src="https://i.imgur.com/X0NPGr3.png"/>

<img src="https://imgur.com/I5PaZEi.png"/>

It doesn't look it worked so let's try the Sensitive Infomration disclosure

<img src="https://i.imgur.com/E4I2GEl.png"/>

<img src="https://i.imgur.com/VAUTk48.png"/>

We got some hashses let's try to crack them with `crackstation`

<img src="https://i.imgur.com/Mzy9WxU.png"/>

Let's try to ssh into the machine

<img src="https://imgur.com/N9eZ45C.png"/>

We are in but something looks odd , it says type `?` for help

<img src="https://i.imgur.com/Brvyw9i.png"/>

If we type commands other than these it wil show error

<img src="https://i.imgur.com/LXSkB6z.png"/>

So this looks like we are in restricted shell but I came across an error when I typed `id`

<img src="https://i.imgur.com/dGpIpTa.png"/>

It seems `lshell.py` is being used so let's do a quick google search on that

<img src="https://imgur.com/vcuktpS.png"/>

This is a python script which restrict some commands to be executed on the shell we can forbid or allow any commands we want

<img src="https://imgur.com/iSQrwss.png"/>

So that's what was happeing , let's search if there are any bypasses related to lshell

https://www.aldeid.com/wiki/Lshell

<img src="https://imgur.com/iSQrwss.png"/>

Bingo , we can by pass this easily ,let's give this is a try

<img src="https://imgur.com/UoKuVbs.png"/>

Reading `work.txt`

```
1.Tell Patrick that shoutbox is not working. We need to revert to the old method to update David about shoutbox. For new, we will use the old director's landing page.

2.Patrick's start of the third year in this company!

3.Attend the meeting to discuss if password policy should be relooked at.

```

This isn't really helpful , so going back to patrick hash I tried to crack it one more time by going to online site 

<img src="https://imgur.com/3Vi54Aa.png"/>

<img src="https://i.imgur.com/ehs8UXP.png"/>

So we have switched to patrick and can see we can escalate to root either using `vim` or `nano` , let's visit GTFOBINS to escalate our shell

### Using Vim

<img src="https://imgur.com/n48vEzl.png"/>

### Using Nano
Launch nano as sudo `sudo /bin/nano` , then press `alt+R` 

<img src="https://imgur.com/B3z94Re.png"/>

Then `alt+X`

<img src="https://imgur.com/SMCS45i.png"/>

You'll get the screen to execute commands

<img src="https://imgur.com/DXLmX0k.png"/>

<img src="https://imgur.com/ipaPvBg.png"/>

You got root !!!

## Unintended way to root 

Recently Ubuntu OverlayFS Local Privesc exploit was found 

https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3493

So I used that exploit to get root by getting the PoC

https://github.com/briskets/CVE-2021-3493/blob/main/exploit.c

<img src="https://i.imgur.com/aVtppnA.png"/>
