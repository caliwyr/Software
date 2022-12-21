# Domain Enumeration - User Hunting

## Power View commands

### Find all machines on current domain where the current user has local admin access

```
Find-LocalAdminAccess -verbose
Invoke-CheckLocalAdminAccess
```

If `find-localadminaccess` is blocked because it sends `Get-NetComputer`  to DC , so we can try to use `Find-WMILocalAdminAccess.ps1`

Save the results of `Get-NetComputer` in a text file then run

```
. .\Find-WMILocalAdminAccess.ps1 -ComputerFile computer.txt -verbose
```

### Find local admins on all machines of the domain (needs administrator on non-dc machines )
```
Invoke-EnumerateLocalAdmin -Verbose
```

this function queries DC of current or provided domain for a list of compters (`Get-NetComputer`) and then use multi-threaded `Get-NetLocalGroup` on each machine.

### Find computers where a domain admin (or specified user/group) has sessions 
```
Invoke-UserHunter
Invoke-UserHunter -GroupName "RDPUsers"
```

this function queries DC of current or provided domain for members of the given group (Domain Admins bt default) using `Get-NetGroupMember` , gets a list of computers (`Get-NetComputer`) and list sessions and logged on users (`Get-NetSession/Get-NetLoggedon`)

### To confirm admin access 

```
Invoke-UserHunter -CheckAccess
```

### Find computers where a domain admin is logged in

```
Invoke-UserHunter -Stealth
```

This option queries DC of current or provided domain for members of given group (Domain Admins by default) using `Get-NetGroupMember` , gets a list_only of high traffic  servers (DC , file servers and Distributed  file servers ) for less traffic generation  and list sessions and logged on users (`Get-NetSession/Get-NetLoggedon`) from each machine