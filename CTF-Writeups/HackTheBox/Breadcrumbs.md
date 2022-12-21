# HackTheBox-Breadcrumbs

## Rustscan

```bash

PORT      STATE SERVICE       REASON          VERSION                                                                                               
22/tcp    open  ssh           syn-ack ttl 127 OpenSSH for_Windows_7.7 (protocol 2.0)                                                                
| ssh-hostkey:       
|   2048 9d:d0:b8:81:55:54:ea:0f:89:b1:10:32:33:6a:a7:8f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD1/bmEHFv3nRSf2uH/akLLIfkmpxbSWiVReOdwmJrM2iD9g1gqVHIceIxat222PnYkLHYG23lUQMiTXcvuwBHeB+dMUNv09IHDKCCT9XOTWc
+900zrFLRoyR6LQ2O3vQ+JgWpWlvtZAV6FvcSSK3ai767qIdBNG8SAxwwQZlSxX7D/n28VJlPcXXtzoiSt+lQ1T1sq7qIXPM2CyY7qoTLjcvDz/IYqbXbinsLLOCZ9MnRnDbE8E9tLeAJGcxhpNg
k0LNN6xGbj49zVhy1TRrVNhh4RD+uczVqufMQIHdCnL61p9ZIepQxhJvwSf4IHH+oaM6wy3Yu0W6pg5wQWXIkj                                                              
|   256 1f:2e:67:37:1a:b8:91:1d:5c:31:59:c7:c6:df:14:1d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBMPvEspRGrd2/vma82j25vli6C/Td5Gvl44e9IhXeZOlvojawx4tbo/OdBytc+X9b/OSP01kLK
4Od62NrQmN39s=                       
|   256 30:9e:5d:12:e3:c6:b7:c6:3b:7e:1e:e7:89:7e:83:e4 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAII+TY3313X2GdjXH6r6IrDURWI4H4itbZG41GaktT00D                                                                  
80/tcp    open  http          syn-ack ttl 127 Apache httpd 2.4.46 ((Win64) OpenSSL/1.1.1h PHP/8.0.1)                                                
135/tcp   open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack ttl 127 Microsoft Windows netbios-ssn
443/tcp   open  ssl/http      syn-ack ttl 127 Apache httpd 2.4.46 ((Win64) OpenSSL/1.1.1h PHP/8.0.1)                                                
| ssl-cert: Subject: commonName=localhost                        
| Issuer: commonName=localhost                                            
| Public Key type: rsa                                                    
| Public Key bits: 1024                                                   
| Signature Algorithm: sha1WithRSAEncryption                              
| Not valid before: 2009-11-10T23:48:47                             
| Not valid after:  2019-11-08T23:48:47                    
| MD5:   a0a4 4cc9 9e84 b26f 9e63 9f9e d229 dee0           
| SHA-1: b023 8c54 7a90 5bfa 119c 4e8b acca eacf 3649 1ff6
| -----BEGIN CERTIFICATE-----                         
445/tcp   open  microsoft-ds? syn-ack ttl 127      
3306/tcp  open  mysql?        syn-ack ttl 127
| fingerprint-strings:                                                    
|   NULL, SIPOptions:                              
|_    Host '10.10.14.196' is not allowed to connect to this MariaDB server   
5040/tcp  open  unknown       syn-ack ttl 127                             
7680/tcp  open  pando-pub?    syn-ack ttl 127                             
49664/tcp open  unknown       syn-ack ttl 127                             
49665/tcp open  unknown       syn-ack ttl 127                             
49666/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49667/tcp open  unknown       syn-ack ttl 127                             
49668/tcp open  unknown       syn-ack ttl 127                             
49669/tcp open  unknown       syn-ack ttl 127                             

```

## PORT 145/445 (SMB)

I tried to anonymously connect to smb but couldn't

<img src="https://imgur.com/LQg5I3A.png"/>


## PORT 80

<img src="https://imgur.com/Z3gAYRE.png"/>

We can see a button `Check Books` it will take us to `book.php`

<img src="https://imgur.com/MEPkW2b.png"/>

Now here I didn't know any books so I just started with letter `A` so it returned a bunch of books

