# HackTheBox-Atom

## Rustscan
```bash
PORT     STATE SERVICE      REASON          VERSION                                                                                         
80/tcp   open  http         syn-ack ttl 127 Apache httpd 2.4.46 ((Win64) OpenSSL/1.1.1j PHP/7.3.27)                                                 
| http-methods:                  
|   Supported Methods: GET POST OPTIONS HEAD TRACE
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27
|_http-title: Heed Solutions    
135/tcp  open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
443/tcp  open  ssl/http     syn-ack ttl 127 Apache httpd 2.4.46 ((Win64) OpenSSL/1.1.1j PHP/7.3.27)                                                 
| http-methods:                  
|   Supported Methods: GET POST OPTIONS HEAD TRACE
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27
|_http-title: Heed Solutions                            
| ssl-cert: Subject: commonName=localhost                                      
| Issuer: commonName=localhost                                               
| Public Key type: rsa                                              
| Public Key bits: 1024                        
| Signature Algorithm: sha1WithRSAEncryption                              
| Not valid before: 2009-11-10T23:48:47                             
| Not valid after:  2019-11-08T23:48:47                    
| MD5:   a0a4 4cc9 9e84 b26f 9e63 9f9e d229 dee0              
| SHA-1: b023 8c54 7a90 5bfa 119c 4e8b acca eacf 3649 1ff6
445/tcp  open  microsoft-ds syn-ack ttl 127 Windows 10 Pro 19042 microsoft-ds (workgroup: WORKGROUP)
5985/tcp open  http         syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)                                                                 
|_http-server-header: Microsoft-HTTPAPI/2.0                               
|_http-title: Not Found              
6379/tcp open  redis        syn-ack ttl 127 Redis key-value store
7680/tcp open  pando-pub?   syn-ack ttl 127                               

```

## PORT 135/445 (SMB)

We can see which shares are there

<img src="https://imgur.com/uD8EngL.png"/>

Now to see which we can read as anonymous

<img src="https://imgur.com/bngVqSx.png"/>

It seems we can read and write `Software_Updates` share

<img src="https://imgur.com/h3lc2bM.png"/>

There's a document available too so let's download it

<img src="https://imgur.com/AxiJUHM.png"/>

So the document tells about a note taking application named `Heed` and it's a client based application there's no interaction with the server but it does get's an update though client's folder and we have seen three client's folder i.e client1,client2,client3, so let's just visit port 80

<img src="https://imgur.com/NfKZMLg.png"/>

<img src="https://imgur.com/oxSqoZB.png"/>

## PORT 80 (HTTP)

<img src="https://imgur.com/SUgIsXr.png"/>

Scrolling a bit down we can see a download option and an email `MrR3boot@atom.htb`

<img src="https://imgur.com/YoOCKt5.png"/>

So first let's add the domain `atom.htb` to `/etc/hosts` file and fuzz for subdomains and also to fuzz for files and directories using `gobuster`

<img src="https://imgur.com/RJ1edoR.png"/>

Running gobuster to fuzz for files

<img src="https://imgur.com/XKu2Hvm.png"/>

Fuzzing for subdomains 

<img src="https://imgur.com/mwcwrls.png"/>

Didn't find one so we would just have to download the heed note taking application

<img src="https://imgur.com/mwcwrls.png"/>

<img src="https://imgur.com/nZm0guT.png"/>

<img src="https://imgur.com/N4wXWBY.png"/>

So I had to switch to my windows machine as this was a windows application

<img src="https://i.imgur.com/UOFwOB1.png"/>

<img src="https://i.imgur.com/xbIBPjn.png"/>

This tells us that this is an electron application

<img src="https://i.imgur.com/xbIBPjn.png"/>

<img src="https://i.imgur.com/zvjBUWL.png"/>

So knowing that it's an electron app I searched on goolge for getting a RCE through it

<img src="https://imgur.com/x167NBE.png"/>

