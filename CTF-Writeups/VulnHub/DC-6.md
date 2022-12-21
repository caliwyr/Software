# Vulnhub-DC 6

## Rustscan


```bash


rustscan -a 192.168.1.11 -- -A -sC -sV
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.                  
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |       
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |                  
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'                  
The Modern Day Port Scanner.                                                                                                                        
________________________________________                                                                                                            
: https://discord.gg/GFrQsGy           :                                  
: https://github.com/RustScan/RustScan :                                  
 --------------------------------------                                   
😵 https://admin.tryhackme.com                                            

[~] The config file is expected to be at "/root/.rustscan.toml"                                                                                     
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 

Open 192.168.1.11:22                 
Open 192.168.1.11:80                 


PORT   STATE SERVICE REASON         VERSION

22/tcp open  ssh     syn-ack ttl 64 OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)                                                                   
| ssh-hostkey:       
|   2048 3e:52:ce:ce:01:b6:94:eb:7b:03:7d:be:08:7f:5f:fd (RSA)      
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDDHiBBFUtpw1T9DZyoXpMp3kg25/RgmGZRFFmZuTfV9SJPxJCvrQXdM6P5GfFLFcgnLlcOBhBbv33N9HvWisycRypK0uLK26bntqfyTAFCdM
Xcud7fKNgRBxJdN8onwl4Hly3wzRBJxFWqTdD1RF8viYH4TYIs5+WLpN7KihosjpbwzPpOnbDQZUw7GdHvosV7dFI6IMcF57R4G5LzSgV66GACNGxRn72ypwfOMaVbsoxzCHQCJBvd8ULL0YeAFt
NeHoyJ8tL3dZlu71Wt9ePYf7ZreO+en701iDqL6T/iyt3wwTDl7NwpZGj5+GrlyfRSFoNyHqdd0xjPmXyoHynp                                                              
|   256 3c:83:65:71:dd:73:d7:23:f8:83:0d:e3:46:bc:b5:6f (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBE+jke+7np4l7EWf0wgySSp3MtYFcI6klVOWm7tDjas8eDxc9jYOhR4uK7koa2CkQPDd18XJSt
0yNAGQFBb7wzI=                       
|   256 41:89:9e:85:ae:30:5b:e0:8f:a4:68:71:06:b4:15:ee (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAII1mnJveN8yJySEDhG8wjYqtSKmcYNdX5EVqzxYb92dP
80/tcp open  http    syn-ack ttl 64 Apache httpd 2.4.25 ((Debian))
| http-methods:                      
|_  Supported Methods: GET HEAD POST OPTIONS                              
|_http-server-header: Apache/2.4.25 (Debian)                              
|_http-title: Did not follow redirect to http://wordy/                    
|_https-redirect: ERROR: Script execution failed (use -d to debug)                                                                                  
MAC Address: 08:00:27:59:AC:2F (Oracle VirtualBox virtual NIC)                                                     

```

We have two ports open 22 and 80 so we can't do much with SSH since we don't know the username , we will be enumearting port 80

## PORT 80 (HTTP)

Going to web server it will shows that it's being reidrected to a domain `wordy`

<img src="https://imgur.com/Lca4YSD.png"/>

So let's add the domain to `/etc/hosts`

<img src="https://imgur.com/yE1Gn40.png"/>

After adding the domain name , let's refresh the page

<img src="https://imgur.com/h7LOMQk.png"/>

Now it loads , since this is a wordpress site we can use `wpscan` to enumerate for users

<img src="https://imgur.com/vkZVTAc.png"/>

<img src="https://imgur.com/twpmdJq.png"/>

And it founds some users , we can also find plugins installed on wordpress with nse (nmap scripting engine)

<img src="https://imgur.com/Ne32HQx.png"/>

I tried to find some exploits but they weren't beneficial to us as there was a xss exploit for `akismet` and changing user permissions through  `user-role-editor` exploit so in the end we have to brute force the credentials.

There was a hint given to use regarding brute forcing that we must grep for `k01` so I did that 

<img src="https://imgur.com/N6xAZAs.png"/>

<img src="https://imgur.com/8kc0AzO.png"/>

We'll get the password for `mark`

<img src="https://imgur.com/Yln5koJ.png"/>

After logging in , we can see that we are not `administrator` so that where `user-role-editor` comes into play. 

<img src="https://imgur.com/Xc5jtfe.png"/>

I tried to exploit this vulnerability through metasploit but it seems that we needed to load this module , I failed to do this so I approached to exploit this manually

<img src="https://imgur.com/WMIAkYD.png"/>

<img src="https://imgur.com/40FyECF.png"/>

Click on user's update profile button and intercept it 

<img src="https://imgur.com/WGKAebp.png"/>

Now add `ure_other_roles=administrator` this paramter 

<img src="https://imgur.com/OISjiSZ.png"/>

<img src="https://imgur.com/1HbNFEk.png"/>

And now we have become an admin on wordpress site ,cool. Add a php reverse shell in `404.php` template

<img src="https://imgur.com/2wbJXUi.png"/>

But it wasn't getting updated 

<img src="https://imgur.com/tJQ8dKw.png"/>

So last option was to go with `metasploit`

<img src="https://imgur.com/kwuMbQD.png"/>

<img src="https://imgur.com/Ws6aIUO.png"/>

For stabilizing the shell

<img src="https://imgur.com/4tjJyvu.png"/>

We see a note in mark's home directory

<img src="https://imgur.com/4f0YVEx.png"/>

<img src="https://imgur.com/wKhbJNB.png"/>

With that password we switched to user `graham`, if we do `sudo -l`

<img src="https://imgur.com/CDvZ1wg.png"/>

Edited the script 

<img src="https://imgur.com/R5rnH7e.png"/>

<img src="https://imgur.com/TRln7NG.png"/>

<img src="https://imgur.com/w00sUSi.png"/>

Now it's so much easier here , we can go GTFOBINS to see what we can do with nmap running as sudo

<img src="https://imgur.com/FteX0CV.png"/>

<img src="https://imgur.com/8NeABkV.png"/>

<img src="https://imgur.com/pUaBE0F.png"/>
