# HackTheBox-Cascade

## NMAP

```bash

PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Microsoft DNS 6.1.7601 (1DB15D39) (Windows Server 2008 R2 SP1)
| dns-nsid:            
|_  bind.version: Microsoft DNS 6.1.7601 (1DB15D39)
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2021-12-26 11:29:46Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn  
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: cascade.local, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?                                          
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: cascade.local, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49154/tcp open  msrpc         Microsoft Windows RPC
49155/tcp open  msrpc         Microsoft Windows RPC
49157/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc         Microsoft Windows RPC
49170/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: CASC-DC1; OS: Windows; CPE: cpe:/o:microsoft:windows_server_2008:r2:sp1, cpe:/o:microsoft:windows
Host script results:
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2021-12-26T11:30:38
|_  start_date: 2021-12-26T11:26:31 

```


## PORT 139/445 (SMB)

We can try to see if there's null authentication on smb to see if we can list and access shares

<img src="https://i.imgur.com/GTloDvh.png"/>

Trying `enum4linux-ng` that would try to list usernames from RPC (Remote Procedure Call) using null authentication

<img src="https://i.imgur.com/vhEccPi.png"/>

<img src="https://i.imgur.com/KBfpTwo.png"/>

This could also be doing from `windapsearch` which is written in golang

<img src="https://i.imgur.com/ETWmgxB.png"/>

So we pretty much get the same results , let's use grep and awk to filter out usernames and save them in a file


```bash
/opt/windap/windapsearch-linux-amd64 -d cascade.local -m users | grep sAMAccountName | awk -F:' ' {'print $2'}
```

<img src="https://i.imgur.com/X1ywwRU.png"/>


Using `kerbrute` to see which ones are valid usernames and out of 15 users we get 11 users that are valid 

<img src="https://i.imgur.com/D7M1tPL.png"/>

Kerbrute does check for Pre-authenitcation disabled but just to be sure I used impacket's GetNPUsers script 

<img src="https://i.imgur.com/BVHleNN.png"/>

So I went on using `ldapsearch` to see if I can get some information out of users's properites like the last password being set or can be find the plain text passwords

```bash
ldapsearch -x -LLL -h 10.10.10.182 -D 'cn=USER,ou=users,dc=cascade,dc=local' -b "dc=cascade,dc=local" 
```

This shows us a ton of information but we can see the results in a file and use `grep` to filter our search

<img  src="https://i.imgur.com/lhtjF6M.png"/>

<img src="https://i.imgur.com/7ofDWDj.png"/>

```bash
cat ldap_info | grep cascade
```

I then just grep for `cascade` and found a base64 encoded text in a `cascadeLegacyPwd` field under `r.thompson` user

<img src="https://i.imgur.com/NvxuAUA.png"/>

On decoding the base64 text we can get a clear text , maybe this could be his password , so to verify it we can use kerbrute's `passwordspray`

<img src="https://i.imgur.com/y6mxXMt.png"/>

<img src="https://i.imgur.com/bVU2Gs2.png"/>

But we can only login to smb

<img src="https://i.imgur.com/WsxALJQ.png"/>

Having user credentials we can try to list any accounts that are associated with a SPN in but there weren't any accounts like that

<img src="https://i.imgur.com/OCzQtV1.png"/>

In the smb share we do we have some files that we can access

<img src="https://i.imgur.com/PWuQoKs.png"/>

I decided to come back at these shares and first enumrate the AD through python bloodhound-injestor

```bash
python3 /opt/Python-Bloodhound/bloodhound.py -d cascade.local -u 'r.thompson' -p 'rY4n5eva' -c all -ns 10.10.10.182
```

<img src="https://i.imgur.com/gUOJgok.png"/>

After getting those json file we need to import them to bloodhound GUI

<img src="https://i.imgur.com/6aKtDYT.png"/>

<img src="https://i.imgur.com/fztqRTg.png"/>

But I didn't find anything that we can do with this user

<img src="https://i.imgur.com/yLZDRKk.png"/>

All we can gather was  that `r.thompson` is a memeber of IT group

<img src="https://i.imgur.com/FihVSIq.png"/>

So going back to smb shares we see a folder named `IT` in `Data` share

<img src="https://i.imgur.com/JS3VgV2.png"/>

<img src="https://i.imgur.com/GZIgC7d.png"/>

I downloaded every file I could find from this directory

<img src="https://i.imgur.com/UfUuCbv.png"/>

Looking at the html file and I didn't get anything juicy

<img src="https://i.imgur.com/7DEzTwm.png"/>

So this was what we could gather as r.thompson, looking at `VNC install.reg` file there was a password in hex

