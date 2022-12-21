# Domain Enumeration finding file servers and shares on hosts

## PowerView commands

### Find shares on hosts in current domain

```
Invoke-ShareFinder -verbose
```

### Find sensitive files on computers in the domain 

```
Invoke-FileFinder -Verbose
```

### Get all fileservers of the domain
```
Get-NetFileServer
```

