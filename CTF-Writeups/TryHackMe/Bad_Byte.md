# TryHackMe-Bad Byte

## Rustscan

```java

rustscan -a 10.10.28.94 -- -A -sC -sV
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.             
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |             
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |              
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'                  
The Modern Day Port Scanner.                                              
________________________________________                                  
: https://discord.gg/GFrQsGy           :                                                                                                            
: https://github.com/RustScan/RustScan :                                                                                                            
 --------------------------------------                                   
😵 https://admin.tryhackme.com                                            

[~] The config file is expected to be at "/root/.rustscan.toml"                                                                                     
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
Open 10.10.28.94:22                  
Open 10.10.28.94:30024               

PORT      STATE SERVICE REASON         VERSION                            
22/tcp    open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                 
| ssh-hostkey:                       
|   2048 f3:a2:ed:93:4b:9c:bf:bb:33:4d:48:0d:fe:a4:de:96 (RSA)           
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC9/A7kkuN5E+SS1C6w1NfeY196Rj4Y1Yx7njNCwNaCgIv8m+V+7MTHsRn3txLXRTHXErMqW3ypCmmjuY3O40kAragZSgA/XhdesGxGVa0szH
K7H4fB28uQiyZgkOfIt/12kGaHB3iGwOeex2Hdg6ct4FdxTWKgDvuKZSLVoPXG66R8SOHql2cXfUtzyUMNJTTqoUED69soEJVG2ctfPKXi4BfFqM3OK2HgKzbmcSPXlLUTNhlcvjPuTa0kMRqiNT
MVdP0PjSFdoaMviXHiznW7Fn6NHe3R/vIQt8Ac05Mdvim21QjRpJ4pm7v5+q1wXCJxGG6Ov71yThKP6yZ4ByMl
|   256 22:72:00:36:eb:37:12:9f:5a:cc:c2:73:e0:4f:f1:4e (ECDSA)   
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBM9QUKykbzCSI7+PgoVzHNKOVIWf+zm0LN/f4n0VJc/P0J9TzLImkYHIOCnRFpNUPtiWGXbHXi
67FQxEpgZMReo=                       
|   256 78:1d:79:dc:8d:41:f6:77:60:65:f5:74:b6:cc:8b:6d (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKrvf1zJBhqU1RxUCYuTgoIy+7NzCqZeFWV67bt8+APV
30024/tcp open  ftp     syn-ack ttl 63 vsftpd 3.0.3                       
| ftp-anon: Anonymous FTP login allowed (FTP code 230)                    
| -rw-r--r--    1 ftp      ftp          1743 Mar 23 20:03 id_rsa   
|_-rw-r--r--    1 ftp      ftp            78 Mar 23 20:09 note.txt
| ftp-syst:                          
|   STAT:                            
| FTP server status:                 
|      Connected to ::ffff:10.8.94.60                                     
|      Logged in as ftp              
|      TYPE: ASCII                   
|      No session bandwidth limit                                         
|      Session timeout in seconds is 300                                  
|      Control connection is plain text                                   
|      Data connections will be plain text                                
|      At session startup, client count was 4                             
|      vsFTPd 3.0.3 - secure, fast, stable
|      At session startup, client count was 4                             
|      vsFTPd 3.0.3 - secure, fast, stable                                
|_End of status                      
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port             

```

We have two ports open , one is 22 (SSH) and the other one is 30024 (FTP)

## PORT 30024 (FTP)

<img src="https://imgur.com/InhrViT.png"/>

From the `note.txt` 

```
I always forget my password. Just let me store an ssh key here.
- errorcauser
```

So `errorcauser` might be a username and we have his `id_rsa` so we can now ssh into the machine

## PORT 22 (SSH)

As soon as we try to login with the private ,it's protected with a passphrase

<img src="https://imgur.com/X96pV5y.png"/>

So here we need `ssh2john` generate a hash for the key so we can crack it with `johntheripper` or `hashcat`

<img src="https://imgur.com/FMD6iKy.png"/>

And we successfully cracked the hash and got the passphrase so now we should be able to login


<img src="https://imgur.com/uGWPD9w.png"/>

We are logged in as `errorcauser` but we see another note which tells that there's a webserver running on local port

<img src="https://imgur.com/uGWPD9w.png"/>

Since there is no `ss` or `nestat` installed we have create a socks proxy on localhost to see which ports are open in order to that we will login through ssh using this command 

`ssh errorcauser@10.10.28.94 -i id_rsa -D 1337`

Also add socks5 proxy in `/etc/proxychains.conf`

<img src="https://imgur.com/Qh1mR9Z.png"/>

Now run a TCP scan on localhost

<img src="https://imgur.com/JvNPSvZ.png"/>

So we can see two more ports 80 and 3306 , so let's scan port 80 what's running on it

<img src="https://imgur.com/d8JYgR2.png"/>

Add proxy with `Foxyproxy` extension or you could manually add proxy setting

<img src="https://imgur.com/bUULaQh.png"/>

<img src="https://imgur.com/BbVshgg.png"/>

Using `wpscan` I enumerated the user

<img src="https://imgur.com/VWzkKvy.png"/>

<img src="https://imgur.com/q8LXKHb.png"/>

For some reason wpscan wasn't giving me plugins for wordpress so I decide to use nse (nmap scripting engine)

<img src="https://imgur.com/jxWJvZg.png"/>

This is the scipt I used to enumerate plugins also to note supply arguemnts to scan upto 1500 results from wordpress plugins script

`proxychains nmap -sT -p 80 --script http-wordpress-enum --script-args search-limit=1500 127.
0.0.1`


<img src="https://imgur.com/FMUZEjS.png"/>

So we have found these two plugins being used on wordpress and these both have exploits on `exploit-db`

<img src="https://imgur.com/5gEmRWu.png"/>

<img src="https://imgur.com/XsLxNnh.png"/>


### Duplicator (Arbitary File Read)

<img src="https://imgur.com/ZzvqaqX.png"/>

<img src="https://imgur.com/jmo01JD.png"/>

### Wp-File manager (RCE)

<img src="https://imgur.com/OwF0kiA.png"/>

<img src="https://imgur.com/WZR3fNK.png"/>

<img src="https://imgur.com/jQ3DkgP.png"/>

I don't like the meterpreter shell so and I can't get the bash through it so I decided to generate a payload that will give a me a reverse shell

<img src="https://imgur.com/JNpk1H1.png"/>

<img src="https://imgur.com/V3Kq8Gd.png"/>

<img src="https://imgur.com/TwOv8Mn.png"/>

Now the room tells that password was logged so by going to `/var/logs` I find `bash.log` belongs cth so we can read it

<img src="https://imgur.com/3KTasuQ.png"/>

Here it gives us the old password , for the current password we can guess that since the year is 2021 so the password must be `G00dP@$sw0rd2021`


<img src="https://imgur.com/whlooza.png"/>

And we guessed it right , we can run any command as sudo

<img src="https://imgur.com/iN8ssj3.png"/>