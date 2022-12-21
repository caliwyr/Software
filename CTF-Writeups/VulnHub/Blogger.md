# VulnHub-Blogger

Before doing the scan let's add blogger.thm to our `/etc/hosts/` file

<img src="https://imgur.com/Pq5YVrT.png"/>

## Rustscan

```bash

PORT   STATE SERVICE REASON         VERSION                                                                                               
22/tcp open  ssh     syn-ack ttl 64 OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)                                                   
| ssh-hostkey:       
|   2048 95:1d:82:8f:5e:de:9a:00:a8:07:39:bd:ac:ad:d3:44 (RSA)      
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCxOfkU+Q4dfPLCyiHlcl3+Rl8fCPL9YJ7GzzYAG8Vl75YbD21HXms6zE8KDBFuMu34+hvYCGxHIZVtZRMf9MFHdamqdx4YC++ZU7EFYy4eSQ
jPSukpIZOz4S4md5AmMFNucvvVOq9XVhWnxy86WSZzLO62y7ygqjG6w3sIXlrOjalqCUVgD60wnk53PW6Etkr6kpJwtrBXl60I6LOrb8hmTO63copeWbcYwi4OhlYAKV9EJjAFl9OohQX7uTR7uz
oYPwaztG2HGQw/LQEQeV6KAfL+cb5QQMnP3ZW3r/nMKKZW3zw5h20sVaeoNcgVZ9ANv3EvldJqrRRG/R1wYJHV
|   256 d7:b4:52:a2:c8:fa:b7:0e:d1:a8:d0:70:cd:6b:36:90 (ECDSA)   
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBE6ost/PYmYfXkZxdW+XZSdvrXfTYifdCxxeASUc4llXCR9sRC0lxNP0AnjWlQq+xnAg95xDHN
YSsNoPDaaqgHE=                       
|   256 df:f2:4f:77:33:44:d5:93:d7:79:17:45:5a:a1:36:8b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICNUmat0TujFtlTGYNCBEuh1P+MbsML6IJihp6I7mERS
80/tcp open  http    syn-ack ttl 64 Apache httpd 2.4.18 ((Ubuntu))
| http-methods:                      
|_  Supported Methods: GET HEAD POST OPTIONS                              
|_http-server-header: Apache/2.4.18 (Ubuntu)                              
|_http-title: Blogger | Home                                              
MAC Address: 02:1C:00:A5:06:70 (Unknown)                                  


```

## PORT (80)

<img src="https://imgur.com/frGgPM5.png"/>

This looked like a normal one page website , on running `dirsearch` on website

<img src="https://imgur.com/uK2G57s.png"/>

We find a directory `/assets` and see `/blog`

<img src="https://imgur.com/MO2g2sT.png"/>

This takes us to a blog site which is using wordpress

<img src="https://imgur.com/V78jGvd.png"/>

Using `wpscan ` on wordpress site

<img src="https://imgur.com/E83jnjw.png"/>

<img src="https://imgur.com/3nwGpbg.png"/>

This will find two usernames on wordpress

```
j@m3s 
jm3s (Not a valid username)
```

Couldn't find any creds through brute force


Running all plugins scan through wspcan

<img src="https://imgur.com/jA8M2JZ.png"/>

```
akismet:4.0.8
wpdiscuz:7.0.4
```

There's an exploit for wpdiscuz 

<img src="https://imgur.com/RyQqQQW.png"/>

But this module wasn't getting imported so I went with manual exploitation , there are some poc on youtube so I followed that.


Go to any blog post

<img src="https://imgur.com/tzAOEZT.png"/>

Edit the php reverse shell with a `GIF89a` and set up a netcat listener

<img src="https://imgur.com/RjTjE79.png"/>

<img src="https://imgur.com/dtBj8HX.png"/>

<img src="https://imgur.com/Ho5w4I0.png"/>

Stabilize the shell with `python3 -c 'import pty;pty.spawn("/bin/bash")';`

Doing `cat /etc/contab` to see any cronjobs running and we see one

<img src="https://imgur.com/VOUpyAh.png"/>

<img src="https://imgur.com/OtloDRe.png"/>

We can see that it's creating an archive using a wild card so here we can exploit it through wildcard.

We can also find creds for mysql

```
/** MySQL database username */                                            
define('DB_USER', 'root');                                                
                                                                          
/** MySQL database password */                                            
define('DB_PASSWORD', 'sup3r_s3cr3t');                    

/** MySQL hostname */                                                     
define('DB_HOST', 'localhost');
                                                                          
/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');                                             
                                                                          
/** The Database Collate type. Don't change this if in doubt. */  
define('DB_COLLATE', '');                                        
```

<img src="https://imgur.com/7UP8p7c.png"/>

<img src="https://imgur.com/GwxLiNn.png"/>

I tried cracking this password but failed. Later found a creds file in `/opt` , didn't understood what type of text was that but tried that password for james user it didn't work as well

<img src="https://imgur.com/lnSxdgc.png"/>

After a lot of struggling , trying password , cracking the hash nothing seemed to work. I read the `/etc/passwd` file , there was a user name `vagrant` , tried the password for vagrant : vagrant and got switched to him

<img src="https://imgur.com/x4LeHM9.png"/>

<img src="https://imgur.com/NoSjz7X.png"/>

Now here I don't know if this was intended or forgot to remove this as there was a cronjob running which could have been exploited through wildcard technique if we could found jame's password but I didn't find it anywhere on the box so just have some doubts here. Anyways this was the root for this box.
