# TryHackMe-WireShark 101

## Wireshark

Wireshark is a packet analyzing tool which deals with PCAP (Packet Capture Files). It is a software that can capture packets on NIC (Network Interface Card).

### Network Taps 

Network taps are like a physical device that physcial tap between a cable these are used DFIR (Digital Forensics and Incident Response) or Threat Hunting and Red Teams to sniff and capture packets.

There are two ways to tap network 

First is by using hardware to tap the wire and intercept the traffic as it comes across, an example of this would be a vampire tap 

Second is  planting a network tap would be an inline network tap, which you would plant between or 'inline' two network devices. The tap will replicate packets as they pass the tap. An example of this tap would be the very common Throwing Star LAN Tap

### MAC Flood

MAC Floods are a tactic commonly used by red teams as a way of actively sniffing packets. MAC Flooding is intended to stress the switch and fill the CAM table. Once the CAM table is filled the switch will no longer accept new MAC addresses and so in order to keep the network alive, the switch will send out packets to all ports of the switch.

### ARP Posining

ARP Poisoning is another technique used by red teams to actively sniff packets. By ARP Poisoning you can redirect the traffic from the host(s) to the machine you're monitoring from. This technique will not stress network equipment like MAC Flooding however should still be used with caution and only if other techniques like network taps are unavailable.

## Wireshark Filters

```
and - operator: and / &&
or - operator: or / ||
equals - operator: eq / ==
not equal - operator: ne / !=
greater than - operator: gt /  >
less than - operator: lt / <
```

### Filtering Examples

ip.addr == <IP Address>
ip.src == <SRC IP Address> and ip.dst == <DST IP Address> 	
tcp.port eq <Port #> or <Protocol Name>
udp.port eq <Port #> or <Protocol Name>

## Analyzing ARP Packets

<img src="https://imgur.com/hYhfCvm.png"/>

1. What is the Opcode for Packet 6?

`request (1)`

<img src="https://imgur.com/Ky69t8h.png"/>

2. What is the source MAC Address of Packet 19?

`80:fb:06:f0:45:d7`

<img src="https://imgur.com/wJBZEHY.png"/>

From the packet info we can see that it's telling that this IP belongs to this MAC address tso this is a reply packet (opcode 2) in ARP

3. What 4 packets are Reply packets?

`74,400,459,520`

<img src="https://imgur.com/A7kuRnF.png"/>

4. What IP Address is at 80:fb:06:f0:45:d7?

`10.251.23.1`


## ICMP

ICMP stands for Internet Control Message Protocol and is used for uitilties like `ping` , `traceroute` and etc. Ping has two codes for the two things that it does , `request` and `respond`. For request code is `8` and for response code is `0`.


<img src="https://imgur.com/BSg91tr.png"/>

We can see that in packet 4 and 5 ping is used and in packet 4 it's a request so code `8` and in packet 5 is a respond so code `0`.

1. What is the type for packet 4?
`8`

2. What is the type for packet 5?
`0`

<img src="https://imgur.com/MKES7C2.png"/>

We can see the timestamp here which is `May 31, 2013` now this might differ from other timezone it maybe `May 30` or `May 31` for me it was 30 because of differnt timezone

3. What is the timestamp for packet 12, only including month day and year? note: Wireshark bases it’s time off of your devices time zone, if your answer is wrong try one day more or less. 
`May 30, 2013`

<img src="https://imgur.com/oRlxgW3.png"/>

Here to see value of the `data` string , right click , select `copy` then the `value`.

4. What is the full data string for packet 18?
`08090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f3031323334353637`


## DNS

DNS stands for Domain Name Service , it's a protocol that resolves domain names into IP addresses , because routers work on IP addresses and need to understand which IP belongs to which domain so they query it through a DNS a server by defualt public dns server is `8.8.8.8` which is Google's DNS Server.

<img src="https://imgur.com/HKP8mSM.png"/>

1. What is being queried in packet 1?
`8.8.8.8.in-addr.arpa`

<img src="https://imgur.com/Od3OMPu.png"/>

2. What site is being queried in packet 26?

`www.wireshark.org`

<img src="https://imgur.com/NopC8o3.png"/>
3. What is the Transaction ID for packet 26?

`0x2c58`

## HTTP

HTTP stands for Hyper Text Transport Protocol it is used in world wide web `www`to access resource ,wwww is an information system where documents and other web resources are identified by Uniform Resource Locators(URL). HTTP is used by some sites but this isn't secure secure meaning that connection is not encrypted. It is used to send GET and POST request inorder to receive resources.


<img src="https://imgur.com/nKyB094.png"/>

We can see these statistics by navigating `Statistics` > `Protocol Hierarchy`.

1. What percent of packets originate from Domain Name System?
`4.7`

<img src="https://imgur.com/6ZI1Fjl.png"/>

We can from the packets that this is the IP which ends on "237".

2. What endpoint ends in .237?
`145.254.160.237`

<img src="https://imgur.com/A2HXVca.png"/>

3. What is the user-agent listed in packet 4?
`Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.6) Gecko/20040113`.

<img src="https://imgur.com/NHwn5Sq.png"/>
4. Looking at the data stream what is the full request URI from packet 18? 

`http://pagead2.googlesyndication.com/pagead/ads?client=ca-pub-2309191948673629&random=1084443430285&lmt=1082467020&format=468x60_as&output=html&url=http%3A%2F%2Fwww.ethereal.com%2Fdownload.html&color_bg=FFFFFF&color_text=333333&color_link=000000&color_url=666633&color_border=666633`


<img src="https://imgur.com/flJ3ACC.png"/>

5. What domain name was requested from packet 38?

`www.ethereal.com`

<img src="https://imgur.com/xzSU1a7.png"/>

6. Looking at the data stream what is the full request URI from packet 38?

`http://www.ethereal.com/download.html`.


## HTTPS 

HTTPS stands for Hyper Text Transfer Protocol Secure , it's the same as HTTP but the only difference is that the connection will be encrypted with the websites

```
Client and server agree on a protocol version
Client and server select a cryptographic algorithm
The client and server can authenticate to each other; this step is optional
Creates a secure tunnel with a public key
```

<img src="https://imgur.com/zUa2ruy.png"/>

1. Looking at the data stream what is the full request URI for packet 31?
`https://localhost/icons/apache_pb.png`


<img src="https://imgur.com/AGUN6XU.png"/>

2. Looking at the data stream was is the full request URI for packet 50?
`https://localhost/icons/back.gif`.

3. What is the User-Agent listed in packet 50?
`Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.0.2) Gecko/20060308 Firefox/1.5.0.2`
