# TryHackMe-USTOUN

## Rustscan

```bash
PORT      STATE SERVICE            REASON          VERSION                   
53/tcp    open  domain?            syn-ack ttl 127
| fingerprint-strings:                     
|   DNSVersionBindReqTCP:                    
|     version                                           
|_    bind                                              
88/tcp    open  kerberos-sec       syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2021-04-03 18:57:34Z)                                   
135/tcp   open  msrpc              syn-ack ttl 127 Microsoft Windows RPC
139/tcp   open  netbios-ssn        syn-ack ttl 127 Microsoft Windows netbios-ssn                                                                    
445/tcp   open  microsoft-ds?      syn-ack ttl 127
464/tcp   open  kpasswd5?          syn-ack ttl 127
593/tcp   open  ncacn_http         syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped         syn-ack ttl 127
1433/tcp  open  ms-sql-s?          syn-ack ttl 127
3268/tcp  open  ldap               syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: ustoun.local0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped         syn-ack ttl 127
3389/tcp  open  ssl/ms-wbt-server? syn-ack ttl 127
| rdp-ntlm-info: 
|   Target_Name: DC01
|   NetBIOS_Domain_Name: DC01
|   NetBIOS_Computer_Name: DC
|   DNS_Domain_Name: ustoun.local
|   DNS_Computer_Name: DC.ustoun.local
|   DNS_Tree_Name: ustoun.local
|   Product_Version: 10.0.17763
|_  System_Time: 2021-04-03T19:00:24+00:00
| ssl-cert: Subject: commonName=DC.ustoun.local
| Issuer: commonName=DC.ustoun.local
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-01-31T19:39:34
| Not valid after:  2021-08-02T19:39:34
| MD5:   fce5 375e 0190 ebc1 bf6e f384 468f 69f6
| SHA-1: dbe7 28d6 1980 1221 c9cb 712a 911e 99b2 303e 5de7
| -----BEGIN CERTIFICATE-----
| MIIC4jCCAcqgAwIBAgIQWPJp5aVu8JlPCbMkI/U6AjANBgkqhkiG9w0BAQsFADAa
| MRgwFgYDVQQDEw9EQy51c3RvdW4ubG9jYWwwHhcNMjEwMTMxMTkzOTM0WhcNMjEw
| ODAyMTkzOTM0WjAaMRgwFgYDVQQDEw9EQy51c3RvdW4ubG9jYWwwggEiMA0GCSqG
| SIb3DQEBAQUAA4IBDwAwggEKAoIBAQDErxES6mfg1M0Ur5tZJHE8BKV+voQAWLa4
| gKJfNi0av9nZ80wp2gJnQmHmZC0ACVpQUufMU9vlaCnk35rqsyM0/igqigSqWXAM
| OY/876ZWGbo5R1g3PjH4bE3mdPtPAJF0wfS8aZ8CdHlmuGDFlJmnu6qFEP/PoACC
| tf1S/vky+8GVs4uLFyxZOY5mam5PNULQvsMz2ycOPwj2CYwgWnrnA52N6m/6O9v7
| XK+K6XBSGHamrHR5EYFXG+u1vItwm4qpUZerUhZl2/WVKIIN4pDXWDCrS59nsVvc
| UC3fDPcgzruHIVJcA+g+CsEYdidS+E1NO3e3ZnWBeWE77ZCSDyTNAgMBAAGjJDAi
| MBMGA1UdJQQMMAoGCCsGAQUFBwMBMAsGA1UdDwQEAwIEMDANBgkqhkiG9w0BAQsF
| AAOCAQEAj9XeCOtYI4LrmeM7qZVQYuuDHIDosWkIw0LMpin4/gt0CDaEB1/uXUnX
| JnBUEHWMDdjzC22hTsTdUIntZgJAk81aQbPm3qMvSE1AXPCCfsN7GehA4kX/n42X
| xiz2rwZo/5DYH0JOWj8iCZyFMiXqSwQm3GWbG4LuTOct+x/rv0UwhyCvdllVRtwz
| P9BM/9qZqy3LecKtJh6UUo8FZ8zkekT9nsJ9/vCv3/THRUMOtEtSXdZUUqccXwRm
| 0HVLxT09wdGGbwdOzzdQSQfLmewi3rSZQf9liaXDtpkK60qrzj4zcyGG2QvX+9EI
| pZV0B4rzCUDWrpaTOsv8z7Qlgeb2GA==
|_-----END CERTIFICATE-----
|_ssl-date: 2021-04-03T19:01:07+00:00; +1m25s from scanner time.
5985/tcp  open  http               syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf             syn-ack ttl 127 .NET Message Framing
47001/tcp open  http               syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc              syn-ack ttl 127 Microsoft Windows RPC
49665/tcp open  msrpc              syn-ack ttl 127 Microsoft Windows RPC
49666/tcp open  msrpc              syn-ack ttl 127 Microsoft Windows RPC
49667/tcp open  msrpc              syn-ack ttl 127 Microsoft Windows RPC
49669/tcp open  msrpc              syn-ack ttl 127 Microsoft Windows RPC
49670/tcp open  ncacn_http         syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
49673/tcp open  msrpc              syn-ack ttl 127 Microsoft Windows RPC
49689/tcp open  msrpc              syn-ack ttl 127 Microsoft Windows RPC
49709/tcp open  msrpc              syn-ack ttl 127 Microsoft Windows RPC
49712/tcp open  msrpc              syn-ack ttl 127 Microsoft Windows RPC
49726/tcp open  msrpc              syn-ack ttl 127 Microsoft Windows RPC

```

From the scan we can see a domain name 

<img src="https://imgur.com/OIXCkjK.png"/>

