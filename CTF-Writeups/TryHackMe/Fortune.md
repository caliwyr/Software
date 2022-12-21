# TryHackMe-Fortune

>Abdullah Rizwan 05:43 PM | 31st October ,2020

## NMAP

```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-10-31 17:44 PKT                                                                                     
Nmap scan report for 10.10.170.185                                                                                                                  
Host is up (0.18s latency).                                                                                                                         
Not shown: 993 closed ports                                                                                                                         
PORT     STATE SERVICE    VERSION                                                                                                                   
21/tcp   open  ftp        vsftpd 3.0.3                                                                                                              
22/tcp   open  ssh        OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                              
| ssh-hostkey:                                                                                                                                      
|   2048 3e:ae:18:87:b8:c3:35:b6:3a:af:0e:a4:c3:a2:ef:13 (RSA)                                                                                      
|   256 42:cf:fe:0d:cb:92:24:b9:8f:dc:11:d4:10:a7:a0:3e (ECDSA)                                                                                     
|_  256 5c:fc:bc:c9:3a:01:b1:b6:78:ac:66:3c:34:8f:22:2a (ED25519)                                                                                   
80/tcp   open  http       Apache httpd 2.4.29 ((Ubuntu))                                                                                            
| http-cookie-flags:                                                                                                                                
|   /:                                                                                                                                              
|     PHPSESSID:                                                                                                                                    
|_      httponly flag not set                                                                                                                       
|_http-server-header: Apache/2.4.29 (Ubuntu)                                                                                                        
|_http-title: Wheel of Fortune!                                                                                                                     
111/tcp  open  rpcbind    2-4 (RPC #100000)
| rpcinfo:                                                                                                                                          
|   program version    port/proto  service                                                                                                          
|   100000  2,3,4        111/tcp   rpcbind                                                                                                          
|   100000  2,3,4        111/udp   rpcbind                                                                                                          
|   100000  3,4          111/tcp6  rpcbind           
   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      38720/udp   mountd
|   100005  1,2,3      39689/tcp   mountd
|   100005  1,2,3      42189/tcp6  mountd
|   100005  1,2,3      58060/udp6  mountd
|   100021  1,3,4      34481/udp6  nlockmgr
|   100021  1,3,4      40507/tcp   nlockmgr
|   100021  1,3,4      42097/tcp6  nlockmgr
|   100021  1,3,4      56091/udp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp open  nfs_acl    3 (RPC #100227)
3333/tcp open  dec-notes?
| fingerprint-strings: 
|   GenericLines, GetRequest, HTTPOptions, JavaRMI, LPDString, NULL, kumo-server: 
|     UEsDBAoACQAAAHplX1EnDfabHwAAABMAAAAJABwAY3JlZHMudHh0VVQJAAMHXJ1fB1ydX3V4CwAB
|     BAAAAAAEAAAAAB4v+fOqW8BXX2wHWKqh2fpp8EeGImPJoQZGGkzD1sxQSwcIJw32mx8AAAATAAAA
|     UEsBAh4DCgAJAAAAemVfUScN9psfAAAAEwAAAAkAGAAAAAAAAQAAAKSBAAAAAGNyZWRzLnR4dFVU
|_    BQADB1ydX3V4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8AAAByAAAAAAA=
9999/tcp open  http       Werkzeug httpd 1.0.1 (Python 3.6.9)
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/
submit.cgi?new-service :
SF-Port3333-TCP:V=7.80%I=7%D=10/31%Time=5F9D5C26%P=x86_64-pc-linux-gnu%r(N 
SF:ULL,124,"UEsDBAoACQAAAHplX1EnDfabHwAAABMAAAAJABwAY3JlZHMudHh0VVQJAAMHXJ 
SF:xQSwcIJw32mx8AAAATAAAA\nUEsBAh4DCgAJAAAAemVfUScN9psfAAAAEwAAAAkAGAAAAAA                                                                    [0/67]
SF:AAQAAAKSBAAAAAGNyZWRzLnR4dFVU\nBQADB1ydX3V4CwABBAAAAAAEAAAAAFBLBQYAAAAA 
SF:AQABAE8AAAByAAAAAAA=\n")%r(GenericLines,124,"UEsDBAoACQAAAHplX1EnDfabHw 
SF:AAABMAAAAJABwAY3JlZHMudHh0VVQJAAMHXJ1fB1ydX3V4CwAB\nBAAAAAAEAAAAAB4v\+f 
SF:OqW8BXX2wHWKqh2fpp8EeGImPJoQZGGkzD1sxQSwcIJw32mx8AAAATAAAA\nUEsBAh4DCgA 
SF:JAAAAemVfUScN9psfAAAAEwAAAAkAGAAAAAAAAQAAAKSBAAAAAGNyZWRzLnR4dFVU\nBQAD 
SF:B1ydX3V4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8AAAByAAAAAAA=\n")%r(LPDStrin 
SF:g,124,"UEsDBAoACQAAAHplX1EnDfabHwAAABMAAAAJABwAY3JlZHMudHh0VVQJAAMHXJ1f 
SF:B1ydX3V4CwAB\nBAAAAAAEAAAAAB4v\+fOqW8BXX2wHWKqh2fpp8EeGImPJoQZGGkzD1sxQ 
SF:SwcIJw32mx8AAAATAAAA\nUEsBAh4DCgAJAAAAemVfUScN9psfAAAAEwAAAAkAGAAAAAAAA 
SF:QAAAKSBAAAAAGNyZWRzLnR4dFVU\nBQADB1ydX3V4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQ 
SF:ABAE8AAAByAAAAAAA=\n")%r(JavaRMI,124,"UEsDBAoACQAAAHplX1EnDfabHwAAABMAA 
SF:AAJABwAY3JlZHMudHh0VVQJAAMHXJ1fB1ydX3V4CwAB\nBAAAAAAEAAAAAB4v\+fOqW8BXX 
SF:2wHWKqh2fpp8EeGImPJoQZGGkzD1sxQSwcIJw32mx8AAAATAAAA\nUEsBAh4DCgAJAAAAem 
SF:VfUScN9psfAAAAEwAAAAkAGAAAAAAAAQAAAKSBAAAAAGNyZWRzLnR4dFVU\nBQADB1ydX3V 
SF:4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8AAAByAAAAAAA=\n")%r(kumo-server,124 
SF:,"UEsDBAoACQAAAHplX1EnDfabHwAAABMAAAAJABwAY3JlZHMudHh0VVQJAAMHXJ1fB1ydX 
SF:3V4CwAB\nBAAAAAAEAAAAAB4v\+fOqW8BXX2wHWKqh2fpp8EeGImPJoQZGGkzD1sxQSwcIJ 
SF:w32mx8AAAATAAAA\nUEsBAh4DCgAJAAAAemVfUScN9psfAAAAEwAAAAkAGAAAAAAAAQAAAK 
SF:SBAAAAAGNyZWRzLnR4dFVU\nBQADB1ydX3V4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8 
SF:AAAByAAAAAAA=\n")%r(GetRequest,124,"UEsDBAoACQAAAHplX1EnDfabHwAAABMAAAA 
SF:JABwAY3JlZHMudHh0VVQJAAMHXJ1fB1ydX3V4CwAB\nBAAAAAAEAAAAAB4v\+fOqW8BXX2w 
SF:HWKqh2fpp8EeGImPJoQZGGkzD1sxQSwcIJw32mx8AAAATAAAA\nUEsBAh4DCgAJAAAAemVf 
SF:UScN9psfAAAAEwAAAAkAGAAAAAAAAQAAAKSBAAAAAGNyZWRzLnR4dFVU\nBQADB1ydX3V4C 
SF:wABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8AAAByAAAAAAA=\n")%r(HTTPOptions,124," 
SF:UEsDBAoACQAAAHplX1EnDfabHwAAABMAAAAJABwAY3JlZHMudHh0VVQJAAMHXJ1fB1ydX3V 
SF:4CwAB\nBAAAAAAEAAAAAB4v\+fOqW8BXX2wHWKqh2fpp8EeGImPJoQZGGkzD1sxQSwcIJw3 
SF:2mx8AAAATAAAA\nUEsBAh4DCgAJAAAAemVfUScN9psfAAAAEwAAAAkAGAAAAAAAAQAAAKSB 
SF:AAAAAGNyZWRzLnR4dFVU\nBQADB1ydX3V4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8AA 
SF:AByAAAAAAA=\n");
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel


```
## Nikto

