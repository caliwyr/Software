# TryHackMe-Lockdown

## NMAP

```bash

22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:                                                            
|   2048 27:1d:c5:8a:0b:bc:02:c0:f0:f1:f5:5a:d1:ff:a4:63 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDA1Xdw3dCrCjetmQieza7pYcBp1ceBvVB6g1A/OU+bqoRSEfnKTHP0k5P2U1BbeciJTqflslP3IHh+py4jkWTkzbU80Mxokn2Kr5Qa5GKgrm
e4Q6GfQsQeeFpbLlIHs+eEBnCLY/J03iddkt6eukd3VwZuRXHnEHl7G6Y1f0IEEzProg15iAtUTbS8OwPx+ZwdvXfJTWujUS+OzLLjQw5wPewCEK+TJHVM02H+5sO+dYBMC9rgiEnPe5ayP+nupA
XMNYB9/p/gO3nj5h33SokY3RkXMFsijUJpoBnsDHNgo2Q41j9AB4txabzUQVFql30WO8l8azO4y/fWYYtU8YCn
|   256 ce:f7:60:29:52:4f:65:b1:20:02:0a:2d:07:40:fd:bf (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBGjTYytQsU83icaN6V9H1Kotl0nKVpR35o6PtyrWy9WjljhWaNr3cnGDUnd7RSIUOiZco3UL5+
YC31sBdVy6b6o=                                                            
|   256 a5:b5:5a:40:13:b0:0f:b6:5a:5f:21:60:71:6f:45:2e (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOHVz0M8zYIXcw2caiAlNCr01ycEatz/QPx1PpgMZqZN
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

## PORT 80  (HTTP)

When we visit to the web server it's going to redirect us to a domain name  `contacttracer.thm/` so let's add this to `/etc/hosts` file

<img src="https://i.imgur.com/JyStBig.png"/>

After adding the domain name in the file , we can see a login portal

<img src="https://i.imgur.com/U8Y7Fl5.png"/>

<img src="https://i.imgur.com/diXZ0fe.png"/>

<img src="https://i.imgur.com/BjeVplg.png"/>

Let's try some default credentials for admin, I tired `admin:admin` , `admin:password` , `admin:admin123` but they didn't worked so I ran `gobuster` to fuzz for files and directories

<img src="https://i.imgur.com/oSbuOho.png"/>

So most of the directories were forbidden , so on the admin panel I tried a simple sqli to login `admin' or 1=1 -- ` and I got access

<img src="https://i.imgur.com/dFyHdeU.png"/>

<img src="https://i.imgur.com/0kXXn4H.png"/>

## Foothold 

To get a shell there are two ways , on going to settings we can change the login page's image to a php rev shell file

<img src="https://i.imgur.com/vBp2sHB.png"/>

<img src="https://i.imgur.com/0EbXtJh.png"/>

Another way ,we can also dump the database on login page that way we can find the name of whatever file we upload but I didn't dump the whole database becuase it was time-based sqli so it was taking some time so I stopped doing this

<img src="https://i.imgur.com/Oy55Nq5.png"/>

Anyway contining with stabilizing the shell

<img src="https://i.imgur.com/On17g0f.png"/>

Let's do some basic enumeration , first I checked `sudo -l`

<img src="https://i.imgur.com/4gckTh6.png"/>

We don't have a password so let's move on , next I checked crontabs but those were empty as well

<img src="https://i.imgur.com/ywz1l3R.png"/>

Checked if there are any SUID's we can abuse but there weren't any

<img src="https://i.imgur.com/yi5WJ8l.png"/>

<img src="https://i.imgur.com/2N3AK0L.png"/>

## Privilege Escalation (Cyrus)

We can see there are two users `cyrus` and `maxine` also if we remeber we saw `config.php` from gobuster's result so let's visit that file also this what the uploaded files look like

<img src="https://i.imgur.com/VRRWK53.png"/>

On reading config.php file we'll get a username and password

