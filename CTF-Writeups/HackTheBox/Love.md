# HackTheBox-Love

## Rustscan

```bash
                               
PORT      STATE SERVICE      REASON          VERSION
80/tcp    open  http         syn-ack ttl 127 Apache httpd 2.4.46 ((Win64) OpenSSL/1.1.1j PHP/7.3.27)                                                
| http-cookie-flags:                                              
|   /:                                                     
|     PHPSESSID:                                        
|_      httponly flag not set                               
|_http-title: Voting System using PHP  
135/tcp   open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
139/tcp   open  netbios-ssn  syn-ack ttl 127 Microsoft Windows netbios-ssn
443/tcp   open  ssl/http     syn-ack ttl 127 Apache httpd 2.4.46 (OpenSSL/1.1.1j PHP/7.3.27)
| ssl-cert: Subject: commonName=staging.love.htb/organizationName=ValentineCorp/stateOrProvinceName=m/countryName=in/organizationalUnitName=love.htb
/localityName=norway/emailAddress=roy@love.htb
| Issuer: commonName=staging.love.htb/organizationName=ValentineCorp/stateOrProvinceName=m/countryName=in/organizationalUnitName=love.htb/localityNa
me=norway/emailAddress=roy@love.htb                                       
| Public Key type: rsa                       
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-01-18T14:00:16
| Not valid after:  2022-01-18T14:00:16
| MD5:   bff0 1add 5048 afc8 b3cf 7140 6e68 5ff6
| SHA-1: 83ed 29c4 70f6 4036 a6f4 2d4d 4cf6 18a2 e9e4 96c2
| -----BEGIN CERTIFICATE-----
| MIIDozCCAosCFFhDHcnclWJmeuqOK/LQv3XDNEu4MA0GCSqGSIb3DQEBCwUAMIGN
| MQswCQYDVQQGEwJpbjEKMAgGA1UECAwBbTEPMA0GA1UEBwwGbm9yd2F5MRYwFAYD
| VQQKDA1WYWxlbnRpbmVDb3JwMREwDwYDVQQLDAhsb3ZlLmh0YjEZMBcGA1UEAwwQ
| c3RhZ2luZy5sb3ZlLmh0YjEbMBkGCSqGSIb3DQEJARYMcm95QGxvdmUuaHRiMB4X
445/tcp   open  microsoft-ds syn-ack ttl 127 Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
3306/tcp  open  mysql?       syn-ack ttl 127
| fingerprint-strings: 
|   LDAPBindReq, LPDString, NULL, giop: 
|_    Host '10.10.14.154' is not allowed to connect to this MariaDB server 
5000/tcp  open  http         syn-ack ttl 127 Apache httpd 2.4.46 (OpenSSL/1.1.1j PHP/7.3.27)
|_http-title: 403 Forbidden
5040/tcp  open  unknown      syn-ack ttl 127
5985/tcp  open  http         syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
5986/tcp  open  ssl/http     syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
| ssl-cert: Subject: commonName=LOVE
| Subject Alternative Name: DNS:LOVE, DNS:Love
| Issuer: commonName=LOVE
| Public Key type: rsa
| Public Key bits: 4096
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-04-11T14:39:19
| Not valid after:  2024-04-10T14:39:19
| MD5:   d35a 2ba6 8ef4 7568 f99d d6f4 aaa2 03b5
| SHA-1: 84ef d922 a70a 6d9d 82b8 5bb3 d04f 066b 12f8 6e73
47001/tcp open  http         syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)          
|_http-title: Not Found                                                   
49664/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49665/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49666/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49667/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49668/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49669/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49670/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC

```

We can see a domain name `love.htb` and `staging.love.htb` so let's add this to our `/etc/hosts` file

<img src="https://imgur.com/nhIRIul.png"/>

## PORT 80 (HTTP)

<img src="https://imgur.com/Y6kHc95.png"/>

On intercepting the request with `burp suite` we can see POST parameters

<img src="https://imgur.com/JLpYvlG.png"/>

I tried messing with parameters and got the error in sql 

<img src="https://imgur.com/SJM3xTz.png"/>

Tried to do sqli but didn't work so let's visit staging.love.htb

<img src="https://imgur.com/HR2YJx3.png"/>

This seems to load a file using url so let's try to add our php shell

`<?php system($_GET['cmd']); ?>`

<img src="https://imgur.com/uJIjZd3.png"/>

<img src="https://imgur.com/Al4rX8t.png"/>

But this didn't work so there was port 5000 open on the machine which we cannot access

<img src="https://imgur.com/bYoofQF.png"/>

So let's try to access this port through that url input field

<img src="https://imgur.com/rDko6kX.png"/>

And we got voter admin's credentials but this won't work there as it needs an id

<img src="https://imgur.com/eLSsZEQ.png"/>

So I though maybe searching on google for voter system and found the exact same application 

https://www.sourcecodester.com/php/12306/voting-system-using-php.html

<img src="https://imgur.com/S5zMMvh.png"/>

<img src="https://imgur.com/2NeEM9G.png"/>

So we need to navigate to `/admin` in order to login with credentials

<img src="https://imgur.com/eCFsAI7.png"/>

<img src="https://imgur.com/9sjjyfQ.png"/>

Click on `Voters` from the dashboard

<img src="https://imgur.com/rppZV6t.png"/>

Add a new voter and for a profile picture add a php file either with GET paramter like I did above or powney shell

<img src="https://imgur.com/JsNuFhE.png"/>

<img src="https://imgur.com/tGdEDt6.png"/>

<img src="https://imgur.com/GhnEscg.png"/>

<img src="https://i.imgur.com/3bY34aY.png"/>

And opening this php file we will get an interactive shell

<img src="https://imgur.com/FBWksyb.png"/>

Now generate a msfvenom payload because the file gets deleted because of some script of task running in the background 

<img src="https://imgur.com/Ek6iVms.png"/>

<img src="https://imgur.com/GfUpuuu.png"/>

<img src="https://imgur.com/birGV2H.png"/>

<img src="https://imgur.com/56mK9Dn.png"/>

<img src="https://imgur.com/XBLivlj.png"/>

Now for privilege escalation we can run `PowerUp.ps1` script to enumerate for misconfigurations or potential vectors for privesc, import the powershell script and run `Invoke-Allchecks`

<img src="https://imgur.com/Pxkc9zD.png"/>

We can see that installation for any program will be installed as SYSTEM 

<img src="https://i.imgur.com/Iw3HUzK.png"/>

I used this as a reference 
https://www.hackingarticles.in/windows-privilege-escalation-alwaysinstallelevated/

Now there were tons of articles on how you can abuse so there were many ways you can either use the abuse function you saw by just running `Write-UserAddMSI` and on running ,it will create a msi program which you can install and it will create a local admin user 

Another way was to metasploit's post exploit module `use exploit/windows/local/always_install_elevated` but I did this exploit manually , I generate a windows 64 bit payload as the noramal one didn't respond

<img src="https://imgur.com/5N0nyrb.png"/>

This is will create windows installer file which can install it on the target machine using `msiexec`. So upload it to the target machine

<img src="https://imgur.com/8auU2hb.png"/>

<img src="https://i.imgur.com/yKLTIp1.png"/>