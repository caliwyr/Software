# TryHackMe-Offline

## NMAP

```
Nmap scan report for 10.10.48.159                                                                                                                   
Host is up (0.17s latency).                                                                                                                         
Not shown: 977 closed ports          
PORT      STATE SERVICE            VERSION                                                                                                          
21/tcp    open  ftp                Microsoft ftpd                                                                                                   
| ftp-syst:                                                               
|_  SYST: Windows_NT                                                                                                                                
22/tcp    open  ssh                OpenSSH for_Windows_8.1 (protocol 2.0)                                                                           
| ssh-hostkey:                                                                                                                                      
|   3072 55:15:8d:d0:54:38:1b:d6:a9:9e:3f:b0:0b:b3:14:34 (RSA)                                                                                      
|   256 cf:5b:e2:de:ce:3b:04:e6:8c:24:6c:2f:37:25:05:c5 (ECDSA)                                                                                     
|_  256 82:bf:bb:09:69:a7:25:5d:66:58:ea:c6:53:d8:c8:8e (ED25519)                                                                                   
53/tcp    open  domain?              
| fingerprint-strings:                                                                                                                              
|   DNSVersionBindReqTCP:                                                 
|     version                                                                                                                                       
|_    bind                                                                
80/tcp    open  http               Microsoft IIS httpd 8.5                                                                                          
| http-methods:                                                                                                                                     
|_  Potentially risky methods: TRACE COPY PROPFIND LOCK UNLOCK PROPPATCH MKCOL PUT DELETE MOVE                                                      
|_http-server-header: Microsoft-IIS/8.5                                   
|_http-svn-info: ERROR: Script execution failed (use -d to debug)                                                                                   
|_http-title: Offline TV                                                  
| http-webdav-scan:                                                       
|   Allowed Methods: OPTIONS, TRACE, GET, HEAD, POST, COPY, PROPFIND, LOCK, UNLOCK                                                                  
|   WebDAV type: Unknown                                                  
|   Server Type: Microsoft-IIS/8.5                                        
|   Public Options: OPTIONS, TRACE, GET, HEAD, POST, PROPFIND, PROPPATCH, MKCOL, PUT, DELETE, COPY, MOVE, LOCK, UNLOCK
|   Server Date: Tue, 22 Sep 2020 15:00:07 GMT                                                                                                      
|   Directory Listing:                                                                                                                              
|     http://10.10.48.159/                                                                                                                          
|     http://10.10.48.159/iis-85.png       
|     http://10.10.48.159/iisstart.htm                                                                                                      [31/105]
|     http://10.10.48.159/otv.jpg                                         
|     http://10.10.48.159/Scarras_Super_Secret_Password.txt                                                                                         
|   Exposed Internal IPs:            
|_    10.10.48.159                   
88/tcp    open  kerberos-sec       Microsoft Windows Kerberos (server time: 2020-09-22 14:57:45Z)                                                   
135/tcp   open  msrpc              Microsoft Windows RPC                  
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn                                                                                    
389/tcp   open  ldap               Microsoft Windows Active Directory LDAP (Domain: kingofthe.domain, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds       Windows Server 2012 R2 Standard 9600 microsoft-ds                                                                
| fingerprint-strings:               
|   SMBProgNeg:                      
|_    SMBr                           
464/tcp   open  kpasswd5?            
593/tcp   open  ncacn_http         Microsoft Windows RPC over HTTP 1.0                                                                              
636/tcp   open  tcpwrapped           
3268/tcp  open  ldap               Microsoft Windows Active Directory LDAP (Domain: kingofthe.domain, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped           
3389/tcp  open  ssl/ms-wbt-server?                                        
|_ssl-date: 2020-09-22T15:00:22+00:00; 0s from scanner time.                                                                                        
9999/tcp  open  http               Microsoft IIS httpd 8.5                                                                                          
| http-methods:                      
|_  Potentially risky methods: TRACE                                      
|_http-server-header: Microsoft-IIS/8.5                                   
|_http-title: Site doesn't have a title (text/plain).                     
49152/tcp open  msrpc              Microsoft Windows RPC                  
49153/tcp open  msrpc              Microsoft Windows RPC                  
49154/tcp open  msrpc              Microsoft Windows RPC                  
49155/tcp open  msrpc              Microsoft Windows RPC                  
49157/tcp open  ncacn_http         Microsoft Windows RPC over HTTP 1.0                                                                              
49158/tcp open  msrpc              Microsoft Windows RPC                  
49159/tcp open  msrpc              Microsoft Windows RPC                  
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/
submit.cgi?new-service :             
SF-Port53-TCP:V=7.80%I=7%D=9/22%Time=5F6A10ED%P=x86_64-pc-linux-gnu%r(DNSV  
SF:ersionBindReqTCP,20,"\0\x1e\0\x06\x81\x04\0\x01\0\0\0\0\0\0\x07version\                                                                          
SF:x04bind\0\0\x10\0\x03");          
Service Info: Host: OFFLINE; OS: Windows; CPE: cpe:/o:microsoft:windows                                                                             

Host script results:                 
|_clock-skew: mean: 1h45m00s, deviation: 3h30m00s, median: 0s                                                                                       
|_nbstat: NetBIOS name: OFFLINE, NetBIOS user: <unknown>, NetBIOS MAC: 02:14:84:5e:69:a1 (unknown)                                                  
| smb-os-discovery:                  
|   OS: Windows Server 2012 R2 Standard 9600 (Windows Server 2012 R2 Standard 6.3)                                                                  
|   OS CPE: cpe:/o:microsoft:windows_server_2012::-                       
|   Computer name: Offline           
|   NetBIOS computer name:           
|   Domain name: kingofthe.domain                                         
|   Forest name: kingofthe.domain                                         
|   FQDN: Offline.kingofthe.domain                                        
|_  System time: 2020-09-22T08:00:07-07:00                                
| smb-security-mode:                 
|   account_used: guest              
|   authentication_level: user                                            
|   challenge_response: supported                                         
|_  message_signing: required                                             
| smb2-security-mode:                
|   2.02:                            
|_    Message signing enabled and required                                
| smb2-time:                         
|   date: 2020-09-22T15:00:07                                             
|_  start_date: 2020-09-22T14:56:06                                       

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                                                      
Nmap done: 1 IP address (1 host up) scanned in 350.03 seconds         	

```


## Gobuster


```


```

## PORT 80

Found a password when looking at the source of web page `OfflineTV2020`


### /Scarras_Super_Secret_Password.txt

username : `scarras` password :`LeagueIsMyLove` 


## Metasploit 


Used msfconsole , `search eternalblue ` , used `4`.

