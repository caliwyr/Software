# VulnHub-Stapler

This a beginner level linux box which was on TJnull's OSCP prep list. This box has many rabbit holes in it also I faced some issues running wpscan because this box is very old and has an older version of wordpress so you may need some patience in doing this box so let's just dig in.

## Netdiscover

<img src="https://imgur.com/xEjyduh.png"/>

## NMAP

```
Nmap scan report for 192.168.1.8
Host is up (0.00044s latency).
Not shown: 992 filtered ports
PORT     STATE  SERVICE     VERSION
20/tcp   closed ftp-data
21/tcp   open   ftp         vsftpd 2.0.8 or later
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: PASV failed: 550 Permission denied.
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 192.168.1.6
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open   ssh         OpenSSH 7.2p2 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 81:21:ce:a1:1a:05:b1:69:4f:4d:ed:80:28:e8:99:05 (RSA)
|   256 5b:a5:bb:67:91:1a:51:c2:d3:21:da:c0:ca:f0:db:9e (ECDSA)
|_  256 6d:01:b7:73:ac:b0:93:6f:fa:b9:89:e6:ae:3c:ab:d3 (ED25519)
53/tcp   open   domain      dnsmasq 2.75
| dns-nsid: 
|_  bind.version: dnsmasq-2.75
80/tcp   open   http        PHP cli server 5.5 or later
|_http-title: 404 Not Found
139/tcp  open   netbios-ssn Samba smbd 4.3.9-Ubuntu (workgroup: WORKGROUP)
666/tcp  open   doom?
| fingerprint-strings: 
|   NULL: 
|     message2.jpgUT 
|     QWux
|     "DL[E
|     #;3[
|     \xf6
|     u([r
|     qYQq
|     Y_?n2
|     3&M~{
|     9-a)T
|     L}AJ
|_    .npy.9
3306/tcp open   mysql       MySQL 5.7.12-0ubuntu1
| mysql-info: 
|   Protocol: 10
|   Version: 5.7.12-0ubuntu1
|   Thread ID: 9
|   Capabilities flags: 63487
|   Some Capabilities: Speaks41ProtocolOld, Support41Auth, IgnoreSpaceBeforeParenthesis, SupportsTransactions, LongColumnFlag, SupportsLoadDataLocal, IgnoreSigpipes, InteractiveClient, FoundRows, LongPassword, Speaks41ProtocolNew, ODBCClient, DontAllowDatabaseTableColumn, SupportsCompression, ConnectWithDatabase, SupportsMultipleResults, SupportsMultipleStatments, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: }\x13V\x10\x06	*<,`\x0D\x0C\x0E88 ]7JV
|_  Auth Plugin Name: mysql_native_password
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port666-TCP:V=7.80%I=7%D=12/25%Time=5FE52027%P=x86_64-pc-linux-gnu%r(NU
SF:LL,2D58,"PK\x03\x04\x14\0\x02\0\x08\0d\x80\xc3Hp\xdf\x15\x81\xaa,\0\0\x
SF:152\0\0\x0c\0\x1c\0message2\.jpgUT\t\0\x03\+\x9cQWJ\x9cQWux\x0b\0\x01\x
SF:04\xf5\x01\0\0\x04\x14\0\0\0\xadz\x0bT\x13\xe7\xbe\xefP\x94\x88\x88A@\x
SF:a2\x20\x19\xabUT\xc4T\x11\xa9\x102>\x8a\xd4RDK\x15\x85Jj\xa9\"DL\[E\xa2
SF:\x0c\x19\x140<\xc4\xb4\xb5\xca\xaen\x89\x8a\x8aV\x11\x91W\xc5H\x20\x0f\
SF:xb2\xf7\xb6\x88\n\x82@%\x99d\xb7\xc8#;3\[\r_\xcddr\x87\xbd\xcf9\xf7\xae
SF:u\xeeY\xeb\xdc\xb3oX\xacY\xf92\xf3e\xfe\xdf\xff\xff\xff=2\x9f\xf3\x99\x
SF:d3\x08y}\xb8a\xe3\x06\xc8\xc5\x05\x82>`\xfe\x20\xa7\x05:\xb4y\xaf\xf8\x
SF:a0\xf8\xc0\^\xf1\x97sC\x97\xbd\x0b\xbd\xb7nc\xdc\xa4I\xd0\xc4\+j\xce\[\
SF:x87\xa0\xe5\x1b\xf7\xcc=,\xce\x9a\xbb\xeb\xeb\xdds\xbf\xde\xbd\xeb\x8b\
SF:xf4\xfdis\x0f\xeeM\?\xb0\xf4\x1f\xa3\xcceY\xfb\xbe\x98\x9b\xb6\xfb\xe0\
SF:xdc\]sS\xc5bQ\xfa\xee\xb7\xe7\xbc\x05AoA\x93\xfe9\xd3\x82\x7f\xcc\xe4\x
SF:d5\x1dx\xa2O\x0e\xdd\x994\x9c\xe7\xfe\x871\xb0N\xea\x1c\x80\xd63w\xf1\x
SF:af\xbd&&q\xf9\x97'i\x85fL\x81\xe2\\\xf6\xb9\xba\xcc\x80\xde\x9a\xe1\xe2
SF::\xc3\xc5\xa9\x85`\x08r\x99\xfc\xcf\x13\xa0\x7f{\xb9\xbc\xe5:i\xb2\x1bk
SF:\x8a\xfbT\x0f\xe6\x84\x06/\xe8-\x17W\xd7\xb7&\xb9N\x9e<\xb1\\\.\xb9\xcc
SF:\xe7\xd0\xa4\x19\x93\xbd\xdf\^\xbe\xd6\xcdg\xcb\.\xd6\xbc\xaf\|W\x1c\xf
SF:d\xf6\xe2\x94\xf9\xebj\xdbf~\xfc\x98x'\xf4\xf3\xaf\x8f\xb9O\xf5\xe3\xcc
SF:\x9a\xed\xbf`a\xd0\xa2\xc5KV\x86\xad\n\x7fou\xc4\xfa\xf7\xa37\xc4\|\xb0
SF:\xf1\xc3\x84O\xb6nK\xdc\xbe#\)\xf5\x8b\xdd{\xd2\xf6\xa6g\x1c8\x98u\(\[r
SF:\xf8H~A\xe1qYQq\xc9w\xa7\xbe\?}\xa6\xfc\x0f\?\x9c\xbdTy\xf9\xca\xd5\xaa
SF:k\xd7\x7f\xbcSW\xdf\xd0\xd8\xf4\xd3\xddf\xb5F\xabk\xd7\xff\xe9\xcf\x7fy
SF:\xd2\xd5\xfd\xb4\xa7\xf7Y_\?n2\xff\xf5\xd7\xdf\x86\^\x0c\x8f\x90\x7f\x7
SF:f\xf9\xea\xb5m\x1c\xfc\xfef\"\.\x17\xc8\xf5\?B\xff\xbf\xc6\xc5,\x82\xcb
SF:\[\x93&\xb9NbM\xc4\xe5\xf2V\xf6\xc4\t3&M~{\xb9\x9b\xf7\xda-\xac\]_\xf9\
SF:xcc\[qt\x8a\xef\xbao/\xd6\xb6\xb9\xcf\x0f\xfd\x98\x98\xf9\xf9\xd7\x8f\x
SF:a7\xfa\xbd\xb3\x12_@N\x84\xf6\x8f\xc8\xfe{\x81\x1d\xfb\x1fE\xf6\x1f\x81
SF:\xfd\xef\xb8\xfa\xa1i\xae\.L\xf2\\g@\x08D\xbb\xbfp\xb5\xd4\xf4Ym\x0bI\x
SF:96\x1e\xcb\x879-a\)T\x02\xc8\$\x14k\x08\xae\xfcZ\x90\xe6E\xcb<C\xcap\x8
SF:f\xd0\x8f\x9fu\x01\x8dvT\xf0'\x9b\xe4ST%\x9f5\x95\xab\rSWb\xecN\xfb&\xf
SF:4\xed\xe3v\x13O\xb73A#\xf0,\xd5\xc2\^\xe8\xfc\xc0\xa7\xaf\xab4\xcfC\xcd
SF:\x88\x8e}\xac\x15\xf6~\xc4R\x8e`wT\x96\xa8KT\x1cam\xdb\x99f\xfb\n\xbc\x
SF:bcL}AJ\xe5H\x912\x88\(O\0k\xc9\xa9\x1a\x93\xb8\x84\x8fdN\xbf\x17\xf5\xf
SF:0\.npy\.9\x04\xcf\x14\x1d\x89Rr9\xe4\xd2\xae\x91#\xfbOg\xed\xf6\x15\x04
SF:\xf6~\xf1\]V\xdcBGu\xeb\xaa=\x8e\xef\xa4HU\x1e\x8f\x9f\x9bI\xf4\xb6GTQ\
SF:xf3\xe9\xe5\x8e\x0b\x14L\xb2\xda\x92\x12\xf3\x95\xa2\x1c\xb3\x13\*P\x11
SF:\?\xfb\xf3\xda\xcaDfv\x89`\xa9\xe4k\xc4S\x0e\xd6P0");
MAC Address: 08:00:27:E1:68:35 (Oracle VirtualBox virtual NIC)
Service Info: Host: RED; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 4h59m57s, deviation: 0s, median: 4h59m57s
|_nbstat: NetBIOS name: RED, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.9-Ubuntu)
|   Computer name: red
|   NetBIOS computer name: RED\x00
|   Domain name: \x00
|   FQDN: red
|_  System time: 2020-12-25T04:11:44+00:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-12-25T04:11:45
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 46.74 seconds
```
```
nmap --script dns-nsid 192.168.1.8                                             
Starting Nmap 7.80 ( https://nmap.org ) at 2020-12-25 04:41 PKT
Nmap scan report for 192.168.1.8
Host is up (0.0010s latency).
Not shown: 992 filtered ports
PORT     STATE  SERVICE
20/tcp   closed ftp-data
21/tcp   open   ftp
22/tcp   open   ssh
53/tcp   open   domain
| dns-nsid: 
|_  bind.version: dnsmasq-2.75
80/tcp   open   http
139/tcp  open   netbios-ssn
666/tcp  open   doom
3306/tcp open   mysql
MAC Address: 08:00:27:E1:68:35 (Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 14.48 seconds

```


