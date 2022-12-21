# TryHackMe-Ninja Skills

>Abdullah Rizwan | 05:36 PM

First of all copied all the files mentioned into `/tmp` folder by finding them with

`find / -name "file_name" `


```
    8V2L  /etc/8V2L 
    bny0  can't find
    c4ZX  /mnt/c4ZX
    D8B3  /mnt/D8B3
    FHl1  /var/FHl1
    oiMO  /opt/oiMO
    PFbD  /opt/PFbD
    rmfX  /media/rmfX
    SRSq  /etc/ssh/SRSq
    uqyw  /var/log/uqyw
    v2Vb /home/v2Vb
    X1Uy /X1Uy
```


1. Which of the above files are owned by the best-group group(enter the answer separated by spaces in alphabetical order)

`find / -group best-group`

`v2Vb D8B3`

2. Which of these files contain an IP address?

`oiMO`

3. Which file has the SHA1 hash of 9d54da7584015647ba052173b84d45e8007eba94

When you have copied the files in one place you can run 

```
ls | xargs sha1sum
```
To check hash of files

`c4ZX`

4. Which file contains 230 lines?

I check every file's and so far they were `209` so only left was `bny0` so I submitted it

`bny0`

5. Which file's owner has an ID of 502?

```
find / -user newer-user -name "*" 2>/dev/null
```
`X1Uy`

6. Which file is executable by everyone?

```
ls -la
```
`8V2L`



