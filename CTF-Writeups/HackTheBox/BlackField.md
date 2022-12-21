# HackTheBox-BlackField

## NMAP

```bash
PORT      STATE SERVICE       VERSION
53/tcp    open  domain?                                                
| fingerprint-strings: 
|   DNSVersionBindReqTCP:                                              
|     version                                                          
|_    bind                                                   
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-01-01 02:43:13Z)
135/tcp   open  msrpc         Microsoft Windows RPC               
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: BLACKFIELD.local0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: BLACKFIELD.local0., Site: Default-First-Site-Name)
49676/tcp open  msrpc         Microsoft Windows RPC
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
```

So from the nmap scan and the LDAP it pretty much tells that this is an active directory box and the only port from where we can start is from ldap ,smb and rpc

Running `enum4linux` to check null authentication on smb , ldap and rpc to gather information about the domain and maybe if we are allowed to gather usernames

<img src="https://i.imgur.com/HEcIY3i.png"/>

<img src="https://i.imgur.com/L0W04AK.png"/>

<img src="https://i.imgur.com/OTC5UYH.png"/>

This shows us that we don't have access to anything so moving on with trying `smbclient`

## PORT 139/445 (SMB)

<img src="https://i.imgur.com/TJvl4s0.png"/>

I tried `forensic` share but we weren't allowed to access being unauthorized

<img src="https://i.imgur.com/qHbM8P7.png"/>

But from access `profiles$` share we get a huge list of usernames

<img src="https://i.imgur.com/1UgvNg7.png"/>

## Foothold

Here I had a difficultly , I can't just use `mget *` here because all these folders are empty and I won't be manually writing these usernames in a file which would take ages , so I went through this list and there were 3 accounts that caught my attention 

<img src="https://i.imgur.com/chvZ5k1.png"/>

<img src="https://i.imgur.com/HXVZ7h7.png"/>

I then made a list of users so to see which usernames are valid

<img src="https://i.imgur.com/VtNCTuS.png"/>

To verify that these accounts are valid , we can use `kerbrute` using the userenum option 

```bash
/opt/kerbrute/kerbrute_linux_amd64 userenum -d BLACKFIELD.local users.txt --dc 10.10.10.192
```

<img src="https://i.imgur.com/ymdzaYV.png"/>

The neat feature about this tool is that it can also tell which account has pre-authentication disabled meaning that we can also perform `AS-REP roasting`
which would allow us to get a hash

This can also be done through impacket's `GetUsersNP` script

```bash
python3 /opt/impacket/examples/GetNPUsers.py -no-pass -dc-ip 10.10.10.192 -usersfile users.txt BLACKFIELD/abc
```

<img src="https://i.imgur.com/L7ALSz6.png"/>

Using `hashcat` we can crack the hash

<img src="https://i.imgur.com/mz98DEu.png"/>

<img src="https://i.imgur.com/YrCZPBp.png"/>

Now that we have an account we can check if we have access to winrm

<img src="https://i.imgur.com/yWJs4hE.png"/>

And it seems that we are only limited to smb with this account

<img src="https://i.imgur.com/5FiTGJN.png"/>

Visting `NETLOGIN` share it's empty , so there wasn't anything interesting in smb shares but since we have a valid account we can use this against enum4linux to see if we are able to list usernames now 

<img src="https://i.imgur.com/EHHrXVZ.png"/>

<img src="https://i.imgur.com/lLG60KQ.png"/>

I though of running `python bloodhoud` to gather information about the AD 

```bash
python3 /opt/Python-Bloodhound/bloodhound.py -d BLACKFIELD.local -u 'support' -p '#00^BlackKnight' -c all -ns 10.10.10.192
```

<img src="https://i.imgur.com/XIAALtz.png"/>

## Privilege Escalation (Audit2020)

On running some pre-built qurues on bloohouond GUI , I didn't find any path which I could use to escalate privileges

<img src="https://i.imgur.com/UzRv6NW.png"/>

But on checking what the support user has rights on outbound control

<img src="https://i.imgur.com/eFJV1Lt.png"/>

Which means that we can change `audit2020` password according to the password policy, so through `rpcclient` we can achieve this

<img src="https://i.imgur.com/LUZADwX.png"/>

<img src="https://i.imgur.com/yugvbg3.png"/>

Now we would have access to `Forensics/Audit Share`

<img src="https://i.imgur.com/8JerYXS.png"/>

<img src="https://i.imgur.com/XRNMDqS.png"/>

I had to download these files one by one because for some reason `mget *` didn't work , but it only had information about domain groups and users , nothing that we can do with

But there was another directory named `memory_analysis` 

<img src="https://i.imgur.com/Z1tYlN0.png"/>

<img src="https://i.imgur.com/f0BOrsZ.png"/>'

