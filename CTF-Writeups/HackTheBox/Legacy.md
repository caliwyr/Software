# HackTheBox-Legacy

## NMAP

```bash

PORT     STATE  SERVICE       VERSION                                                                                                               
139/tcp  open   netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open   microsoft-ds  Windows XP microsoft-ds                     
3389/tcp closed ms-wbt-server
Service Info: OSs: Windows, Windows XP; CPE: cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_xp                                                     
Host script results:                                                      
|_clock-skew: mean: 5d00h31m36s, deviation: 2h07m16s, median: 4d23h01m36s
| nbstat: NetBIOS name: LEGACY, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:b9:cc:42 (VMware)                                                    
| Names:                                                                  
|   LEGACY<00>           Flags: <unique><active>
|   HTB<00>              Flags: <group><active>                  
|   LEGACY<20>           Flags: <unique><active>                     
|   HTB<1e>              Flags: <group><active>                       
|   HTB<1d>              Flags: <unique><active>                  
|_  \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>                 
| smb-os-discovery:                                                       
|   OS: Windows XP (Windows 2000 LAN Manager)                             
|   OS CPE: cpe:/o:microsoft:windows_xp::-                                
|   Computer name: legacy                             
|   NetBIOS computer name: LEGACY\x00                                     
|   Workgroup: HTB\x00                                                    
|_  System time: 2021-05-18T01:01:14+03:00                                
| smb-security-mode:                                                      
|   account_used: guest                           
```

## PORT 139/445 (SMB)

Let's see if we can access any shares on the machine

<img src="https://imgur.com/tHZtw5N.png"/>

Seems like we can't so knowing this is a windows xp machine , it might be vulnerable to SMB exploit since this is a very old windows operating system , so let's run nmap `vuln` script to confirm the vulnerability.

```bash
nmap -p 445 --script vuln 10.10.10.4                                                                 
Starting Nmap 7.80 ( https://nmap.org ) at 2021-05-13 01:02 PKT                                                                                     
Nmap scan report for 10.10.10.4                                           
Host is up (0.19s latency).                                               
                                                                          
PORT    STATE SERVICE                                                                                                                               
445/tcp open  microsoft-ds                                                
|_clamav-exec: ERROR: Script execution failed (use -d to debug)           
                                                                          
Host script results:                                                      
|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED                       
| smb-vuln-ms08-067: 
|   VULNERABLE:
|   Microsoft Windows system vulnerable to remote code execution (MS08-067)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2008-4250
|           The Server service in Microsoft Windows 2000 SP4, XP SP2 and SP3, Server 2003 SP1 and SP2,
|           Vista Gold and SP1, Server 2008, and 7 Pre-Beta allows remote attackers to execute arbitrary
|           code via a crafted RPC request that triggers the overflow during path canonicalization.
|           
|     Disclosure date: 2008-10-23
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-4250
|_      https://technet.microsoft.com/en-us/library/security/ms08-067.aspx 
|_smb-vuln-ms10-054: false
|_smb-vuln-ms10-061: ERROR: Script execution failed (use -d to debug)
| smb-vuln-ms17-010: 

```

This confirms that this machine is vulnerable to smb exploit so here I'll show case using with and without metasploit

## Metasploit

This CVE for this exploit is MS08-067

<img src="https://imgur.com/qYIjQSk.png"/>

<img src="https://i.imgur.com/hlDuzVn.png"/>

Configure the options in the exploit

<img src="https://imgur.com/2y2hq9x.png"/>

<img src="https://imgur.com/0RZ7Ns3.png"/>

## Without Metasploit

Download the POC for MS 08-067 

<img src="https://imgur.com/JAa8Jzj.png"/>

Here we can see that it's using a shell code of msfvenom reverse shell payload so we need to generate one

<img src="https://imgur.com/VWr1TNl.png"/>

Replace the shellcode which is in the script

<img src="https://imgur.com/EikundA.png"/>

Now let's run the script

<img src="https://imgur.com/Jg6R9SU.png"/>

Here it says it needs the target IP and port also the version of windows xp so I ran the aggressive scan to know which version of windows xp is this and chances were that it is XP 3
<img src="https://i.imgur.com/T3uXpvg.png"/>

<img src="https://i.imgur.com/xPbhu3H.png"/>

And we get a shell 