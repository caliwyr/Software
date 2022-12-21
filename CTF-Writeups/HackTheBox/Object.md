# HackTheBox-Object

## NMAP

```bash
PORT     STATE SERVICE VERSION
80/tcp   open  http    Microsoft IIS httpd 10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Mega Engines
5985/tcp open  http    Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
8080/tcp open  http    Jetty 9.4.43.v20210629
|_http-favicon: Unknown favicon MD5: 23E8C7BD78E8CD826C5A6073B15068B1
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Jetty(9.4.43.v20210629)
|_http-title: Site doesn't have a title (text/html;charset=utf-8).
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

```

## PORT 80 (HTTP)

<img src="https://i.imgur.com/tGujaU4.png"/>

On port 80 we can see a domain name `object.htb` so let's add this domain name in `/etc/hosts` file and start fuzzing for files and directories using `gobuster` also it tells about to "login and submit code on the automation server" which is running at port 8080

<img src="https://i.imgur.com/wycpaUd.png"/>

Gobuster didn't find anything so next we can enumerate for subdomains

<img src="https://i.imgur.com/Xb9q51F.png"/>

I kept running `wfuzz` so while it's running we can look at port 8080, on this port we have an instance on jenkins running 


## PORT 8080 (HTTP)

<img src="https://i.imgur.com/Ie65x9w.png"/>

I tried the default admin:admin credentials but it didn't work so we can just create an account

<img src="https://i.imgur.com/jBOuUzP.png"/>

<img src="https://i.imgur.com/nAFhhwO.png"/>

<img src="https://i.imgur.com/XjIZFgk.png"/>

We are logged and on bottom right corner we can see the version of jenkins which is `2.317`

Also there wasn't any subdomain which wfuzz found

<img src="https://i.imgur.com/In21HsK.png"/>

So we can make a Freestyle project by going to `New Item`

<img src="https://i.imgur.com/kq5h86P.png"/>

After naming the project you'll be presented to Build Triggers, Build Environment, Source code management and etc. Select `Build Triggers `and then select `Build periodically` , it will allow to create a schedule task which you can configure similar to a cron job and this will start building your project, we can configure the job to run after a minute `* * * * *`

https://stackoverflow.com/questions/12472645/how-do-i-schedule-jobs-in-jenkins

<img src="https://i.imgur.com/77yaHff.png"/>

Next under Build, we can see an option for Add Build step in which we can select `Execute Windows Batch command`

<img src="https://i.imgur.com/LhJKUOd.png"/>

Going back to dashboard we can see a successful build 

<img src="https://i.imgur.com/P57GPSN.png"/>

<img src="https://i.imgur.com/GfRZXzH.png"/>

This shows that we are executing commands as `oliver`

So next I tried to see if I can ping my machine from here

<img src="https://i.imgur.com/rykIM06.png"/>

<img src="https://i.imgur.com/iBDPXa8.png"/>

We can so now let's transfer nc64.exe on this machine 

<img src="https://i.imgur.com/b6h2JWb.png"/>

<img src="https://i.imgur.com/6k2M5ot.png"/>

But it wasn't able to make a connection to this port

<img src="https://i.imgur.com/FvlQimP.png"/>

So I changed the port to 9001 and it still didn't make a connection 

<img src="https://i.imgur.com/yGKTZrB.png"/>

It could be that there's a firewall configure to not allow any outbound traffic, so we can use powershell's cmdlet `Get-NetFirewallRule` to list firewall rules and we need to check for outbound

```bash
cmd.exe /c powershell.exe -c Get-NetFirewallRule -Action Block -Enabled True -Direction Outbound

```

<img src="https://i.imgur.com/i89GL7o.png">

So we can't get a reverse shell as the traffic won't go out , next we can do is look where jenkins stores passwords or how it stores them so we can retrieve and decrpyt those, I found a question asked on stackoverflow about this

<img src="https://i.imgur.com/4vNrCGx.png"/>

https://stackoverflow.com/questions/39340322/how-to-reset-the-user-password-of-jenkins-on-windows

