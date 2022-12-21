#Packet sniffer in python for Linux, not working on Windows
#Run with sudo
#Sniffs only incoming TCP packet
#Struct CTypes: https://docs.python.org/3/library/struct.html

import socket, sys, time
from struct import *
from scapy.all import *

#Create a raw socket
try:
    #TCP packets = socket.IPPROTO_TCP | UDP packets = socket.IPPROTO_UDP | ICMP packets = socket.IPPROTO_ICMP
    #s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    s = socket.socket(socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
except socket.error as msg:
    print ("Socket could not be created. Error Code : " + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

#MAC address parser
def eth_addr (a) :
  b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (a[0], a[1], a[2], a[3], a[4], a[5])
  return b

#TCP flags parser
def tcp_flags(flags):
    tcp_flags = str(f"{flags:08b}")
    str_flags = ""
    if tcp_flags[-1] == "1":
        str_flags += "FIN"
    if tcp_flags[-2] == "1":
        str_flags += "+SYN"
    if tcp_flags[-3] == "1":
        str_flags += "+RST"
    if tcp_flags[-4] == "1":
        str_flags += "+PSH"
    if tcp_flags[-5] == "1":
        str_flags += "+ACK"
    if tcp_flags[-6] == "1":
        str_flags += "+URG"
    if tcp_flags[-7] == "1":
        str_flags += "+ECE"
    if tcp_flags[-8] == "1":
        str_flags += "+CWR"

    if str_flags[0] == "+":
        return str_flags.lstrip("+")
    return str_flags

#crafting SYN packet
def send_SYN_packet(s_addr,source_port):
    print ("Sending SYN packet")
    craftsyn = IP(len=40, ttl=64, src="192.168.25.10", dst=s_addr)/TCP(sport=80, dport=source_port, seq=0, flags="S")
    send(craftsyn)
    print ("Custom SYN sended!")
#crafting ACK packet
def send_ACK_packet(s_addr,pid,ttl,source_port,seqnum,acknum):
    print ("Sending ACK packet")
    craftack = IP(len=40, id=pid+1, ttl=ttl, src="192.168.25.10", dst=s_addr)/TCP(sport=80, dport=source_port, seq=acknum+1, ack=seqnum+1, flags="A")
    send(craftack)
    print ("Custom ACK sended!")

#Capturing loop
while True:
    #capture ethernet frame string from tuple
    raw_frame = s.recvfrom(65565)[0]

    #parse ethernet header
    eth_header = raw_frame[0:14]
    eth = unpack('!6s6sH' , eth_header)
    eth_proto = socket.ntohs(eth[2])
 
    #capture IP packet
    if eth_proto == 8:
        packet = raw_frame[14:]
        #take first 20 characters for the IP header and now unpack them :)
        ip_header = unpack('!BBHHHBBH4s4s', packet[0:20])
        #IP header information
        IP_ver = ip_header[0] >> 4
        ihl = ip_header[0] & 0xF
        ip_header_length = ihl * 4
        tos = ip_header[1]
        plen = ip_header[2]
        pid = ip_header[3]
        offset = ip_header[4]
        ttl = ip_header[5]

        IPproto = ip_header[6]
        if IPproto == 6:
            proto = "TCP(6)"
        elif IPproto == 17:
            proto = "UDP(17)"
        elif IPproto == 1:
            proto = "ICMP(1)"
        else:
            proto = "NoReg " + str(IPproto)
        ipsum = ip_header[7]
        s_addr = socket.inet_ntoa(ip_header[8]);
        d_addr = socket.inet_ntoa(ip_header[9]);
    

        #unpack from IP header to TCP header length
        tcp_header = unpack('!HHLLBBHHH', packet[ip_header_length:ip_header_length + 20])
    
        #TCP Header information
        source_port = tcp_header[0]
        dest_port = tcp_header[1]
        seqnum = tcp_header[2]
        acknum = tcp_header[3]
        tcp_header_length = (tcp_header[4] >> 4) * 4
        flags = tcp_header[5]
        window = tcp_header[6]
        tcpsum = tcp_header[7]
        pointer = tcp_header[8]
    
        #get data and size
        data_size = plen - ip_header_length - tcp_header_length
        data = packet[plen - data_size:]

        #filters only HTTP packets
        if source_port == 80 or dest_port == 80:
            print ('SourceMAC:' + eth_addr(raw_frame[6:12]) + '  DestinationMAC:' + eth_addr(raw_frame[0:6]) + '  Protocol:' + str(eth_proto))
            print ('Version:' + str(IP_ver) + '  Protocol:' + str(proto) + '  DSCP:' + str(tos) + '  ID:' + str(pid) + '  Offset:' + str(hex(offset)) + '  TTL:' + str(ttl))
            print ('TotalLength:' + str(plen) + '  IPHeadLength:' + str(ip_header_length)  + '  Checksum:' + str(hex(ipsum)) + '  TCPHeadLength:' + str(tcp_header_length) + '  Checksum:' + str(hex(tcpsum)))
            print ('SrcAddress:' + str(s_addr) + '  SrcPort:' + str(source_port) + '  DstAddress:' + str(d_addr) + '  DstPort:' + str(dest_port))
            print ('SeqNum:' + str(seqnum) + '  AckNum:' + str(acknum) + '  Flags:' + tcp_flags(flags) + '  WindowSize:' + str(window) +  '  Pointer:' + str(pointer))
            try:
                print ("Data: " + str(data_size) + "\n" + data.decode('utf-8'))
            except UnicodeDecodeError as e:
                print ("Data Hex: " + str(data_size) + "\n" + data.hex())

            #if matches the packet sent by the server, send our packets
            if dest_port == 80 and tcp_flags(flags) == "SYN":
                send_SYN_packet(s_addr,source_port)
                send_ACK_packet(s_addr,pid,ttl,source_port,seqnum,acknum)

            print ("\n" + ("-" * 85) + "\n")
