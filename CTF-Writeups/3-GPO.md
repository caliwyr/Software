# Domain Enumeration Group Policy Objects

## PowerView commands

### Get list of GPO in current domain 

```
Get-NetGPO
Get-NetGPO -ComputerName computername.domainname

```
### Get GPO(s) which use restricted groups or groups.xml for interesting users

```
Get-NetGPOGroup
```

### Get users which are in a local group of a machine using GPO 

```
Find-GPOComputerAdmin -Computername computername.domainname
```

### Get machines where the given user is member of a specific group 

```
Find-GPOLocation -Username username -Verbose
```

### Get OUs in a domain
```
Get-NetOU -FullData
```

### Get GPO applied on an OU . Read GPOname from gplink attribute

```
Get-NetGPO -GPOname "{guid_string}"
```

## Group Policy Module commands

### Get list of GPO in current domain 

```
Get-GPO -All

Get-GPResultantSetOfPolicy -ReportType Html -Path C:\Users\Administrator\report.html
```

### Get GPO applied on an OU . Read GPOname from gplink attribute
```
Get-GPO -Guid guid_string
```


## AD Module 

### Get OUs in a domain
```
Get-ADOrganizationalUnit -Filter * -Properties *
```

