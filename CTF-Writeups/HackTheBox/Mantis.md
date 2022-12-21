# HackTheBox-Mantis

## NMAP

```bash
PORT      STATE SERVICE      VERSION            
53/tcp    open  domain       Microsoft DNS 6.1.7601 (1DB15CD4) (Windows Server 2008 R2 SP1)
| dns-nsid:                                                            
|_  bind.version: Microsoft DNS 6.1.7601 (1DB15CD4)              
88/tcp    open  kerberos-sec Microsoft Windows Kerberos (server time: 2022-01-03 16:26:51Z)
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn             
389/tcp   open  ldap         Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds Windows Server 2008 R2 Standard 7601 Service Pack 1 microsoft-ds (workgroup: HTB)
464/tcp   open  kpasswd5?                                              
593/tcp   open  ncacn_http   Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
1337/tcp  open  http         Microsoft IIS httpd 7.5
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/7.5
|_http-title: IIS7
1433/tcp  open  ms-sql-s     Microsoft SQL Server 2014 12.00.2000.00; RTM
| ms-sql-ntlm-info: 
|   Target_Name: HTB
|   NetBIOS_Domain_Name: HTB
|   NetBIOS_Computer_Name: MANTIS
|   DNS_Domain_Name: htb.local
|   DNS_Computer_Name: mantis.htb.local
|_  Product_Version: 6.1.7601
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Issuer: commonName=SSL_Self_Signed_Fallback
| Public Key type: rsa
| Public Key bits: 1024
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2022-01-03T16:23:47
| Not valid after:  2052-01-03T16:23:47
| MD5:   c8ce e7c1 63c6 b69c f8ad 9227 769f b67c
|_SHA-1: 6810 c8c8 1e18 458d 4fd3 60d6 90b1 ca8e 5619 e790                        
|_ssl-date: 2022-01-03T16:28:00+00:00; 0s from scanner time.
3268/tcp  open  ldap         Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5722/tcp  open  msrpc        Microsoft Windows RPC
8080/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: Microsoft-IIS/7.5
|_http-title: Tossed Salad - Blog
9389/tcp  open  mc-nmf       .NET Message Framing
47001/tcp open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49155/tcp open  msrpc        Microsoft Windows RPC
49157/tcp open  ncacn_http   Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc        Microsoft Windows RPC
49164/tcp open  msrpc        Microsoft Windows RPC
49166/tcp open  msrpc        Microsoft Windows RPC
49172/tcp open  msrpc        Microsoft Windows RPC
50255/tcp open  ms-sql-s     Microsoft SQL Server 2014 12.00.2000
| ms-sql-ntlm-info: 
|   Target_Name: HTB
|   NetBIOS_Domain_Name: HTB
|   NetBIOS_Computer_Name: MANTIS
|   DNS_Domain_Name: htb.local
|   DNS_Computer_Name: mantis.htb.local
|   DNS_Tree_Name: htb.local
|_  Product_Version: 6.1.7601
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Issuer: commonName=SSL_Self_Signed_Fallback
Service Info: Host: MANTIS; OS: Windows; CPE: cpe:/o:microsoft:windows_server_2008:r2:sp1, cpe:/o:microsoft:windows
Host script results:
|_clock-skew: mean: 42m51s, deviation: 1h53m24s, median: 0s
| ms-sql-info: 
|   10.10.10.52:1433: 
|     Version: 
|       name: Microsoft SQL Server 2014 RTM
|       number: 12.00.2000.00
|       Product: Microsoft SQL Server 2014
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
| smb-os-discovery: 
|   OS: Windows Server 2008 R2 Standard 7601 Service Pack 1 (Windows Server 2008 R2 Standard 6.1)
|   OS CPE: cpe:/o:microsoft:windows_server_2008::sp1
|   Computer name: mantis
|   NetBIOS computer name: MANTIS\x00
|   Domain name: htb.local
|   Forest name: htb.local
|   FQDN: mantis.htb.local
|_  System time: 2022-01-03T11:27:49-05:00
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: required
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required

```

## PORT 139/445/389 (SMB/LDAP)

Running enum4linux to check null authentication on smb , ldap and rpc to enumerate usernames if possible

<img src="https://i.imgur.com/Y7hlwYJ.png"/>

<img src="https://i.imgur.com/Ey7ndVC.png"/>