<img src="https://i.imgur.com/QGgIAA7.png"/>

Looking at this article it seems that we can get the plain text password

https://www.raymond.cc/blog/crack-or-decrypt-vnc-server-encrypted-password/

I found a one liner for this to decrypt the vnc hex password to get plain text

```bash
echo -n 6bcf2a4b6e5aca0f | xxd -r -p | openssl enc -des-cbc --nopad --nosalt -K e84ad660c4721ae0 -iv 0000000000000000 -d | hexdump -Cv
 ```

<img src="https://i.imgur.com/r7oN1jL.png"/>

And with this we got smith's passsword

<img src="https://i.imgur.com/J6kTJgW.png"/>

Verifiying with crackmapexec to see if we can get a shelll through winrm

<img src="https://i.imgur.com/D5znG1J.png"/>

We can now use `evil-winrm` to get a shell as `s.smith` user

<img src="https://i.imgur.com/8YALx2W.png"/>

After gettting a shell one thing note is that this user is in `Audit Share` group and back when we listed the shares there was a share named `Audit$` but we weren't able to access it but now we can

<img src="https://i.imgur.com/j7Saugt.png"/>

Grabbing the `Audit.db` file we need to open this with `DB Browser For SQLite` which we can install it on ubuntu (it's available by default on kali linux) 

<img src="https://i.imgur.com/Ju0dvPO.png"/>

Here we can see the table names and the fields , to view the data in these table switch to `Browse Data`

<img src="https://i.imgur.com/5d6MyRJ.png"/>

`DeletedUserAudit` doesn't have anything here, switch the table to `Ldap` we see the same username that was in that html file and it's password which is encrpyted

<img src="https://i.imgur.com/oGn1Ru0.png"/>

<img src="https://i.imgur.com/VApDPIH.png"/>

From here we can't move forward only through using linux as we need to analyze the dll and the executable which can only be done through windows only (regretting for using dual boot )

So after switching to windows and downloading `dnspy` to analyze executables and dll files I was able to retrieve two strings , one was an ecrypted string and the other was the IV key


Opening the exe , we can navgiate to main module and see the secret key to decrypt the base64 string we already got from the db file 

<img src="https://i.imgur.com/F2tdHya.png"/>

<img src="https://i.imgur.com/E4ssU69.png"/>

Further more , opening the dll file , we can find IV key  and see that it's using CBC mode encryption

<img src="https://i.imgur.com/MQAXtpc.png"/>

I visited this site https://www.devglan.com/online-tools/aes-encryption-decryption as when trying on cyberchef I didn't understand what format I needed to specify as I was having difficulty in specifying the ouput to be in base64 so that site gave me the option clearly

<img src="https://i.imgur.com/W5dXUzV.png"/>

<img src="https://i.imgur.com/aQMMG0I.png"/>

And now all that is left is to decode this text from base64

<img src="https://i.imgur.com/GyurudI.png"/>

Using kerbrute again to check which user does this password belong to (although it's very clear but doing it anyways )

<img src="https://i.imgur.com/NvW9x6J.png"/>

Logging with this user , we can see that we are in `AD Recycle bin` group

<img src="https://i.imgur.com/Xru8Uax.png"/>

Now looking back at the meeting note , I understood what it meant , being in this group we need to recover the deleted object so when we get the password of `TempAdmin` we get the password for the `Administrator` account

<img src="https://i.imgur.com/RjeXfAC.png"/>

Searching for abusing this group , I found that we can read about deleted AD objects using AD management powershell module , so downloading the AD module from here

https://github.com/samratashok/ADModule

<img src="https://i.imgur.com/MXSyhGd.png"/>

After listing deleted objects we can see again `cascadelegacypwd` field which will show base64 encoded password 

<img src="https://i.imgur.com/D95dcQJ.png"/>

<img src="https://i.imgur.com/3jyOv5P.png"/>

Now the moment of truth, according to meeting notes we should be able to login as administrator account with this password

<img src="https://i.imgur.com/PlW6jR6.png"/>

Further we can dump hashes using impacket's `secretsdump.py`

<img src="https://i.imgur.com/qDtqx2Q.png"/>


## References

- https://www.raymond.cc/blog/crack-or-decrypt-vnc-server-encrypted-password/
- https://github.com/billchaison/VNCDecrypt
- https://linuxhint.com/install-sqlite-browser-ubuntu/
- https://github.com/dnSpy/dnSpy
- https://www.devglan.com/online-tools/aes-encryption-decryption
- https://github.com/samratashok/ADModule
- https://book.hacktricks.xyz/windows/active-directory-methodology/privileged-accounts-and-token-privileges
