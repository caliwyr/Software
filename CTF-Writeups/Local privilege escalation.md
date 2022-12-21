# Privilege Escalation - Local

This is the technique that we should follow while looking to escalate our privileges in an AD environment 

```
Recon 
Domain Enum 
Local priv 
Admin Recon 
Lateral Movement (while being persistant) 
Domain 
Admin priv 
Cross Trust Attacks
```

We should hunt for local admin access on other machine , hunt for high privilege domain account like a domain administrator

Other than that we should look for 

- missing patches 
- automated deployment and  autologon passwords
- alwaysintallelevated (any user can run msi as system user)
- misconfigured services
- dll hijacking

Using the tools below we can quickly identify the above privilege escalation vectors

- https://github.com/PowerShellMafia/PowerSploit/blob/master/Privesc/PowerUp.ps1 `Invoke-AllChecks`
- https://github.com/AlessandroZ/BeRoot `.\beRoot.exe`
- https://github.com/enjoiz/Privesc/blob/master/privesc.ps1 `Invoke-PrivEsc`

## PowerUp

### Get services with unquoted path and a space in thier name
```
Get-ServiceUnquoted -Verbose
```

### Get services where current user can write to it's binary path or change arguments to the binary

```
Get-ModifiableServiceFile -Verbose
```

### Get services whose configuration urrent user can modify

```
Get-ModifiableService -Verbose
```