<img src="https://i.imgur.com/kxxBPdS.png"/>

<img src="https://i.imgur.com/u1lqh0w.png"/>

And looks like that we are not successful here, running `smbclient` and `smbmap` also failed

<img src="https://i.imgur.com/8nbhwkN.png"/>

## PORT 1337 (HTTP)

This port gives us a IIS version 7 default page

<img src="https://i.imgur.com/tkRcfKi.png"/>

So running `gobuster` against this I didn't found anything interesting

<img src="https://i.imgur.com/4SKx2Ru.png"/>

And this gives us forbidden message that we can't access this directory

<img src="https://i.imgur.com/BZ70M7r.png"/>

So I just left running a gobuster on this port with the wordlist  `directory-list-2.3-medium.txt` and moved forward 

## PORT 8080 (HTTP)

Visting port 8080 , this shows a blog page

<img src="https://i.imgur.com/WwLAKML.png"/>

There's an option to add a comment in blog post , so let's try and see if there's xss here

<img src="https://i.imgur.com/jtJBhWB.png"/>

But nothing really happened , even the comment wasn't added , so gobuster to fuzz for files here I did found some directories

<img src="https://i.imgur.com/YGViaDl.png"/>

<img src="https://i.imgur.com/EX9bnXV.png"/>

<img src="https://i.imgur.com/qz0jjZo.png"/>

But these are two posts that we already saw on the main page, and the admin page would require us to enter credentials which we can just try the default ones like `admin:admin` but it didn't worked

<img src="https://i.imgur.com/58vgk4e.png"/>

Going back to the scan left on port 1337 it found a directory `secure_notes`

<img src="https://i.imgur.com/VfiNwVe.png"/>

<img src="https://i.imgur.com/mP4ctf7.png"/>

`web.config` file returned 404 but with text file we found some juicy information

<img src="https://i.imgur.com/Ejs795A.png"/>

Scrolling down below we can also find a password for orchid cms admin user which is in binary 

<img src="https://i.imgur.com/w5QYtph.png"/>

<img src="https://i.imgur.com/nwUw4AL.png"/>

Logging in with this password we can become admin on orchid user

<Img src="https://i.imgur.com/jykkDMf.png"/>

But being admin on orchid cms , there wasn't anything that we can abuse neither there were any exploits available that could give us code execution

<img src="https://i.imgur.com/7mX8bTN.png"/>

Notice that the file name we saw in secure_notes `dev_notes_NmQyNDI0NzE2YzVmNTM0MDVmNTA0MDczNzM1NzMwNzI2NDIx.txt.txt` , the text in the middle "NmQyNDI0NzE2YzVmNTM0MDVmNTA0MDczNzM1NzMwNzI2NDIx" this looks like some sort of encoding , using the magic feature of cyber chef this can identify and decode it 

<img src="https://i.imgur.com/D6Wf0oP.png"/>

Further decoding this from base64 to hex

<img src="https://i.imgur.com/wMEvmv8.png"/>

This decoded to a plain text which is mssql login password , we already saw the username from the text file which is `sa`, so using `crackmapexec` we can verify if we have correct credentials

<img src="https://i.imgur.com/UPqaGsK.png"/>

But these creds failed ,tried with admin user as well but no luck

<img src="https://i.imgur.com/N6YAXqt.png"/>

So switched to using metasploit module for mssql login and it worked ,it could be that the mssql version that the target machine is using is quite old for crackmapexec so that's why this module works

<img src="https://i.imgur.com/mZc1FyW.png"/>

There's a tool for linux called `sqsh` which works well with older version of mssql and it's a client for linux when interacting with sql

```bash
sqsh -S 10.10.10.52 -U 'admin' -P 'm$$ql_S@_P@ssW0rd!'
```

<img src="https://i.imgur.com/iI8XuLG.png"/>

After connecting with mssql we need to now run commands in order to select the database we want to use and then see which tables are there

```sql
select name from sys.databases
go
```

<img src="https://i.imgur.com/egh2rD3.png"/>

I tried listing tables in `orcharddb` but it wasn't in a good format and was un readable 

<img src="https://i.imgur.com/sOjnIbU.png"/>

<img src="https://i.imgur.com/Arm4owT.png"/>

Also tried to see if we can get command execution here but it failed

