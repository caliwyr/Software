# TryHackMe-Production

## NMAP


```
Nmap scan report for 10.10.248.128
Host is up (0.19s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 d3:4a:2e:ae:df:db:e1:1b:c1:62:2b:ce:15:00:73:6e (RSA)
|   256 2e:63:62:b7:95:16:ea:0a:01:0e:12:ef:66:21:23:0b (ECDSA)
|_  256 20:fe:a0:ce:52:f9:35:7b:8a:7a:d0:ee:c1:41:96:90 (ED25519)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
9001/tcp open  tor-orport?
| fingerprint-strings: 
|   GenericLines, GetRequest, JavaRMI, Radmin: 
|     ================================================
|     Ashu's Password Protected Backdoor 
|     ================================================
|     Password Incorrect
|   NULL, SSLSessionReq, SSLv23SessionReq, TLSSessionReq, mongodb: 
|     ================================================
|     Ashu's Password Protected Backdoor 
|_    ================================================
9002/tcp open  dynamid?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GetRequest, HTTPOptions, LANDesk-RC, NotesRPC, RTSPRequest, SIPOptions, afp, giop: 
|     Overly Limited Shell
|     Segfault
|   GenericLines, Help, JavaRMI, LPDString, X11Probe: 
|     Overly Limited Shell
|     Command Executed
|   Kerberos, LDAPBindReq, LDAPSearchReq, NCP, NULL, RPCCheck, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, WMSRequest, ms-sql-s, oracle-tns: 
|_    Overly Limited Shell
9999/tcp open  http        Golang net/http server
| fingerprint-strings: 
|   FourOhFourRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Date: Sat, 03 Oct 2020 10:22:41 GMT
|     Content-Length: 8
|     Content-Type: text/plain; charset=utf-8
|     demnboi
|   GenericLines, Help, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, Socks5: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Date: Sat, 03 Oct 2020 10:22:40 GMT
|     Content-Length: 8
|     Content-Type: text/plain; charset=utf-8
|     demnboi
|   OfficeScan: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain
|     Connection: close
|_    Request: missing required Host header
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
3 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port9001-TCP:V=7.80%I=7%D=10/3%Time=5F7850F0%P=x86_64-pc-linux-gnu%r(NU
SF:LL,95,"\n================================================\n\x20\x20\x20
SF:\x20\x20\x20Ashu's\x20Password\x20Protected\x20Backdoor\x20\x20\x20\x20
SF:\x20\x20\x20\x20\n================================================\n\n"
SF:)%r(GenericLines,A8,"\n================================================
SF:\n\x20\x20\x20\x20\x20\x20Ashu's\x20Password\x20Protected\x20Backdoor\x
SF:20\x20\x20\x20\x20\x20\x20\x20\n=======================================
SF:=========\n\nPassword\x20Incorrect\n")%r(GetRequest,A8,"\n=============
SF:===================================\n\x20\x20\x20\x20\x20\x20Ashu's\x20
SF:Password\x20Protected\x20Backdoor\x20\x20\x20\x20\x20\x20\x20\x20\n====
SF:============================================\n\nPassword\x20Incorrect\n
SF:")%r(SSLSessionReq,95,"\n==============================================
SF:==\n\x20\x20\x20\x20\x20\x20Ashu's\x20Password\x20Protected\x20Backdoor
SF:\x20\x20\x20\x20\x20\x20\x20\x20\n=====================================
SF:===========\n\n")%r(TLSSessionReq,95,"\n===============================
SF:=================\n\x20\x20\x20\x20\x20\x20Ashu's\x20Password\x20Protec
SF:ted\x20Backdoor\x20\x20\x20\x20\x20\x20\x20\x20\n======================
SF:==========================\n\n")%r(SSLv23SessionReq,95,"\n=============
SF:===================================\n\x20\x20\x20\x20\x20\x20Ashu's\x20
SF:Password\x20Protected\x20Backdoor\x20\x20\x20\x20\x20\x20\x20\x20\n====
SF:============================================\n\n")%r(JavaRMI,A8,"\n====
SF:============================================\n\x20\x20\x20\x20\x20\x20A
SF:shu's\x20Password\x20Protected\x20Backdoor\x20\x20\x20\x20\x20\x20\x20\
SF:x20\n================================================\n\nPassword\x20In
SF:correct\n")%r(Radmin,A8,"\n============================================
SF:====\n\x20\x20\x20\x20\x20\x20Ashu's\x20Password\x20Protected\x20Backdo
SF:or\x20\x20\x20\x20\x20\x20\x20\x20\n===================================
SF:=============\n\nPassword\x20Incorrect\n")%r(mongodb,95,"\n============
SF:====================================\n\x20\x20\x20\x20\x20\x20Ashu's\x2
SF:0Password\x20Protected\x20Backdoor\x20\x20\x20\x20\x20\x20\x20\x20\n===
SF:=============================================\n\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port9002-TCP:V=7.80%I=7%D=10/3%Time=5F7850F0%P=x86_64-pc-linux-gnu%r(NU
SF:LL,15,"Overly\x20Limited\x20Shell\n")%r(GenericLines,26,"Overly\x20Limi
SF:ted\x20Shell\nCommand\x20Executed\n")%r(GetRequest,1E,"Overly\x20Limite
SF:d\x20Shell\nSegfault\n")%r(HTTPOptions,1E,"Overly\x20Limited\x20Shell\n
SF:Segfault\n")%r(RTSPRequest,1E,"Overly\x20Limited\x20Shell\nSegfault\n")
SF:%r(RPCCheck,15,"Overly\x20Limited\x20Shell\n")%r(DNSVersionBindReqTCP,1
SF:E,"Overly\x20Limited\x20Shell\nSegfault\n")%r(DNSStatusRequestTCP,1E,"O
SF:verly\x20Limited\x20Shell\nSegfault\n")%r(Help,26,"Overly\x20Limited\x2
SF:0Shell\nCommand\x20Executed\n")%r(SSLSessionReq,15,"Overly\x20Limited\x
SF:20Shell\n")%r(TerminalServerCookie,15,"Overly\x20Limited\x20Shell\n")%r
SF:(TLSSessionReq,15,"Overly\x20Limited\x20Shell\n")%r(Kerberos,15,"Overly
SF:\x20Limited\x20Shell\n")%r(SMBProgNeg,15,"Overly\x20Limited\x20Shell\n"
SF:)%r(X11Probe,26,"Overly\x20Limited\x20Shell\nCommand\x20Executed\n")%r(
SF:FourOhFourRequest,1E,"Overly\x20Limited\x20Shell\nSegfault\n")%r(LPDStr
SF:ing,26,"Overly\x20Limited\x20Shell\nCommand\x20Executed\n")%r(LDAPSearc
SF:hReq,15,"Overly\x20Limited\x20Shell\n")%r(LDAPBindReq,15,"Overly\x20Lim
SF:ited\x20Shell\n")%r(SIPOptions,1E,"Overly\x20Limited\x20Shell\nSegfault
SF:\n")%r(LANDesk-RC,1E,"Overly\x20Limited\x20Shell\nSegfault\n")%r(Termin
SF:alServer,15,"Overly\x20Limited\x20Shell\n")%r(NCP,15,"Overly\x20Limited
SF:\x20Shell\n")%r(NotesRPC,1E,"Overly\x20Limited\x20Shell\nSegfault\n")%r
SF:(JavaRMI,26,"Overly\x20Limited\x20Shell\nCommand\x20Executed\n")%r(WMSR
SF:equest,15,"Overly\x20Limited\x20Shell\n")%r(oracle-tns,15,"Overly\x20Li
SF:mited\x20Shell\n")%r(ms-sql-s,15,"Overly\x20Limited\x20Shell\n")%r(afp,
SF:1E,"Overly\x20Limited\x20Shell\nSegfault\n")%r(giop,1E,"Overly\x20Limit
SF:ed\x20Shell\nSegfault\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port9999-TCP:V=7.80%I=7%D=10/3%Time=5F7850F1%P=x86_64-pc-linux-gnu%r(Ge
SF:tRequest,7C,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Sat,\x2003\x20Oct\x2020
SF:20\x2010:22:40\x20GMT\r\nContent-Length:\x208\r\nContent-Type:\x20text/
SF:plain;\x20charset=utf-8\r\n\r\ndemnboi\n")%r(HTTPOptions,7C,"HTTP/1\.0\
SF:x20200\x20OK\r\nDate:\x20Sat,\x2003\x20Oct\x202020\x2010:22:41\x20GMT\r
SF:\nContent-Length:\x208\r\nContent-Type:\x20text/plain;\x20charset=utf-8
SF:\r\n\r\ndemnboi\n")%r(FourOhFourRequest,7C,"HTTP/1\.0\x20200\x20OK\r\nD
SF:ate:\x20Sat,\x2003\x20Oct\x202020\x2010:22:41\x20GMT\r\nContent-Length:
SF:\x208\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\n\r\ndemnboi\n
SF:")%r(GenericLines,58,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Typ
SF:e:\x20text/plain\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")
SF:%r(RTSPRequest,58,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\
SF:x20text/plain\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(
SF:Help,58,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/pl
SF:ain\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(SSLSession
SF:Req,58,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/pla
SF:in\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(LPDString,5
SF:8,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain\r\
SF:nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(SIPOptions,58,"H
SF:TTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain\r\nCon
SF:nection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(Socks5,58,"HTTP/1\.1
SF:\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain\r\nConnection:
SF:\x20close\r\n\r\n400\x20Bad\x20Request")%r(OfficeScan,76,"HTTP/1\.1\x20
SF:400\x20Bad\x20Request\r\nContent-Type:\x20text/plain\r\nConnection:\x20
SF:close\r\n\r\n400\x20Bad\x20Request:\x20missing\x20required\x20Host\x20h
SF:eader");
Service Info: Host: THM-PROD; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 2h19m59s, deviation: 4h02m30s, median: 0s
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: thm-prod
|   NetBIOS computer name: THM-PROD\x00
|   Domain name: \x00
|   FQDN: thm-prod
|_  System time: 2020-10-03T03:25:32-07:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-10-03T10:25:32
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 259.04 seconds


```

## SMB

`smbclient -L \\\\machine_ip\\`
`smbclient \\\\machine_ip\key`

You'll find private key of `ashu`

## SSH

ssh ashu@machine_ip - id_rsa