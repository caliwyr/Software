# TryHackMe-Nax

## NMAP

```
Host is up (0.45s latency).          
Not shown: 995 closed ports          
PORT    STATE SERVICE  VERSION                                                                                                                      
22/tcp  open  ssh      OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)                                                                 
| ssh-hostkey:                                                                                                                                      
|   2048 62:1d:d9:88:01:77:0a:52:bb:59:f9:da:c1:a6:e3:cd (RSA)                                                                                      
|   256 af:67:7d:24:e5:95:f4:44:72:d1:0c:39:8d:cc:21:15 (ECDSA)                                                                                     
|_  256 20:28:15:ef:13:c8:9f:b8:a7:0f:50:e6:2f:3b:1e:57 (ED25519)     
25/tcp  open  smtp     Postfix smtpd                                      
|_smtp-commands: ubuntu.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, 
|_ssl-date: TLS randomness does not represent time                        
80/tcp  open  http     Apache httpd 2.4.18 ((Ubuntu))                     
|_http-server-header: Apache/2.4.18 (Ubuntu)                              
|_http-title: Site doesn't have a title (text/html).                      
389/tcp open  ldap     OpenLDAP 2.2.X - 2.3.X                             
443/tcp open  ssl/http Apache httpd 2.4.18 ((Ubuntu))                     
|_http-server-header: Apache/2.4.18 (Ubuntu)                              
|_http-title: 400 Bad Request                                             
| ssl-cert: Subject: commonName=192.168.85.153/organizationName=Nagios Enterprises/stateOrProvinceName=Minnesota/countryName=US
| Not valid before: 2020-03-24T00:14:58                                   
|_Not valid after:  2030-03-22T00:14:58                                   
|_ssl-date: TLS randomness does not represent time                        
| tls-alpn:                          
|_  http/1.1                         
Service Info: Host:  ubuntu.localdomain; OS: Linux; CPE: cpe:/o:linux:linux_kernel                                                                  

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                                                      
Nmap done: 1 IP address (1 host up) scanned in 95.23 seconds                          
```

## PORT 80

If we go to port 80 we'll see a figure with some ASCII characters and on the bottom we will see some periodic table elements

<img src="https://imgur.com/HWq8nZG.png"/>

If we do some fuzzing we will only be able to find `index.php` which is a login page for nagios XI

<img src="https://imgur.com/M6Yowgq.png"/>

<img src="https://imgur.com/ZsIINj4.png"/>

I tried using default credentials like `root` : `password` , `admin` `admin` , `admin` : `password` none of them worked , I also tried changing the cookie value but this was the message I got when I tried to login with that 

<img src="https://imgur.com/TCmc0bS.png"/>

Tried searching the `nagiosxi` directory but no look because I can't access them without being logged in !

<img src="https://imgur.com/EHIiNcN.png"/>


Going back to the webpage where we saw the elements we know that these elements have atomic numbers 

<img src="https://imgur.com/Amm7mov.png"/>

Do this for all elements and get thier atomic numbers

Ag - 47 
Hg - 80 
Ta - 73
Sb - 51
Po - 84
Pd - 46
Hg - 80
Pt - 78
Lr - 103


Now I tried to merge those numbers in a string `47480735184468078103` put it in cyberchef and tried convert from decimal,hex,base64.32 and all but couldn't find anything but then I had a hunch that these numbers might lead to an ASCII conversion of letters


<img src="https://imgur.com/c5PVfm0.png"/>

47 - /
80 - P
73 - I
51 - 3
84 - T
46 - .
80 - P
78 - N
103 - g


So now combining them `/PI3T.PNg` 

<img src="https://imgur.com/A8TKWHh.png"/>

Using an online piet interpreter we'll get an error

<img src="https://imgur.com/PFwBLbl.png"/>

First convert it to `.png` and then upload it to online interpreter for piet

<img src="https://imgur.com/EBawCiq.png"/>

nagiosadmin: n3p3UQ&9BjLp4$7uhWdY

These are the credentials

<img src="https://imgur.com/tyNfqXl.png"/>

Now for the CVE

<img src="https://imgur.com/BRmcbDq.png"/>

So we have found the exploit which is authenticated RCE and it is  a metasploit exploit

<img src="https://imgur.com/PzUaNa4.png"/>

<img src="https://imgur.com/avv0XU5.png"/> 