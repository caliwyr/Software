# Contemporaneous Open

This is a challenge where we need to manipulate TCP packets. When we connect to the server, we need to provide an IP to ther server, then it
can send the flag in a POST request form, it explicitly says that no SYN+ACK packets will be received to the server, so the 3-way handshake will
not be possible. But, is there another way to connect with the server using TCP ? The answer is yes! and the hint is in the challenge's name.
There is a alternative way to create a TCP connection called "TCP Simultaneous Open" (explanation [here](https://diameter-protocol.blogspot.com/2014/03/simultaneous-open-tcp-connections.html)) which consists in the two devices will
act as a server and client at the same time, and the connection is established when both responds to a special SYN packet.

So, in this challenge we need to create that kind connection first in order the server can be able to send us the flag.

I had in my pending projects, write a packet sniffer with Python, so I put my hands on this. This can be simply done with the Scapy framework
but, I prefer to do it using sockets, this way I can see and manipulate raw data.
![screenshot](https://github.com/stevenvegar/CTF-Tools/blob/main/NahamCon22/ContemporaneousOpen/ContemporaneousOpen.png)


## [frame_sniffer.py](https://github.com/stevenvegar/CTF-Tools/blob/main/NahamCon22/ContemporaneousOpen/frame_sniffer.py)
This script captures the ethernet frames, here we can grab the information from OSI-layer 2, which means, we can clasify frames depending on 
their [EtherType](https://en.wikipedia.org/wiki/EtherType). In this case, we will capture IPv4 only frames. The script grabs all the raw information and declare them into variables, useful 
when we need to manipulate or get a specific packet field. This script captures <ins>inbound and outbound frames</ins>, works in Linux only.
```bash
└──╼ $sudo python3 frame_sniffer.py 
SourceMAC:08:00:27:xx:xx:xx  DestinationMAC:e4:8d:8c:xx:xx:xx  Protocol:8
Version:4  Protocol:TCP(6)  DSCP:0  ID:23257  Offset:0x4000  TTL:64
TotalLength:412  IPHeadLength:20  Checksum:0xcfdc  TCPHeadLength:32  Checksum:0x1035
SrcAddress:192.168.XX.XX  SrcPort:36880  DstAddress:23.239.29.5  DstPort:80
SeqNum:54073446  AckNum:2448585548  Flags:PSH+ACK  WindowSize:501  Pointer:0
Data: 360
GET / HTTP/1.1
Host: openspeedtest.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate
-------------------------------------------------------------------------------------
SourceMAC:e4:8d:8c:xx:xx:xx  DestinationMAC:08:00:27:xx:xx:xx  Protocol:8
Version:4  Protocol:TCP(6)  DSCP:0  ID:52906  Offset:0x4000  TTL:51
TotalLength:52  IPHeadLength:20  Checksum:0x6a73  TCPHeadLength:32  Checksum:0x5d9c
SrcAddress:23.239.29.5  SrcPort:80  DstAddress:192.168.XX.XX  DstPort:36880
SeqNum:2448585548  AckNum:54073806  Flags:ACK  WindowSize:505  Pointer:0
Data: 0
-------------------------------------------------------------------------------------
```

## [packet_sniffer.py](https://github.com/stevenvegar/CTF-Tools/blob/main/NahamCon22/ContemporaneousOpen/packet_sniffer.py)
This script is similar to the above, but this captures only TCP <ins>inbound packets</ins> and doesn't shows link layer info.
```bash
└──╼ $sudo python3 packet_sniffer.py 
Version:4  Protocol:TCP(6)  DSCP:0  ID:26910  Offset:0x4000  TTL:41
TotalLength:52  IPHeadLength:20  Checksum:0x3ccf  TCPHeadLength:32  Checksum:0xb1b
SrcAddress:188.184.21.108  SrcPort:80  DstAddress:192.168.XX.XX  DstPort:49200
SeqNum:3925070653  AckNum:385774714  Flags:ACK  WindowSize:235  Pointer:0
Data: 0
-------------------------------------------------------------------------------------
Version:4  Protocol:TCP(6)  DSCP:0  ID:26911  Offset:0x4000  TTL:41
TotalLength:930  IPHeadLength:20  Checksum:0x3960  TCPHeadLength:32  Checksum:0x8f91
SrcAddress:188.184.21.108  SrcPort:80  DstAddress:192.168.XX.XX  DstPort:49200
SeqNum:3925070653  AckNum:385774714  Flags:PSH+ACK  WindowSize:235  Pointer:0
Data: 878
HTTP/1.1 200 OK
Date: Fri, 06 May 2022 18:54:19 GMT
Server: Apache
Last-Modified: Wed, 05 Feb 2014 16:00:31 GMT
Content-Length: 646
Content-Type: text/html

<html><head></head><body><header>
```

### TODO:
- Add support to capture other IP packet types (UDP, ICMP, etc).
- Add filters specifing them with parameters.
- Save output to pcap file.


## Solving the challenge
First, as the server is requesting our IP address, this should be a public IP address and we need to receive it requests directly to our machine so,
we need to do a NAT port forwarding on our ISP and home's router. All packets with the destination port = 80 received at our IP public address should be
redirected to out home's router and it should redirect it again to out machine within the local network. This is a little networking basics.

chall-server -> our public address -> ISP router -> home's router -> out attacking machine

Then, let's try to capture the packets sent by the challenge server using the frame_sniffer.py script and analyze them. Also, let's put a filter in our frame_sniffer.py to visualize only the packets with src_port or dst_port = 80. Also, remember to rename this script to TCPSimultaneousOpen.py to avoid re-write the original code.

```python
#before the script prints the packet info, add an "if" condition
....
        if source_port == 80 or dest_port == 80:
            #prints all the info
            print ('SourceMAC:' + eth_addr(raw_frame[6:12]) + '  DestinationMAC:' + eth_addr(raw_frame[0:6]) + '  Protocol:' + str(eth_proto))
            print ('Version:' + str(IP_ver) + '  Protocol:' + str(proto) + '  DSCP:' + str(tos) + '  ID:' + str(pid) + '  Offset:' + str(hex(offset)) + '  TTL:' + str(ttl))
....
```

```bash
└──╼ $sudo python3 TCPSimultaneousOpen.py 
SourceMAC:e4:8d:8c:xx:xx:xx  DestinationMAC:08:00:27:xx:xx:xx  Protocol:8
Version:4  Protocol:TCP(6)  DSCP:0  ID:43085  Offset:0x4000  TTL:56
TotalLength:60  IPHeadLength:20  Checksum:0x4324  TCPHeadLength:40  Checksum:0xc263
SrcAddress:34.121.91.31  SrcPort:50746  DstAddress:192.168.XX.XX  DstPort:80
SeqNum:513852226  AckNum:0  Flags:SYN  WindowSize:42600  Pointer:0
Data: 0
-------------------------------------------------------------------------------------
SourceMAC:08:00:27:xx:xx:xx  DestinationMAC:e4:8d:8c:xx:xx:xx  Protocol:8
Version:4  Protocol:TCP(6)  DSCP:0  ID:0  Offset:0x4000  TTL:64
TotalLength:40  IPHeadLength:20  Checksum:0xe385  TCPHeadLength:20  Checksum:0xb017
SrcAddress:192.168.XX.XX  SrcPort:80  DstAddress:34.121.91.31  DstPort:50746
SeqNum:0  AckNum:513852227  Flags:RST+ACK  WindowSize:0  Pointer:0
Data: 0
-------------------------------------------------------------------------------------
```

As we can see, the challenge server sends a SYN packet and our machine responds to it with a RST+ACK packet because it doesn't expect to receive a connection over HTTP. Following the "TCP Simultaneous Open" procedure, we need to send to the server a SYN packet equal to the one received and another packet with the ACK flag to acknowledge the first SYN sent by the server. Remember that the server will not receive SYN+ACK packets, instead, we will send a simple ACK packet to tell the server we are ready to connect.

In order to connect with the server we need to create the following packets:
- SYN packet:
   - srce IP : our machine's IP
   - dest IP : server's IP (taken from the server's SYN source IP)
   - srce port : 80
   - dest port : server's source port (taken from the server's SYN source port)
   - seq num : 0
   - TCP flags : SYN

- ACK packet:
   - pack id :  server's SYN packet id + 1
   - srce IP : our machine's IP
   - dest IP : server's IP (taken from the server's SYN source IP)
   - srce port : 80
   - dest port : server's source port (taken from the server's SYN source port)
   - seq num : server's SYN packet ack num + 1
   - ack num : server's SYN packet seq num + 1
   - TCP flags : ACK

