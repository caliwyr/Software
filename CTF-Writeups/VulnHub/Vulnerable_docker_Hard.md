# Vulnhub- Vulnerable Docker (Hard)

## NMAP

```
nmap -p- -sC -sV 192.168.1.7

Starting Nmap 7.80 ( https://nmap.org ) at 2021-03-25 22:24 PKT
Nmap scan report for 192.168.1.7
Host is up (0.00013s latency).
Not shown: 65533 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 6.6p1 Ubuntu 2ubuntu1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 45:13:08:81:70:6d:46:c3:50:ed:3c:ab:ae:d6:e1:85 (DSA)
|   2048 4c:e7:2b:01:52:16:1d:5c:6b:09:9d:3d:4b:bb:79:90 (RSA)
|   256 cc:2f:62:71:4c:ea:6c:a6:d8:a7:4f:eb:82:2a:22:ba (ECDSA)
|_  256 73:bf:b4:d6:ad:51:e3:99:26:29:b7:42:e3:ff:c3:81 (ED25519)
8000/tcp open  http    Apache httpd 2.4.10 ((Debian))
|_http-generator: WordPress 4.8.15
|_http-open-proxy: Proxy might be redirecting requests
| http-robots.txt: 1 disallowed entry 
|_/wp-admin/
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: NotSoEasy Docker &#8211; Just another WordPress site
|_http-trane-info: Problem with XML parsing of /evox/about
MAC Address: 08:00:27:D7:94:9E (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.88 seconds

```

## PORT 8000 (HTTP)

<img src="https://imgur.com/4wuEUWv.png"/>

We can see this is a wordpress site so let's run `wpscan` on the site

<img src="https://imgur.com/J7HGIje.png"/>

<img src="https://imgur.com/wgiI1TN.png"/>

wpscan found a user name `bob` we can now try brute forcing the password

<img src="https://imgur.com/6djRxkI.png"/>

<img src="https://imgur.com/ymuYTKf.png"/>

Login with the credentials found

<img src="https://imgur.com/r5W1jKg.png"/>

<img src="https://imgur.com/v5UQ9qk.png"/>

Now we can either manually upload a php reverse shell or use metasploit exploit

<img src="https://imgur.com/KANQ5mo.png"/>

<img src="https://imgur.com/vjKDJDX.png"/>

<img src="https://imgur.com/ULFPXUl.png"/>

We didn't get a proper meterpreter shell because of web shell exploit we used so we need to generate linux payload , upload and execute on the target machine

<img src="https://imgur.com/halR2va.png"/>

Open another meterpreter window and configure the listener

<img src="https://imgur.com/O6FP7U4.png"/>

<img src="https://imgur.com/TAN9ndn.png"/>

<img src="https://imgur.com/RhAdX4C.png"/>

Now commands can be run properly

<img src="https://imgur.com/zZgC9v9.png"/>

Use metasploit's `autoroute` to do pivoting

<img src="https://imgur.com/cBNY93g.png"/>

Now we need to find what's running on docker conatiner so we can use metasploit's `auxiliary/scanner/portscan/tcp` module

<img src="https://imgur.com/bXNkEyQ.png"/>

In order to access the ports we found we need to use proxychains for that we run `socks` module on metasploit and use proxyfroxy to configure proxy for browser

<img src="https://imgur.com/wabq5Aw.png"/>

Verify that the port is added in the `/etc/porxychains.conf`

<img src="https://imgur.com/3yNH0lR.png"/>

<img src="https://imgur.com/t5gRjvR.png"/>

<img src="https://imgur.com/SGVeRwL.png"/>

We can find `docker.sock` on the container which means we can create another container having host machien file system mounted on it 

<img src="https://imgur.com/ahgLzTq.png"/>

<img src="https://imgur.com/pjyVzWJ.png"/>

But to upload a static binary on that container there is no utility to download a file but we do have  internet avaiable on the machine so we can download `docker` as well but before that I downloaded `python3` on the container so I could get a stabilized shell

Run `apt update` and then `apt install python3`

<img src="https://imgur.com/uuv22cO.png"/>

<img src="https://imgur.com/xE8MdHu.png"/>
 

Download static binary and transfer it to target machine

<img src="https://imgur.com/6SsmjVZ.png"/>

<img src="https://imgur.com/DDRcq2R.png"/>

<img src="https://imgur.com/wdfi1Xo.png"/>

Since we have `docker.sock` on our container we can list the imgaes being used 

`./docker -H unix:///var/run/docker.sock images`

<img src="https://imgur.com/NrKk09C.png"/>

Now to mount the host file system on the container

`./docker -H unix:///var/run/docker.sock run -it -v /:/host/ wordpress chroot /host`

<img src="https://imgur.com/4UYMBI9.png"/>

Add your generated ssh public key in `authorized_keys` and then ssh on the box as root

<img src="https://imgur.com/ZxDwQzY.png"/>

<img src="https://imgur.com/xvu5SyQ.png"/>