```
root@kali:~/TryHackMe/KoTH/Frotune# nikto -h http://10.10.170.185
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.170.185
+ Target Hostname:    10.10.170.185
+ Target Port:        80
+ Start Time:         2020-10-31 17:46:28 (GMT5)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ Cookie PHPSESSID created without the httponly flag
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.29 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ Web Server returns a valid response with junk HTTP methods, this may cause false positives.
^[[As^Croot@kali:~/TryHackMe/KoTH/Frotune# nikto -h http://10.10.170.185:80

```
Didn't found anything on nikto scan

## Gobuster 

Gobuster will find only one hidden directory which is `/videogames`

<img src="https://imgur.com/4Usefk8.png"/>

## PORT 3333

If we connect to port 3333

<img src="https://imgur.com/BFAyhtG.png"/>

This is a base64 encoded text , we can tell it by looking at the end `==` 

<img src="https://imgur.com/0tAX36c.png"/>

But this has to be converted into a file so,

<img src="https://imgur.com/CoUcr6Y.png"/>


<img src="https://imgur.com/APgOUpx.png"/>

We got the file but it is protected with a password

## Fcrackzip

Frackzip is a tool to crack zip archive passwords

<img src="https://imgur.com/iw5UqkV.png"/>

<img src="https://imgur.com/eRdW0WW.png"/>


`fortuna:ZjUyMmYyMG`