I know, it's a little confusing, but it makes stronger our knowlegde in how TCP works and our packet-level understanding.

Next step is to get rid of the RST+ACK packet sent by our machine. This can be done with the help of iptables included in our machine or with a external firewall in our local network. The easiest way is to set a new iptables rule to stop (drop) RST packets get out from our machine, we can achieve it with the following command:
```bash
sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST --sport 80 -j DROP
```
(thanks to [yetanotherf0rked](https://github.com/yetanotherf0rked) for this command in his writeup)

Now, let's create the syntax for our packets and make a new filter to send them only when it's the correct moment. To do this, we have to use Scapy framework to craft our special packets so, we will modify the following lines in the TCPSimultaneousOpen.py script:
```python
#after the info is printed out from the last modification, add another "if" condition
....
                print ("Data Hex: " + str(data_size) + "\n" + data.hex())

            if dest_port == 80 and tcp_flags(flags) == "SYN":
                send_SYN_packet(s_addr,source_port)
                send_ACK_packet(s_addr,pid,ttl,source_port,seqnum,acknum)

            print ("\n" + ("-" * 85) + "\n")
....
```
```python
#at the beginning of the script, import scapy framework and declare the functions
from scapy.all import *
def send_SYN_packet(s_addr,source_port):
    print ("Sending SYN packet")
    craftsyn = IP(len=40, ttl=64, src="192.168.XX.XX", dst=s_addr)/TCP(sport=80, dport=source_port, seq=0, flags="S")
    send(craftsyn)
    print ("Custom SYN sended!")

def send_ACK_packet(s_addr,pid,ttl,source_port,seqnum,acknum):
    print ("Sending ACK packet")
    craftack = IP(len=40, id=pid+1, ttl=ttl, src="192.168.XX.XX", dst=s_addr)/TCP(sport=80, dport=source_port, seq=acknum+1, ack=seqnum+1, flags="A")
    send(craftack)
    print ("Custom ACK sended!")
```

Alright, we've got everything we need set up. Let's trigger the script and request the flag!!!

```bash
└──╼ $nc challenge.nahamcon.com 32062
so glad you're here! i would love to give you the flag. just give me the IP address that's running an HTTP server, and I'll shoot you the flag immediately.
oh one snag, we've got some firewall issues on our side, and some important packets are getting dropped. shouldn't be a problem for you, though.
>>> 201.202.XXX.XXX
here it comes!
hmm nope looks like you didn't get it...
```
```bash
└──╼ $sudo python3 TCPSimultaneousOpen.py 
SourceMAC:e4:8d:8c:xx:xx:xx  DestinationMAC:08:00:27:xx:xx:xx  Protocol:8
Version:4  Protocol:TCP(6)  DSCP:0  ID:24428  Offset:0x4000  TTL:56
TotalLength:60  IPHeadLength:20  Checksum:0x8c05  TCPHeadLength:40  Checksum:0x1afa
SrcAddress:34.121.91.31  SrcPort:44916  DstAddress:192.168.XX.XX  DstPort:80
SeqNum:422867056  AckNum:0  Flags:SYN  WindowSize:42600  Pointer:0
Data: 0

Sending SYN packet
.
Sent 1 packets.
Custom SYN sended!
Sending ACK packet
.
Sent 1 packets.
Custom ACK sended!
------------------------------------------------------------------------------------- ↑ the first SYN packet sent by the server, and our two crafted packets sent
SourceMAC:08:00:27:xx:xx:xx  DestinationMAC:e4:8d:8c:xx:xx:xx  Protocol:8
Version:4  Protocol:TCP(6)  DSCP:0  ID:1  Offset:0x0  TTL:64
TotalLength:40  IPHeadLength:20  Checksum:0x2385  TCPHeadLength:20  Checksum:0x88d3
SrcAddress:192.168.XX.XX  SrcPort:80  DstAddress:34.121.91.31  DstPort:44916
SeqNum:0  AckNum:0  Flags:SYN  WindowSize:8192  Pointer:0
Data: 0
------------------------------------------------------------------------------------- ↑ our SYN sent to the server with the dst port same as src port of first packet 
SourceMAC:08:00:27:xx:xx:xx  DestinationMAC:e4:8d:8c:xx:xx:xx  Protocol:8
Version:4  Protocol:TCP(6)  DSCP:0  ID:24429  Offset:0x0  TTL:56
TotalLength:40  IPHeadLength:20  Checksum:0xcc18  TCPHeadLength:20  Checksum:0xff1e
SrcAddress:192.168.XX.XX  SrcPort:80  DstAddress:34.121.91.31  DstPort:44916
SeqNum:1  AckNum:422867057  Flags:ACK  WindowSize:8192  Pointer:0
Data: 0
------------------------------------------------------------------------------------- ↑ our ACK sent to the server with all modification to respond to the first packet
SourceMAC:e4:8d:8c:xx:xx:xx  DestinationMAC:08:00:27:xx:xx:xx  Protocol:8
Version:4  Protocol:TCP(6)  DSCP:0  ID:24429  Offset:0x4000  TTL:56
TotalLength:60  IPHeadLength:20  Checksum:0x8c04  TCPHeadLength:40  Checksum:0x1a30
SrcAddress:34.121.91.31  SrcPort:44916  DstAddress:192.168.XX.XX  DstPort:80
SeqNum:422867056  AckNum:1  Flags:SYN+ACK  WindowSize:42600  Pointer:0
Data: 0
------------------------------------------------------------------------------------- ↑ a SYN+ACK from the server responding to our SYN, now, the server is connected to our machine
SourceMAC:e4:8d:8c:xx:xx:xx  DestinationMAC:08:00:27:xx:xx:xx  Protocol:8
Version:4  Protocol:TCP(6)  DSCP:0  ID:24430  Offset:0x4000  TTL:56
TotalLength:256  IPHeadLength:20  Checksum:0x8b3f  TCPHeadLength:20  Checksum:0xb681
SrcAddress:34.121.91.31  SrcPort:44916  DstAddress:192.168.XX.XX  DstPort:80
SeqNum:422867057  AckNum:1  Flags:PSH+ACK  WindowSize:333  Pointer:0
Data: 216
POST / HTTP/1.1
Host: 201.202.XX.XX
User-Agent: python-requests/2.27.1
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
Content-Length: 50
Content-Type: application/x-www-form-urlencoded

flag=flag%7B6acfdfc9369eadfdb9439b0ac3969711%7D%0A

------------------------------------------------------------------------------------- ↑ the POST request sent from the server with the flag !!! =D
```

That was an exciting journey, I learned a lot of new things, improved my Python scripting skills, I didn't know anything about "TCP Simultaneous Open" and finally I have my own packet capture script that will help me in future CTFs.

Thanks to the players who uploaded write-ups right after the CTF finished. Check theirs too:
   - [yetanotherf0rked - Spending spring days crafting packets at NahamCon 2022 (1 of 3)](https://github.com/yetanotherf0rked/ctf-writeups/blob/main/NahamCon2022/Just%20crafting%20packets%20at%20Nahamcon2022%20(1%20of%203).md)
   - [nneonneo - server.py](https://gist.github.com/nneonneo/1b371ac9da8703eda9c3a9b26d61a483)

