# Vulnhub- DC2
Before starting the scan it was told to add a domain name into `/etc/hosts` file

<img src="https://imgur.com/mnRlgX4.png"/>

<img src="https://imgur.com/Q2L8IQf.png"/>


## Rustscan
```bash


rustscan -a 192.168.1.6 -- -A -sC -sV
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.                  
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |           
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |                  
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'                                                                                            
The Modern Day Port Scanner.                                              
________________________________________
: https://discord.gg/GFrQsGy           :                       
: https://github.com/RustScan/RustScan :
 --------------------------------------

Open 192.168.1.6:80
Open 192.168.1.6:7744



PORT     STATE SERVICE REASON         VERSION

80/tcp   open  http    syn-ack ttl 64 Apache httpd 2.4.10 ((Debian))      
| http-methods:        
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.10 (Debian)                         
|_http-title: Did not follow redirect to http://dc-2/                        
|_https-redirect: ERROR: Script execution failed (use -d to debug)
7744/tcp open  ssh     syn-ack ttl 64 OpenSSH 6.7p1 Debian 5+deb8u7 (protocol 2.0)
| ssh-hostkey:   
|   1024 52:51:7b:6e:70:a4:33:7a:d2:4b:e1:0b:5a:0f:9e:d7 (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBAMT3xv0ReIK733JHqB5o5t1Knur7MHfTeYoqdn2fxpfdk79iDYAD46e/C1hLs6R0CH1fSWfpJ0x45g77ZaEn/nOaR2UXiod20R6kyrAPyL4UELizECoJ9M
dHSULedr0+4QcXhtUZ+4b76umJhENpOhH+vZjrjMI5uZo+EMjlylxFAAAAFQDzg8StOWpV7J5ZjSfIdcddFgqB/QAAAIA84WMMKmOEkvzgQZLuW5lTTecIrk+UXJyWVZSZFxvFbnt5mUvEzPBMqP
ZIo1h1dkzpEp1Xpk9Vb16LMrQcS6LgH8yhlo5402lUCfP6onxVNvGvP5uhLoQVjzPd65ZKJ7J1VSoz9xOmPkWr2HFuCf6XOBXy8WCxqZxWYTYERTuexgAAAIAI8DjfDmIjv0jUBAPZu0crpPoxvK
4ZvdEy6UbfjK+pZYzkd6qnVLdWrvP9evbWaA5VoDZjWp1301VjX8Y1pqHFVaRUu3OBY7DgidJXA3zLd1BSdPzYfRJSZ1/xN75Yo13wW6XIEsy1kvUNOwA0Nm6zmcQ+SN/aBITwGOIBGrp06w==
|   2048 59:11:d8:af:38:51:8f:41:a7:44:b3:28:03:80:99:42 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDC92AIbO8wDuOXLMCrnJkTKDLxXzpwFY0EI4urz6cZpmOjGOZYbWz6Ele1sM3WXEWmOWkszLrMbVEFmuYan545oIHnylYX6ZY+eMPjJBRH/V
DukRsNtAA8VRsvIkfCtcG5J9zAQTQDYYprEJljKPYavf4bIW3NZb0v57O01tGylLh23ZSfGpTmQXx+GsWet9vnbCr1+bzf/QeZ7PNK9BeBsLJsvWgLQmuaTdBYeW1b415xOaszWrutHQoaBdud/S
PX1Uvy2PNFUfKIPjdbmAdRxTAvRHHaMTRdrvEhdJWz3wmefXr9e3S3YEu05USTqhMwi6OBxeqkjc+6mdR/PYR9
|   256 df:18:1d:74:26:ce:c1:4f:6f:2f:c1:26:54:31:51:91 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBE329BkKjKxz7Y23cZSshQ76Ge3DFsJsTO89pgaInzX6w5G3h6hU3xDVMD8G8BsW3V0CwXWt1f
TnT3bUc+JhdcE=
|   256 d9:38:5f:99:7c:0d:64:7e:1d:46:f6:e9:7c:c6:37:17 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGyWHwWC3fLufEnM1R2zsvjMZ1TovPCp3mky/2s+wXTH
MAC Address: 08:00:27:90:02:65 (Oracle VirtualBox virtual NIC)

```

## PORT 80 (HTTP)

We see a wordpress site , so to enumerate wordperss there is a tool called `wpscan` which makes your life easier

<img src="https://imgur.com/0sFy6iq.png"/>

We see a flag  which hints about making a wordlist with `cewl`

<img src="https://imgur.com/jRBlCtr.png"/>

<img src="https://imgur.com/owY4o5d.png"/>

We found three users using wpscan

<img src="https://imgur.com/qwQR9vO.png"/>

So let's generate a wordlist using `cewl`

<img src="https://imgur.com/jpePUHv.png"/>

Running wpscan again to brute force the three users's password

<img src="https://imgur.com/2aZ39ap.png"/>

And we get two users

<img src="https://imgur.com/JfZU6cl.png"/>

Logged in as jerry and we see second flag page

<img src="https://imgur.com/3uvZiyz.png"/>

<img src="https://imgur.com/GxBMkMP.png"/>

But there wasn't anything I could on wordpress as jerry had only the editor role also `tom` was a regular user on the site but SSH was open on port 7744 maybe we can try credentials there

Tried for jerry but failed

<img src="https://imgur.com/DUdlyPt.png"/>

But tom's credentials worked !

<img src="https://imgur.com/OOhcjqZ.png"/>

<img src="https://imgur.com/5ayttOL.png"/>

Commands were not being run , so I checked the PATH variable

<img src="https://imgur.com/yl7dmGV.png"/>

Doing `ls -la`

<img src="https://imgur.com/PvvI2lr.png"/>

Doing less on `flag3.txt`

<img src="https://imgur.com/MrvfVTb.png"/>

So we cannot run commands like `cd,cat,su,/bin/bash` as we are in a restricted shell, A restricted shell is a shell that block/restricts some of the commands like cd,ls,echo etc or"block" the environment variables like SHELL,PATH,USER.

<img src="https://imgur.com/x1g6CQ0.png"/>

I tried using python,python3,vi,less,awk,find to escape restricted shell but wasn't able to

The binaries we can only run are

<img src="https://imgur.com/ueBfD7G.png"/>

So to escape the restricted shell I tried everything but there was one trick which I haven't tried and that was to open `vi` then,

: set shell =/bin/sh
: shell

<img src="https://imgur.com/VStpbON.png"/>

<img src="https://imgur.com/lviaZcN.png"/>

Still we are in a restricted shell

<img src="https://imgur.com/mbD7a6x.png"/>

<img src="https://imgur.com/qowBSTB.png"/>

<img src="https://imgur.com/IHNNBCq.png"/>

We can switch to jerry by using the password we found from cewl wordlist

<img src="https://imgur.com/EEbqKAO.png"/>

And jerry can run git as root

<img src="https://imgur.com/A73dTDk.png"/>

So on visting GTFOBINS

<img src="https://imgur.com/PyXoHt1.png"/>

<img src="https://imgur.com/ipiIs6s.png"/>

<img src="https://imgur.com/Z6OuVUX.png"/>