<img src="https://imgur.com/MVAE0Eb.png"/>

<img src="https://imgur.com/5LWhtMX.png"/>

Viewing these dialog boxes doen't really help us so I intercepted the request with `Brup Suite`

<img src="https://imgur.com/10iH6t9.png"/>

Here we can see a paramter `book` which is taking a filename so there's a chance that LFI (Local File Inclusion) exists here so to test it for `index.php`

<img src="https://i.imgur.com/4LdjMlh.png"/>

It throws an error as index.php is not in `/books` directory so we need to go parent directory where index.php is  using `../`

<img src="https://imgur.com/zCU1HwZ.png"/>

So it does work we can see the source code of `index.php` now since this is a windows machine we can try to view the hosts file

`../../../../../../WINDOWS/system32/drivers/etc/hosts`

<img src="https://imgur.com/Il6GP72.png"/>

We saw previously from erros regarding `bookController.php` so let's try to read the file

`../../../../../../Users/www-data/Desktop/xampp/htdocs/includes/bookController.php`

<img src="https://i.imgur.com/am9oeHm.png"/>

On reading we can `db.php` so maybe there must be some credentials we can find

`../../../../../../Users/www-data/Desktop/xampp/htdocs/db/db.php`

<img src="https://i.imgur.com/r5TgOBi.png"/>

Although the port is open to use (3306) but still we are not allowed to connect to mysql service

<img src="https://imgur.com/0WikV7Z.png"/>

I tried to read the apache error log and was sucessful in reading so we can do Log poisining to get RCE

`../../../../../../Users/www-data/Desktop/xampp/apache/logs/error.log`

<img src="https://imgur.com/wv5m5kQ.png"/>


So in `User-Agent` we will add a php GET parameter

<img src="https://i.imgur.com/WsCsBFZ.png"/>

`User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0`

Tried doing this but couldn't get LFI to RCE so went step back to do fuzzing with `dirsearch`

<img src="https://imgur.com/vzXvlwS.png"/>

Found a directory named portal `portal`

<img src="https://imgur.com/t1OR2K5.png"/>

We can try to signup an account on the site

<img src="https://imgur.com/qM1ceJ4.png"/>

After going through all the site I read the `login.php` page I found it was using `authController.php` page

<img src="https://i.imgur.com/YxczgcT.png"/>

<img src="https://i.imgur.com/wEQhrYt.png"/>


We can see that there's a JWT token involved also there's a php file `cookie.php` and we can see the salt being used in there to generate `PHPSESSID`

<img src="https://i.imgur.com/qyYkzp9.png"/>

Also we can see in `files.php` that username should be "paul"

<img src="https://i.imgur.com/aP0GbS3.png"/>

So going to JWT.io to create a token for `paul`

<img src="https://imgur.com/oMCB74C.png"/>

Then generating PHPSESSION

<img src="https://imgur.com/MaiI4g6.png"/>

<img src="https://i.imgur.com/EeILglR.png"/>

Here I ran the file in loop because of the random number it's going to take in generating the cookie so that cookie worked when I replaced it with the current cookie

<img src="https://imgur.com/eZkrlk5.png"/>

After hitting refresh the user got changed and we logged in as `paul`

<img src="https://imgur.com/iYvg5X5.png"/>

Going to `File Management` we can upload files but there's a restriction that only zip files are allowed

<img src="https://imgur.com/xbNmpHf.png"/>

Testing for uploading a zip file

<img src="https://imgur.com/D68y8bk.pnghttps://imgur.com/D68y8bk.png"/>

On uploading it gives us an error 

<img src="https://imgur.com/O4yvyIl.png"/>

So Intercepting the request we can see that there's a `.zip` extension that will added to a file name we can by pass it by adding a .php extension

<img src="https://i.imgur.com/VGli5Tu.png"/>

So I downloaded  a php script from https://github.com/flozz/p0wny-shell, copied contents of the `shell.php` file then pasted the contents along with adding `.php` file extension

<img src="https://imgur.com/w6Qv2xn.png"/>

<img src="https://imgur.com/bxMtx4j.png"/>

<img src="https://imgur.com/6spI1li.png"/>

