# HackTheBox-Writeup

## NMAP

```bash
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
| ssh-hostkey:                                                            
|   2048 dd:53:10:70:0b:d0:47:0a:e2:7e:4a:b6:42:98:23:c7 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDKBbBK0GkiCbxmAbaYsF4DjDQ3JqErzEazl3v8OndVhynlxNA5sMnQmyH+7ZPdDx9IxvWFWkdvPDJC0rUj1CzOTOEjN61Qd7uQbo5x4rJd3P
AgqU21H9NyuXt+T1S/Ud77xKei7fXt5kk1aL0/mqj8wTk6HDp0ZWrGBPCxcOxfE7NBcY3W++IIArn6irQUom0/AAtR3BseOf/VTdDWOXk/Ut3rrda4VMBpRcmTthjsTXAvKvPJcaWJATtRE2NmFj
BWixzhQU+s30jPABHcVtxl/Fegr3mvS7O3MpPzoMBZP6Gw8d/bVabaCQ1JcEDwSBc9DaLm4cIhuW37dQDgqT1V                                                              
|   256 37:2e:14:68:ae:b9:c2:34:2b:6e:d9:92:bc:bf:bd:28 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPzrVwOU0bohC3eXLnH0Sn4f7UAwDy7jx4pS39wtkKMF5j9yKKfjiO+5YTU//inmSjlTgXBYNv
aC3xfOM/Mb9RM=                       
|   256 93:ea:a8:40:42:c1:a8:33:85:b3:56:00:62:1c:a0:ab (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEuLLsM8u34m/7Hzh+yjYk4pu3WHsLOrPU2VeLn22UkO
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.25 ((Debian)) 
| http-methods:                      
|_  Supported Methods: GET HEAD POST OPTIONS                              
| http-robots.txt: 1 disallowed entry                                     
|_/writeup/                          
|_http-title: Nothing here yet.                                           
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel                   
```

## PORT 80 (HTTP)

On the webserver we only see a html page which is made with `CMS made simple` from the results of `wappalyzer` , also looking at the source there's nothing we can look for 

<img src="https://i.imgur.com/3Kis0HE.png"/>

From the nmap scan it did show us that there's a `robots.txt` file so let's look at that

<img src="https://i.imgur.com/ADRxzpS.png"/>

We see a disallowed entry `/writeup/` that shouldn't be picked up by search engines

<img src="https://i.imgur.com/DNRCfw4.png"/>

<img src="https://i.imgur.com/kcNwozQ.png"/>

Now I went through all of the posts but found nothing , but I did notice a GET parameter `page` was being used

<img src="https://i.imgur.com/GUiwQ0y.png"/>

So I tried to see if it was vulnerable to `LFI` (Local FIle Inclusion)

<img src="https://i.imgur.com/iRDm84K.png"/>

I kept trying but didn't seem it was we can do LFI here, now we don't know the version of `CMS made simple` so let's just see if there are any exploits for this CMS

<img src="https://i.imgur.com/iRDm84K.png"/>

The first result came up with `exploit-db` and it was related to SQL injection

<img src="https://i.imgur.com/v55NRL4.png"/>

So let's try this maybe and see if we can somehow get the password, run the exploit script

<img src="https://i.imgur.com/9Q6znRS.png"/>

<img src="https://i.imgur.com/eRiyC9c.png"/>

We get the username and password, so let's see if we can access admin panel in `CMS Made Simple`

<img src="https://i.imgur.com/6GyIt44.png"/>

But when I tried those creds , it failed . So the only option left for us is to see if these credentials work on ssh

## PORT 22 (SSH)

<img src="https://i.imgur.com/OzTR7DT.png"/>

Neat , we are in !

Let's do a quick `sudo -l` to see if we can run anything as sudo

<img src="https://i.imgur.com/RZqvtHE.png"/>

It seems `sudo` command isn't available on this machine, I ran linpeas but didn't found anything useful , than decide to run `pspy` which is a process and cronjob monitor which can even monitor cronjobs running as different users or as root

<img src="https://i.imgur.com/2G3W28Y.png"/>

Running the tool , we can see a fail2ban script running in the background which is why we weren't able to run fuzzing tools

<img src="https://i.imgur.com/Pa9yZ02.png"/>

Also there's a script which is running like every minute

<img src="https://i.imgur.com/o1JRntp.png"/>

But it's in `root` directory and we can't do anything with it 
<img src="https://i.imgur.com/ZJCfk7Z.png"/>

So I used ssh again to login and found that it was running `message of the day script`  (/etc/update-motd.d)  through a binary named `run-parts` , notice that `run-parts` isn't using it's absolute PATH so here we can abuse it by creating `run-parts` file by giving it executable permissions,the path variable includes `/usr/local/sbin` and `/usr/local/bin` which we have permissions to it as these folders are owned by `staff` group and we are in that group so we can create that file there 


<img src="https://i.imgur.com/ANG0qDt.png"/>

<img src="https://i.imgur.com/WaYaYaV.png"/>

We can write into `/usr/local/sbin` 

<img src="https://i.imgur.com/ZJ7iaFX.png"/>

<img src="https://i.imgur.com/DSwJac7.png"/>

Now we have created a file named `run-parts` which has a bash reverse shell which will execute when we will login to ssh our `run-parts` file will be executed and give us a reverse shell

<img src="https://i.imgur.com/v8yy2xz.png"/>
