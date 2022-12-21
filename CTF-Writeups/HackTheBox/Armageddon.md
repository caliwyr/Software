# HackTheBox-Armageddon

## Rustscan

```bash

rustscan -a 10.129.89.150 -- -A -sC -sV

Open 10.129.89.150:22                                              
Open 10.129.89.150:80 

PORT   STATE SERVICE REASON         VERSION                               
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey:       
|   2048 82:c6:bb:c7:02:6a:93:bb:7c:cb:dd:9c:30:93:79:34 (RSA)      
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDC2xdFP3J4cpINVArODYtbhv+uQNECQHDkzTeWL+4aLgKcJuIoA8dQdVuP2UaLUJ0XtbyuabPEBzJl3IHg3vztFZ8UEcS94KuWP09ghv6fhc
7JbFYONVJTYLiEPD8nrS/V2EPEQJ2ubNXcZAR76X9SZqt11JTyQH/s6tPH+m3m/84NUU8PNb/dyhrFpCUmZzzJQ1zCDStLXJnCAOE7EfW2wNm1CBPCXn1wNvO3SKwokCm4GoMKHSM9rNb9FjGLIY
0nq+8mt7RTJZ+WLdHsje3AkBk1yooGFF+0TdOj42YK2OtAKDQBWnBm1nqLQsmm/Va9T2bPYLLK5aUd4/578u7h
|   256 3a:ca:95:30:f3:12:d7:ca:45:05:bc:c7:f1:16:bb:fc (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBE4kP4gQ5Th3eu3vz/kPWwlUCm+6BSM6M3Y43IuYVo3ppmJG+wKiabo/gVYLOwzG7js497Vr7e
GIgsjUtbIGUrY=                                                            
|   256 7a:d4:b3:68:79:cf:62:8a:7d:5a:61:e7:06:0f:5f:33 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIG9ZlC3EA13xZbzvvdjZRWhnu9clFOUe7irG8kT0oR4A
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.6 ((CentOS) PHP/5.4.16)
|_http-favicon: Unknown favicon MD5: 1487A9908F898326EBABFFFD2407920D
|_http-generator: Drupal 7 (http://drupal.org)                            
| http-methods:                                                           
|_  Supported Methods: GET HEAD POST OPTIONS                              
| http-robots.txt: 36 disallowed entries                   
| /includes/ /misc/ /modules/ /profiles/ /scripts/               
| /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt   
| /INSTALL.pgsql.txt /INSTALL.sqlite.txt /install.php /INSTALL.txt 
| /LICENSE.txt /MAINTAINERS.txt /update.php /UPGRADE.txt /xmlrpc.php          
| /admin/ /comment/reply/ /filter/tips/ /node/add/ /search/
| /user/register/ /user/password/ /user/login/ /user/logout/ /?q=admin/     
| /?q=comment/reply/ /?q=filter/tips/ /?q=node/add/ /?q=search/
|_/?q=user/password/ /?q=user/register/ /?q=user/login/ /?q=user/logout/
|_http-server-header: Apache/2.4.6 (CentOS) PHP/5.4.16                    
|_http-title: Welcome to  Armageddon |  Armageddon                        


```

## PORT 80 (HTTP)

<img src="https://imgur.com/8TtXLaX.png"/>

Let's create a new account

<img src="https://imgur.com/rqJgsvy.png"/>

<img src="https://imgur.com/XxbPzSY.png"/>

But we can't login as it says activation email has been sent but the box doesn't have any internet connection so we can't really do much here

So I treid fuzzing but couldn't find anything intersting stuff other than default files 

<img src="https://imgur.com/ehuFa4j.png"/>

But if we go through these files 

<img src="https://imgur.com/OCbwHwG.png"/>

We can see that it's using `Druapl CMS` and going to `modules` we can see it's using `Agggregator` module

<img src="https://imgur.com/Oao6mYJ.png"/>

Now the webiste hints us about `Drupalgeddon` , since `# Armageddon` isn't anything in drupal so I searched for bunch of drupal 7 exploits as we can see the verions through wappalyzer

<img src="https://imgur.com/Sa441Xa.png"/>

<img src="https://imgur.com/YPNsPHy.png"/>

I tried getting the stablized shell but was getting permission denied

<img src="https://imgur.com/5DEESMA.png"/>

<img src="https://imgur.com/sDZz7Se.png"/>

We can find the credentials for database from `/var/www/html/sites/default/settings.php`

<img src="https://imgur.com/6VmCQOH.png"/>


```
 database => drupal,                                             
username => drupaluser,                                         
password => CQHEy@9M*m23gBVj
	  
```

Doing `/bin/bash -i` will  give you a bash shell

<img src="https://imgur.com/bEUxclW.png"/>

No we know that there's a user on machine

<img src="https://imgur.com/IPuwJQF.png"/>

So the only option is to brute force the user

 <img src="https://imgur.com/09NGmH6.png"/>
 
 <img src="https://imgur.com/DCbWlAs.png"/>
 
 Doing `sudo -l`
 
 <img src="https://imgur.com/iqUXSih.png"/>
 
 Now here we could try to install a custom snap packge to do that let's test this locally on our machine so first let's intall `snap` which is a package manager like `apt`
 
 <img src="https://imgur.com/U138n5Q.png"/>
 
 Then install snapcraft which build the snap packages
 
 <img src="https://imgur.com/wRq56s9.png"/>
 
 <img src="https://imgur.com/EjrVYXQ.png"/>
 
 We can see that it's installed
 
 <img src="https://imgur.com/xlAQG3f.png"/>
 
 To see if we can run `snapcraft`
 
 <img src="https://imgur.com/Rk2lSVj.png"/>
 
 Everything was installed but it gave me an error when I was trying to build snap package so I tried to find some publicaly available exploits for snap and came across this
 
 https://0xdf.gitlab.io/2019/02/13/playing-with-dirty-sock.html
 
 <img src="https://imgur.com/dI3eBQQ.png"/>
 
 Here we can just copy the base64 encoded text which is being printed with python and then pipe it to `base64 -d` and write it to any file name with `.snap` extensions. What's happening in that encoded text that's it's creating a user `dirty_sock` and adding to sudoers giving all permissions to it so it can give us root.
 
 <img src="https://imgur.com/5FfOhLs.png"/>
 
 <img src="https://imgur.com/3yhzvaW.png"/>
 
 But still it was giving errors that the package must be verified so to avoid these signature checks 
 
 <img src="https://imgur.com/QfaiUsu.png"/>
 
 Now it was finally installed , now to switch the user and become root
 
 <img src="https://imgur.com/d6Kg7dp.png"/>
 
 <img src="https://imgur.com/mUThfgR.png"/>