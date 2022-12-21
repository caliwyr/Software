# HackTheBox-Spectra

## NMAP

```
PORT     STATE SERVICE          VERSION                                   
22/tcp   open  ssh              OpenSSH 8.1 (protocol 2.0)
| ssh-hostkey:
|_  4096 52:47:de:5c:37:4f:29:0e:8e:1d:88:6e:f9:23:4d:5a (RSA)
80/tcp   open  http             nginx 1.17.4                                   
|_http-server-header: nginx/1.17.4                 
|_http-title: Site doesn't have a title (text/html).                 
3306/tcp open  mysql            MySQL (unauthorized)
8081/tcp open  blackice-icecap?                                              
| fingerprint-strings:                                               
|   FourOhFourRequest:                            
|     HTTP/1.1 200 OK                                                     
|     Content-Type: text/plain                                            
|     Date: Thu, 04 Mar 2021 16:38:15 GMT
|     Connection: close                               
|     Hello World                               
|   GetRequest:                      
|     HTTP/1.1 200 OK                
|     Content-Type: text/plain                                            
|     Date: Thu, 04 Mar 2021 16:38:14 GMT                                 
|     Connection: close              
|     Hello World                    
|   HTTPOptions:                     
|     HTTP/1.1 200 OK                
|     Content-Type: text/plain                                            
|     Date: Thu, 04 Mar 2021 16:38:25 GMT                                 
|     Connection: close              
|_    Hello World        
```

## PORT 80 (HTTP)
<img src="https://imgur.com/aNXvip6.png"/>

Clicking on `Test` or `Softwaer Issue Tracker` would be leading us  to `http://spectra.htb` so let's add this to `/etc/hosts`

<img src="https://imgur.com/P0KY28k.png"/>

<img src="https://imgur.com/dLk6e3I.png"/>

<img src="https://imgur.com/FVrnLZC.png"/>

<img src="https://imgur.com/BTpBDp7.png"/>

<img src="https://imgur.com/FRtmiix.png"/>

Going to `wp-config.php.save` we can find credentials to the database 

<img src="https://imgur.com/VSRhiu9.png"/>

But when connecting to them it just doesn't allow

<img src="https://imgur.com/wjfH4dZ.png"/>

### Wpscan

So we can't connect to mysql so we have a wordpress site let's run `wpscan` on it 

<img src="https://imgur.com/GomMYG0.png"/>

<img src="https://imgur.com/cAzWQxm.png"/>

So we have a wordpress user `administrator`

<img src="https://imgur.com/f4JfP4q.png"/>

Using the password `devteam01` we logged in with `administrator`

<img src="https://imgur.com/faWVNps.png"/>

We can edit the `404.php` template in the active theme

<img src="https://imgur.com/h2DIC5A.png"/>

<img src="https://imgur.com/06A0v9C.png"/>

Using a metasploit payload

<img src="https://imgur.com/CvLoXLI.png"/>

<img src="https://imgur.com/bbYRLsM.png"/>

Add ssh public key in `/home/nginx/.ssh/authorized_keys`

<img src="https://imgur.com/Bp2ZWS3.png"/>

<img src="https://imgur.com/h0utHDJ.png"/>

Going in `/opt` directory

<img src="https://imgur.com/aAXcFE8.png"/>

<img src="https://imgur.com/5tDMR1I.png"/>

We find a `passwd` file

<img src="https://imgur.com/djoWHPT.png"/>

ssh as `katie`

<img src="https://imgur.com/j8iUIUL.png"/>

On doing `sudo -l` we'll see what we can run as root

<img src="https://imgur.com/tULPcp6.png"/>

And we can run `initctl` which is used for running services, these services are stored in `/etc/init`

We can see the services we can edit 

<img src="https://imgur.com/OiPGXTo.png"/>

<img src="https://imgur.com/Ckviuh7.png"/>

Here this service is running a nodejs file which is `nodetest.js`

<img src="https://imgur.com/h2RowUK.png"/>

This is what we see when we visit port 8081 on the web browser we can edit this file by a node js reverse shell

<img src="https://imgur.com/U6XnnAj.png"/>

After editing set a netcat listener

<img src="https://imgur.com/xTP232M.png"/>
