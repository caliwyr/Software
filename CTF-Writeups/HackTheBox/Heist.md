# HackTheBox-Heist

## NMAP

```bash
PORT      STATE SERVICE       REASON          VERSION                     
80/tcp    open  http          syn-ack ttl 127 Microsoft IIS httpd 10.0
| http-cookie-flags:                                                      
|   /:                                                                    
|     PHPSESSID:                                                          
|_      httponly flag not set                                             
| http-methods:                                                           
|   Supported Methods: OPTIONS TRACE GET HEAD POST                                 
|_  Potentially risky methods: TRACE                                      
|_http-server-header: Microsoft-IIS/10.0                                  
| http-title: Support Login Page
|_Requested resource was login.php                                        
135/tcp   open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
445/tcp   open  microsoft-ds? syn-ack ttl 127                             
5985/tcp  open  http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)                                                               
|_http-server-header: Microsoft-HTTPAPI/2.0                               
|_http-title: Not Found                                                   
49669/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows                  
```

## PORT 445 (SMB)
Since smb service is running we can see if anonymous login is enabled on smb or not

<img src="https://i.imgur.com/H24u5mJ.png"/>

Looks like it isn't so let's move on to port 80

## PORT 80

On the webserver we can see a login page

<img src="https://i.imgur.com/acn2kXJ.png"/>

So let's try the usual `admin:admin`

<img src="https://i.imgur.com/7S8jup0.png"/>

But this asks us to enter email address , there's login as guest option available to us so let's see what it does

<img src="https://i.imgur.com/pG2eYsZ.png"/>

<img src="https://i.imgur.com/bQRcYfO.png"/>

In parallel I started running `gobuster`

<img src="https://i.imgur.com/edI1Zoj.png"/>

It seems there's nothing interesting that I found so on viewing the attachment `Hazard` sent 

<img src="https://i.imgur.com/ulAtsyw.png"/>

We can see a Cisco IOS MD5 hash and two ciso type 7 passwords use a very weak algorithm that can be easily reversed, so going to a online tool for decrypting the two passwords

<img src="https://i.imgur.com/L9zQ5YV.png"/>

<img src="https://i.imgur.com/t9iGp1X.png"/>

Also we have 3 usernames `rout3r` , `Hazard` and `admin`  and we got two decrpyted passwords except for the hash, so let's try to brute force for that I'll make a wordlist for usernames and passwords ,for brutefocring I used `crackmapexec` against smb.

<img src="https://i.imgur.com/Q7cJDtR.png"/>

So it failed maybe we do need to crack that hash, so let's fire up `hashcat` and crack that hash, we can see the hash format number from hashcat examples wiki page

<img src="https://i.imgur.com/JRKO8Sy.png"/>

<img src="https://i.imgur.com/8LdMZ7q.png"/>

<img src="https://i.imgur.com/k4HgfO5.png"/>

Awesome we cracked the hash ,let's add this to our passwords wordlist and see if this makes a difference

<img src="https://i.imgur.com/iyAJ6jC.png"/>

Nice ,we got the correct credenitals let's try to access smb and see how many shares are there

<img src="https://i.imgur.com/bWv6dxl.png"/>

We can only access `IPC` share , I don't know if that would be much of a use for us, so now I was only left with running `enum4linux-ng` since we have the creds for smb we can run it now 

<img src="https://i.imgur.com/eeYHH78.png"/>

<img src="https://i.imgur.com/iy21uMM.png"/>

Now we got bunch of usernames so we can try brute forcing on both smb and winrm porotocol

<img src="https://i.imgur.com/PozK4hp.png"/>

It shows that status `pwned` so it means we can get a shell , we can use evil-winrm to login to target machine using the credentials

<img src="https://i.imgur.com/JUSOfQI.png"/>

I first decided to look for running processes and found `firefox` to be running

<img src="https://i.imgur.com/btimN6x.png"/>

So maybe firefox may have saved credentials so we need to go to the path where firefox files are stored under a user

<img src="https://i.imgur.com/btimN6x.png"/>

Now we have to transfer these files on to our machine , luckily evil-winrm supports downloading files or folders just by specifying `download` and then the file/folder name

<img src="https://i.imgur.com/x4fIK1x.png"/>

I searched for a tool that can recover or decrypt passwords from firefox files and I found a python script on github

https://github.com/lclevy/firepwd

<img src="https://i.imgur.com/kBBkoqt.png"/>

But I ran into some errors

<img src="https://i.imgur.com/3xf6Oj2.png"/>

I then decided to follow this blog posts where it shows dumping creds using metasploit module

https://null-byte.wonderhowto.com/how-to/hacking-windows-10-steal-decrypt-passwords-stored-chrome-firefox-remotely-0183600/

For that we need a meterpter shell so let's just generate a windows payload ,upload and execute it 

<img src="https://i.imgur.com/HBCN5fe.png"/>

<img src="https://i.imgur.com/ufwGiZH.png"/>

profile doesn't exist to there are no saved passwords on firefox browser so we can't proceed further. Now nothing was coming into my mind except that firefox browser is currently runnning so I searched for dumping firefox process and this came up

<img src="https://i.imgur.com/2cczktB.png"/>

<img src="https://i.imgur.com/ArMyGHD.png"/>

So we can use `procdump` a sysinternal tool to dump firefox's process and run strings command on it to get the password maybe, I downloaded the tool from microsoft's site

<img src="https://i.imgur.com/aFtb9gU.png"/>

<img src="https://i.imgur.com/PuR9GgI.png"/>

Run `ps` on meterpreter to see the running processes and we can see the process ID of firefox

<img src="https://i.imgur.com/GQ2Tt7f.png"/>

Now we need to run `procdump` to dump process of firefox and transfer it on our machine

<img src="https://i.imgur.com/58PtNP8.png"/>

But the dump's size was 293 MB so I decided not to transfer it and instead use `strings.exe` which is another tool from sysinternal tools

<img src="https://i.imgur.com/jyM2Dna.png"/>

But we don't know what parameters we need to look for so I decided to intercept the web page with `burpsite`

<img src="https://i.imgur.com/4MJ5RMZ.png"/>

<img src="https://i.imgur.com/gwP2fs5.png"/>

But it wasn't working on the target machine so I had to download it on my machine

<img src="https://i.imgur.com/GNHdfDF.png"/>

We can now just run strings and grep for any of the parameters we saw earlier

<img src="https://i.imgur.com/E4VMYK1.png"/>

Now we can just login as Administrator with the password through `evil-winrm` but I wanna dump all hashes so we can use impacket's `seceretsdump.py` do dump hashes from SAM `Security Account Manager`

<img src="https://i.imgur.com/OtvndSo.png"/>

<img src="https://i.imgur.com/2lXUZES.png"/>
