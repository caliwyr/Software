# Vulnhub-DC 1

## Rustscan
```bash
rustscan -a 192.168.1.5 -- -A -sC -sV
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

Open 192.168.1.5:22
Open 192.168.1.5:80
Open 192.168.1.5:111
Open 192.168.1.5:55928

PORT      STATE SERVICE REASON         VERSION                                                                                                      
22/tcp    open  ssh     syn-ack ttl 64 OpenSSH 6.0p1 Debian 4+deb7u7 (protocol 2.0)                                                                 
| ssh-hostkey:       
|   1024 c4:d6:59:e6:77:4c:22:7a:96:16:60:67:8b:42:48:8f (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBAI1NiSeZ5dkSttUT5BvkRgdQ0Ll7uF//UJCPnySOrC1vg62DWq/Dn1ktunFd09FT5Nm/ZP9BHlaW5hftzUdtYUQRKfazWfs6g5glPJQSVUqnlNwVUBA46q
S65p4hXHkkl5QO0OHzs8dovwe3e+doYiHTRZ9nnlNGbkrg7yRFQLKPAAAAFQC5qj0MICUmhO3Gj+VCqf3aHsiRdQAAAIAoVp13EkVwBtQQJnS5mY4vPR5A9kK3DqAQmj4XP1GAn16r9rSLUFffz/
ONrDWflFrmoPbxzRhpgNpHx9hZpyobSyOkEU3b/hnE/hdq3dygHLZ3adaFIdNVG4U8P9ZHuVUk0vHvsu2qYt5MJs0k1A+pXKFc9n06/DEU0rnNo+mMKwAAAIA/Y//BwzC2IlByd7g7eQiXgZC2pG
E4RgO1pQCNo9IM4ZkV1MxH3/WVCdi27fjAbLQ+32cGIzjsgFhzFoJ+vfSYZTI+avqU0N86qT+mDCGCSeyAbOoNq52WtzWId1mqDoOzu7qG52HarRmxQlvbmtifYYTZCJWJcYla2GAsqUGFHw==
|   2048 11:82:fe:53:4e:dc:5b:32:7f:44:64:82:75:7d:d0:a0 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCbDC/6BDEUIa7NP87jp5dQh/rJpDQz5JBGpFRHXa+jb5aEd/SgvWKIlMjUDoeIMjdzmsNhwCRYAoY7Qq2OrrRh2kIvQipyohWB8nImetQe52
QG6+LHDKXiiEFJRHg9AtsgE2Mt9RAg2RvSlXfGbWXgobiKw3RqpFtk/gK66C0SJE4MkKZcQNNQeC5dzYtVQqfNh9uUb1FjQpvpEkOnCmiTqFxlqzHp/T1AKZ4RKED/ShumJcQknNe/WOD1ypeDeR
+BUixiIoq+fR+grQB9GC3TcpWYI0IrC5ESe3mSyeHmR8yYTVIgbIN5RgEiOggWpeIPXgajILPkHThWdXf70fiv
|   256 3d:aa:98:5c:87:af:ea:84:b8:23:68:8d:b9:05:5f:d8 (ECDSA)
|_ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKUNN60T4EOFHGiGdFU1ljvBlREaVWgZvgWlkhSKutr8l75VBlGbgTaFBcTzWrPdRItKooYsej
eC80l5nEnKkNU=
80/tcp    open  http    syn-ack ttl 64 Apache httpd 2.2.22 ((Debian))
|_http-favicon: Unknown favicon MD5: B6341DFC213100C61DB4FB8775878CEC
|_http-generator: Drupal 7 (http://drupal.org)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| http-robots.txt: 36 disallowed entries 
| /includes/ /misc/ /modules/ /profiles/ /scripts/ 
| /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt 
| /INSTALL.pgsql.txt /INSTALL.sqlite.txt /install.php /INSTALL.txt 
| /LICENSE.txt /MAINTAINERS.txt /update.php /UPGRADE.txt /xmlrpc.php 
| /admin/ /comment/reply/ /filter/tips/ /node/add/ /search/ 
| /user/register/ /user/password/ /user/login/ /user/logout/ /?q=admin/ 
| /?q=comment/reply/ /?q=filter/tips/ /?q=node/add/ /?q=search/ 
|_/?q=user/password/ /?q=user/register/ /?q=user/login/ /?q=user/logout/
|_http-server-header: Apache/2.2.22 (Debian)
|_http-title: Welcome to Drupal Site | Drupal Site
111/tcp   open  rpcbind syn-ack ttl 64 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          34128/udp   status
|   100024  1          48408/tcp6  status
|   100024  1          50078/udp6  status
|_  100024  1          55928/tcp   status
55928/tcp open  status  syn-ack ttl 64 1 (RPC #100024)
```

## PORT 80 (HTTP)

<img src="https://imgur.com/7XAgdo4.png"/>

Using wappalyzer I can see the version of druapl CMS which is `Durpal 7`

So here we can try creating an account

<img src="https://imgur.com/gW9Hqmb.png"/>

And we get this message

<img src="https://imgur.com/Hd2HALh.png"/>

So  we can search for druapl 7 exploits  , and I found an exploit on metasploit

<img src="https://imgur.com/vyBBLcu.png"/>

<img src="https://imgur.com/SaorVUT.png"/>

<img src="https://imgur.com/uCqTEIZ.png"/>

So for stabilizing the shell I used bash reverse shell to get a shell and this stabilize it using `python`

<img src="https://imgur.com/KuyFHNV.png"/>

We see a `flag1.txt` file

<img src="https://imgur.com/JAOxalU.png"/>

Maybe this refers to a database config file for druapl so I googled for druapl cms config file

<img src="https://imgur.com/dPnBbtO.png"/>

<img src="https://imgur.com/ajZPgZD.png"/>

And we got the mysql creds

<img src="https://imgur.com/L11hBby.png"/>

So let's try these credentials

<img src="https://imgur.com/WcmSany.png"/>

<img src="https://imgur.com/acoqgok.png"/>

<img src="https://imgur.com/AkxHs5h.png"/>

We can see which hash is this by going to hashcat examples

<img src="https://imgur.com/7hiJEWd.png"/>

Tried to crack those hashes but it was taking too long

<img src="https://imgur.com/OjMQQnt.png"/>

So I moved on to `/home` directory, there I saw a user `flag4` having a text file which hints to getting a flag in root's directory

<img src="https://imgur.com/E21ZUpH.png"/>

Running a find command to look for SUID we saw that `find` has a SUID bit on

<img src="https://imgur.com/Mr9VB69.png"/>

Going to GTFOBINS

<img src="https://imgur.com/r73L7jb.png"/>

<img src="https://imgur.com/bf70kuI.png"/>

We are root

<img src="https://imgur.com/3gUznaK.png"/>