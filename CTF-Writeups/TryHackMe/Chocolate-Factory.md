# TryHackMe-Chocolate Factory

## NMAP

```
PORT    STATE SERVICE    VERSION                                                                                                           [337/397]
21/tcp  open  ftp        vsftpd 3.0.3                                                                                                               
|_auth-owners: ERROR: Script execution failed (use -d to debug)                                                                                     
| ftp-anon: Anonymous FTP login allowed (FTP code 230)                                                                                              
|_-rw-rw-r--    1 1000     1000       208838 Sep 30 14:31 gum_room.jpg                                                                              
| ftp-syst:                                                                                                                                         
|   STAT:                                                                                                                                           
| FTP server status:                                                                                                                                
|      Connected to ::ffff:10.2.54.209                                                                                                              
|      Logged in as ftp                                                                                                                             
|      TYPE: ASCII                                                                                                                                  
|      No session bandwidth limit                                                                                                                   
|      Session timeout in seconds is 300                                                                                                            
|      Control connection is plain text                                                                                                             
|      Data connections will be plain text                                                                                                          
|      At session startup, client count was 2                                                                                                       
|      vsFTPd 3.0.3 - secure, fast, stable                                                                                                          
|_End of status                                                                                                                                     
22/tcp  open  ssh        OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                               
|_auth-owners: ERROR: Script execution failed (use -d to debug)                                                                                     
| ssh-hostkey:                                                                                                                                      
|   2048 16:31:bb:b5:1f:cc:cc:12:14:8f:f0:d8:33:b0:08:9b (RSA)                                                                                      
|   256 e7:1f:c9:db:3e:aa:44:b6:72:10:3c:ee:db:1d:33:90 (ECDSA)                                                                                     
|_  256 b4:45:02:b6:24:8e:a9:06:5f:6c:79:44:8a:06:55:5e (ED25519)                                                                                   
80/tcp  open  http       Apache httpd 2.4.29 ((Ubuntu))                                                                                             
|_http-server-header: Apache/2.4.29 (Ubuntu)                                                                                                        
|_http-title: Site doesn't have a title (text/html).                                                                                                
100/tcp open  newacct?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
|_    hope you wont drown Augustus"
106/tcp open  pop3pw?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings: 
|   GenericLines, NULL: 
|     "Welcome to chocolate room!! 
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;) 
|_    hope you wont drown Augustus"
109/tcp open  pop2?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings: 
|   GetRequest, SMBProgNeg: 

```

This machine had 11 ports open out of which three were useful to us http,ftp and ssh rest of them were false positive giving a hint like look somewhere else



## PORT 21

<img src="https://imgur.com/FiFuAtq.png"/>

Running steghide to extract something from the image gave us a text file

<img src="https://imgur.com/TbUYwit.png"/>

<img src="https://imgur.com/ViIroLS.png"/>

So this is like a backup of `/etc/shadow` on the target machine here we need to crack this hash

<img src="https://imgur.com/hkqRX5W.png"/>

<img src="https://imgur.com/7TK9XJa.png"/>

It seems we cannot crack this hash easily so let's just enumerate the next service which is port 80

## PORT 80

<img src="https://imgur.com/t71Aj7Y.png"/>

So we cannot login without a valid username and guessing usernames other than admin didn't worked so next options is to start fuzzing for directories or pages

<img src="https://imgur.com/t4Wz0Iq.png"/>

<img src="https://imgur.com/6gJCU7J.png"/>

We can get a shell as on `/home.php` there is rce so by inserting python payload for reverse shell and setting up a netcat listener we can get a shell

<img src="https://imgur.com/AkyHltI.png"/>

We see a `key_rev_key` file

<img src="https://imgur.com/NAeRrYh.png"/>

But it is a binary file and we cannot execute it as it does not have permissions and we cannot set for it but there's validate.php that we can read and it gives us the password for the login page

<img src="https://imgur.com/6Bq9ysj.png"/>

Also I cat the binary file and got the key

<img src="https://imgur.com/kb0VFh6.png"/>

Still it gives us the same page after logging in to `/home.php` so we have to do something with that binary. In charlie's directory we can see `teleport` file which is a private key for ssh

<img src="https://imgur.com/Hshm836.png"/>

By transfering the ssh key to our machine and then logging in with ssh was successful we are now `charlie`

<img src="https://imgur.com/nWN2vWC.png"/>

We can see that `vi` can be run as all users other than the root so there comes a sudo vulnerability but I just used sudo normally and then typed `!/bin/sh` and got root

<img src="https://imgur.com/A8AdD9U.png"/>

<img src="https://imgur.com/6IupJoB.png"/>

The root flag is encrypted with the key we found in `/var/www/html`

Running the file with python

<img src="https://imgur.com/ZuYu5oA.png"/>