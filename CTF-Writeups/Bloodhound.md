# Domain Enumeration - Bloodhound

Bloodhound is useful for gathering AD entities , relationships , it uses graph theory for providing the capability of mapping shortest path for interesting thing , it can find interesting things like `Domain Admins` , it has built-in queries.

https://github.com/BloodHoundAD/BloodHound

## Sharphound

https://github.com/BloodHoundAD/BloodHound/blob/master/Collectors/SharpHound.ps1

### Generate archive 

```
Invoke-BloodHound -CollectionMethod All
```

### Avoiding detection form Advanced Threat Analytics (ATA)
```
Invoke-BloodHound -CollectionMethod All -ExcludeDC
```

