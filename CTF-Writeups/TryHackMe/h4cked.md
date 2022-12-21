# TryHackMe- H4cked

##  Oh no! We've been hacked!

Download the pacp file we are given , on opening the `.pcap` file we can see a lot of traffic

<img src="https://imgur.com/aL3glwA.png"/>

At the starting we can see that a number of times connection to port 21 is being made which is a port for `FTP`. 

If we follow the tcp stream for port 21 we can see the username and the password the attacker is trying 

<img src="https://imgur.com/Ixqqqaf.png"/>

Here username is `jenny` , changing the stream we will find the password is brute forced

<img src="https://imgur.com/b9xLb4n.png"/>

<img src="https://imgur.com/628EZPw.png"/>

Here we can see that attacker uploaded a backdoor `shell.php` in `/var/www/html`

<img src="https://imgur.com/cRIF7tz.png"/>

<img src="https://imgur.com/XovV9Mn.png"/>

Here we can see once the attacker gain access he stabilizes the shell , switches to user jenny and since that user can run any command as sudo he escalates to root and to gain persistance intalls `reptile` rootkit


## Tasks


1. The attacker is trying to log into a specific service. What service is this?
`FTP`
2. There is a very popular tool by Van Hauser which can be used to brute force a series of services. What is the name of this tool?
`hydra`
3. The attacker is trying to log on with a specific username. What is the username?
`jenny`
4. What is the user's password?
`password123`
5. What is the current FTP working directory after the attacker logged in?
`/var/www/html`
6. The attacker uploaded a backdoor. What is the backdoor's filename?
`shell.php`
7. The backdoor can be downloaded from a specific URL, as it is located inside the uploaded file. What is the full URL?
`http://pentestmonkey.net/tools/php-reverse-shell`
8. Which command did the attacker manually execute after getting a reverse shell?
What is the computer's hostname?
`whoami`

9. Which command did the attacker execute to spawn a new TTY shell?
`python3 -c 'import pty;pty.spawn("/bin/bash")'`
10. Which command was executed to gain a root shell?
`sudo su `
11. The attacker downloaded something from GitHub. What is the name of the GitHub project?
`Reptile`
12. The project can be used to install a stealthy backdoor on the system. It can be very hard to detect. What is this type of backdoor called?
`rootkit`
13. What is the computer's hostname ?
`wir3`

## Rustscan

```bash

PORT   STATE SERVICE REASON         VERSION                                                                                                 [25/685]
21/tcp open  ftp     syn-ack ttl 63 vsftpd 2.0.8 or later 
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
| http-methods:                                                           
|_  Supported Methods: GET POST OPTIONS HEAD                              
|_http-server-header: Apache/2.4.29 (Ubuntu)                          
|_http-title: Apache2 Ubuntu Default Page: It works 
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port   
```

## Hydra

<img src="https://imgur.com/Bcm5NZD.png"/>

<img src="https://imgur.com/O5HHz1b.png"/>

We got  the password now let's login to ftp server

<img src="https://imgur.com/8P9RMfj.png"/>

Here after logging I uploaded a php interactive shell and gave permissions to execute

<img src="https://imgur.com/HrrIHz6.png"/>

Gain a shell through BSD netcat and stabilize it using python3

<img src="https://imgur.com/3LdPEb5.png"/>

Switch to user jenny with the password you brute forced

<img src="https://imgur.com/ABXPU2t.png"/>

<img src="https://imgur.com/BuFXMed.png"/>
