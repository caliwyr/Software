# HackTheBox - Lame

## NMAP

```bash

PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)       
| ftp-syst:          
|   STAT:
| FTP server status:
|      Connected to 10.10.14.2
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text                   
|      Data connections will be plain text                
|      vsFTPd 2.3.4 - secure, fast, stable                
|_End of status                                           
22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
| ssh-hostkey:                                            
|   1024 60:0f:cf:e1:c0:5f:6a:74:d6:90:24:fa:c4:d5:6c:cd (DSA)
|_  2048 56:56:24:0f:21:1d:de:a7:2b:ae:61:b1:24:3d:e8:f3 (RSA)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.0.20-Debian (workgroup: WORKGROUP)
3632/tcp open  distccd     distccd v1 ((GNU) 4.2.4 (Ubuntu 4.2.4-1ubuntu4))
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel                

```

## PORT 21 (FTP)
From the nmap scan we can see that anonymous login is enabled on `ftp`

<img src="https://i.imgur.com/FylyPes.png"/>

But when logged in  , we don't see anything as nothing is in ftp share

## PORT 139/445 (SMB)
There's also smb server running so let's see if we anonymous login is enabled on smb as well
<img src="https://i.imgur.com/tyezRyA.png"/>

Using `smbmap` we have a list of shares out of which we have read access to `tmp` share but there wasn't anything in those files so moving onto another service which was running

## PORT 3632 (distccd)

Now this service can be used to compile programs quickly and configured to use multiple devices to aid in the compilation, the issue here is that if it's exposed over the network i- https://www.rapid7.com/db/modules/exploit/unix/misc/distcc_exec/t can be vulnerable to remote code execution due to which compilation jobs are executed without any authorization checks.

## Foothold

For exploiting this we have a metasploit module that we can use 

<img src="https://i.imgur.com/DwSyhL1.png"/>

We can do rce from here so to get a reverse shell , base64 encode the python reverse shell ,pipe it to base64 decode and then to bash

<img src="https://i.imgur.com/iXgommL.png"/>

<img src="https://i.imgur.com/nvFty01.png"/>

<img src="https://i.imgur.com/2DemeTP.png"/>

Stabilizing the shell with python so that we can have tty terminal on the target machine 

<img src="https://i.imgur.com/05rlyKZ.png"/>

For privilege escalation , I tried reading cron jobs , looking into directories, checking local ports but there wasn't anything interesting , I checked the kernel version and it was `2.6.24-16` which looked promising as there's a kernel exploit called `dirty_cow` but when I tried to compile the source code it failed 

<img src="https://i.imgur.com/edOC0WA.png"/>
## Privilege Escalation
Running `ps -aux --forest` will list us the running processes and we can see `smbd` which is smb server daemon which is running as a root user so searching for smb related exploits

<img src="https://i.imgur.com/6WP2vAY.png"/>

<img src="https://i.imgur.com/Z9ETdCb.png"/>

So once we get a shell from this service we will be `root`

<img src="https://i.imgur.com/Bs3YaO4.png"/>

<img src="https://i.imgur.com/Bs3YaO4.png"/>


## References

- https://www.rapid7.com/db/modules/exploit/unix/misc/distcc_exec/
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
- https://www.rapid7.com/db/modules/exploit/multi/samba/usermap_script/
