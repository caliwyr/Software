# Vulnhub - DC 5

## Rustscan

```bash
rustscan -a 192.168.1.5 -- -A -sC -sV

Open 192.168.1.5:80                                             
Open 192.168.1.5:111                                                      
Open 192.168.1.5:46209 

PORT      STATE SERVICE REASON         VERSION                   
80/tcp    open  http    syn-ack ttl 64 nginx 1.6.2
| http-methods:                                
|_  Supported Methods: GET HEAD POST                                    
|_http-server-header: nginx/1.6.2                                               
|_http-title: Welcome            
111/tcp   open  rpcbind syn-ack ttl 64 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          36602/tcp6  status
|   100024  1          46209/tcp   status
|   100024  1          49690/udp6  status
|_  100024  1          56402/udp   status
46209/tcp open  status  syn-ack ttl 64 1 (RPC #100024)
MAC Address: 08:00:27:01:36:B6 (Oracle VirtualBox virtual NIC)
```

## PORT 80 (HTTP)

<img src="https://imgur.com/1Lol2Ue.png"/>

Running gobuster on the website

<img src="https://imgur.com/f8tWzGC.png"/>

`footer.php` looked interesting

<img src="https://imgur.com/qXuOYx8.png"/>

After refreshing the page the copyright text changes

<img src="https://imgur.com/UxGRzXy.png"/>

But `thankyou.php` had footer.php so there the text was also changing on reload , which was a hint for the box to look for a page which reloads

<img src="https://imgur.com/ojmKKOG.png"/>

I went to `contact.php`

<img src="https://imgur.com/u25kfEd.png"/>

Filled the details and submitted them , it redirected me to thankyou.php with the url having our submitted details

<img src="https://imgur.com/Eh6sGLx.png"/>

But here this file doesn't suppose to having these paramters so let's fuzz for paramters

<img src="https://imgur.com/0BU4laq.png"/>

This showed a lot of parameters with the same result so let's filter it according to words

<img src="https://imgur.com/oHmUgsP.png"/>

And we got `file` as a parameter

<img src="https://imgur.com/pHXCfXz.png"/>

Since this is website is using nginx so we can read it's log file 

<img src="https://imgur.com/Rz78wvX.png"/>

We can poison the nginx log with a php command injection by adding the php payload by replacing the user agent

<img src="https://imgur.com/EJDLP6W.png"/>

But it didn't work

Added that php injection command in `file` parameter

<img src="https://imgur.com/IDcbXhy.png"/>

<img src="https://imgur.com/cRL5HmP.png"/>

It was being url encoded

<img src="https://imgur.com/8zsFtON.png"/>

<img src="https://i.imgur.com/jbndY07.png"/>

Now it seems to work

<img src="https://imgur.com/TTrJop1.png"/>

Finding SUID's , I found `screen-4.5.0`

<img src="https://i.imgur.com/aE2Ypw4.png"/>

There's an exploit for it on exploit-db

<img src="https://imgur.com/o6du48d.png"/>

Transfer the exploit on target machine

<img src="https://imgur.com/TnzyPfV.png"/>

But we'll get this error when compiling it 

<img src="https://imgur.com/5l4rFft.png"/>

So it seems we need to manually create and compile files

<img src="https://i.imgur.com/vaVBvCU.png"/>

<img src="https://imgur.com/nOMzcAO.png"/>
 
<img src="https://imgur.com/yzsYGbR.png"/> 

Before you compile you will be seeing this error

`gcc: error trying to exec 'cc1': execvp: No such file or directory`

So to resolve this export gcc's path in PATH variable

`export PATH=/usr/bin:$PATH`

And then run these commands 

1. gcc -fPIC -shared -ldl -o /tmp/libhax.so /tmp/libhax.c
2. gcc -o /tmp/rootshell /tmp/rootshell.c 

Finally run this command

<img src="https://imgur.com/4LDYh6q.png"/>

You'll see `rootshell` binary gets owned by `root`

<img src="https://i.imgur.com/qj5Csk8.png"/>

Now just run that binary and you will get root on the machine

<img src="https://imgur.com/ZZwLmh0.png"/>

<img src="https://imgur.com/kvXOzjI.png"/>


## Things Learned from this machine

1. If a page has get paramters make sure to fuzz for them 
2. If you find a LFI on a page try to read logs (apache2 or nginx) and poison the logs by adding php get parameter
3. Look for SUID binaries
4. Before using the exploit ,see what's it doing