Which had `lsass.zip` , if you don't know what lsass  (Local Security Authority Subsystem Service) is , it's a process which locally holds the hashes of the users currently logged into the memory which can only be dumped if you have higher privileges or being an `Administrator`

## Privilege Escalation (svc_backup)

So after getting this file on local machine we can use `pypykatz` which is a mimikatz implementation in python , this can be installed by simply cloing the github repo 
https://github.com/skelsec/pypykatz and running `python3 setup.py install` .

After unzipping the `lsass.zip` we get `lsass.DMP` file which we can pass onto to pypykatz

```bash
/usr/local/bin/pypykatz lsa minidump lsass.DMP 
```

By analyizing the lsass dump process of memory we can get `svc_bakup`'s NT hash which we can use it to perform `pass the hash` to get a shell or access smb share, 

<img src="https://i.imgur.com/kYtRvFT.png"/>

<img src="https://i.imgur.com/JMjGThH.png"/>

We can also get Administrator's hash

<img src="https://i.imgur.com/3TpWkCF.png"/>

But this didn't worked maybe the password was changed after the dump 

<img src="https://i.imgur.com/E5ySVEC.png"/>

Using `evil-winrm` we can get a shell through WinRM

<img src="https://i.imgur.com/wsqSoHj.png"/>

Now to see in which groups this account is we can do `net user svc_backup`

<img src="https://i.imgur.com/VSvy4E3.png"/>

<img src="https://i.imgur.com/LGI0Ua9.png"/>

## Privilege Escalation (Administrator)

We can abuse the privilege as we have rights to take backup meaning that we can copy any file we want which lead us to copying `NTDS.dit` file which is located in `C:\Windows\NTDS\NTDS.dit` on the domain controller which is our target machine

Using `SePrivilegeBackup` dll files which can be found from this github repo

https://github.com/giuliano108/SeBackupPrivilege/tree/master/SeBackupPrivilegeCmdLets/bin/Debug
 
 After downloading them on target machine , import those two dll files
 
 <img src="https://i.imgur.com/pr7iLdo.png"/>
 
 But the issue when copying NTDS.dit is that it constantly is going to be used by windows processes
 
 <img src="https://i.imgur.com/5XuHZnM.png"/>
 
 So to counter this we need to create a shadow copy of the C drive and then copy the NTDS.dit file , to do that we need to create a text file that will define which drive we want to make a shadow copy of
 
```bash
set context persistent nowriters
set metadata C:\temp\metdata.cab
set verbose on
add volume C: alias uwu
create 
expose %uwu% f:
```

 <img src="https://i.imgur.com/6a1LVFj.png"/>

To make this compatible with windows as sometimes the formatting might cause an issue use `unix2dos`

<img src="https://i.imgur.com/9QuNUVR.png"/>

<img src="https://i.imgur.com/hm6zkPl.png"/>

Before running this make sure to create a folder in C drive , `mkdir temp` and then run it with `diskshadow`

<img src="https://i.imgur.com/tteoe9F.png"/>

Switching to `f:` drive we can see the contents of `C:` drive

<img src="https://i.imgur.com/7YvOnz9.png"/>

Using SeBackupPrivilege cmdlets we can copy the ntds.dit to the current directory and then download it on to our local machine

<img src="https://i.imgur.com/Y4PwwZ2.png"/>

Here I faced another issue and it was with evil-winrm , version 3.3 has some issues when downloading files and it just either hangs up showing no progress and says download or either fails by saying path error

<img src="https://i.imgur.com/A0wckHa.png"/>

I downloaded version 3.2 and used it to download this file

https://github.com/Hackplayers/evil-winrm/releases/tag/v3.2

<img src="https://i.imgur.com/2p27mYt.png"/>

<img src="https://i.imgur.com/KYl5n25.png"/>

Next we need is the `SYSTEM` file from registry hive

<img src="https://i.imgur.com/gIyMJV8.png"/>

<img src="https://i.imgur.com/pKyYkFN.png"/>

Now we just need to use impacket's `secretsdump.py` to read hashes from ntds file

<img src="https://i.imgur.com/KqBuny3.png"/>

<img src="https://i.imgur.com/fLXW6Fu.png"/>

## References

- https://malicious.link/post/2017/reset-ad-user-password-with-linux/
- https://www.whiteoaksecurity.com/blog/attacks-defenses-dumping-lsass-no-mimikatz/
- https://github.com/skelsec/pypykatz
- https://github.com/giuliano108/SeBackupPrivilege/tree/master/SeBackupPrivilegeCmdLets/bin/Debug
- https://youtu.be/pWkWIa2dfHY?t=1042
- https://pentestlab.blog/tag/ntds-dit/
- https://www.hackingarticles.in/windows-privilege-escalation-sebackupprivilege/
