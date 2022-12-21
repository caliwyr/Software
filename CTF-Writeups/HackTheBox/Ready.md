# HackTheBox-Ready

## Rustscan
```
rustscan -a 10.10.10.220 -- -A -sC -sV                                        
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.                  
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |                  
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |                  
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'                                                                                            
The Modern Day Port Scanner.                              
________________________________________                                                                                                            
: https://discord.gg/GFrQsGy           :                                                                                                            
: https://github.com/RustScan/RustScan :                                                                                                            
 --------------------------------------
Nmap? More like slowmap.🐢
[~] The config file is expected to be at "/root/.rustscan.toml"                                                                                     
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
Open 10.10.10.220:22                 
Open 10.10.10.220:5080               

PORT     STATE SERVICE REASON         VERSION                                                                                                       
22/tcp   open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)                                                           
5080/tcp open  http    syn-ack ttl 62 nginx                               
|_http-favicon: Unknown favicon MD5: F7E3D97F404E71D302B3239EEF48D5F2         
| http-methods:                                                           
|_  Supported Methods: GET HEAD POST OPTIONS                              
| http-robots.txt: 53 disallowed entries (40 shown)                       
| / /autocomplete/users /search /api /admin /profile                      
| /dashboard /projects/new /groups/new /groups/*/edit /users /help
| /s/ /snippets/new /snippets/*/edit /snippets/*/raw   
| /*/*.git /*/*/fork/new /*/*/repository/archive* /*/*/activity                
| /*/*/new /*/*/edit /*/*/raw /*/*/blame /*/*/commits/*/*     
| /*/*/commit/*.patch /*/*/commit/*.diff /*/*/compare /*/*/branches/new
| /*/*/tags/new /*/*/network /*/*/graphs /*/*/milestones/new
| /*/*/milestones/*/edit /*/*/issues/new /*/*/issues/*/edit        
| /*/*/merge_requests/new /*/*/merge_requests/*.patch                     
|_/*/*/merge_requests/*.diff /*/*/merge_requests/*/edit                   
| http-title: Sign in \xC2\xB7 GitLab                                     
|_Requested resource was http://10.10.10.220:5080/users/sign_in                                                                                     
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port                                               
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete                                                                   
Aggressive OS guesses: Linux 2.6.32 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP 
(Linux 3.4) (93%), Linux 3.16 (93%), Adtran 424RG FTTH gateway (92%), Linux 2.6.39 - 3.2 (92%), Linux 3.1 - 3.2 (92%), Linux 3.11 (92%)
No exact OS matches for host (test conditions non-ideal).                        
```

## PORT 5080 (HTTP)

<img src="https://imgur.com/QFZLkBg.png"/>

<img src="https://imgur.com/yAloxhV.png"/>

<img src="https://imgur.com/Ctp7SqW.png"/>

I tried to use metasploit exploit for gitlab but found it was not vulnerable to because that was for version 12.8.x something and the version that was running on the site was 11.4.7 so looked for an exploit

<img src="https://imgur.com/M3WoNpj.png"/>

Ran the exploit

<img src="https://imgur.com/pEgIo8V.png"/>

And got a shell

<img src="https://imgur.com/EzKn2ZG.png"/>

Stabilized the shell

<img src="https://imgur.com/LOLqKJ5.png"/>

We can see the users on gitlab with id

<img src="https://imgur.com/Gh7Vmi8.png"/>

Using gitlab-rails shell to reset a user's password

<img src="https://imgur.com/1miWgDj.png"/>

<img src="https://imgur.com/bRTRXsC.png"/>

<img src="https://imgur.com/lsmjV7R.png"/>


Going to `/opt` folder found a directory called "backup"

<img src="https://imgur.com/s11ySKA.png"/>

Reading the docker.yml it seems that we are in a privileged container also found `root_pass` it had a password but it didn't worked

<img src="https://imgur.com/4wNBjWm.png"/>

Also I found another password

<img src="https://imgur.com/C34HxoC.png"/>

We got root for the container

<img src="https://imgur.com/LK8DquJ.png"/>

But still we need to breakout from this docker conatiner so use `fdisk -l`

<img src="https://imgur.com/eCB9xEO.png"/>

Now we can see that system is mounted on `/dev/sda2` so following hacktricks for docker escape we can mount this on a folder

<img src="https://imgur.com/1MXWniA.png"/>

<img src="https://imgur.com/tu6FbpU.png"/>

<img src="https://imgur.com/Yf3dFY5.png"/>

Transfer the `id_rsa` key you can find on the host machine's root folder

<Img src="https://imgur.com/ZfFsTcH.png"/>

<img src="https://imgur.com/xuc3ZCB.png"/>

<img src="https://imgur.com/2ZXDJe3.png"/>

And we have a proper root on the box
 