# HackTheBox-Granny

## NMAP

```bash

PORT   STATE SERVICE REASON          VERSION                                                                                                        
80/tcp open  http    syn-ack ttl 127 Microsoft IIS httpd 6.0
| http-methods:                                           
|   Supported Methods: OPTIONS TRACE GET HEAD DELETE COPY MOVE PROPFIND PROPPATCH SEARCH MKCOL LOCK UNLOCK PUT POST
|_  Potentially risky methods: TRACE DELETE COPY MOVE PROPFIND PROPPATCH SEARCH MKCOL LOCK UNLOCK PUT                                               
| http-ntlm-info:                                                         
|   Target_Name: GRANNY                                     
|   NetBIOS_Domain_Name: GRANNY                                           
|   NetBIOS_Computer_Name: GRANNY                                         
|   DNS_Domain_Name: granny                                               
|   DNS_Computer_Name: granny                                     
|_  Product_Version: 5.2.3790                           
|_http-server-header: Microsoft-IIS/6.0
| http-webdav-scan:                  
|   Public Options: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, POST, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, SEARCH
|   Allowed Methods: OPTIONS, TRACE, GET, HEAD, DELETE, COPY, MOVE, PROPFIND, PROPPATCH, SEARCH, MKCOL, LOCK, UNLOCK
|   Server Type: Microsoft-IIS/6.0                                        
|   WebDAV type: Unknown             
|_  Server Date: Wed, 26 May 2021 15:53:30 GMT                            

```

## PORT 80 (HTTP)

<img src="https://imgur.com/a2c68mM.png"/>

As seen from the nmap scan , this web server is using IIS 6.0 version which might havev some vulnerabilites since it's old


## Using Metasploit

On googling around exploits for IIS 6.0 I found a metasploit module

<img src="https://imgur.com/TrmXjnl.png"/>

So use the metasploit module and configure the options

<img src="https://imgur.com/yPowb83.png"/>

<img src="https://imgur.com/UncUyLv.png"/>

Right now we are not a privileged user so we need to find a way to escalate our privileges so let's run `whoami /all`

<img src="https://i.imgur.com/Jtcm9HL.png"/>

We can see Seimpersonate privleges is on , what  Seimperonsate is that a local admin can impersonate himself to a logged user but here a service account has these privileges so we can abuse these to create a token which will enable us switch user to admin

<img src="https://i.imgur.com/6Zd9geT.png"/>

Since this is a windows server 2003 operating system we are going to search for abusing the privileges for this particular system


<img src="https://imgur.com/lOdyVqP.png"/>

We can see the file `churrasco` which we can use to abuse impersonate privileges

<img src="https://imgur.com/XfgRuhF.png"/>

Now to upload this on the target machine I had some problems while doing it as powershell was not available so we cannot use it's functionality to download files also `curl` wasn't available too , `certutil` was also giving problems

<img src="https://i.imgur.com/eIItkUJ.png"/>

I then just used functionality of meterpreter to upload files and it worked like a charm

<img src="https://i.imgur.com/q1793f6.png"/>

But I forogt to allow downloading malicious files as firefox gave a warningthat's why  showing it's empty so let's download it again


https://github.com/Re4son/Churrasco/raw/master/churrasco.exe

To run commands through this exe `churrasco.exe -d` after that the command we want to run as SYSTEM

<img src="https://i.imgur.com/H7CXxgB.png"/>

<img src="https://imgur.com/r0XG0LZ.png"/>

I get a connection back didn't get a shell

<img src="https://imgur.com/h6Ng31S.png"/>

And I soon reliazed my mistake that I didn't provide `-e` argument to invoke `cmd.exe` on getting a connection,so let's run it again

<img src="https://i.imgur.com/LBDzywu.png"/>

<img src="https://i.imgur.com/LBDzywu.png"/>

And now we got a shell as SYSTEM
