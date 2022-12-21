# TryHackMe-Anthem

## NMAP

```
tats: 0:01:37 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan                                                                          
NSE Timing: About 97.50% done; ETC: 20:14 (0:00:00 remaining)                                                                                       
Nmap scan report for 10.10.109.113                                        
Host is up (0.19s latency).                                                                                                                         
Not shown: 995 closed ports                                                                                                                         
PORT     STATE SERVICE       VERSION                                                                                                                
80/tcp   open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)                                                                                
135/tcp  open  msrpc         Microsoft Windows RPC                                                                                                  
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn                                                                                          
445/tcp  open  microsoft-ds?                                              
3389/tcp open  ms-wbt-server Microsoft Terminal Services                                                                                            
| rdp-ntlm-info:                                                          
|   Target_Name: WIN-LU09299160F                                          
|   NetBIOS_Domain_Name: WIN-LU09299160F                                  
|   NetBIOS_Computer_Name: WIN-LU09299160F                                
|   DNS_Domain_Name: WIN-LU09299160F                                      
|   DNS_Computer_Name: WIN-LU09299160F                                                                                                              
|   Product_Version: 10.0.17763                                           
|_  System_Time: 2020-10-25T15:13:32+00:00                                
| ssl-cert: Subject: commonName=WIN-LU09299160F                                                                                                     
| Not valid before: 2020-10-24T15:12:24                                                                                                             
|_Not valid after:  2021-04-25T15:12:24                                   
|_ssl-date: 2020-10-25T15:14:42+00:00; 0s from scanner time.                                                                                        
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows                                                                                            
                                     
Host script results:                                                      
| smb2-security-mode:                
|   2.02:                                                                 
|_    Message signing enabled but not required                            
| smb2-time:                         
|   date: 2020-10-25T15:13:32                                                                                                                       
|_  start_date: N/A                                                                                                                                 
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                                                      
Nmap done: 1 IP address (1 host up) scanned in 97.59 seconds                                  
```

## SMB

```
smbclient -L \\\\10.10.109.113\\
Enter WORKGROUP\root's password: 
session setup failed: NT_STATUS_ACCESS_DENIED
```

That's dead end 

## PORT 80

<img src="https://imgur.com/6MSUuT8.png"/>

On the page source we can find a flag of some sort 
<img src="https://imgur.com/rcMo4ig.png"/>

<img src="https://imgur.com/4S7GBX8.png"/>

 
`UmbracoIsTheBest!` potential password 
`JD@anthem.com` email address at `http://10.10.109.113/archive/we-are-hiring/`

## Gobuster

```
===============================================================                                                                               [9/21]
Gobuster v3.0.1       
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.109.113
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1                                                                                                                  
[+] Timeout:        10s                                                                                                                             
===============================================================                                                                                     
2020/10/25 20:20:30 Starting gobuster                                                                                                               
===============================================================                                                                                     
/search (Status: 200)                                                                                                                               
/blog (Status: 200)                                                                                                                                 
/sitemap (Status: 200)                                                                                                                              
/rss (Status: 200)                                                                                                                                  
/archive (Status: 301)                                                                                                                              
/categories (Status: 200)
/authors (Status: 200)                                                                                                                              
/Search (Status: 200)                                                                                                                               
/tags (Status: 200)
/install (Status: 302)             
/RSS (Status: 200)
/Blog (Status: 200)
/Archive (Status: 301)
/SiteMap (Status: 200)
/siteMap (Status: 200)
/INSTALL (Status: 302)
/Sitemap (Status: 200)
/1073 (Status: 200)
/Rss (Status: 200)
/Categories (Status: 200)

```
## CMS 

<img src="https://imgur.com/lsGPuhu.png"/>

For getting the name of admin visit the page there is a poem written , search on goolge to find who wrote this poem 

<img src="https://imgur.com/5DjsIBe.png"/>

<img src="https://imgur.com/DyFe1Kr.png"/>

We peviously found `JD@anthem.com` the hint says that `There is another email address on the website that should help us figuring out the email pattern used by the administrator.`

<img src="https://imgur.com/wRKtDx5.png"/>


So admin is Solomon Grundy and carfting the email like the pattern above `sg@anthem.com` will let us login with the credentials `UmbracoIsTheBest!`

## PORT 3389 (RDP)

Launch `Remmina` with the credentials username as `sg` and passowrd `UmbracoIsTheBest!`


### User Flag
<img src="https://imgur.com/QdV7VKa.png"/>

### Root Flag

Turn on the option for `show hidden files` as the hints says that admin's password is hidden.

<img src="https://imgur.com/CKnN3Dh.png"/>

You can find a folder named `backup` and in thier `restore.txt` but you don't have rights to view this file.
<img src="https://imgur.com/tGcOFjY.png"/>


What you could do is right click on properites and change but I'll show how you can do this with cmd.

<img src="https://imgur.com/l0SvZgT.png"/>

When try to view it will show you that you don't have permissions so,

<img src="https://imgur.com/qmMge2x.png"/>

`ChangeMeBaby1MoreTime`


<img src="https://imgur.com/mAvxb4j.png"/>

<img src="https://imgur.com/XIweE75.png"/>s

## Flags

Flag 1 `THM{L0L_WH0_US3S_M3T4}` On html boiler plate `http://10.10.109.113/archive/we-are-hiring/`

Flag 2 `THM{G!T_G00D}` in body of html  `http://10.10.109.113`

Flag 3 `THM{L0L_WH0_D15`} `http://10.10.109.113/authors`

Flag 4 `THM{AN0TH3R_M3TA}` `http://10.10.109.113/archive/a-cheers-to-our-it-department/`