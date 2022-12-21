# Vulnhub-Literally Vulnerable

## Rustscan

```bash
PORT   STATE SERVICE REASON         VERSION                    
21/tcp open  ftp     syn-ack ttl 64 vsftpd 3.0.3               
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 ftp      ftp           325 Dec 04  2019 backupPasswords
| ftp-syst:                                             
|   STAT:                                                                 
| FTP server status:                                                      
|      Connected to ::ffff:192.168.1.8                                     
|      Logged in as ftp                              
|      TYPE: ASCII                                                        
|      No session bandwidth limit                          
|      Session timeout in seconds is 300                                  
|      Control connection is plain text                                   
|      Data connections will be plain text
|      At session startup, client count was 1                             
|      vsFTPd 3.0.3 - secure, fast, stable                                
|_End of status                                                      
22/tcp open  ssh     syn-ack ttl 64 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                    
| ssh-hostkey:       
|   2048 2f:26:5b:e6:ae:9a:c0:26:76:26:24:00:a7:37:e6:c1 (RSA)      
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCjIkOglOWYfz+TBASrrFUwDGUNBzPhMd6PLVbELdtIRKWEy2IHM2JrlncDFPEh1YTE79HaRbhJLnEI2z+fVLH1hDKafEjvhGdo62uenhZlI5
GUk/b60hqv0yybZftezvRLXQ5Aa9fPxHerRZOktHoRzkS5WeeZmp5Bprm//q5Di8BBnFQERH28hIUTqHBHmSOLMfRPP8OSrC3txB6gk3w2asp7YLio/tb+BljUlxpDUAGZ3laHKEBhkm5936ShDh
OidZ+oduKxy2j3gji9Pk/yDXdt0109knCYW2Wz3Nh6sZBbvhSR6mSeYRmRcgtmSw3GLdA6WPaNqytn51w6uwEd                                                              
|   256 79:c0:12:33:d6:6d:9a:bd:1f:11:aa:1c:39:1e:b8:95 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAnd9KWbuz1oyVBcGqABiFwm+tO2EGRsE5KzvvzYuzjYk/U2tgOx1joZAX/jeii3oK2oW/Kmtu
DA07GPEplj9sY=                                                            
|   256 83:27:d3:79:d0:8b:6a:2a:23:57:5b:3c:d7:b4:e5:60 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMhQsU6o12hyENGgq/DI3I4sWHsJpLCuxITMtMaiwh/A
80/tcp open  http    syn-ack ttl 64 nginx 1.14.0 (Ubuntu)
|_http-favicon: Unknown favicon MD5: D41D8CD98F00B204E9800998ECF8427E
|_http-generator: WordPress 5.3                                           
| http-methods:                      
|_  Supported Methods: GET HEAD POST OPTIONS                              
|_http-server-header: nginx/1.14.0 (Ubuntu)                               
|_http-title: Not so Vulnerable &#8211; Just another WordPress site
|_http-trane-info: Problem with XML parsing of /evox/about
65535/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works

MAC Address: 80:00:0B:3C:4A:7E (Intel Corporate)                          

```

## PORT 21 (FTP)

<img src="https://imgur.com/8JYkfjh.png"/>

We get a file having passwords

<img src="https://imgur.com/Tyv3afr.png"/>

## PORT 80 (HTTP)

We have a wordpress site but css isn't loaded properly because it's using literally.vulnerable

<img src="https://imgur.com/9folHju.png"/>

<img src="https://imgur.com/m2X7Dxy.png"/>

So let's add it to our /etc/hosts file

<img src="https://imgur.com/sSpANcS.png"/>

Running wpscan against the wordpress site we only find 1 user (admin)

<img src="https://imgur.com/p1UzSwv.png"/>

<img src="https://imgur.com/JrhDxaI.png"/>

Tried brute forcing against user `admin`

<img src="https://imgur.com/EvyKIon.png"/>

So I ran wpscan again for enumerating plugins

<img src="https://imgur.com/Sv3xHCZ.png"/>

Let's just keep it running in the background and enumerate another http port




## PORT 65535 (HTTP)

<img src="https://imgur.com/TVRrZBr.png"/>

Ran dirbuster on that port but nothing seemed interesting 

<img src="https://imgur.com/HEBol5s.png"/>

Used the wordlist from seclists

<img src="https://imgur.com/5wvcrAg.png"/>

And found `/phpcms`

<img src="https://imgur.com/nyBk6AP.png"/>

We find a post regarding a note for `john`

<img src="https://imgur.com/RJETW7C.png"/>

Ran wpscan on this wordpress site and found two usernames

<img src="https://imgur.com/HEd20JJ.png"/>

And we found a valid password for `maybeadmin` by using the passwords we found from ftp

<img src="https://imgur.com/uoHE2i4.png"/>

We got into the dashboard but we are not admin

<img src="https://imgur.com/24WwnoG.png"/>

So we cannot do anything but there was a password protected post maybe we can see what's in there

<img src="https://imgur.com/m78KNzd.png"/>

<img src="https://imgur.com/Uy9vfuU.png"/>

Let's login as `notadmin`

<img src="https://imgur.com/OS3jnjK.png"/>

Edit the `404.php` page of the theme with a php reverse shell

<img src="https://imgur.com/uCJcZBs.png"/>

But it seems we can't do it manually so my next option is to use metasploit wordpress upload shell exploit

<img src="https://imgur.com/tMVHc0N.png"/>

<img src="https://imgur.com/mqVL3lU.png"/>

<img src="https://imgur.com/dqbcYun.png"/>

I used a php reverse shell so that I can get a stabilized one

<img src="https://imgur.com/OWvKDkR.png"/>

We see some files in `doe`'s  directory

<img src="https://imgur.com/TrCUTK8.png"/>

On running the binary `itseasy` it was printing the current path 

<img src="https://imgur.com/pLf3LOf.png"/>

<img src="https://imgur.com/msGpCvh.png"/>

So this means we must export `PWD` and tamper with it

<img src="https://imgur.com/3Sq6Y9D.png"/>

So here I edit the environmental variable `PWD` with a command which will run the whoami command and save it's output in `/tmp/output`

<img src="https://imgur.com/aLmhFbz.png"/>

So it means we can run commands as `john` through this binary so I created a .ssh folder in john's directory now I can add id_rsa.pub in authorized_keys file

<img src="https://imgur.com/NRxlYWL.png"/>

<img src="https://imgur.com/yx534HM.png"/>

<img src="https://imgur.com/uL6a7oe.png"/>

We get the user flag plus a note

<img src="https://imgur.com/smYVfvZ.png"/>

On running find command for finding files owned by `john`

<img src="https://imgur.com/Ap3rt1p.png"/>

<img src="https://imgur.com/Hn4IUME.png"/>

<img src="https://imgur.com/a1oGPxD.png"/>

Now we can run `test.html` file as root but there it isn't on the machine and we cannot make that file as john does not have the permissions but `www-data` so going back to that user

<img src="https://imgur.com/uaIAod2.png"/>

<img src="https://imgur.com/hIXysIi.png"/>

<img src="https://imgur.com/XsZQ3tP.png"/>