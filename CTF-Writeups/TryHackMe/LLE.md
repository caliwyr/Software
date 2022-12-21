# TryHackMe-Linux Local Enumeration

## NMAP

```
Nmap scan report for 10.10.185.249
Host is up (0.17s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 35:30:91:45:b9:d1:ed:5a:13:42:3e:20:95:6d:c7:b7 (RSA)
|   256 f5:69:6a:7b:c8:ac:89:b5:38:93:50:2f:05:24:22:70 (ECDSA)
|_  256 8f:4d:37:ba:40:12:05:fa:f0:e6:d6:82:fb:65:52:e8 (ED25519)
80/tcp   open  http    Apache httpd 2.4.29
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Index of /
3000/tcp open  http    PHP cli server 5.5 or later
|_http-title: Fox's website
Service Info: Host: 127.0.1.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 41.99 seconds

```

## Gaining a shell

We see through `nmap` scan that there are 2 ports open 80 and 3000 , we can clearly see that port 3000 has php running so it maybe vulnerable to RCE or something 

<img src="https://imgur.com/oLWw71u.png"/>

I'm going to do RCE one so 

<img src="https://imgur.com/VNow06N.png"/>


### Task 1 Let's go!

`No answer needed`

### Task 2 How would you execute /bin/bash with perl?

`perl -e 'exec "/bin/bash";'`


### Task 3 Where can you usually find the id_rsa file? (User = user)

`/home/user/.ssh/id_rsa`

#### Is there an id_rsa file on the box? (yay/nay)

<img src="https://imgur.com/hO5djff.png"/>

`nay`

<img src="https://imgur.com/caSZMrz.png"/>

### Task 4 How would you print machine hardware name only?

`uname -m`

#### Where can you find bash history?

`~/.bash_history`

####  What's the flag?

`thm{clear_the_history}`


<img src="https://imgur.com/NM2qYKw.png"/>

### Task 5 Can you read /etc/passwd on the box? (yay/nay)

`yay`

<img src="https://imgur.com/ywriz39.png"/>

<img src="https://imgur.com/wZbhJ8c.png"/>

### Task 6 What's the password you found?

`THMSkidyPass`

#### Did you find a flag?

`thm{conf_file}`


<img src="https://imgur.com/iHxd9AF.png"/>

<img src="https://imgur.com/BcllTsl.png"/>

<img src="https://imgur.com/MBVW2b7.png"/>

### Task 7 Which SUID binary has a way to escalate your privileges on the box?

`grep`

#### What's the payload you can use to read /etc/shadow with this SUID?

`grep '' /etc/shadow`

