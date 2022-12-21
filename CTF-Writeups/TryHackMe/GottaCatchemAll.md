# TryHackMe-Gotta Catch'Em All!

>Abdullah Rizwan | 08:54 PM , 24 October 2020

## NMAP

```
nmap -sC -sV 10.10.122.194                                                                              
Starting Nmap 7.80 ( https://nmap.org ) at 2020-10-24 20:55 PKT                                                                                     
Nmap scan report for 10.10.122.194                                        
Host is up (0.27s latency).                                               
Not shown: 998 closed ports                                               
PORT   STATE SERVICE VERSION                                              
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)                                                                   
| ssh-hostkey:                       
|   2048 58:14:75:69:1e:a9:59:5f:b2:3a:69:1c:6c:78:5c:27 (RSA)                                                                                      
|   256 23:f5:fb:e7:57:c2:a5:3e:c2:26:29:0e:74:db:37:c2 (ECDSA)                                                                                     
|_  256 f1:9b:b5:8a:b9:29:aa:b6:aa:a2:52:4a:6e:65:95:c5 (ED25519)                                                                                   
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))                                                                                                 
|_http-server-header: Apache/2.4.18 (Ubuntu)                              
|_http-title: Can You Find Them All?                                      
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel                                                                                             

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                                                      
Nmap done: 1 IP address (1 host up) scanned in 33.19 seconds   

```
## Gobuster

```
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.122.194
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/10/24 21:13:03 Starting gobuster
===============================================================
/.htaccess (Status: 403)
/.hta (Status: 403)
/.htpasswd (Status: 403)
/index.html (Status: 200)
/server-status (Status: 403)
===============================================================
2020/10/24 21:14:36 Finished
===============================================================

```
Running the gobuster , didn't find any directory 

## PORT 80

Coming on to the web page we see a default apache server running 

<img src="https://imgur.com/R9Ef1LC.png"/>

Going through the source of the web page we will find something interesting


<img src="https://imgur.com/BmV9tVZ.png"/>

<img src="https://imgur.com/yJJa6Cv.png"/>

`<pokemon>:<hack_the_pokemon>` looks like username and password for ssh since port 22 is open.

## PORT 22

```
root@kali:~/TryHackMe/Easy/GottaCatchemAll# ssh pokemon@10.10.122.194
pokemon@10.10.122.194's password: 
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.15.0-112-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

84 packages can be updated.
0 updates are security updates.


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

pokemon@root:~$ 

```
And we got in but we this user is not in `sudoers` so it cannot run commands as root or doesn't have permissions to run privleged commands

```

pokemon@root:~$ whoami
pokemon
pokemon@root:~$ sudo -l
[sudo] password for pokemon: 
Sorry, try again.
[sudo] password for pokemon: 
sudo: 1 incorrect password attempt
pokemon@root:~$ sudo -l
[sudo] password for pokemon: 
Sorry, user pokemon may not run sudo on root.
pokemon@root:~$ 

```
We can find `roots-pokemon.txt` but cannot read it as only the user `ash` and `root ` are owners of it.

<img src="https://imgur.com/YWg2htw.png"/>

Going to `pokemon`'s directory we can see there is `P0kEmOn.zip` 

<img src="https://imgur.com/nhjLvu1.png"/>

### Grass-Type Pokemon 
```
pokemon@root:~/Desktop$ unzip P0kEmOn.zip 
Archive:  P0kEmOn.zip
   creating: P0kEmOn/
  inflating: P0kEmOn/grass-type.txt  
pokemon@root:~/Desktop$ ls -la
total 16
drwxr-xr-x  3 pokemon pokemon 4096 Oct 24 12:52 .
drwxr-xr-x 19 pokemon pokemon 4096 Oct 24 11:54 ..
drwxrwxr-x  2 pokemon pokemon 4096 Jun 22 22:37 P0kEmOn
-rw-rw-r--  1 pokemon pokemon  383 Jun 22 22:40 P0kEmOn.zip
pokemon@root:~/Desktop$ 

```
On decompressing it you will get a folder, read the file `grass-type.txt` and find this hex encoded text