Looking for a decrpytor for passwords I found a github repo which was go script

https://github.com/hoto/jenkins-credentials-decryptor

<img src="https://i.imgur.com/vyO0aj8.png"/>

And this wants `credentials.xml`,  `master.key` and `hudson.util.Secret`

<img src="https://i.imgur.com/jErsujH.png"/>

We still don't see a credentials.xml file , so to transfer these on our machine we need to base64 encode this and then read those files 

<img src="https://i.imgur.com/RKtj2CT.png"/>

Now we can just decode them from base64 and get the original file

<img src="https://i.imgur.com/R6YHBb9.png"/>

<img src="https://i.imgur.com/hqFDGgp.png"/>

But still we need to credentials.xml file but couldn't find on the box, so looking into directories there was a folder named `users`

<img src="https://i.imgur.com/fBRaKp2.png"/>

There's a `config.xml` so let's just grab it and see if it's of any use for us

<img src="https://i.imgur.com/NjcwjLf.png"/>

<img src="https://i.imgur.com/daONweg.png"/>

It wasn't what we needed so going into admin's folder might be something what we need 

<img src="https://i.imgur.com/GwwG9ja.png"/>

## Foothold

Now we see another config file, so there's no need to encode it we can just read this as it will be in plain text

<img src="https://i.imgur.com/326df0D.png"/>

<img src="https://i.imgur.com/VzNtA2z.png"/>

So this is contains the hashed password that we can crack using the tool we found on github

<img src="https://i.imgur.com/zcFuIdK.png"/>

Like this we were able to recover the plain text password which is `c1cdfun_d2434`, since winrm is open on the machine we can just use this password for oliver user and get a shell on the machine

<img src="https://i.imgur.com/Y1Naw0A.png"/>

Looking at `C:\Users` we do see other users as well

<img src="https://i.imgur.com/EKsMMIu.png"/>

We can check for local ports on the machine by running `nestat -aof`

<img src="https://i.imgur.com/eQdeB9v.png"/>

Port 88 being open on this machine tells us that it's an active directory machine and this is a domain controller as kerberos runs on a DC.

So to enumerate the AD domain we need to somehow transfer `sharphound.exe` on the machine so we can gather information about the domain, thankfully we can upload files through evil-winrm with it's `upload` feature (also to note that I am using evil-winrm v 3.2 as the recent one was using having issues with uploading and downloading files )

<img src="https://i.imgur.com/y6mkG9H.png"/>

We can get the domain name by running `$env:USERDNSDOMAIN`

<img src="https://i.imgur.com/FWcfQnA.png"/>

```bash
SharpHound.exe --domain object.local --CollectionMethod all --domaincontroller 127.0.0.1
```

<img src="https://i.imgur.com/SEFoiOZ.png"/>

Giving the absolute path to zip archive we can download the file to our machine (remember that downloading only works with absolute path)

<img src="https://i.imgur.com/ICRmst1.png"/>

Start bloohound by running neo4j first and then bloodhoud GUI and upload the json files from the zip archive

<img src="https://i.imgur.com/cQ9oovZ.png"/>

Running any of the pre-build query we can see the data is loaded and it returns the result

<img src="https://i.imgur.com/jZh9ZO5.png"/>

We can search for oliver node and mark it as owned so we can look for paths to gain privileges

<img src="https://i.imgur.com/W0CcB3G.png"/>

## Privilege Escalation (Smith)

Running the query shortest path to domain admin, we can see a path from oliver to smith that we can change smith's password, further `smith` has write options on `maria` user object  and maria is a writeowner of domain admin

<img src="https://i.imgur.com/dgqghpp.png"/>

I tried to change smith's password with `net user ` but it didn't work

<img src="https://i.imgur.com/X7Z8bVo.png"/>

We could try to use powerview module to do that which is suggested in bloodhound help to abuse `ForceChangePassword`

<img src="https://i.imgur.com/0KMdqKB.png"/>

<img src="https://i.imgur.com/LmWjCLG.png"/>