## FTP (PORT 21)

<img src="https://imgur.com/BV1Y1AU.png"/>

The banner gives us a name "harry" so it can be a username

<img src="https://imgur.com/UCShAQ3.png"/>

```
Elly, make sure you update the payload information. Leave it in your FTP account once your are done, John.
```

Again this note has some usernames

## SMB (PORT 139)

To enumarate smb we run `enum4linux` . I am using an updated version of it which is called enum4linux-ng.

<img src="https://imgur.com/Vy71cfA.png"/>

<img src="https://imgur.com/Vy71cfA.png"/>

Here it did found some user names


### Hydra

Now using hydra we will try to crack the credentials for ftp by using the same wordlist of user we found for passwords and users

<img src="https://imgur.com/vyNYlrc.png"/>

Again if we use this wordlist for ssh we will get the same result and will be able to login into the box

<img src="https://imgur.com/7sE8lwr.png"/>


<img src="https://imgur.com/QrwM5RB.png"/>

On running ss -tupln to see which ports are open on the box we see port `12380`

Also there are some directories on webserver

<img src="https://imgur.com/4xlTbKB.png"/>

But going on to port 80 we don't find any directories and ruuning gobuster is useless because it doesn't show anything interesting

## PORT 80

<img src="https://imgur.com/Oa5VivL.png"/>

