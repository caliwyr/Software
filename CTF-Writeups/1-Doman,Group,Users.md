# Domain Enumeration

`$ADClass=[System.DirectoryServices.ActiveDirectoy.Domain]`

`$ADClass::GetCurrentDomain()`
  
  We can use modules like `PowerView` or `ADModule`
  
  https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1
  
  https://github.com/samratashok/ADModule
  
  
 ## PowerView Commands

### Get current domain

`Get-NetDomain`

### Get Object of another domain

`Get-NetDomain -Domain <domainname>`

### Get Domain SID for current domain

`Get-DomainSID`

### Get Domain Controller for current domain
`Get-NetDomainController`

### Get Domain Controllers for another domain

`Get=NetDomainController -Domain <domain_name>`

### Get Domain Policy for current domain

```
 Get-DomainPolicy`
(Get-DomainPolicy)."system access"
(Get-DomainPolicy)."Kerberos Policy"
```

### Get Domain Policy for another domain

`(Get-DomainPolicy -domain <domainname>). "system access"`

 ### Get a list of users in the current domain
 
```
Get-NetUser
Get-NetUser -Username <user>
Get-NetUser | select cn
```

 ### Get list of all properites for users in current domain 
 
 ```
 Get-UserProperty
 Get-UserProperty -Properties pwdlastset
 Get-UserProperty -Properties logoncount (user is either not active or it's just a decoy user so we should avoid enumerating these users)
 ```
 
 ### Search for a particular string in  a user's attribute
 
 `Find-UserField -SearchField  Description -SearchTerm "built"`
 
 ### Get list of computers in current domain
 
```
 Get-NetComputer
 Get-NetComputer -OperatingSystem "*Server 2016"
 Get-NetComputer -Ping
 Get-NetComputer -FullData
```

### Get all groups in current domain

```
Get-NetGroup
Get-NetGroup -Domain <targetdomain>
Get-NetGroup -FullData

```

### Get all group containing the word "admin"
```
Get-NetGroup "admin"
Get-NetGroup "admin" -Domain <domainname>
```

### Get all members of Domain Admins group for current domain

```
Get-NetGroupMember -GroupName "Enterprise Admins"
Get-NetGroupMember -GroupName "Domain Admins" 
Get-NetGroupMember -GroupName "Administartors"
```

### Get all members of Domain Admins group for all domains
```
Get-NetGroupMember -GroupName "Administartors" -Recurse
```


### Get the group membership of a user

```
Get-NetGroup -Username "<username>"
```


 ## AD Module
 
 Use the psd1 file for AD module

### Get current domain

`Get-ADDomain`

### Get Object of another domain

`Get-ADDomain -Identity <domainname>`

### Get Domain SID for current domain

`(Get-ADDomain).DomainSID`

### Get Domain Controller for current domain
`Get-ADDomainController`

### Get Domain Controllers for another domain

`Get-ADDomainController -DomainName <domainname> -Discover`

### Get a list of users in the current domain
`Get-ADUser -Filter * -Properties *`
`Get-ADUser -Identity <user> -Properties *`

### Get list of all properties for users in the current domain
`Get-ADUser -Filter * -Properties * | select -First 1 | Get-Member -MemberType * Property | select Name`

`Get-ADUser -Filter * -Properties * | select name ,@(expression*`

 ### Search for a particular string in  a user's attribute
 
 `Get-ADUser-Filter 'Description' -like "*built"' -Properties Description | select name,Description`
 
  ### Get list of computers in current domain
 
 `Get-ADComputer -Filter * | select Name`
 
 `Get-ADComputer -Filter 'OperatingSystem -like "*Server 2016*"' -Properties OperatingSystem | select Name,OperatingSystem`

`Get-ADComputer -Filter * -Properties DNSHostName | %{Test - Connection -Count 1 -ComputerNmae $_ DNSHostName)`

 `Get-ADComputer -Filter * -Properties *`
 
 ### Get all groups in current domain 

```
Get-ADGroup -Filter * | select Name
Get-ADGroup -Filter * -Properties
```

### Get all groups containing word "admin" in group name 
```
Get-ADGroup -Filter 'Name -like "*admin" | select Name
```

### Get all members of Domain Admins group

```
Get-ADGroupMember - Identity "Domain Admins" -Recursive
```

### Get the group membership of a user

```
Get-ADPrincipalGroupMembership -Identity <username>
```