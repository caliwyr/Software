# TryHackMe-DevelPy

## NMAP

```
Host is up (0.15s latency).                                                                                          
Not shown: 65533 closed ports                                                                                        
PORT      STATE SERVICE           VERSION                                                                            
22/tcp    open  ssh               OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)                       
| ssh-hostkey:                                                                                                       
|   2048 78:c4:40:84:f4:42:13:8e:79:f8:6b:e4:6d:bf:d4:46 (RSA)                                                       
|   256 25:9d:f3:29:a2:62:4b:24:f2:83:36:cf:a7:75:bb:66 (ECDSA)                                                      
|_  256 e7:a0:07:b0:b9:cb:74:e9:d6:16:7d:7a:67:fe:c1:1d (ED25519)                                                    
10000/tcp open  snet-sensor-mgmt?                                                                                    
| fingerprint-strings:                                                                                               
|   GenericLines:                                                                                                    
|     Private 0days                                                                                                  
|     Please enther number of exploits to send??: Traceback (most recent call last):
|     File "./exploit.py", line 6, in <module>                                                                       
|     num_exploits = int(input(' Please enther number of exploits to send??: '))
|     File "<string>", line 0                                                                                        
|     SyntaxError: unexpected EOF while parsing                                                                      
|   GetRequest:                                                                                                      
|     Private 0days                                                                                                  
|     Please enther number of exploits to send??: Traceback (most recent call last):                                 
|     File "./exploit.py", line 6, in <module>                                                                       
|     num_exploits = int(input(' Please enther number of exploits to send??: '))
|     File "<string>", line 1, in <module>
|     NameError: name 'GET' is not defined
|   HTTPOptions, RTSPRequest:  
|     Private 0days
|     Please enther number of exploits to send??: Traceback (most recent call last):
|     Please enther number of exploits to send??: Traceback (most recent call last):                                 
|     File "./exploit.py", line 6, in <module>                                                                       
|     num_exploits = int(input(' Please enther number of exploits to send??: '))                                     
|     File "<string>", line 0                                                                                        
|     SyntaxError: unexpected EOF while parsing                                                                      
|   GetRequest:                                                                                                      
|     Private 0days                                                                                                  
|     Please enther number of exploits to send??: Traceback (most recent call last):                                 
|     File "./exploit.py", line 6, in <module>                                                                       
|     num_exploits = int(input(' Please enther number of exploits to send??: '))
|     File "<string>", line 1, in <module>
|     NameError: name 'GET' is not defined
|   HTTPOptions, RTSPRequest:  
|     Private 0days
|     Please enther number of exploits to send??: Traceback (most recent call last):
|     File "./exploit.py", line 6, in <module>
|     num_exploits = int(input(' Please enther number of exploits to send??: '))
|     File "<string>", line 1, in <module>
|     NameError: name 'OPTIONS' is not defined
|   NULL: 
|     Private 0days
|_    Please enther number of exploits to send??:
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerpri
nt at https://nmap.org/cgi-bin/submit.cgi?new-service :

```

## PORT 10000

<img src="https://imgur.com/J9ACAKN.png"/>

__import__() is not really necessary in everyday Python programming. Its direct use is rare. But sometimes, when there is a need of importing modules during the runtime, this function comes quite handy.

Now we can exploit and insert this line to import os module and run bash we could do this as assigning it to a variable


<img src="https://imgur.com/izJGYFf.png"/>

Save the `credentials.png` on your local machine

<img src="https://imgur.com/ogvUZML.png"/>

Now I had now idea what was that but I had heared of a lanaguage like that looking at the results of `exiftool` it pointed me towards `Mondrian` on googling I came to know that `Piet Mondrian` is a Dutch artist best known for his abstract paintings and googling it even more resulted in that `Piet` is some kind of programming langauge


<img src="https://imgur.com/aYEyzyJ.png"/>

<img src="https://imgur.com/WHG87ct.png"/>

I found online interpreter for `piet` programming lanaguage https://www.bertnase.de/npiet/npiet-execute.php

But this was a rabbithole

<img src="https://imgur.com/0eKYhSt.png"/>


Now `king`'s home directory has `run.sh` and `root.sh` what we want do is somehow put a reverse shell in root.sh because it is running as `root` user in cronbjobs everyminute so delete that file make a new one so we can edit it set up a netcat listener to capture it

You can use bash or netcat reverse shell , I used the netcat reverse shell

<img src="https://imgur.com/NIJe5m6.png"/>

