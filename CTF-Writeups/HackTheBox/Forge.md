# HackTheBox-Forge

## NMAP

```bash
PORT   STATE    SERVICE REASON         VERSION
21/tcp filtered ftp     no-response        
22/tcp open     ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open     http    syn-ack ttl 63 Apache httpd 2.4.41
| http-methods:                      
|_  Supported Methods: GET HEAD POST OPTIONS                     
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Did not follow redirect to http://forge.htb
Service Info: Host: 10.10.11.111; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## PORT 80 (HTTP)

<img src="https://i.imgur.com/gFc4q87.png"/>

on visting http server , it's going to redirect us to `forge.htb` so let's add this to `/etc/hosts`  file 

<img src="https://i.imgur.com/Tozixid.png"/>

<img src="https://i.imgur.com/AkIQju6.png"/>

We can try to upload images through this page , but after that there's nothing we can do , we can't upload a php file as it replaces the a random name 

<img src="https://i.imgur.com/K2LrZ2W.png"/>

<img src="https://i.imgur.com/EJh7bsj.png"/>

I tried to visit `uploads` directory but it just gives an error

<img src="https://i.imgur.com/wYjc2wn.png"/>

We can see `static` directory from where javascript ,css and images are loaded

<img src="https://i.imgur.com/D08h6S5.png"/>

I ran `gobuster` to fuzz for files and directories but didn't found anything so went with `wfuzz` to look for any subdomains

<img src="https://i.imgur.com/pfDT7km.png"/>

We found `admin.forge.htb` so let's add this to /etc/hosts file

<img src="https://i.imgur.com/aD1znZ4.png"/>

so going to `admin.com.forge.htb`

<img src="https://i.imgur.com/4oHjlXJ.png"/>

It seems that we can't access this as it's only allowed from localhost , going back to `forge.htb` I missed looking into `upload from url` option

<img src="https://i.imgur.com/Kh2oP6n.png"/>

So what if we try to access `admin.forge.htb` through this which is known as a SSRF attack (Server Side Request Foregery) where we make a request from the web application to access internal resources

<img src="https://i.imgur.com/1mg1571.png"/>

<img src="https://i.imgur.com/tDbytOp.png"/>

So it seems there's a wordlist being used here , let's try if we can acesss localhost

<img src="https://i.imgur.com/J7BWm8P.png"/>

It gives the same error again so we need to bypass this backlist somehow , for localhost we can try this `http://127.127.127.127`  , `http://127.0.1.1` or `http://[::]:80/`


<img src="https://imgur.com/K2XNCZA.png"/>

And it uploads the file now we can just wget it and see the response

<img src="https://imgur.com/lQPXEQX.png"/>

Perfect , we bypassed making a request to localhost but still have to do something about the admin subdomain so why not try accessing it like this

`http://admin.Forge.htb` or `http://ADMIN.FORGE.HTB`

<img src="https://imgur.com/8SOxFLn.png"/>

Here we can see an `upload` folder again which I assume it's the same one but we have `announcmennts` so let's try to see what's in there

`http://ADMIN.FORGE.HTB/announcements/`

<img src="https://imgur.com/D0GXXCR.png"/>

Here it gives us the ftp creds also it tells us that there's a GET parameter on `/upload` which supports ftp,http or https , so we need to make the request again with the ftp creds to `upload` on `admin.forge.htb` domain

`http://ADMIN.FORGE.HTB/upload?u=ftp://user:heightofsecurity123!@127.127.127.127`

<img src="https://i.imgur.com/KzdVwWX.png"/>

We can grab the `user.txt` if we want but we don't see much here . I went to `snap` folder but it was just a rabitt hole wasn't anything there , so we can try to access `.ssh` folder if it exists we can get the contents there so fingers crossed.


`http://ADMIN.FORGE.HTB/upload?u=ftp://user:heightofsecurity123!@127.127.127.127/.ssh/`

<img src="https://i.imgur.com/SrO9iXv.png"/>

Boom we can get the `id_rsa` key but we don't know the user yet so let's grab` authorized_keys` file too as it contains the username for whom the keys are generated for

<img src="https://imgur.com/Xodr36h.png"/>

This key is for `user` so let's try logging in 

<img src="https://imgur.com/InwSVtf.png"/>

We can do `sudo -l` to see if the user can run commands as sudo

<img src="https://imgur.com/ohoxvyN.png"/>

Checking the python , what it's about and it's opening up a TCP port to listen on and we can connect to it using `telnet` which it's going to ask for a password and after that we can run commands like ps -aux , ss -ltp, df 

<img src="https://imgur.com/CBdTZrU.png"/>

<img src="https://imgur.com/uuMU1c6.png"/>

If we specify a wrong option other than 1,2,3,4 and `Pdb` prompt is going to show up

<img src="https://imgur.com/xlEKt2o.png"/>

So I googled what this Pdb  is and it's a python debugger

<img src="https://imgur.com/NlyS0yI.png"/>

Being a debugger we can try to run some python commands through it 

<img src="https://imgur.com/hAAqsQb.png"/>

<img src="https://imgur.com/Q3WJXbb.png"/>

With this we rooted this box 

## References

- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Request%20Forgery/README.md
- https://docs.python.org/3/library/pdb.html
