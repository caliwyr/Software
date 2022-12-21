# TryHackMe-Common Linux Privilege Escalation

## NMAP

```
Nmap scan report for 10.10.235.8                                                                             [37/154]
Host is up (0.20s latency).                               
Not shown: 994 closed ports                               
PORT     STATE SERVICE     VERSION         
22/tcp   open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:                                            
|   2048 37:c9:2d:7e:01:c5:ea:33:a9:e2:19:ea:66:1c:95:82 (RSA)
|   256 9f:48:65:f7:67:2e:92:cf:73:ce:0e:69:f1:32:46:40 (ECDSA)
|_  256 ac:5f:9a:38:23:ee:ac:14:88:9e:aa:08:df:98:f4:a7 (ED25519)
80/tcp   open  http        Apache httpd 2.4.29 ((Ubuntu))                                                            
|_http-server-header: Apache/2.4.29 (Ubuntu)                                                                         
|_http-title: Apache2 Ubuntu Default Page: It works                                                                  
111/tcp  open  rpcbind     2-4 (RPC #100000)                                                                         
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      39913/tcp   mountd
|   100005  1,2,3      43930/udp   mountd
|   100005  1,2,3      50462/udp6  mountd
|   100005  1,2,3      53247/tcp6  mountd
|   100021  1,3,4      38879/tcp   nlockmgr
|   100005  1,2,3      53247/tcp6  mountd
|   100021  1,3,4      38879/tcp   nlockmgr
|   100021  1,3,4      40883/tcp6  nlockmgr
|   100021  1,3,4      47812/udp   nlockmgr
|   100021  1,3,4      57217/udp6  nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
2049/tcp open  nfs_acl     3 (RPC #100227)
Service Info: Host: LINUX; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 1h40m00s, deviation: 2h53m12s, median: 0s
|_nbstat: NetBIOS name: LINUX, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: polobox
|   NetBIOS computer name: LINUX\x00
|   Domain name: \x00
|   FQDN: polobox
|_  System time: 2020-11-21T10:27:08-05:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-11-21T15:27:08 
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 25.45 seconds

```

## Enumeration



1. First, lets SSH into the target machine, using the credentials user3:password. This is to simulate getting a foothold on the system as a normal privilege user.
`No answer needed`

2. What is the target's hostname?


`polobox`

<img src="https://imgur.com/cIQZlOM.png"/>

By reading the contents of `/etc/passwd` there are 8 users

3. Look at the output of /etc/passwd how many "user[x]" are there on the system?

`8`

<img src="https://imgur.com/ps8gddG.png"/>

4. How many available shells are there on the system?

`4`

<img src="https://imgur.com/1X1bWkQ.png"/>

5. What is the name of the bash script that is set to run every 5 minutes by cron? 

`autoscript.sh`

6. What critical file has had its permissions changed to allow some users to write to it?

`/etc/passwd`

## Abusing SUID/GUID Files

<img src="https://imgur.com/b4T3log.png"/>

1. What is the path of the file in user3's directory that stands out to you?
`/home/user3/shell`


## Exploiting a writable /etc/passwd

1. Having read the information above, what direction privilege escalation is this attack?
`Vertical`

Now to generate a simple password hash , `openssl` can do that however it is not only used for generating md5 hash it's  a cryptography toolkit implementing the Secure Sockets Layer (SSL v2/v3) and Transport Layer ,Security (TLS v1) network protocols and related cryptography standards required by them.

`openssl passwd -1 --salt abc 123` so let's breakdown this command 

```
openssl , is the tool that we are using
passwd , is telling to generate a passwd
-1     ,it's telling to use md5 hashing algorithm
--salt ,telling to use the salt which is a random value but in this case we are using new and 123 is the actual password on which this alogrithm will be applied
```


<img src="https://imgur.com/o0VewRd.png"/>

2. What is the hash created by using this command with the salt, "new" and the password "123"?
`$1$new$p7ptkEKU1HnaHpRtzNizS1`


<img src="https://imgur.com/R8QFh9Y.png"/>

3. What would the /etc/passwd entry look like for a root user with the username "new" and the password hash we created before?
`new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash`

## Escaping Vi Editor

Use "su" to swap to user8, with the password "password"

<img src="https://imgur.com/EBlBf5b.png"/>

Run it with `sudo /usr/bin/vi`

<img src="https://imgur.com/UkunmAC.png"/>

<img src="https://imgur.com/UySCvQ2.png"/>

1. `sudo -l` command, what does this user require (or not require) to run vi as root?
`NOPASSWD`


## Exploiting Crontab

We can see a cronjob running as `root` user

<img src="https://imgur.com/C6lsigg.png"/>

So now we have to create a payload and append it to the cron script

<img src="https://imgur.com/GOE3YSW.png"/>

<img src="https://imgur.com/Ld6hwUh.png"/>

<img src="https://imgur.com/1XcVEuU.png"/>

1. What directory is the "autoscript.sh" under?

`/home/user4/Desktop`

## Exploiting PATH Variable

<img src="https://imgur.com/m0y30wa.png"/>

1. Let's go to user5's home directory, and run the file "script". What command do we think that it's executing?
`ls`

<img src="https://imgur.com/JdKqiXI.png"/>

2. What would the command look like to open a bash shell, writing to a file with the name of the executable we're imitating
`echo "/bin/bash" `

3. Great! Now we've made our imitation, we need to make it an executable. What command do we execute to do this?

`chmod +x ls`

Now we must edit the $PATH variable to do this we must include the path for our `ls` binary

`export PATH=/tmp:$PATH` , when we run it in bash it would just invoke a bash 

<img src="https://imgur.com/aJ8smTM.png"/>

<img src="https://imgur.com/tDyqlo0.png"/>

Now we are root !

To revert back and use `ls` command we can just edit the enviromental variable `$PATH` and remove the `/tmp` from it 

<img src="https://imgur.com/I4iUuce.png"/>