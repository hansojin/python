#!/usr/bin/env python

import sys
input= sys.stdin.readline
li=[]
for i in range(0,32):
    li.append(2**i)
for _ in range(int(input())):
    if int(input()) in li:
        print(1)
    else:
        print(0)
