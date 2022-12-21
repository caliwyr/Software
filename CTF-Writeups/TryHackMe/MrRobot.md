# TryHackMe-MrRobotCTF

## NMAP

```
Nmap scan report for 10.10.200.232                                        
Host is up (0.23s latency).                                               
Not shown: 997 filtered ports                                             
PORT    STATE  SERVICE  VERSION                                           
22/tcp  closed ssh                                                        
80/tcp  open   http     Apache httpd                                      
|_http-server-header: Apache                                              
|_http-title: Site doesn't have a title (text/html).                                                                                                
443/tcp open   ssl/http Apache httpd                                                                                                                
|_http-server-header: Apache                                                                                                                        
|_http-title: 400 Bad Request                                                                                                                       
| ssl-cert: Subject: commonName=www.example.com                                                                                                     
| Not valid before: 2015-09-16T10:45:03                                                                                                             
|_Not valid after:  2025-09-13T10:45:03                                   

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                                                      
Nmap done: 1 IP address (1 host up) scanned in 60.16 seconds

```

## PORT 80

<img src="https://imgur.com/hyURjVb.png"/>

Looking at `robots.txt` which is just a basic enumeration looking for these files

<img src="https://imgur.com/vew4kd4.png"/>

We have two files here `fscoiety.dic` which looks like a wordlist and `key-1-of-3.txt` which has the first flag



## Gobuster


```
/images (Status: 301)
/index.php (Status: 301)
/blog (Status: 301)
/rss (Status: 301)
/sitemap (Status: 200)
/login (Status: 302)
/0 (Status: 301)
/feed (Status: 301)
/video (Status: 301)
/image (Status: 301)
/atom (Status: 301)
/wp-content (Status: 301)
/admin (Status: 301)
/audio (Status: 301)
/intro (Status: 200)
/wp-login (Status: 200)
/wp-login.php (Status: 200)
/css (Status: 301)
/rss2 (Status: 301)
/license (Status: 200)
/wp-includes (Status: 301)

```
This was the list of directories I was able to find but only `wp-login` was of our interest rest of them were giving forbidden access messages

<img src="https://imgur.com/z7LIZg8.png"/>


So we need to know the usernames , there isn't any username on the blog so we might have to do trial and error to guess it but we have `fsociety.dic` that might be useful for usernames so let's intercept the login request to get paramters and then start bruteforcing it with `hydra` But it's going to take a lot of time bruteforcing against a list of usernames so as this box has theme of mr robot and the main character of that series is `elliot`

<img src="https://imgur.com/cBCNGKJ.png"/>

<img src="https://imgur.com/zx9T3MZ.png"/>

So this username is correct all we need to do is bruteforce against the words in fsociety.dic but picking the first word which is `true` it has 150 matches so it has a number of words repeated in it so we need to remove repeated words (I checked this through sublime's regex mode)

<img src="https://imgur.com/olul95x.png"/> 

<img src='https://imgur.com/ku52oGe.png'/>

You see the difference in the repeated words

<img src="https://imgur.com/jlNXkrs.png"/>

Perfect now let's continue with intercepting the request and bruteforcing it against hydra

<img src="https://imgur.com/vWeNu1I.png"/>

But hydra was taking longer than usual so I moved to wspcan to bruteforce elliot's password

<img src="https://imgur.com/rdhp1YF.png"/>

<img src="https://imgur.com/kf1TBLt.png"/>

<img src="https://imgur.com/FJUJAXn.png"/>

Now go to `Appearance -> Editor` Then select the Twenty Fifteen theme and paste the php reverse-shell from pentest monkey (GitHub one)

<img src="https://imgur.com/s9giwgO.png"/> 

Click on the update button

<img src="https://imgur.com/QykCq2q.png"/>

<img src="https://imgur.com/6o9Bq4Q.png"/>

Stablize the shell 

<img src="https://imgur.com/wzag057.png"/>

<img src="https://imgur.com/Jvz28mz.png"/>

In the home directory of `robot` we can see a md5 hash that we need to crack inorder to switch user 

<img src="https://imgur.com/GcRkbcB.png"/>

<img src="https://imgur.com/7fxygco.png"/>

We can see a cronjob running on the system

<img src="https://imgur.com/8ysoOSg.png"/>

Looking for SUID we find nmap having SUID bit 

<img src="https://imgur.com/ggHhRnm.png"/>

Going to GTFOBINS

<img src="https://imgur.com/PZHOO4e.png"/>

<img src="https://imgur.com/34y1odH.png"/>