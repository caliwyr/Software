# HackTheBox-Chatterbox


## Rustscan

I first ran rustscan because it was taking way longer for nmap to scan all ports


```bash
rustscan --batch-size 45000 -a 10.10.10.74
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
Open 10.10.10.74:9255                                                     
Open 10.10.10.74:9256
[~] Starting Script(s)                                                    
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.80 ( https://nmap.org ) at 2021-05-13 02:38 PKT
Initiating Ping Scan at 02:38
Scanning 10.10.10.74 [4 ports]
Completed Ping Scan at 02:38, 0.23s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 02:38
Completed Parallel DNS resolution of 1 host. at 02:38, 0.30s elapsed
DNS resolution of 1 IPs took 0.30s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating SYN Stealth Scan at 02:38
Discovered open port 9256/tcp on 10.10.10.74
Discovered open port 9255/tcp on 10.10.10.74
Completed SYN Stealth Scan at 02:38, 0.22s elapsed (2 total ports)
Nmap scan report for 10.10.10.74
Host is up, received echo-reply ttl 127 (0.19s latency).
Scanned at 2021-05-13 02:38:13 PKT for 1s

PORT     STATE SERVICE REASON
9255/tcp open  mon     syn-ack ttl 127
9256/tcp open  unknown syn-ack ttl 127
```

## NMAP


```bash
PORT     STATE SERVICE VERSION
9255/tcp open  http    AChat chat system httpd
|_http-favicon: Unknown favicon MD5: 0B6115FAE5429FEB9A494BEE6B18ABBE
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: AChat
|_http-title: Site doesn't have a title.
9256/tcp open  achat   AChat chat system
```

## PORT 9256 (HTTP)

Visiting the 9256 we will just see a message "ERROR"

<img src="https://imgur.com/A33GqVP.png"/>

Also visiting port 9255 we will be redirected back to 9256 so nothing we can do here but from nmap scan it tells that this is `AChat chat system` so let's search for it on google

<img src="https://i.imgur.com/c89PbRj.png"/>

Right off the bat it reutrns with an exploit so let's give this is a try, this repo has two files , one a bash script which will generate the raw payload that we have to edit it in the python script which is the actual exploit which will give the shell

<img src="https://imgur.com/mpQLNrQ.png"/>

<img src="https://i.imgur.com/R0xQoOs.png"/>

Paste the payload in the python script

<img src="https://imgur.com/ABcxm1C.png"/>

Also edit the target ip

<img src="https://i.imgur.com/2ptOY1t.png"/>

Set the meterpreter listener

<img src="https://imgur.com/qhfmhg3.png"/>

But when I run the exploit it gives me a shell but dies suddenly

<img src="https://i.imgur.com/DHnAEpl.png"/>

I also tried by changning the payload from `windows/meterpreter/reverse_tcp` to `windows/shell/reverse_tcp` but it sill died 

<img src="https://imgur.com/udflW6x.png"/>

But using the payload `windows/shell/reverse_tcp` on metepreter I was able to get a shell

<img src="https://imgur.com/8Mc2r22.png"/>

<img src="https://imgur.com/L3Z3lo7.png"/>

To get a meterpreter session let's use the module `post/multi/manage/shell_to_meterpreter`

<img src="https://imgur.com/JXZgNVq.png"/>

<img src="https://i.imgur.com/wgRnZD8.png"/>

I ran winpeas after getting a metepreter uploaded it using `upload file` and saw that we have access to `Administrator` folder

<img src="https://i.imgur.com/FbludpK.png"/>

But we can't access file root. txt , it's weird as we have access to the whole directory

<img src="https://i.imgur.com/D7IRwni.png"/>

I tried to give `read` access to root.txt but it gave access denied then used `cacls` which is a deprecated windows command which is replaced `icacls`

<img src="https://i.imgur.com/zNiar6X.png"/>

It's showing `N` for user Alfred which means no permissions are given to this user on root.txt file , going to the documentation I was able to give rights to this file

https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cacls

<img src="https://i.imgur.com/htuzKDI.png"/>
