# TryHackMe-Empline

## NMAP

```bash

22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:                                                            
|   2048 c0:d5:41:ee:a4:d0:83:0c:97:0d:75:cc:7b:10:7f:76 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDR9CEnxhm89ZCC+SGhOpO28srSTnL5lQtnqd4NaT7hTT6N1NrRZQ5DoB6cBI+YlaqYe3I4Ud3y7RF3ESms8L21hbpQus2UYxbWOl+/s3muDp
Zww1nvI5k9oJguQaLG1EroU8tee7yhPID0+285jbk5AZY72pc7NLOMLvFDijArOhj9kIcsPLVTaxzQ6Di+xwXYdiKO0F3Y7GgMMSszIeigvZEDhNnNW0Z1puMYbtTgmvJH6LpzMSEC+32iNRGlvb
jebE9Ehh+tGiOuHKXT1uexrt7gbkjp3lJteV5034a7G1t/Vi3JJoj9tMV/CrvgeDDncbT5NNaSA6/ynLLENqSP
|   256 83:82:f9:69:19:7d:0d:5c:53:65:d5:54:f6:45:db:74 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFhf+BTt0YGudpgOROEuqs4YuIhT1ve23uvZkHhN9lYSpK9WcHI2K5IXIi+XgPeSk/VIQLsRUA
0kOqbsuoxN+u0=
|   256 4f:91:3e:8b:69:69:09:70:0e:82:26:28:5c:84:71:c9 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDkr5yXgnawt7un+3Tf0TJ+sZTrbVIY0TDbitiu2eHpf
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: HEAD GET POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Empline
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
3306/tcp open  mysql   syn-ack ttl 63 MySQL 5.5.5-10.1.48-MariaDB-0ubuntu0.18.04.1
| mysql-info:                                                             
|   Protocol: 10
|   Version: 5.5.5-10.1.48-MariaDB-0ubuntu0.18.04.1
|   Thread ID: 85
|   Capabilities flags: 63487
|   Some Capabilities: ConnectWithDatabase, IgnoreSpaceBeforeParenthesis, IgnoreSigpipes, Speaks41ProtocolNew, SupportsTransactions, ODBCClient, Spe
aks41ProtocolOld, Support41Auth, FoundRows, DontAllowDatabaseTableColumn, LongColumnFlag, LongPassword, SupportsLoadDataLocal, InteractiveClient, Su
pportsCompression, SupportsAuthPlugins, SupportsMultipleResults, SupportsMultipleStatments
|   Status: Autocommit
|   Salt: 3[Qe)7{&IzMS7Y9RnVB*
|_  Auth Plugin Name: mysql_native_password
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

## PORT 80 (HTTP)

<img src="https://i.imgur.com/7fC63nN.png"/>

On the web server we can see a page which looks like a static html template , so running `gobuster` on the site for fuzzing for files 

<img src="https://i.imgur.com/RsSywMx.png"/>

But this didn't find much files , but looking at the source code we found a subdomain

<img src="https://i.imgur.com/vMukBnN.png"/>

So let's add this to `/etc/hosts`  file

<img src="https://i.imgur.com/HmPdYNZ.png"/>

This brings us to a page where it says `opencats`

<img src="https://i.imgur.com/5luHh4C.png"/>

We can search for exploits available if any 

<img src="https://i.imgur.com/dyK2dWj.png"/>

And we found a XXE exploit which would allows us to perform Local File Inclusion (LFI), for the exploit to work we need to install `python-docx` and then we can run the exploit to see if we can read `passwd` file

<img src="https://i.imgur.com/pjCz6qz.png"/>

Trying to fuzz for files on subdomain 

<img src="https://i.imgur.com/kMKIkTi.png"/>

I didn't find any php files so adding them with `-x` I found `config.php`

<img src="https://i.imgur.com/kPduMiN.png"/>

<img src="https://i.imgur.com/UmC9D1n.png"/>

We can now use the same exploit by supplying config.php file to read

<img src="https://i.imgur.com/R1wlvQ5.png"/>

<img src="https://i.imgur.com/wedDDOL.png"/>

After connecting to database since the port was open we can get user creds

<img src="https://i.imgur.com/VYKlR7u.png"/>


<img src="https://i.imgur.com/N5WOpU9.png"/>

Putting those hashes on `crackstation` we can get george's password

<img src="https://i.imgur.com/SyoncBp.png"/>

<img src="https://i.imgur.com/NlfXTE1.png"/>

## Privilege Escalation

We can check for `sudo -l` and see if we have permissions to run anything as root

<img src="https://i.imgur.com/Szw6BCm.png"/>

Next we can check for `crontabs` if there's a script running in a background

<img src="https://i.imgur.com/3r2ZM8p.png"/>

We see nothing in corontabs as well , we can look for SUID binaries 

<img src="https://i.imgur.com/xfjNZxY.png"/>

No interesting SUID's here that we can utilize , so next thing to check is for linux capabilites and what capabilites in linux are that things that the root user can do his permissions are broken down into some permissions like changing setting suid or changing ownership of folders

<img src="https://i.imgur.com/cLEi54p.png"/>

Here we can see `ruby` has those capabilities set and can change ownernship of the directories with `chown`

<img src="https://i.imgur.com/vSaLaBX.png"/>

Following the documentation of ruby we can look for changing ownership of files/folders

<img src="https://i.imgur.com/l5Crc9g.png"/>

<img src="https://i.imgur.com/7GScsbJ.png"/>

And we see that root's directory is now owned by `george` , we can add ssh public key in `authorized_keys` file and see if we can get ssh session as root user but it won't work because in `sshd_config` file it's configuired to not allow root to login through ssh

<img src="https://i.imgur.com/0WpFYW3.png"/>

Now there are so many ways here we can change ownership of `/etc/` and either allow root to login through ssh (but that would require ssh to restart), add a new root user entry in `/etc/shadow` or edit `sudoers` file

<img src="https://i.imgur.com/PSzW7sD.png"/>

<img src="https://i.imgur.com/G6EQ9iC.png"/>

We need to now revert the file permissions as it needs to be owned by root user

<img src="https://i.imgur.com/6UShuhg.png"/>

<img src="https://i.imgur.com/iKym4jb.png"/>


## References

- https://book.hacktricks.xyz/linux-unix/privilege-escalation/linux-capabilities
- https://ruby-doc.org/stdlib-2.4.1/libdoc/fileutils/rdoc/FileUtils.html#method-c-chown_R