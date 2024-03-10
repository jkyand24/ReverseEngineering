#!/usr/bin/env python3
from z3 import *

# solver class
s = Solver()

buf = [BitVec(f"buf_{i}", 8) for i in range(16)]
flag = [0]*16

s.add(buf[0] == ord('F'))
s.add(buf[1] == ord('L'))
s.add(buf[2] == ord('A'))
s.add(buf[3] == ord('G'))
s.add(buf[0]^buf[3] == 1)
s.add(buf[1]^buf[11] == 35)
s.add(buf[1]^buf[2]^buf[14] == 105)
s.add(buf[3]^buf[14]^buf[8] == 79)
s.add(buf[12]^buf[4]^buf[13] == 101)
s.add(buf[5]^buf[9] == 7)
s.add(buf[13]^buf[6] == 9)
s.add(buf[2]^(buf[7]^buf[15]) == 80)
s.add(buf[1]^buf[8] == 32)
s.add(buf[2]^(buf[12]^buf[9]) == 92)
s.add(buf[3]^(buf[14]^buf[10]) == 84)
s.add(buf[11]^buf[5] == 7)
s.add(buf[14]^(buf[13]^buf[10]) == 127)
s.add(buf[5]^buf[15] == 21)

if s.check() != sat:
    exit("[!] ERR")


m = s.model()
for i in range(16):
    flag[i] = m[buf[i]].as_long()

print("".join(map(chr, flag)))