# TryHackMe-Anonymous

## NMAP

```
Nmap scan report for 10.10.126.173                                                                                                                  
Host is up (0.41s latency).                                                                                                                         
Not shown: 996 closed ports          
PORT    STATE SERVICE     VERSION                                         
21/tcp  open  ftp         vsftpd 2.0.8 or later                                                                                                     
| ftp-anon: Anonymous FTP login allowed (FTP code 230)                    
|_drwxrwxrwx    2 111      113          4096 Jun 04  2020 scripts [NSE: writeable]                                                                  
| ftp-syst:                          
|   STAT:                                                                 
| FTP server status:                 
|      Connected to ::ffff:10.2.54.209                                    
|      Logged in as ftp                                                   
|      TYPE: ASCII                   
|      No session bandwidth limit                                         
|      Session timeout in seconds is 300                                  
|      Control connection is plain text                                   
|      Data connections will be plain text                                
|      At session startup, client count was 4                             
|      vsFTPd 3.0.3 - secure, fast, stable                                
|_End of status                                                           
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                              
| ssh-hostkey:                                                            
|   2048 8b:ca:21:62:1c:2b:23:fa:6b:c6:1f:a8:13:fe:1c:68 (RSA)                                                                                      
|   256 95:89:a4:12:e2:e6:ab:90:5d:45:19:ff:41:5f:74:ce (ECDSA)                                                                                     
|_  256 e1:2a:96:a4:ea:8f:68:8f:cc:74:b8:f0:28:72:70:cd (ED25519)                                                                                   
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)                                                                               
445/tcp open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)                                                                            
Service Info: Host: ANONYMOUS; OS: Linux; CPE: cpe:/o:linux:linux_kernel 
Host script results:                 
|_clock-skew: mean: 0s, deviation: 1s, median: -1s                        
|_nbstat: NetBIOS name: ANONYMOUS, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)                                                        
| smb-os-discovery:                  
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)                                  
|   Computer name: anonymous         
|   NetBIOS computer name: ANONYMOUS\x00                                  
|   Domain name: \x00                
|   FQDN: anonymous                  
|_  System time: 2020-12-11T21:44:31+00:00                                
| smb-security-mode:                 
|   account_used: guest              
|   authentication_level: user                                            
|   challenge_response: supported                                         
|_  message_signing: disabled (dangerous, but default)                    
| smb2-security-mode:                
|   2.02:                            
|_    Message signing enabled but not required                            
| smb2-time:                         
|   date: 2020-12-11T21:44:31                                             
|_  start_date: N/A                  

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                                                      
Nmap done: 1 IP address (1 host up) scanned in 54.45 seconds                                 s
```

From the nmap scan we can anonymously login into ftp since it's enabled

## FTP (PORT 21)

<img src="https://imgur.com/lgkDur4.png"/>

<img src="https://imgur.com/orbnWlZ.png"/>

These are the files that we see on the ftp server

<img src="https://imgur.com/Vc3APQQ.png"/>

There wasn't anything on the ftp server so just a Rabbit Hole...but there is another port open which is `SMB` on port 445 and by running `smbmap` to check if `anonymous` user read any share

<img src="https://imgur.com/Rwq5D7A.png"/>

So it looks like we can read share `pics` on the box , now we are going to use `smbclient` to access that share

<img src="https://imgur.com/v2TfQwl.png"/>

We only have two image files `.jpg` and `.jpeg` 

<img src="https://imgur.com/nw9vyJk.png"/>

And through `strings` and `steghide` I couldn't find anything, But then I thought about that ftp server and went back and it had all permissions setup means  that we can write files on it so I edited the `clean.sh` and put a bash reverse sehll in it

<img src="https://imgur.com/XUoA7M5.png"/>

Then putted it on the ftp server and I saw that `removed_files.log` is modified so when downloaded it to see what changes happened it I got a reverse shell on my netcat 

Now I ran a find command to look for SUID's 

<img src="https://imgur.com/QTu3Vtv.png"/>

<img src="https://imgur.com/rJpXRGd.png"/>

Here I found that `env` has a SUID so I visited `GTFOBIN` to see I can become root with it

<img src="https://imgur.com/zR9e4PF.png"/>

So we can become root , let's put this into practice

<img src="https://imgur.com/H72GLZQ.png"/>

This could have also been done with `lxd` but for that you have to make image , transfer to target then run 4-5 commands and I was lazy to do that so we got root that's the only thing that matters ( :