<img src="https://imgur.com/d2ULBmN.png"/>

## PORT 12380

<img src="https://imgur.com/ybnycg8.png"/>

Running nikto on this port it returned as that these directories do exists the ones we found in `/var/www/https`

<img src="https://imgur.com/ftrTgiq.png"/>

<img src="https://imgur.com/YsE7WS1.png"/>

## Wpscan

On running `wpscan` along with port 12380 on directory `blogblog` which is a wordpress site it gave me erros

<img src="https://imgur.com/VI9pcc7.png"/>

So added a parameter `--disable-tls-checks` and it worked fine

<img src="https://imgur.com/Sw8C8LR.png"/>

<img src="https://imgur.com/YwDbJVA.png"/>

Now we know the registered users on wordpress , let's enumerate more to get plugins 

<img src="https://imgur.com/IgdmMJl.png"/>

<img src="https://imgur.com/7ALUtkZ.png"/>

It didn't returned me any plugins so now add a paramter `--plugins-detection aggressive` there are only three modes for detecting plugins passive,mixed and agressive 

<img src="https://imgur.com/qmXBpl1.png"/>

<img src="https://imgur.com/PgDPxzF.png"/>

<img src="https://imgur.com/kfjMT0Q.png"/>

Using this technique I was able to identify 4 plugins

```
two-factor
shortcode-ui
akismet
advanced-video-embed-embed-videos-or-playlists
```

Searching for an exploit for one these plugins I found something on exploit-db 

<img src="https://imgur.com/5bIC8uJ.png"/>

<img src="https://imgur.com/t7NCM5M.png"/>

So here only LFI can be useful.

<img src="https://imgur.com/VW3kRij.png"/>

Edit the exploit by putting the proper url where `blogblog` is 

