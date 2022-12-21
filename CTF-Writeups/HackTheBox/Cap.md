# HackTheBox-Cap

## Rustscan

```bash

PORT   STATE SERVICE REASON         VERSION                                                                                                         
21/tcp open  ftp     syn-ack ttl 63 vsftpd 3.0.3                          
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)                                                    
80/tcp open  http    syn-ack ttl 63 gunicorn                              
| fingerprint-strings:               
|   FourOhFourRequest:               
|     HTTP/1.0 404 NOT FOUND                                              
|     Server: gunicorn               
|     Date: Sat, 05 Jun 2021 19:06:17 GMT                                 
|     Connection: close              
|     Content-Type: text/html; charset=utf-8                              
|     Content-Length: 232            
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
|     <title>404 Not Found</title>                                        
|     <h1>Not Found</h1>             
|     <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
|   GetRequest:                      
|     HTTP/1.0 200 OK                
|     Server: gunicorn               
|     Date: Sat, 05 Jun 2021 19:06:10 GMT                                 
|     Connection: close              
|     Content-Type: text/html; charset=utf-8                              
|     Content-Length: 19386          
|     <!DOCTYPE html>                
|     <html class="no-js" lang="en">                                      
|     <head>
|     <meta charset="utf-8">                                              
|     <meta http-equiv="x-ua-compatible" content="ie=edge">
|     <title>Security Dashboard</title>                                   
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <link rel="shortcut icon" type="image/png" href="/static/images/icon/favicon.ico">
|     <link rel="stylesheet" href="/static/css/bootstrap.min.css">
|     <link rel="stylesheet" href="/static/css/font-awesome.min.css">
|     <link rel="stylesheet" href="/static/css/themify-icons.css">   
|     <link rel="stylesheet" href="/static/css/metisMenu.css">
|     <link rel="stylesheet" href="/static/css/owl.carousel.min.css"> 
|     <link rel="stylesheet" href="/static/css/slicknav.min.css">
|     <!-- amchar                    
|   HTTPOptions:                     
|     HTTP/1.0 200 OK                
|     Server: gunicorn               
|     Date: Sat, 05 Jun 2021 19:06:11 GMT                                 
|     Connection: close              
|     Content-Type: text/html; charset=utf-8                              
|     Allow: GET, OPTIONS, HEAD                                           
|     Content-Length: 0              
|   RTSPRequest:                     
|     HTTP/1.1 400 Bad Request                                            
|     Connection: close              
|     Content-Type: text/html                                             
|     Content-Length: 196            
|     <html>                         
|     <head>                         
|     <title>Bad Request</title>                                          
|     <body>                         
|     <h1><p>Bad Request</p></h1>                                         
|     Invalid HTTP Version &#x27;Invalid HTTP Version: &#x27;RTSP/1.0&#x27;&#x27;
|     </body>                        
|_    </html>                        
| http-methods:                      
|_  Supported Methods: GET OPTIONS HEAD                                   
|_http-server-header: gunicorn                                            
|_http-title: Security Dashboard                                          
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin
```

## PORT 80 (HTTP)
<img src="https://imgur.com/aJ9bm0R.png"/>

We can enumerate what's on the web page

<img src="https://imgur.com/izT44rx.png"/>

<img src="https://imgur.com/ccbsjlC.png"/>

Then I saw we can download pcap file

<img src="https://imgur.com/CNG3vV1.png"/>

But that file was empty

<img src="https://imgur.com/emzgSVV.png"/>

I ran `dirsearch` to fuzz for files and directories

<img src="https://imgur.com/vPFO2qd.png"/>

After running the dirsearch I saw that some packets were captured

<img src="https://imgur.com/sjxaZF7.png"/>

I kept banging my head against the wall , I went to thier twitter to see the announcment of this box as that might give a hint 

<img src="https://i.imgur.com/LJyboqr.png"/>

Here It referes to `Flask` and `Cap` which they are refering to pcap files , so here I though maybe there's SSTI involved in flask application so I started to try the payload like `{{7*7}}`

<img src="https://imgur.com/vCVtn1q.png"/>

It didn't work ,here I wasted majority of my time thinking it has something to do with flask SSTI exploit but I was going into a rabbit hole

Some time passed and I just started to switch between different numbers on Security Snapshots PCAP files, I tried looking at files /data/1,2,3,4,5,6,... but those pcap files were generated when I was making a request on the machine ,scanning the machine or doing fuzzing so this was a dead end until I send a request `/data/0`

<img src="https://i.imgur.com/S1NHZCg.png"/>

On opening this file with `wireshark` 

<img src="https://i.imgur.com/XOEZ3ji.png"/>

There are some things to note

First , we can see that there are local IP addresses which means this PCAP file is from the target machine,

Second , we can see port 21 which is the port number for FTP (File Transfer Protocl)

Third ,the user name `nathan`

Fourth,the password `Buck3tH4TF0RM3!`

And lastly the file being retreived from FTP `note.txt`

So the creds we found are for FTP so let's try those

## PORT 21 (FTP)

<img src="https://imgur.com/vcV1jgY.png"/>

And we got the user.txt , now let's these same creds on SSH maybe we can login through this on the machine

## PORT 22 (SSH)

<img src="https://imgur.com/0M3eSN9.png"/>

And boom we are in the machine, now let's check `sudo -l`

<img src="https://imgur.com/LIeTitU.png"/>

It seems we are not in sudoers group, so the next thing I wanted to check if web application was actually made on flask as SSTI didn't work so I went to `/var/www/html`

<img src="https://imgur.com/Ew6faD1.png"/>

And this indeed looks like a flask applicaiton ,so I decided to see the source code

<img src="https://imgur.com/Ew6faD1.png"/>

<img src="https://i.imgur.com/LA1kqI5.png"/>

Here we can see something intersting , python3 is being used and user id is being set to 0 which is of `root` user and then it's capturing packets with tcpdump so this made me think that by default we cannot do this with python3 so I tried to look for capabilites on the machine and what these are that ,capabilities are special attributes in the linux kernel that grant processes and binary executables specific privileges that are normally reserved for processes whose effective user ID is 0.

So let's search for capbilites using this command 

```bash
getcap -r / 2>/dev/null
```

<img src="https://i.imgur.com/DkdYK9T.png"/>

We can see here that python3 has `cap_setuid` which manipulates process ID

<img src="https://imgur.com/OBfibOv.png"/>

<img src="https://i.imgur.com/Z4v8Juc.png"/>

We could have found this capbility with linpeas as well

<img src="https://imgur.com/0hJj3zQ.png"/>

<img src="https://i.imgur.com/HILTw8Z.png"/>

Since python3 has a capbility we can easily get a shell from here by setting uid to 0 ( which is root user's id) ,so let's visit gtfobins

<img src="https://i.imgur.com/B8woxYY.png"/>
          
<img src="https://i.imgur.com/RbolGVC.png"/>