<img src="https://imgur.com/DAszhh0.png"/>

It says here that it will update from `latest.yml`

<img src="https://imgur.com/CzgMinR.png"/>

<img src="https://imgur.com/0m0z1NF.png"/>


## Exploit

So first we generate our payload with name having a single quote

<img src="https://imgur.com/dwDF7M2.png"/>

Now we need to generate a sha512 sum hash and encode it to hex and then further encode it to base64

<img src="https://imgur.com/13mxXzP.png"/>


```
093RMZA6MwaxL21rB2eTb14NNIH8+bfGjldpX5bFLvlALJJpKvi8Gm+TGXmqW/ROJsy+TEcGyDQk
djSS7Avnow==
```

Host this payload on your local machine using python3

<img src="https://imgur.com/NgsksYv.png"/>

Create a `latest.yml` file

<img src="https://imgur.com/3PIKSTm.png"/>

Upload the yml file in smb share

<img src="https://imgur.com/vVm6rdo.png"/>

Run the meterpeter listener

<img src="https://imgur.com/5jWyyWX.png"/>

<img src="https://imgur.com/XAydhPm.png"/>

So for escalating privileges I first ran `getprivs` to show privileges for the current user

<img src="https://imgur.com/QtKKaxR.png"/>

Going into `Program Files`

<img src="https://imgur.com/mbLqD4B.png"/>

Further going into `Redis` folder

<img src="https://imgur.com/2n52hBM.png"/>

We see `redis.windows-service.conf` and there's a password for redis cli

<img src="https://i.imgur.com/5XghlFZ.png"/>

<img src="https://imgur.com/tjdBlpp.png"/>

Run `info` command

<img src="https://imgur.com/kgLEeNM.png"/>

<img src="https://imgur.com/64uCZrL.png"/>

<img src="https://imgur.com/LFafaYJ.png"/>

Redis stores data in database and we can there is only on database , we can access it by the command `SELECT 0`

<img src="https://imgur.com/yfVbwEj.png"/>

<img src="https://imgur.com/42W7KDP.png"/>

Now to access the KEY we need to first know it's data type, in redis there are 5 data types

1. String
2. Hash
3. List
4. Sets
5. Sorted Sets

<img src="https://imgur.com/c5r8BUx.png"/>

<img src="https://imgur.com/eRIHg0u.png"/>

<img src="https://imgur.com/laWYI3Z.png"/>


Going to jason's `Download` direcotry we can find `PortableKanban` which is a tak managment tool for windows 

<img src="https://imgur.com/U7fFncB.png"/>

Reading the `User Guide.pdf`  portable kanban we can only user available is `Administartor` but we can't get the passoword as the guide says if the data is lost there is not way in retreiving it

<img src="https://imgur.com/LR7OxV0.png"/>

We can see that we are on the last version of portable kanban

<img src="https://i.imgur.com/3wZosbE.png"/>

So this is the encrypted password which we can't retrieve

<img src="https://i.imgur.com/iXDmZeQ.png"/>

But there's an exploit for it 

<img src="https://imgur.com/KuTxxzD.png"/>

Now we extracted the encrypted portable kanban passowrd from redis key and we need to save the contents in a file `PortableKanban.pk3` but on running the exploit it showed errors so we may need to edit the exploit

<img src="https://imgur.com/mUDE8eY.png"/>

After editing it will decrypt the password

<img src="https://i.imgur.com/0PICIdt.png"/>

<img src="https://imgur.com/AbhqXWl.png"/>

Now since port 5985 was open which is for winrm we will use `evilwinrm` to login

<img src="https://imgur.com/w41mfJS.png"/>

Evilwinrm was acting wierd so I downloaded the windows payload I used earlier to get foothold and ran the payload with cmd while listening at meterpreter for connections

<img src="https://imgur.com/Drzdt25.png"/>

<img src="https://imgur.com/Q8jJ29o.png"/>

