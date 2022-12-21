# TryHackMe-Relevant

## NMAP

```
Nmap scan report for 10.10.179.43
Host is up (0.15s latency).                                               
Not shown: 995 filtered ports
PORT     STATE SERVICE       VERSION                                                                                                                
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods:                                                           
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0  
|_http-title: IIS Windows Server
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds  Windows Server 2016 Standard Evaluation 14393 microsoft-ds
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info:      
|   Target_Name: RELEVANT
|   NetBIOS_Domain_Name: RELEVANT                                         
|   NetBIOS_Computer_Name: RELEVANT
|   DNS_Domain_Name: Relevant
|   DNS_Computer_Name: Relevant    
|   Product_Version: 10.0.14393
|_  System_Time: 2020-11-12T01:17:03+00:00                                                                                                          
| ssl-cert: Subject: commonName=Relevant                    
| Not valid before: 2020-07-24T23:16:08
|_Not valid after:  2021-01-23T23:16:08
|_ssl-date: 2020-11-12T01:17:42+00:00; 0s from scanner time.
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows
49663/tcp open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows
```

## PORT 80

<img src="https://imgur.com/O0DByH0.png"/>

## PORT 139/445 (SMB)

```
root@kali:~/TryHackMe/Medium/Relevant# smbclient -L \\\\10.10.179.43\\
Enter WORKGROUP\root's password: 

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        nt4wrksv        Disk      
SMB1 disabled -- no workgroup available
root@kali:~/TryHackMe/Medium/Relevant# smbclient \\\\10.10.179.43\\nt4wrksv
Enter WORKGROUP\root's password: 
Try "help" to get a list of possible commands.
smb: \> ls -al
NT_STATUS_NO_SUCH_FILE listing \-al
smb: \> dir
  .                                   D        0  Sun Jul 26 02:46:04 2020
  ..                                  D        0  Sun Jul 26 02:46:04 2020
  passwords.txt                       A       98  Sat Jul 25 20:15:33 2020

                7735807 blocks of size 4096. 4937572 blocks available
smb: \> get passwords.txt
getting file \passwords.txt of size 98 as passwords.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \> 
```

We saved the text file on our local machine 
```
[User Passwords - Encoded]
Qm9iIC0gIVBAJCRXMHJEITEyMw==
QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk
```
Then these look like base64 so we decoded them through cyberchef and found some credentials
```
Bob - !P@$$W0rD!123
Bill - Juw4nnaM4n420696969!$$$
```
Let's try if they are credentials for smbshares

<img src="https://imgur.com/cGgbG2E.png"/>

Through these users we can read `IPC$` share but I failed to do anything on it


## PORT 49663

Now this may seem similar to PORT 80 but it's not here that `nt4wrksv` share is linked which means that it's writable too and we can upload a reverse shell on it.

<img src="https://imgur.com/LBrpl2K.png"/>

<img src="https://imgur.com/bcNoJG4.png"/>

We can put a `aspx` payload in that share

<img src="https://imgur.com/c17U68t.png"/>

<img src="https://imgur.com/zLbRGnt.png"/>

<img src="https://imgur.com/01bddII.png"/>

<img src="https://imgur.com/j3urQ8B.png"/>

Running `getprivs` will tell how we can escalate our privileges.

<img src="https://imgur.com/w8cfUN4.png"/>

Here `SeImpersonatePrivilege` is enabled so any process holding this privilege can impersonate(but not create) any token for which it is able to gethandle. You can get a privileged tokenfrom a  Windows service making it perform an NTLM authentication against the exploit, then execute a process as SYSTEM.

<img src="https://imgur.com/asYKYl4.png"/>

<img src="https://imgur.com/Jc8IRBp.png"/>

<img src="https://imgur.com/9vRSSIj.png"/>

But still we are not `NT\AUTHORITY `

<img src="https://imgur.com/1gRH1QI.png"/>

Download print spoofer.exe (64 bit version)

<img src="https://imgur.com/dd7Es1p.png"/>

Upload where we have write permissions

<img src="https://imgur.com/YkfDkWG.png"/>

<img src="https://imgur.com/eMYz83r.png"/>