<img src="https://i.imgur.com/AehelDq.png"/>

I tried cracking this hash but was not successful , I read `DBConnection.php` file and found some creds 

<img src="https://i.imgur.com/1AlcTkU.png"/>

<img src="https://i.imgur.com/aqLAPZr.png"/>

But there wasn't anything in the database that was interesting to us but this `admin` hash , on cracking it we get the password `sweetpandemonium`

<img src="https://i.imgur.com/vnlcpCP.png"/>

<img src="https://i.imgur.com/GWF9hEN.png"/>

<img src="https://i.imgur.com/GXFzUpf.png"/>

## Privilege Escalation (root)

On running `sudo -l` , this user can run a script as a root user

<img src="https://i.imgur.com/4T6pfAE.png"/>

```bash
#!/bin/bash
read -p "Enter path: " TARGET                                                                                                                       
                                                                          
if [[ -e "$TARGET" && -r "$TARGET" ]]                                     
  then                                                                                                                                              
    /usr/bin/clamscan "$TARGET" --copy=/home/cyrus/quarantine                                                                                       
    /bin/chown -R cyrus:cyrus /home/cyrus/quarantine                      
  else                                                                                                                                              
    echo "Invalid or inaccessible path."                                  
fi  
```

This is the bash script , it's going to read the file name and it's going to check in the if condition with `-e` that if that file exists and with `-r` if that files is readable then it's going to run `clamscan` which is an AV tool , if there's a virus found it's going to copy that file to `/home/cyrus/quarantine` so let's run this tool with the provided sample in cyrus's home directory

<img src="https://i.imgur.com/NARWga4.png"/>

So it copied that file in that `quarantine` directory

<img src="https://i.imgur.com/EBlVAvi.png"/>

I looked up on clamscan's documentation and it seems that we can write our own rules (YARA rules) to identifiy which file maybe contain a virus

https://docs.clamav.net/manual/Signatures/YaraRules.html

We need to find where `clamscan` loads the rules from ,so I used `find` command to search for `clam*` and found the directory where it had rule to flag a file it has a virus or not

<img src="https://i.imgur.com/Z3931nX.png"/>

<img src="https://i.imgur.com/qjE1qAN.png"/>

<img src="https://i.imgur.com/tZkLfJ8.png"/>

This is the rule file 

<img src="https://i.imgur.com/NeaaYG3.png"/>

But it's more of a signature based rule file `hdb` , we can't do that as we are not able to `root.txt` flag so we won't be able to do this instead we can write a yara rule for `/etc/shadow` file , as we can flag that file as malicious by creating rule which would look for `root` string and if that exists it's going to flag that file has a virus and will copy that file to quaranitne folder

```bash
rule root
{
        strings:
                $string = "root"


        condition:
                $string
}
```

This is a simple YARA rule which holds the string value "root" in `string` variable and in condition section it's going to check for the `string` variable that if it's found in any of the file when it's passed to `clamscan` it's going to flag it as a malicious file

<img src="https://i.imgur.com/WcAZE7D.png"/>

<img src="https://i.imgur.com/oxkbnlF.png"/>

<img src="https://i.imgur.com/YyK0E0c.png"/>

In the shadow file we don't see any root hash but we do have hashes for the two users

<img src="https://i.imgur.com/6JhTgej.png"/>

We already have passsword for cyrus , so let's crack the hash for `maxine` user

<img src="https://i.imgur.com/fwEo6QW.png"/>

<img src="https://i.imgur.com/qYlBo0W.png"/>

<img src="https://i.imgur.com/fZs9jq0.png"/>


## References

- https://docs.clamav.net/manual/Signatures/YaraRules.html
- https://blog.nviso.eu/2017/02/14/hunting-with-yara-rules-and-clamav/


```
dev_oretnom : 5da283a2d990e8d8512cf967df5bc0d0
cts         : YOUMKtIXoRjFgMqDJ3WR799tvq2UdNWE
			  sweetpandemonium	

```