# TryHackMe-Hacker Of The Hill

## Medium

### NMAP

```                 
PORT      STATE SERVICE       VERSION                  
80/tcp    open  http          Microsoft IIS httpd 10.0
| http-methods:                                                  
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: PhotoStore - Home                                           
81/tcp    open  http          Microsoft IIS httpd 10.0
| http-methods:                
|_  Potentially risky methods: TRACE                                      
|_http-server-header: Microsoft-IIS/10.0        
|_http-title: Network Monitor                                             
82/tcp    open  http          Microsoft IIS httpd 10.0
| http-methods:                                                           
|_  Potentially risky methods: TRACE                                      
|_http-server-header: Microsoft-IIS/10.0                         
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2021-03-07 17:02:28Z)
135/tcp   open  msrpc         Microsoft Windows RPC                    
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: troy.thm0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?                                             
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped                                                
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: troy.thm0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: TROY
|   NetBIOS_Domain_Name: TROY
|   NetBIOS_Computer_Name: TROY-DC
|   DNS_Domain_Name: troy.thm
|   DNS_Computer_Name: TROY-DC.troy.thm
|   DNS_Tree_Name: troy.thm
|   Product_Version: 10.0.17763
|_  System_Time: 2021-03-07T17:03:27+00:00
| ssl-cert: Subject: commonName=TROY-DC.troy.thm
| Not valid before: 2021-02-18T18:07:12
|_Not valid after:  2021-08-20T18:07:12
|_ssl-date: 2021-03-07T17:04:06+00:00; +35s from scanner time.
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49670/tcp open  msrpc         Microsoft Windows RPC
49671/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: TROY-DC; OS: Windows; CPE: cpe:/o:microsoft:windows
```

### PORT 139/445 (SMB)

<img src="https://imgur.com/jJQJmjr.png"/>

Didn't found any shares on the machine so now we have 3 http ports to enumerate

### PORT 80 (HTTP)

<img src="https://imgur.com/E8KPjxS.png"/>

I fuzzed for files and directory but found nothing interesting

<img src="https://imgur.com/iZWyLIQ.png"/>

We see a `sign-up` page

<img src="https://imgur.com/mNH5S7D.png"/>

On registering an account

<img src="https://imgur.com/3VQRg3W.png"/>

I uploaded an image having `.jpg` extension

<img src="https://imgur.com/HGsVv1m.png"/>

And could see full path of the image

<img src="https://imgur.com/o0AvsvE.png"/>

Also inspecting the source code we see that this using  javascript

<img src="https://imgur.com/y1fULEC.png"/>

<img src="https://imgur.com/IO555bb.png"/>

Now I used burpsuite to send this request to intruder so I could test for command injection but before doing it we need to block the javascript file which is filtering

<img src="https://imgur.com/4dAkyZy.png"/>

Make sure to check tick on `Disable Cache` and right click on `script.js` and select `block url` and refresh the page you will be able to use spaces in text field

<img src="https://imgur.com/IM06xcD.png"/>

We can now use ping command to verify command injeciton

<img src="https://imgur.com/0b4vg41.png"/>

<img src="https://imgur.com/nsI8Z7J.png"/>

<img src="https://imgur.com/LOEMxNw.png"/>

Using a powershell reverse shell I got rce to the machine

<img src="https://imgur.com/n5Kw9gG.png"/>

For convinince I generated a payload for getting a metepreter session

<img src="https://imgur.com/44gJFAG.png"/>

Ran `winPeas` but nothing interesting 

Also I tried to upload `BloodHound.ps1` to gather information about active directory

<img src="https://imgur.com/9SHL7Q8.png"/>

<img src="https://imgur.com/OvOFOmV.png"/>

`Invoke-Bloodhound -CollectionMethod All -Domain troy.thm -ZipFileName loot.zip`

<img src="https://imgur.com/zM1ZRfA.png"/>

Now I want this zip archive on my local machine so I could see what information it found

<img src="https://imgur.com/NWTkMMS.png"/>
The reason why I used metasploit : )

After having the zip archive on my local machine I started `bloodhound` and `neo4j`

<img src="https://imgur.com/9Oae3ah.png"/>

<img src="https://imgur.com/TH6RsdL.png"/>

Now simply drag and drop the zip archive it will automatically extract the archive and then you can run quries

On running the qurey `Find All Domain Admins`

<img src="https://imgur.com/WdrVCWj.png"/>

Then running `Kerberoastable accounts`

<img src="https://imgur.com/yYOhN4C.png"/>

`Kerberoastable accounts of high value`

<img src="https://imgur.com/ccJTHw9.png"/>

Download `rubeus.exe` 

https://github.com/r3motecontrol/Ghostpack-CompiledBinaries

<img src="https://imgur.com/PI4VaT4.png"/>

<img src="https://imgur.com/xMayFl4.png"/>

On running rubeus we will immediately get a hash

<img src="https://imgur.com/sFq3gIX.png"/>

<img src="https://imgur.com/pmT0uS8.png"/>

<img src="https://imgur.com/uNPeqtO.png"/>

Now we need to run hashcat against it and we are done because `achilles` is an administartor

<img src="https://imgur.com/mkDBbiX.png"/>

<img src="https://imgur.com/4CXNo89.png"/>

It cracks the hash 

<img  src="https://imgur.com/WQcdy6a.png"/>

Now we could either login with `RDP` ,`psexec` or with `evil-winrm`

### Evil-Winrm

<img src="https://imgur.com/Ke6ov5d.png"/>

### Psexec

<img src="https://imgur.com/ymx40bN.png"/>