Host `ncat64.exe` on your local machine

<img src="https://imgur.com/VfSwkoe.png"/>

And download it on the target machine 

<img src="https://imgur.com/AlVoq2w.png"/>

<img src="https://imgur.com/NcjR1CL.png"/>

<img src="https://i.imgur.com/xn6DiCu.png"/>

We can see a folder `pizzaDeliveryUserData`

<img src="https://i.imgur.com/HXTcloE.png"/>

There's a user `juliette` 

<img src="https://i.imgur.com/2jMPmV3.png"/>

So going back to that directory we can see the json file for the user and can find credentials in there

<img src="https://i.imgur.com/zB6LjmV.png"/>

<img src="https://i.imgur.com/Abzl7dn.png"/>

There's ssh port open on the machine we can try to login through ssh using these credentials

<img src="https://imgur.com/AoJ97Xq.png"/>

<img src="https://imgur.com/Ioawt8O.png"/>

Looking at the contents of `todo.html`

<img src="https://imgur.com/TAsD1fM.png"/>

<img src="https://imgur.com/EG8WWEn.png"/>

As the html file says about `Stick Notes` let's see if we can find where Windows saves sticky notes so going to this link I was able to find where the notes were stored

https://www.thewindowsclub.com/where-are-sticky-notes-saved-in-windows-10

<img src="https://imgur.com/SZtJywt.png"/>

<img src="https://imgur.com/EA95y7Q.png"/>

Now to save this on our machine we need to transfer it by creating a smb share on our local machine and making sure it has both read and write permissions so doing `nano /etc/samba/smb.conf`

<img src="https://imgur.com/R3gAkUZ.png"/>

<img src="https://i.imgur.com/4LW7Pep.png"/>

Start the service and transfer the file using `copy filename \\ip\share`

<img src="https://imgur.com/2GId8WP.png"/>

<img src="https://i.imgur.com/8hLsdPC.png"/>
 
 Make sure to copy all plum files and unfortunately you will need to transfer these files to Windows and copy them in the same location where you found these files on the target machine 
 
 <img src="https://i.imgur.com/d1jn9NV.png"/>
 
 Now just launch `Sticky Notes` application on Windows
 
 <img src="https://i.imgur.com/ma2nTGp.png"/>
 
 Now that we got the password for another use `development` we can access his folder and see what's in there
  
 <img src="https://imgur.com/nyj3tNA.png"/>
 
 <img src="https://imgur.com/iCoxTND.png"/>
 
 Here we see a binary called `Krypter_Linux` so again copy that file to local machine's smb share
 
 <img src="https://imgur.com/Z97sY5l.png"/>
 
 <img src="https://imgur.com/SXHjnrP.png"/>
 
 
 Running `strings` command on binary we can see a domain name on port 1234 
 
 <img src="https://i.imgur.com/Yc7scMM.png"/>

Let's further analyze the binary with `Ghidra`

<img src="https://i.imgur.com/SKCJEja.png"/>

We can see that it's in the form of a  GET parameters so we can send a request to that port with this data but before we do that let's do port forwarding for port 1234

 So doing dynamic port forwarding through ssh
 
 <img src="https://imgur.com/VRUSftS.png"/>
 
Now let's make the request to that port 

<img src="https://imgur.com/kgYU55E.png"/>

We get an aes key but don't get a password so we can try to sql injection on the parameters by using `sqlmap`

<img src="https://imgur.com/41i2ptd.png"/>

<img src="https://imgur.com/Q38uHel.png"/>

Now we have the encrpyted text and then aes key so we need to decrypt it , I visited this online tool 

https://www.devglan.com/online-tools/aes-encryption-decryption

<img src="https://imgur.com/iBwnlLN.png"/>

<img src="https://imgur.com/omD2L5C.png"/>

Now we just need to decode it from base64

<img src="https://imgur.com/ntbSHhm.png"/>

<img src="https://imgur.com/HsZ18YM.png"/>

And that's it we got administrator on the machine

# Things Learned

1. If you got LFI always look around in the source code you will find how the application works
2. If you find a binary make sure to analyze what's in there
3. We can transfer files from windows to linux by running smb service on linux machine