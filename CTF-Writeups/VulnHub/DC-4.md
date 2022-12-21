# Vulnhub- DC 4

## Rustscan

```bash

 rustscan -a 192.168.1.3 -- -A -sC -sV                                                                                           
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.         
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |                  
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |                  
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'                                                                                            
Open 192.168.1.3:22                                                       
Open 192.168.1.3:80               


PORT   STATE SERVICE REASON         VERSION                                                                                                         
22/tcp open  ssh     syn-ack ttl 64 OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)                                                                   
| ssh-hostkey:       
|   2048 8d:60:57:06:6c:27:e0:2f:76:2c:e6:42:c0:01:ba:25 (RSA)      
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCp6/VowbK8MWfMDQsxHRV2yvL8ZO+FEkyIBPnDwTVKkJiVKaJMZ5ztAwTnkc30c3tvC/yCqDAJ5IbHzgvR3kHKS37d17K+/OLxalDutFjrWj
G7mBxhMW/0gnrCqJokZBDXDuvHQonajsfSN6FmWoP0PDsfL8NQXwWIoMvTRYHtiEQqczV5CYZZtMKuOyiLCiWINUqKMwY+PTb0M9RzSGYSJvN8sZZnvIw/xU7xBCmaWuq8h2dIfsxy+FhrwZMhvh
JOpBYtwZB+hos3bbV5FKHhVztxEo+Y2vyKTl6MXJ4qwCChJdaBAip/aUt1zDoF3cIb+yebteyDk8KIqmp5Ju4r                                                              
|   256 e7:83:8c:d7:bb:84:f3:2e:e8:a2:5f:79:6f:8e:19:30 (ECDSA)   
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIbZ4PXPXShXCcbe25IY3SYbzB4hxP4K2BliUGtuYSABZosGlLlL1Pi214yCLs3ORpGxsRIHv8
R0KFQX+5SNSog=                                                            
|   256 fd:39:47:8a:5e:58:33:99:73:73:9e:22:7f:90:4f:4b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDcvQZ2DbLqSSOzIbIXhyrDJ15duVKd9TEtxfX35ubsM
80/tcp open  http    syn-ack ttl 64 nginx 1.15.10                         
| http-methods:                                                           
|_  Supported Methods: GET HEAD POST                                      
|_http-server-header: nginx/1.15.10                                       
|_http-title: System Tools                                                
MAC Address: 08:00:27:2A:E7:75 (Oracle VirtualBox virtual NIC)                                         

```

## PORT 80 (HTTP)

<img src="https://imgur.com/HXr2W1d.png"/>

It looks like login page , so let's default credentials like admin:admin and it didn't work, I intercepted the request with burp 

<img src="https://imgur.com/7lmfYCp.png"/>

Saved it in a file and ran `sqlmap` against it 

<img src="https://imgur.com/fvxMYTw.png"/>

<img src="https://imgur.com/HzOsVXD.png"/>

That didn't work as well so we know that this is admin's login and we can brute force his password so using burp , we can use hydra to brute force admin's password

<img src="https://imgur.com/nFQXbk7.png"/>

But if there isn't any erorr messages so we need to use somthing that will show the message after being logged in typically logout is shown when you login to a portal or a site

So the hydra command will look like this

```bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.168.1.3 http-post-form '/login.php:username=^USE
R^&password=^PASS^:S=logout' -t 64 -V -I
```

<img src="https://imgur.com/YagTBwa.png"/>

<img src="https://imgur.com/CE0VU20.png"/>

We can only three options 

<img src="https://imgur.com/Pen7hzZ.png"/>

So let's intercept it with burp

<img src="https://imgur.com/jOXUktz.png"/>

On chaing the `raido` parameter's value

<img src="https://imgur.com/3dV2gFI.png"/>

<img src="https://imgur.com/LcyapjC.png"/>

Python exists on the machine so we can get a reverse shell

<img src="https://imgur.com/x7ueTvL.png"/>

<img src="https://imgur.com/rDqZU3U.png"/>

Here only `jim` folder looks interesting

<img src="https://imgur.com/mXdGcfT.png"/>

<img src="https://imgur.com/FjwxmwY.png"/>

We can also see `test.sh` which can be read,write and executed by anyone

<img src="https://imgur.com/AwUTbW3.png"/>

Host the file so we can save it on our local machine and then try to bruteforce jim's password

<img src="https://imgur.com/MPwVo3R.png"/>

<img src="https://imgur.com/5yXKOx2.png"/>

But jim isn't in sudoers group

<img src="https://imgur.com/7gyVhGF.png"/>

Then I used search to find all files for jim

<img src="https://imgur.com/Dr8chCc.png"/>

<img src="https://imgur.com/wbrspgK.png"/>

Now we got charles's password as well

<img src="https://imgur.com/8I8vuAJ.png"/>

Doing a `sudo -l`

<img src="https://imgur.com/AU7SjCJ.png"/>

This is a tee binary so we can look up on GTFOBINS

<img src="https://imgur.com/KbOTH04.png"/>

So we can add a user in `/etc/passwd` with our own hash with an id of 0 which is root

<img src="https://imgur.com/ni7gLaC.png"/>