```
50 6f 4b 65 4d 6f 4e 7b 42 75 6c 62 61 73 61 75 72 7d

```
On decoding it you will get the flag : `PoKeMoN{Bulbasaur}`





### Find 

By running the find command to look for all .txt files we can find 3 files that we need 
```
pokemon@root:/$ find / -type f -name "*.txt" 2>/dev/null                                                                                            
/var/cache/dictionaries-common/ispell-dicts-list.txt                                                                                                
/var/lib/nssdb/pkcs11.txt                                                                                                                           
/var/www/html/water-type.txt                                                                                                                        
/etc/X11/rgb.txt                                                                                                                                    
/etc/why_am_i_here?/fire-type.txt                                                                                                                   
/etc/brltty/Input/bd/all.txt                                                                                                                        
/etc/brltty/Input/vs/all.txt                                                                                                                        
/etc/brltty/Input/eu/all.txt                                                                                                                        
/etc/brltty/Input/tt/all.txt                                                                                                                        
/etc/brltty/Input/lb/all.txt                                                                                                                        
/etc/brltty/Input/vr/all.txt                                                                                                                        
/etc/brltty/Input/tn/all.txt                                                                                                                        
/etc/brltty/Input/mb/all.txt                                                                                                                        
/etc/brltty/Input/mn/all.txt                                                                                                                        
/etc/brltty/Input/vd/all.txt                                                                                                                        
/etc/brltty/Input/bl/18.txt                                                                                                                         
/etc/brltty/Input/bl/40_m20_m40.txt                                                                                                                 
/etc/brltty/Input/ba/all.txt                                                                                                                        
/etc/brltty/Input/ec/spanish.txt                                                                                                                    
/etc/brltty/Input/ec/all.txt           
.....

```
```
/var/www/html/water-type.txt
/etc/why_am_i_here?/fire-type.txt 
/home/roots-pokemon.txt
```
But we already found `roots-pokemon.txt` we just don't have permissions to view it


### Water-Type Pokemon
```
pokemon@root:/$ cat /var/www/html/water-type.txt
Ecgudfxq_EcGmP{Ecgudfxq}
```
This gives us a rot13(shift cipher) encoded text , by changing the key of rot13 we can get the flag


<img src="https://imgur.com/Ms1lu4Z.png"/>

flag `Squirtle_SqUaD{Squirtle}`


### Fire-Type Pokemon

```
pokemon@root:/$ cat /etc/why_am_i_here?/fire-type.txt 
UDBrM20wbntDaGFybWFuZGVyfQ==

```

By looking at two equal signs(=) we can say that this is a base64 encoded text on decoding it

flag `P0k3m0n{Charmander}`


### Root's Favorite Pokemon

Now only thing which is left is to root the box and read that `/home/roots-pokemon.txt`

I found another interesting thing in `~/Vidoes`

```
pokemon@root:~$ cd Videos/
pokemon@root:~/Videos$ ls -la
total 12
drwxr-xr-x  3 pokemon pokemon 4096 Jun 22 23:10 .
drwxr-xr-x 19 pokemon pokemon 4096 Oct 24 11:54 ..
drwxrwxr-x  3 pokemon pokemon 4096 Jun 22 23:10 Gotta
pokemon@root:~/Videos$ cd Gotta/
pokemon@root:~/Videos/Gotta$ ls
Catch
pokemon@root:~/Videos/Gotta$ cd Catch/
pokemon@root:~/Videos/Gotta/Catch$ ls
Them
pokemon@root:~/Videos/Gotta/Catch$ cd Them/
pokemon@root:~/Videos/Gotta/Catch/Them$ ls
ALL!
pokemon@root:~/Videos/Gotta/Catch/Them$ cd ALL\!/
pokemon@root:~/Videos/Gotta/Catch/Them/ALL!$ ls
Could_this_be_what_Im_looking_for?.cplusplus
pokemon@root:~/Videos/Gotta/Catch/Them/ALL!$ 

```
Now on reading that c++ source code

```
int main() {
        std::cout << "ash : pikapika"
        return 0;

```
This will give us password for user `ash`



<img src="https://imgur.com/JJpAryg.png"/>

Now we can bascially run everything

```
ash@root:/home$ sudo bash
root@root:/home# 
```
