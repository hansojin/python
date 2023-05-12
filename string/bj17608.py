#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
block=[]
for _ in range(n):
    block.append(int(input()))
cnt=1
last=block[-1]
for num in block[::-1]:
    if num>last:
        last=num
        cnt+=1
print(cnt)
