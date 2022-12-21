# HackTheBox-Notebook

## Rustscan

```
rustscan -a 10.129.84.245 -- -A -sC -sV                                                       
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.                  
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |                  
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |                  
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'                                                                                            
The Modern Day Port Scanner.                                                                                                                        
________________________________________                                                                                                            
: https://discord.gg/GFrQsGy           :                                                                                                            
: https://github.com/RustScan/RustScan :                                                                                                            
 --------------------------------------                                                                                                             
Real hackers hack time ⌛                
[~] The config file is expected to be at "/root/.rustscan.toml"
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
Open 10.129.84.245:22                
Open 10.129.84.245:80                
PORT   STATE SERVICE REASON         VERSION                               
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                    
| ssh-hostkey:                                                            
|   2048 86:df:10:fd:27:a3:fb:d8:36:a7:ed:90:95:33:f5:bf (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCZwjrB05nGUvacI81YxNqy+6WpPHhIju6c73aoiru9nW/aVhTmOEsSOGoChEXeQeDN67ZN5QW4LFf0tXeQeJqvgO82HtFkUOiN8tt1RpI98S
V+hx8scCzpmtAyu1OJSUM3/cL2tEPTcPHAgHTmroWiXxIMPhTFLIoDVBIqmBrORUIwgjIzFUbEDQJXKPkFciofbowVOkHnT+lv5XokU6571wrX/LRJvTNBEAvbbz0HAfvUkne8ycQsW08qk/Bugi
LnJHLg24YryGdHl5RqqW/42fsUADngFLncy2+/XCo8Pe/erO+7Zw6r4n1qVb0W0BZ+lRflcRss3diM/21R6O0z
|   256 e7:81:d6:6c:df:ce:b7:30:03:91:5c:b5:13:42:06:44 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLeuBF/ZBUM0ZBYW4+vgQMhIPWVs2fzv9lmQHoflWFNMP/sFWZDeVneJE0CRSLnYi2y/wwc079
bIsQRibay3Fpg=
|   256 c6:06:34:c7:fc:00:c4:62:06:c2:36:0e:ee:5e:bf:6b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDg0mzA1xTe9hivlJN4s+7eXaiyIYefpyykHIir3btEA
80/tcp open  http    syn-ack ttl 63 nginx 1.14.0 (Ubuntu)
|_http-favicon: Unknown favicon MD5: B2F904D3046B07D05F90FB6131602ED2
| http-methods:                      
|_  Supported Methods: GET HEAD OPTIONS                                   
|_http-server-header: nginx/1.14.0 (Ubuntu)                               
|_http-title: The Notebook - Your Note Keeper                             
```

## PORT 80 (HTTP)

<img src="https://imgur.com/I1NTuJ9.png"/>

I went to `login` page and tried basic sqli

<img src="https://imgur.com/13lJcWB.png"/>

Tried `admin:admin`

<img src="https://imgur.com/Sbiq56t.png"/>

And got this error so we know that `admin` user exists

Then I decide to register an account

<img src="https://imgur.com/AV6CmzR.png"/>

After registering an account I tried to to do some stuff with HTML but saw couldn't do anything

<img src="https://imgur.com/RxzOtTN.png"/>

On running `dirsearch` I didn't found anything

<img src="https://imgur.com/4F0JUo9.png"/>

So I decided to intercept the request with `burp suite` and found a base64 encoded cookie

<img src="https://imgur.com/gvj5ucv.png"/>

Which I then took it to cyberchef 

<img src="https://imgur.com/Rkh6ioF.png"/>

Alternatively it is best to vist https://jwt.io

<img src="https://imgur.com/F32iQD4.png"/>

Now we want to create our own key and host it on port 7070

https://gist.github.com/ygotthilf/baa58da5c3dd1f69fae9

<img src="https://imgur.com/aT8aKAw.png"/>

<img src="https://imgur.com/07yxVZs.png"/>

Notice we have two keys public and private we want the public to be hosted and rename it to `privKey.key`

<img src="https://imgur.com/lo1SuSz.png"/>

<img src="https://imgur.com/brwDQcH.png"/>

<img src="https://imgur.com/v4174MW.png"/>

Notice we have added `admin_cap =true` and changed the `kid` to our machine 

now copy the whole encoded text and replace it with the cookie

Notice we will see `admin panel`

<img src="https://imgur.com/jEMn97H.png"/>

I decide to upload `phpbash.php` which give us a nice sessions on the web browser

<img src="https://imgur.com/LaABinj.png"/>

<img src="https://imgur.com/s51NR88.png"/>

Running linpeas we can see that there's docker installed on the box

<img src="https://imgur.com/INmrnLf.png"/>

We can also see IPTABLES have docker rules configured

<img src="https://imgur.com/ONRy7HK.png"/>

I tried connecting to docker with `docker -H 127.0.0.1:10101`, `127.0.0.1:8080` but was doing it wrong maybe


Going back to the website as admin I saw some notes which I was able to view

<img src="https://imgur.com/HHp1bqz.png"/>

Here Noah says that he has some files in `backups`

<img src="https://imgur.com/TuIoUeu.png"/>

<img src="https://imgur.com/AHcZI4r.png"/>

We can see `home.tar.gz`

I started a python server on target machine and transfer that gz archive

<img src="https://imgur.com/lqRGgxa.png"/>

<img src="https://imgur.com/wvtMfeI.png"/>

So we have ssh keys for user `noah`

<img src="https://imgur.com/bMzSGFv.png"/>

<img src="https://imgur.com/y6qFjCU.png"/>

This `*` will accept any argument so let's see if we can run commands on the container

<img src="https://imgur.com/ezLQ4c4.png"/>

<img src="https://imgur.com/jbnQVE9.png"/>

Appearently there's a CVE for docker exec

https://github.com/Frichetten/CVE-2019-5736-PoC

Download the `golang` file and compile it on your machine 

Set SUID on bash  in `payload`

<im src="https://imgur.com/fyEBhGO.png"/>

Then compile the golang source code with `go build docker.go` transfer that binary to docker container execute it and in the same time execute `sh` on docker

<img src="https://imgur.com/fyEBhGO.png"/>

<img src="https://imgur.com/admmduH.png"/>

<img src="https://imgur.com/qLv5VYu.png"/>

Or if we simply want a reverse shell we could use a bash reverse shell payload instead of making /bin/bash a SUID

<im src="https://imgur.com/CEf577v.png"/>

<img src="https://imgur.com/mAVoURG.png"/>

<img src="https://imgur.com/V0srjkt.png"/>