And now to login as smith 

<img src="https://i.imgur.com/950Xdxo.png"/>

Now to abuse `GenericWrite`, we can make this user account a SPN to get a TGS ticket 

<img src="https://i.imgur.com/QQ6yPNq.png"/>

I followed the abuse described in bloodhound

<img src="https://i.imgur.com/mLbZWIo.png"/>

<img src="https://i.imgur.com/EaDe58o.png"/>

This added a SPN to this user account, but when I tried to kerberoast it didn't work

<img src="https://i.imgur.com/HFGFiFR.png"/>

We still can abuse this by setting up a logon script, this will execute when maria will logon to the machine 

https://www.thehacker.recipes/ad/movement/access-controls/logon-script

## Privilege Escalation (Maria)

So using powerview's module we can use 

```powershell
Set-DomainObject -Identity maria -SET @{scriptpath="C:\ProgramData\logonscript.ps1"}
```

This will execute the powershell script which will list the contents in Desktop folder of maria, I did however tried to change maria's password through `net user maria Password123!` but this didn't work

```powershell
dir C:\Users\maria\Desktop > C:\ProgramData\dir_result.txt
```

<img src="https://i.imgur.com/YIJH6Vi.png"/>

<img src="https://i.imgur.com/tnZvkr0.png"/>


<img src="https://i.imgur.com/iHHLC7p.png"/>

We can see a text has been created which shows that there's an execl file in Desktop folder of maria user

<img src="https://i.imgur.com/FCxcWEU.png"/>

Now just replace the current command in the ps1 script with this 

```powershell
copy C:\Users\maria\Desktop\Engines.xls C:\ProgramData\
```

And we'll get the excel file in ProgramData

<img src="https://i.imgur.com/6Qxsm1E.png"/>

Download the file

<img src="https://i.imgur.com/soBA9AW.png"/>

On opening the excel document we can see three passwords for maria user

<img src="https://i.imgur.com/RL2CKvm.png" />

So I made a list of these three passwords and use `crackmapexec` to brute force password for maria user

<img src="https://i.imgur.com/Of6n5uQ.png"/>

This shows a `Pwn3d!`status meaning that we can get a shell

<img src="https://i.imgur.com/Ks4qkPv.png"/>

Now going back to bloodhound GUI we can see the `WriteOwner` on `Domain Admins ` group

https://book.hacktricks.xyz/windows/active-directory-methodology/acl-persistence-abuse

```powershell
Set-DomainObjectOwner -Identity "Domain Admins" -OwnerIdentity maria
```

<img src="https://i.imgur.com/5gi02VL.png"/>

So now we have set the object owner of the group domain admins to maria and we now have to grant all permissions on this object

```powershell
Add-DomainObjectAcl -TargetIdentity "Domain Admins" -PrincipalIdentity maria -Rights All
```

Now add maria user to this domain admins group

```powershell
Add-DomainGroupMember -Identity 'Domain Admins' -Members 'maria'
```

<img src="https://i.imgur.com/IbZvGva.png"/>

<img src="https://i.imgur.com/yc3NyCJ.png"/>

We can see that we are a memeber of domains admins group so we can read the root and user flag but you need to login again because the changes will be effected after you login again

<img src="https://i.imgur.com/eCZC5dt.png"/>

<img src="https://i.imgur.com/9zaN9mA.png"/>

## References
- https://stackoverflow.com/questions/12472645/how-do-i-schedule-jobs-in-jenkins
- http://woshub.com/manage-windows-firewall-powershell/
- https://stackoverflow.com/questions/39340322/how-to-reset-the-user-password-of-jenkins-on-windows
- https://github.com/hoto/jenkins-credentials-decryptor
- https://shellgeek.com/get-domain-name-using-powershell-and-cmd/
- https://cheatsheet.haax.fr/windows-systems/network-and-domain-recon/domain_mapping/
- https://www.thehacker.recipes/ad/movement/access-controls/logon-script
- https://book.hacktricks.xyz/windows/active-directory-methodology/acl-persistence-abuse
