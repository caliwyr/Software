# Vulnhub-Alfa

## Rustscan

```
PORT      STATE SERVICE     REASON         VERSION                      
21/tcp    open  ftp         syn-ack ttl 64 vsftpd 3.0.3                  
| ftp-anon: Anonymous FTP login allowed (FTP code 230)              
|_drwxr-xr-x    2 0        0            4096 Dec 17 12:02 thomas               
| ftp-syst:    
|   STAT:                            
| FTP server status:                 
|      Connected to ::ffff:192.168.1.8                                    
|      Logged in as ftp              
|      TYPE: ASCII                   
|      No session bandwidth limit                                         
|      Session timeout in seconds is 300                                  
|      Control connection is plain text                                   
|      Data connections will be plain text                                
|      At session startup, client count was 1                             
|      vsFTPd 3.0.3 - secure, fast, stable                                
|_End of status                      
80/tcp    open  http        syn-ack ttl 64 Apache httpd 2.4.38 ((Debian))
| http-methods:                      
|_  Supported Methods: POST OPTIONS HEAD GET                              
|_http-server-header: Apache/2.4.38 (Debian)                              
|_http-title: Alfa IT Solutions                                           
139/tcp   open  netbios-ssn syn-ack ttl 64 Samba smbd 3.X - 4.X (workgroup: WORKGROUP)                                                              
445/tcp   open  netbios-ssn syn-ack ttl 64 Samba smbd 4.9.5-Debian (workgroup: WORKGROUP)                                                           
65111/tcp open  ssh         syn-ack ttl 64 OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)                                                           
| ssh-hostkey:                       
|   2048 ad:3e:8d:45:48:b1:63:88:63:47:64:e5:62:28:6d:02 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC2/gN4xwraW4+k393E8l0qsfBzclz6JW+SZG4rtYaonpi1RNGoTWSOgfEUm74RQocMqqklmzlqYVpr1jWu7+hqKZyQvhS3Z02/bbl2aPLsk$
|   2048 ad:3e:8d:45:48:b1:63:88:63:47:64:e5:62:28:6d:02 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC2/gN4xwraW4+k393E8l0qsfBzclz6JW+SZG4rtYaonpi1RNGoTWSOgfEUm74RQocMqqklmzlqYVpr1jWu7+hqKZyQvhS3Z02/bbl2aPLskz
xJSHNQwX6C5gbA1m4ilgWr7beOvLr0ZsS1FwsM7F3UghKpgjWcXhK+PGYi9kh79q3HO0KZlhv46fpiPLxVOi7g4jA/TB7RZFEyWUgH0oUFqC6h9TGitOuH9mm1cVFbSFve/Xv+R3Fg1/nOsXtMp/
dbk3/qRBLnAZuMie4Lfi6Ri/ogb16NfQBowSv65zq3V312ctWdtp9ACrqNdHukHavW09qanQ6j+MAYFqI/gVx/
|   256 1d:b3:0c:ca:5f:22:a4:17:d6:61:b5:f7:2c:50:e9:4c (ECDSA)   
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJWoOk2y6Gj22LwB1cphvfRxANuV99NkaatiHlQ3qoGomRhyzNzK2AWLBrHasjWbJKDxci+7JE
dP99XCBYZzKHQ=                       
|   256 42:15:88:48:17:42:69:9b:b6:e1:4e:3e:81:0b:68:0c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICRMwXyo2xpfoG0gAJKYSDnTdwp8RRZMVHrQS2wNB5T1    

```


## PORT 21 (FTP)
Since anonymous login is enabled we can what's on ftp.

<img src="https://imgur.com/mQ8Q5dv.png"/>

We only find `milo.png`

<img src="https://imgur.com/94MQ19W.png"/>


## PORT 80 (HTTP)

<img src="https://imgur.com/KRjDxDb.png"/>

Visit `robots.txt` we see some entries but there is only `images` directory on web server.

<img src="https://imgur.com/puYfAbt.png"/>

<img src="https://imgur.com/WRsz435.png"/>

Scrolling down a bit we can see  something written in `Brainfuck` 

<img src="https://imgur.com/Yrn5KP5.png"/>

<img src="https://imgur.com/Zs6umn0.png"/>

<img src="https://imgur.com/ezzB1xQ.png"/>

Now here we can see a conversation between `Thomas` and Alfa IT support where the user thomas is requesting for password reset and he tells that his current password is petname and 3 digit numbers so we brute force his password

<img src="https://imgur.com/AmgeyFv.png"/>

Now that the wordlist has been generated we can brute force against the user `thomas`

<img src="https://imgur.com/N9QuAXh.png"/>

And we found the password

<img src="https://imgur.com/H1z9bwI.png"/>

<img src="https://imgur.com/reHJLN0.png"/>

We can see `.remote_secret` which might be a password for vnc , we can verify to see if vnc is running or not which is usually on port 5900 or 5901

<img src="https://imgur.com/FN5mpen.png"/>

Now since vnc client is not installed on target machine we can do port forwarding for vnc port using ssh

<img src="https://imgur.com/ZNxTKmV.png"/>

Now that port is open on our local machine

<img src="https://imgur.com/Jwzo5nH.png"/>

Simply connect to that port using `remote_secret`

<img src="https://imgur.com/xhuYtUJ.png"/>

<img src="https://imgur.com/iA2onWQ.png"/>
