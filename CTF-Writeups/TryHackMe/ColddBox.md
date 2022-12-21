# TryHackMe-ColddBox

## Rustscan

<img src="https://imgur.com/VW0IztZ.png"/>

<img src="https://imgur.com/Yn5ZiC8.png"/>


Open 10.10.218.218:80                                                             
Open 10.10.218.218:4512 

## PORT 80

<img src="https://imgur.com/vAiwYMa.png"/>

This looks like a wordpress site to ensure this let's visit `/wp-admin`

<img src="https://imgur.com/3PitIQV.png"/>

## Dirsearch

I started fuzzing for directories using dirsearch and expected to found wp-admin as it is a wordpress site

<img src="https://imgur.com/RzKcrg0.png"/>

<img src="https://imgur.com/8QbEzYa.png"/>

This gave us a valid username and we can verify it as wordpress allows us to know if the username is correct but the password is invalid

<img src="https://imgur.com/hNbxZX0.png"/>

We can bruteforce password for this user account.

## WPSCAN

For wordpress it is recommended to run wpscan to enumerate for user names ,plugins and themes installed also it looks for vulnerable plugins

<img src="https://imgur.com/4O6rJkA.png"/>

We found a few more users along with hugo so let's start the bruteforce attack through wpscan

<img src="https://imgur.com/0XPVlo5.png"/>

<img src="https://imgur.com/lcSQipa.png"/>

<img src="https://imgur.com/9iqHQDF.png"/>

We logged into the wordpress dashboard now goto `Appearance` -> `Editor` -> `Select 404 Template`-> `Paste php reverse shell` 

<img src="https://imgur.com/QDzdwA2.png"/>

<img src="https://imgur.com/oEzHJ5d.png"/>

Now we have to invoke the php reverse shell as setting up a netcat listener to do that we have added our malicious 404.php file now we need to navigate to where it is stored as we have edited theme twentyfiteen it is in `wp-content/themes/twentyfifteen/404.php`

<img src="https://imgur.com/Rd5CJtv.png"/>

But we need to escalate our privileges in order read `user.txt`	

<img src="https://imgur.com/uQffE6i.png"/>

<img src="https://imgur.com/kQEuDQW.png"/>

We see find as SUID so we abuse it to gain access to root

<img src="https://imgur.com/VVUh9o5.png"/>

We can see that our prompt as changed as a root user