<img src="https://i.imgur.com/PHZakqp.png"/>

To counter this , I searched for GUI client for linux in order to connect to mssql and found `DBeaver`

<img src="https://i.imgur.com/6HsnuDb.png"/>

Installing the debian package for dbeaver

<img src="https://i.imgur.com/Bfb51Sr.png"/>

after it's installed , select the connection for SQL Server 

<img src="https://i.imgur.com/Oe5MBRE.png"/>

<img src="https://i.imgur.com/nK8qEOO.png"/>

Now we can see the databases easily so this is a really good tool to view databases, moving on , we can access `orcharddb`  and selecting the table `UserPartRecord` we can see the columns username and password so this seems promising as we may find potential username

Switching to data , we can see the admin user and james user 

<img src="https://i.imgur.com/SkHkcHt.png"/>

Trying to verify the login with crackmapexec it will fail as the cme may not support older version of smb 

<img src="https://i.imgur.com/3bUJttX.png"/>

However using `smbmap` we can see the shares and the permissions we have on them

<img src="https://i.imgur.com/IkF5CiE.png"/>

Running enum4linux just to check if we can enumerate usernames and groups on the machine

<img src="https://i.imgur.com/uohMVUC.png"/>

<img src="https://i.imgur.com/rqA5B1n.png"/>

Looking into NETLOGON , there wasn't anything there, SYSVOL Share had some policies files which just showed what privileges were enabled but it really wasn't interesting other than that just password policy files were there

So being an AD machine only thing that was coming into my mind was running bloodhound and since there's no winrm running we can't get just use sharphound powershell script so there's a python implementation for sharphound that collects information of AD and generates json files that we can import to bloodhound GUI

```bash
python3 /opt/Python-Bloodhound/bloodhound.py -d htb.local -u 'James' -p 'J@m3s_P@ssW0rd!' -c all -
ns 10.10.10.52
```

<img src="https://i.imgur.com/Ue9j6Zw.png"/>

<img src="https://i.imgur.com/blFrv7N.png"/>

Running the pre-built query `Shortest path to high level targets` we only see that this user can RDP into the machine but there's no RPD service running (port 3389) on the machine

As this machine is way old , judging from the MSSQL version and OS version being used ,the domain controller may also be vulnerable 

So a vulnerability exists in unpatched versions of windows AD servers which is known as `MS14-068` which escalates privileges of a normal user to an administrator or a nt authority \ system on the machine , there was a issue in validating singatures in  PAC (Privilege Attribute Certificate) as Domain controller wasn't able to validate invalid singature created by a valid domain user that can cause an attacker to give him the highest privileges by forging information in PAC to grant him higher privileges 

To abuse this attack there's an impacket script called `goldenPac.py` , so simply we need to just supply correct credentials and also to note that we need to specify the computer name as well else it won't work


<img src="https://i.imgur.com/o4QJgbq.png"/>

Without specifying the computer name it gives an error

<img src="https://i.imgur.com/3MvWwph.png"/>

So adding the computer name in `/etc/hosts` file 

<img src="https://i.imgur.com/gwtioIg.png"/>

And with the computer name the exploit works , we can dump hashes as well from NTDS.dit , to do this add `James` to `Administrators` group

<img src="https://i.imgur.com/AYEfza0.png"/>


Also just to get a powershell session we need to enable WinRM service as well

<img src="https://i.imgur.com/EXW7ns9.png"/>

To verify that we can reach to that port 

<img src="https://i.imgur.com/HZehGHo.png"/>

Using `secretsdump.py` which is also a part of impacket which can be used to dump hashes from either SAM or NTDS.dit 

<img src="https://i.imgur.com/jiAUnBr.png"/>

<img src="https://i.imgur.com/b3ITq7k.png"/>

<img src="https://i.imgur.com/EDKYk0b.png"/>

## References

- https://www.rapid7.com/db/modules/auxiliary/scanner/mssql/mssql_login/
- https://noraj.gitlab.io/the-hacking-trove/Tools/sqsh/
- https://www.sqlshack.com/working-sql-server-command-line-sqlcmd/
- https://askubuntu.com/questions/788197/graphical-ms-sql-clients-for-a-ubuntu-desktop
- https://wizard32.net/blog/knock-and-pass-kerberos-exploitation.html
- https://adsecurity.org/?p=525
