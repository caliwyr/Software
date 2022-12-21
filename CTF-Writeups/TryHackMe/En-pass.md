# TryHackMe-Enpass

## Rustscan


```
rustscan -a 10.10.215.65 -- -A -sC -sV

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
Open 10.10.215.65:22
Open 10.10.215.65:8001
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

PORT     STATE SERVICE REASON         VERSION                                                                                                       
22/tcp   open  ssh     syn-ack ttl 61 OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)                                                 
| ssh-hostkey:                                                            
|   2048 8a:bf:6b:1e:93:71:7c:99:04:59:d3:8d:81:04:af:46 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCicax/djwvuiP5H2ET5UJCYL3Kp7ukHPJ0YWsSBUc6o8O/wwzOkz82yJRrZAff40NmLEpbvf0Sxw2JhrtoxDmdj+FSHpV/xDUG/nRE0FU10w
DB75fYP4VFKR8QbzwDu6fxkgkZ3SAWZ9R1MgjN3B49hywgwqMRNtw+z2r2rXeF56y1FFKotBtK1wA223dJ8BLE+lRkAZd4nOr5HFMwrO+kWgYzfYJgSQ+5LEH4E/X7vWGqjdBIHSoYOUvzGJJmCu
m2/MOQPoDw5B85Naw/aMQqsv7WM1mnTA34Z2eTO23HCKku5+Snf5amqVwHv8AfOFub0SS7AVfbIyP9fwv1psbP
|   256 40:fd:0c:fc:0b:a8:f5:2d:b1:2e:34:81:e5:c7:a5:91 (ECDSA)    
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBENyLKEyFWN1XPyR2L1nyEK5QiqJAZTV2ntHTCZqMtXKkjsDM5H7KPJ5EcYg5Rp1zPzaDZxBmP
P0pDF1Rhko7sw=                                                            
|   256 7b:39:97:f0:6c:8a:ba:38:5f:48:7b:cc:da:72:a8:44 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJmb0JdTeq8kjq+30Ztv/xe3wY49Jhc60LHfPd5yGiRx
8001/tcp open  http    syn-ack ttl 61 Apache httpd 2.4.18 ((Ubuntu))                                                                                
| http-methods:                                                           
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: En-Pass

```

So we have 2 ports open , 8001 (HTTP) and 22 (SSH)

## PORT 8001 (HTTP)

<img src="https://imgur.com/Dd8gkUf.png"/>

At the the bottom of the page we see an ecrypted text

<img src="https://imgur.com/qMP24xb.png"/>

Which is ROT13

<img src="https://imgur.com/MRbxT92.png"/>

<img src="https://imgur.com/GTnGyfe.png"/>

We have another text which is encrypted

<img src="https://imgur.com/2W3Z44X.png"/>

This again lead us to nowhere. So I decided to fuzz for directories

<img src="https://imgur.com/GM4xKxS.png"/>

Doing with feroxbuster I found that `/web` has more directories or files in it 

<img src="https://imgur.com/CO3aIlv.png"/>


As we found `/reg.php`

<img src="https://imgur.com/Hed312o.png"/>

There's a input filed where we can type and submit.Trying for RCE by running `id` resulted incorrect

<img src="https://imgur.com/KRZfCn6.png"/>

<img src="https://imgur.com/46bVFWG.png"/>

Looking at the source it's running a php script that is checking for input so here `!preg_ match('/[a-zA-Z0-9]/i` will reject the regular expression pattern for upper and lowercase characters also digits and `explode` is going to split the string into substring using `,`. Then the for loop will run 8 times and it's checking if the string's first character has a length of 2 and last character of the string which is 8th (starting from 0) character must be of length 3 then it's further checking that 5th character and 8th character must not be equal similarly for 3rd and 7th value.

So this means we can only use special characters

`@@,$,$,*,$,!,$,!,@@@`

This will pass the checks as the value on the 0th index is of length 2 `@@`
8th index value is of length 3 `@@@`
Value at 5th index is not similar to the value at 8th index `! , @@@`
And the value at 3rd index is not similar to value at 7th index `*,!`

It's not necessary that this will be the exact string

`$$,!,&,!,^,^,^,*,%%%` This can pass the checks as well

On inputing the string

<img src="https://imgur.com/9TjxTrS.png"/>


While ferxobuster was running in the background there were directories upto `configure`

<img src="https://imgur.com/IKjnlDP.png"/>


I ran dirsearch again and finally found a file

<img src="https://imgur.com/HcvSKzp.png"/>

It's better to run other tools because gobuster was failing for me and feroxbuster didn't find the `key` file

<img src="https://imgur.com/QqG3pEz.png"/>

But I don't know the username so can't really ssh into the machine

<img src="https://imgur.com/haYcBGb.png"/>

<img src="https://imgur.com/wiBIpMt.png"/>

These archives had the same files and some had recrusive archive with content `sadman`

So we have the key which is passpharse of id_rsa and we also have the ssh private key so let's see if we can login 

<img src="https://imgur.com/xOqgOiL.png"/>

And this gives us an error maybe `sandman` isn't the correct username. Looking at the hint we see that it's saying something about bypassing

<img src="https://imgur.com/WtSDW73.png"/>

We know that there is `403.php` page that gives us 403 status code which is  `Forbidden client error`

<img src="https://imgur.com/BhePlIu.png"/>
So I googled for Bypasse scripts and found this so thought about trying and see if this lead us to somewhere

<img src="https://imgur.com/FESweTX.png"/>

I don't think this worked 

<img src="https://imgur.com/m7yKeKL.png"/>

Then I used another script from github
https://github.com/intrudir/403fuzzer

<img src="https://imgur.com/UCTlgHE.png"/>

You can see the status code is 200 but here focus on the length for 200 status code as this the home page (`/`)

<img src="https://imgur.com/m6NYH9A.png"/>

Here we see a change in length of status code 200 which is `917` so let's try using this as our url

<img src="https://imgur.com/i38oAa2.png"/>

And bingo we got the username so now let's ssh into the box

<img src="https://imgur.com/J1StDYN.png"/>

Transfer `psyp64` on the machine

<img src="https://imgur.com/KhWJIkU.png"/>

<img src="https://imgur.com/oCZDfBB.png"/>

A cronjob for root user is running that first change the ownership of `file.yml` then runs the python script and then removes the file.yml also there exists a yaml deserialization vulnerability so we can make a payload for setting SUID on `/bin/bash`

<img src="https://imgur.com/ht9eLu0.png"/>

<img src="https://imgur.com/y8LrFCe.png"/>

<img src="https://imgur.com/fcE3E3i.png"/>

<img src="https://imgur.com/QlUzZIZ.png"/>

We can grab the root flag !!