<img src="https://imgur.com/xdEHmSr.png"/>

And it will throw this error

<img src="https://imgur.com/jKPN1fG.png"/>

To resolve this import ssl and a line `ssl._create_default_https_context = ssl._create_unverified_context`

<img src="https://imgur.com/Gv28vRN.png"/>

On running this exploit it will create a jpeg file with random string

<img src="https://imgur.com/h95s0Ss.png"/>

When we'll download this it will be php script in which the contents of `wp-config.php` are stored but we don't need to do this as we have our foothold on to the box and we can just search for that file

<img src="https://imgur.com/javj7NZ.png"/>

<img src="https://imgur.com/7IwSAro.png"/>

And we will find the credentials for mysql database since port 3306 is running we can connect to it

<img src="https://imgur.com/KnkGHHR.png"/>

<img src="https://imgur.com/Vg2iPsD.png"/>

<img src="https://imgur.com/qK9XQIy.png"/>

<img src="https://imgur.com/kaGpxTd.png"/>

We get a bunch of usernames and passwords but we need to crack these hashes so lets store them in a file and to crack them I will be using johntheripper but you can do it with hashcat for that you need to specify with what kind of hash are we dealing with so I went up to hashcat examples and found this is a wordpress MD5 hash

<img src="https://imgur.com/EdqNJ1V.png"/>

<img src="https://imgur.com/WQ9wRjR.png"/>

On cracking those hashes

```
john:$P$B7889EMq/erHIuZapMB8GEizebcIy9. 	:incorrect
elly:$P$BlumbJRRBit7y50Y17.UPJ/xEgv4my0 	:ylee
peter:$P$BTzoYuAFiBA5ixX2njL0XcLzu67sGD0 	:washere
barry:$P$BIp1ND3G70AnRAkRY41vpVypsTfZhk0 	:passphrase
heather:$P$Bwd0VpK8hX4aN.rZ14WDdhEIGeJgf10  :football
garry:$P$BzjfKAHd6N4cHKiugLX.4aLes8PxnZ1 	:monkey
harry:$P$BqV.SQ6OtKhVV7k7h1wqESkMh41buR0 	:cookie
scott:$P$BFmSPiDX1fChKRsytp1yp8Jo7RdHeI1 	:coolgirl
kathy:$P$BZlxAMnC6ON.PYaurLGrhfBi6TjtcA0 	:thumb
tim:$P$BXDR7dLIJczwfuExJdpQqRsNf.9ueN0 		:damachine
zoe:$P$B.gMMKRP11QOdT5m1s9mstAUEDjagu1 		:0520
dave:$P$Bl7/V9Lqvu37jJT.6t4KWmY.v907Hy.		: -
simon:$P$BLxdiNNRP008kOQ.jE44CjSK/7tEcz0 	: -
abby:$P$ByZg5mTBpKiLZ5KxhhRe/uqR.48ofs. 	: -
vicki:$P$B85lqQ1Wwl2SqcPOuKDvxaSwodTY131 	: -
pam:$P$BuLagypsIJdEuzMkf20XyS5bRm00dQ0 		: -
```

<img src="https://imgur.com/XLnbkqe.png"/>

<img src="https://imgur.com/lJNV13K.png"/>

On logging in with username `john` we can see that we are administrator. Now we cannot upload a php file directly but we can upload it through a plugin upload

<img src="https://imgur.com/tvt0EJ7.png"/>

<img src="https://imgur.com/A2RBaXR.png"/>

<img src="https://imgur.com/TS7lfzb.png"/>

But we are in the same situation and this was again a rabbit hold that we got into so only thing now we can do is look for general information about the linux os
<img src="https://imgur.com/tkRLApC.png"/>

So, the os is ubuntu 16.04 and kernel version is 4.4.0-21 

<img src="https://imgur.com/O2HFAwr.png"/>

But by the result `i686 i686 i686` it says that it is 32 bit architecture.

<img src="https://imgur.com/rBe0CnJ.png"/>

So this may be the exploit that will work

On reading the text file that is found with searchsploit it would tell to go to site where zip file is uploaded for the exploit.

<img src="https://imgur.com/nXUtiL1.png"/>

And according to the read we have to run `compile.sh` and `doubleput`.

<img src="https://imgur.com/o3JitMv.png"/>

Transfer exploit.tar to the target box and extract .tar

<img src="https://imgur.com/yEnp5QS.png"/>

Now compile the doubleput.c and ran compile.sh and doubleput 

<img src="https://imgur.com/kai9kC8.png"/>