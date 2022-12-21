# Vulnhub-ICMP

## Netdiscover

Running `netdiscover` to find IP for the target machine

<img src="https://imgur.com/EZfLijE.png"/>

## Rustscan

```
 rustscan -a 192.168.1.9 -- -A -sC -sV 
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
🌍HACK THE PLANET🌍

[~] The config file is expected to be at "/root/.rustscan.toml"
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
Open 192.168.1.9:22
Open 192.168.1.9:80
            
PORT   STATE SERVICE REASON         VERSION                                                                                                         
22/tcp open  ssh     syn-ack ttl 64 OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey:                                                            
|   2048 de:b5:23:89:bb:9f:d4:1a:b5:04:53:d0:b7:5c:b0:3f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3bVoBm6Jd8SD9AJ0qjLyo0oU4cgQthlFxui+n/qXM6NYRxBcWn0gva/MDLyW1neLva6hhuKFR/6GE6PtQ1Gge9SKOzmQPGXi2RBUQaVINZu
Ydb6Q0QR0BT3ppGMMsw8bNxluttaYIzbeK5tR4zCG8xPGss6LvLbtjfcjugxKWRF58hstDIHwtPhzYX3gnH17yN5w6NuSlpPwaCTbcFZNAqqAhoKSBBIUcZTYC5mdcp+EOR6ao3LCsk98bOxNSKz
3RdfmN3ch1Z6NaEbR/A9DIEoeC5e+e1GG6zGoDoSET1QstiMAahrs2yIhfHVxQUhlS9upju8OrRB0yCWvE2IG3
|   256 16:09:14:ea:b9:fa:17:e9:45:39:5e:3b:b4:fd:11:0a (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJPWpmfjbTeUtsjjJTkCPHFjiq+48Q/3ZYU+H0Kc/K6S785qBs1oRncFAGFV9A0xYtaUnmnohu
0OHP7sRJVoUR8=                                                            
|   256 9f:66:5e:71:b9:12:5d:ed:70:5a:4f:5a:8d:0d:65:d5 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJElctLWgcGu5SJqqW0MvhE4rBIGL0YLBZYt4sg+esy/
80/tcp open  http    syn-ack ttl 64 Apache httpd 2.4.38 ((Debian))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.38 (Debian)
| http-title:             Monitorr            | Monitorr        
|_Requested resource was http://192.168.1.9/mon/
MAC Address: 08:00:27:11:3E:2B (Oracle VirtualBox virtual NIC)


```

## PORT 80 (HTTP)

<img src="https://imgur.com/1L2YU1d.png"/>

At the bottom we can see the version of `Monitor` which is front end to display status of any web applicaiton.

<img src="https://imgur.com/KfbuHz1.png"/>

<img src="https://imgur.com/i2hyI93.png"/>

We can see that path where it uploads our reverse shell

<img src="https://imgur.com/JV7wrFq.png"/>

Run the exploit 

<img src="https://imgur.com/rZ8nl1T.png"/>

And setup a netcat listner also to visit where the reverse shell is uploaded

<img src="https://imgur.com/XnNvTUw.png"/>

We can see a note 

<img src="https://imgur.com/wNTbCCC.png"/>

<img src="https://imgur.com/G57JRPc.png"/>

Now running `sudo -l` we can see that we can `hping3` but with --icmp

<img src="https://imgur.com/1AjAh8B.png"/>

So run hping3 with icmp on localhost and send `id_rsa` and receive on localhost 

https://www.commandlinefu.com/commands/view/12851/sending-a-file-over-icmp-with-hping

<img src="https://imgur.com/VZNf2U1.png"/>

<img src="https://imgur.com/ETczaJc.png"/>
