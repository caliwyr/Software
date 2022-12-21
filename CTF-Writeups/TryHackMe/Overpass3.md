# TryHackMe-Overpass 3

## NMAP

```
Nmap scan report for 10.10.206.68
Host is up (0.40s latency).
Not shown: 997 filtered ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   3072 de:5b:0e:b5:40:aa:43:4d:2a:83:31:14:20:77:9c:a1 (RSA)
|   256 f4:b5:a6:60:f4:d1:bf:e2:85:2e:2e:7e:5f:4c:ce:38 (ECDSA)
|_  256 29:e6:61:09:ed:8a:88:2b:55:74:f2:b7:33:ae:df:c8 (ED25519)
80/tcp open  http    Apache httpd 2.4.37 ((centos))
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.37 (centos)
|_http-title: Overpass Hosting
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 39.56 seconds
```

## PORT 80

<img src="https://imgur.com/zPWd0Dd.png"/>

Viewing the source we see a comment

<img src="https://imgur.com/TnrHBIL.png"/>

`0.99999% is 5 nines, right?`

Running a gobuster resulted in finding a `backups` directory

<img src="https://imgur.com/N3iS7l2.png"/>

<img src="https://imgur.com/W6TpOQu.png"/>

<img src="https://imgur.com/oXCjxFy.png"/>

This `backup.zip` gave us two files `priv.key` and `CustomerDetails.xlsx.gpg`

Use `gpg` to import the key file and decrypt the file by appending the result to a `xlsx` file

<img src="https://imgur.com/LqC9IpR.png"/>

<img src="https://imgur.com/PBGmx9z.png"/>

10.10.184.192

```
paradox			:ShibesAreGreat123  - FTP
0day 			:OllieIsTheBestDog	- X
muirlandoracle  :A11D0gsAreAw3s0me	- X
```

## PORT 21 (FTP)

<img src="https://imgur.com/zFaQgxs.png"/>

We were able to login with the credentials of `paradox` on ftp server

<img src="https://imgur.com/Do4Xjxe.png"/>

By looking at the file permission of root folder it seems we can `write` something so I tried to put a text file and it was uploaded

<img src="https://imgur.com/8c22mcf.png"/>

<img src="https://imgur.com/JIE9uwU.png"/>

<img src="https://imgur.com/MCnI0iK.png"/>

And we get a shell

Using the password we found for `paradox` let's try to switch user with that password.Since binaries like nc,wget,curl were not avaiable on the machine I decide to transfer linpeas on the box through ftp server

<img src="https://imgur.com/LdKHC4P.png"/>

<img src="https://imgur.com/XfLovzu.png"/>

<img src="https://imgur.com/S85sGFA.png"/>

Seems like there is an nfs share but the nmap scan didn't showed as any port for it so it's likely to be running on localhost but we cannot check because there aren't binaries for it so assuming it's on port 2049 we have to uss ssh port forwarding for that we have to be able to login with ssh so I generated a ssh keypair copied contents of `id_rsa.pub` to `/paradox/.ssh/authorized_keys`

<img src="https://imgur.com/S1qvNHD.png"/>

<img src="https://imgur.com/7kUZvsv.png"/>

<img src="https://imgur.com/ZYmNm3p.png"/>

Running nmap scan on our localhost will show that port 2049 is open

<img src="https://imgur.com/HvKHdR9.png"/>

<img src="https://imgur.com/J1AkmCT.png"/>

But when we try to mount it will fail because it is NFS v4 which is differnt from what we are doing

<img src="https://imgur.com/kN9q4p6.png"/>

After so many trial and erros ,searching on google I finally managed to mount the share

<img src="https://imgur.com/qXLW1a0.png"/>

<img src="https://imgur.com/xsXKGNu.png"/>

Now with the `id_rsa` we are now logged in as `james`

<img src="https://imgur.com/fAuYB3W.png"/>

Going back to the enumeration script we ran (linpeas) we can see that `no_root_squash` ,this option basically gives authority to the root user on the client to access files on the nfs server as root. We can take advantage of this  by first creating a binary having SUID and SGID set to 0 which root then mount the nfs share set SUID bit on the file then copy it to the share which will transfer it to the machine and then execute that binary which will give you root.

So the source code of c program we have to compile is 

```
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(void)
{

setuid(0); 
setgid(0); 
system("/bin/bash");

}
```
As you can SUID and SGID are set 0 which is the id of root user and `system("/bin/bash")` will execute bash as system command

<img src="https://imgur.com/BmPB2Zc.png"/>

<img src="https://imgur.com/WKQJwcB.png"/>

<img src="https://imgur.com/94Iedsy.png"/>

Going back to the target machine check if the owner is root and it has a SUID bit on

<img src="https://imgur.com/WK4j3j9.png"/>

Now just simply execute the binary

<img src="https://imgur.com/6BnSYnd.png"/>

And we are root !!!