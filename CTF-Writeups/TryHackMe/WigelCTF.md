# TryHackMe-WgelCTF
Abdullah Rizwan ,21 August , 03:07 PM

Wgel CTF is free box to try on TryHackMe and it's a beginner level box

## Look for open ports
First of all we are going to scan the box for open ports , you can use any port scanner but here I am using nmap,it's going to take some time while scanning because we scan for every open port on the box.
```
nmap -T4 -A -p- 10.10.81.198
```

<a href="https://imgur.com/e6lpe4V"><img src="https://i.imgur.com/e6lpe4V.png" title="source: imgur.com" /></a>



From here we can see that there are 2 ports open

```
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 94:96:1b:66:80:1b:76:48:68:2d:14:b5:9a:01:aa:aa (RSA)
|   256 18:f7:10:cc:5f:40:f6:cf:92:f8:69:16:e2:48:f4:38 (ECDSA)
|_  256 b9:0b:97:2e:45:9b:f3:2a:4b:11:c7:83:10:33:e0:ce (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))

```
## Port 80

<a href="https://imgur.com/uTuPxF9"><img src="https://i.imgur.com/uTuPxF9.png" title="source: imgur.com" /></a>

It just shows the default http server page but if we look at the source code of this page we can find a user name there 'jessie'.

<a href="https://imgur.com/F5EsGgc"><img src="https://i.imgur.com/F5EsGgc.png" title="source: imgur.com" /></a>

Lets enumerate directories by using dirbuster

<a href="https://imgur.com/UpKWFqm"><img src="https://i.imgur.com/UpKWFqm.png" title="source: imgur.com" /></a>

I am also going to perform a nikto scan for vulnerabilites on the site

```
nikto -h 10.10.81.198
```
## Result of Nikto

<a href="https://imgur.com/VVerLhx"><img src="https://i.imgur.com/VVerLhx.png" title="source: imgur.com" /></a>
Nothing much came out of nikto scan

## Result of Dirbuster
<a href="https://imgur.com/rhpDUPi"><img src="https://i.imgur.com/rhpDUPi.png" title="source: imgur.com" /></a>

From directory busting , we came to know that there is a directory called sitemap

<a href="https://imgur.com/ai260IH"><img src="https://i.imgur.com/ai260IH.png?1" title="source: imgur.com" /></a>

I again tried to bruteforce directory but this time i used 'common.txt.' wordlist

<a href="https://imgur.com/pXi8eVH"><img src="https://i.imgur.com/pXi8eVH.png" title="source: imgur.com" /></a>

Here we can see that there is a directory ".ssh" with sub directory "id_rsa"

<a href="https://imgur.com/H5QgKlc"><img src="https://i.imgur.com/H5QgKlc.png" title="source: imgur.com" /></a>

Copy the whole text found here into a file a name it 'id_rsa' which is a key file for ssh.
Now we can utilize this key through the port 22 which is ssh

## Port 22

First of all change the file permissions because it won't allow to execute this file.

<a href="https://imgur.com/5SWd6MM"><img src="https://i.imgur.com/5SWd6MM.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/yw4h1Pv"><img src="https://i.imgur.com/yw4h1Pv.png" title="source: imgur.com" /></a>

We can now grab the user flag from here but we are not done yet we still have to escalate our privileges to get root flag to complete the whole box.

By using netcat we will listen on any port
```
nc -lvp 4444

```
And on the target machine we will try to send that file to us

<a href="https://imgur.com/j1h9gM7"><img src="https://i.imgur.com/j1h9gM7.png" title="source: imgur.com" /></a>



<a href="https://imgur.com/2wZ4Nqo"><img src="https://i.imgur.com/2wZ4Nqo.jpg" title="source: imgur.com" /></a>

This will be the response you will receive on your terminal.

Submit the flag in order to complete this CTF