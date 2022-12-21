# TryHackMe-The Great Escape

## NMAP

```
nmap -sC -sV 10.10.108.159

Starting Nmap 7.80 ( https://nmap.org ) at 2021-02-15 16:17 PKT
Stats: 0:02:08 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 50.00% done; ETC: 16:21 (0:02:05 remaining)
Stats: 0:02:13 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 50.00% done; ETC: 16:22 (0:02:10 remaining)
Nmap scan report for 10.10.108.159
Host is up (0.16s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh?
| fingerprint-strings: 
|   GenericLines: 
|_    uT9UNaD!^xFWU'tGL'-@"d2gE"Xd
|_ssh-hostkey: ERROR: Script execution failed (use -d to debug)
80/tcp open  http    nginx 1.19.6
| http-robots.txt: 3 disallowed entries 
|_/api/ /exif-util /*.bak.txt$
|_http-server-header: nginx/1.19.6
|_http-title: docker-escape-nuxt
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port22-TCP:V=7.80%I=7%D=2/15%Time=602A5867%P=x86_64-pc-linux-gnu%r(Gene
SF:ricLines,1F,"uT9UNaD!\^xFWU'tGL\\'-@\"d2gE\"Xd\r\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 195.11 seconds

```

## PORT 80 (HTTP)
<img src="https://imgur.com/CX94tHx.png"/>

From  the nmap scan we see 3 disallowed entries 

<img src="https://imgur.com/1D64CQ5.png"/>

The first entry which is `/api/` gives 503 which we get when a server is currently unable to handle the request due to a temporary overloading or maintenance of the server.

<img src="https://imgur.com/QtvYUjh.png"/>

The second entry invloves uploading a image file

<img src="https://imgur.com/vJs6muB.png"/>

And for the third I didn't know how to access `/\*.bak.txt$`

<img src="https://imgur.com/3FD7Zzi.png"/>

## Dirsearch

For fuzzing I used dirsearch but I was getting a lot of 503 status codes

<img src="https://imgur.com/s5LJLNh.png"/>

But I did saw `/api/` which was having 301 status code with a length of  `169` bytes

<img src="https://imgur.com/BXngywD.png"/>

I also ran `nikto` and it found some cert and archive files but they were also giving 503 errors

<img src="https://imgur.com/ypgZ1Ye.png"/>

So there is some WAF (Web Application Firewall) that is implemented that we need to bypass so here automated tools may not work .

For the web flag I looked at the hint which said about a "well-known file",  I though about robots.txt , the javascript file but it was a dead end so started to guess it and eventually got there

<img src="https://imgur.com/w6ZKCCE.png"/>

It says to make a request with a HEAD 

<img src="https://imgur.com/noGY1WL.png"/>

Going back to `robots.txt` I tried to combine two disallowed entries and got to somewhere

<img src="https://imgur.com/5czQ3rF.png"/>

<img src="https://imgur.com/B2moczb.png"/>

If we focus on this part

<img src="https://imgur.com/rVr2Zzx.png"/>

We can see that it's pointing at `/exif` and has a parameter `url`

<img src="https://imgur.com/S1vdlZb.png"/>

<img src="https://imgur.com/KPBSVA7.png"/>

We can do LFI now , since it's a docker container you can tell as there aren't any usernames so we'll directly go `/root/` directory

<img src="https://imgur.com/ViuDOUM.png"/>

Reading the `dev-note.txt`

<img src="https://imgur.com/RnJu3sL.png"/>

So we got the password but not sure if it's for hydra. Visiting the `/root/.git/` folder

<img src="https://imgur.com/CH2b3vX.png"/>


I used this command to search for files

```
http://10.10.176.126/api/exif?url=http://api-dev-backup:8080/exif?url=;cd%20/root/.git/;pwd;ls%20-la%20objects
```

<img src="https://imgur.com/RfgiY7S.png"/>

And found objects which could be recovered using `git show <object>`

```
a3d30a7d0510dc6565ff9316e3fb84434916dee8
3f5e51190a2c8e2a4ea226e7c004ff656148a168
4530ff7f56b215fa9fe76c4d7cc1319960c4e539
4b825dc642cb6eb9a060e54bf8d69288fbee4904
5242825dfd6b96819f65d17a1c31a99fea4ffb6a
89dcd015496baca7521df9a07de050c37cb3d4ba
aae81292b0aeb73d28ce77dd3078470897151cd8
efadf5b5aa6d0b3bd434c0437be8559edef2a52e
fc326ab9338571dfeb64c00f4b9d85c09d557828
```
These were the objects I gathered by going back and forth

<img src="https://imgur.com/RJOCfUu.png"/>

We get a flag but it was invalid also got some ports to knock .So I did a simple port knock through a tool we can install 

https://www.howtogeek.com/442733/how-to-use-port-knocking-on-linux-and-why-you-shouldnt/

But this method failed so I looked for scripts on github and found one  and modified a little to add some more arguments for ports


```
#!/usr/bin/python

import sys
from socket import *
from itertools import permutations

if len(sys.argv) < 5:
    print "---------------------------------------------"
    print "               Port Knocker                  "
    print "Usage: python knock.py <ip> <p1> <p2> <p3>   "
    print "Ex: python knock.py 192.168.209.130 1 2 3    "
    print "---------------------------------------------"
    sys.exit(0)

host = sys.argv[1]
ports = permutations([int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6])])

def Knockports(ports):
  for port in ports:
      try:
          s = socket(AF_INET, SOCK_STREAM)
          s.settimeout(0.1)
          s.connect_ex((host, port))
          s.close()
          print "Knocked on port " + str(port)
      except Exception, e:
          print "Error: " + str(e)

for combination in list(ports):
    print "Testing permutation: " + str(combination)
    Knockports(combination)
```

Then ran the python2 script

<img src="https://imgur.com/EhLAgEw.png"/>

Doing a nmap scan we can see that docker port is open now

<img src="https://imgur.com/dGKW339.png"/>

After that I visited the hacktricks tried to run some commands but wasn't able to do anything and kept failing. But this blog saved me from quiting on this room

https://www.hackingarticles.in/docker-for-pentester-abusing-docker-api/

<img src="https://imgur.com/5oTagqe.png"/>

First I tried to view the images then tried connecting to them but since they were not running I used `ps -a` to see which images were running and saw  conatiner ID `49fe455a9681` was running so I was able to connect with it

But this container didn't had any intersting stuff so connected to another one which was running on port 8080 of that image

<img src="https://imgur.com/jhjjSdn.png"/>

Then switched to another container

<img src="https://imgur.com/mhBhMkI.png"/>

<img src="https://imgur.com/JzAFfSZ.png"/>

Gathering the objects from before I used git cat-file -p <object_file_name>

<img src="https://imgur.com/JMPf2Ug.png"/>

<img src="https://imgur.com/7gjk5at.png"/>

This was the second flag

Now I tried to look for docker breakouts, exploits,capabilites but nothing seemed to work and I was getting the feeling that this is a huge rabbit hole. So going back to seeing docker images I saw alpine at the bottom and gave a shot to mount it 

<img src="https://imgur.com/DqkM296.png"/>

<img src="https://imgur.com/d8p9PiQ.png"/>

This is box was a lot difficult because there was a prize for this box the one's who completed it within 3 days will be added to the raffle and I completed this box after 2 days so hopefully I'll win a prize with that we can all the flag.

