# TryHackMe - Crack The Hashes

> Abdullah Rizwan | 10th September , 06 : 03 PM


## Cracking The Hashes

### Level 1

1 ) 48bb6e862e54f2a795ffc4e541caed4d

Hash = `md5`

```
easy
```

2) CBFDAC6008F9CAB4083784CBD1874F76618D2A97 


Hash =  `SHA-1`

```
password123
```

3) 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032

Hash = `SHA-512`

```
letmein
```
4) $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom

Hash = `bcrypt`

```
```


5) 279412f945939ba78ce0758d3fd83daa


Hash = `md4`

```
Eternity22
```

### Level 2

1) F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85

Hash = `SHA-256`

```
paule
```

2) 1DFECA0C002AE40B8619ECF94819CC1B


Hash = `NTLM`
```
n63umy8lkf4i

```

3) Hash: $6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.

Salt: aReallyHardSalt

Rounds: 5

Hash = `SHA-512`

```
hashcat -m 1800 hash /usr/share/wordlists/rockyou.txt -O
waka99

```

4) Hash: e5d8870e5bdd26602cab8dbe07a942c8669e56d6

   Salt: tryhackme



Hash = `SHA-1`


```
hashcat -m 110 hash /usr/share/wordlists/rockyou.txt -O

481616481616
```