## PORT 445 (SMB)

<img src="https://imgur.com/sA6YUaV.png"/>

<img src="https://imgur.com/k0wCwOY.png"/>

We can only access `$IPC` as anonymous but there is no use of it. So using `crackmapexec` we can use RID bruteforce which will enumerate all AD objects including users and groups by guessing every resource identifier (RID)

<img src="https://i.imgur.com/QGaD5Jm.png"/>

Here you can see `SVC-Kerb` might be a user we can try to bruteforce as MS-SQL is running we can try there

## PORT 1433 (MS-SQL)
<img src="https://imgur.com/DHqrNIp.png"/>

The database is Microsfoft SQL so let's brute force credentials using `hydra`

<img src="https://imgur.com/vWk2cmP.png"/>

<img src="https://imgur.com/TRWb0an.png"/>

We found the password so we can use metasploit's module for code execution  `use admin/mssql/mssql_exec`

<img src="https://imgur.com/W9HB0pl.png"/>

So there's a command execution alternatively we can try do `sqsh` which is an opensource program for getting a interactive database shell 

<img src="https://imgur.com/PflMsh9.png"/>

Here `-S` indicates the server where we put the IP address or the port if MS-SQL was on a different port

`-U` specifies the username

`-P` specifies the passowrd

Now to execute windows commands we are going to use `xp_cmdshell` which spawns a windows command shell . `xp_cmdshell` is an extended stored procedure provided by Microsoft and stored in the master database. So the whole command will be  `EXEC master ..xp_cmdshell'whoami'` , here `EXEC` is used to execute stored procedure on a database and stored procedures are kinda like functions in mysql /mssql.
 
<img src="https://imgur.com/NYV4xtt.png"/>

We can find the user.txt in `C:\Users\SVC-Kerb.DC01`

<img src="https://imgur.com/MeBsk2U.png"/>

But when I tried to read it I get access denied

<img src="https://imgur.com/GAscxyn.png"/>

So first to get a proper shell I uploaded `ncat64.exe`  you can download it from here

https://github.com/int0x33/nc.exe

<img src="https://imgur.com/NcJwQeg.png"/> 

<img src="https://imgur.com/gOKSRx5.png"/>

Now we got a shell at least so to see what permissions does `SVC-kerb` has we can do `net user SVC-kerb`

<img src="https://imgur.com/xie3JR2.png"/>

It tells that we are just a domain user also this looks like a service account and we won't be able to with it much since this is a Active Directory we can try to run `SharpHoundp.ps1` to gather everything it could find about the domain

<img src="https://imgur.com/Y88CXKM.png"/>

I transfered the file onto target machine but before run it let's find the domain name we already know it from the nmap scan but just to be sure spawn a powershell by running `powershell` and run `Get-ADDomain` this will show you the information of the domain

<img src="https://i.imgur.com/Pm5Ab7r.png"/>

Now we will import sharphound.ps1 and use it's functions

<img src="https://i.imgur.com/5ddi7Y2.png"/>

We need to transfer this on to our local machine so we can analyze the data through `BloodHound`

To transfer it I tried creating a smb share on my local machine and copying the zip file there but windows gave an error that it wasn't allowing to transfer the file so I thought of trying to get a meterpter shell through which I can download the zip file

<img src="https://imgur.com/wRUhqV3.png"/>

<img src="https://imgur.com/M7jC7X1.png"/>

<img src="https://imgur.com/tCsXD3s.png"/>

Run `neo4j console`

<img src="https://imgur.com/Jqtbs8R.png"/>

Then  `bloodhound`

<img src="https://imgur.com/vYCg9fk.png"/>

<img src="https://imgur.com/EuOKUHC.png"/>

I imported that zip file in blood hound but didn't find anything intersting, so can now upload `PowerUp.ps1` to enumerate for misconfigurations or privilege escalation techniques

## PowerUp

You can download the script from here 

https://github.com/PowerShellMafia/PowerSploit/tree/master/Privesc

Also read the documentation from here 

https://www.harmj0y.net/blog/powershell/powerup-a-usage-guide/

Now importing the powershell script and running `Invoke-AllChecks`

<img src="https://imgur.com/aX1QL2g.png"/>

<img src="https://i.imgur.com/9X9ENOs.png"/>

So here we have 2 ways of getting admin first let's try abusing the service `UsoSvc`

### Service Abuse 

Looking at the documentation 

<img src="https://imgur.com/Ml07hzx.png"/>

We can abuse a service by creating a local administartor by creating a new username and then adding it local adminstrators group or by using the current username

<img src="https://i.imgur.com/EKei5Zt.png"/>

Creating a new username and adding it to local adminstrator

<img src="https://i.imgur.com/YwGMx6H.png"/>

To see if this user was added

<img src="https://i.imgur.com/EH8qq9Y.png"/>

Now to switch to this user we can `evil-winrm` to login since winrm service is rinning

<img src="https://imgur.com/fTnSs0g.png"/>

### SeImpersonatePrivilege

Running `whoami /all` to see what privleges the user has

<img src="https://i.imgur.com/1WaniHC.png"/>

<img src="https://i.imgur.com/fXkijU2.png"/>

Now we can abuse this service by through `PrintSpoofer`

<img src="https://i.imgur.com/dgTPbh0.png"/>

Download printspoofer 64 bit verison

https://github.com/itm4n/PrintSpoofer/releases/tag/v1.0

<img src="https://imgur.com/keSGD1i.png"/>

<img src="https://imgur.com/rNRNqV0.png"/>

<img src="https://i.imgur.com/j2XHOue.png"/>

And we can access Administrator's directory

<img src="https://imgur.com/kjdgsVb.png"/>
