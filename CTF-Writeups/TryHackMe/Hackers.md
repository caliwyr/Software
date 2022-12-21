# TryHackMe-Hackers

## NMAP

```
PORT     STATE SERVICE VERSION                                                                                                                      
21/tcp   open  ftp     vsftpd 2.0.8 or later                                                                                                        
| ftp-anon: Anonymous FTP login allowed (FTP code 230)                                                                                              
|_-rw-r--r--    1 ftp      ftp           400 Apr 29  2020 note                                                                                      
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
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                                 
| ssh-hostkey:                                                                                                                                      
|   256 3b:ff:4a:88:4f:dc:03:31:b6:9b:dd:ea:69:85:b0:af (ECDSA)                                                                                     
|_  256 fa:fd:4c:0a:03:b6:f7:1c:ee:f8:33:43:dc:b4:75:41 (ED25519)                                                                                   
80/tcp   open  http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)                                                                    
|_http-title: Ellingson Mineral Company                                   
9999/tcp open  abyss?                
| fingerprint-strings:               
|   FourOhFourRequest:               
|     HTTP/1.0 200 OK                
|     Date: Thu, 12 Nov 2020 19:43:39 GMT                                 
|     Content-Length: 1              
|     Content-Type: text/plain; charset=utf-8                             
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request                                            
|     Content-Type: text/plain; charset=utf-8        
    Connection: close              
|     Request                        
|   GetRequest, HTTPOptions:                                              
|     HTTP/1.0 200 OK                
|     Date: Thu, 12 Nov 2020 19:43:38 GMT                                 
|     Content-Length: 1              
|_    Content-Type: text/plain; charset=utf-8                             
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/
submit.cgi?new-service :             
```

## PORT 21 (FTP)

```
ftp> ls -al
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Apr 30  2020 .
drwxr-xr-x    2 ftp      ftp          4096 Apr 30  2020 ..
-rw-r--r--    1 ftp      ftp            38 Apr 30  2020 .flag
-rw-r--r--    1 ftp      ftp           400 Apr 29  2020 note
226 Directory send OK.
ftp> get .flag
local: .flag remote: .flag
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for .flag (38 bytes).
226 Transfer complete.
38 bytes received in 0.00 secs (108.8251 kB/s)
ftp> get note
local: note remote: note
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for note (400 bytes).
226 Transfer complete.
400 bytes received in 0.00 secs (303.9883 kB/s)
ftp> 

```

Note

```
Note:
Any users with passwords in this list:
love
sex
god
secret
will be subject to an immediate disciplinary hearing.
Any users with other weak passwords will be complained at, loudly.
These users are:
rcampbell:Robert M. Campbell:Weak password
gcrawford:Gerard B. Crawford:Exposing crypto keys, weak password
Exposing the company's cryptographic keys is a disciplinary offense.
Eugene Belford, CSO
```
## PORT 80 (robots.txt)
```
Skiddies keep out.
Any unauthorised access will be forwarded straight to Richard McGill FBI and you WILL be arrested.
- plague

```
## Gobuster

```
root@kali:~/TryHackMe/KoTH/Hackers# gobuster dir -u http://10.10.105.193:80 -w /usr/share/wordlists/dirb/common.txt
                              
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.105.193:80
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/11/13 00:59:16 Starting gobuster
===============================================================
/backdoor (Status: 301)
/contact (Status: 301)
/img (Status: 301)
/index.html (Status: 301)
/news (Status: 301)
/robots.txt (Status: 200)
/staff (Status: 301)
```

<img src="https://imgur.com/DYOGfJ1.png"/>



## Flags

* On webpage css `thm{b63670f7192689782a45d8044c63197f}`
* On ftp `.flag ` `thm{b63670f7192689782a45d8044c63197f}`