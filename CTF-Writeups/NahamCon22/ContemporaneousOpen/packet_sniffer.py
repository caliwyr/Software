#Packet sniffer in python for Linux, not working on Windows
#Run with sudo
#Sniffs only incoming TCP packet
#Struct CTypes: https://docs.python.org/3/library/struct.html

import socket, sys
from struct import *

#Create a raw socket
try:
    #TCP packets = socket.IPPROTO_TCP | UDP packets = socket.IPPROTO_UDP | ICMP packets = socket.IPPROTO_ICMP
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error as msg:
    print ("Socket could not be created. Error Code : " + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

#TCP flags parser
def tcp_flags(flags):
    tcp_flags = str(f"{flags:08b}")
    str_flags = ""
    if tcp_flags[-1] == "1":
        str_flags += "FIN"
    if tcp_flags[-2] == "1":
        str_flags += "+SIN"
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


#Capturing loop
while True:
    #packet data from tuple
    packet = s.recvfrom(65565)[0]
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
    tcp_header = unpack('!HHLLBBHHH', packet[ip_header_length:ip_header_length+20])
    
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
    
    #prints all the info
    print ('Version:' + str(IP_ver) + '  Protocol:' + str(proto) + '  DSCP:' + str(tos) + '  ID:' + str(pid) + '  Offset:' + str(hex(offset)) + '  TTL:' + str(ttl))
    print ('TotalLength:' + str(plen) + '  IPHeadLength:' + str(ip_header_length)  + '  Checksum:' + str(hex(ipsum)) + '  TCPHeadLength:' + str(tcp_header_length) + '  Checksum:' + str(hex(tcpsum)))
    print ('SrcAddress:' + str(s_addr) + '  SrcPort:' + str(source_port) + '  DstAddress:' + str(d_addr) + '  DstPort:' + str(dest_port))
    print ('SeqNum:' + str(seqnum) + '  AckNum:' + str(acknum) + '  Flags:' + tcp_flags(flags) + '  WindowSize:' + str(window) +  '  Pointer:' + str(pointer))
    try:
        print ("Data: " + str(data_size) + "\n" + data.decode('utf-8'))
    except UnicodeDecodeError as e:
        print ("Data Hex: " + str(data_size) + "\n" + data.hex())

    print ("\n" + ("-" * 85) + "\n")
