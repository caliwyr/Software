# VulnHub-Fart Knocker

## NMAP

```
Nmap scan report for Huhuhhhhhuhuhhh (192.168.43.108)
Host is up (0.00012s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
MAC Address: 08:00:27:35:8B:64 (Oracle VirtualBox virtual NIC)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.30 seconds
```

## PORT 80

On visiting the web page we had link named `Wooah` on clicking it prompt as to save or open a pacp file which is a wireshark file for analyzing packets

<img src="https://i.ibb.co/5MdMhDp/wireshark-analyze.png"/>

From the packets we can see that an IP was trying to connect with a port sequence of `7000,8000,9000,800`. So this looks like a port knocking scenario where you have to connect to number of ports in a sequence which will unlock a port for you to connect which is used to hide a port from connecting.

## Port Knocking 

We can either use a for loop to conenct to certain port or we can use netcat to connect to these port sequence but a command `knock` can help us out in port knocking

<img src="https://i.ibb.co/jMxtVWR/port-knock.png"/>

Now we after port knocking run the nmap scan again immediately after running the knock command

<img src="https://i.ibb.co/HrNL75z/again-scan.png"/>

We can see that port 8888 is opened but in seconds it will be turned due to it's timeout configuration so run the knock command again and connect to this port using netcat or telnet

<img src="https://i.ibb.co/tcFBxtY/again-port-knock.png"/>

Visting the page we get

<img src="https://i.ibb.co/TrM44xt/burger-wordl.png"/>

<img src="https://i.ibb.co/bRK4Rvb/again-pcap.png"/>

We again get a prompt for opening or saving a pcap file let's do that an open it with wireshark

<img src="https://imgur.com/jYld7ct.png"/>

We can these packets here so follow the tcp stream of these packets

<img src="https://imgur.com/nmVLJLp.png"/>

On following it gives this message

```
eins drei drei sieben
```
Which on translating is in german which is translated to `1 3 3 7` which is the next sequence for port knock

<img src="https://imgur.com/RuxnE38.png"/>

On connecting with that port it gives us another page

<img src="https://imgur.com/Nz1bXJV.png"/>

<img src="https://imgur.com/WpkMqvB.png"/>

The heading gives us a hint `that base`

<img src="https://imgur.com/QhgjMM9.png"/>

Looks like another port which needs to be knocked

<img src="https://imgur.com/OceOfbd.png"/>

<img src="https://imgur.com/wyRWswt.png"/>

Connecting with any username will give you the ssh banner which has username and password

<img src="https://imgur.com/7Gx9epV.png"/>

But ssh was keep closing when we were loggin in with the correct creds but on giving the command /bin/bash I was able to get on the box

<img src="https://imgur.com/tIJlSOy.png"/>

I tried to stabilize the shell but bash not spawning in any way

<img src="https://imgur.com/r3QN2qe.png"/>

So ignoring to stabilize the shell let's enumerate the box using linpeas so I used `netcat` to transfer the file

<img src="https://imgur.com/uWuE8iv.png"/>

<img src="https://imgur.com/XoTtfjz.png"/>

Immediately it pointed that it is using an older version of linux kernel so we can look it up on exploit-db for any exploit available.

<img src="https://imgur.com/1gaGWBu.png"/>

This is the most common exploit of linux kernel which I have seen in alot of vulnerable machines

<img src="https://imgur.com/1rr7vgD.png"/>

Make sure to convert it into dos format because usually this is the error which occurs when running the binary , transfer the file to the machine , compile it then run it

<img src="https://imgur.com/32Wlfn4.png"/>

<img src="https://imgur.com/CwDDQNB.png"/>