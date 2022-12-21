# Domain Enumeration - Trusts

In AD , trust is a relationship b/w domains or forest that allows user of one domain or forest to access resources in other domain or forest, trust can be automatic (parent-child).
TDOs (Trusted Domain Objects) represent the trust relationship in a domain

## One way trust 
It's an undirectional trust in which users in trusted domain can access resources in trusting domain (resource) but cannot be done in reverse

## Two way trust (bi directional)
Users of both domains can access resources in the other domain

## Trust Transitivity 
Trust can be extended to establish trust relationships with othe domains 

### Transitive
All default intra-forest trust relationships (tree-root, parent-child) between domains within a same forest are transitive two-way trust

### Non-transitive
Cannot be extended to other domains in forest , can be two-way or one-way, this is the default trust (called external trust) between two domains in different forest do not have a trust realtionship.

## Domain Trusts

### Default/Automatic Trusts

- Parent-child trust , it's created automatically b/w new domain and domain that preceeds it in the namespace hierarrchy , whenever a new domain is added in a tree , for example `dollarcorp.moenycorp.local` is a child of `moneycorp.local`, trust will always be bi-directional
- Tree-root trust , it's created automatically whenever a new domain tree is added to a forest root , this trust is bi-directional as well

### Shortcut Trusts
Used to reduce access time in complex trust scenarios , can be one way or two way transitive

### External Trust
External trust b/w two domains in different forests when forests do not have a trust relationship , can be one way or two way

# Domain Trust mapping 

## Powerview commands

### Get list of all domain trusts for current domain

```
Get-NetDomainTrust
Get-NetDomainTrust -Domain domain_name
```

## AD Module

### Get list of all domain trusts for current domain

```
Get-ADTrust
Get-ADTrust- Identity domain_name
```

# Forest Mapping 
## Power View

### Get details about current forest 

```
Get-NetForest
Get-NetForest -Forest name
```

### Get all domains in current forest

```
Get-NetForestDomain
Get-NetForestDomain -Forest name
```

### Get all global catalogs for current forest
```
Get-NetForestCatalog
Get-NetForestCatalog -Forest name 
```
### Map trusts of a forest
```
Get-NetForestTrust
Get-NetForestTrust -Forest name 
```

## AD Module

###  Get details about current forest 
```
Get-ADForest
Get-ADForest -Identity name
```

### Get all domains in current forest
```
(Get-ADForest).Domain
```

### Get all global catalogs for current forest
```
Get-ADForest | select -ExpandPropery GlobalCatalogs
```
### Map trusts of a forest
```
Get-ADTrust -Filter 'msDS0TrustForestTrustInfo -ne "$null$"'
```
